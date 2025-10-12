 
 
 
 
 
Clarion Application Broker 
 
 
 
 
 
 


---

2 
Application Broker 
 
 
 
COPYRIGHT SoftVelocity Inc. All rights reserved. 
 
This publication is protected by copyright and all rights are reserved by SoftVelocity Incorporated. It may not, in whole or 
part, be copied, photocopied, reproduced, translated, or reduced to any electronic medium or machine-readable form 
without prior consent, in writing, from SoftVelocity. 
 
This publication supports Clarion. It is possible that it may contain technical or typographical errors. SoftVelocity 
provides this publication “as is,” without warranty of any kind, either expressed or implied. 
 
 
 
 
 
 
 
www.softvelocity.com 
 
 
 
 
 
Application Broker  
 
 
 
 
 
 
Trademark Acknowledgements: 
 
 
SoftVelocity is a trademark of SoftVelocity Inc. 
Clarion is a trademark of SoftVelocity Inc. 
 
 
 
 
 
 
 
 
 
 
 
 
 
Printed in the United States of America (1105) 


---

3 
Chapter 1 
Introduction 
 
 
Contents: 
Clarion Application Broker ............................................................................................................. 1 
1 - Introduction ................................................................................................................................ 5 
What is the Application Broker? .................................................................................................................................... 5 
What You’ll Find in this Book ........................................................................................................................................ 6 
Documentation Conventions .......................................................................................................... 7 
2 - General Setup ............................................................................................................................. 8 
System Requirements ................................................................................................................................................... 8 
Server System ........................................................................................................................................................ 8 
Client System .......................................................................................................................................................... 8 
Application Broker Installation .............................................................................................................................. 13 
3 - The Application Broker ............................................................................................................ 13 
Running the AppBroker ............................................................................................................................................... 13 
Using the AppBroker ................................................................................................................................................... 13 
Testing Concurrent Access ......................................................................................................................................... 14 
Running your Applications using the Broker ............................................................................................................... 14 
Using Hyperlinks to start an application ............................................................................................................... 15 
Firewalls ................................................................................................................................................................ 15 
4 – Application Broker (Overview) ................................................................................................ 17 
General Overview ....................................................................................................................................................... 17 
Running the Application Broker .................................................................................................................................. 17 
Starting / Stopping the Application Broker .................................................................................................................. 18 
Connecting to your Applications using the Application Broker ................................................................................... 18 
Changing the password for the administrator account ............................................................................................... 19 
Remote Admin Access ................................................................................................................................................ 19 
Additional Notes:................................................................................................................................................... 19 
Registry Key Information ............................................................................................................................................. 19 
Debugging ................................................................................................................................................................... 19 
Notes on SSL support ................................................................................................................................................. 21 
SSL Registry Support .................................................................................................................................................. 21 
5. 
Application Deployment ..................................................................................................... 21 
Folders ........................................................................................................................................................................ 21 
Remote Access to the Application Broker ................................................................................................................... 23 
Application Broker Configuration Options ................................................................................................................... 24 
Deployment Checklist ................................................................................................................................................. 27 
Testing Locally ...................................................................................................................................................... 28 
Index ............................................................................................................................................... 29 
 


---

4 
Application Broker 
 
 
 


---

5 
Chapter 1 
Introduction 
 
 
1 - Introduction 
 
This book contains information on installation and setup of the Application Broker for web applications created with 
the H5 Web extension template. 
 
The Application Broker is supported on all OS editions of Windows. 
 
 
What is the Application Broker? 
The Application Broker is your connection to web apps made with Clarion. It allows end-users to run Web-enabled 
applications using a browser. 
 
 
 
 
 
The Application Broker is used for testing and deploying your Web-enabled application on any Windows OS. The 
Application Broker provides SSL support, and is installed as Windows Service. 


---

6 
Application Broker 
 
 
 
 
What You’ll Find in this Book 
 
The following lists the parts of this book and summarizes its content: 
 
Introduction 
 
Chapter One: the chapter you’re reading now. This is an introduction to the Application Broker. 
 
Setup 
 
Chapter Two: System Requirements, and step-by-step instructions tell you how to install the Clarion Application Broker 
 
Running the Application Broker 
 
Chapter Three: Documents the Clarion Application Broker. 
 
Running the Application Broker 
 
