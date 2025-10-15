// Clarion Knowledge Base - RAG Search Application

// State management
const state = {
    isSearching: false,
    lastQuery: '',
    currentResults: [],
    currentProvider: 'deepseek',
    currentModel: 'deepseek-chat',
    providerConfigured: false,
    availableProviders: []
};

// DOM Elements
const searchInput = document.getElementById('searchInput');
const askAIButton = document.getElementById('askAIButton');
const docTypeFilter = document.getElementById('docTypeFilter');
const maxResults = document.getElementById('maxResults');
const minScore = document.getElementById('minScore');
const loadingIndicator = document.getElementById('loadingIndicator');
const errorMessage = document.getElementById('errorMessage');
const resultsContainer = document.getElementById('results');

// LLM Configuration DOM Elements
const providerSelect = document.getElementById('providerSelect');
const modelSelect = document.getElementById('modelSelect');
const apiKeyInput = document.getElementById('apiKeyInput');
const saveApiKeyButton = document.getElementById('saveApiKeyButton');
const statusIndicator = document.getElementById('statusIndicator');
const apiKeyRow = document.getElementById('apiKeyRow');

// API Configuration
const API_BASE_URL = 'http://localhost:8080';

// Initialize application
async function init() {
    setupEventListeners();
    await loadProviders();
    loadSavedSettings();
    focusSearchInput();
}

// Load saved settings from localStorage
function loadSavedSettings() {
    try {
        const savedSettings = localStorage.getItem('clarionKbSettings');
        if (savedSettings) {
            const settings = JSON.parse(savedSettings);

            // Restore provider selection
            if (settings.provider && providerSelect) {
                providerSelect.value = settings.provider;
                state.currentProvider = settings.provider;

                // Update models dropdown for this provider
                updateModelsDropdown(settings.provider);
            }

            // Restore model selection (after models dropdown is populated)
            if (settings.model && modelSelect) {
                modelSelect.value = settings.model;
                state.currentModel = settings.model;
            }

            // Check if provider is configured (API key was saved)
            if (settings.isConfigured) {
                // Auto-check connection
                checkProviderConnection();
            }

            // Show masked API key hint if it was saved
            if (settings.apiKeyHint) {
                apiKeyInput.placeholder = `Saved: ${settings.apiKeyHint}`;
            }

            // Show/hide API key input based on provider
            const provider = state.availableProviders.find(p => p.id === settings.provider);
            if (provider) {
                if (provider.requires_api_key) {
                    apiKeyRow.style.display = 'flex';
                } else {
                    apiKeyRow.style.display = 'none';
                }
            }

            console.log('Settings loaded from localStorage');
        }
    } catch (error) {
        console.error('Error loading saved settings:', error);
    }
}

// Save settings to localStorage
function saveSettings(provider, model, isConfigured, apiKeyHint) {
    try {
        const settings = {
            provider: provider,
            model: model,
            isConfigured: isConfigured,
            apiKeyHint: apiKeyHint || null
        };
        localStorage.setItem('clarionKbSettings', JSON.stringify(settings));
        console.log('Settings saved to localStorage');
    } catch (error) {
        console.error('Error saving settings:', error);
    }
}

// Check if provider is already configured
async function checkProviderConnection() {
    try {
        // Load providers to check actual configuration status from backend
        const response = await fetch(`${API_BASE_URL}/api/providers`);
        if (response.ok) {
            const data = await response.json();
            const currentProvider = data.providers.find(p => p.id === state.currentProvider);

            if (currentProvider && currentProvider.configured) {
                // Backend confirms API key is configured
                updateStatusIndicator(true, `Connected to ${currentProvider.name}`);
                state.providerConfigured = true;
                console.log('Provider connected:', currentProvider.name);
            } else {
                // Backend says not configured, clear the saved flag
                updateStatusIndicator(false, currentProvider && currentProvider.requires_api_key ?
                    'API key required' : 'Not configured');
                state.providerConfigured = false;

                // Clear the isConfigured flag from localStorage
                const savedSettings = localStorage.getItem('clarionKbSettings');
                if (savedSettings) {
                    const settings = JSON.parse(savedSettings);
                    settings.isConfigured = false;
                    localStorage.setItem('clarionKbSettings', JSON.stringify(settings));
                }
                console.log('Provider not configured on backend');
            }
        }
    } catch (error) {
        console.log('Error checking provider connection:', error);
        updateStatusIndicator(false, 'Connection check failed');
        state.providerConfigured = false;
    }
}

