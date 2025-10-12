"""
Clarion Knowledge Base MCP Server
Provides semantic search and documentation access via MCP protocol
"""

import asyncio
import logging
from typing import Any, Dict, List, Optional
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Resource, Tool, TextContent, ImageContent, EmbeddedResource
import mcp.types as types

from vector_store import ClarionVectorStore
from embeddings import EmbeddingModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ClarionMCPServer:
    """
    MCP Server for Clarion documentation access.
    Provides tools for semantic search and resource browsing.
    """

    def __init__(self):
        """Initialize the MCP server with vector store and embedding model."""
        self.server = Server("clarion-knowledge-base")
        self.vector_store = ClarionVectorStore()
        self.embedding_model = None  # Lazy load to avoid startup delay

        # Setup handlers
        self._setup_handlers()

        logger.info("Clarion MCP Server initialized")

    def _get_embedding_model(self) -> EmbeddingModel:
        """Lazy load the embedding model."""
        if self.embedding_model is None:
            logger.info("Loading embedding model...")
            self.embedding_model = EmbeddingModel()
        return self.embedding_model

    def _setup_handlers(self):
        """Setup MCP protocol handlers."""

        @self.server.list_resources()
        async def list_resources() -> List[Resource]:
            """
            List available Clarion documentation resources.
            """
            logger.info("Received list_resources request")

            # Get collection info
            try:
                info = self.vector_store.get_collection_info()
                points_count = info.get('points_count', 0)
            except:
                points_count = 0

            resources = [
                Resource(
                    uri="clarion://docs/all",
                    name="All Clarion Documentation",
                    description=f"Complete Clarion documentation ({points_count} chunks indexed)",
                    mimeType="text/markdown"
                ),
                Resource(
                    uri="clarion://docs/core_language",
                    name="Core Language Documentation",
                    description="Language reference, programming guide, and learning materials",
                    mimeType="text/markdown"
                ),
                Resource(
                    uri="clarion://docs/libraries",
                    name="Libraries and Components",
                    description="ABC Library, Internet Builder, Business Math library references",
                    mimeType="text/markdown"
                ),
                Resource(
                    uri="clarion://docs/ide_development",
                    name="IDE and Development",
                    description="IDE reference, user guides, and getting started materials",
                    mimeType="text/markdown"
                ),
                Resource(
                    uri="clarion://docs/templates",
                    name="Templates",
                    description="Template guide and language reference",
                    mimeType="text/markdown"
                ),
                Resource(
                    uri="clarion://docs/specialized",
                    name="Specialized Features",
                    description="Database drivers, XML support, Report Writer, Application Broker",
                    mimeType="text/markdown"
                )
            ]

            return resources

        @self.server.read_resource()
        async def read_resource(uri: str) -> str:
            """
            Read a specific documentation resource.
            Returns a summary or index of the requested resource.
            """
            logger.info(f"Received read_resource request for: {uri}")

            # Parse URI
            if not uri.startswith("clarion://docs/"):
                raise ValueError(f"Invalid URI: {uri}")

            resource_type = uri.replace("clarion://docs/", "")

            # Get collection info
            try:
                info = self.vector_store.get_collection_info()
                total_chunks = info.get('points_count', 0)
            except:
                total_chunks = 0

            # Build response based on resource type
            if resource_type == "all":
                content = f"""# Clarion Documentation - Complete Index

**Total Chunks Indexed:** {total_chunks}

## Available Documentation Categories

1. **Core Language** - Language reference, programming guide, learning materials
2. **Libraries and Components** - ABC Library, Internet Builder, Business Math
3. **IDE and Development** - IDE reference, user guides, getting started
4. **Templates** - Template guide and language reference
5. **Specialized Features** - Database, XML, Reports, Application Broker

## How to Use

Use the `search_docs` tool to perform semantic searches across all documentation.

Example queries:
- "How do I define a QUEUE in Clarion?"
- "What's the syntax for a LOOP statement?"
- "Show me examples of using the ABC library"
- "How do I connect to a SQL database?"
"""
            else:
                # Category-specific content
                categories = {
                    'core_language': "Core Language Documentation",
                    'libraries': "Libraries and Components",
                    'ide_development': "IDE and Development Tools",
                    'templates': "Templates and Template Language",
                    'specialized': "Specialized Features",
                    'advanced': "Advanced Topics",
                    'utilities': "Utilities and Tools"
                }

                category_name = categories.get(resource_type, resource_type.replace('_', ' ').title())

                content = f"""# {category_name}

**Category:** {resource_type}
**Total Chunks Indexed:** {total_chunks}

## About This Category

This resource provides access to Clarion documentation in the "{category_name}" category.

Use the `search_docs` tool with `doc_type: "{resource_type}"` filter to search only within this category.

## Example Query

```
search_docs(
    query="your search query",
    doc_type="{resource_type}",
    max_results=5
)
```
"""

            return content

        @self.server.list_tools()
        async def list_tools() -> List[Tool]:
            """
            List available tools for interacting with Clarion documentation.
            """
            logger.info("Received list_tools request")

            tools = [
                Tool(
                    name="search_docs",
                    description="Semantic search across Clarion documentation. Returns relevant documentation chunks with similarity scores and source citations. NOTE: Code examples may have lost indentation during PDF conversion - manually format Clarion code (e.g., indent MAP statements) before use.",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "Natural language query about Clarion programming (e.g., 'How do I define a QUEUE?')"
                            },
                            "max_results": {
                                "type": "integer",
                                "description": "Maximum number of results to return (default: 5)",
                                "default": 5
                            },
                            "doc_type": {
                                "type": "string",
                                "description": "Filter by document type (e.g., 'core_language', 'libraries', 'templates')",
                                "enum": ["core_language", "libraries", "ide_development", "templates", "specialized", "advanced", "utilities"]
                            },
                            "min_score": {
                                "type": "number",
                                "description": "Minimum similarity score threshold (0.0 to 1.0, default: 0.3)",
                                "default": 0.3
                            }
                        },
                        "required": ["query"]
                    }
                )
            ]

            return tools

        @self.server.call_tool()
        async def call_tool(name: str, arguments: Any) -> List[TextContent]:
            """
            Execute a tool call.
            """
            logger.info(f"Received call_tool request: {name}")

            if name == "search_docs":
                return await self._handle_search_docs(arguments)
            else:
                raise ValueError(f"Unknown tool: {name}")

    async def _handle_search_docs(self, arguments: Dict) -> List[TextContent]:
        """
        Handle search_docs tool call.
        """
        query = arguments.get("query")
        max_results = arguments.get("max_results", 5)
        doc_type = arguments.get("doc_type")
        min_score = arguments.get("min_score", 0.3)

        logger.info(f"Searching for: '{query}' (max_results={max_results}, doc_type={doc_type}, min_score={min_score})")

        # Get embedding model
        embedding_model = self._get_embedding_model()

        # Generate query embedding
        query_embedding = embedding_model.encode_text(query)

        # Build filter
        filter_dict = {}
        if doc_type:
            filter_dict['doc_type'] = doc_type

        # Perform search
        results = self.vector_store.search(
            query_vector=query_embedding.tolist(),
            limit=max_results,
            score_threshold=min_score,
            filter_dict=filter_dict if filter_dict else None
        )

        # Format results
        if not results:
            response = f"""# Search Results for: "{query}"

No results found matching your query.

**Suggestions:**
- Try using different keywords
- Lower the minimum score threshold
- Remove document type filters
- Check if documents are indexed (use resources/list)
"""
            return [TextContent(type="text", text=response)]

        # Build formatted response
        response_parts = [f"# Search Results for: \"{query}\"\n"]
        response_parts.append(f"**Found {len(results)} relevant chunks**\n")

        for i, result in enumerate(results, 1):
            score = result['score']
            metadata = result['metadata']
            text = result['text']

            source = metadata.get('source', 'Unknown')
            doc_type_val = metadata.get('doc_type', 'unknown')
            chunk_idx = metadata.get('chunk_index', 0)
            chunk_count = metadata.get('chunk_count', 0)

            response_parts.append(f"\n## Result {i}: {source}")
            response_parts.append(f"**Score:** {score:.4f} | **Type:** {doc_type_val} | **Chunk:** {chunk_idx + 1}/{chunk_count}\n")
            response_parts.append("**Content:**\n")
            response_parts.append(f"```\n{text}\n```\n")

        response_parts.append("\n---\n")
        response_parts.append(f"*Retrieved from Clarion Knowledge Base (Vector Store: {len(results)} chunks)*")

        response_text = "\n".join(response_parts)

        return [TextContent(type="text", text=response_text)]

    async def run(self):
        """Run the MCP server."""
        logger.info("Starting Clarion MCP Server...")

        async with stdio_server() as (read_stream, write_stream):
            await self.server.run(
                read_stream,
                write_stream,
                self.server.create_initialization_options()
            )


async def main():
    """Main entry point."""
    server = ClarionMCPServer()
    await server.run()


if __name__ == "__main__":
    asyncio.run(main())