Chapter Four: Documents the Application Broker service, and the supporting applet. 
 
Deployment Checklist 
 
Chapter Five: Documents the files needed in order to deploy a Web enabled application. 


---

7 
Chapter 1 
Introduction 
 
 
Documentation Conventions 
Typeface Conventions 
 
Italics 
Indicates what to type at the keyboard, such as Enter This. It also indicates information displayed in a 
window’s title bar. 
 
Boldface 
Indicates commands or options from a pulldown menu or text in a dialog window. 
 
Courier New Used for diagrams, source code listings, to annotate examples, and for examples of the usage of source 
statements. 
 
 
 
 
 


---

10 
Application Broker 
 
 
2 - General Setup 
 
System Requirements 
 
 
Server System 
You can run the Application Broker and Web-enabled applications on any Windows OS edition. 
 
Performance of your web app depends on the speed of your server’s connection to the Internet and the traffic you 
expect your application to handle.  
 
 
Client System 
Clients can run a Clarion Web application on any platform which has an internet browser available (mobile, tablet, 
desktop). 


---

9 
Chapter 2 
General Setup 
 
 
 
 
Web-enabled Clarion applications work under any browser that supports JavaScript. 
 
 
 


---



---

13 
Chapter 3 
The Application Broker 
 
 
 Application Broker Installation 
The Application Broker has its own install program.  
 
By default, the AppBroker is installed in the \AppBroker folder.  
 
 
 
 
3 - The Application Broker 
 
Running the AppBroker 
 
The Application Broker uses the ports you specified during installation. You can change the ports (and more) at any time 
by running the AppBrokerServiceMgr.exe. If you are running any other program which uses port 80, you must specify 
another port (e.g., 8080) for the Application Broker. 
 
 
Using the AppBroker 
 
A client must exit the application for the application to close; simply closing the internet browser does not immediately 
close an application. If the client closes the browser, the application won't actually close until a timeout occurs. The 
templates used to create the web app set an application's timeout to 10 minutes by default. You can modify this timeout 
interval in the H5 global extension used in the application. 


---

14 
Application Broker 
 
 
 
 
Testing Concurrent Access 
You can easily test any concurrency issues (i.e., issues in your application concerning more than one user) with multiple 
clients. You can also test with a single client by starting two instances of your browser and running a copy of the 
application in each. 
 
 
Running your Applications using the Broker 
To run a Web-enabled application from a browser, just open your favorite internet browser and enter a URL in the 
following format: 
 
http://nnn.nnn.nnn.nnn/appname.wap.0 
 
where appname.wap is your application's executable file name, substituting “wap” for the “exe” extension (make 
sure to add a dot zero (.0) at the end of the URL)  
The nnn.nnn.nnn.nnn is your IP address, or 
 
http://domain.ext/appname.wap.0 
 
where domain.ext is your domain name, if your IP address has a name registered with a Domain Name Server (DNS). 
If you are running the broker on a port other than port 80 (the default HTTP port), include the port number in the URL. 
Examples: 
http://nnn.nnn.nnn.nnn:8080/appname.wap.0 
http://domain.ext:8080/appname.wap.0 
 
 
 
If your application is located in a subdirectory under the \EXEC folder, then the sub-folder must be entered after the 
domain name (Example: http://domain.ext:8080/exec/order/appname.wap.0 where ORDER is a subdirectory under the 
\EXEC folder) 


---

15 
Chapter 3 
The Application Broker 
 
 
Using Hyperlinks to start an application 
You can create hyperlinks in an HTML Web page to execute Web-enabled applications.  
For example: 
<A HREF="http://nnn.nnn.nnn.nnn/appname.wap.0">Click to start app</a> 
 
<A HREF="http://nnn.nnn.nnn.nnn:8080/appname.wap.0">Click to start app</a> 
 
 
Firewalls 
To facilitate access for users behind firewalls or proxy servers, just be sure to open the port in the firewall (8080, 
or the port that you are using). 


---

16 
Application Broker 
 
 
 


---

17 
Chapter 4 
The Application Broker 
 
 
4 – Application Broker (Overview) 
 
General Overview 
The Application Broker supports both HTTP and HTTPS (SSL/TLS) connections for data exchange. 
 
System services can be executed under the Local System Account or under a specific Windows user account. 
If you want to enable interaction with the Clarion debugger the service must be set to allow interaction with the 
desktop. 
 