// Mask API key for display (show first 6 chars + ***)
function maskApiKey(apiKey) {
    if (!apiKey || apiKey.length < 10) return '***';
    return apiKey.substring(0, 6) + '***' + apiKey.substring(apiKey.length - 4);
}

// Setup event listeners
function setupEventListeners() {
    // Ask AI button
    askAIButton.addEventListener('click', handleAskAI);

    searchInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            // Enter without Shift: Submit query
            e.preventDefault(); // Prevent new line
            handleAskAI();
        }
        // Shift+Enter: Allow default behavior (new line in textarea)
    });

    // LLM Configuration listeners
    providerSelect.addEventListener('change', handleProviderChange);
    modelSelect.addEventListener('change', handleModelChange);
    saveApiKeyButton.addEventListener('click', handleSaveApiKey);

    // Auto-clear error on input change
    searchInput.addEventListener('input', () => {
        hideError();
    });
}

// Focus search input on page load
function focusSearchInput() {
    searchInput.focus();
}


// API: Load providers
async function loadProviders() {
    try {
        const response = await fetch(`${API_BASE_URL}/api/providers`);

        if (!response.ok) {
            console.error('Failed to load providers');
            return;
        }

        const data = await response.json();
        state.availableProviders = data.providers || [];

        // Update provider select with price ranges
        providerSelect.innerHTML = '';
        data.providers.forEach(provider => {
            const option = document.createElement('option');
            option.value = provider.id;
            // Display price range instead of average cost
            const costInfo = provider.requires_api_key ?
                ` (${provider.price_range})` :
                ' (FREE)';
            option.textContent = `${provider.name}${costInfo}`;
            providerSelect.appendChild(option);
        });

        // Check if any provider is configured
        const configured = data.providers.find(p => p.configured);
        if (configured) {
            state.providerConfigured = true;
            state.currentProvider = configured.id;
            providerSelect.value = configured.id;
            updateStatusIndicator(true, `Connected to ${configured.name}`);
            updateModelsDropdown(configured.id);
        }

        // Handle provider change to update models
        if (providerSelect.value) {
            handleProviderChange();
        }
    } catch (error) {
        console.error('Error loading providers:', error);
    }
}

// Handle provider selection change
function handleProviderChange() {
    const providerId = providerSelect.value;
    state.currentProvider = providerId;

    // Find provider info
    const provider = state.availableProviders.find(p => p.id === providerId);

    if (provider) {
        // Update models dropdown
        updateModelsDropdown(providerId);

        // Show/hide API key input
        if (provider.requires_api_key) {
            apiKeyRow.style.display = 'flex';
        } else {
            apiKeyRow.style.display = 'none';
        }

        // Update status based on backend configuration
        if (provider.configured) {
            updateStatusIndicator(true, `Connected to ${provider.name}`);
            state.providerConfigured = true;
        } else {
            updateStatusIndicator(false, provider.requires_api_key ?
                'API key required' : 'Not configured');
            state.providerConfigured = false;
        }

        // Save provider selection to localStorage
        const savedSettings = localStorage.getItem('clarionKbSettings');
        const settings = savedSettings ? JSON.parse(savedSettings) : {};
        // Save isConfigured based on actual backend state, not saved state
        saveSettings(providerId, state.currentModel, provider.configured || false, settings.apiKeyHint || null);
    }
}

