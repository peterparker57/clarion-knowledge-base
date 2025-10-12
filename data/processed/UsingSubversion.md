Inside the Clarion IDE 
Integrating Subversion Version Control 
 
 
Introduction 
The IDE has integration for the free, open source, Subversion version control 
system. In this lesson, we'll teach you how 
to install Subversion and make it part of your development cycle. 
 
From the Subversion home page: 
Subversion is an open source version control system. Founded in 2000 by 
CollabNet, Inc., the Subversion project and software have seen incredible 
success over the past decade. Subversion has enjoyed and continues to enjoy 
widespread adoption in both the open source arena and the corporate world. 
 
Why Version Control? 
Version Control, also known as revision or source control, manages changes to 
your projects and solutions. If you have a team of developers working on a 
medium to large size project, it is strongly recommended. 
 
Without a version control system in place, you would have to rely on a project 
manager to keep track of who is working on what part of the project. Version 
control simplifies this process, and once set up properly it virtually manages 
itself. 
 
The simplest method of preventing concurrent access problems of applications 
involves locking or “checking out” the file so that one developer at a time has 
write access to the central “repository” of those files. Once a developer “checks 
out” a file, others can read that file, but no one else may change that file until that 
developer “checks in” the updated version. 
 
Installing Subversion Version Control 
To install the TortoiseSVN GUI interface, first obtain the download at the 
following link: 
 
http://tortoisesvn.tigris.org/ 
 
The following link contains additional information regarding Subversion.  
 
http://subversion.tigris.org/ 
 
 


---

How to Set up Subversion Control in the Clarion IDE 
 
To use SVN in a stand-alone environment allowing a single developer to easily 
track versions of a product you do the following: 
 
First, configure the Clarion IDE to monitor the directories where you want 
applications and dictionaries to be version controlled via Subversion. See the 
Binary File auto-export/import Tools Option to see how this is done. 
 
Create the text files that will be stored in SVN. To create the text files for 
applications all you need to do is open the application and press the "Save & 
Close" button. To create the text files for dictionary files you will need to either 
manually export the dictionary to text or make a change to the dictionary so that 
the "Save" option is enabled. If you manually create the text file, don't forget to 
set the extension of the text file to the same extension the Dictionary monitor is 
configured to read/write (default is dcv). 
 
Once you have created the text files you are ready to set up Subversion to track 
changes. 
 
Activating Subversion Control in the Clarion IDE 
 
Here are the steps to activating Subversion for your targeted Clarion solution. 
 
1. Create a directory to hold the SVN repository (for example., 
E:\dev\svnrepository). A network drive is recommend where all members 
of your development team will have access. 
 
2. Right click on the new created folder in Step (1) and select 
TortoiseSVN/Create repository here. 
 
3. Next, navigate to the directory that is the root of your development. For 
example, if you put all of your applications in separate directories below 
E:\dev, then go to the E:\dev folder. 
 
4. Right click in the folder (not on any file or folder) and select SVN 
Checkout. 
 
5. Next, set the URL of the repository to the folder where you created the 
SVN repository. The URL must start with file:/// and all slashes must be 
forward slashes. For example: file:///E:/Dev/SVNRepository. Also in this 
repository should contain the subfolders of projects that you wish to 
activate version control. 
 
6. Verify that the Checkout directory has not been changed (TortoiseSVN 
often adds a subfolder), and then click OK. 


---

 
7. You will get a warning message that the “target folder is not empty”. Click 
Yes. 
 
8. Right click in the folder (not on any file or folder) and select SVN Commit. 
 
9. Tick (select) the files you want version controlled, and then click OK.. 
Normally the files you tick will be the solution (.SLN), project (.cwproj), 
application text (.apv) and dictionary text (.dcv) files. 
 
 
To make it easier for you to find newly added files to your system, you should 
add files that you do not want in SVN to the SVN ignore list. To do this, right click 
on the file in the lower panel of the Commit dialog and select "Add to Ignore List".  
 
Alternatively, you can right click on your root folder in Windows and select 
Properties. You will see there is a new Subversion tab. Select that and then click 
on the Properties button. From the Property name dropdown select svn:ignore, 
then add file patterns (eg *.clw or *.app) to the Property values entry control. 
Ticking the "Apply property recursively" checkbox will apply the ignore filter to all 
child folders. This is a much faster way to set up the system if you have lots of 
directories that you are setting up. 
 
The process is now complete. Next time you load a dictionary or application in 
the IDE you will see a History tab at the bottom of the window. When selected, it 
will show the history of the file. Further, right clicking on a file in the Solution 
Explorer allows you access to SVN commands like commit or Diff. 
 
If you add your dictionary file as a solution item you can then easily access the 
SVN commands for the dictionary. You can also open the dictionary directly from 
the Solution Explorer. 
 
 
 