Changes to the Application Broker parameters take effect immediately except for changes to the communication 
ports and the public directory. Changes to these parameters only take effect after SE Application Broker Service 
is stopped and restarted. 
 
 
 
Running the Application Broker 
The Application Broker is installed as a System Service under Windows. 
 
 
 
The Application Broker starts when the OS is loaded (before any user login). The service may be configured to start 
automatically or manually. 
 
The communication ports for the Application Broker are defined at the time the AppBroker service is started. By default 
port number 8080 is used for non-secure communications and port 443 for secure communications. 


---

18 
Application Broker 
 
 
Starting / Stopping the Application Broker 
There are two ways to start and stop the Application Broker 
 
1. Running the AppBrokerServiceMgr.exe 
 
2. Use the Control Service Manager panel 
 
 
A user must exit the web application for the web app to exit/close; simply closing the internet browser does not close the 
web apps connection to the AppBroker. If the client closes the browser without exiting the application, the application 
won't close until a timeout occurs. The templates used to design the application set an application's timeout to 10 minutes 
by default. You can modify this timeout interval in the global extension used in the application. 
 
 
Connecting to your Applications using the Application Broker 
If you are using Secure Socket Layers SSL for your web connections, type https instead of http. 
Examples: 
https://nnn.nnn.nnn.nnn/appname.wap.0 
https://domain.ext/appname.wap.0 


---

21 
Chapter 4 
The Application Broker 
 
 
Changing the password for the administrator account 
The Application Broker permits remote access to your Clarion web applications. The remote access is password 
protected. To set the Admin username/password: 
 
Run the AppBrokerServiceMgr.exe (located in the root of the folder where the AppBroker is installed) and choose the 
menu item “Change Server Security” 
 
Remote Admin Access 
 
To open a remote session point your browser at: 
 
If testing on your development machine 
http://localhost:8088/appbroker/ 
 
***Note replace the 8088 with whatever Port you configured the AppBroker to listen on. Also, don’t forget the trailing / at 
the end of the URL 
 
If you have set up a remote server point your browser at 
http://#.#.#.#:PortNumber/appbroker/ 
 
***Note replace the #.#.#.#:PortNumber with the IP address (or domain name) and whatever Port you configured the 
AppBroker to listen on. Also, don’t forget the trailing / at the end of the URL 
 
 
If you haven’t changed the Admin username/password when you attempt remote access to the AppBroker and are 
prompted for the Username, enter “CWIC” for the Username and leave the Password blank. You can change the 
username/password used to login to the broker by running the Running the AppBrokerServiceMgr.exeError! Bookmark not 
defined. 
 
Changes to the communication ports numbers and public directory take effect after the Application Broker is stopped 
and restarted. 
 
Additional Notes: 
 
If the account used to run the service (a user account or the Local System account used for the App Broker 
service) does not have sufficient rights to the Public folder (Read-Write-Create-Execute), your applications will fail 
to execute. 
 
 
 
 
 
Registry Key Information 
The Application Broker settings are stored in the following Windows Registry location: 
HKEY_LOCAL_MACHINE\SYSTEM\ControlSetxxx\Services\Clarion Application Broker 
(xxx is a transient number (001, 002, etc.)) 
You can edit this this registry key if you wish to manually change any of the Application Broker settings. 
 
 
Debugging 
As the Application Broker is a service, it needs to be able to interact with the desktop to allow a debugger to be 
opened. Therefore, the Application Broker service needs the Allow service to interact with desktop setting to be 


---

20 
Application Broker 
 
switched on. 
 
To change the "Allow service to interact with desktop" setting: 
 
1. Open the Windows Services application (Control Panel Administrative Tools Services) 
and from the list of services choose Clarion Application Broker. 
 


---

21 
Chapter 5 
Application Deployment 
 
 
Notes on SSL support 
LibreSSL is a version of the TLS/crypto stack forked from OpenSSL in 2014, with goals of modernizing the codebase, 
improving security, and applying best practice development processes. The AppBroker uses the LibreSSL stack for SSL 
support. SSL can protect data in transit on a live connection, but it cannot protect data before it is sent or after it 
arrives. 
 
The Openssl.exe program is a command line tool for using the various cryptography functions of OpenSSL's crypto 
library. You can obtain the OpenSSL utilities from various Internet download sites. 
 