// Update models dropdown with per-model pricing
function updateModelsDropdown(providerId) {
    const provider = state.availableProviders.find(p => p.id === providerId);

    if (provider && provider.models) {
        modelSelect.innerHTML = '';
        provider.models.forEach(model => {
            const option = document.createElement('option');
            // Handle both old (string) and new (object) formats for backwards compatibility
            const modelName = typeof model === 'string' ? model : model.name;
            const avgCost = typeof model === 'object' && model.avg_cost_per_1m !== undefined ? model.avg_cost_per_1m : null;

            option.value = modelName;

            // Display pricing info if available
            if (avgCost !== null) {
                const costDisplay = avgCost === 0 ? 'FREE' : `$${avgCost.toFixed(2)}/1M avg`;
                option.textContent = `${modelName} (${costDisplay})`;
            } else {
                option.textContent = modelName;
            }

            modelSelect.appendChild(option);
        });

        // Set current model to first model's name
        state.currentModel = typeof provider.models[0] === 'string' ?
            provider.models[0] :
            provider.models[0].name;
    }
}

// Handle model selection change
function handleModelChange() {
    state.currentModel = modelSelect.value;

    // Save model selection to localStorage
    const savedSettings = localStorage.getItem('clarionKbSettings');
    const settings = savedSettings ? JSON.parse(savedSettings) : {};
    saveSettings(state.currentProvider, modelSelect.value, settings.isConfigured || false, settings.apiKeyHint || null);
}

// Handle save API key
async function handleSaveApiKey() {
    const apiKey = apiKeyInput.value.trim();

    if (!apiKey) {
        showError('Please enter an API key');
        return;
    }

    try {
        saveApiKeyButton.disabled = true;
        saveApiKeyButton.textContent = 'Saving...';

        await configureProvider(state.currentProvider, apiKey);

        // Save to localStorage with masked key hint
        const maskedKey = maskApiKey(apiKey);
        saveSettings(state.currentProvider, state.currentModel, true, maskedKey);

        // Clear input and show masked key
        apiKeyInput.value = '';
        apiKeyInput.placeholder = `Saved: ${maskedKey}`;

        // Update status
        const provider = state.availableProviders.find(p => p.id === state.currentProvider);
        updateStatusIndicator(true, `Connected to ${provider ? provider.name : state.currentProvider}`);
        state.providerConfigured = true;

        showSuccess('API key saved successfully!');
    } catch (error) {
        console.error('Error saving API key:', error);
        showError(error.message || 'Failed to save API key');
    } finally {
        saveApiKeyButton.disabled = false;
        saveApiKeyButton.textContent = 'Save';
    }
}

// API: Configure provider
async function configureProvider(provider, apiKey) {
    const response = await fetch(`${API_BASE_URL}/api/configure`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            provider: provider,
            api_key: apiKey
        })
    });

    if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.error || 'Failed to configure provider');
    }

    return await response.json();
}

// Update status indicator
function updateStatusIndicator(configured, message) {
    if (configured) {
        statusIndicator.className = 'status-indicator configured';
        statusIndicator.innerHTML = `<span class="status-text">✓ ${message}</span>`;
    } else {
        statusIndicator.className = 'status-indicator not-configured';
        statusIndicator.innerHTML = `<span class="status-text">⚠ ${message}</span>`;
    }
}

// Handle Ask AI (RAG Query)
async function handleAskAI() {
    const query = searchInput.value.trim();

    if (!query) {
        showError('Please enter a question');
        return;
    }

    if (!state.providerConfigured) {
        showError('Please configure an LLM provider first');
        return;
    }

    if (state.isSearching) {
        return;
    }

    try {
        state.isSearching = true;
        state.lastQuery = query;

        // Update UI
        showLoading('Asking AI...');
        hideError();
        clearResults();
        disableSearch();

        // Build query parameters
        const queryMode = document.getElementById('queryMode');

        const params = {
            query: query,
            mode: queryMode.value,
            max_results: parseInt(maxResults.value),
            min_score: parseFloat(minScore.value),
            llm_provider: state.currentProvider,
            llm_model: state.currentModel
        };

        // Add doc_type filter if selected
        const docType = docTypeFilter.value;
        if (docType) {
            params.doc_type = docType;
        }

        // Make API request
        const response = await queryRAG(params);

        // Display RAG response
        displayRAGResponse(response, query);

    } catch (error) {
        console.error('RAG query error:', error);
        showError(error.message || 'An error occurred while querying the AI. Please try again.');
    } finally {
        state.isSearching = false;
        hideLoading();
        enableSearch();
    }
}