LibreSSL is available for download in source format from https://www.libressl.org/ 
 
There are pre-built binary versions available for download. 
 
To make use of SSL with your web-enabled application you need to deploy the key pair files. LibreSSL supports two 
formats for storing and exchanging key pairs. The format used with the Application Broker is PEM, which is defined in 
RFCs 1421, 1422, 1423 and 1424. PEM data is base-64 encoded and provides abilities to encrypt the data before its 
encoded. 
 
The Application Broker service accepts the certificate file specified as CertificateFile in the broker’s registry key, or uses 
the "server.pem" file located in the directory that contains the AppBroker executable file, if the CertificateFile parameter is 
empty. 
 
The Application Broker install contains a sample self-signed certificate file. For actual distribution, a valid signed 
certificate should be obtained from a proper certificate authority. 
 
SSL Registry Support 
The Application Broker requires a certificate file for SSL support. The service uses the certificate file specified in the 
following registry key: 
 
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Clarion Application Broker\CertificateFile 
 
By default, it uses the Server.pem file located in the directory that contains the AppBroker executable, if the 
"CertificateFile" registry key is empty. 
 
To specify an SSL Certificate run the AppBrokerServiceMgr.exe and choose the menu item “Change Server 
Security”. The PEM must be located in the same directory where the AppBroker is installed. 
 
Example: 
C:\AppBroker\server.pem 
 
 
5. Application Deployment 
 
Folders 
When using the Application Broker, the directory from which it is installed is the virtual root directory for all executables. 
The \PUBLIC folder below the AppBroker folder is the virtual root for any downloadable files. For example, a link to an 
HTML document in the \Public directory would be addressed as: 
 
http://nnn.nnn.nnn.nnn/index.htm 
 
 An executable in the same directory as the Application Broker is referenced using a similar URL: 
 
http://nnn.nnn.nnn.nnn/appname.wap.0 
 


---

22 
Application Broker 
 
In most deployments, you copy all executables and required DLLs to the EXEC folder or a subfolder under the EXEC 
folder. 
 
Even though these files are in different directories, the Application Broker handles the routing and no relative directory 
information is required. 
 
If you want to keep your applications in different directories, you call the application using its relative path. For example, 
with the AppBroker running in \AppBroker and an application named myapp.exe is deployed to 
\AppBroker\Exec\OrdersApp. You would start it by using this URL: 
 
http://localhost/exec/ordersapp/appname.wap.0 


---

23 
Chapter 5 
Application Deployment 
 
 
Remote Access to the Application Broker 
If you provide a Remote password in the Application Broker Setup, you can access your AppBroker remotely from your 
web browser. This allows you to modify settings, suspend and enable access to an application, and see the status of the 
latest requests. 
 
To access the AppBroker from a browser: 
 
1. 
Enter the following URL in your browser's Address or Location entry control using the URL in 
the following format: 
HTTP://domainname.ext/appbroker/ 
or 
HTTP://nnn.nnn.nnn.nnn/appbroker/ 
a password dialog appears. 
2. 
Enter the Username and the password when prompted 
 
A Web page appears with hyperlinks for the following functions: 
 
Setup 
Provides access to modify the setup options. You can modify any of the setup options except the Port Number 
and the Remote Password. Those settings can only be changed on the server. 
 
Suspend 
Allows you to suspend access to any Web-enabled application deployed on the Application Broker site. This must 
be done in order to update the application or data files. If an application is running, the session is closed and the 
application is closed. Users who were running the program receive a message informing them that the application 
has been suspended for maintenance. 
 
To suspend access, type in the full name of the executable file (including the extension), then press the OK 
button. If the application to suspend is deployed to a subdirectory, you need not specify that directory here. A 
Web page is returned listing the applications which are currently suspended. 
 
Enable 
Allows you to re-enable access to any Web-enabled application on the Application broker site which has been 
suspended. 
 
To re-enable access, type in the full name of the executable file (including the extension), then press the OK 
button. A Web page is returned listing the applications which are still suspended. 
 
Status 
This displays the current status of applications running on your broker site including the time of access and the IP 
address of the clients accessing applications. 


---

24 
Application Broker 
 
 
Application Broker Configuration Options 
 
 
 
From the Application Broker’s Setup menu option, you can specify the following options: 
 
Default Home Page 
The document which is delivered by default if no specific URL is specified. The default is index.htm. 
 
Public Directory 
The directory where common deliverable files are deployed (HTML files, images, etc.). This is also the directory 
under which temporary directories containing the HTML files representing an application are created. The default 


---

25 
Chapter 5 
Application Deployment 
 
is /Public. 
 
Port Number 
The HTTP port to which the application broker is bound. If specified on the broker's command line, this is disabled 
and cannot be modified. 
 
When a port other than 80 (the default HTTP port) is used, clients (or your hyperlinks) must specify the port in the 
URL. For example if the broker is attached to port 8080, you would specify: 
 
http://nnn.nnn.nnn.nnn:8080/appname.wap.0 
 
Use Log File 
Checking this box enables server logging. This generates a logfile entry for each request made by clients 
accessing the Application Broker. The logfile contains the requester's IP address, the date and time of the 
request, and the request made. Keep in mind that the logfile will continue to grow as entries are appended to it. 
 
Log File Name 
Specifies the name of the logfile. 


---

26 
Application Broker 
 
 
 
Max Simultaneous Connections 
This specifies the maximum number of connections allowed. A notice is returned to users trying to access the 
broker when an attempt to exceed this number is made. 
 
Use Debug Setup 
This specifies to run applications in the debugger. You must have access to the Server machine to run the 
debugger. Specify the location of the debugger and redirection file in the entry field provided. For example: 
 
C:\Clarion\bin\Cladb.exe C:\Clarion\bin\Clarion110.red 


---

27 
Chapter 5 
Application Deployment 
 
 
Deployment Checklist 
1. 
Install and configure the Application Broker.  
 
2. 
Start the Application Broker Service. 
 
3. 
Deploy your application and any the files it needs (DLLs, data files, image files, etc.) to the directory from which 
the Application Broker will run it. These should be placed in a subdirectory in or under C:\AppBroker\EXEC\. 
Data files should be in the same directory as the executable, or if your application is created to use data files in a 
different directory or drive, this location must be accessible to the application. 
 
4. 
The install creates a subdirectory below the broker directory named \Public. This directory is used to deliver files 
(such as images or other HTML files) by the Application Broker. 
 
The Application Broker will not deliver any files from its executable directory. This prevents downloading data files 
or executables from your site. Your application creates HTML files at runtime and automatically places them in a 
temporary subdirectory below either the \Public directory. 
 
At runtime, a temporary directory is created for each client connection. These directories are automatically 
deleted when the connection terminates. Graphics in IMAGE controls are automatically extracted to this directory 
when they are not found in the /Public directory. Icons displayed in LISTs or on BUTTONs are not automatically 
extracted and must be deployed to the /Public directory. 
 
5. 
Run the Application Broker service on the Windows machine.  
 
6. 
Provide users who want to access the application a URL in the following format: 
 
http://nnn.nnn.nnn.nnn/appname.wap.0 
 
Or 
 
http://domain.ext/appname.wap.0 
 
Appname.wap is your application's executable file name. Make sure the user adds a dot zero (.0) after 
the executable name. 
 
If you are running the executable broker on a port other than 80 (the default HTTP port), users must include the 
port number in the URL. For example, 
 
http://nnn.nnn.nnn.nnn:8080/appname.wap.0 


---

28 
Application Broker 
 
 
If your application has any command line parameters, add a question mark and the command line parameter. For 
example: 
 
http://nnn.nnn.nnn.nnn/appname.wap.0?myargument 
 
Testing Locally 
You can use ‘localhost or 127.0.0.1, as the IP address for testing your application locally (with the broker and browser 
on the same machine). 
 


---

29 
Chapter 5 
Application Deployment 
 
Index 
Index 
AppBrokerServiceMgr.exe, 13, 18, 19, 
21 
Application Broker Configuration, 24 
Application Deployment, 21 
Architecture, 5 
Changing the password for the 
administrator account, 19 
Connecting to your Applications, 18 
Deployment Checklist, 27 
Firewalls, 15 
LibreSSL, 21 
Public Directory, 24 
Registry Key, 19 
Remote Access to the Application 
Broker, 23 
Running your Applications using the 
Broker, 14 
Supported clients, 8 
the EXEC folder, 22 
timeout, 13, 18 
Use Log File, 25 
 
 