// API: Query RAG
async function queryRAG(params) {
    // Create AbortController for 5-minute timeout (matches backend)
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 300000); // 5 minutes

    try {
        const response = await fetch(`${API_BASE_URL}/api/query`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(params),
            signal: controller.signal
        });

        clearTimeout(timeoutId);

        if (!response.ok) {
            const errorData = await response.json().catch(() => ({}));
            throw new Error(errorData.detail || errorData.error || `HTTP error! status: ${response.status}`);
        }

        return await response.json();
    } catch (error) {
        clearTimeout(timeoutId);
        if (error.name === 'AbortError') {
            throw new Error('Query timed out after 5 minutes. Try using "Chat" mode (faster, no doc search) or ask a more specific question.');
        }
        throw error;
    }
}

// Display RAG response
function displayRAGResponse(response, query) {
    // Create answer card
    const answerCard = createAnswerCard(response, query);
    resultsContainer.appendChild(answerCard);

    // Create sources section (collapsible)
    if (response.chunks && response.chunks.length > 0) {
        const sourcesSection = createSourcesSection(response.chunks);
        resultsContainer.appendChild(sourcesSection);
    }

    // Add fade-in animation
    resultsContainer.classList.add('fade-in');
}

// Create answer card
function createAnswerCard(response, query) {
    const card = document.createElement('div');
    card.className = 'answer-card';

    const metadata = response.metadata || {};
    const formattedAnswer = formatContent(response.answer);

    card.innerHTML = `
        <h3>AI Answer</h3>
        <div class="answer-text">
            ${formattedAnswer}
        </div>
        <div class="answer-metadata">
            <div class="metadata-item">
                <span>🎯</span>
                <strong>Mode:</strong> ${formatModeName(metadata.query_mode || 'augmented')}
            </div>
            <div class="metadata-item">
                <span>⚡</span>
                <span>${metadata.response_time_ms || 0}ms</span>
            </div>
            <div class="metadata-item">
                <span>🔢</span>
                <span>${metadata.tokens_used || 0} tokens</span>
            </div>
            <div class="metadata-item">
                <span>💰</span>
                <span>$${(metadata.cost_estimate || 0).toFixed(5)}</span>
            </div>
            <div class="metadata-item">
                <span>🤖</span>
                <span>${escapeHtml(metadata.model_used || state.currentModel)}</span>
            </div>
            <div class="metadata-item">
                <span>📄</span>
                <span>${metadata.chunks_retrieved || 0} sources</span>
            </div>
        </div>
    `;

    // Add copy buttons to code blocks
    addCopyButtons(card);

    return card;
}

// Create sources section (collapsible)
function createSourcesSection(chunks) {
    const section = document.createElement('div');
    section.className = 'sources-section';

    const headerId = 'sources-header-' + Date.now();
    const contentId = 'sources-content-' + Date.now();

    section.innerHTML = `
        <div class="sources-header" id="${headerId}">
            <h3>Source Documentation (${chunks.length} chunks)</h3>
            <span class="toggle-icon">▼</span>
        </div>
        <div class="sources-content" id="${contentId}">
        </div>
    `;

    // Add chunks to content
    const sourcesContent = section.querySelector('.sources-content');
    chunks.forEach((chunk, index) => {
        const chunkCard = createChunkCard(chunk, index);
        sourcesContent.appendChild(chunkCard);
    });

    // Add toggle functionality
    const header = section.querySelector('.sources-header');
    const content = section.querySelector('.sources-content');
    const toggleIcon = section.querySelector('.toggle-icon');

    header.addEventListener('click', () => {
        content.classList.toggle('collapsed');
        toggleIcon.textContent = content.classList.contains('collapsed') ? '▶' : '▼';
    });

    return section;
}

// Create chunk card (similar to result card but smaller)
function createChunkCard(chunk, index) {
    const card = document.createElement('div');
    card.className = 'result-card chunk-card';

    const scorePercent = Math.round(chunk.score * 100);
    const docType = formatDocType(chunk.doc_type);
    const formattedContent = formatContent(chunk.text);

    card.innerHTML = `
        <div class="result-header">
            <div class="result-meta">
                <div class="result-source">
                    Source: ${escapeHtml(chunk.source)}
                </div>
                <span class="result-doc-type">${docType}</span>
            </div>
            <div class="result-score">
                <span>${scorePercent}%</span>
                <div class="score-bar">
                    <div class="score-fill" style="width: ${scorePercent}%"></div>
                </div>
            </div>
        </div>
        <div class="result-content">
            ${formattedContent}
        </div>
    `;

    // Add copy buttons to code blocks
    addCopyButtons(card);

    return card;
}

// API: Search documentation (existing vector search)
async function searchDocs(params) {
    const response = await fetch(`${API_BASE_URL}/api/search`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(params)
    });

    if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.error || `HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    return data.results || [];
}

// Display search results
function displayResults(results, query) {
    if (!results || results.length === 0) {
        displayNoResults(query);
        return;
    }

    // Create results header
    const header = createResultsHeader(results.length, query);
    resultsContainer.appendChild(header);

    // Create result cards
    results.forEach((result, index) => {
        const card = createResultCard(result, index);
        resultsContainer.appendChild(card);
    });

    // Add fade-in animation
    resultsContainer.classList.add('fade-in');
}

// Create results header
function createResultsHeader(count, query) {
    const header = document.createElement('div');
    header.className = 'results-header';
    header.innerHTML = `
        <h2>Search Results</h2>
        <p class="results-count">
            Found ${count} result${count !== 1 ? 's' : ''} for "${escapeHtml(query)}"
        </p>
    `;
    return header;
}

// Create result card
function createResultCard(result, index) {
    const card = document.createElement('div');
    card.className = 'result-card';

    // Calculate score percentage
    const scorePercent = Math.round(result.score * 100);

    // Format doc type
    const docType = formatDocType(result.doc_type);

    // Format content with basic markdown-like formatting
    const formattedContent = formatContent(result.content);

    card.innerHTML = `
        <div class="result-header">
            <div class="result-meta">
                <div class="result-source">
                    Source: ${escapeHtml(result.source)}
                </div>
                <span class="result-doc-type">${docType}</span>
            </div>
            <div class="result-score">
                <span>${scorePercent}%</span>
                <div class="score-bar">
                    <div class="score-fill" style="width: ${scorePercent}%"></div>
                </div>
            </div>
        </div>
        <div class="result-content">
            ${formattedContent}
        </div>
    `;

    // Add copy buttons to code blocks
    addCopyButtons(card);

    return card;
}

// Format document type
function formatDocType(docType) {
    if (!docType) return 'Unknown';

    const typeMap = {
        'core_language': 'Core Language',
        'libraries': 'Libraries',
        'ide_development': 'IDE & Development',
        'templates': 'Templates',
        'specialized': 'Specialized',
        'advanced': 'Advanced',
        'utilities': 'Utilities'
    };

    return typeMap[docType] || docType.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
}

// Format mode name
function formatModeName(mode) {
    const modeMap = {
        'augmented': 'Augmented (Docs + AI)',
        'strict': 'Strict (Docs Only)',
        'chat': 'Chat (AI Only)'
    };
    return modeMap[mode] || mode;
}

// Format content with markdown rendering
function formatContent(content) {
    if (!content) return '';

    // Configure marked.js options
    if (typeof marked !== 'undefined') {
        marked.setOptions({
            breaks: true,        // Convert \n to <br>
            gfm: true,          // GitHub Flavored Markdown
            headerIds: false,   // Don't add IDs to headers
            mangle: false       // Don't mangle email addresses
        });

        try {
            // Use marked.js to render markdown as HTML
            return marked.parse(content);
        } catch (e) {
            console.error('Markdown rendering error:', e);
            // Fallback to basic formatting
        }
    }

    // Fallback: Basic formatting if marked.js is not available
    let formatted = escapeHtml(content);
    formatted = formatted.replace(/```([\s\S]*?)```/g, '<pre><code>$1</code></pre>');
    formatted = formatted.replace(/`([^`]+)`/g, '<code>$1</code>');
    formatted = formatted.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
    formatted = formatted.replace(/\*([^*]+)\*/g, '<em>$1</em>');
    const paragraphs = formatted.split('\n\n').filter(p => p.trim());
    formatted = paragraphs.map(p => `<p>${p.replace(/\n/g, '<br>')}</p>`).join('');
    return formatted;
}

// Add copy buttons to all code blocks in a container
function addCopyButtons(container) {
    const codeBlocks = container.querySelectorAll('pre');

    codeBlocks.forEach(pre => {
        // Skip if copy button already exists
        if (pre.querySelector('.copy-button')) return;

        // Create copy button
        const copyButton = document.createElement('button');
        copyButton.className = 'copy-button';
        copyButton.innerHTML = `
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
            </svg>
            <span>Copy</span>
        `;

        // Add click handler
        copyButton.addEventListener('click', async () => {
            const code = pre.querySelector('code');
            const text = code ? code.textContent : pre.textContent;

            try {
                await navigator.clipboard.writeText(text);

                // Visual feedback
                copyButton.innerHTML = `
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <polyline points="20 6 9 17 4 12"></polyline>
                    </svg>
                    <span>Copied!</span>
                `;
                copyButton.classList.add('copied');

                // Reset after 2 seconds
                setTimeout(() => {
                    copyButton.innerHTML = `
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                            <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                        </svg>
                        <span>Copy</span>
                    `;
                    copyButton.classList.remove('copied');
                }, 2000);
            } catch (err) {
                console.error('Failed to copy:', err);
                copyButton.innerHTML = `
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <circle cx="12" cy="12" r="10"></circle>
                        <line x1="15" y1="9" x2="9" y2="15"></line>
                        <line x1="9" y1="9" x2="15" y2="15"></line>
                    </svg>
                    <span>Failed</span>
                `;
                setTimeout(() => {
                    copyButton.innerHTML = `
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                            <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                        </svg>
                        <span>Copy</span>
                    `;
                }, 2000);
            }
        });

        // Wrap pre in container and add button
        const wrapper = document.createElement('div');
        wrapper.className = 'code-block-wrapper';
        pre.parentNode.insertBefore(wrapper, pre);
        wrapper.appendChild(pre);
        wrapper.appendChild(copyButton);
    });
}

// Display no results message
function displayNoResults(query) {
    resultsContainer.innerHTML = `
        <div class="no-results">
            <div class="no-results-icon">🔍</div>
            <h3>No Results Found</h3>
            <p>No documentation found for "${escapeHtml(query)}"</p>
            <p style="margin-top: 10px;">Try adjusting your search terms or filters.</p>
        </div>
    `;
}

// UI Helper Functions
function showLoading(message = 'Searching documentation...') {
    loadingIndicator.querySelector('p').textContent = message;
    loadingIndicator.style.display = 'block';
}

function hideLoading() {
    loadingIndicator.style.display = 'none';
}

function showError(message) {
    errorMessage.textContent = message;
    errorMessage.className = 'error';
    errorMessage.style.display = 'block';
}

function showSuccess(message) {
    errorMessage.textContent = message;
    errorMessage.className = 'success';
    errorMessage.style.display = 'block';

    // Auto-hide after 3 seconds
    setTimeout(() => {
        hideError();
    }, 3000);
}

function hideError() {
    errorMessage.style.display = 'none';
}

function clearResults() {
    resultsContainer.innerHTML = '';
    resultsContainer.classList.remove('fade-in');
}

function disableSearch() {
    askAIButton.disabled = true;
    searchInput.disabled = true;
}

function enableSearch() {
    askAIButton.disabled = false;
    searchInput.disabled = false;
}

// Utility function to escape HTML
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// Initialize on DOM ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
} else {
    init();
}

// Export for testing (if needed)
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        searchDocs,
        formatDocType,
        formatContent,
        escapeHtml
    };
}
