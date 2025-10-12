 


---

COPYRIGHT 1994-2013 SoftVelocity Inc.  All rights reserved. 
This publication is protected by copyright and all rights are reserved by SoftVelocity Incorporated.  
It may not, in whole or part, be copied, photocopied, reproduced, translated, or reduced to any 
electronic medium or machine-readable form without prior consent, in writing, from SoftVelocity 
Incorporated. 
This publication supports Clarion.  It is possible that it may contain technical or typographical 
errors.  SoftVelocity Incorporated provides this publication “as is,” without warranty of any kind, 
either expressed or implied. 
 
 
 
 
 
 
SoftVelocity Inc. 
P.O. Box 510190 
Melbourne Beach, Florida  32951 
(866) 783-4320 
www.softvelocity.com 
 
 
 
 
Trademark Acknowledgements: 
 
SoftVelocity is a trademark of SoftVelocity Inc. 
Clarion is a trademark of SoftVelocity Incorporated. 
Microsoft,  Windows,  and Visual Basic  are registered trademarks of Microsoft Corporation. 
All other products and company names are trademarks of their respective owners. 
 
 
 
 
 
 
 
Printed in the United States of America  (0409) 


---

 
i 
Contents 
Table of Contents 
Error! Bookmark not defined. 
Database Drivers and Interfaces ..................................................................... 1 
Data Independence ......................................................................................... 1 
Choosing the Right Database Driver ............................................................... 1 
Common Database Driver Features ................................................................ 2 
Database Driver System-wide Logging ........................................................... 2 
On Demand Logging ................................................................................. 3 
Driver Strings ................................................................................................... 5 
DRIVER('Driver', '/DriverString = value') ................................................... 5 
SEND(file, 'DriverString') ........................................................................... 5 
file{PROP:DriverString} ............................................................................. 5 
## ALLOWDETAILS ....................................................................................... 6
## LOGFILE ................................................................................................... 6
ISAM File Drivers 
7 
ASCII Database Driver 
7 
ASCII:Driver Strings ........................................................................................ 8 
ASCII:Supported Commands and Attributes ................................................. 11 
Basic Database Driver 
16 
Basic:Driver Strings ....................................................................................... 17 
Basic:Supported Commands and Attributes ................................................. 21 
Btrieve Database Driver 
26 
Btrieve:Driver Strings ..................................................................................... 29 
Btrieve:Supported Commands and Attributes ............................................... 35 
Btrieve:Other.................................................................................................. 40 
Clarion Database Driver 
44 
Clarion:Driver Strings .................................................................................... 45 
Clarion:Supported Commands and Attributes ............................................... 47 
Clarion:Other ................................................................................................. 51 
Clipper Database Driver 
54 
Clipper:Driver Strings .................................................................................... 56 
Clipper:Supported Commands and Attributes ............................................... 58 
Clipper:Other ................................................................................................. 64 
dBaseIII Database Driver 
66 
dBaseIII:Driver Strings ................................................................................... 68 
dBaseIII: Supported Commands and Attributes ............................................ 70 
dBaseIII:Other................................................................................................ 76 
dBaseIV Database Driver 
78 
dBaseIV:Driver Strings .................................................................................. 80 
dBaseIV:Supported Commands and Attributes ............................................. 82 
dBaseIV:Other ............................................................................................... 88 
DOS Database Driver 
92 
DOS:Driver Strings ........................................................................................ 93 
DOS:Supported Commands and Attributes .................................................. 94 


---

Table of Contents 
ii 
FoxPro / FoxBase Database Driver 
100 
FoxPro:Driver Strings .................................................................................. 102 
FoxPro:Supported Commands and Attributes ............................................. 104 
FoxPro:Other ............................................................................................... 110 
TopSpeed Database Driver 
114 
Enhanced Encryption Support in the TopSpeed driver ............................... 116 
TopSpeed:Driver Strings ............................................................................. 118 
TopSpeed:Supported Commands and Attributes........................................ 120 
TopSpeed:Other .......................................................................................... 125 
Transaction Processing--the TCF File .................................................. 127 
TopSpeed File Errors .................................................................................. 131 
TopSpeed Database Recovery Utility ......................................................... 133 
TPSFIX Command Line Parameters ........................................................... 135 
SQL Accelerators (Drivers) 
138 
General Information for all SQL Drivers ...................................................... 138 
SQL Driver Behavior .................................................................................... 139 
Using SQL Tables in your Clarion Application ............................................ 141 
Server Side Auto incrementing .................................................................... 143 
Language Support................................................................................. 143 
VIEW support for aggregate functions ........................................................ 148 
Date and Time Column Considerations ...................................................... 150 
Clarion Functions used in SQL Filter Statements ....................................... 152 
## CHECKFORNULL ....................................................................................... 156
Optimizing SET processing using the WHERE driver string ....................... 157 
Performance Considerations ....................................................................... 160 
Using Embedded SQL ................................................................................. 163 
General Rules for Browsing SQL-Based Tables ......................................... 169 
Runtime SQL Properties for Views using SQL Drivers ............................... 173 
Debugging Your SQL Application ................................................................ 174 
SQL Driver Strings 
177 
## APPENDBUFFER ....................................................................................... 178
## AUTOINC ..................................................................................................... 178
## BINDCOLORDER ........................................................................................ 179
## BINDCONSTANTS ...................................................................................... 179
## BUSYHANDLING ........................................................................................ 180
## BUSYMESSAGE ......................................................................................... 181
## BUSYRETRIES ........................................................................................... 182
## CLIPSTRINGS ............................................................................................. 182
## FASTCOLUMNFETCH ................................................................................ 182
## FORCEUPPERCASE .................................................................................. 183
## GATHERATOPEN ....................................................................................... 183
## GETINFO ..................................................................................................... 184
## IGNORETRUNCATION ............................................................................... 187
## ISOLATIONLEVEL ...................................................................................... 188
## JOINTYPE ................................................................................................... 190
## MULTIPLEACTIVERESULTSETS .............................................................. 193
## NESTING ..................................................................................................... 193
## ODBCCALL ................................................................................................. 194
## ORDERINSELECT ...................................................................................... 194
## PREAUTOINC ............................................................................................. 194
## TURBOSQL ................................................................................................. 195
## USEINNERJOIN .......................................................................................... 196


---

Table of Contents 
iii 
## UNICODE .................................................................................................... 196
## VERIFYVIASELECT .................................................................................... 197
WHERE (SQL Driver String) ........................................................................ 198 
## ZERODATE ................................................................................................. 199
## ZEROISNULL .............................................................................................. 200
SQL Driver Properties 
202 
PROP:Alias .................................................................................................. 203 
PROP:AlwaysRebind ................................................................................... 203 
PROP:ConnectString ................................................................................... 203 
PROP:DBMSver .......................................................................................... 204 
PROP:Details............................................................................................... 204 
PROP:Disconnect ........................................................................................ 204 
PROP:DriverTracing .................................................................................... 204 
PROP:GroupBy, PROP:Having ................................................................... 205 
PROP:hdbc .................................................................................................. 206 
PROP:henv .................................................................................................. 206 
PROP:Hint ................................................................................................... 206 
PROP:hstmt ................................................................................................. 206 
PROP:Inner ................................................................................................. 206 
PROP:IsolationLevel ................................................................................... 206 
PROP:LogonScreen .................................................................................... 207 
PROP:Log .................................................................................................... 207 
PROP:LogFile .............................................................................................. 207 
PROP:LoginTimeout .................................................................................... 208 
PROP:LogSQL ............................................................................................ 208 
PROP:MaxStatements ................................................................................ 208 
PROP:Name (SQL Properties) .................................................................... 209 
PROP:OrderAllTables ................................................................................. 210 
PROP:OrderInSelect ................................................................................... 210 
PROP:Profile ............................................................................................... 210 
PROP:QuoteString ...................................................................................... 211 
PROP:ServerCaseInsensitive ..................................................................... 211 
## PROP:SQL .................................................................................................. 212
PROP:SQLFilter .......................................................................................... 214 
PROP:SQLJoinExpression .......................................................................... 215 
PROP:SQLOrder ......................................................................................... 216 
PROP:SQLRowSet ...................................................................................... 217 
PROP:TraceFile .......................................................................................... 218 
PROP:TraceKey .......................................................................................... 218 
MSSQL Accelerator 
219 
Overview ...................................................................................................... 219 
MSSQL Import Wizard--Login Dialog .......................................................... 220 
MSSQL Import Wizard--Import List Dialog .................................................. 222 
MSSQL Connection Information and Driver Configuration--File Properties 223 
MSSQL Accelerator Performance Considerations ...................................... 224 
MSSQL Connection Tips ............................................................................. 224 
MSSQL Accelerator Calling a Stored Procedure ........................................ 226 
MSSQL Accelerator Using Embedded SQL ................................................ 229 
MSSQL Accelerator Driver Strings .............................................................. 232 
## AUTOINCUSESSCOPEIDENTITY ....................................................... 233
## HINT ...................................................................................................... 234
LOGONSCREEN (MSSQL Accelerator) ............................................... 234 
GATHERATOPEN (MSSQL Accelerator) ............................................. 234 
SAVESTOREDPROC (MSSQL Accelerator) ........................................ 236 


---

Table of Contents 
iv 
TRUSTEDCONNECTION (MSSQL Accelerator) ................................. 236 
MSSQL Accelerator Driver Properties ......................................................... 237 
PROP:LogonScreen (MSSQL Accelerator) .......................................... 237 
MSSQL Supported Commands and Attributes ............................................ 238 
MSSQL Accelerator Synchronizer Server ................................................... 243 
ODBC Accelerator Driver 
245 
ODBC:Overview .......................................................................................... 245 
What is ODBC? ........................................................................................... 245 
ODBC Pros and Cons ................................................................................. 246 
How ODBC Works ....................................................................................... 247 
ODBC Data Types ....................................................................................... 248 
Importing from ODBC Data Sources ........................................................... 250 
ODBC Driver Configuration--Table Properties ............................................ 251 
ODBC Column Configuration--Column Properties ...................................... 252 
ODBC Key Configuration--Key Properties .................................................. 253 
Debugging Your ODBC Application ............................................................ 254 
ODBC:Driver Strings ................................................................................... 254 
ODBC:Driver Properties .............................................................................. 254 
ODBC:Supported Commands and Attributes .............................................. 255 
Microsoft Access and ODBC ....................................................................... 259 
ODBC Caveats ............................................................................................ 259 
Oracle Accelerator 
260 
Oracle Accelerator Overview ....................................................................... 260 
Oracle Accelerator System Requirements .................................................. 261 
Oracle Accelerator Installation..................................................................... 262 
Registering the Oracle Accelerator ............................................................. 262 
Oracle Accelerator Table Import Wizard--Login Dialog ............................... 263 
Oracle Accelerator Table Import Wizard--Import List Dialog ....................... 264 
Oracle Accelerator Performance Considerations ........................................ 265 
Oracle Accelerator Automatic Login Dialog ................................................. 265 
Oracle Accelerator Generating Unique Key Values .................................... 266 
Oracle Accelerator Driver Strings ................................................................ 267 
## HINT ...................................................................................................... 267
## LOGON SCREEN ................................................................................. 268
## PERSONAL ........................................................................................... 268
## USEASYNCHRONOUSCALLS ............................................................ 268
## WHERE ....................................................................................................... 269
Oracle Accelerator Driver Properties ........................................................... 270 
Oracle Accelerator --Using Embedded SQL ............................................... 270 
## PL/SQL ........................................................................................................ 270
Calling a Stored Procedure ......................................................................... 271 
DLL Coding Practices .................................................................................. 271 
Oracle Accelerator Troubleshooting ............................................................ 272 
Oracle Accelerator Supported Commands and Attributes .......................... 274 
Oracle Accelerator Data Types ................................................................... 279 
Pervasive SQL Accelerator Driver 
282 
Pervasive SQL Import Wizard—Import List Dialog ..................................... 282 
Pervasive SQL Import Wizard--Login Dialog ............................................... 283 
Connection Information and Driver Configuration--File Properties ............. 284 
Pervasive SQL:Supported Commands and Attributes ................................ 285 
SQLAnywhere Accelerator 
290 
Overview ...................................................................................................... 290 


---

Table of Contents 
v 
Start the SQLAnywhere Client..................................................................... 290 
SQLAnywhere Import Wizard--Login Dialog ............................................... 291 
SQLAnywhere Import Wizard—Import List Dialog ...................................... 292 
SQLAnywhere Connection Info/Driver Configuration--File Properties ........ 292 
SQLAnywhere Accelerator Driver Strings ................................................... 293 
LOGONSCREEN (SQLAnywhere Accelerator) .................................... 293 
GATHERATOPEN (SQLAnywhere Accelerator) .................................. 293 
SQLAnywhere Accelerator Driver Properties .............................................. 294 
PROP:LogonScreen (SQLAnywhere Accelerator ) .............................. 294 
Using Embedded SQL(SQLAnywhere Accelerator ) ................................... 295 
Calling a Stored Procedure (SQLAnywhere Accelerator ) .......................... 295 
SQLAnywhere Accelerator Supported File Commands and Functions ...... 296 
SQLAnywhere Accelerator - Synchronizer Server ...................................... 301 
SQLite File Driver 
302 
Overview ...................................................................................................... 302 
Warning: ................................................................................................ 302 
Tip: ........................................................................................................ 302 
Note: ...................................................................................................... 302 
SQLite Accelerator Supported Commands and Attributes .......................... 302 
SQLite Accelerator Driver Strings................................................................ 305 
SQLite Accelerator Properties ..................................................................... 306 
PROP:CreateDB ................................................................................... 306 
Updating data with SQLite ........................................................................... 306 
SQLite and Multithreading ........................................................................... 306 
SQLite Accelerator Error Handling .............................................................. 306 
ADO Interface 
309 
What is ADO? .............................................................................................. 309 
ADO Requirements ..................................................................................... 310 
ADO Logging ............................................................................................... 310 
Index 
311 
 
 


---



---

Database Drivers and Interfaces 
1 
Database Drivers and Interfaces 
 
Data Independence 
Clarion achieves database independence with its built-in driver technology, which lets you access 
data from virtually any file system using the same set of Clarion language commands. Many file 
drivers are available and more are being added. 
 
Before you can use a database driver, it must be registered. The database drivers 
in this package are pre-registered.  See the IDE User's Guide and online help for 
more information on registering add-on database drivers. 
The Clarion language commands for accessing data are the same regardless of the file system 
you use; simply choose the appropriate file driver from the drop-down list in your Data Dictionary, 
then don't worry about it. The file driver translates the Clarion commands to the chosen file 
system's native format. The drivers read and write in the file system's native format without 
temporary files or import/export routines. 
 
Choosing the Right Database Driver 
Choosing a file system is an important decision, and we encourage you to gather as much 
information from as many good sources as you can to support your decision. Although the choice 
of file systems is important, with Clarion, it is not irrevocable. If the file system you choose does 
not live up to your expectations, you can change to one that does. For example, some developers 
use the TopSpeed file system for project development, then switch to an SQL file system during 
project implementation in order to postpone the expense of the SQL software and server 
hardware until late in the development cycle. 


---

Database Drivers 
2 
Common Database Driver Features 
Importing File Definitions 
For existing data, you can generally import file definitions into your Clarion data dictionary. We 
strongly recommend importing file definitions whenever possible, because it reduces your 
development time and effort, plus it results in fewer errors in file definitions.  
Keys, Indexes, and Performance 
Although you may define indexes within your Clarion data dictionary that do not exist within the 
native file system, we do not recommend doing so because your application performance will 
generally suffer. Instead, we recommend defining the required key or index with the native file 
system's tools, then importing the file definition, including the key or index definitions, into your 
Clarion data dictionary. 
Sorting and Collating Sequences 
By default, all SoftVelocity's database drivers sort using the ANSI collating sequence. Adding the 
OEM attribute causes the driver to use the ASCII collating sequence.  Specifying a locale and 
code page via the LOCALE attribute forces the driver to use that locale/code page pair for sorting. 
Disk Caching and Data Integrity 
Disk caching can interfere with the data integrity features of many file systems. By disk caching, 
we mean any facility (for example SMARTDRV) that tells the database driver that a record was 
written to the disk when in fact it was not. 
To improve performance, disk-caching facilities typically accumulate several records at a time in 
RAM then write them to disk all at once. While this does improve performance, it can result in 
corrupt data files if the system fails (due to a power outage, etc.) before the records are written to 
disk.  
A reliable Uninterruptible Power Supply (UPS) can drastically reduce this risk. Therefore, we 
generally recommend no disk caching, but if you must cache, then be sure to use a reliable UPS. 
Database Driver System-wide Logging 
All of SoftVelocity's database drivers can create a log file documenting Clarion I/O statements 
they process, and the SQL Accelerator drivers can log the corresponding SQL statements, and 
the SQL return codes. 
You can generate system-wide logs and on-demand logs (conditional logging based on your 
program logic). 
By default the file drivers read the DRIVERS.INI file located in 
CSIDL_APPDATA\SoftVelocity\Clarion\<clarion_version> to get system wide tracing settings.  
You can override this using either PROP:TraceFile or PROP:TraceKey. 
You can disable system wide logging using PROP:DriverTracing. 
A utility/example application is included--Trace.EXE. A compiled version is installed in the ..\bin 
directory and the source .APP is installed in the \Examples\Resource\Trace directory. This utility 
allows you to easily set tracing options for each file driver and for the VIEW engine. These setting 
are stored in DRIVERS.INI.   
For system-wide logging, you can add the following to your DRIVERS.INI file: 
[filedriver] 
Profile=[1|0] 
Details=[1|0] 


---

Database Drivers and Interfaces 
3 
Trace=[1|0] 
TraceFile=[Pathname] 
where filedriver is the database driver name (for example [MS-SQL]). Neither the INI section 
name [filedriver] nor the INI entry names are case sensitive. 
Profile=1 tells the driver to include the Clarion I/O statements in the log file; Profile=0 tells the 
driver to omit Clarion I/O statements. The Profile switch must be turned on for the Details switch 
to have any effect. 
Details=1 tells the driver to include record buffer contents in the log file; however, if the file is 
encrypted, you must turn on both the Details switch and the ALLOWDETAILS switch to log record 
buffer contents (see ALLOWDETAILS). Details=0 tells the driver to omit record buffer contents. 
The Profile switch must be turned on for the Details switch to have any effect. 
Trace=1 tells the driver to include all calls to the back-end DBMS, including the generated SQL 
statements and their return codes, in the log file. Trace=0 omits these calls. The Trace switch 
generally generates log information that helps to debug the SQL drivers, but is normally not 
particularly useful to the developer. 
TraceFile names the log file to write to. If TraceFile is omitted the driver writes the log to driver.log 
in the current directory. Pathname is the full pathname or the filename of the log file to write. If no 
path is specified, the driver writes the specified file to the current directory. 
  
To view the trace details in your system debugger, name the target trace file DEBUG:.  
Logging opens the named log file for exclusive access. If the file exists, the new log data is 
appended to the file. 
On Demand Logging 
For on-demand logging you can use property syntax within your program to conditionally turn 
various levels of logging on and off. The logging is effective for the target table and any view for 
which the target table is the primary table. 
file{PROP:Profile}=Pathname   !Turns Clarion I/O logging on 
file{PROP:Profile}=''         !Turns Clarion I/O logging off 
PathName = file{PROP:Profile} !Queries the name of the log file 
file{PROP:Log}=string         !Writes the string to the log file 
file{PROP:Details}=1          !Turns Record Buffer logging on 
fFile{PROP:Details}=0         !Turns Record Buffer logging off 
Pathname is the full pathname or the filename of the log file to create. If you do not specify a 
path, the driver writes the log file to the current directory. 
You can also accomplish on demand logging with a SEND() command and the LOGFILE  driver 
string.  
 


---

Database Drivers 
4 


---

Database Drivers and Interfaces 
5 
Driver Strings 
There are switches or "driver strings" you can set to control the way your application creates, 
reads, and writes files with a specific driver. Driver strings are simply messages or parameters 
that are sent to the file driver at run-time to control its behavior. The various driver specific driver 
strings are described in the Driver Strings section for each driver.  
Driver strings are sent in three ways: with the OPEN or CREATE statement, with the SEND 
procedure, and with property syntax. 
All File Drivers support the following Driver Strings: 
## ALLOWDETAILS
## LOGFILE
 
DRIVER('Driver', '/DriverString = value') 
The OPEN(file) and CREATE(file) statements send any driver strings specified in the FILE's 
DRIVER attribute. OPEN sends the string immediately before the file is opened. You may specify 
these driver strings with a hand coded FILE declaration (see DRIVER in the Language Reference 
for more information) or in the Data Dictionary (Driver Options field in the File Properties dialog--
see File Properties ). In either case, you must prepend a forward slash (/) to the driver string. For 
example: 
MyFile FILE,DRIVER('TopSpeed','/LOGFILE=MyFile.Log') 
## CODE
 OPEN(MyFile)         !sends the LOGFILE driver string 
 
SEND(file, 'DriverString') 
The SEND function sends a driver string to the file driver at any time, including before the file is 
opened. SEND functions take two forms--with an equal sign to change the value of the switch, 
and without an equal sign to return the value of the switch. With SEND, the ISAM drivers do not 
require the preceeding forward slash, but the SQL drivers do require it. For example: 
SEND(MyFile,'LOGFILE='&MyLogFile)             !Set the logfile 
MyLogFile=SEND(MyFile,'/LOGFILE')             !Query the logfile 
OldLogFile=SEND(MyFile,'LOGFILE='&NewLogFile) !Set & Query the logfile 
 
file{PROP:DriverString} 
Property syntax is an alternative to the SEND function. With property syntax you can send a 
driver string to the file driver any time after the file is opened. With property syntax, the driver 
string does not require the preceeding forward slash. For example: 
MyLogFile = 'MyFile.Log' 
MyFile{PROP:Profile}=MyLogFile   !Set the logfile 
MyLogFile = MyFile{PROP:Profile} !Query the logfile 
 
 


---

Database Drivers 
6 
## ALLOWDETAILS
 
DRIVER('Driver', '/ALLOWDETAILS = TRUE | FALSE' ) 
  
The ALLOWDETAILS driver string allows the file driver to include record buffer contents in the log 
file for encrypted files. 
The ALLOWDETAILS driver string works with the Details switch described in the Database Driver 
System-wide Logging section. 
 
## LOGFILE
 
DRIVER( 'Driver', '/LOGFILE [= Pathname] [[message]]' ) 
[ LogFile" = ] SEND(file, '/LOGFILE [= Pathname] [[message]]' ) 
 
The LOGFILE driver string turns logging on and off, and optionally writes a message to the log 
file. Turning the LOGFILE switch on writes Clarion I/O statements processed by the driver to the 
specified log file. The LOGFILE driver string is equivalent to the Profile switch described in the 
Database Driver System-wide Logging section.  
Pathname is the full pathname or the filename of the log file to write. If you do not specify a path, 
the driver writes the log file to the current directory. If Pathname is omitted, the driver writes the 
log to Driver.log in the current directory. 
If the log file already exists, the driver appends to it; otherwise, the driver creates the log file. 
The message is optional, however, if included, it must be surrounded by square brackets ([]) and 
a space must preceed the opening square bracket. 
 
  
/LOGFILE must be the last driver string specified by the DRIVER attribute. 
 
 


---

Database Drivers and Interfaces 
7 
ISAM File Drivers 
 
ASCII Database Driver 
ASCII:Specifications 
The ASCII driver reads and writes standard ASCII files without field delimiters. This is often used 
for mainframe data import/export with an ASCII flat-file. By default, a carriage-return/line-feed 
delimits records. The ASCII driver does not support keys. 
Files: 
## CLAASCL.LIB
Windows Static Link Library 
 
## CLAASC.LIB
Windows Export Library 
 
## CLAASC.DLL
Windows Dynamic Link Library 
 
 
Due to its lack of relational features and security (anyone can view and change an ASCII 
file using Notepad), it's unlikely you'll use the ASCII driver to store large data files. But it 
can help you create a text file viewer--use it to open a file, and read it in to a multi-line edit 
or list box control! 
 ASCII:Supported Data Types 
## STRING
## GROUP
## USTRING
 
 ASCII:File Specifications/Maximums 
File Size:             4 GB 
Records per File:      4,294,967,295 bytes 
Record Size:           65,520 bytes  
Field Size:            65,520 bytes  
Fields per Record:     65,520 
Keys/Indexes per File: n/a 
Key Size:              n/a 
Memo fields per File:  n/a 
Memo Field Size:       n/a 
Open Data Files:       Operating system dependent 
 


---

Database Drivers 
8 
ASCII:Driver Strings 
There are switches or "driver strings" you can set to control the way your application creates, 
reads, and writes files with a specific driver. Driver strings are simply messages or parameters 
that are sent to the file driver at run-time to control its behavior. See Common Driver Features--
Driver Strings for an overview of these runtime Database Driver switches and parameters. 
 
 
Some driver strings have no effect after the file is open, so no SEND function syntax is 
listed for those strings. However, the SEND function syntax to return the value of the 
switch is listed for all driver strings.  
The ASCII Driver supports the following Driver Strings: 
## CLIP
 
DRIVER('ASCII', '/CLIP = on | off' ) 
[ Clip" = ] SEND(file, 'CLIP [ = on | off ]' ) 
The driver automatically removes trailing spaces from a record before writing it to file. Conversely, 
the driver automatically expands the clipped records with spaces when read. To disable this 
feature, set CLIP to OFF. The default is ON. SEND returns the CLIP setting (ON or OFF) in the 
form of a STRING(3). 
## CTRLZISEOF
 
DRIVER('ASCII', '/CTRLZISEOF = on | off' ) 
[ EOF" = ] SEND(file, 'CTRLZISEOF [ = on | off ]' ) 
By default (CTRLZISEOF=on) the file driver assumes that any Ctrl-Z characters in the file indicate 
the end of file. To disable this feature set CTRLZISEOF=off. SEND returns the CTRLZISEOF 
setting in a STRING(3). 
## ENDOFRECORD
 
DRIVER('ASCII', '/ENDOFRECORD = n [,m ]' ) 
[ EOR" = ] SEND(file, 'ENDOFRECORD [ = n [,m ]]' ) 
Specifies the end of record delimiter. 
 n represents the number of characters that make up the end-of-record delimiter.  
m represents the ASCII code(s) for the end-of-record delimiter, separated by commas. The 
default is 2,13,10, indicating 2 characters mark the end-of-record, namely, carriage return (13) 
and line feed (10). SEND returns the end of record delimiter. 
 
 
Mainframes and MACs frequently use just a carriage return to delimit records.  
You can use ENDOFRECORD=1,13 to read these files. UNIX/Linux files frequently  
terminate with just a line feed and can be read using ENDOFRECORD=1,10 


---

Database Drivers and Interfaces 
9 
## FILEBUFFERS
 
DRIVER('ASCII', '/FILEBUFFERS = n' ) 
[ Buffers" = ] SEND(file, 'FILEBUFFERS [ = n ]' ) 
Sets the size of the buffer used to read and write to the file, where the buffer size is (n * 512 
bytes). Use the /FILEBUFFERS driver string to increase the buffer size if access is slow. 
Maximum buffer size is 4,294,967,264. SEND returns the size of the buffer in bytes. 
 
 
The default buffer size for files opened denying write access to other users is the larger of 
1024 or (2 * record size), and the larger of 512 or record size for all other open modes.  
TAB 
 
DRIVER('ASCII', '/TAB = n' ) 
[ Spaces" = ] SEND(file, 'TAB [ = n ]' ) 
Sets or queries TAB/SPACE expansion. The ASCII driver expands TABs (ASCII character 9) to 
spaces when reading. The value indicates the number of spaces with which to replace the tab, 
subject to the guidelines below. The default value is 8. SEND returns the number of spaces which 
replace the tab character. 
If n > 0, spaces replace each tab until the character pointer moves to the next multiple of n. For 
example, with the default of 8, if the TAB character is the third character in the record, 6 spaces 
replace the TAB. 
If n = 0, the driver removes tabs without replacement.  
If n < 0, the driver removes tabs with the positive value of n spaces. For example, "TAB=-4" 
causes 4 spaces to replace every tab, regardless of the position of the tab in the record. 
If n = -1, the driver replaces tabs with a single space. 
If n = -100, tabs remain as tabs; the driver does not replace them with spaces. 
## QUICKSCAN
 
DRIVER('ASCII', '/QUICKSCAN = on | off' ) 
[ QScan" = ] SEND(file, 'QUICKSCAN [ = on | off ]' ) 
Specifies buffered access behavior. The ASCII driver reads a buffer at a time (not a record), 
allowing faster access. In a multi-user environment these buffers are not 100% trustworthy for 
subsequent access, because another user may change the file between accesses. As a 
safeguard, the driver rereads the buffers before each record access. To disable the reread, set 
QUICKSCAN to ON. The default is ON for files opened denying write access to other users, and 
OFF for all other open modes. SEND returns the Quickscan setting (ON or OFF) in the form of a 
## STRING(3).
 
 


---

Database Drivers 
10 
UTF 
 
## DRIVER('ASCII', '/UTF = 8 | 16BE | 16LE' )
[ Clip" = ] SEND(file, 'UTF [ = 8 | 16BE | 16LE' ]' ) 
The driver reads and writes data using ASCII, UTF-8, UTF-16LE (little-endian), or UTF-16BE 
(big-endiant) formats.  ASCII uses 1 byte per character.  As a single byte is not enough space to 
store every different character, the same byte can represent different characters depending on 
the code page being used.  The UTF-8 format stores information using 1-4 bytes per character.  
Due to backwards compatibility and size, UTF-8 is the most common format of text files currently 
in use.  UTF-16 uses 2 or 4 bytes per character. The endianness of a 16bit character indicates 
which order the two bytes are written.  According to RFC 2781 if no BOM is written at the 
beginning of a file, then big-endian is assumed.  However, Windows (and many programs running 
under Windows) uses little-endian encoding for LONGs.  Therefore, there are many UTF-16 files 
without BOM that use little-endian and programs that expect UTF-16LE format. 
If UTF is not specified, then the driver will check for a Bit Order Marker (BOM) at the start of the 
file to work out how to read and write data.  If there is no BOM and if there is a USTRING field in 
the file structure, the driver will read and write data using UTF-8.  If there is no BOM and no 
USTRING field, then the driver will read and write data using ASCII characters. 
## UTFBOM
 
DRIVER('ASCII', '/UTFBOM = on | off' ) 
[ UTFBOM" = ] SEND(file, 'UTFBOM [ = on | off ]' ) 
By default, the driver will not write a bit order marker if UTF-16 format is being written.  Otherwise 
no BOM is written.  You can force the driver to write a BOM for UTF-8 files by setting 
UTFBOM=ON.  You can force the driver to not write a BOM for UTF-16 files by setting 
## UTFBOM=OFF.
 


---

Database Drivers and Interfaces 
11 
ASCII:Supported Commands and Attributes 
 
 
File Attributes 
Supported 
 
## CREATE
Y 
 
DRIVER(filetype [,driver string]) 
Y 
 
## NAME
Y 
 
## ENCRYPT
N 
 
OWNER(password) 
N 
 
## RECLAIM
N 
 
PRE(prefix) 
Y 
 
## BINDABLE
Y 
 
## THREAD
Y4 
 
EXTERNAL(member) 
Y 
 
DLL([flag]) 
Y 
 
OEM 
Y 
 
## LOCALE
N 
 
File Structures 
Supported 
 
## INDEX
N 
 
KEY 
N 
 
## MEMO
N 
 
## BLOB
N 
 
## RECORD
Y 
 
 
Index, Key, Memo Attributes 
Supported 
 
## BINARY
N 
 
DUP 
N 
 
## NOCASE
N 
 
OPT 
N 
 
## PRIMARY
N 


---

Database Drivers 
12 
 
## NAME
N 
 
Ascending Components 
N 
 
Descending Components 
N 
 
Mixed Components 
N 
 
 
Field Attributes 
Supported 
 
DIM 
Y 
 
## OVER
Y 
 
## NAME
Y 
 
 
File Procedures 
Supported 
 
BOF(file) 
N 
 
BUFFER(file) 
N 
 
BUILD(file) 
N 
 
BUILD(key) 
N 
 
BUILD(index) 
N 
 
BUILD(index, components) 
N 
 
BUILD(index, components, filter) 
N 
 
BYTES(file) 
Y5 
 
CLOSE(file) 
Y 
 
COPY(file, new file) 
Y 
 
CREATE(file) 
Y 
 
DUPLICATE(file) 
N 
 
DUPLICATE(key) 
N 
 
EMPTY(file) 
Y 
 
EOF(file) 
Y 
 
FLUSH(file) 
N 
 
LOCK(file) 
Y 
 
NAME(label) 
Y 


---

Database Drivers and Interfaces 
13 
 
OPEN(file, access mode) 
Y 
 
PACK(file) 
N 
 
POINTER(file) 
Y2 
 
POINTER(key) 
N 
 
POSITION(file) 
Y3 
 
POSITION(key) 
N 
 
RECORDS(file) 
N 
 
RECORDS(key) 
N 
 
REMOVE(file) 
Y 
 
RENAME(file, new file) 
Y 
 
SEND(file, message) 
Y 
 
SHARE(file, access mode) 
Y 
 
STATUS(file) 
Y 
 
STREAM(file) 
N 
 
UNLOCK(file) 
Y 
 
 
Record Access 
Supported 
 
ADD(file) 
Y 
 
ADD(file, length) 
N 
 
APPEND(file) 
Y 
 
APPEND(file, length) 
N 
 
DELETE(file) 
N 
 
GET(file,key) 
N 
 
GET(file, filepointer) 
Y 
 
GET(file, filepointer, length) 
N 
 
GET(key, keypointer) 
N 
 
HOLD(file) 
N 
 
NEXT(file) 
Y 
 
NOMEMO(file) 
N 


---

Database Drivers 
14 
 
PREVIOUS(file) 
N 
 
PUT(file) 
Y1 
 
PUT(file, filepointer) 
Y1 
 
PUT(file, filepointer, length) 
N 
 
RELEASE(file) 
N 
 
REGET(file,string) 
Y 
 
REGET(key,string) 
N 
 
RESET(file,string) 
Y 
 
RESET(key,string) 
N 
 
SET(file) 
Y  
 
SET(file, key) 
N 
 
SET(file, filepointer) 
Y 
 
SET(key) 
N 
 
SET(key, key) 
N 
 
SET(key, keypointer) 
N 
 
SET(key, key, filepointer) 
N 
 
SKIP(file, count) 
N 
 
WATCH(file) 
N 
 
 
Transaction Processing 
Supported 
 
LOGOUT(timeout, file, ..., file) 
N 
 
## COMMIT
N 
 
## ROLLBACK
N 
 
 
Null Data Processing 
Supported 
 
NULL(field) 
N 
 
SETNULL(field) 
N 
 
SETNULL(file, field) 
N 
 
SETNONNULL(field) 
N 


---

Database Drivers and Interfaces 
15 
Notes 
1 
When using PUT() with this driver you should take care to PUT back the same number of 
characters that were read. If you PUT back more characters than were read, then the 
"extra" characters will overwrite the first part of the subsequent record. If you PUT back 
fewer characters than were read, then only the first part of the retrieved record is 
overwritten, while the last part of the retrieved record remains as it was prior to the PUT(). 
2 
POINTER() returns the relative byte position within the file. 
3 
POSITION(file) returns a STRING(4). 
4 
THREADed files consume additional file handles for each thread that accesses the file. 
5 
BYTES() returns the actual bytes read from the file. The size of the clipped RECORD 
may be different depending on the file driver and it's DRIVER() strings. With the ASCII or 
BASIC file drivers BYTES will include the ENDOFRECORD (typically 13,10) byte count, 
but these bytes are not in the RECORD. With the ASCII driver the /TAB driver string can 
affect (expand, change or remove) the tab (9) characters in the record buffer resulting in 
a different length. 


---

Database Drivers 
16 
Basic Database Driver 
 
 Basic:Specifications 
The BASIC file driver reads and writes comma-delimited ASCII files. By default, quotes ( " " ) 
surround strings, commas delimit fields, and a carriage-return/line-feed delimits records. The 
original BASIC programming language defined this file format. The Basic driver does not support 
keys or backward file processing (thus Basic files are not a good choice for random access 
processing). 
 
 
The Basic file format provides a good choice for a common file format for sharing data 
with spreadsheet programs. A common file extension used for these files is *.CSV, which 
stands for "comma separated values." 
Files: 
## CLABASL.LIB
Windows Static Link Library (32-bit) 
 
## CLABAS.LIB
Windows Export Library (32-bit) 
 
## CLABAS.DLL
Windows Dynamic Link Library (32-bit) 
 Basic:Supported Data Types 
## BYTE
## DECIMAL
## SHORT
## PDECIMAL
## USHORT
## STRING
## LONG
## CSTRING
## ULONG
## PSTRING
## SREAL
## DATE
## REAL
## TIME
## BFLOAT4
## GROUP
## BFLOAT8
 
 Basic:File Specifications/Maximums 
File Size:             4 GB 
Records per File:      4,294,967,295 bytes 
Record Size:           65,520 bytes  
Field Size:            65,520 bytes  
Fields per Record:     65,520 
Keys/Indexes per File: n/a 
Key Size:              n/a 
Memo fields per File:  0 
Memo Field Size:       n/a 
Open Data Files:       Operating system dependent 
 


---

Database Drivers and Interfaces 
17 
Basic:Driver Strings 
There are switches or "driver strings" you can set to control the way your application creates, 
reads, and writes files with a specific driver. Driver strings are simply messages or parameters 
that are sent to the file driver at run-time to control its behavior. See Common Driver Features--
Driver Strings for an overview of these runtime Database Driver switches and parameters. 
 
 
Some driver strings have no effect after the file is open, so no SEND function syntax is 
listed for those strings. However, the SEND function syntax to return the value of the 
switch is listed for all driver strings.  
The Basic Driver supports the following Driver Strings: 
## ALWAYSQUOTE
 
DRIVER('BASIC', '/ALWAYSQUOTE = on | off' ) 
[ QScan" = ] SEND(file, 'ALWAYSQUOTE [ = on | off ]' ) 
For compatibility with Basic format data files created by products that do not place string values in 
quotes, set ALWAYSQUOTE to OFF.  
When the contents of a string field includes the comma or quote character(s), and 
ALWAYSQUOTE is off, the Basic driver automatically places quotes around the string when 
writing to file. This also applies to delimiter characters specified with FIELDDELIMITER, or 
COMMA. For example, with the defaults in use and ALWAYSQUOTE off, a STRING field 
containing the value 1313 Mockingbird Lane, Apt. 33 is automatically stored as: "1313 
Mockingbird Lane, Apt. 33" 
SEND returns the ALWAYSQUOTE setting (ON or OFF) in the form of a STRING(3). 
## COMMA
 
DRIVER('BASIC', /COMMA = n' ) 
[ Comma" = ] SEND(file, 'COMMA [ = n ]' ) 
Specifies a single character field separator. 
n represents the ANSI code for the field separator character. The default is 44, which is 
equivalent to "/FIELDDELIMITER=1,44." 
SEND returns the ASCII code for the field separator character. 
## CTRLZISEOF
 
DRIVER('BASIC', '/CTRLZISEOF = on | off' ) 
[ EOF" = ] SEND(file, 'CTRLZISEOF [ = on | off ]' ) 
By default (CTRLZISEOF=on) the file driver assumes that any Ctrl-Z characters in the file indicate 
the end of file. To disable this feature set CTRLZISEOF=off. SEND returns the CTRLZISEOF 
setting in a STRING(3). 


---

Database Drivers 
18 
## ENDOFRECORD
 
DRIVER('BASIC', '/ENDOFRECORD = n [,m ]' ) 
[ EOR" = ] SEND(file, 'ENDOFRECORD [ = n [,m ]]' ) 
Specifies the end of record delimiter. 
 n represents the number of characters that make up the end-of-record delimiter.  
m represents the ANSI code(s) for the end-of-record delimiter, separated by commas. The default 
is 2,13,10, indicating 2 characters mark the end-of-record, namely, carriage return (13) and line 
feed (10). SEND returns the end of record delimiter. 
 
 
Mainframes frequently use just a carriage return to delimit records. You can use 
ENDOFRECORD to read these files. 
## ENDOFRECORDINQUOTE
 
DRIVER('BASIC', '/ENDOFRECORDINQUOTE = on | off' ) 
[ EORQuote" = ] SEND(file, 'ENDOFRECORDINQUOTE [ = on | off ]' ) 
By default (ENDOFRECORDINQUOTE=ON) the file driver does not recognize an end-of-record 
marker that is within a quoted string. To force End-Of-Record markers to always terminate a 
record, set ENDOFRECORDINQUOTE=OFF. SEND returns the ENDOFRECORDINQUOTE 
setting (ON or OFF) in the form of a STRING(3). 
## FIELDDELIMITER
 
DRIVER('BASIC', '/FIELDDELIMITER = n [,m ]' ) 
[ Limiter" = ] SEND(file, 'FIELDDELIMITER [ = n [,m ]]' ) 
Specifies the field separator. This is in addition to any string delimiter specified by the /QUOTE 
driver string. 
n represents the number of characters that make up the field separator. 
m represents the ANSI code(s) for the field separator characters, separated by commas. The 
default is 1,44 which indicates the comma character. 
SEND returns the field delimiter character. 
 
 
If both FIELDDELIMITER and COMMA are specified, the last specification prevails. 


---

Database Drivers and Interfaces 
19 
## FILEBUFFERS
 
DRIVER('BASIC', '/FILEBUFFERS = n' ) 
[ Buffers" = ] SEND(file, 'FILEBUFFERS [ = n ]' ) 
 Sets the size of the buffer used to read and write to the file, where the buffer size is (n * 512 
bytes). Use the /FILEBUFFERS driver string to increase the buffer size if access is slow. 
Maximum buffer size is 4,294,967,264. SEND returns the size of the buffer in bytes. 
 
 
The default buffer size for files opened denying write access to other users is the larger of 
1024 or (2 * record size), and the larger of 512 or record size for all other open modes.  
 
## FIRSTROWHEADER
 
## DRIVER('BASIC', '/FIRSTROWHEADER=[ON|OFF]' )
[ Buffers" = ] SEND(file, '/FIRSTROWHEADER [ = ON|OFF]' ) 
 
 
This  indicates if the first row of the file contains the labels of the columns. 
 
By default this switch is off.  If turned on, then CREATE(file) will add a line containing the labels of 
the fields separated by the comma character (as specified by the COMMA switch or ','), further the 
first line will always be skipped when reading from the file. 
 
 
## QUICKSCAN
 
DRIVER('BASIC', '/QUICKSCAN = on | off' ) 
[ QScan" = ] SEND(file, 'QUICKSCAN [ = on | off ]' ) 
Specifies buffered access behavior. The BASIC driver reads a buffer at a time (not a record), 
allowing faster access. In a multi-user environment these buffers are not 100% trustworthy for 
subsequent access, because another user may change the file between accesses. As a 
safeguard, the driver rereads the buffers before each record access. To disable the reread, set 
QUICKSCAN to ON. The default is ON for files opened denying write access to other users, and 
OFF for all other open modes. SEND returns the QUICKSCAN setting (ON or OFF) in the form of 
a STRING(3). 
 
 
TAB-delimited values are a common format compatible with the Windows clipboard. Using 
the BASIC file driver string 
/COMMA=9 lets you read Windows clipboard files 


---

Database Drivers 
20 
## QUOTE
 
DRIVER('BASIC', '/QUOTE = n' ) 
[ Quote" = ] SEND(file, 'QUOTE [ = n ]' ) 
Specifies a single character string delimiter.  
n is the ANSI code of the delimiter character. The default is 34, the ASCII value for the quotation 
mark. 
SEND returns the ASCII code of the single character string delimiter. 
Popular File Formats 
The following demonstrates how to use the driver strings to create two popular file formats: 
Microsoft Word for Windows Mail Merge: 
## /ALWAYSQUOTE=OFF
## /FIELDDELIMITER=1,9
## /ENDOFRECORD=1,13
 
TAB delimited format: 
## /COMMA=9
 


---

Database Drivers and Interfaces 
21 
Basic:Supported Commands and Attributes 
 
 
File Attributes 
Supported 
 
## CREATE
Y 
 
DRIVER(filetype [,driver string]) 
Y 
 
## NAME
Y 
 
## ENCRYPT
N 
 
OWNER(password) 
N 
 
## RECLAIM
N 
 
PRE(prefix) 
Y 
 
## BINDABLE
Y 
 
## THREAD
Y4 
 
EXTERNAL(member) 
Y 
 
DLL([flag]) 
Y 
 
OEM 
Y 
 
## LOCALE
N 
 
File Structures 
Supported 
 
## INDEX
N 
 
KEY 
N 
 
## MEMO
N 
 
## BLOB
N 
 
## RECORD
Y 
 
 
Index, Key, Memo, Attributes  
Supported 
 
## BINARY
N 
 
DUP 
N 
 
## NOCASE
N 
 
OPT 
N 
 
## PRIMARY
N 


---

Database Drivers 
22 
 
## NAME
N 
 
Ascending Components 
N 
 
Descending Components 
N 
 
Mixed Components 
N 
 
 
Field Attributes 
Supported 
 
DIM 
Y 
 
## OVER
Y 
 
## NAME
Y 
 
 
File Procedures 
Supported 
 
BOF(file) 
N 
 
BUFFER(file) 
N 
 
BUILD(file) 
N 
 
BUILD(key) 
N 
 
BUILD(index) 
N 
 
BUILD(index, components) 
N 
 
BUILD(index, components, filter) 
N 
 
BYTES(file) 
Y5 
 
CLOSE(file) 
Y 
 
COPY(file, new file) 
Y 
 
CREATE(file) 
Y 
 
DUPLICATE(file) 
N 
 
DUPLICATE(key) 
N 
 
EMPTY(file) 
Y 
 
EOF(file) 
Y 
 
FLUSH(file) 
N 
 
LOCK(file) 
Y 
 
NAME(label) 
Y 


---

Database Drivers and Interfaces 
23 
 
OPEN(file, access mode) 
Y 
 
PACK(file) 
N 
 
POINTER(file) 
Y2 
 
POINTER(key) 
N 
 
POSITION(file) 
Y3 
 
POSITION(key) 
N 
 
RECORDS(file) 
N 
 
RECORDS(key) 
N 
 
REMOVE(file) 
Y 
 
RENAME(file, new file) 
Y 
 
SEND(file, message) 
Y 
 
SHARE(file, access mode) 
Y 
 
STATUS(file) 
Y 
 
STREAM(file) 
N 
 
UNLOCK(file) 
Y 
 
 
Record Access 
Supported 
 
ADD(file) 
Y 
 
ADD(file, length) 
N 
 
APPEND(file) 
Y 
 
APPEND(file, length) 
N 
 
DELETE(file) 
N 
 
GET(file,key) 
N 
 
GET(file, filepointer) 
Y 
 
GET(file, filepointer, length) 
N 
 
GET(key, keypointer) 
N 
 
HOLD(file) 
N 
 
NEXT(file) 
Y 
 
NOMEMO(file) 
N 


---

Database Drivers 
24 
 
PREVIOUS(file) 
N 
 
PUT(file) 
Y1 
 
PUT(file, filepointer) 
Y1 
 
PUT(file, filepointer, length) 
N 
 
RELEASE(file) 
N 
 
REGET(file,string) 
Y 
 
REGET(key,string) 
N 
 
RESET(file,string) 
Y 
 
RESET(key,string) 
N 
 
SET(file) 
Y  
 
SET(file, key) 
N 
 
SET(file, filepointer) 
Y 
 
SET(key) 
N 
 
SET(key, key) 
N 
 
SET(key, keypointer) 
N 
 
SET(key, key, filepointer) 
N 
 
SKIP(file, count) 
N 
 
WATCH(file) 
N 
 
 
Transaction Processing 
Supported 
 
LOGOUT(timeout, file, ..., file) 
N 
 
## COMMIT
N 
 
## ROLLBACK
N 
 
 
Null Data Processing 
Supported 
 
NULL(field) 
N 
 
SETNULL(field) 
N 
 
SETNULL(file, field) 
N 
 
SETNONNULL(field) 
N 


---

Database Drivers and Interfaces 
25 
Notes 
1 
When using PUT() with this driver you should take care to PUT back the same number of 
characters that were read. If you PUT back more characters than were read, then the 
"extra" characters will overwrite the first part of the subsequent record. If you PUT back 
fewer characters than were read, then only the first part of the retrieved record is 
overwritten, while the last part of the retrieved record remains as it was prior to the PUT(). 
2 
POINTER() returns the relative byte position within the file. 
3 
POSITION(file) returns a STRING(4). 
4 
THREADed files consume additional file handles for each thread that accesses the file. 
5 
BYTES() returns the actual bytes read from the file. The size of the clipped RECORD 
may be different depending on the file driver and it's DRIVER() strings. With the ASCII or 
BASIC file drivers BYTES will include the ENDOFRECORD (typically 13,10) byte count, 
but these bytes are not in the RECORD. With the ASCII driver the /TAB driver string can 
affect (expand, change or remove) the tab (9) characters in the record buffer resulting in 
a different length. 
 


---

Database Drivers 
26 
Btrieve Database Driver 
 
 Btrieve:Specifications 
This file driver reads and writes Btrieve files using low-level direct access.  
Under Clarion, the Btrieve file driver is implemented by using .DLLs and an .EXE supplied by 
Pervasive Software (formerly Btrieve Technologies, Inc.). For an application to use a Btrieve file 
driver, the following files must accompany the executable: 
You must purchase a 32-bit Btrieve engine from Pervasive Software. 
LICENSE WARNING: A registered Clarion owner cannot redistribute the above files 
outside of his/her organization without a license from Pervasive Software.  
 
Files: 
## CLABTRL.LIB
Windows Static Link Library 
 
## CLABTR.LIB
Windows Export Library 
 
## CLABTR.DLL
Windows Dynamic Link Library 
Btrieve:Data Types 
Clarion data type 
Btrieve data type 
## BYTE
STRING (1 byte) 
## SHORT
INTEGER (2 bytes) 
## LONG
INTEGER (4 bytes) 
## SREAL
FLOAT (4 bytes) 
## REAL
FLOAT (8 bytes) 
## BFLOAT4
BFLOAT (4 bytes) 
## BFLOAT8
BFLOAT (8 bytes) 
## PDECIMAL
## DECIMAL
## STRING
## STRING
## CSTRING
## ZSTRING
## PSTRING
## LSTRING
## DATE
## DATE
## TIME
## TIME
## USHORT
UNSIGNED BINARY (2 bytes) 
## ULONG
UNSIGNED BINARY (4 bytes) 
## MEMO
STRING,LVAR or NOTE  
(see /MEMO below) 
## BYTE,NAME('LOGICAL')
## LOGICAL*
## USHORT,NAME('LOGICAL')
## LOGICAL*
## PDECIMAL,NAME('MONEY')
## MONEY*
STRING(@N0n-),NAME('STS') 
## SIGNED TRAILING SEPARATE*
## DECIMAL*
 
Notes: 
*You can store Clarion DECIMAL types in a Btrieve file. However, you cannot build a key or 
index using the field. This is provided for backward compatibility with older Clarion programs 
which used the Btrieve LEM. If you need standard Btrieve decimal data that is compatible with 
any other Btrieve compliant program, you should use the PDECIMAL data type and not the 
DECIMAL data type. 


---

Database Drivers and Interfaces 
27 
*If you want to create a file with LOGICAL or MONEY field types, you must specify LOGICAL 
or MONEY in the field's NAME attribute. If you are accessing an existing file, the NAME 
attribute is not required.  
*LOGICAL may be declared as a BYTE or USHORT, depending on whether it is a one or two 
byte LOGICAL: 
    LogicalField1  BYTE    !One byte LOGICAL 
    LogicalField2  USHORT  !Two byte LOGICAL 
*MONEY may be declared as a PDECIMAL(x,2), where x is the total number of digits to be 
stored: 
    MoneyField  PDECIMAL(7,2),NAME('MONEY') !Store up to 99999.99 
*Btrieve NUMERIC fields are not fully supported by the driver. Btrieve NUMERIC is stored as a 
string with the last character holding a digit and an implied sign. The possible values for this 
last character are: 
            1 2 3 4 5 6 7 8 9 0 
Positive:   A B C D E F G H I { 
Negative:   J K L M N O P Q R } 
*To access a NUMERIC field you must define a STRING(@N0x), where x is one less than the 
digits in the NUMERIC, and a STRING(1) to hold the sign indicator. The Btrieve driver does not 
maintain this sign field, the application must be written to directly handle it. 
*For example to access a NUMERIC(7) you would have: 
NumericGroup GROUP         !Store -999999 to 999999 
Number        STRING(@N06) !Numbers 
Sign          STRING(1)    !Sign indicator 
             END 


---

Database Drivers 
28 
 Btrieve:File Specifications/Maximums 
 
The specifications below document Version 6.15. Your specific limits are dependant on what 
version of Btrieve you are using, and are not dependant on the Btrieve driver. Refer to your 
Btrieve documentation for your specific limitations. 
 
File Size :            4,000,000,000 bytes 
Records per File :     Limited by the size of the file 
Record Size 
 Client-based :        65,535 bytes variable length 
 Server based :        57,000 bytes variable length 
Field Size :           65,520 bytes 
Fields per Record:     65,520 
Keys/Indexes per File: 24 with NLM5 
                       256 with NLM6. 
Client Btrieve v6.15  
Page Size    Max Key Segments 
512               8 
1,024             23 
1,536             24 
2,048             54 
4,096             119 
 
This is the total number of components. If you have a multi
component key built from three fields, this counts as three
indexes when counting the number of allowed indexes. 
 
Key Size :            255 bytes 
Memo fields per File: System memory dependent 
Memo field size :     65,520 bytes 
Open Files :          Operating system dependent 
 
 
 
The Btrieve driver supports data only and key only files. 
 


---

Database Drivers and Interfaces 
29 
Btrieve:Driver Strings 
There are switches or "driver strings" you can set to control the way your application creates, 
reads, and writes files with a specific driver. Driver strings are simply messages or parameters 
that are sent to the file driver at run-time to control its behavior. See Common Driver Features--
Driver Strings for an overview of these runtime Database Driver switches and parameters. 
The Btrieve Driver supports the following Driver Strings: 
ACS 
 
DRIVER('BTRIEVE', '/ACS = filename' ) 
[ SortSeq" = ] SEND(file, 'ACS [ = filename ]' ) 
When creating a Btrieve file you can specify an alternate collating sequence for sorting STRING 
keys. This sorting sequence is normally obtained from the sort sequence you define in the INI file 
for your program. However, Btrieve supplies files for doing case insensitive sorts. To create your 
file using these sort sequences you specify the name of the sort file in the driver string. 
## ALLOWREAD
 
## DRIVER('BTRIEVE', '/ALLOWREAD = ON | OFF' )
[ Read" = ] SEND(file, 'ALLOWREAD [ = ON | OFF ]' ) 
By default, a Btrieve file created with an owner name may be accessed only in read-only mode 
when the owner name is not known. To prevent all access to the file without the owner name, set 
ALLOWREAD to OFF. SEND returns the ALLOWREAD setting (ON or OFF) in the form of a 
## STRING(3).
## APPENDBUFFER
 
DRIVER('BTRIEVE', '/APPENDBUFFER = size ' ) 
[ Buffer" = ] SEND(file, 'APPENDBUFFER [ = size ]' ) 
By default, APPEND adds records to the file one at a time. To get better performance over a 
network you can tell the driver to build up a buffer of records then send all of them to Btrieve at 
once. Size is the number of records you want to allocate for the buffer. SEND returns the number 
of records that will fit in the buffer. 
## BALANCEKEYS
 
## DRIVER('BTRIEVE', '/BALANCEKEYS = ON | OFF' )
[ Balance" = ] SEND(file, 'BALANCEKEYS [ = ON | OFF ]' ) 
When creating a Btrieve file, you can use this driver string to tell Btrieve that all keys associated 
with the file must be stored in a balanced btree. This saves disk space, but will slow down file 
adds, deletes and updates where key values change. SEND returns the BALANCEKEYS setting 
(ON or OFF) in the form of a STRING(3). 


---

Database Drivers 
30 
## COMPRESS
 
## DRIVER('BTRIEVE', '/COMPRESS = ON | OFF' )
[ Read" = ] SEND(file, 'COMPRESS [ = ON | OFF ]' ) 
Btrieve lets you compress the data before storage. This allows for a smaller storage requirement, 
but reduces performance. When COMPRESS is ON, CREATE creates a compressed Btrieve file. 
SEND returns the COMPRESS setting (ON or OFF) in the form of a STRING(3). 
## CLIENTID
 
DRIVER('BTRIEVE', '/CLIENTID = xx' ) 
[ Read" = ] SEND(file, 'CLIENTID = xx ' ) 
 
Btrieve allows you to specify the Client ID used in the Btrieve APIs to uniquely identify a client 
application.  This can be used to help monitor Btrieve activity as well as avoid a deadlock 
situation inside the MicroKernel if multiple threads access the MicroKernel simultaneously. 
 
To set the Client ID, add /CLIENTID=xx to the driver string for the first Btrieve file that you use. 
 
xx is the ID you want to set.  This is limited to 2 characters.  The following character pairs should 
not be used: 
 
Used internally by the MicroKernel: 
@A 
## 0FFFFH
RI 
DR 
 
Used to identify clients originated by Scalable SQL: 
SE 
SC 
DC 
DE 
DU 
 
You can also use SEND before any file I/O to set this value. You can also use SEND to read the 
value. 
 
## FREESPACE
 
## DRIVER('BTRIEVE', '/FREESPACE = 0 | 10 | 20 | 30' )
[ Read" = ] SEND(file, 'FREESPACE [ = 0 | 10 | 20 | 30 ]' ) 
Specifies the percentage of free space to maintain on variable length pages. The default is zero. 
SEND returns the percentage of free space to maintain on variable length pages. 


---

Database Drivers and Interfaces 
31 
## LACS
 
DRIVER('BTRIEVE', '/LACS [ = | country_id,codepage ]' ) 
[ Sequence" = ] SEND(file, 'LACS [ = | country_id,codepage ]' ) 
Btrieve v6.15 and later offers the Local Alternate Collating Sequences feature. This allows your 
string keys to sort based on the country code for the machine running your program. To use this 
feature include '/LACS' in your driver string. 
LACS=country_ID,code_page {obsolete} 
You can also specify a User-Defined Alternate Collating Sequence. This allows your string key to 
sort based on the DOS country code and code page for a particular country. To use this feature 
you put '/LACS=country_id,codepage' in your driver string. Note that there must be no spaces 
surrounding the comma. 
SEND returns country_id,codepage or the string ',' if using the Local Alternate Collating 
Sequences feature. 
 
This driver switch has been replaced by the LOCALE attribute 
 
## MEMO
 
DRIVER('BTRIEVE', '/MEMO = SINGLE | LVAR | NOTE [,delimiter]' ) 
[ Memo" = ] SEND(file, 'MEMO [ =  SINGLE | LVAR | NOTE [,delimiter]]' ) 
## /MEMO=SINGLE
To access existing Btrieve files created with the Btrieve LEM from Clarion Professional Developer 
2.1(DOS), or files with variable length records set MEMO to SINGLE. 
To access a file with variable length records, use a SINGLE style MEMO whose size equals the maximum size 
of the variable length component of the record. To add/put records to this style file with binary data stored in the 
variable length section, use the ADD(file,length), APPEND(file,length) and PUT(file,pos,length) functions. The 
driver ignores the pos parameter in the PUT function, but initialize it to 0 (zero) for future compatibility. The ADD, 
APPEND or PUT functions will remove all trailing spaces for text memos and NULL characters for binary memos 
before storing the record. 
## /MEMO=LVAR
/MEMO=NOTE,<delimiter> 
To access Xtrieve data files that have data type of Note or LVar, set the driver string to NOTE 
and LVAR respectively. With the NOTE data type, specify the end-of-field delimiter. Specify the 
ASCII value for the delimiter. NOTE and LVAR memos do not require the use of the size variants 
of ADD, APPEND and PUT, when storing records. The end of record marker is not necessary for 
a NOTE style memo. The driver automatically adds the end of record marker before storing the 
record and removes it before putting the memo data into the memo buffer. 
As an example, "/MEMO=NOTE,141" indicates a file with an Xtrieve Notes field using CR/LF as 
the delimiter. For more information on the Xtrieve data types refer to the documentation supplied 
by Novell. 
SEND(file,'MEMO') 


---

Database Drivers 
32 
Returns the MEMO setting: NORMAL, NOTE, LVAR, or SINGLE. 
## NULLPDECIMALS
## DRIVER('BTRIEVE', '/NULLPDECIMALS = ON|OFF' )
[ PSize" = ] SEND(file, NULLPDECIMALS = ON|OFF') 
A PDECIMAL field has two different values for 0, the sign nibble can be either 0FH or 0.  Clarion 
normally uses a sign nibble of 0FH.  However, if you define a key in Btrieve with the OPT attribute 
and this key has a PDECIMAL component, then Btrieve requires that the sign nibble be 0.  The 
Btrieve file driver detects these situations and automatically converts the sign nibble to and from 
0FH as required.  The driver does this conversion only for PDECIMAL fields that are components 
of a key with the OPT attribute.  If you want to force the driver to do this conversion work for all 
PDECIMAL fields you can set NULLPDECIMAL=ON.  Your program will run fractionally slower, 
but you will not have problems in the future if you decide to add an OPT key on that field.  If you 
do not set this switch to on you later decide to add an OPT key, then you will need to add this 
driver string to your file, read every record in the file and write it out again to make sure the 0 
nibble is set. 
## PAGESIZE
 
## DRIVER('BTRIEVE', '/PAGESIZE = SIZE' )
[ PSize" = ] SEND(file, 'PAGESIZE[=SIZE]' ) 
Sets the Btrieve Page size at file creation time. The size must be a multiple of 512, with a 
maximum of 4096. Larger page sizes usually result in more efficient disk storage. 
SEND returns the page size setting. 
## PREALLOCATE
 
DRIVER('BTRIEVE', '/PREALLOCATE = n' ) 
[ Read" = ] SEND(file, 'PREALLOCATE [ = n ]' ) 
When creating a Btrieve file, you can preallocate n pages of disk space for the file. The default is 
zero. SEND returns the number of pages of allocated disk space. 
## TRUNCATE
 
## DRIVER('BTRIEVE', '/TRUNCATE  = ON | OFF' )
[ Trunc" = ] SEND(file, 'TRUNCATE [ = ON | OFF ]' ) 
When creating a Btrieve file, you can use this driver string to tell Btrieve to truncate trailing 
spaces. This forces the record to be stored as a variable length record. SEND returns the 
TRUNCATE setting (ON or OFF) in the form of a STRING(3). 
 Btrieve:Driver Properties 
You can use Clarion's property syntax to query and set certain driver properties. These properties 
are described below. 
PROP:PageLevelLocking 
PROP:PageLevelLocking sets the type of locking the driver uses with LOGOUT. The driver uses 
either page or file level locking schemes. Set to PageLevelLocking by setting the property to '1'. 
This is the default. To set the driver to file level locking, set the property to ''.  


---

Database Drivers and Interfaces 
33 
MyFile{PROP:PageLevelLocking} = '1'      !Set Page level locking 
MyFile{PROP:PageLevelLocking} = ''       !Set File level locking 
loc:lock = MyFile{PROP:PageLevelLocking} !read locking scheme 


---

Database Drivers 
34 
PROP:PositionBlock 
PROP:PositionBlock returns the Btrieve pointer to the Btrieve position block used by the Btrieve 
driver for the named file. This allows you to call Btrieve operations directly. For example:  
  MAP 
  MODULE('Btrieve') 
## BTRV(USHORT,LONG,<*STRING>,*UNSIGNED,<*STRING>,BYTE,BYTE),|
## NAME('BTRV'),PASCAL,RAW
    END 
  END 
 
StatData STRING(33455) 
KeyData  STRING(64) 
DataLen  UNSIGNED(33455) 
 
## CODE
 PosBlock = file{PROP:PositionBlock} 
 BTRV(15,PosBlock,StatData,DataLen,KeyData,64,0)  !Get file statistics 
 


---

Database Drivers and Interfaces 
35 
Btrieve:Supported Commands and Attributes 
 
File Attributes 
Supported 
 
## CREATE
Y 
 
DRIVER(filetype [,driver string]) 
Y 
 
## NAME
Y 
 
## ENCRYPT
Y 
 
OWNER(password) 
Y1 
 
## RECLAIM
Y 
 
PRE(prefix) 
Y 
 
## BINDABLE
Y 
 
## THREAD
Y15 
 
EXTERNAL(member) 
Y 
 
DLL([flag]) 
Y 
 
OEM 
Y 
 
## LOCALE
Y17 
 
File Structures 
Supported 
 
## INDEX
Y 
 
KEY 
Y 
 
## MEMO
Y2 
 
## BLOB
N 
 
## RECORD
Y 
 
Index, Key, Memo Attributes 
Supported 
 
## BINARY
Y16 
 
DUP 
Y 
 
## NOCASE
Y 
 
OPT 
Y 
 
## PRIMARY
Y 
 
## NAME
Y2 
 
Ascending Components 
Y 


---

Database Drivers 
36 
 
Descending Components 
Y 
 
Mixed Components 
Y 
 
Field Attributes 
Supported 
 
DIM 
Y 
 
## OVER
Y 
 
## NAME
Y 
 
File Procedures 
Supported 
 
BOF(file) 
Y10 
 
BUFFER(file) 
N 
 
BUILD(file) 
Y3 
 
BUILD(key) 
Y3 
 
BUILD(index) 
Y3 
 
BUILD(index, components) 
Y3 
 
BUILD(index, components, filter) 
N 
 
BYTES(file) 
N 
 
CLOSE(file) 
Y 
 
COPY(file, new file) 
Y 
 
CREATE(file) 
Y 
 
DUPLICATE(file) 
Y 
 
DUPLICATE(key) 
Y 
 
EMPTY(file) 
Y 
 
EOF(file) 
Y10 
 
FLUSH(file) 
N 
 
LOCK(file) 
N4 
 
NAME(label) 
Y 
 
OPEN(file, access mode) 
Y 
 
PACK(file) 
Y 
 
POINTER(file) 
Y11 
 
POINTER(key) 
Y11 


---

Database Drivers and Interfaces 
37 
 
POSITION(file) 
Y12 
 
POSITION(key) 
Y12 
 
RECORDS(file) 
Y 
 
RECORDS(key) 
Y 
 
REMOVE(file) 
Y 
 
RENAME(file, new file) 
Y 
 
SEND(file, message) 
Y 
 
SHARE(file, access mode) 
Y 
 
STATUS(file) 
Y 
 
STREAM(file) 
Y 
 
UNLOCK(file) 
N 
 
Record Access 
Supported 
 
ADD(file) 
Y5 
 
ADD(file, length) 
Y5 
 
APPEND(file) 
Y6 
 
APPEND(file, length) 
## Y5,6
 
DELETE(file) 
Y7 
 
GET(file,key) 
Y 
 
GET(file, filepointer) 
Y 
 
GET(file, filepointer, length) 
N 
 
GET(key, keypointer) 
Y 
 
HOLD(file) 
Y 
 
NEXT(file) 
Y 
 
NOMEMO(file) 
Y 
 
PREVIOUS(file) 
Y 
 
PUT(file) 
Y5 
 
PUT(file, filepointer) 
N 
 
PUT(file, filepointer, length) 
Y 


---

Database Drivers 
38 
 
RELEASE(file) 
Y 
 
REGET(file,string) 
Y 
 
REGET(key,string) 
Y 
 
RESET(file,string) 
Y 
 
RESET(key,string) 
Y 
 
SET(file) 
Y  
 
SET(file, key) 
Y 
 
SET(file, filepointer) 
Y8 
 
SET(key) 
Y 
 
SET(key, key) 
Y 
 
SET(key, keypointer) 
Y8 
 
SET(key, key, filepointer) 
Y9 
 
SKIP(file, count) 
Y 
 
WATCH(file) 
Y 
 
Transaction Processing 
Supported 
 
LOGOUT(timeout, file, ..., file) 
## Y13,14
 
## COMMIT
Y14 
 
## ROLLBACK
Y 
 
Null Data Processing 
Supported 
 
NULL(field) 
N 
 
SETNULL(field) 
N 
 
SETNULL(file,field) 
N 
 
SETNONNULL(field) 
N 
Notes 
1      We recommend using a variable password that is lengthy and contains special characters 
because this more effectively hides the password value from anyone looking for it. For 
example, a password like "dd....#$...*&" is much more difficult to "find" than a password 
like "SALARY." 
 
 
To specify a variable instead of the actual password in the Owner Name field of the 


---

Database Drivers and Interfaces 
39 
File Properties dialog, type an exclamation point (!) followed by the variable name. 
For example: !MyPassword. 
2      The driver ignores any NAME attribute on a MEMO field. MEMO fields can reside either in 
a separate file, or in the data file if the driver string /MEMO is set to SINGLE, LVAR or 
NOTE. If the driver string /MEMO is not set, the separate MEMO file name is "MEM," 
preceded by the first five characters of the file's label, plus the file extension ".DAT." 
Setting the driver string /MEMO restricts you to one memo field per file. 
3      If used after an APPEND(), but before a file is closed, this adds the keys dropped by 
APPEND(). In all other cases BUILD() rebuilds the file and keys. If you only want to 
rebuild keys, doing a BUILD(key) for each key is faster than BUILD(file). 
4      Btrieve does not directly support file locking. If you require file locking, use LOGOUT. 
5      When using the LVAR and NOTE memo type, make certain that the memo has the 
appropriate structure. If the structure is incorrect and the driver calculates a length 
greater than the maximum memo size defined for that file, these functions fail and set 
errorcode to 57 - Invalid Memo File. 
6      Btrieve does not support non-key updates. To emulate APPEND() behavior, the driver 
drops all indexes possible when APPEND() is first called. Calling BUILD() immediately 
after appending records rebuilds the dropped key fields. 
7      Btrieve's DELETE destroys positioning information when processing in file order. The 
driver attempts to reposition to the appropriate record. This is not always possible and 
may require the driver to read from the start of the file. Using key order processing avoids 
this possible slow down. 
8      If a file pointer or key pointer has a value of zero, the driver ignores the pointer parameter. 
Processing is set to either file or key order, and the record pointer is set to the first 
element. 
9      If the file pointer has a value of zero, processing starts at the first key value whose 
position is greater than (or less than for PREVIOUS) the file pointer. Not passing a valid 
pointer, other than maximum LONG or maximum ULONG, is inefficient.  
10     These functions are supported, but not recommended. They cause more disk I/O than 
ERRORCODE(). Btrieve returns eof when reading past the last record. Therefore, the 
driver must read the next record, then the next to see if it's at the end of file, then return 
to the record you want. 
11     POINTER() returns a relative position within the file, not a record number. 
12     POSITION(file) returns a STRING(4). POSITION(key) returns a STRING the size of the 
key fields + 4 bytes. 
13     If a system crashes during a transaction (LOGOUT--COMMIT), the recovery is 
automatically handled by the Btrieve driver the next time the affected file is accessed. 
When you issue a LOGOUT, all Btrieve files accessed during the transaction are logged 
out. The following code is illegal because you cannot close a logged-out file: 
  LOGOUT(1,file1) 
  OPEN(file1) 
  CLOSE(file1) 
14     See also PROP:Logout in the Language Reference. 
15     THREADed files do not consume additional file handles for each thread that accesses 
the file. 
16     OEM conversion is not applied to BINARY MEMOs. The driver assumes BINARY 
MEMOs are zero padded; otherwise, space padded. 


---

Database Drivers 
40 
17 
LOCALE only effects the CREATE statement.  Below is a list of locale/code page pairs 
supported by Btrieve.  If one of these pairs is set, then the CREATE statement will create 
a Btrieve ISR ACS.  See Pervasive SQL’s documentation on ISR for more information. 
Any English Locale 
 
437 MS-DOS Latin-US 
850 MS-DOS-Latin-1 
Any French Locale 
437 MS-DOS Latin-US 
850 MS-DOS-Latin-1 
Any German Locale 
437 MS-DOS Latin-US 
850 MS-DOS-Latin-1 
Any Spanish Locale 
437 MS-DOS Latin-US 
850 MS-DOS-Latin-1 
Any Japanese Locale 
932 Shift-JIS 
 
 
Btrieve:Other 
Client/Server 
For Client/Server-based Btrieve, Netware Btrieve is a server-based version of Btrieve that runs on 
a Novell server. 
Collating Sequence 
NOCASE Key Attribute 
NLM 5 does not support case insensitive indexing. When necessary, you must supply an 
alternate collating sequence which implements case insensitive sorting. 
Btrieve supports an alternate collating sequence. However, NLM 6 does not support both 
NOCASE and an alternate collating sequence. If you specify both, the NOCASE attribute takes 
precedence. No error is returned fromThe SEND function. 
Changing the Collating Sequence 
Btrieve stores the collating sequence inside the file. So to change the collating sequence you 
have to change the .ENV file, then create a new Btrieve file based on the modified .ENV file, 
then copy the data from the old file to the new file. 
Error Codes 
All Btrieve error codes up to 2007 are now mapped to appropriate error messages.  
File Sharing 
Btrieve lets you open a file in five different formats: NORMAL, ACCELERATED, READ-ONLY, 
VERIFY, or EXCLUSIVE. The equivalent Clarion OPEN() states are: 
Btrieve State   Clarion OPEN/SHARE access mode 
ACCELERATED     Read/Write with FCB compatibility mode (2H) 
READ-ONLY       Read Only  (0H,10H,20H,30H,40H) 
VERIFY          Write Only with FCB compatibility mode (1H) 
EXCLUSIVE       Write Only with any Deny flag (11H,21H,31H,41H); 
                Read/Write with Deny All, Read or Write (12H,22H,32H) 
NORMAL          Read/Write with Deny None (42H) 
Btrieve allows a file to have a specified owner. See the /READONLY driver string for details on 
setting this flag. The file may also be encrypted with the ENCRYPT attribute. A file can only be 
encrypted when an owner name is supplied. 


---

Database Drivers and Interfaces 
41 
File Structure 
A single file normally holds the data and all keys. Data filenames default to a *.DAT file extension. 
By default, the driver stores memos in a separate file, or optionally in the data file itself, given the 
appropriate driver string. 
Because Btrieve is a data-model independent, indexed record manager, it does not store field 
definitions within the data itself. The application accessing the data determines how to interpret 
the Btrieve record. Absent .DDF files describing the Btrieve file, it is very difficult for an application 
that does not create or maintain the file to meaningfully interpret its data. 
The Btrieve file format stores minimal file structure information in the file. As far as possible, the 
driver validates your description against the information in the file. However, it is possible to 
successfully open a Btrieve file that has key definitions that do not exactly match your definition. 
You must make certain that your file and key definitions accurately match the Btrieve file. 


---

Database Drivers 
42 
KEY Definitions 
When defining a file, the key definition does not need to exactly match the underlying file. For 
example, you can have a physical file with a single component STRING(20). You can define 
this as a key with two string components with a total length of 20. The rule is that the data 
types must match and the total size must match. However, if your Clarion definition does not 
exactly match the underlying file, the driver cannot optimize APPEND() or BUILD() statements. 
A Key's NAME attribute can add additional functionality. 
KEY,NAME('MODIFIABLE=true|false') 
Btrieve lets you create a key that cannot be changed once created. To use this feature you can 
use the name attribute on the key to set MODIFIABLE to FALSE. It defaults to TRUE. 
## KEY,NAME('ANYNULL')
Btrieve lets you create a key that will not include a record if any key components are null. To 
create such a key you specify ANYNULL in the key name. 
For example, to create a key that is non-modifiable and excludes keys if any component is null: 
    Key1   KEY(+pre:field1,-pre:field2),NAME('ANYNULL MODIFIABLE=FALSE') 
## KEY,NAME('AUTOINCREMENT')
The Clarion CREATE statement creates a Btrieve autoincrement key.  The key must have 1 
key component of type LONG. 
## KEY,NAME('REPEATINGDUPLICATE')
By default Btrieve version 6 stores a reference to only the first record in a series of duplicate 
records in a key. The other occurrences of the duplicate key value are obtained by following a 
link list stored at the record. To create an index where all duplicate records are stored in the 
key you use the NAME('REPEATINGDUPLICATE'). This produces larger keys, but random 
access to duplicate records is faster (this feature is only available for version 6 files). 
Keys and Indexes 
KEYs are dynamic, and automatically update when the data file changes.  
INDEXes are stored separately from data files. INDEX files receive a temporary file name, and 
are deleted when the program terminates normally. INDEXes are static--they are not 
automatically updated when the data file changes. The BUILD statement creates or updates 
index files. 
Page Size 
To determine the physical record length, add 8 bytes for each KEY that allows duplicates. Add 4 
bytes if the file allows variable record lengths. Finally, allow 6 bytes for overhead per page. 
For example: If the record size is 300 bytes and the file has three KEYs that allow Duplicates, the 
total record size is: 
 
 
300 
record size  
 
x 
24 
overhead for three KEYs with the DUP attribute 
 
= 
324 
physical record length 
A page size of 512 would only hold one such record, and 182 bytes per page would go unused 
(512 - 6 - 324). If the page size were 1024, three records could be stored per page and only 46 
bytes would go unused (1024 - 6 - (324 * 3)). 


---

Database Drivers and Interfaces 
43 
You must load BTRIEVE.EXE with a page size equal to or greater than the largest page size of 
any file that you will be accessing. 
Record Lengths 
The driver stores records less than 4K as fixed length. It stores records greater than 4K as 
variable length. The minimum record length is 4 bytes. One record can be held in each open file 
by each user. 
Record Pointers 
Btrieve uses an unsigned long for its internal record pointer; negative values are stripped of their 
sign. We recommend the ULONG data type for your record pointer. 
Transaction Framing 
You cannot create files inside a transaction frame with Btrieve.  This means that if you have 
"Defer opening files until accessed" template option checked in your applications, you must make 
sure that all files exist before entering transaction frames (initiated with LOGOUT).  The easiest 
way to ensure this is that on startup of an application, it should detect if a file exists, and if it does 
not, then create a routine that creates the files as needed (by simply calling FileManager.Open for 
all the files). 
 


---

Database Drivers 
44 
Clarion Database Driver 
 Clarion:Specifications 
The Clarion file driver is compatible with the file system used by Clarion for DOS 3.1 and Clarion 
Professional Developer 2.1, patch 2.109 and later. 
Keys and Indexes exist as separate files from the data file. Keys are dynamic--they are 
automatically updated as the data file changes. The default file extension for a key file is *.K##. 
Indexes are static--they do not automatically update, but instead require the BUILD statement for 
updating. 
The driver stores records as fixed length. It stores memo fields in a separate file. The memo file 
defaults to the first eight characters of the File Label plus an extension of .MEM. 
Files: 
## CLACLAL.LIB
Windows Static Link Library 
 
## CLACLA.LIB
Windows Export Library 
 
## CLACLA.DLL
Windows Dynamic Link Library 
 
By avoiding the ASCII-only file formats of many other popular PC database application 
development systems, the Clarion file format provides a more secure means of storing 
data. 
 Clarion:Data Types 
## BYTE
## DECIMAL
SHORT STRING(255 byte maximum) 
## LONG
## MEMO
## REAL
## GROUP
 Clarion:File Specifications/Maximums 
File Size:              4,294,967,295 
Records per File :      4,294,967,295 
Record Size:            65,520 bytes  
Field Size :            65,520 bytes 
Field Name:             12 characters  
Fields per Record:      65,520 
Keys/Indexes per File:  251 
Key Size:               245 bytes 
Memo fields per File :  1 
Memo Field Size:        65,520 bytes  
Open Data Files:        Operating system dependent 
 
A Clarion file name (including path) cannot be longer than 79 characters. 


---

Database Drivers and Interfaces 
45 
Clarion:Driver Strings 
There are switches or "driver strings" you can set to control the way your application creates, 
reads, and writes files with a specific driver. Driver strings are simply messages or parameters 
that are sent to the file driver at run-time to control its behavior. See Common Driver Features--
Driver Strings for an overview of these runtime Database Driver switches. 
 
 
Some driver strings have no effect after the file is open, so no SEND function 
syntax is listed for those strings. However, the SEND function syntax to return the 
value of the switch is listed for all driver strings.  
The Clarion Driver supports the following Driver Strings: 
## DELETED
 
SEND(file, 'DELETED') 
For use only with the SEND command when IGNORESTATUS is on. Reports the status of the 
loaded record. If deleted, the return string is "ON" and if not "OFF."  
## HELD
 
SEND(file, 'HELD') 
For use only with the SEND command when IGNORESTATUS is on. Reports the status of the 
loaded record. If held, the return string is "ON" and if not "OFF."  
## IGNORESTATUS
 
DRIVER('Clarion', '/IGNORESTATUS = on | off' ) 
[ Status" = ] SEND(file, 'IGNORESTATUS [ = on | off ]' ) 
When set on, the driver does not skip deleted records when accessing the file with GET(), 
NEXT(), and PREVIOUS() in file order. It also enables a PUT() on a deleted or held record. 
IGNORESTATUS requires opening the file in exclusive mode. However, any MEMO data of the 
deleted records is not recoverable. SEND returns the IGNORESTATUS setting (ON or OFF) in 
the form of a STRING(3). 
## MAINTAINHEADERTIME
 
DRIVER('Clarion', '/MAINTAINHEADERTIME = on | off' ) 
[ Status" = ] SEND(file, 'MAINTAINHEADERTIME [ = on | off ]' ) 
When set on, the driver maintains the file header time stamp (last updated) under all 
circumstances. When set to off (the default), the driver improves performance by ignoring the 
time stamp under some circumstances. SEND returns the MAINTAINHEADERTIME setting (ON 
or OFF) in the form of a STRING(3). 
## RECOVER
 
SEND(file, 'RECOVER = n' ) 


---

Database Drivers 
46 
The RECOVER string, when n is greater than 0, UNLOCKs data files, RELEASEs held records, 
and rolls back incomplete transactions in order to recover from a system crash. See also 
Transaction Processing for Clarion Files. 
n represents the number of seconds to wait before invoking the recovery process. When n is 
equal to 1, the recovery process is invoked immediately. When n is equal to 0, the recovery 
process is disarmed.  
There are two ways of using RECOVER: 
SEND(file, 'RECOVER=n') 
OPEN(file) 
This releases a LOCK on a file that was locked when a machine crashed. It also rolls back a 
transaction that was in process when a system crashed. 
SEND(file, 'RECOVER=n') 
GET or NEXT or PREVIOUS 
This removes a hold flag from records that where held when a machine crashed. Here is a piece 
of code that removes all hold flags from a file: 
OPEN(file)  !make sure no one else is using the file 
SEND(file,'IGNORESTATUS=ON') 
SET(file) 
## LOOP
 NEXT(file) 
## IF ERRORCODE()
## BREAK
 END 
 IF SEND(file,'HELD') = 'ON' THEN 
  SEND(file,'RECOVER=1') 
  REGET(file,POSITION(file)) 
 END 
END 
RECOVER may not be used as a DRIVER string--you may only use it with the SEND function. 
The SEND function returns a blank string. 
 


---

Database Drivers and Interfaces 
47 
Clarion:Supported Commands and Attributes 
 
File Attributes 
Supported 
 
## CREATE
Y 
 
DRIVER(filetype [,driver string]) 
Y 
 
## NAME
Y 
 
## ENCRYPT
Y 
 
OWNER(password) 
Y1 
 
## RECLAIM
Y 
 
PRE(prefix) 
Y 
 
## BINDABLE
Y 
 
## THREAD
Y8 
 
EXTERNAL(member) 
Y 
 
DLL([flag]) 
Y 
 
OEM 
Y 
 
## LOCALE
Y 
 
File Structures 
Supported 
 
## INDEX
Y 
 
KEY 
Y 
 
## MEMO
Y 
 
## BLOB
N 
 
## RECORD
Y 
 
Index, Key, Memo Attributes 
Supported 
 
## BINARY
Y9 
 
DUP 
Y 
 
## NOCASE
Y 
 
OPT 
Y 
 
## PRIMARY
Y 
 
## NAME
Y 


---

Database Drivers 
48 
 
Ascending Components 
Y 
 
Descending Components 
N 
 
Mixed Components 
N 
 
Field Attributes 
Supported 
 
DIM 
Y 
 
## OVER
Y 
 
## NAME
Y 
 
File Procedures 
Supported 
 
BOF(file) 
Y2 
 
BUFFER(file) 
N 
 
BUILD(file) 
Y 
 
BUILD(key) 
Y 
 
BUILD(index) 
Y 
 
BUILD(index, components) 
Y 
 
BUILD(index, components, filter) 
N 
 
BYTES(file) 
Y 
 
CLOSE(file) 
Y 
 
COPY(file, new file) 
Y 
 
CREATE(file) 
Y 
 
DUPLICATE(file) 
Y 
 
DUPLICATE(key) 
Y 
 
EMPTY(file) 
Y 
 
EOF(file) 
Y2 
 
FLUSH(file) 
Y 
 
LOCK(file) 
Y 
 
NAME(label) 
Y 
 
OPEN(file, access mode) 
Y 
 
PACK(file) 
Y 
 
POINTER(file) 
Y3 


---

Database Drivers and Interfaces 
49 
 
POINTER(key) 
Y3 
 
POSITION(file) 
Y4 
 
POSITION(key) 
Y4 
 
RECORDS(file) 
Y 
 
RECORDS(key) 
Y 
 
REMOVE(file) 
Y 
 
RENAME(file, new file) 
Y 
 
SEND(file, message) 
Y 
 
SHARE(file, access mode) 
Y 
 
STATUS(file) 
Y 
 
STREAM(file) 
Y 
 
UNLOCK(file) 
Y 
 
Record Access 
Supported 
 
ADD(file) 
Y10 
 
ADD(file, length) 
N 
 
APPEND(file) 
Y 
 
APPEND(file, length) 
N 
 
DELETE(file) 
Y 
 
GET(file,key) 
Y 
 
GET(file, filepointer) 
Y 
 
GET(file, filepointer, length) 
N 
 
GET(key, keypointer) 
Y 
 
HOLD(file) 
Y 
 
NEXT(file) 
Y 
 
NOMEMO(file) 
Y 
 
PREVIOUS(file) 
Y 
 
PUT(file) 
Y10 
 
PUT(file, filepointer) 
Y 


---

Database Drivers 
50 
 
PUT(file, filepointer, length) 
N 
 
RELEASE(file) 
Y 
 
REGET(file,string) 
Y 
 
REGET(key,string) 
Y 
 
RESET(file,string) 
Y 
 
RESET(key,string) 
Y 
 
SET(file) 
Y  
 
SET(file, key) 
Y 
 
SET(file, filepointer) 
Y 
 
SET(key) 
Y 
 
SET(key, key) 
Y 
 
SET(key, keypointer) 
Y 
 
SET(key, key, filepointer) 
Y 
 
SKIP(file, count) 
Y 
 
WATCH(file) 
Y 
 
Transaction Processing 
Supported5 
 
LOGOUT(timeout, file, ..., file) 
## Y6,7
 
## COMMIT
Y 
 
## ROLLBACK
Y 
 
Null Data Processing 
Supported 
 
NULL(field) 
N 
 
SETNULL(field) 
N 
 
SETNULL(file,field) 
N 
 
SETNONNULL(field) 
N 
 


---

Database Drivers and Interfaces 
51 
Notes 
1      We recommend using a variable password that is lengthy and contains special characters 
because this more effectively hides the password value from anyone looking for it. For 
example, a password like "dd....#$...*&" is much more difficult to "find" than a password 
like "SALARY." 
 
To specify a variable instead of the actual password in the Owner Name field of the 
File Properties dialog, type an exclamation point (!) followed by the variable name. 
For example: !MyPassword. 
2      These functions are supported but not recommended due to the lack of support in other 
file systems. NEXT and PREVIOUS post Error 33 if you attempt to read beyond the end 
of the file. 
3      POINTER() returns a record number. 
4      POSITION(file) returns a STRING(4). POSITION(key) returns a STRING the size of the 
key fields + 4 bytes. 
5      The RECOVER switch must be "armed" at the beginning of your program in order to 
support transaction processing. See Driver Strings for more information on the 
RECOVER function. 
6      LOGOUT has the effect of LOCKing the file. See also PROP:Logout in the Language 
Reference. 
7      You cannot LOGOUT an aliased file and its primary file at the same time.  
8      THREADed files consume additional file handles for each thread that accesses the file. 
9      OEM conversion is not applied to BINARY MEMOs. The driver assumes BINARY MEMOs 
are zero padded; otherwise, space padded. 
10     Prior to Clarion 2.003 in 16-bit programs under Microsoft operating systems, writes (ADD, 
PUT) did not correctly flush operating system buffers. This problem is corrected with 
Clarion 2.003 and higher, so that writes are slower but safer. To implement the pre 2.003 
behavior, use STREAM and FLUSH. 
 
Clarion:Other 
Transaction Processing for Clarion Files 
When you issue a LOGOUT statement the Clarion file driver creates a transaction file called 
programname.TR$. By default this file is created in the same directory as the program. To create 
the transaction file elsewhere, add a CWC21 section to the WIN.INI file as follows: 
## [CWC21]
CLATMP=path   
where path is a directory visible to all users. This statement  
PUTINI('CWC21','CLATMP',path) 
creates the correct .INI file section. 
During a transaction datafile.LOG files are created for each data file edited during the transaction. 
These LOG files always reside in the same directory as the data file. 
If a system crashes while a transaction is active, no user will be able to access the files until a 
recovery is run on the files. See the RECOVER send command on how to do this. 
LOGOUT has the effect of LOCKing the file. 


---

Database Drivers 
52 
Field Labels 
The Clarion driver only supports fully qualified field names (prefix + label) of 16 characters or 
less. That is, within the Clarion file (*.DAT) header, the driver truncates prefix + label to the first 
16 characters. If the first 16 characters are not unique, the truncation results in duplicate field 
names. 
Duplicate field names within the file header can cause problems with Clarion for DOS 2.1 and 
earlier. In addition, it can cause problems if you import the file definition from the Clarion file 
(*.DAT), then compile a Clarion application based on the imported file definition containing the 
duplicate field names. 
You can avoid duplicate field name problems by using the NAME attribute (the External Name 
field in the Data Dictionary's Field Properties dialog) to provide unique names for fields whose 
first 16 characters are duplicated. By providing unique names in the NAME attribute, your 
application can refer to the field by its (long) label, and the Clarion driver uses the unique NAME 
attribute to resolve conflicts. 


---

Database Drivers and Interfaces 
53 


---

Database Drivers 
54 
Clipper Database Driver 
 
Clipper:Specifications 
The Clipper file driver is compatible with Clipper Summer '87 and Clipper 5.0. The default data file 
extension is *.DBF. 
Keys and Indexes exist as separate files from the data file. Keys are dynamic--they automatically 
update as the data file changes. Indexes are static--they do not automatically update, but instead 
require the BUILD statement for updating. The default file extension for the index file is *.NTX. 
The driver stores records as fixed length. It stores memo fields in a separate file. The memo file 
name takes the first eight characters of the File Label plus an extension of .DBT. 
Files: 
## CLACLPL.LIB
Windows Static Link Library 
 
## CLACLP.LIB
Windows Export Library 
 
## CLACLP.DLL
Windows Dynamic Link Library 
 
 
As a popular xBase database application development system, Clipper provides a 
common file format for many installed business applications and their data files. Use the 
Clipper driver to access these files in their native format. 
 Clipper:Data Types 
The xBase file format stores all data as ASCII strings. You may either specify STRING types with 
declared pictures for each field, or specify native Clarion data types, which the driver converts 
automatically. 
Clipper data type 
Clarion data type 
STRING w/ picture 
Date 
## DATE
## STRING(@D12)
*Numeric 
## REAL
STRING(@N-_p.d) 
*Logical 
## BYTE
## STRING(1)
Character 
## STRING
## STRING
*Memo 
## MEMO
## MEMO
If your application reads and writes to existing files, a pictured STRING will suffice. However, if 
your application creates a Clipper file, you may require additional information for these Clipper 
types: 
*       To create a Numeric field in the Data Dictionary, choose the REAL data type. In the 
External Name field on the Attributes tab, specify 
'NumericFieldName=N(Precision,DecimalPlaces)' where NumericFieldName is the name 
of the field, Precision is the precision of the field and DecimalPlaces is the number of 
decimal places. With a REAL data type, you cannot access the Character or Places fields 
in the Field definition, you must specify those attributes with an expression in the External 
Name Field on the Attributes tab. 
For example, if you want to create a field called Number with nine significant digits and 
two decimal places, enter 'Number=N(9,2) in the External Name field on the Attributes 
tab of the Field properties in the Data Dictionary. 
If you're hand coding a native Clarion data type, add the NAME attribute using the same 
syntax.  


---

Database Drivers and Interfaces 
55 
If you're hand coding a STRING with picture, STRING(@N-_9.2), NAME('Number'), 
where Number is the field name. 
*      To create a logical field, using the data dictionary, choose the BYTE data type. There are 
no special steps; however, see the miscellaneous section for tips on reading the data 
from the field. 
If you're hand coding a STRING with picture, add the NAME attribute: STRING(1), 
NAME('LogFld = L'). 
*      To create a date field, using the data dictionary, choose the DATE data type, rather than 
LONG, which you usually use for the TopSpeed or Clarion file formats. 
*      MEMO field declarations require the a pointer field in the file's record structure. Declare 
the pointer field as a STRING(10) or a LONG. This field will be stored in the .DBF file 
containing the offset of the memo in the .DBT file. The MEMO declaration must have a 
NAME() attribute naming the pointer field. An example file declaration follows: 
File FILE, DRIVER('Clipper') 
Memo1  MEMO(200),NAME('Notes') 
Memo2  MEMO(200),NAME('Text') 
Rec    RECORD 
Mem1Ptr LONG,NAME('Notes') 
Mem2Ptr STRING(10),NAME('Text') 
       END 
     END 
 
 
Whenever possible, use the File Import Utility in the Dictionary Editor to define 
your files. 
Clipper:File Specifications/Maximums 
File Size:             2,000,000,000 bytes 
Records per File:      1,000,000,000  
Record Size:           4,000 bytes (Clipper '87) 
                       8,192 bytes (Clipper 5.0) 
Field Size 
     Character:        254 bytes (Clipper '87) 
                       2048 bytes (Clipper 5.0) 
     Date:             8 bytes 
     Logical:          1 byte 
     Numeric:          20 bytes including decimal point 
     Memo:             65,520 bytes (see note) 
Field Name:            10 characters 
Fields per Record:     1024 
Keys/Indexes per File: No Limit 
Key Sizes 
     Character:        100 bytes 
     Numeric, Date:    8 bytes 
Memo fields per File:  Dependent on available memory 
Open Files:            Operating system dependent 


---

Database Drivers 
56 
Clipper:Driver Strings 
There are switches or "driver strings" you can set to control the way your application creates, 
reads, and writes files with a specific driver. Driver strings are simply messages or parameters 
that are sent to the file driver at run-time to control its behavior. See Common Driver Features--
Driver Strings for an overview of these runtime Database Driver switches and parameters. 
 
Some driver strings have no effect after the file is open, so no SEND function syntax is 
listed for those strings. However, the SEND function syntax to return the value of the 
switch is listed for all driver strings.  
The Clipper Driver supports the following Driver Strings: 
## BUFFERS
 
DRIVER('CLIPPER', '/BUFFERS = n' ) 
[ Status" = ] SEND(file, 'BUFFERS [ = n ]' ) 
 Sets the size of the buffer used to read and write to the file, where the buffer size is (n * 512 
bytes). Use the /BUFFERS driver string to increase the buffer size if access is slow. Maximum 
buffer size is 4,294,967,264. SEND returns the size of the buffer in bytes. 
 
 
The default is three buffers of 1024 bytes each. Increasing the number of buffers will not 
increase performance when a file is shared by multiple users. 
## RECOVER
 
## DRIVER('CLIPPER', '/RECOVER' )
[ Status" = ] SEND(file, 'RECOVER' ) 
Equivalent to the Xbase RECALL command, which recovers records marked for deletion. When 
using the Clipper driver, the DELETE statement flags a record as "inactive." The driver does not 
remove the record until the PACK command is executed. 
RECOVER is evaluated each time you open the file if you add the driver string to the data 
dictionary. When the driver recovers the records previously marked for deletion, you must 
manually rebuild keys and indexes with the BUILD statement. 
## IGNORESTATUS
 
DRIVER('CLIPPER', '/IGNORESTATUS = on | off ' ) 
[ Status" = ] SEND(file, 'IGNORESTATUS [ on | off ]' ) 
When set on, the driver does not skip deleted records when accessing the file with GET, NEXT, 
and PREVIOUS in file order. It also enables a PUT on a deleted or held record. IGNORESTATUS 
requires opening the file in exclusive mode. SEND returns the IGNORESTATUS setting (ON or 
OFF) in the form of a STRING(3). 


---

Database Drivers and Interfaces 
57 
## DELETED
 
[ Status" = ] SEND(file, 'DELETED' ) 
For use only with the SEND command, when IGNORESTATUS is on. Returns the status of the 
current record. If deleted, the return string is "ON" and if not, "OFF."  
## ZEROY2K
DRIVER('CLIPPER', '/ZEROY2K = on | off' ) 
[ Status" = ] SEND(file, 'ZEROY2K [ on | off ]' ) 
In the header of Clipper files there is a field that stores the year that the file was last edited. Some 
applications store this as the number of years since 1900. Others store it as a 2-digit year. So for 
dates in the year 2000 some applications store 0 in this field and others 100. Clarion will read files 
with either. However it will write 100. Writing 100 may make the files unreadable by products that 
only support 0. To change this behavior you can with use a driver string of ZEROY2K, a SEND 
command or a setting in the WIN.INI file. 
 
The driver will store 0 in the DBF file header when the WINI.INI setting is set to 1 or 'on' in a 
SEND command or driver string, otherwise a 100 will be stored in the DBF file header. 
  
The SEND command causes the setting to be set for all files that use that driver, not just 
for that file. 
Example: 
## WIN.INI
 ;Sets all Clipper files to store a 0 in the DBF file header 
## [CWCLIPPER]
## ZEROY2K=1
SEND command  
 SEND('Orders', ZEROY2K='on'  !sets Orders file to store 0 in the DBF file header 
 SEND('Orders', ZEROY2K='off'  !sets Orders file to store 100 in the DBF file header 
Driver String 
 Orders FILE, DRIVER('clipper', '/ZEROY2K=on'),PRE(ORD)  !SETS Orders file to store 0  
 
 


---

Database Drivers 
58 
Clipper:Supported Commands and Attributes 
 
 
File Attributes 
Supported 
 
## CREATE
Y1 
 
DRIVER(filetype [,driver string]) 
Y 
 
## NAME
Y 
 
## ENCRYPT
N 
 
OWNER(password) 
N 
 
## RECLAIM
N2 
 
PRE(prefix) 
Y 
 
## BINDABLE
Y 
 
## THREAD
Y16 
 
EXTERNAL(member) 
Y 
 
DLL([flag]) 
Y 
 
OEM 
Y 
 
## LOCALE
Y 
 
File Structures 
Supported 
 
## INDEX
Y 
 
KEY 
Y 
 
## MEMO
Y3 
 
## BLOB
N 
 
## RECORD
Y 
 
 
Index, Key, Memo Attributes 
Supported 
 
## BINARY
N 
 
DUP 
Y4 
 
## NOCASE
Y 
 
OPT 
N 
 
## PRIMARY
Y 


---

Database Drivers and Interfaces 
59 
 
## NAME
Y3 
 
Ascending Components 
Y 
 
Descending Components 
Y 
 
Mixed Components 
Y 
 
 
Field Attributes 
Supported 
 
DIM 
N 
 
## OVER
Y 
 
## NAME
Y1 
 
 
File Procedures 
Supported 
 
BOF(file) 
Y11 
 
BUFFER(file) 
N 
 
BUILD(file) 
Y 
 
BUILD(key) 
Y 
 
BUILD(index) 
Y 
 
BUILD(index, components) 
Y5 
 
BUILD(index, components, filter) 
N 
 
BYTES(file) 
N 
 
CLOSE(file) 
Y 
 
COPY(file, new file) 
Y6 
 
CREATE(file) 
Y1 
 
DUPLICATE(file) 
Y 
 
DUPLICATE(key) 
Y 
 
EMPTY(file) 
Y 
 
EOF(file) 
Y11 
 
FLUSH(file) 
Y 
 
LOCK(file) 
Y 
 
NAME(label) 
Y 


---

Database Drivers 
60 
 
OPEN(file, access mode) 
Y7 
 
PACK(file) 
Y 
 
POINTER(file) 
Y12 
 
POINTER(key) 
Y12 
 
POSITION(file) 
Y13 
 
POSITION(key) 
Y13 
 
RECORDS(file) 
Y14 
 
RECORDS(key) 
Y14 
 
REMOVE(file) 
Y 
 
RENAME(file, new file) 
Y8 
 
SEND(file, message) 
Y 
 
SHARE(file, access mode) 
Y7 
 
STATUS(file) 
Y 
 
STREAM(file) 
Y 
 
UNLOCK(file) 
Y 
 
 
Record Access 
Supported 
 
ADD(file) 
Y9 
 
ADD(file, length) 
N 
 
APPEND(file) 
Y9 
 
APPEND(file, length) 
N 
 
DELETE(file) 
Y6 
 
GET(file,key) 
Y 
 
GET(file, filepointer) 
Y 
 
GET(file, filepointer, length) 
N 
 
GET(key, keypointer) 
Y 
 
HOLD(file) 
Y10 
 
NEXT(file) 
Y 
 
NOMEMO(file) 
Y 


---

Database Drivers and Interfaces 
61 
 
PREVIOUS(file) 
Y 
 
PUT(file) 
Y 
 
PUT(file, filepointer) 
Y 
 
PUT(file, filepointer, length) 
N 
 
RELEASE(file) 
Y 
 
REGET(file,string) 
Y 
 
REGET(key,string) 
Y 
 
RESET(file,string) 
Y 
 
RESET(key,string) 
Y 
 
SET(file) 
Y  
 
SET(file, key) 
Y 
 
SET(file, filepointer) 
Y 
 
SET(key) 
Y 
 
SET(key, key) 
Y 
 
SET(key, keypointer) 
Y 
 
SET(key, key, filepointer) 
Y 
 
SKIP(file, count) 
Y 
 
WATCH(file) 
Y 
 
 
Transaction Processing 
Supported 
 
LOGOUT(timeout, file, ..., file) 
N15 
 
## COMMIT
N 
 
## ROLLBACK
N 
 
 
Null Data Processing 
Supported 
 
NULL(field) 
N 
 
SETNULL(field) 
N 
 
SETNULL(file,field) 
N 
 
SETNONNULL(field) 
N 


---

Database Drivers 
62 
Notes 
1      If your application creates a Clipper file, you may require additional NAME information for 
these Clipper data types: 
For a Clipper numeric field, use the Clarion REAL data type. Then in the NAME attribute 
(the External Name field on the Attributes tab in the Field Properties dialog), specify 
'NumericFieldName=N(Precision,DecimalPlaces)' where NumericFieldName is the name 
of the field, Precision is the precision of the field and DecimalPlaces is the number of 
decimal places. See Data Types above for more information. 
For a Clipper logical field, use the Clarion BYTE data type. See Data Types above for 
more information. See the Miscellaneous section for tips on reading the data from the 
field. 
For a Clipper date field, use the Clarion DATE data type. See Data Types above for more 
information.  
2      When the driver deletes a record from a Clipper database, the record is not physically 
removed, instead the driver marks it inactive. Memo fields are not physically removed 
from the memo file, however they cannot be retrieved if they refer to an inactive record. 
To remove records and memo fields permanently, execute a PACK(file). 
 
To those programmers familiar with Clipper, this driver processes deleted records 
consistent with the way Clipper processes them after the SET DELETED ON 
command is issued. Records marked for deletion are ignored from processing by 
executable code statements, but remain in the data file. 
3      MEMO field declarations require a pointer field in the file's record structure. Declare the 
pointer field as a STRING(10) or a LONG. This field will be stored in the .DBF file 
containing the offset of the memo in the .DBT file. The MEMO declaration must have a 
NAME() attribute naming the pointer field. See Data Types above for more information.  
4      In Clipper it is legal to enter multiple records with duplicates of the unique key 
components. However, only the first of these records is indexed. So processing in key 
order only shows this first record. If you delete a record, then enter a new record with the 
same key value, the key file continues to point at the deleted record rather than the new 
record. In this situation, the Clipper file driver driver changes the key file to point at the 
active record rather than the deleted record. This means that if you use a Clipper 
program to delete a unique record, then insert a duplicate of this record, the new record 
is invisible when processing in key order until a pack is done. If you do the same process 
in a Clarion program, the new record is visible when processing in key order. 
5      When building dynamic indexes, the components may take one of two forms: 
 BUILD(DynNdx, '+Pre:FLD1, -Pre:FLD2') 
This form specifies the names of the fields on which to build the index. The field names 
must appear as specified in the fields' NAME() attribute if supplied, or must be the label 
name. A prefix may be used for compatibility with Clarion conventions but is ignored. 
 BUILD(DynNdx, 'T[Expression]') 
This form specifies the type and Expression used to build an index--see Miscellaneous--
Key Definition below. 
6      The COPY() command copies data and memo files using newfile, which may specify a 
new file name or directory. Key or index files are copied if the newfile is a subdirectory 
specification. To copy an index file to a new file, use a special form of the copy 
command: 
  COPY(file,'<index>|<newfile>') 


---

Database Drivers and Interfaces 
63 
This returns File Not Found if an invalid index is passed. The COPY command assumes 
a default extension of .NTX for both the source and the target file names if none is 
specified. If you require a file name without an extension, terminate the name with a 
period. Given the file structure: 
Clar2  FILE,CREATE,DRIVER('Clipper'),PRE(CL2) 
NumKey   KEY(+CL2:Num),DUP 
StrKey   KEY(+CL2:Str1) 
StrKey2  KEY(+CL2:Str2) 
AMemo    MEMO(100), NAME('mem') 
Record   RECORD 
Num       STRING(@n-_9.2) 
## STR1      STRING(2)
## STR2      STRING(2)
Mem       STRING(10) 
         END 
       END 
The following commands copy this file definition to A: 
COPY(Clar2,'A:\CLAR2') 
COPY(Clar2,'StrKey|A:\STRKEY') 
COPY(Clar2,'StrKey2|A:\STRKEY2') 
COPY(Clar2,'NumKey|A:\NUMKEY') 
After these calls, the following files would exist on drive A: CLAR2.DBF, CLAR2.DBT, 
STRKEY.NTX, STRKEY2.NTX, and NUMKEY.NTX. 
7      You do not need SHARE (or VSHARE) in any environment (for example, Novell) that 
supplies file locking as part of the operating system.  
8      The RENAME command copies the data and memo files using newfile, which may specify 
a new file name or directory path. Key and index files must be renamed using the same 
syntax as the COPY command, above. 
9      The ADD statement tests for duplicate keys before modifying the data file or its 
associated KEY files. Consequently it is slower than APPEND which performs no checks 
and does not update KEYs. When adding large amounts of data to a database use 
APPEND...BUILD in preference to ADD. 
10    Clipper performs record locking by locking the entire record within the data file. This 
prevents read access to other processes. Therefore we recommend minimizing the 
amount of time for which a record is held. 
11    Although the driver supports these functions, we do not recommend their use. They must 
physically access the files and add overhead. Instead, test the value returned by 
ERRORCODE() after each sequential access. NEXT or PREVIOUS post Error 33 
(Record Not Available) if an attempt is made to access a record beyond the end or 
beginning of the file. 
12    There is no distinction between file pointers and key pointers; they both return the record 
number for any given record. 
13    POSITION(file) returns a STRING(12). POSITION(key) returns a STRING the size of the 
key fields + 4 bytes. 
14    Under Clipper, the RECORDS() function reports the same number of records for the data 
file and its keys and indexes. Usually there will be no difference in the number of records 
unless the INDEX is out of date. Because the DELETE statement does not physically 
remove records, the number of records reported by the RECORDS() function includes 
inactive records. Exercise care when using this function. 
15    See also PROP:Logout in the Language Reference. 
16    THREADed files consume additional file handles for each thread that accesses the file. 


---

Database Drivers 
64 
Clipper:Other 
Boolean Evaluation 
Clipper allows a logical field to accept one of nine possible values (y,Y,n,N,t,T,f,F or a space 
character). The space character is neither true nor false. When using a logical field from a 
preexisting database in a logical expression, account for all these possibilities. Remember that 
when a STRING field is used as an expression, it is true if it contains any data and false if it is 
equal to zero or blank. Therefore, to evaluate a Logical field's truth, the expression should be true 
if the field contains any of the "true" characters (T,t,Y, or y). For example, if a Logical field were 
used to specify a product as taxable or nontaxable, the expression to evaluate its truth would be:   
(If Condition): 
    Taxable='T' OR Taxable='t' OR Taxable='Y' OR Taxable='y' 
Large MEMOs 
Clipper supports MEMO fields up to a maximum of 64K. If you have an existing file which 
includes a memo greater than 64K, you can use the file but not modify the large MEMOs. 
You can determine when your application encounters a large MEMO by detecting when the 
memo pointer variable is non-blank, but the memo appears to be blank. Error 47 (Bad Record 
Declaration) is posted. If you attempt to update such a record, any modification to the MEMO field 
is ignored. 
Long Field Names 
Clipper supports a maximum of 10 characters in a field name. If you require more, use an 
External Name with 10 characters or less.  
Sort Sequence 
The Clipper driver supports international sort orders, however, to maintain compatibility with 
Clipper's international sort order, remove the CLADIGRAPH= line from ..\(CLA 
root)\BIN\Clarion7.ENV file. 
Key Definition 
Clipper supports the use of expressions to define keys. Within the Dictionary Editor, you can 
place the expression in the external name field in the Key Properties dialog. The format of the 
external name is: 
'FileName=T[Expression]' 
Where FileName represents the name of the index file (which can contain a path and file 
extension), and T represents the type of the index. Valid types are: C = character, D = date, and 
N = numeric. If the type is D or N then Expression can name only one field. 
String expressions may use the '+' operator to concatenate multiple string arguments. Numeric 
expressions use the '+' or '-' operators with their conventional meanings. The maximum length of 
a Clipper expression is 250 characters. 
The expression may refer to multiple fields in the record, and may contain xBase functions. 
Square brackets must enclose the expression. The currently supported functions appear below. If 
the driver encounters an unsupported Xbase function in a preexisting file, it posts error 76 'Invalid 
Index String' when the file is opened for keys and static indexes. 
Supported xBase Key Definition Functions 
ALLTRIM(string) 
Removes leading and trailing spaces. 


---

Database Drivers and Interfaces 
65 
CTOD(string) 
Converts a string key to a date. The string must be in the 
format mm/dd/yy; the result takes the form 'yyyymmdd'. The 
yyyy element of the date defaults to the twentieth century. 
An invalid date results in a key containing blanks. 
## DELETED()
Returns TRUE if the record is deleted. 
DESCEND(string|date|numeric) Inverts the argument, and creates descending Clipper 
indexes.  
DTOC(date) 
Converts a date key to string format 'mm/dd/yy' 
DTOS(date) 
Converts a date key to string format 'yyyymmdd' 
FIXED(float) 
Converts a float key to a numeric. 
FLOAT(numeric) 
Converts a numeric key to a float. 
IIF(bool,val1,val2) 
Returns val1 if the first parameter is TRUE, otherwise 
returns val2. 
LEFT(string, n) 
Returns the leftmost n characters of the string key as a string 
of length n. 
LOWER(string) 
Converts a string key to lower case. 
LTRIM(string) 
Removes spaces from the left of a string. 
## RECNO()
Returns the current record number. 
RIGHT(string, n) 
Returns the rightmost n characters of the string key as a string 
RTRIM(string) 
Removes spaces from the right of a string. 
STR(numeric [,length 
[, decimal places]]) 
Converts a numeric to a string. The length of the string and 
the number of decimal places are optional. The default string 
length is 10, and the number of decimal places is 0. 
SUBSTR(string,offset,n) 
Returns a substring of the string key starting at offset and of 
n characters in length. 
TRIM(string) 
Removes spaces from the right of a string (identical to 
## RTRIM).
UPPER(string) 
Converts a string key to upper case. 
VAL(string) 
Converts a string key to a numeric. 
 


---

Database Drivers 
66 
dBaseIII Database Driver 
dBaseIII:Specifications 
The dBase3 file driver is compatible with dBase III. The default data file extension is *.DBF. 
Keys and Indexes exist as separate files from the data file. Keys are dynamic--they automatically 
update as the data file changes. Indexes are static--they do not automatically update, but instead 
require the BUILD statement for updating. The default file extension for the index file is *.NDX. 
International sort orders are supported. 
The driver stores records as fixed length. It stores memo fields in a separate file. The memo file 
name takes the first eight characters of the File Label plus an extension of .DBT. 
Files: 
## CLADB3L.LIB
Windows Static Link Library 
 
## CLADB3.LIB
Windows Export Library 
 
## CLADB3.DLL
Windows Dynamic Link Library 
 
dBaseIII:Data Types 
The xBase file format stores all data as ASCII strings. You may either specify STRING types with 
declared pictures for each field, or specify native Clarion types, which the driver converts 
automatically. 
dBase data type 
Clarion data type 
STRING w/ picture 
Date 
## DATE
## STRING(@D12)
*Numeric 
## REAL
STRING(@N-_p.d) 
*Logical 
## BYTE
## STRING(1)
Character 
## STRING
## STRING
*Memo 
## MEMO
## MEMO
If your application reads and writes to existing files, a pictured STRING will suffice. However, if 
your application creates a dBase III file, you may require additional information for these dBase III 
types: 
*      To create a Numeric field in the Data Dictionary, choose the REAL data type. In the 
External Name field on the Attributes tab, specify 
'NumericFieldName=N(Precision,DecimalPlaces)' where NumericFieldName is the name 
of the field, Precision is the precision of the field and DecimalPlaces is the number of 
decimal places. With a REAL data type, you cannot access the Character or Places fields 
in the Field definition, you must specify those attributes with an expression in the External 
Name Field on the Attributes tab. 
For example, if you want to create a field called Number with nine significant digits and 
two decimal places, enter 'Number=N(9,2) in the External Name field on the Attributes 
tab of the Field properties in the Data Dictionary. 
If you're hand coding a native Clarion data type, add the NAME attribute using the same 
syntax.  
If you're hand coding a STRING with picture, STRING(@N-_9.2), NAME('Number'), 
where Number is the field name. 


---

Database Drivers and Interfaces 
67 
*      To create a logical field, using the data dictionary, choose the BYTE data type. There are 
no special steps; however, see the miscellaneous section for tips on reading the data 
from the field. 
If you're hand coding a STRING with picture, add the NAME attribute: STRING(1), 
NAME('LogFld = L'). 
To create a date field, using the data dictionary, choose the DATE data type, rather than 
LONG, which you usually use for the TopSpeed or Clarion file formats. 
*      MEMO field declarations require the a pointer field in the file's record structure. Declare 
the pointer field as a STRING(10) or a LONG. This field will be stored in the .DBF file 
containing the offset of the memo in the .DBT file. The MEMO declaration must have a 
NAME() attribute naming the pointer field. An example file declaration follows: 
File  FILE, DRIVER('dBase3') 
Memo1  MEMO(200),NAME('Notes') 
Memo2  MEMO(200),NAME('Text') 
Rec    RECORD 
Mem1Ptr LONG,NAME('Notes') 
Mem2Ptr STRING(10),NAME('Text') 
       END 
      END 
 
Use the File Import Utility in the Clarion Dictionary Editor to define your files. 
dBaseIII:File Specifications/Maximums 
File Size:             2,000,000,000 bytes 
Records per File:      1,000,000,000 
Record Size:           4,000 bytes 
Field Size 
     Character:        254 bytes 
     Date:             8 bytes 
     Logical:          1 byte 
     Numeric:          20 bytes including decimal point 
     Memo:             64K (see note) 
Fields per Record:     128 
Field Name:            10 characters 
Keys/Indexes per File: No Limit 
Key Sizes 
     Character:        100 bytes 
     Numeric, Date:    8 bytes 
Memo fields per File:  Dependent on available memory 
Open Files:            Operating system dependent 
 
 


---

Database Drivers 
68 
dBaseIII:Driver Strings 
There are switches or "driver strings" you can set to control the way your application creates, 
reads, and writes files with a specific driver. Driver strings are simply messages or parameters 
that are sent to the file driver at run-time to control its behavior. See Common Driver Features--
Driver Strings for an overview of these runtime Database Driver switches and parameters. 
 
Some driver strings have no effect after the file is open, so no SEND function syntax is 
listed for those strings. However, the SEND function syntax to return the value of the 
switch is listed for all driver strings.  
The dBaseIII Driver supports the following Driver Strings: 
## BUFFERS
 
DRIVER('DBASE3', '/BUFFERS = n' ) 
[ Status" = ] SEND(file, 'BUFFERS [ = n ]' ) 
Sets the size of the buffer used to read and write to the file, where the buffer size is (n * 512 
bytes). Use the /BUFFERS driver string to increase the buffer size if access is slow. Maximum 
buffer size is 4,294,967,264. SEND returns the size of the buffer in bytes. 
 
The default is three buffers of 1024 bytes each. Increasing the number of buffers will not 
increase performance when a file is shared by multiple users. 
## RECOVER
 
## DRIVER('DBASE3', '/RECOVER' )
[ Status" = ] SEND(file, 'RECOVER' ) 
Equivalent to the Xbase RECALL command, which recovers records marked for deletion. When 
using the dBaseIV driver, the DELETE statement flags a record as "inactive." The driver does not 
remove the record until the PACK command is executed. 
RECOVER is evaluated each time you open the file if you add the driver string to the data 
dictionary. When the driver recovers the records previously marked for deletion, you must 
manually rebuild keys and indexes with the BUILD statement. 
## IGNORESTATUS
 
DRIVER('DBASE3', '/IGNORESTATUS = on | off ' ) 
[ Status" = ] SEND(file, 'IGNORESTATUS [ on | off ]' ) 
When set on, the driver does not skip deleted records when accessing the file with GET, NEXT, 
and PREVIOUS in file order. It also enables a PUT on a deleted or held record. IGNORESTATUS 
requires opening the file in exclusive mode. SEND returns the IGNORESTATUS setting (ON or 
OFF) in the form of a STRING(3). 


---

Database Drivers and Interfaces 
69 
## DELETED
 
[ Status" = ] SEND(file, 'DELETED' ) 
For use only with the SEND command, when IGNORESTATUS is on. Returns the status of the 
current record. If deleted, the return string is "ON" and if not, "OFF."   
## OMNIS
 
## DRIVER('DBASE3', '/OMNIS' )
SEND(file, 'OMNIS' ) 
Specifies OMNIS file header and file delimiter compatibility. SEND is only valid when the file is 
closed; it returns nothing. 
## ZEROY2K
 
DRIVER('DBASE3', '/ZEROY2K = on | off' ) 
[ Status" = ] SEND(file, 'ZEROY2K [ on | off ]' ) 
In the header of dBase3files there is a field that stores the year that the file was last edited. Some 
applications store this as the number of years since 1900. Others store it as a 2 digit year. So for 
dates in the year 2000 some applications store 0 in this field and others 100. Clarion will read files 
with either. However it will write 100. Writing 100 may make the files unreadable by products that 
only support 0. To change this behavior you can with use a driver string of ZEROY2K, a SEND 
command or a setting in the WIN.INI file. 
 
The driver will store 0 in the DBF file header when the WINI.INI setting is set to 1 or 'on' in a 
SEND command or driver string, otherwise a 100 will be stored in the DBF file header. 
 
 
The SEND command causes the setting to be set for all files that use that driver, not just 
for that file. 
Examples: 
## WIN.INI:
 ;Sets all dBase3 files to store a 0 in the DBF file header 
## [CWDBASE3]
## ZEROY2K=1
 
 SEND command:  
 SEND('Orders', ZEROY2K='on'   !sets Orders file to store 0 in the DBF file header 
 SEND('Orders', ZEROY2K='off'  !sets Orders file to store 100 in the DBF file header 
 
 Driver String Orders:  
 FILE, DRIVER('dbase3', '/ZEROY2K=on'),PRE(ORD)  !SETS Orders file to store 030 – 
 
 


---

Database Drivers 
70 
dBaseIII: Supported Commands and Attributes 
 
 
File Attributes 
Supported 
 
## CREATE
Y 
 
DRIVER(filetype [,driver string]) 
Y 
 
## NAME
Y 
 
## ENCRYPT
N 
 
OWNER(password) 
N 
 
## RECLAIM
N1 
 
PRE(prefix) 
Y 
 
## BINDABLE
Y 
 
## THREAD
Y12 
 
EXTERNAL(member) 
Y 
 
DLL([flag]) 
Y 
 
OEM 
Y 
 
## LOCALE
Y 
 
File Structures 
Supported 
 
## INDEX
Y 
 
KEY 
Y 
 
## MEMO
Y 
 
## BLOB
N 
 
## RECORD
Y 
 
 
Index, Key, Memo Attributes 
Supported 
 
## BINARY
N 
 
DUP 
Y2 
 
## NOCASE
Y 
 
OPT 
N 
 
## PRIMARY
Y 


---

Database Drivers and Interfaces 
71 
 
## NAME
Y 
 
Ascending Components 
Y 
 
Descending Components 
Y 
 
Mixed Components 
N 
 
 
Field Attributes 
Supported 
 
DIM 
N 
 
## OVER
Y 
 
## NAME
Y 
 
 
File Procedures 
Supported 
 
BOF(file) 
Y8 
 
BUFFER(file) 
N 
 
BUILD(file) 
Y 
 
BUILD(key) 
Y 
 
BUILD(index) 
Y 
 
BUILD(index, components) 
Y3 
 
BUILD(index, components, filter) 
N 
 
BYTES(file) 
N 
 
CLOSE(file) 
Y 
 
COPY(file, new file) 
Y4 
 
CREATE(file) 
Y 
 
DUPLICATE(file) 
Y 
 
DUPLICATE(key) 
Y 
 
EMPTY(file) 
Y 
 
EOF(file) 
Y8 
 
FLUSH(file) 
Y 
 
LOCK(file) 
N 
 
NAME(label) 
Y 


---

Database Drivers 
72 
 
OPEN(file, access mode) 
Y5 
 
PACK(file) 
Y 
 
POINTER(file) 
Y9 
 
POINTER(key) 
Y9 
 
POSITION(file) 
Y10 
 
POSITION(key) 
Y10 
 
RECORDS(file) 
Y11 
 
RECORDS(key) 
Y11 
 
REMOVE(file) 
Y 
 
RENAME(file, new file) 
Y4 
 
SEND(file, message) 
Y 
 
SHARE(file, access mode) 
Y5 
 
STATUS(file) 
Y 
 
STREAM(file) 
Y 
 
UNLOCK(file) 
N 
 
 
Record Access 
Supported 
 
ADD(file) 
Y6 
 
ADD(file, length) 
N 
 
APPEND(file) 
Y6 
 
APPEND(file, length) 
N 
 
DELETE(file) 
Y1 
 
GET(file,key) 
Y 
 
GET(file, filepointer) 
Y 
 
GET(file, filepointer, length) 
N 
 
GET(key, keypointer) 
Y 
 
HOLD(file) 
Y7 
 
NEXT(file) 
Y 
 
NOMEMO(file) 
Y 


---

Database Drivers and Interfaces 
73 
 
PREVIOUS(file) 
Y 
 
PUT(file) 
Y 
 
PUT(file, filepointer) 
Y 
 
PUT(file, filepointer, length) 
N 
 
RELEASE(file) 
Y 
 
REGET(file,string) 
Y 
 
REGET(key,string) 
Y 
 
RESET(file,string) 
Y 
 
RESET(key,string) 
Y 
 
SET(file) 
Y  
 
SET(file, key) 
Y 
 
SET(file, filepointer) 
Y 
 
SET(key) 
Y 
 
SET(key, key) 
Y 
 
SET(key, keypointer) 
Y 
 
SET(key, key, filepointer) 
Y 
 
SKIP(file, count) 
Y 
 
WATCH(file) 
Y 
 
 
Transaction Processing 
Supported 
 
LOGOUT(timeout, file, ..., file) 
N 
 
## COMMIT
N 
 
## ROLLBACK
N 
 
 
Null Data Processing 
Supported 
 
NULL(field) 
N 
 
SETNULL(field) 
N 
 
SETNULL(file,field) 
N 
 
SETNONNULL(field) 
N 


---

Database Drivers 
74 
Notes 
1      When the driver deletes a record from a dBase III database, the record is not physically 
removed, instead the driver marks it inactive. Memo fields are not physically removed 
from the memo file, however they cannot be retrieved if they refer to an inactive record. 
Key values are removed from the index files. To remove records and memo fields 
permanently, execute a PACK(file). 
 
 
To those programmers familiar with dBase III, this driver processes deleted 
records consistent with the way dBase III processes them after the SET DELETED 
ON command is issued. Records marked for deletion are ignored from processing 
by executable code statements, but remain in the data file. 
2      dBase III does not support any form of  unique index.  So the DUP attribute must be on all 
keys. 
3      When building dynamic indexes, the components may take one of two forms: 
   BUILD(DynNdx, '+Pre:FLD1, -Pre:FLD2') 
This form specifies the names of the fields on which to build the index. The field names 
must appear as specified in the fields' NAME() attribute if supplied, or must be the label 
name. A prefix may be used for compatibility with Clarion conventions but is ignored. 
   BUILD(DynNdx, 'T[Expression]') 
This form specifies the type and Expression used to build an index--see Miscellaneous--
Key Definition below. 
4      These commands copy data and memo files using newfile, which may specify a new file 
name or directory. Key or index files are copied if the newfile is a subdirectory 
specification. To copy an index file to a new file, use a special form of the copy or rename 
command: 
    COPY(file,'<index>|<newfile>') 
This returns File Not Found if an invalid index is passed. The COPY command assumes 
a default extension of ".NDX" for both the source and the target file names if none is 
specified. If you require a file name without an extension, terminate the name with a 
period. Given the file structure: 
Clar2  FILE,CREATE,DRIVER('dBase3'),PRE(CL2) 
NumKey  KEY(+CL2:Num),DUP 
StrKey  KEY(+CL2:Str1) 
StrKey2 KEY(+CL2:Str2) 
AMemo   MEMO(100), NAME('mem') 
Record  RECORD 
Num      STRING(@n-_9.2) 
## STR1     STRING(2)
## STR2     STRING(2)
Mem      STRING(10) 
        END 
       END 
The following commands copy this file definition to A: 
COPY(Clar2,'A:\CLAR2') 
COPY(Clar2,'StrKey|A:\STRKEY') 
COPY(Clar2,'StrKey2|A:\STRKEY2') 
COPY(Clar2,'NumKey|A:\NUMKEY') 
After these calls, the following files would exist on drive A: CLAR2.DBF, CLAR2.DBT, 
STRKEY.NDX, STRKEY2.NDX, and NUMKEY.NDX. 


---

Database Drivers and Interfaces 
75 
5      You do not need SHARE (or VSHARE) in any environment (for example, Novell) that 
supplies file locking as part of the operating system. 
6      The ADD statement tests for duplicate keys before modifying the data file or its 
associated KEY files. Consequently it is slower than APPEND which performs no checks 
and does not update KEYs. When adding large amounts of data to a database use 
APPEND...BUILD in preference to ADD. 
7      dBase III performs record locking by locking the entire record within the data file. This 
prevents read access to other processes. Therefore we recommend minimizing the 
amount of time for which a record is held. 
8      Although the driver supports these functions, we do not recommend their use. They must 
physically access the files and add overhead. Instead, test the value returned by 
ERRORCODE() after each sequential access. NEXT or PREVIOUS post Error 33 
(Record Not Available) if an attempt is made to access a record beyond the end or 
beginning of the file. 
9      There is no distinction between file pointers and key pointers; they both return the record 
number for any given record. 
10     POSITION(file) returns a STRING(12). POSITION(key) returns a STRING the size of the 
key fields + 4 bytes. 
11     Under dBase III, the RECORDS() function reports the same number of records for the 
data file and its keys and indexes. Usually there will be no difference in the number of 
records unless the INDEX is out of date. Because the DELETE statement does not 
physically remove records, the number of records reported by the RECORDS() function 
includes inactive records. Exercise care when using this function. 
12     THREADed files consume additional file handles for each thread that accesses the file. 


---

Database Drivers 
76 
dBaseIII:Other 
Boolean Evaluation 
dBase III allows a logical field to accept one of nine possible values (y,Y,n,N,t,T,f,F or a space 
character). The space character is neither true nor false. When using a logical field from a 
preexisting database in a logical expression, account for all these possibilities. Remember that 
when a STRING field is used as an expression, it is true if it contains any data and false if it is 
equal to zero or blank. Therefore, to evaluate a Logical field's truth, the expression should be true 
if the field contains any of the "true" characters (T,t,Y, or y). For example, if a Logical field were 
used to specify a product as taxable or nontaxable, the expression to evaluate its truth would be:  
(If Condition): 
    Taxable='T' OR Taxable='t' OR Taxable='Y' OR Taxable='y' 
Large MEMOs 
dBase III supports MEMO fields up to a maximum of 64K. If you have an existing file which 
includes a memo greater than 64K, you can use the file but not modify the large MEMOs. 
You can determine when your application encounters a large MEMO by detecting when the 
memo pointer variable is non-blank, but the memo appears to be blank. Error 47 (Bad Record 
Declaration) is posted, and any modification to the MEMO field is ignored. 
Long Field Names 
dBase III supports a maximum of 10 characters in a field name. If you require more, use an 
External Name with 10 characters or less.  
International Sort Sequence 
The dBaseIII driver supports international sort orders, however, to maintain compatibility with 
dBaseIII's international sort order, remove the CLADIGRAPH= line from ..\BIN\Clarion7.ENV file. 
KEY Definitions 
dBase III supports the use of expressions to define keys. Within the Dictionary Editor, you can 
place the expression in the external name field in the Key Properties dialog. The general format 
of the external name is :  
'FileName=T[Expression]' 
Where FileName represents the name of the index file (which can contain a path and file 
extension), and T represents the type of the index. Valid types are: C = character, D = date, and 
N = numeric. If the type is D or N then Expression can name only one field. 
String expressions may use the '+' operator to concatenate multiple string arguments. Numeric 
expressions use the '+' or '-' operators with their conventional meanings. The maximum length of 
a dBase III expression is 250 characters. 
The expression may refer to multiple fields in the record, and contain xBase functions. Square 
brackets must enclose the expression. The currently supported functions appear below. If the 
driver encounters an unsupported Xbase function in a preexisting file, it posts error 76 'Invalid 
Index String' when the file is opened for keys and static indexes. 


---

Database Drivers and Interfaces 
77 
Supported xBase Key Definition Functions 
ALLTRIM(string) 
Removes leading and trailing spaces. 
CTOD(string) 
Converts a string key to a date. The string must be in the format 
mm/dd/yy; the result takes the form 'yyyymmdd'. The yyyy element 
of the date defaults to the twentieth century. An invalid date results 
in a key containing blanks. 
## DELETED()
Returns TRUE if the record is deleted. 
DTOC(date) 
Converts a date key to string format 'mm/dd/yy.' 
DTOS(date) 
Converts a date key to string format 'yyyymmdd.' 
FIXED(float) 
Converts a float key to a numeric. 
FLOAT(numeric) 
Converts a numeric key to a float. 
IIF(bool,val1,val2) 
Returns val1 if the first parameter is TRUE, otherwise returns val2. 
LEFT(string, n) 
Returns the leftmost n characters of the string key as a string of 
length n. 
LOWER(string) 
Converts a string key to lower case. 
LTRIM(string) 
Removes spaces from the left of a string. 
## RECNO()
Returns the current record number. 
RIGHT(string, n) 
Returns the rightmost n characters of the string key as a string of length n. 
RTRIM(string) 
Removes spaces from the right of a string. 
STR(numeric[,length[,decimal places]]) 
Converts a numeric to a string. The length of 
the string and the number of decimal places 
are optional. The default string length is 10, 
and the number of decimal places is 0. 
SUBSTR(string,offset,n) Returns a substring of the string key starting at offset and of n 
characters in length. 
TRIM(string) 
Removes spaces from the right of a string (identical to RTRIM). 
UPPER(string) 
Converts a string key to upper case. 
VAL(string) 
Converts a string key to a numeric. 
 


---

Database Drivers 
78 
dBaseIV Database Driver 
 
dBaseIV:Specifications 
The dBase4 file driver is compatible with dBase IV. The default data file extension is *.DBF. 
Keys and Indexes exist as separate files from the data file. Keys are dynamic--they automatically 
update as the data file changes. Indexes are static--they do not automatically update, but instead 
require the BUILD statement for updating. The default file extension for the index file is *.NDX. 
dBase IV supports multiple index files, whose extension is *.MDX. The miscellaneous section 
describes procedures for using .MDX files. 
The driver stores records as fixed length. It stores memo fields in a separate file. The memo file 
name takes the first eight characters of the File Label plus an extension of .DBT. 
Files: 
## CLADB4L.LIB
Windows Static Link Library 
 
## CLADB4.LIB
Windows Export Library 
 
## CLADB4.DLL
Windows Dynamic Link Library 
dBase IV was never as widely adopted as dBase III. Choose this driver only when you must 
share data with an end-user using dBase IV. 
dBaseIV:Data Types 
The xBase file format stores all data as ASCII strings. You may either specify STRING types with 
declared pictures for each field, or specify native Clarion types, which the driver converts 
automatically. 
dBase data type 
Clarion data type 
STRING w/ picture 
Date 
## DATE
## STRING(@D12)
*Numeric 
## REAL
STRING(@N-_p.d) 
*Logical 
## BYTE
## STRING(1)
Character 
## STRING
## STRING
*Memo 
## MEMO
## MEMO
If your application reads and writes to existing files, a pictured STRING will suffice. However, if 
your application creates a dBase IV file, you may require additional information for these dBase 
IV types: 
*      To create a Numeric field in the Data Dictionary, choose the REAL data type. In the 
External Name field on the Attributes tab, specify 
'NumericFieldName=N(Precision,DecimalPlaces)' where NumericFieldName is the name 
of the field, Precision is the precision of the field and DecimalPlaces is the number of 
decimal places. With a REAL data type, you cannot access the Character or Places fields 
in the Field definition, you must specify those attributes with an expression in the External 
Name Field on the Attributes tab. 
For example, if you want to create a field called Number with nine significant digits and 
two decimal places, enter 'Number=N(9,2) in the External Name field on the Attributes 
tab of the Field properties in the Data Dictionary. 
If you're hand coding a native Clarion data type, add the NAME attribute using the same 
syntax.  
If you're hand coding a STRING with picture, STRING(@N-_9.2), NAME('Number'), 
where Number is the field name. 


---

Database Drivers and Interfaces 
79 
*      To create a Logical field, using the data dictionary, choose the BYTE data type. There are 
no special steps; however, see the miscellaneous section for tips on reading the data 
from the field. 
If you're hand coding a STRING with picture, add the NAME attribute: STRING(1), 
NAME('LogFld = L'). 
*      To create a Date field, using the data dictionary, choose the DATE data type, rather than 
LONG, which you usually use for the TopSpeed or Clarion file formats. 
*      MEMO field declarations require the a pointer field in the file's record structure. Declare 
the pointer field as a STRING(10) or a LONG. This field will be stored in the .DBF file 
containing the offset of the memo in the .DBT file. The MEMO declaration must have a 
NAME() attribute naming the pointer field. An example file declaration follows: 
 
File FILE, DRIVER('dBase4') 
Memo1 MEMO(200),NAME('Notes') 
Memo2 MEMO(200),NAME('Text') 
Rec   RECORD 
Mem1Ptr LONG,NAME('Notes') 
Mem2Ptr STRING(10),NAME('Text') 
      END 
     END 
 
Use the File Import Utility in the Clarion Dictionary Editor to define your files. 
dBaseIV:File Specifications/Maximums 
File Size:             2,000,000,000 bytes 
Records per File:      1,000,000,000 
Record Size:           4,000 bytes 
Field Size 
  Character:           254 bytes 
  Date:                8 bytes 
  Logical:             1 byte 
  Numeric:             20 bytes including decimal point 
  Float:               20 bytes including decimal point 
  Memo:                64K (see note) 
Fields per Record:     512 
Field Name:            12 characters 
Keys/Indexes per File:  
      .NDX:            No Limit 
      .MDX             47 tags per .MDX files 
Key Sizes 
  Character:           100 bytes 
  Numeric, Date:       8 bytes 
Memo fields per File:  Dependent on available memory 
Open Files:            Operating system dependent 


---

Database Drivers 
80 
dBaseIV:Driver Strings 
There are switches or "driver strings" you can set to control the way your application creates, 
reads, and writes files with a specific driver. Driver strings are simply messages or parameters 
that are sent to the file driver at run-time to control its behavior. See Common Driver Features--
Driver Strings for an overview of these runtime Database Driver switches and parameters. 
 
 
Some driver strings have no effect after the file is open, so no SEND function syntax is 
listed for those strings. However, the SEND function syntax to return the value of the 
switch is listed for all driver strings.  
The dBaseIV Driver supports the following Driver Strings: 
## BUFFERS
 
DRIVER('DBASE4', '/BUFFERS = n' ) 
[ Status" = ] SEND(file, 'BUFFERS [ = n ]' ) 
Sets the size of the buffer used to read and write to the file, where the buffer size is (n * 512 
bytes). Use the /BUFFERS driver string to increase the buffer size if access is slow. Maximum 
buffer size 4,294,967,264. SEND returns the size of the buffer in bytes. 
 
 
The default is three buffers of 1024 bytes each. Increasing the number of buffers will not 
increase performance when a file is shared by multiple users. 
## RECOVER
 
## DRIVER('DBASE4', '/RECOVER' )
[ Status" = ] SEND(file, 'RECOVER' ) 
Equivalent to the Xbase RECALL command, which recovers records marked for deletion. When 
using the dBaseIV driver, the DELETE statement flags a record as "inactive." The driver does not 
remove the record until the PACK command is executed. 
RECOVER is evaluated each time you open the file if you add the driver string to the data 
dictionary. When the driver recovers the records previously marked for deletion, you must 
manually rebuild keys and indexes with the BUILD statement. 
## IGNORESTATUS
 
DRIVER('DBASE4', '/IGNORESTATUS = on | off ' ) 
[ Status" = ] SEND(file, 'IGNORESTATUS [ on | off ]' ) 
When set on, the driver does not skip deleted records when accessing the file with GET, NEXT, 
and PREVIOUS in file order. It also enables a PUT on a deleted or held record. IGNORESTATUS 
requires opening the file in exclusive mode. SEND returns the IGNORESTATUS setting (ON or 
OFF) in the form of a STRING(3). 


---

Database Drivers and Interfaces 
81 
## DELETED
 
[ Status" = ] SEND(file, 'DELETED' ) 
For use only with the SEND command, when IGNORESTATUS is on. Returns the status of the 
current record. If deleted, the return string is "ON" and if not, "OFF."  
## ZEROY2K
 
DRIVER('DBASE4', '/ZEROY2K = on | off' ) 
[ Status" = ] SEND(file, 'ZEROY2K [ on | off ]' ) 
In the header of dBaase4 files there is a field that stores the year that the file was last edited. 
Some applications store this as the number of years since 1900. Others store it as a 2 digit year. 
So for dates in the year 2000 some applications store 0 in this field and others 100. Clarion will 
read files with either. However it will write 100. Writing 100 may make the files unreadable by 
products that only support 0. To change this behavior you can with use a driver string of 
ZEROY2K, a SEND command or a setting in the WIN.INI file. 
 
The driver will store 0 in the DBF file header when the WINI.INI setting is set to 1 or 'on' in a 
SEND command or driver string, otherwise a 100 will be stored in the DBF file header. 
 
  
The SEND command causes the setting to be set for all files that use that driver, not just 
for that file. 
Examples: 
## WIN.INI:
 ;Sets all dBase4 files to store a 0 in the DBF file header 
## [CWDBASE4]
## ZEROY2K=1
 
SEND command:  
 SEND('Orders', ZEROY2K='on'   !sets Orders file to store 0 in the DBF file header 
 SEND('Orders', ZEROY2K='off'  !sets Orders file to store 100 in the DBF file header 
 
Driver String: 
 Orders FILE, DRIVER('dbase4', '/ZEROY2K=on'),PRE(ORD) !SETS Orders file to store 0  
 
 


---

Database Drivers 
82 
dBaseIV:Supported Commands and Attributes 
 
 
File Attributes 
Supported 
 
## CREATE
Y 
 
DRIVER(filetype [,driver string]) 
Y 
 
## NAME
Y 
 
## ENCRYPT
N 
 
OWNER(password) 
N 
 
## RECLAIM
N1 
 
PRE(prefix) 
Y 
 
## BINDABLE
Y 
 
## THREAD
Y12 
 
EXTERNAL(member) 
Y 
 
DLL([flag]) 
Y 
 
OEM 
Y 
 
## LOCALE
Y 
 
File Structures 
Supported 
 
## INDEX
Y 
 
KEY 
Y 
 
## MEMO
Y 
 
## BLOB
N 
 
## RECORD
Y 
 
 
Index, Key, Memo Attributes 
Supported 
 
## BINARY
N 
 
DUP 
Y2 
 
## NOCASE
Y 
 
OPT 
N 
 
## PRIMARY
Y 


---

Database Drivers and Interfaces 
83 
 
## NAME
Y 
 
Ascending Components 
Y 
 
Descending Components 
Y 
 
Mixed Components 
N 
 
 
Field Attributes 
Supported 
 
DIM 
N 
 
## OVER
Y 
 
## NAME
Y 
 
 
File Procedures 
Supported 
 
BOF(file) 
Y8 
 
BUFFER(file) 
N 
 
BUILD(file) 
Y 
 
BUILD(key) 
Y 
 
BUILD(index) 
Y 
 
BUILD(index, components) 
Y3 
 
BUILD(index, components, filter) 
N 
 
BYTES(file) 
N 
 
CLOSE(file) 
Y 
 
COPY(file, new file) 
Y4 
 
CREATE(file) 
Y 
 
DUPLICATE(file) 
Y 
 
DUPLICATE(key) 
Y 
 
EMPTY(file) 
Y 
 
EOF(file) 
Y8 
 
FLUSH(file) 
Y 
 
LOCK(file) 
N 
 
NAME(label) 
Y 


---

Database Drivers 
84 
 
OPEN(file, access mode) 
Y5 
 
PACK(file) 
Y 
 
POINTER(file) 
Y9 
 
POINTER(key) 
Y9 
 
POSITION(file) 
Y10 
 
POSITION(key) 
Y10 
 
RECORDS(file) 
Y11 
 
RECORDS(key) 
Y11 
 
REMOVE(file) 
Y 
 
RENAME(file, new file) 
Y4 
 
SEND(file, message) 
Y 
 
SHARE(file, access mode) 
Y5 
 
STATUS(file) 
Y 
 
STREAM(file) 
Y 
 
UNLOCK(file) 
N 
 
 
Record Access 
Supported 
 
ADD(file) 
Y6 
 
ADD(file, length) 
N 
 
APPEND(file) 
Y6 
 
APPEND(file, length) 
N 
 
DELETE(file) 
Y1 
 
GET(file,key) 
Y 
 
GET(file, filepointer) 
Y 
 
GET(file, filepointer, length) 
N 
 
GET(key, keypointer) 
Y 
 
HOLD(file) 
Y7 
 
NEXT(file) 
Y 
 
NOMEMO(file) 
Y 


---

Database Drivers and Interfaces 
85 
 
PREVIOUS(file) 
Y 
 
PUT(file) 
Y 
 
PUT(file, filepointer) 
Y 
 
PUT(file, filepointer, length) 
N 
 
RELEASE(file) 
Y 
 
REGET(file,string) 
Y 
 
REGET(key,string) 
Y 
 
RESET(file,string) 
Y 
 
RESET(key,string) 
Y 
 
SET(file) 
Y  
 
SET(file, key) 
Y 
 
SET(file, filepointer) 
Y 
 
SET(key) 
Y 
 
SET(key, key) 
Y 
 
SET(key, keypointer) 
Y 
 
SET(key, key, filepointer) 
Y 
 
SKIP(file, count) 
Y 
 
WATCH(file) 
Y 
 
 
Transaction Processing 
Supported 
 
LOGOUT(timeout, file, ..., file) 
N 
 
## COMMIT
N 
 
## ROLLBACK
N 
 
 
Null Data Processing 
Supported 
 
NULL(field) 
N 
 
SETNULL(field) 
N 
 
SETNULL(file,field) 
N 
 
SETNONNULL(field) 
N 


---

Database Drivers 
86 
Notes 
1      When the driver deletes a record from a dBase IV database, the record is not physically 
removed, instead the driver marks it inactive. Memo fields are not physically removed 
from the memo file, however they cannot be retrieved if they refer to an inactive record. 
Key values are removed from the index files. To remove records and memo fields 
permanently, execute a PACK(file). 
 
To those programmers familiar with dBase IV, this driver processes deleted 
records consistent with the way dBase IV processes them after the SET DELETED 
ON command is issued. Records marked for deletion are ignored from processing 
by executable code statements, but remain in the data file. 
2      In dBase IV it is legal to enter multiple records with duplicates of the unique key 
components. However, only the first of these records is indexed. So processing in key 
order only shows this first record. If you delete a record, then enter a new record with the 
same key value, the key file continues to point at the deleted record rather than the new 
record. In this situation, the dBase IV file driver driver changes the key file to point at the 
active record rather than the deleted record. This means that if you use a dBase IV 
program to delete a unique record, then insert a duplicate of this record, the new record 
is invisible when processing in key order until a pack is done. If you do the same process 
in a Clarion program, the new record is visible when processing in key order. 
3      When building dynamic indexes, the components may take one of two forms: 
   BUILD(DynNdx, '+Pre:FLD1, -Pre:FLD2') 
This form specifies the names of the fields on which to build the index. The field names 
must appear as specified in the fields' NAME() attribute if supplied, or must be the label 
name. A prefix may be used for compatibility with Clarion conventions but is ignored. 
   BUILD(DynNdx, 'T[Expression]') 
This form specifies the type and Expression used to build an index--see Miscellaneous--
Key Definition below. 
4      These commands copy data and memo files using newfile, which may specify a new file 
name or directory. Key or index files are copied if the newfile is a subdirectory 
specification. To copy an index file to a new file, use a special form of the copy 
command: 
  COPY(file,'<index>|<newfile>') 
This returns File Not Found if an invalid index is passed. The COPY command assumes 
a default extension of .NDX for both the source and the target file names if none is 
specified. If you require a file name without an extension, terminate the name with a 
period. Given the file structure: 
Clar2 FILE,CREATE,DRIVER('dBase4'),PRE(CL2) 
NumKey  KEY(+CL2:Num),DUP 
StrKey  KEY(+CL2:Str1) 
StrKey2 KEY(+CL2:Str2) 
AMemo   MEMO(100), NAME('mem') 
Record  RECORD 
Num      STRING(@n-_9.2) 
## STR1     STRING(2)
## STR2     STRING(2)
Mem      STRING(10) 
        END 
      END 
The following commands copy this file definition to A: 


---

Database Drivers and Interfaces 
87 
COPY(Clar2,'A:\CLAR2') 
COPY(Clar2,'StrKey|A:\STRKEY') 
COPY(Clar2,'StrKey2|A:\STRKEY2') 
COPY(Clar2,'NumKey|A:\NUMKEY') 
After these calls, the following files would exist on drive A: CLAR2.DBF, CLAR2.DBT, 
STRKEY.NDX, STRKEY2.NDX, and NUMKEY.NDX. 
5      You do not need SHARE (or VSHARE) in any environment (for example, Novell) that 
supplies file locking as part of the operating system. 
6      The ADD statement tests for duplicate keys before modifying the data file or its 
associated KEY files. Consequently it is slower than APPEND which performs no checks 
and does not update KEYs. When adding large amounts of data to a database use 
APPEND...BUILD in preference to ADD. 
7      dBase IV performs record locking by locking the entire record within the data file. This 
prevents read access to other processes. Therefore we recommend minimizing the 
amount of time for which a record is held. 
8      Although the driver supports these functions, we do not recommend their use. They must 
physically access the files and add overhead. Instead, test the value returned by 
ERRORCODE() after each sequential access. NEXT or PREVIOUS post Error 33 
(Record Not Available) if an attempt is made to access a record beyond the end or 
beginning of the file. 
9      There is no distinction between file pointers and key pointers; they both return the record 
number for any given record. 
10     POSITION(file) returns a STRING(12). POSITION(key) returns a STRING containing the 
size of the key fields + 4 bytes. 
11     Under dBase IV, the RECORDS() function reports the same number of records for the 
data file and its keys and indexes. Usually there will be no difference in the number of 
records unless the INDEX is out of date. Because the DELETE statement does not 
physically remove records, the number of records reported by the RECORDS() function 
includes inactive records. Exercise care when using this function.The field names must 
appear as specified in the fields' NAME() attribute if supplied, or must be the label name. 
A prefix may be used for compatibility with the Clarion conventions but is ignored.  
12      THREADed files consume additional file handles for each thread that accesses the file. 


---

Database Drivers 
88 
dBaseIV:Other 
International Sort Sequence 
dBase IV sorts as if there were no diacritics in a field, thus A is sorted the same as Ä. If two words 
are identical except for diacritic characters, then the words are sorted as though the diacritic 
character was greater than the normal character. For example Äa < Ab < Äb whereas a 
CLADIGRAPH of ÄAE will sort as Ab < Äa < Äb. Solution- if the same file is used in Clarion and 
dBase IV, issue a BUILD statement rebuild the keys before updating the file (reading the file 
causes no problems). 
Boolean Evaluation 
dBase IV allows a logical field to accept one of 11 possible values (1,0,y,Y,n,N,t,T,f,F or a space 
character). The space character is neither true nor false. When using a logical field from a 
preexisting database in a logical expression, account for all these possibilities. Remember that 
when a STRING field is used as an expression, it is true if it contains any data and false if it is 
equal to zero or blank. Therefore, to evaluate a Logical field's truth, the expression should be true 
if the field contains any of the "true" characters (T,t,Y, or y). For example, if a Logical field were 
used to specify a product as taxable or nontaxable, the expression to evaluate its truth would be:  
(If Condition):   
    Taxable='1' OR Taxable='T' OR Taxable='t' OR Taxable='Y' OR Taxable='y' 
 
Large MEMOs 
Clarion supports MEMO fields up to a maximum of 64K. If you have an existing file which 
includes a memo greater than 64K, you can use the file but not modify the large MEMOs. 
You can determine when your application encounters a large MEMO by detecting when the 
memo pointer variable is non-blank, but the memo appears to be blank. Error 47 (Bad Record 
Declaration) is posted, and any modification to the MEMO field is ignored. 
Long Field Names 
dBase IV supports a maximum of 10 characters in a field name. If you require more, use an 
External Name with 10 characters or less.  
Key Definition 
dBase IV supports the use of expressions to define keys. Within the Dictionary Editor, you can 
place the expression in the external name field in the Key Properties dialog. The general format 
of the external name is :  
'FileName=T[Expression]' 
Where FileName represents the name of the index file (which can contain a path and file 
extension), and T represents the type of the index. Valid types are: C = character, D = date, and 
N = numeric. If the type is D or N then Expression can name only one field. 
Multiple-index (.MDX) files require the NAME() attribute on a KEY or INDEX to specify the 
storage type of the key and any expression used to generate the key values. The general format 
of the NAME() attribute on a KEY or INDEX is: 
    NAME('TagName|FileName[PageSize]=T[Expression],FOR[Expression]') 


---

Database Drivers and Interfaces 
89 
The following documents the parameters for the NAME() attribute: 
TagName 
Specifies the name of an index tag within a multiple index file. If omitted 
the driver creates a dBase IV style .NDX file using the name specified in 
FileName. 
FileName 
Specifies the name of the index file, which may contain a path and 
extension. 
PageSize 
Specifies that when creating a .MDX file, (if a TagName is specified), a 
number in the range 2-32 specifying the number of 512-byte blocks in 
each index page. This value is only used when creating the file. If you 
specify multiple values with declarations for different tags in the same 
.MDX file, the largest value will be selected. The default value is 2. 
T 
Specifies the type of index. Legal types are C = character, D = date, N = 
numeric. If the type is D or N then Expression may name only one field. 
Expression 
Specifies an expression to generate the index. It may refer to multiple 
fields and invoke multiple xBase functions. The functions currently 
supported are listed below. Square brackets must enclose the 
expression. 
Elements of the NAME() attribute may be omitted from the right. When specifying an 
Expression, you must also specify the type and name. If the Expression is omitted, the 
driver determines the Expression from the key fields when the file is created, or from the 
index file when opened. 
If the type is omitted, the driver determines the index type from the first key component 
when the file is created, or from the index file when opened. 
If the NAME() attribute is omitted altogether, the index file name is determined from the 
key label. The path defaults to the same location as the .DBF. 
Tag names are limited to 9 characters in length. If the supplied name is too long it is 
automatically truncated. 
Specify all field names in the NAME() attribute without a prefix. 
 
dBase IV additionally supports the use of the Xbase FOR statement in expressions to define 
keys. The expressions supported in the FOR condition must be a simple condition of the form: 
expression comparison_op expression 
comparison_op may be <, <=, =<, <>, =, =>, >= or >. 
The expression may refer to multiple fields in the record and contain xBase functions. 
Square brackets must enclose the expression. The currently supported functions appear 
below. If the driver encounters an unsupported Xbase function in a preexisting file, it 
posts error 76 'Invalid Index String' when the file is opened for keys and static indexes. 
String expressions may use the '+' operator to concatenate multiple string arguments. 
Numeric expressions use the '+' or '-' operators with their conventional meanings. The 
maximum length of a dBase IV expression is 250 characters. 


---

Database Drivers 
90 
Supported xBase Key Definition Functions 
ALLTRIM(string) 
Removes leading and trailing spaces. 
CTOD(string) 
Converts a string key to a date. The string must be in the format 
mm/dd/yy; the result takes the form 'yyyymmdd'. The yyyy element 
of the date defaults to the twentieth century. An invalid date results 
in a key containing blanks. 
## DELETED()
Returns TRUE if the record is deleted. 
DTOC(date) 
Converts a date key to string format 'mm/dd/yy.' 
DTOS(date) 
Converts a date key to string format 'yyyymmdd.' 
FIXED(float) 
Converts a float key to a numeric. 
FLOAT(numeric) 
Converts a numeric key to a float. 
IIF(bool,val1,val2) 
Returns val1 if the first parameter is TRUE, otherwise returns val2. 
LEFT(string, n) 
Returns the leftmost n characters of the string key as a string of 
length n. 
LOWER(string) 
Converts a string key to lower case. 
LTRIM(string) 
Removes spaces from the left of a string. 
## RECNO()
Returns the current record number. 
RIGHT(string, n) 
Returns the rightmost n characters of the string key as a string of length n. 
RTRIM(string) 
Removes spaces from the right of a string. 
STR(numeric[,length[,decimal places]]) 
Converts a numeric to a string. The length of 
the string and the number of decimal places 
are optional. The default string length is 10, 
and the number of decimal places is 0. 
SUBSTR(string,offset,n) Returns a substring of the string key starting at offset and of n 
characters in length. 
TRIM(string) 
Removes spaces from the right of a string (identical to RTRIM). 
UPPER(string) 
Converts a string key to upper case. 
VAL(string) 
Converts a string key to a numeric. 
 


---

Database Drivers and Interfaces 
91 


---

Database Drivers 
92 
DOS Database Driver 
 
DOS:Specifications 
The DOS file driver reads and writes any binary, byte-addressable files. Neither fields nor records 
are delimited. When reading a record, the driver reads the number of bytes defined in the file's 
RECORD structure, unless a length parameter is specified in the GET statement. 
The DOS driver supports the length parameter for the ADD, APPEND, GET, and PUT 
statements; this allows for variable length records in a DOS file. 
The POINTER function returns the relative byte position within the file of the beginning of the last 
record accessed by an ADD, APPEND, GET, or NEXT statement. 
This file driver performs forward sequential processing only. No key or transaction processing 
functions are supported, and the PREVIOUS statement is not supported. 
 
Due to its limitations, the main function of this driver is as a disk editor for binary files. 
Files: 
## CLADOSL.LIB
Windows Static Link Library 
 
## CLADOS.LIB
Windows Export Library 
 
## CLADOS.DLL
Windows Dynamic Link Library (32-bit) 
DOS:Data Types 
## BYTE
## DECIMAL
## SHORT
## PDECIMAL
## USHORT
## STRING
## LONG
## CSTRING
## ULONG
## PSTRING
## SREAL
## DATE
## REAL
## TIME
## BFLOAT4
## GROUP
## BFLOAT8
 
DOS:File Specifications/Maximums 
File Size:            4,294,967,295 
Records per File:     4,294,967,295 
Record Size:          64K 
Field Size:           64K 
Fields per Record:    64K 
Keys/Indexes per File:n/a 
Key Size:             n/a 
Memo fields per File: n/a 
Memo Field Size:      n/a 
Open Data Files:      Operating system dependent 
 
 


---

Database Drivers and Interfaces 
93 
DOS:Driver Strings 
There are switches or "driver strings" you can set to control the way your application creates, 
reads, and writes files with a specific driver. Driver strings are simply messages or parameters 
that are sent to the file driver at run-time to control its behavior. See Common Driver Features--
Driver Strings for an overview of these runtime Database Driver switches and parameters. 
 
 
Some driver strings have no effect after the file is open, so no SEND function syntax is 
listed for those strings. However, the SEND function syntax to return the value of the 
switch is listed for all driver strings.  
The DOS Driver supports the following Driver Strings: 
## FILEBUFFERS
 
DRIVER('DOS', '/FILEBUFFERS = n' ) 
[ Buffers" = ] SEND(file, 'FILEBUFFERS [ = n ]' ) 
Sets the size of the buffer used to read and write to the file, where the buffer size is (n * 512 
bytes). Use the /FILEBUFFERS driver string to increase the buffer size if access is slow. 
Maximum buffer size is 4,294,967,264. SEND returns the size of the buffer in bytes. 
 
 
The default buffer size for files opened denying write access to other users is the larger of 
1024 or (2 * record size), and the larger of 512 or record size for all other open modes.  
## QUICKSCAN
 
DRIVER('DOS', '/QUICKSCAN = on | off' ) 
[ QScan" = ] SEND(file, 'QUICKSCAN [ = on | off ]' ) 
Specifies buffered access behavior. The DOS driver reads a buffer at a time (not a record), 
allowing faster access. In a multi-user environment these buffers are not 100% trustworthy for 
subsequent access, because another user may change the file between accesses. As a 
safeguard, the driver rereads the buffers before each record access. To disable the reread, set 
QUICKSCAN to ON. The default is ON for files opened denying write access to other users, and 
OFF for all other open modes. SEND returns the Quickscan setting (ON or OFF) in the form of a 
## STRING(3).
 


---

Database Drivers 
94 
DOS:Supported Commands and Attributes 
 
 
File Attributes 
Supported 
 
## CREATE
Y 
 
DRIVER(filetype [,driver string]) 
Y 
 
## NAME
Y 
 
## ENCRYPT
N 
 
OWNER(password) 
N 
 
## RECLAIM
N 
 
PRE(prefix) 
Y 
 
## BINDABLE
Y 
 
## THREAD
Y4 
 
EXTERNAL(member) 
Y 
 
DLL([flag]) 
Y 
 
OEM 
Y 
 
## LOCALE
Y 
 
File Structures 
Supported 
 
## INDEX
N 
 
KEY 
N 
 
## MEMO
N 
 
## BLOB
N 
 
## RECORD
Y 
 
 
Index, Key, Memo Attributes 
Supported 
 
## BINARY
N 
 
DUP 
N 
 
## NOCASE
N 
 
OPT 
N 
 
## PRIMARY
N 


---

Database Drivers and Interfaces 
95 
 
## NAME
N 
 
Ascending Components 
N 
 
Descending Components 
N 
 
Mixed Components 
N 
 
 
Field Attributes 
Supported 
 
DIM 
Y 
 
## OVER
Y 
 
## NAME
Y 
 
 
File Procedures 
Supported 
 
BOF(file) 
N 
 
BUFFER(file) 
N 
 
BUILD(file) 
N 
 
BUILD(key) 
N 
 
BUILD(index) 
N 
 
BUILD(index, components) 
N 
 
BUILD(index, components, filter) 
N 
 
BYTES(file) 
Y 
 
CLOSE(file) 
Y 
 
COPY(file, new file) 
Y 
 
CREATE(file) 
Y 
 
DUPLICATE(file) 
N 
 
DUPLICATE(key) 
N 
 
EMPTY(file) 
Y 
 
EOF(file) 
Y 
 
FLUSH(file) 
Y 
 
LOCK(file) 
Y 
 
NAME(label) 
Y 


---

Database Drivers 
96 
 
OPEN(file, access mode) 
Y 
 
PACK(file) 
N 
 
POINTER(file) 
Y2 
 
POINTER(key) 
N 
 
POSITION(file) 
Y3 
 
POSITION(key) 
N 
 
RECORDS(file) 
Y 
 
RECORDS(key) 
N 
 
REMOVE(file) 
Y 
 
RENAME(file, new file) 
Y 
 
SEND(file, message) 
Y 
 
SHARE(file, access mode) 
Y 
 
STATUS(file) 
Y 
 
STREAM(file) 
N 
 
UNLOCK(file) 
Y 
 
 
Record Access 
Supported 
 
ADD(file) 
Y 
 
ADD(file, length) 
Y 
 
APPEND(file) 
Y 
 
APPEND(file, length) 
Y 
 
DELETE(file) 
N 
 
GET(file,key) 
N 
 
GET(file, filepointer) 
Y 
 
GET(file, filepointer, length) 
Y 
 
GET(key, keypointer) 
N 
 
HOLD(file) 
N 
 
NEXT(file) 
Y 
 
NOMEMO(file) 
N 


---

Database Drivers and Interfaces 
97 
 
PREVIOUS(file) 
Y 
 
PUT(file) 
Y 
 
PUT(file, filepointer) 
Y1 
 
PUT(file, filepointer, length) 
Y1 
 
RELEASE(file) 
N 
 
REGET(file,string) 
Y 
 
REGET(key,string) 
N 
 
RESET(file,string) 
Y 
 
RESET(key,string) 
N 
 
SET(file) 
Y  
 
SET(file, key) 
N 
 
SET(file, filepointer) 
Y 
 
SET(key) 
N 
 
SET(key, key) 
N 
 
SET(key, keypointer) 
N 
 
SET(key, key, filepointer) 
N 
 
SKIP(file, count) 
N 
 
WATCH(file) 
N 
 
 
Transaction Processing 
Supported 
 
LOGOUT(timeout, file, ..., file) 
N 
 
## COMMIT
N 
 
## ROLLBACK
N 
 
 
Null Data Processing 
Supported 
 
NULL(field) 
N 
 
SETNULL(field) 
N 
 
SETNULL(file,field) 
N 
 
SETNONNULL(field) 
N 


---

Database Drivers 
98 
Notes 
1      When using PUT() with this driver you should take care to PUT back the same number of 
characters that were read. If you PUT back more characters than were read, then the 
"extra" characters will overwrite the first part of the subsequent record. If you PUT back 
fewer characters than were read, then only the first part of the retrieved record is 
overwritten, while the last part of the retrieved record remains as it was prior to the PUT(). 
2      POINTER() returns the relative byte position within the file. 
3      POSITION(file) returns a STRING(4). 
4      THREADed files consume additional file handles for each thread that accesses the file. 


---

Database Drivers and Interfaces 
99 


---

Database Drivers 
100 
FoxPro / FoxBase Database Driver 
 
FoxPro:Specifications 
The FoxPro file driver is compatible with FoxPro and FoxBase. The default data file extension is *.DBF. 
The default index file extension is *.IDX. The default Memo file extension is .FBT. FoxPro also 
supports multiple index files, whose default extension is *.CDX. The miscellaneous section 
describes the procedures for using the .CDX files. 
Files: 
## CLAFOXL.LIB
Windows Static Link Library 
 
## CLAFOX.LIB
Windows Export Library 
 
## CLAFOX.DLL
Windows Dynamic Link Library 
 
 
The FoxPro index file format is the backbone of its vaunted "Rushmore" technology. The 
old saying "There's no free lunch," however, applies. Adding and appending records to a 
large database is a slower process than in other xBase formats, due to the time required to 
update the index file. 
 FoxPro:Data Types 
The xBase file format stores all data as ASCII strings. You may either specify STRING types with 
declared pictures for each field, or specify native Clarion types, which the driver converts 
automatically. 
FoxPro data type 
Clarion data type 
STRING w/ picture 
*Date 
## DATE
## STRING(@D12)
*Numeric 
## REAL
STRING(@N-_p.d) 
*Logical 
## BYTE
## STRING(1)
Character 
## STRING
## STRING
*Memo 
## MEMO
## MEMO
If your application reads and writes to existing files, a pictured STRING will suffice. However, if 
your application creates a FoxPro or FoxBase file, you may require additional information for 
these FoxPro and FoxBase types: 
*      To create a numeric field in the Data Dictionary, choose the REAL data type. In the 
External Name field on the Attributes tab, specify 
'NumericFieldName=N(Precision,DecimalPlaces)' where NumericFieldName is the name 
of the field, Precision is the precision of the field and DecimalPlaces is the number of 
decimal places. With a REAL data type, you cannot access the Character or Places fields 
in the Field definition, you must specify those attributes with an expression in the External 
Name Field on the Attributes tab. 
For example, if you want to create a field called Number with nine significant digits and 
two decimal places, enter 'Number=N(9,2) in the External Name field on the Attributes 
tab of the Field properties in the Data Dictionary. 
If you're hand coding a native Clarion data type, add the NAME attribute using the same 
syntax.  
If you're hand coding a STRING with picture, STRING(@N-_9.2), NAME('Number'), 
where Number is the field name. 


---

Database Drivers and Interfaces 
101 
*      To create a logical field, using the data dictionary, choose the BYTE data type. There are 
no special steps; however, see the miscellaneous section for tips on reading the data 
from the field. 
If you're hand coding a STRING with picture, add the NAME attribute: STRING(1), 
NAME('LogFld = L'). 
*      To create a date field, using the data dictionary, choose the DATE data type, rather than 
LONG, which you usually use for the TopSpeed or Clarion file formats. 
*      MEMO field declarations require the a pointer field in the file's record structure. Declare 
the pointer field as a STRING(10) or a LONG. This field will be stored in the .DBF file 
containing the offset of the memo in the .DBT file. The MEMO declaration must have a 
NAME() attribute naming the pointer field. An example file declaration follows: 
File  FILE, DRIVER('FoxPro') 
Memo1  MEMO(200),NAME('Notes') 
Memo2  MEMO(200),NAME('Text') 
Rec    RECORD 
Mem1Ptr LONG,NAME('Notes') 
Mem2Ptr STRING(10),NAME('Text') 
       END 
      END 
FoxPro:File Specifications/Maximums 
File Size:             2,000,000,000 bytes 
Records per File:      1,000,000,000 bytes 
Record Size:           4,000 bytes 
Field Size 
  Character:           254 bytes 
  Date:                8 bytes 
  Logical:             1 byte 
  Numeric:             20 bytes including decimal point 
  Float:               20 bytes including decimal point 
  Memo:                65,520 bytes (see note) 
Fields per Record:     512 
Field Name:            10 characters 
Keys/Indexes per File: No Limit 
Key Sizes 
  Character:           100 bytes (.IDX) 
                       254 bytes (.CDX) 
  Numeric, Date:       8 bytes 
Memo fields per File:  Dependent on available memory 
Open Files:            Operating system dependent 


---

Database Drivers 
102 
FoxPro:Driver Strings 
There are switches or "driver strings" you can set to control the way your application creates, 
reads, and writes files with a specific driver. Driver strings are simply messages or parameters 
that are sent to the file driver at run-time to control its behavior. See Common Driver Features--
Driver Strings for an overview of these runtime Database Driver switches and parameters. 
 
Some driver strings have no effect after the file is open, so no SEND function syntax is 
listed for those strings. However, the SEND function syntax to return the value of the 
switch is listed for all driver strings.  
The FoxPro Driver supports the following Driver Strings: 
## BUFFERS
 
DRIVER('FOXPRO', '/BUFFERS = n' ) 
[ Status" = ] SEND(file, 'BUFFERS [ = n ]' ) 
Sets the size of the buffer used to read and write to the file, where the buffer size is (n * 512 
bytes). Use the /BUFFERS driver string to increase the buffer size if access is slow. Maximum 
buffer size is 4,294,967,264. SEND returns the size of the buffer in bytes. 
 
The default is three buffers of 1024 bytes each. Increasing the number of buffers will not 
increase performance when a file is shared by multiple users. 
## RECOVER
 
## DRIVER('FOXPRO', '/RECOVER' )
[ Status" = ] SEND(file, 'RECOVER' ) 
Equivalent to the Xbase RECALL command, which recovers records marked for deletion. When 
using the FoxPro driver, the DELETE statement flags a record as "inactive." The driver does not 
remove the record until the PACK command is executed. 
RECOVER is evaluated each time you open the file if you add the driver string to the data 
dictionary. When the driver recovers the records previously marked for deletion, you must 
manually rebuild keys and indexes with the BUILD statement. 
## IGNORESTATUS
 
DRIVER('FOXPRO', '/IGNORESTATUS = on | off ' ) 
[ Status" = ] SEND(file, 'IGNORESTATUS [ on | off ]' ) 
When set on, the driver does not skip deleted records when accessing the file with GET, NEXT, 
and PREVIOUS in file order. It also enables a PUT on a deleted or held record. IGNORESTATUS 
requires opening the file in exclusive mode. SEND returns the IGNORESTATUS setting (ON or 
OFF) in the form of a STRING(3). 


---

Database Drivers and Interfaces 
103 
## DELETED
 
[ Status" = ] SEND(file, 'DELETED' ) 
For use only with the SEND command, when IGNORESTATUS is on. Returns the status of the 
current record. If deleted, the return string is "ON" and if not, "OFF."  
## ZEROY2K
 
DRIVER('FOXPRO', '/ZEROY2K = on | off' ) 
[ Status" = ] SEND(file, 'ZEROY2K [ on | off ]' ) 
In the header of FoxPro files there is a field that stores the year that the file was last edited. Some 
applications store this as the number of years since 1900. Others store it as a 2 digit year. So for 
dates in the year 2000 some applications store 0 in this field and others 100. Clarion will read files 
with either. However it will write 100. Writing 100 may make the files unreadable by products that 
only support 0. To change this behavior you can with use a driver string of ZEROY2K, a SEND 
command or a setting in the WIN.INI file. 
 
The driver will store 0 in the DBF file header when the WINI.INI setting is set to 1 or 'on' in a 
SEND command or driver string, otherwise a 100 will be stored in the DBF file header. 
 
  
The SEND command causes the setting to be set for all files that use that driver, not just 
for that file. 
Example: 
## WIN.INI:
 ;Sets all FoxPro files to store a 0 in the DBF file header 
## [CWFOXPRO]
## ZEROY2K=1
 
SEND command: 
!sets Orders file to store 0 in the DBF file header: 
SEND('Orders', ZEROY2K='on' ) 
!sets Orders file to store 100 in the DBF file header: 
SEND('Orders', ZEROY2K='off') 
 
Driver String: 
!SETS Orders file to store 0  
 Orders FILE, DRIVER('FOXPRO', '/ZEROY2K=on'),PRE(ORD)   
 


---

Database Drivers 
104 
FoxPro:Supported Commands and Attributes 
 
 
File Attributes 
Supported 
 
## CREATE
Y 
 
DRIVER(filetype [,driver string]) 
Y 
 
## NAME
Y 
 
## ENCRYPT
N 
 
OWNER(password) 
N 
 
## RECLAIM
N1 
 
PRE(prefix) 
Y 
 
## BINDABLE
Y 
 
## THREAD
Y13 
 
EXTERNAL(member) 
Y 
 
DLL([flag]) 
Y 
 
OEM 
N2 
 
## LOCALE
Y 
 
File Structures 
Supported 
 
## INDEX
Y 
 
KEY 
Y 
 
## MEMO
Y 
 
## BLOB
N 
 
## RECORD
Y 
 
 
Index, Key, Memo Attributes 
Supported 
 
## BINARY
N14 
 
DUP 
Y3 
 
## NOCASE
Y 
 
OPT 
N 
 
## PRIMARY
Y 


---

Database Drivers and Interfaces 
105 
 
## NAME
Y 
 
Ascending Components 
Y 
 
Descending Components 
Y 
 
Mixed Components 
N 
 
 
Field Attributes 
Supported 
 
DIM 
N 
 
## OVER
Y 
 
## NAME
Y 
 
 
File Procedures 
Supported 
 
BOF(file) 
Y9 
 
BUFFER(file) 
N 
 
BUILD(file) 
Y 
 
BUILD(key) 
Y 
 
BUILD(index) 
Y 
 
BUILD(index, components) 
Y4 
 
BUILD(index, components, filter) 
N 
 
BYTES(file) 
N 
 
CLOSE(file) 
Y 
 
COPY(file, new file) 
Y5 
 
CREATE(file) 
Y 
 
DUPLICATE(file) 
Y 
 
DUPLICATE(key) 
Y 
 
EMPTY(file) 
Y 
 
EOF(file) 
Y9 
 
FLUSH(file) 
Y 
 
LOCK(file) 
N 
 
NAME(label) 
Y 


---

Database Drivers 
106 
 
OPEN(file, access mode) 
Y6 
 
PACK(file) 
Y 
 
POINTER(file) 
Y10 
 
POINTER(key) 
Y10 
 
POSITION(file) 
Y11 
 
POSITION(key) 
Y11 
 
RECORDS(file) 
Y12 
 
RECORDS(key) 
Y12 
 
REMOVE(file) 
Y 
 
RENAME(file, new file) 
Y5 
 
SEND(file, message) 
Y 
 
SHARE(file, access mode) 
Y6 
 
STATUS(file) 
Y 
 
STREAM(file) 
Y 
 
UNLOCK(file) 
Y 
 
 
Record Access 
Supported 
 
ADD(file) 
Y7 
 
ADD(file, length) 
N 
 
APPEND(file) 
Y7 
 
APPEND(file, length) 
N 
 
DELETE(file) 
Y1 
 
GET(file,key) 
Y 
 
GET(file, filepointer) 
Y 
 
GET(file, filepointer, length) 
N 
 
GET(key, keypointer) 
Y 
 
HOLD(file) 
Y8 
 
NEXT(file) 
Y 
 
NOMEMO(file) 
Y 


---

Database Drivers and Interfaces 
107 
 
PREVIOUS(file) 
Y 
 
PUT(file) 
Y 
 
PUT(file, filepointer) 
Y 
 
PUT(file, filepointer, length) 
N 
 
RELEASE(file) 
Y 
 
REGET(file,string) 
Y 
 
REGET(key,string) 
Y 
 
RESET(file,string) 
Y 
 
RESET(key,string) 
Y 
 
SET(file) 
Y  
 
SET(file, key) 
Y 
 
SET(file, filepointer) 
Y 
 
SET(key) 
Y 
 
SET(key, key) 
Y 
 
SET(key, keypointer) 
Y 
 
SET(key, key, filepointer) 
Y 
 
SKIP(file, count) 
Y 
 
WATCH(file) 
Y 
 
 
Transaction Processing 
Supported 
 
LOGOUT(timeout, file, ..., file) 
N 
 
## COMMIT
N 
 
## ROLLBACK
N 
 
 
Null Data Processing 
Supported 
 
NULL(field) 
N 
 
SETNULL(field) 
N 
 
SETNULL(file,field) 
N 
 
SETNONNULL(field) 
N 


---

Database Drivers 
108 
Notes: 
1      When the driver deletes a record from a FoxPro database, the record is not physically 
removed, instead the driver marks it inactive. Memo fields are not physically removed 
from the memo file, however they cannot be retrieved if they refer to an inactive record. 
Key values are removed from the index files. To remove records and memo fields 
permanently, execute a PACK(file). 
 
 
To those programmers familiar with FoxPro, this driver processes deleted records 
consistent with the way FoxPro processes them after the SET DELETED ON 
command is issued. Records marked for deletion are ignored from processing by 
executable code statements, but remain in the data file. 
2      If you need to access FoxPro data with alternate characters stored using a non-English 
version of FoxPro, then you should use ODBC. However, if you do not have any string 
based kesys, you can use the FoxPro driver and call the ConvertOEMToANSI and 
ConvertANSIToOEM after retrieving and before updating a record. 
3      In FoxPro it is legal to enter multiple records with duplicates of the unique key 
components. However, only the first of these records is indexed. So processing in key 
order only shows this first record. If you delete a record, then enter a new record with the 
same key value, the key file continues to point at the deleted record rather than the new 
record. In this situation, the FoxPro file driver changes the key file to point at the active 
record rather than the deleted record. This means that if you use a FoxPro program to 
delete a unique record, then insert a duplicate of this record, the new record is invisible 
when processing in key order until a pack is done. If you do the same process in a 
Clarion program, the new record is visible when processing in key order. 
4      When building dynamic indexes, the components may take one of two forms: 
   BUILD(DynNdx, '+Pre:FLD1, -Pre:FLD2') 
This form specifies the names of the fields on which to build the index. The field names 
must appear as specified in the fields' NAME() attribute if supplied, or must be the label 
name. A prefix may be used for compatibility with Clarion conventions but is ignored. 
   BUILD(DynNdx, 'T[Expression]') 
This form specifies the type and Expression used to build an index--see Miscellaneous--
Key Definition for more information. 
5      These commands copy data and memo files using newfile, which may specify a new file 
name or directory. Key or index files are copied if the newfile is a subdirectory 
specification. To copy an index file to a new file, use a special form of the copy 
command: 
    COPY(file,'<index>|<newfile>') 
This returns File Not Found if an invalid index is passed. The COPY command assumes 
a default extension of .IDX for both the source and the target file names if none is 
specified. If you require a file name without an extension, terminate the name with a 
period. Given the file structure: 
  Clar2  FILE,CREATE,DRIVER('FoxPro'),PRE(CL2) 
  NumKey   KEY(+CL2:Num),DUP 
  StrKey   KEY(+CL2:Str1) 
  StrKey2  KEY(+CL2:Str2) 
  AMemo    MEMO(100), NAME('mem') 
  Record   RECORD 
  Num       STRING(@n-_9.2) 
## STR1      STRING(2)


---

Database Drivers and Interfaces 
109 
## STR2      STRING(2)
  Mem       STRING(10) 
           END 
         END 
The following commands copy this file definition to A: 
  COPY(Clar2,'A:\CLAR2') 
  COPY(Clar2,'StrKey|A:\STRKEY') 
  COPY(Clar2,'StrKey2|A:\STRKEY2') 
  COPY(Clar2,'NumKey|A:\NUMKEY') 
After these calls, the following files would exist on drive A: CLAR2.DBF, CLAR2.FPT, 
STRKEY.IDX, STRKEY2.IDX, and NUMKEY.IDX. 
6      You do not need SHARE (or VSHARE) in any environment (for example, Novell) that 
supplies file locking as part of the operating system. 
7      The ADD statement tests for duplicate keys before modifying the data file or its 
associated KEY files. Consequently it is slower than APPEND which performs no checks 
and does not update KEYs. When adding large amounts of data to a database use 
APPEND...BUILD in preference to ADD. 
8      FoxPro performs record locking by locking the entire record within the data file. This 
prevents read access to other processes. Therefore we recommend minimizing the 
amount of time for which a record is held. 
9      Although the driver supports these functions, we do not recommend their use. They must 
physically access the files and they are slow. Instead, test the value returned by 
ERRORCODE() after each sequential access. NEXT or PREVIOUS post Error 33 
(Record Not Available) if an attempt is made to access a record beyond the end or 
beginning of the file. 
10    There is no distinction between file pointers and key pointers; they both return the record 
number for the given record. 
11    POSITION(file) returns a STRING(12). POSITION(key) returns a STRING the size of the 
key fields + 4 bytes. 
12    Under FoxPro, the RECORDS() function reports the same number of records for the data 
file and its keys and indexes. Usually there will be no difference in the number of records 
unless the INDEX is out of date. Because the DELETE statement does not physically 
remove records, the number of records reported by the RECORDS() function includes 
inactive records. Exercise care when using this function.The field names must appear as 
specified in the fields' NAME() attribute if supplied, or must be the label name. A prefix 
may be used for compatibility with the Clarion conventions but is ignored. 
13    THREADed files consume additional file handles for each thread that accesses the file. 
14 OEM conversion is not applied to BINARY MEMOs. The driver assumes BINARY MEMOs 
are zero padded; otherwise, space padded. 


---

Database Drivers 
110 
FoxPro:Other 
Boolean Evaluation 
FoxPro and FoxBase allow a logical field to accept one of 11 possible values (0,1,y,Y,n,N,t,T,f,F 
or a space character). The space character is neither true nor false. When using a logical field 
from a preexisting database in a logical expression, account for all these possibilities. Remember 
that when a STRING field is used as an expression, it is true if it contains any data and false if it 
is equal to zero or blank. Therefore, to evaluate a Logical field's truth, the expression should be 
true if the field contains any of the "true" characters (1,T,t,Y, or y). For example, if a Logical field 
were used to specify a product as taxable or nontaxable, the expression to evaluate its truth 
would be:  
(If Condition): 
    Taxable='1' OR Taxable='T' OR Taxable='t' OR Taxable='Y' OR Taxable='y' 
 
Large MEMOs 
FoxPro supports MEMO fields up to a maximum of 64K. If you have an existing file which 
includes a memo greater than 64K, you can use the file but not modify the large MEMOs. 
You can determine when your application encounters a large MEMO by detecting when the 
memo pointer variable is non-blank, but the memo appears to be blank. Error 47 (Bad Record 
Declaration) is posted, and any modification to the MEMO field is ignored. 
Long Field Names 
FoxPro and FoxBase support a maximum of 10 characters in a field name. If you require more, 
use an External Name with 10 characters or less.  
Key Definition 
FoxPro and FoxBase support the use of expressions to define keys. Within the Dictionary 
Editor, you can place the expression in the external name field in the Key Properties 
dialog. The general format of the external name is :  
'FileName=T[Expression]' 
Where FileName represents the name of the index file (which can contain a path and file 
extension), and T represents the type of the index. Valid types are: C = character, D = 
date, and N = numeric. If the type is D or N then Expression can name only one field. 
Multiple-index (.CDX) files require the NAME() attribute on a KEY or INDEX to specify the 
storage type of the key and any expression used to generate the key values. The general 
format of the NAME() attribute on a KEY or INDEX is: 
    NAME('TagName|FileName=T[Expression],COMPRESSED') 
The following are the parameters for the NAME() attribute: 
TagName 
Names an index tag within a multiple index file. If the TagName is 
omitted the driver creates an .IDX file with the name specified in 
FileName. 
 
 


---

Database Drivers and Interfaces 
111 
FileName 
Names the index file, and optionally contains a path and 
extension. 
T 
Specifies the type of the index; legal types are C = character, D = 
date, N = numeric. If the type is D or N then Expression may 
name only one field. 
Expression 
Specifies the expression used to generate the index. The 
expression may refer to multiple fields, and invoke multiple of 
xBase functions. The functions currently supported are listed 
below. Square brackets must enclose the expression. 
## COMPRESSED
When specified, the FoxPro Driver creates a FoxPro 2 compatible 
compressed .IDX file. 
Elements of the NAME() attribute may be omitted from the right. When specifying an 
Expression, the type and name must also be specified. If the Expression is omitted, the 
driver determines the Expression from the key fields when the file is created, or from the 
index file when opened. 
If the type is omitted, the driver determines the index type from the first key component 
when the file is created, or from the index file when opened. 
If the NAME() attribute is omitted altogether, the index file name is determined from the 
key label. The path defaults to the same location as the .DBF. 
Tag names are limited to 10 characters in length; if the supplied name is too long it is 
automatically truncated. 
All field names in the NAME() attribute must be specified without a prefix. 
FoxPro additionally supports the use of the Xbase FOR statement in expressions to 
define keys. The expressions supported in the FOR condition must be a simple condition 
of the form: 
    expression comparison_op expression 
comparison_op may be one of the following: <, <=, =<, <>, =, =>, >= or >. 
The expression may refer to multiple fields in the record, and contain xBase functions. 
Square brackets must enclose the expression. The currently supported functions appear 
below. If the driver encounters an unsupported Xbase function in a preexisting file, it 
posts error 76 'Invalid Index String' when the file is opened for keys and static indexes. 
String expressions may use the '+' operator to concatenate multiple string arguments. 
Numeric expressions use the '+' or '-' operators with their conventional meanings. The 
maximum length of a FoxPro or FoxBase expression is 250 characters. 


---

Database Drivers 
112 
Supported xBase Key Definition Functions 
ALLTRIM(string) 
Removes leading and trailing spaces. 
CTOD(string) 
Converts a string key to a date. The string must be in the format 
mm/dd/yy; the result takes the form 'yyyymmdd'. The yyyy element 
of the date defaults to the twentieth century. An invalid date results 
in a key containing blanks. 
## DELETED()
Returns TRUE if the record is deleted. 
DTOC(date) 
Converts a date key to string format 'mm/dd/yy.' 
DTOS(date) 
Converts a date key to string format 'yyyymmdd.' 
FIXED(float) 
Converts a float key to a numeric. 
FLOAT(numeric) 
Converts a numeric key to a float. 
IIF(bool,val1,val2) 
Returns val1 if the first parameter is TRUE, otherwise returns val2. 
LEFT(string, n) 
Returns the leftmost n characters of the string key as a string of 
length n. 
LOWER(string) 
Converts a string key to lower case. 
LTRIM(string) 
Removes spaces from the left of a string. 
## RECNO()
Returns the current record number. 
RIGHT(string, n) 
Returns the rightmost n characters of the string key as a string of length n. 
RTRIM(string) 
Removes spaces from the right of a string. 
STR(numeric[,length[,decimal places]]) 
Converts a numeric to a string. The length of 
the string and the number of decimal places 
are optional. The default string length is 10, 
and the number of decimal places is 0. 
SUBSTR(string,offset,n) Returns a substring of the string key starting at offset and of n 
characters in length. 
TRIM(string) 
Removes spaces from the right of a string (identical to RTRIM). 
UPPER(string) 
Converts a string key to upper case. 
VAL(string) 
Converts a string key to a numeric. 
 


---

Database Drivers and Interfaces 
113 


---

Database Drivers 
114 
TopSpeed Database Driver 
 
The TopSpeed Database file system is a high-performance, high-security, proprietary file driver 
for Clarion development tools. It is not file compatible with the Clarion file driver's data. 
Data tables, keys, indexes and memos can all be stored together in a single DOS file. The default 
file extension is *.TPS. A separate "Transaction Control File" uses the *.TCF extension by default. 
The TopSpeed driver can optionally store multiple tables in a single file. This lets you open as 
many data tables, keys, and indexes as necessary using a single DOS file handle. This feature 
may be especially useful when there are a large number of small tables, or when a group of 
related files are normally accessed together. All keys, indexes, and memos are stored internally. 
 
 
When multiple tables share a single DOS handle, the first OPEN mode applies to all the 
tables within the file.  
In addition, the TopSpeed file system supports the BLOB data type (Binary Large OBject), a field 
which is completely variable-length and may be greater than 64K in size. A BLOB must be 
declared before the RECORD structure. Memory for a BLOB is dynamically allocated and de-
allocated as necessary. For more information, see BLOB in the Language Reference. 
Files: 
## CLATPSL.LIB
Windows Static Link Library 
 
## CLATPS.LIB
Windows Export Library 
 
## CLATPS.DLL
Windows Dynamic Link Library 
 
 
This driver offers speed, security, and takes up fewer resources on the end user's system. 


---

Database Drivers and Interfaces 
115 
TopSpeed:Specifications 
Data Types 
## BYTE   SHORT   USHORT  LONG  ULONG  SREAL  DECIMAL  REAL
## STRING CSTRING PSTRING MEMO  GROUP  BLOB   DATE     TIME
 
File Maximums/Specifications 
File Size : 2 GB 
Records per File : Unsigned Long (4,294,967,295) 
Record Size : 15,000 bytes 
Field Size : 15,000 bytes 
Fields per Record : 15,000 
Keys/Indexes per File: 240 
Key Size : 15,000 bytes 
Memo fields per File: 255 
Memo Field Size : 64,000 bytes 
BLOB fields per File: 255 
BLOB Size : Hardware dependent (Max size 640 MB) 
Open Data Files : Operating system dependent 
Table Name : 1,000 bytes 
Tables per DOS File :  Limited only by the maximum DOS f
ile size--
approximately 2^32 bytes (4,294,9
67,296). 
Concurrent Users per File: 1024 
 


---

Database Drivers 
116 
Enhanced Encryption Support in the TopSpeed driver 
 
The TopSpeed driver has a built-in encryption system.  However, the encryption algorithm is 
proprietary and this makes the TopSpeed file format unavailable to some developers who have to 
guarantee the encryption algorithm.  Available starting with Clarion 7.0, you have the option to 
use any encryption algorithm supported by any encryption provider that plugs into the Windows 
encryption subsystem.  This will enable developers to create, store and exchange data in a very 
secure environment. 
There are two providers that are installed on all Windows Operating Systems: Microsoft Base 
Cryptographic Provider and Microsoft Enhanced Cryptographic Provider. 
The Microsoft Enhanced Cryptographic Provider supports the same capabilities as the Microsoft 
Base Cryptographic Provider, but provides for stronger security through longer keys and 
additional algorithms. The Enhanced provider is installed on your machine when you apply the 
Internet Explorer 128-bit security patch. 
In addition, you now have the ability to use any encryption algorithm supported by any 
encryption provider that plugs into the Windows encryption subsystem. So you can now 
even use new encryption providers as they become available! 
To enable use of an alternative encryption algorithm you just supply at least one of the following 
encryption settings to the driver via the driver string: 
Example Format: 
(DriverString = Default Value) 
## /PROVIDER= PROV_RSA_FULL 1
Driver String 
Default Value 
Description 
## /PROVIDER
Microsoft Enhanced 
Cryptographic Provider 
The name of the cryptographic 
service provider 
## /CONTAINER
## NULL
The container within the provider 
where the key algorithm is 
located (see (2) below) 
## /PROVIDERTYPE
(Full RSA) 
The encryption type (see (3) 
below) 
## /KEYALGORITHM
## (RC4)
The algorithm used to encrypt 
data (see (5) below) 
## /HASHALGORITH
## (MD5)
The algorithm used to hash the 
password (see (4) below) 
## /FORCEKEY
## FALSE
Set to FALSE to use the default 
key algorithm if the supplied key 
algorithm is not available or not 
valid 
## /FORCEHASH
## FALSE
Set to FALSE to use the default 
hash algorithm if the supplied 
hash algorithm is not available 


---

Database Drivers and Interfaces 
117 
Additional Notes: 
(1) You can use any of the driver string switches in a SEND command before the file is open to 
set the encryption algorithm. You can also retrieve the current value of any of the encryption 
options as the return result of the SEND command. 
(2) /CONTAINER is the key container name. This is a string that identifies the key container to 
the CSP (cryptographic service provider). This name is independent of the method used to store 
the keys. Some CSPs store their key containers internally (in hardware), some use the system 
registry, and others use the file system. 
When /CONTAINER is not specified, a default key container name is used. For example, the 
Microsoft Base Cryptographic Provider uses the logon name of the currently logged on user as 
the key container name. Other CSPs can also have default key containers that can be acquired in 
this way. 
(3) This is the value associated with the different provider types. See the Microsoft Cryptographic 
Provider Types page for full details on provider types. The values of the different provider types 
supplied by the Microsoft Enhanced Cryptographic Provider (MECP) are: 
## PROV_RSA_FULL 1
## PROV_RSA_SIG 2
## PROV_DSS 3
## PROV_FORTEZZA 4
## PROV_MS_EXCHANGE 5
## PROV_SSL 6
## PROV_RSA_SCHANNEL 12
## PROV_DSS_DH 13
## PROV_EC_ECDSA_SIG 14
## PROV_EC_ECNRA_SIG 15
## PROV_EC_ECDSA_FULL 16
## PROV_EC_ECNRA_FULL 17
## PROV_DH_SCHANNEL 18
## PROV_SPYRUS_LYNKS 20
## PROV_RNG 21
## PROV_INTEL_SEC 22
## PROV_REPLACE_OWF 23
## PROV_RSA_AES 24
 
(4) Values supported by the Microsoft Enhanced Cryptographic Provider are: 
## 32769 MD2
## 32770 MD4
## 32771 MD5
32772 U.S. DSA Secure Hash Algorithm 
32773 Message Authentication Code 
32776 SSL3 client authentication 
32777 HMAC, a keyed hash algorithm 
32778 TLS1PRF, Transport Layer Security 1 Pseudo Random Function 
(5) Some values supported by various providers are: 
## 26113 DES
## 26114 RC2
## 26115 3DES
## 26121 3DES 112
## 26625 RC4
For full list of key and hash algorithms the user should consult the documentation of their 
cryptography provider. 


---

Database Drivers 
118 
TopSpeed:Driver Strings 
There are switches or "driver strings" you can set to control the way your application creates, 
reads, and writes files with a specific driver. Driver strings are simply messages or parameters 
that are sent to the file driver at run-time to control its behavior. See Common Driver Features--
Driver Strings for an overview of these runtime Database Driver switches and parameters. 
 
Some driver strings have no effect after the file is open, so no SEND function syntax is 
listed for those strings. However, the SEND function syntax to return the value of the 
switch is listed for all driver strings. 
The TopSpeed Driver supports the following Driver Strings: 
DECIMALCheck 
 
[ DECCheck" = ] SEND(file, 'DECIMALCheck [ = ON|OFF ]' ) 
 
DECIMALCheck=OFF ensures compatibility of TopSpeed files originally created in certain early 
versions of Clarion with the current version by disabling error reporting for the number of decimal 
places in DECIMAL fields during file header comparisons. 
 
This switch should be used as a driver string, or, in a SEND command before the file is opened. 
## FLAGS
 
[ Flags" = ] SEND(file, 'FLAGS [ = bitmap ]' ) 
Sets and returns the configuration flags for the file. Use the following EQUATEs declared in 
EQUATES.CLW to control the behavior of the target TopSpeed file: 
!TopSpeed File Flags 
 
## TPSREADONLY    EQUATE(1)
For example, the following code makes the file read-only for ODBC access while preserving any 
other flags: 
TpsFlags = SEND(MyFile, 'FLAGS') 
SEND(MyFile, 'FLAGS ='&BOR(TpsFlags,TPSREADONLY) 
## FULLBUILD
 
[ State" = ] SEND(file, 'FULLBUILD [ = on | off ]' ) 
[ State" = ] file{PROP:FULLBUILD} [ = on | off ]' ) 
The TopSpeed driver has an optimized appending mechanism where you can add large numbers 
of records to an existing table with the APPEND statement. Issuing a subsequent BUILD updates 
only the appended key information, making incremental batch updates very fast. This is the 
default behavior. Use the FULLBUILD driver string to modify this default behavior. 
FULLBUILD=ON tells the next BUILD statement to fully rebuild the keys. FULLBUILD=OFF 
restores the BUILD to its optimized state. Both versions of the SEND command return the current 
build state as a string 'ON' or 'OFF'. Issue SEND(file,'FULLBUILD') to return the current build 
state without changing it. 


---

Database Drivers and Interfaces 
119 
## PNM=
 
TName" = SEND(file, 'PNM=[starting point]' ) 
Returns the next table name in the file's TopSpeed super file, after the specified starting point. If 
there are no table names after the specified starting point, SEND returns an empty string. If 
starting point is omitted or contains an empty string, SEND returns the first table name in the file. 
PNM= is only valid with the SEND command. There are no spaces surrounding the equal sign 
(=). The target file is the label of any of the tables within the TopSpeed super file.  
For example, given a TopSpeed file containing the Supp table, the following code displays an 
alphabetical listing of all the tables in the file: 
## CODE
name = '' 
## LOOP
 name = SEND(Supp,'PNM=' & name) 
 If name 
  MESSAGE(name) 
## ELSE
## BREAK
 END 
END 
 TCF 
 
DRIVER('TOPSPEED', '/TCF = filename' ) 
[TCFPath =] SEND(file, 'TCF [ = filename ]' ) 
Specifies a transaction control file other than the default TOPSPEED.TCF. The file identifies all 
transactions in progress until the program terminates or a SEND(file, 'TCF = filename') executes. 
In other words, the TCF setting affects all TopSpeed files accessed by the program. This returns 
the name of the transaction control file. For example, TCFPath = SEND(file, 'TCF'). 
 
We recommend using one transaction control file for a system. Using multiple files with 
different access rights can result in partially committed transactions-- some of the files 
within a transaction might be updated and others left unchanged.  
See Also: Transaction Control Files 
 


---

Database Drivers 
120 
TopSpeed:Supported Commands and Attributes 
 
 
File Attributes 
Supported 
 
## CREATE
Y 
 
DRIVER(filetype [,driver string]) 
Y 
 
## NAME
Y 
 
## ENCRYPT
Y 
 
OWNER(password) 
Y1 
 
## RECLAIM
N2 
 
PRE(prefix) 
Y 
 
## BINDABLE
Y 
 
## THREAD
Y12 
 
EXTERNAL(member) 
Y 
 
DLL([flag]) 
Y 
 
OEM 
Y 
 
## LOCALE
Y 
 
File Structures 
Supported 
 
## INDEX
Y 
 
KEY 
Y 
 
## MEMO
Y3 
 
## BLOB
Y15 
 
## RECORD
Y 
 
 
Index, Key, Memo Attributes 
Supported 
 
## BINARY
Y13 
 
DUP 
Y 
 
## NOCASE
Y 
 
OPT 
Y 
 
## PRIMARY
Y 


---

Database Drivers and Interfaces 
121 
 
## NAME
Y4 
 
Ascending Components 
Y 
 
Descending Components 
Y 
 
Mixed Components 
Y 
 
 
Field Attributes 
Supported 
 
DIM 
Y 
 
## OVER
Y 
 
## NAME
Y 
 
 
File Procedures 
Supported 
 
BOF(file) 
Y 
 
BUFFER(file) 
N 
 
BUILD(file) 
Y 
 
BUILD(key) 
Y 
 
BUILD(index) 
Y 
 
BUILD(index, components) 
Y 
 
BUILD(index, components, filter) 
Y 
 
BYTES(file) 
Y 
 
CLOSE(file) 
Y 
 
COPY(file, new file) 
Y 
 
CREATE(file) 
Y 
 
DUPLICATE(file) 
Y 
 
DUPLICATE(key) 
Y 
 
EMPTY(file) 
Y 
 
EOF(file) 
Y 
 
FLUSH(file) 
Y 
 
LOCK(file) 
Y5 
 
NAME(label) 
Y 


---

Database Drivers 
122 
 
OPEN(file, access mode) 
Y 
 
PACK(file) 
Y6 
 
POINTER(file) 
Y8 
 
POINTER(key) 
Y8 
 
POSITION(file) 
Y9 
 
POSITION(key) 
Y9 
 
RECORDS(file) 
Y 
 
RECORDS(key) 
Y 
 
REMOVE(file) 
Y 
 
RENAME(file, new file) 
Y 
 
SEND(file, message) 
Y 
 
SHARE(file, access mode) 
Y 
 
STATUS(file) 
Y 
 
STREAM(file) 
Y7 
 
UNLOCK(file) 
Y 
 
 
Record Access 
Supported 
 
ADD(file) 
Y 
 
ADD(file, length) 
N 
 
APPEND(file) 
Y 
 
APPEND(file, length) 
N 
 
DELETE(file) 
Y2 
 
GET(file,key) 
Y 
 
GET(file, filepointer) 
Y8 
 
GET(file, filepointer, length) 
N 
 
GET(key, keypointer) 
Y 
 
HOLD(file) 
Y 
 
NEXT(file) 
Y 
 
NOMEMO(file) 
Y 


---

Database Drivers and Interfaces 
123 
 
PREVIOUS(file) 
Y 
 
PUT(file) 
Y 
 
PUT(file, filepointer) 
Y 
 
PUT(file, filepointer, length) 
N 
 
RELEASE(file) 
Y 
 
REGET(file,string) 
Y 
 
REGET(key,string) 
Y 
 
RESET(file,string) 
Y 
 
RESET(key,string) 
Y 
 
SET(file) 
Y  
 
SET(file, key) 
Y 
 
SET(file, filepointer) 
Y 
 
SET(key) 
Y 
 
SET(key, key) 
Y 
 
SET(key, keypointer) 
Y 
 
SET(key, key, filepointer) 
Y 
 
SKIP(file, count) 
Y 
 
WATCH(file) 
Y 
 
 
Transaction Processing 
Supported10 
 
LOGOUT(timeout, file, ..., file) 
Y11 
 
## COMMIT
Y 
 
## ROLLBACK
Y 
 
 
Null Data Processing 
Supported 
 
NULL(field) 
N 
 
SETNULL(field) 
N 
 
SETNULL(file,field) 
N 
 
SETNONNULL(field) 
N 


---

Database Drivers 
124 
Notes 
1        We recommend using a variable password that is lengthy and contains special characters 
because this more effectively hides the password value from anyone looking for it. For 
example, a password like "dd....#$...*&" is much more difficult to "find" than a password 
like "SALARY." 
 
 
To specify a variable instead of the actual password in the Owner Name field of the 
File Properties dialog, type an exclamation point (!) followed by the variable name. 
For example: !MyPassword. 
2         The TopSpeed driver automatically reclaims space freed by deleted records and keys. 
3         The TopSpeed file system uses the same compression algorithm for RECORDs and 
MEMOs. For data of 255 bytes or less, MEMOs have no disk space advantage over 
STRINGs. However, STRINGs are always allocated space (RAM) within the record 
buffer, whereas MEMOs are only allocated space when the file is OPENed. MEMOs do 
carry the advantage of BINARY versus NONBINARY, plus MEMOs may be omitted from 
all processing with the NOMEMO statement. 
4         The TopSpeed driver does not support external names for keys, because all keys are 
stored internally. 
5         LOCK() only affects other LOCK() calls. The only effect of a successful call to LOCK() is 
that other processes will get an error (‘File is Already Locked’) when they call LOCK().  
6         PACK performs a BUILD and truncates the file to it's minimum size. 
7         STREAM has the effect of LOCKing the file. 
8         GET(file,filepointer) requires a pointer value returned from the POINTER() function. 
POINTER() returns a physical record address (not a record number). Therefore you 
cannot use 
GET(file,1) 
to retrieve the first record in a TopSpeed file because 1 is not a valid pointer in a 
TopSpeed file. 
9         POSITION(file) returns a STRING(4). POSITION(key) returns a STRING the size of the 
key fields + 4 bytes. 
10        TopSpeed file logging is very fast (about 100 times faster than the Clarion driver). With 
LOGOUT, the TopSpeed engine posts all transactions to memory. ROLLBACK simply 
frees the memory, while COMMIT writes out the database changes in a stream. 
If a system crashes during a transaction (LOGOUT--COMMIT), the recovery is 
automatically handled by the TopSpeed driver the next time the affected file is accessed. 
11        LOGOUT has the effect of LOCKing the file. See also PROP:Logout in the Language 
Reference. 
12        THREADed files do not consume additional file handles for each thread that accesses the 
file. 
13        OEM conversion is not applied to BINARY MEMOs and BLOBs.  
14        The TopSpeed driver accomplishes case insensitivity by converting strings to lowercase. 
This can cause unexpected behavior for characters that fall between the upper and lower 
case alphabet (that is, ^(94) and _(95) for both ANSI and ASCII sequences). 
15        The driver can store BLOBs up to 640 MB.  If you attempt to store a BLOB bigger than 
this, an ERRORCODE  80 - Function not supported, is returned.  This error is returned 
after the BLOB handle assignment: 
(e.g., blobname{PROP:Handle} = image{PROP:Handle}). 


---

Database Drivers and Interfaces 
125 
TopSpeed:Other 
## ERRORCODE 90
The TopSpeed driver posts an ERRORCODE of 90 for unexpected runtime errors. At the same 
time, the driver posts a FILEERRORCODE (the former TPSBT error code) that helps us diagnose 
the problem. This error handling gives you more control over runtime errors and provides us with 
more information. That is, your program can trap for ERRORCODE=90 and react accordingly. 
Should you receive an ERRORCODE of 90 from the TopSpeed driver, we want to know about it. 
Please send us a copy of the file and the corresponding FILEERRORCODE value. 
Large Keys (or small RAM) 
APPEND() is recommended over ADD() if the total size of the keys exceeds the amount of RAM 
available, if there is more than one key, or when adding a large number of records. The size of a 
key (for this purpose) is the number of entries times (the sum of key fields + 10 bytes). If the 
records being added are already in an approximate key order, then you can discount that key for 
the purposes of the above calculation. 
As an example, if a file has two 40 byte keys and 2 Megabytes of RAM are available, then ADD() 
becomes (relatively) slow when the database size exceeds about 2,000,000 / (40 + 10 + 40 + 10) 
= 20,000 records. 
Incremental Key/Index Build 
The TopSpeed driver implements incremental building; this means that building a key only reads 
records starting from the first record appended since the key was last built. The driver merges the 
new keys with the existing key. Thus building a large key where only a few recently added 
records have been modified should be fast. See the FULLBUILD driver string above. 
Building an index is similar, but must start at the minimum physical record whose position in the 
index has changed since the index was last built. 
Dynamic indexes are not retained, so cannot be built incrementally. 
Batch Processing Performance 
When writing a large number of records, use STREAM() or open the file in a deny write mode, 
that is, OPEN(file) rather than SHARE(file). After the records have been written, call FLUSH() to 
allow other users access. 
It is very important to use STREAM() when ADDing/APPENDing/PUTting a large number of 
records. STREAM() will typically make processing about 20 times faster. For example, adding 
1000 records might take nearly 2 minutes without STREAM(), but only 5 seconds with STREAM.  
It is not necessary to use STREAM() or FLUSH() on a logged out file (performance on logged out 
files is always good). 
STREAM has the effect of LOCKing the file. 
POINTERs and Deleted Records 
POINTER(key) returns the relative position of the record within the file. Consequently when that 
record is DELETEd, the pointer becomes invalid. Any subsequent access using the pointer fails. 
If you require fuzzy matching whereby the nearest record is returned, use the POSITION() 
function. 


---

Database Drivers 
126 
Data Compression--STRINGs v MEMOs 
The TopSpeed driver compresses the entire record buffer area (not individual fields within the 
record), therefore, compression gains can be realized by placing similar fields adjacent to each 
other in the FILE declaration. 
The TopSpeed file system uses the same compression algorithm for STRINGs and MEMOs; 
however, the compression occurs at a "higher level" for MEMOs than for STRINGs. As a result, 
MEMOs do have a disk space advantage over large STRINGs (over 500 bytes) and smaller 
STRINGS can have a slight performance advantage over MEMOs. The larger the STRING, the 
greater the advantage. 
MEMOs do carry the advantage of BINARY versus NONBINARY, plus MEMOs may be omitted 
from all processing with the NOMEMO statement. 
STRINGs are always allocated space (RAM) within the record buffer, whereas MEMOs are only 
allocated space when the file is OPENed. Also MEMOs cannot be key components.  
Estimating File Size 
The TopSpeed file driver compresses data and key information, so the ultimate file size depends 
on the "compressibility" of the data and keys. In the worst case (data and keys cannot be 
compressed because there is no repeating information) the file size may be estimated as: 
(RecordSize + All Key components) * Records + Fixed Overhead 
In a more realistic case (data and keys are compressible), the file size may be estimated as: 
((size of all string fields)/(compressibility factor) +  
size of all binary fields +  
size of all binary key components +  
(4 * number of string key components)) * Records + Fixed Overhead 
Note that Fixed Overhead varies depending on your file definition. Fixed overhead includes about 
800 bytes for the driver, plus the header information describing the fields and keys for the file. 
The more fields and keys, and the longer the names, the higher the fixed overhead. A rough rule 
of thumb for calculating fixed overhead is 800 bytes + 40 bytes for each field and key. For 
Example: 
File Description 
Estimated Fixed Overhead 
1 field, no keys 
1KB 
20 fields, 10 keys 
2KB 
200 fields, 10 keys 
9KB 
Concurrent User Limit 
The TopSpeed driver limits concurrent users to 1024 per file; additional users would have to wait 
momentarily until a slot opens up. Practically speaking the driver is very unlikely to reach this limit 
since very few networks and servers will support this many concurrent users. Generally, we 
recommend a client/server file system for more than 30 concurrent users. 


---

Database Drivers and Interfaces 
127 
Transaction Processing--the TCF File 
Speedy Logging and Automatic Recovery 
TopSpeed transaction logging is very fast (about 100 times faster than the Clarion driver). With 
LOGOUT, the TopSpeed engine posts all transactions to memory. ROLLBACK simply frees the 
memory, while COMMIT writes out the database changes in a stream. 
If a system crashes during a transaction (LOGOUT--COMMIT), the recovery is automatically 
handled by the TopSpeed driver the next time the affected file is accessed. 
The Transaction Control File 
The transaction control file (.TCF) is used to ensure that changes to more than one DOS file, 
which are grouped into a transaction, either all happen or none happen. By default the transaction 
control file has the name "TOPSPEED.TCF." The TCF driver string lets you change this. See 
TCF for more information. 
When any workstation finds a file which is in a partially committed state, and which was involved 
in a multi-file transaction, it needs to access the TCF file to decide what to do. The TCF file 
provides "atomicity"--a single (boolean) storage location which inndicates if a multi-file transaction 
committed or not. 
Note that the .TCF file contains very little information; it just serves to coordinate multi-file 
commits. The actual rollback/commit data is stored in the data (.TPS) files. 
How TopSpeed Transaction Logging Works 
LOGOUT gives each transaction a unique id which it stores in the .TCF file. LOGOUT also stores 
the .TCF file name and transaction id in each data (.TPS) file which is updated, so that after a 
crash, the next time the file is opened the TopSpeed driver can find the .TCF file and do any 
necessary recovery. COMMIT removes the unique transaction id from the .TCF file.  
To be effective, the .TCF file must be accessible when any files controlled by it are accessed. 
Therefore, you generally should not delete or move .TCF files. If a transaction updates network 
files, you should specify a transaction control file on the network.  
It is not necessary to use the same TCF file for all transactions; however, we strongly recommend 
it. The consequence of there being several TCF files with various levels of accessibility (or of a 
deleted or overwritten TCF file) is that some of the files within a transaction might be updated and 
others left unchanged.  
 
 Storing Multiple Tables in a single .TPS File 
By using the characters '\!' in the NAME() attribute of a TopSpeed file declaration, you can specify 
that a single .TPS file will hold more than one table. For example, to declare a single .TPS file 
's&p.tps' that contains 3 tables called supp, part and ship: 
Supp FILE,DRIVER('TopSpeed'),PRE(Supp),CREATE,NAME('S&P\!Supp') 
    ... 
Part FILE,DRIVER('TopSpeed'),PRE(Part),CREATE,NAME('S&P\!Part') 
    ... 
Ship FILE,DRIVER('TopSpeed'),PRE(Ship),CREATE,NAME('S&P\!Ship') 
    ... 
 


---

Database Drivers 
128 
Access and Sharing Modes 
The TopSpeed driver optimizes the use of file handles, so that only one file handle is used per 
DOS file per thread.  The access mode for that handle is set to the least restrictive of any open 
mode used for that file handle. The sharing mode is set to the most restrictive for sharing. 
 
For example: 
 
FileA FILE,DRIVER('TopSpeed'),NAME('TPSFile\!SubTable') 
... 
      END 
FileB FILE,DRIVER('TopSpeed'),NAME('TPSFile\!SubTable') 
... 
      END 
FileC FILE,DRIVER('TopSpeed'),NAME('TPSFile\!SubTable2') 
... 
      END 
FileD FILE,DRIVER('TopSpeed'),NAME('TPSFile\!SubTable2') 
... 
      END 
 
## CODE
  OPEN(FileA, 10H)  ! Read Only - Deny None 
  OPEN(FileB), 12H) ! Read/Write - Deny None 
  ! Due to access promotion FileA now has Read/Write access 
 
  OPEN(fileC, 22H) ! Read Only / Deny All 
  ! Due to sharing restriction all files now have Deny All sharing 
 
  OPEN(fileD, 22H) ! Read Only / Deny All 
  ! This will succeed even though the file handle has sharing 
  ! set to deny all because of the file handle sharing 
  ! At this stage all four files are open in Read/Write - Deny All 
 
  CLOSE(File) does not reset access modes, so given the above example doing: 
 
    CLOSE(fileD) 
    CLOSE(fileC) 
    CLOSE(fileB) 
 
fileA is still open with access mode Read/Write - Deny All 


---

Database Drivers and Interfaces 
129 
Similarly, if one of the tables in the file is logged out, then all the tables are effectively logged out. 
If one table in the file is flushed, then all the tables are flushed. 
This feature is especially useful when there are a large number of small tables, or when the 
application must normally access several related tables at once. 
  
When using a variable to hold the name of the multi-table element, you can browse the file in the 
Dictionary Editor by selecting the Browse tablename option, selecting the core file name, and 
appending the specific table name to the mutil-file name before loading.  Example: 
invoice.tps\!customer where invoice.tps is the file name stored on disk. 
You can retrive the names of tables within the .TPS files with the SEND() command. To retrieve 
the first name, issue:  
SEND(file,'PNM=') 
This returns the name of the first table. To retrieve the second name, issue:  
SEND(file,'PNM=FirstTableName') 
This returns the name of the second table, and so on. 
You can also rename the tables; for example, given the above declarations the following 
command renames the table called Supp to Old_Supp: 
RENAME(Supp,'S&P\!Old_Supp') 
If you use the OWNER attribute on multiple tables in a single .TPS file, all the tables must have 
the same OWNER attribute. 
If you don't specify a table name, the table is called 'unnamed', so that the following are all 
equivalent: 
myname     FILE,DRIVER('TopSpeed') 
myname     FILE,DRIVER('TopSpeed'),NAME('myname') 
myname     FILE,DRIVER('TopSpeed'),NAME('myname\!unnamed') 
Collating Sequences 
Changing Collating Sequence 
Changing the collation sequence on a Clarion 2.003 or earlier TopSpeed file (by changing .ENV 
file or OEM flag) corrupts the file. 
This is no longer true, because the collating seqence for the file is now stored within the file. This 
change is fully backward compatible. Old files continue to work as before and new files are 
accessible by older programs. 
To add the collating sequence information to an existing file, simply do a full build on the file: 
SEND(file,'FULLBUILD=on') 
BUILD(file) 
The collating sequence for a TopSpeed file is established when the table is created or a full build 
is performed. Therefore the OEM flag and LOCALE attribute are only significant at the creation of 
the file or on a full build. 
Any application that uses an incorrect sequence (due to an incompatible .ENV file) to access a 
file may get unpredictable results, but will not corrupt the data. 


---

Database Drivers 
130 
Accessing TopSpeed files with Access Jet and ODBC 
Occasionally, the Access Jet engine returns "#deleted" for each requested field. This is a known 
bug in Microsoft Access. The default query used by Access does an internal comparison of the 
record set to determine if a record has been deleted or modified from the database. The 
mechanism is known to work poorly for certain data types, notably DECIMAL. 
Microsoft recommends using an SQL pass-through query as a work around to this problem. To 
create a SQL pass-through query: 
1. Choose SQL Specific, Pass Through from the Query menu in query design mode. For 
Access 7, Select Query, and press the New button.  
2. Accept the default of Design View. 
3. Close the Show Table Window.  
4. Select SQL Specific from the Query menu and select the Pass-Through option. 
5. Enter the SQL statement. 
The Query can be saved for future use. This method will correct virtually all display problems, but 
the resulting grid is not updatable. Updates must be performed using an Update Query when SQL 
Passthrough is used. 


---

Database Drivers and Interfaces 
131 
TopSpeed File Errors 
Here is a list of the TopSpeed file errors returned by FILEERRORCODE , and a brief explanation: 
231 
trying to append a record when the btree is marked read-only 
232 
cannot get btree header when trying to append a record 
256 
cannot get btree header when trying to get a record 
300 
btree structure corrupt (discovered when deleting a record) 
327 
btree structure corrupt (discovered when putting a record) 
337 
trying to put a record when the btree is marked read-only 
522 
invalid data size found while unpacking record (from disk) 
530 
invalid repeat count found while unpacking record (from disk) 
706 
btree structure corrupt (discovered when inserting a record) 
780 
btree structure corrupt (discovered when removing a record) 
824 
btree record size to big (on allocation) 
1013 
cannot get btree header (while loading root page) 
1043 
cannot get btree header (while packing a record to disk) 
1163 
trying to create new record ID when the btree is marked read-only 
1164 
cannot get btree header (while allocating new record ID) 
1173 
maximum record ID reached on allocation (probably indicating file corruption) 
1194 
trying to insert record when the btree is marked read-only 
1203 
trying to remove record when the btree is marked read-only 
1364 
btree structure corrupt (discovered while splitting a page) 
1477 
btree page size (from header) does not match size stored on disk 
1602 
btree unpacked page size (from header) does not match size loaded from disk 
1659 
btree page size increased after packing 
1678 
btree page size larger than maximum allowed 
1735 
btree header corrupt (discovered when trying to calculate disk file size)  
1781 
btree structure corrupt (discovered while shifting btree pages up) 


---

Database Drivers 
132 
1891 
btree structure corrupt (discovered while moving btree pages) 
1894 
btree structure corrupt invalid page parent level (discovered while moving btree 
pages) 
2172 
reading of btree page from disk failed 
2183 
too many files logged out 
2272 
encryption block invalid size (discovered when reading page from disk) 
2277 
ReadFile Win32 API function failed (when reading page from disk) 
2286 
encryption block invalid size (discovered when writing a page to disk) 
2328 
invalid internal btree locking mode (on lock) 
2352 
invalid internal btree locking mode (on unlock) 
2341 
SetFilePointer Win32 API function failed (when reading page from disk) 
 


---

Database Drivers and Interfaces 
133 
TopSpeed Database Recovery Utility 
The TopSpeed file system is designed to automatically repair most errors. However, if a 
TopSpeed file is physically damaged during a system malfunction, the TopSpeed Database 
Recovery Utility (TPSFIX.EXE) can recover the undamaged portions of your data.  
 
 
The TopSpeed Database Recovery Utility is an emergency repair tool and should not be 
used on a regular basis. Use it only when a file has been damaged. 
The TopSpeed Database Recovery Utility reads the damaged file and writes the recovered 
records to a new file. It uses the information stored in the file's header and scans the file 
recovering undamaged portions.  
Optionally, you can provide an example file containing the header information in the event the 
original header information is damaged. An example file is any file with a FILE declaration 
identical to the damaged file. You can create an example file by issuing a CREATE(file) 
command, then saving the resulting empty file to a new name.  
The TopSpeed Database Recovery Utility is a distributable utility designed to help your end users 
recover damaged files. 
The following DLLs, found in the Clarion BIN folder, also need to be distributed with TPSFIX.EXE: 
## CLARUN
## CLATPS
 
 
The Clarion license agreement applies to TPSFIX.EXE and its associated DLLs. You may 
distribute to your users, but they may not redistribute it. 
The recovery utility is designed to work either interactively or noninteractively with command line 
parameters. Interactively, you provide the parameters through two wizard dialogs. You can run 
TPSFIX noninteractively by supplying the command line parameters with the Clarion RUN() 
statement, Windows API calls, Windows 95 shortcuts, or Program Manager Icons. 
ERRORCODE 90 and Corrupted Files 
The TopSpeed driver posts an ERRORCODE of 90 for unexpected runtime errors. When an 
ERRORCODE of 90 occurs, the driver also posts a FILEERRORCODE (the former TPSBT error 
code) that helps us diagnose the problem.  
An ERRORCODE of 90 usually indicates your TopSpeed file is corrupted. In most cases the 
corruption is a result of hardware failure. For example, one customer with a 50 machine network 
traced a near daily file corruption to bad network cards on 2 of the 50 machines. After replacing 
the bad cards, the corruptions disappeared. 
However, should you receive an ERRORCODE of 90 from the TopSpeed driver, we want to know 
about it. Before you repair the file, please make a copy of the damaged file and send it to us 
along with the corresponding FILEERRORCODE value. We analyze all the corrupted files we 
receive for recognizable patterns that can help us improve the driver. 
TopSpeed File Errors  
Standard Errorcodes and Errors 
Using the Recovery Utility Interactively 


---

Database Drivers 
134 
1. Start the utility by DOUBLE-CLICKING on the TopSpeed Database Recovery Utility Icon 
In the Clarion Program Group. 
The TopSpeed Database Recovery Utility dialog appears. The utility consists of two wizard 
dialogs.  
2. In the Source (file to recover) section, specify the file name or press the Browse button to 
select it from a standard file open dialog. 
3. If the file has a password, type it in the Password entry box. 
If the database file contains multiple tables (data files), each table must have the same 
password. 
4. Optionally, in the Destination (result file) section, specify the file name for the target file or 
press the Browse button to select it from a standard file open dialog. 
By default the .TPR extension is added to the source file name. This parameter is 
optional. If omitted, the original (source file) is overwritten and a backup file is created. 
The source file is renamed to filename.TPx, where x is automatically incremented from 1 
to 9 each time a new file is created. If all nine numbers are used, any subsequent files 
created are given the extension .TP$ and are overwritten. 
5. If the result file is to have a different password, type it in the Password entry box. If 
omitted, the password is removed. 
6. Press the Next button. 
The second wizard dialog for the TopSpeed Database Recovery Utility appears. 
7. Optionally, specify the Example File file name or press the Browse button to select it from 
a standard file open dialog.  
The utility uses the Example File to determine table layouts and key definitions in the 
event those areas of the source file are damaged. The default extension is .TPE, but if 
you choose, you may use any valid DOS extension  
 
 
We recommend shipping an example file when you deploy your application. This 
improves data recovery from a damaged file. 
8. If the example file has a password, type it in the Password entry box. 
9. If you want the utility to rebuild Keys, check the Build Keys box. 
If omitted, the keys are rebuilt by the original application when it attempts to open it. 
10. If you want to use the Header Information in the source file, check the Use Header box. 
Using Header Information optimizes the utility's performance, but should not be used if 
the file header is corrupt. If omitted, the utility searches the entire data file and restores all 
undamaged pages. 
11. If the application uses a Locale (.ENV) File for an alternate collating sequence, specify 
the .ENV file or press the Browse button to select it from a standard file open dialog. 
12. If the file is using the OEM attribute to control the collating sequence, Check the Use OEM 
box. 
This enables the OEMTOANSI and ANSITOOEM conversion. 
13. Press the Start button to begin the recovery process. 
If the utility does not find any errors, a message appears informing you that "No Errors 
Detected in <fliename.ext>" and asks if you want to continue with recovery.   


---

Database Drivers and Interfaces 
135 
TPSFIX Command Line Parameters 
The TPSFIX utility can accept command line parameters which lets you execute it from an 
application, from a Desktop Icon, or from a Windows Shortcut. 
Here is the syntax for running TPSFIX noninteractively with command line parameters. 
 
## TPSFIX
sourcepath[?password] [destpath[?password]] [/E:examplepath[?password]]  
 
[/A][/C:codepage][/LO:locale][/L:localepath] [/H] [/K] [/P] [/O] [/T:filename] 
  
## TPSFIX
The executable (TPSFIX.EXE). 
sourcepath 
The file name and path of the source (damaged) database file. 
?password 
The file's password.  
destpath 
The file name and path of the recovered database file. If omitted, the destpath 
is the same as the sourcepath and an example file is required. 
/A 
If specified, the user is not offered a backup prompt. The prompt suppressed, 
however a backup of the file is made. 
/C:codepage 
If specified, the code page will be used when rebuilding keys.  See also /LO 
parameter 
/E:examplepath 
The file name and path of the example database file. This parameter is 
required for any fix-in-place operation (that is, when sourcepath = destpath). 
/H- 
If specified, the utility uses the header information in the source file. 
/K 
If specified, the utility rebuilds all keys for the database. 
/L:localepath 
The file name and path of the Locale (.ENV) file used to specify an alternate 
collating sequence. 
/LO:locale 
If specified, the locale will be used when rebuilding keys.  See also /LO 
parameter 
/N 
If specified, the file will be checked for errors. No errors will be corrected. 
/O 
If specified, the file uses OEMTOANSI and ANSITOOEM to determine the 
collating sequence. 
/P 
If specified, the user is prompted for each parameter even if they are supplied 
on the command line. 
/T:filename 
If there are file errors, a log file with the supplied filename will be created. 
 


---

Database Drivers 
136 
Using the Recovery Utility Non-Interactively 
There are some issues to consider before running the TPSFIX utility. Because of the following, 
we do not recommend running TPSFIX from your application program. Rather, it is better to 
instruct your end users to close down the application program completely before running the 
TPSFIX utility.  
• 
The database file should NOT be open when running TPSFIX. Ensure the file is closed 
before starting TPSFIX. 
• 
To prevent access during the recovery process is completed, TPSFIX LOCKs the file 
automatically.  
• 
It is more efficient and safer to have your application rebuild the KEYs (omit the /K 
parameter). It is also a good way to check the status of a recovery. 
Automatic Fix-in-Place Recovery 
By omitting the destpath parameter and supplying an example file, you can directly overwrite the 
damaged file. This is a fix-in-place recovery. The TPSFIX utility does create an intermediate file, 
but you don't have to worry about it. For Example: 
TPSFIX.EXE Datafile.TPS /E:Example.TPE /H 
or with Embedded Source Code: 
RUN('TPSFIX.EXE Datafile.TPS /E:Example.TPE /H') 
This recovers the "datafile.TPS" file using the "Example.TPE" file as an example for the table and 
key layouts, does not rebuild the keys, and uses the header information in the original file. 
TPSFIX automatically saves the original file to a backup with a file extension of TP1 through TP9. 
Each time the utility is executed, the numeric portion of the extension is incremented. 
Separate Source and Target Recovery 
This method requires two lines of embedded source code but gives you control over the renaming 
process. You insert the source code in the Accepted Embed point for the Menu Item or button.  
Example: 
COPY(datafilelabel, 'Datafile.OLD')       !  copies the original file 
                     !  to Datafile.OLD  
RUN(TPSFIX Datafile.OLD Datafile.tps /H)  !  Runs the utility using the 
                     !  renamed file as 
                     !  the source and the original 
                     !  name as the target 
 
This copies the datafilelabel file to DATAFILE.OLD, recovers the file and writes it to 
DATAFILE.TPS using the header information in the original file. 
 


---

Database Drivers and Interfaces 
137 


---

Database Drivers 
138 
SQL Accelerators (Drivers) 
This section offers general tips and programming considerations when using any of the SQL 
Accelerators (Drivers). 
 
General Information for all SQL Drivers 
These SQL Accelerator Drivers share a common code base and many common features such as 
the unique, high speed buffering technology (see BUFFER in the Language Reference), common 
driver strings, and SQL logging capability. However, their primary purpose is to translate Clarion 
file commands into appropriate, efficient SQL statements specific to their respective SQL servers, 
and to handle any result sets returned by those servers. 
The SQL Accelerator Drivers convert standard Clarion file I/O statements and function calls into 
optimized SQL statements, which they send to their backend SQL servers for processing. This 
means you can use the same Clarion code to access both SQL tables and other file systems 
such as TopSpeed files. It also means you can use Clarion template generated code with your 
SQL databases. 
Examples: 
Clarion Expression 
SQL Optimization 
SUB(var,1,LEN('value')) 
var LIKE 'value%' 
INSTRING('value',var,1,1) <> 0 
var LIKE '%value%' 
NULL(SQLFld) = 0 
SQLFld NOT NULL 
NULL(SQLFld) = 1 
SQLFld NULL 
var is UPPER(SQLFld), LOWER(SQLFld), or SQLFld 
SQLFld is a field in an SQL table 
In addition, UPPER and LOWER are converted into the equivalent SQL function, depending on 
the backend used. 
In addition to the automatically generated SQL statements, the SQL Accelerator Drivers forward 
any additional SQL statements you specify to the backend SQL servers. The SQL Accelerator 
Driver interprets the result set returned from the SQL server and makes it available to your 
application program with the Clarion NEXT or PREVIOUS statement.  
All the common behavior of all the SQL Accelerator drivers is documented in this chapter. Driver-
specific behavior is documented the chapter for that specific SQL driver. 
SQL Accelerator Unique Keys 
The SQL Accelerator drivers should generally be used only on tables with unique keys. The 
drivers will function on files without unique keys, but only with substantially limited capabilities. 
Without a unique key, the RESET and REGET commands return errors, and the driver cannot 
update the SQL database. 
Most Clarion templates also require that you define a primary key for each table in order to 
generate code. 
 
 


---

Database Drivers and Interfaces 
139 
SQL Driver Behavior 
Automatic Login Dialog 
The SQL Accelerator drivers automatically look for UserName and Password values whenever 
they access an SQL table. If a UserName and Password have already been supplied, the driver 
uses those values. If no values have been supplied, the driver prompts for the UserName and 
Password with the automatic login dialog. 
We recommend opening a table at the start of your program so the time devoted to logging in 
occurs at program start up. Clarion's Application Wizard automatically generates code to do this 
for SQL Accelerator drivers. However, if you do not use the Application Wizard, you can 
accomplish the same effect simply by adding an SQL table to the Data / Tables Pad for your main 
procedure. This automatically generates code to open the table. 
Except for the ODBC Acclerator Driver, the automatic Login dialog lets the user specify 
Username, Password and Database. 
In the Database drop-down list, select from previously selected hosts. If the Database list is 
empty, you may type in the database name. 
SET/NEXT and SET/PREVIOUS Processing (SELECT/ORDER BY) 
A SET statement followed by a NEXT in a LOOP structure is the most common Clarion method to 
process records sequentially. When the SQL Accelerator drivers encounter a SET/NEXT 
combination, they generate an SQL SELECT statement with an ORDER BY clause based on the 
KEY component fields. The KEY component fields are determined by the KEY names in the SET 
statement. For example, the SQL driver translates this Clarion code 
 
Ord      FILE,PRE(Ord),DRIVER('SQLDriver'),NAME('ord') 
NameDate  KEY(+Ord:Name,+Ord:Date),NAME('DateKey') 
Record    RECORD 
Name       STRING(12),NAME('NameId') 
Date       DATE,NAME('OrderDate') 
Type       STRING(1),NAME('OrderType') 
Details    STRING(20),NAME('OrderDetails') 
          END 
         END 
## CODE
 Ord:Name = 'SMITH' 
 SET(Ord:NameDate,Ord:NameDate) 
## LOOP
  NEXT(Ord) 
  !... some processing 
 END 
into a SELECT statement similar to: 
 SELECT NameId,OrderDate,OrderType,OrderDetails FROM Ord 
  WHERE (NameID >= 'SMITH') 
  ORDER BY NameID, OrderDate 
 
 
 
The SET(file) statement (to process in file order, not keyed order) only supports the NEXT 
statement. Any attempt to execute a PREVIOUS statement when processing in file order 
causes ERRORCODE 80 (Function Not Supported). 


---

Database Drivers 
140 
NULL Fields 
When you read a row with NULL values from an SQL table, the Clarion record buffer contains an 
empty string for string fields, or a 0 for numeric fields, and NULL(field) returns TRUE for the field. 
If the field's contents are later changed to a non-empty or non-zero value then NULL(field) returns 
## FALSE.
If you want to change a NULL field to non-null, but still blank or zero, then you must call 
SETNONULL(field) to reset the null flag. 
If you wish to clear a field to NULL that was previously non-null then call SETNULL(field) or 
SETNULL(record). SETNULL() clears the contents of the field or record and resets the null flag. 
When adding a new record to a file, by default all blank fields are added as blank or zero fields, 
not as NULL. If you want to force a field to be added with a NULL value, then you must call 
SETNULL(field) or SETNULL(record) to null all the fields. 


---

Database Drivers and Interfaces 
141 
Using SQL Tables in your Clarion Application 
Register the SQL Accelerator Driver 
Before your application can use a particular database driver, the driver must be registered with 
the Clarion development environment. The in-the-box drivers are already registered when you 
install Clarion. You must register any add-on drivers. See Clarion's Development Environment--
Database Driver Registry in the User's Guide for information on registering database drivers. 
Import the Table Definitions 
Typically, you add SQL support to your application by importing the SQL table, view, and 
synonym definitions into your Clarion Data Dictionary. See The Dictionary Editor--Importing File 
Definitions in the User's Guide for general information on importing table, file, and view 
definitions. This section describes SQL Driver imports generally. Driver-specific import 
information is described in the chapter or manual for each driver. 
Although you can manually add table definitions to the dictionary (or even hand code your FILE 
declarations) for your SQL tables, we strongly recommend importing the table definitions. 
Importing the table definitions reduces the chance of introducing errors into the dictionary and 
guarantees the correct specification of data types, key structures, etc.  
The importing approach assumes your SQL tables are already defined within the SQL database. 
In the case where you are designing a new SQL database, you may, of course, lay out the table 
definitions for the first time in the Clarion Data Dictionary. However, we recommend this approach 
only for prototyping and for databases with minimum complexity and maintenance requirements. 
In most cases, to correctly implement an SQL database requires defining more items than are 
stored in the Clarion Data Dictionary--for example, stored procedures, triggers, access rights, and 
storage allocation. 
Once your table definitions are in the Clarion Data Dictionary, you develop your SQL based 
applications just as you would any other application. 
 
 
Driver-specific import information is described in the chapter or manual for each driver. 
SQL Import Wizard--Login Dialog 
When you select an SQL Accelerator Driver from the driver drop-down list, the Import Wizard 
opens the Login/Connection dialog. The Login/Connection dialog collects the connection 
information for the SQL database. 
 
 
Before you can connect to the SQL database and import table definitions, the database 
must be started and must be accessible from your computer. 
Fill in the fields in the Login/Connection dialog.  
Next > 
Press this button to open the Import Wizard's Import List dialog. 


---

Database Drivers 
142 
SQL Import Wizard--Import List Dialog 
When you press the Next > button, the Import Wizard opens the Import List dialog. The Import 
List dialog lists the importable items. 
Highlight the table, view, or synonym whose definition to import, then press the Finish button to 
import. The Import Wizard adds the definition to your Clarion Data Dictionary, then opens the File 
Properties dialog to let you modify the default definition. 
Import additional tables, views, and synonyms by repeating these steps. After all the items are 
imported, return to the Dictionary Editor where you can define relationships and delete any 
columns not used in your Clarion application. See Advanced Techniques--Define Only the Fields 
You Use. 
Connection Information and Driver Configuration--File Properties 
Typically, you add SQL support to your application by importing the SQL or ODBC table, view, 
and synonym definitions into your Clarion Data Dictionary. The Import Wizard automatically fills in 
the File Properties dialog with default values based on the imported item. However, there are 
several fields in the File Properties dialog you can use to further configure the way the SQL 
Accelerator Driver accesses the data. These File Properties fields are described below. 
Driver Options 
Typically, the Import Wizard places nothing in the Driver Options field. However, you can add 
driver strings to this field to control how the driver accesses your SQL data. For example, you can 
generate a log of driver activity or specify how the driver handles dates with a value of zero (0). 
See SQL Driver Strings for more information. 
Owner Name 
Typically, the Import Wizard places the SQL database connection information (Host, Username, 
Password, etc.) in the Owner Name field. 
For security and portability reasons, you may want to specify this connection information with 
variables rather than hard coded strings in your dictionary. To use a variable specification, type 
the variable name, preceeded by an exclamation point in the Owner Name field; for example 
!LoginString. Then use whatever method you choose to prime the variable before accessing the 
SQL table. 
Some SQL Accelerator drivers allow additional information in the Owner Name field. This 
information is described in the documentation for each driver. 
 
The SQL drivers now parse out double quotes within the owner attribute to allow commas to be 
passed in a section. For example, you can now do  
"server,port",database,uid,pwd  
to connect to an MS-SQL database running on a non-standard port. 
 


---

Database Drivers and Interfaces 
143 
Server Side Auto incrementing 
 
All SQL drivers support the ability to automatically retrieve values set by the server when an 
INSERT is issued or to set values via server calls before an INSERT is issued. Normally, this 
usage is designed for auto incrementing columns that are not set up as auto number key columns 
on the client side. 
These techniques are designed so that the value in columns that are auto incremented by actions 
that are performed by the Database Server (as opposed to auto incrementing on the client side) 
are available to the client application right after the insert without having to perform a requery of 
the database. 
This feature is achieved by using the file property (PROP:ServerAutoInc) and two driver strings 
(/AUTOINC and /PREAUTOINC). 
 
Language Support 
Here is the "behind the scenes" language support provided for Server Side Auto Incrementing. In 
most cases, if you were using the application/dictionary approach to development, you would not 
need to hand code these properties (they are built-in to the template support via dictionary driver 
string and field option settings – see below) 
 
PROP:ServerAutoInc 
This property is READ/WRITE. To make the driver automatically update fields after an ADD or 
APPEND call (or before in some cases) you need to issue the following statement  
file{PROP:ServerAutoInc} 
before issuing the ADD(file) or APPEND(file). 
This property is a flag that is reset by ADD and APPEND.  So it must be reissued each time an 
ADD or APPEND is done.  If you always want this flag set, you should attach a file driver 
callback interface to the file and set the property before the ADD or APPEND statements are 
executed. 
 
To specify which field is actually set on the server, you need to issue the following statement: 
file{PROP:ServerAutoInc, n} = m 
where n is the field number and m is the column number of the returning SQL code.  This is 
almost always 1. However, in the following SELECT statement: 
SELECT MAX(Col1),MAX(Col2)….FROM ACCOUNTS 
and your file structure had Col1 as the first field and Col2 as the second field then you would 
issue:, you would issue: 
Accounts{PROP:ServerAutoInc, 1} = 1 
Accounts{PROP:ServerAutoInc, 2} = 2 
You only need to set the value of {PROP:ServerAutoInc, n} once for non-threaded files and once 
per thread for threaded files. 
If no valid fields are specified to receive the results for the auto incrementing method and 
file{PROP:ServerAutoInc} has been issued, ADD() will return error code 80 (Function not 
supported). 


---

Database Drivers 
144 
 
You can query PROP:ServerAutoInc to see if the next ADD or APPEND will do a server side 
auto increment or to verify that a field is set to receive the results of the auto increment. 
 
## /AUTOINC AND /PREAUTOINC
For MSSQL, SQLAnywhere and Pervasive.SQL drivers, the above is all the work you normally 
need to do.  For Oracle and the ODBC driver or other drivers not mentioned above (and in 
special cases for those first three drivers) you will also need to apply the following driver string: 
/AUTOINC = your SQL SELECT statement 
with the necessary SQL statement you want executed for retrieving the auto-incrementing fields 
and  
## /PREAUTOINC=[TRUE|FALSE]
to indicate that the auto-incrementing code should be executed before or after the INSERT 
statement.  For all the drivers (except Oracle), if PREAUTOINC is not specified, then the SQL 
code is issued after the SELECT.  For Oracle, it is issued before the SELECT. 
These properties can easily be set through the Dictionary Driver String Options. 
 
Example: 
 
!ORACLE Example 
OracleFile FILE,DRIVER('Oracle', '/AUTOINC=SELECT Myseq.nextVal') 
## RECORD
SomeData     STRING 
autoIncFld   PDECIMAL(31) 
            END 
           END 
 
## CODE
   OPEN(OracleFile) 
   OracleFile{PROP:ServerAutoInc} 
   ADD(OracleFile)  !will return error code 80 as no field has been set to 
receive the result of the SELECT statement 
   OracleFile{PROP:ServerAutoInc, 2} = 2 
   ADD(OracleFile)  !will return error code 80 as no first field has been set 
   OracleFile{PROP:ServerAutoInc, 2} = 1 
   OracleFile{PROP:ServerAutoInc} 
   ADD(OracleFile) 
   ! This will first put the nextval sequence value into  
   ! OracleFile.autoIncFld and then do a normal ADD call. 
 
 
!******************************************************** 
!MySQL Example 
Pet FILE,DRIVER('ODBC','/AUTOINC=SELECT LAST_INSERT_ID()'),| 
              OWNER('menagerie,root'),NAME('pet'),PRE(pet),BINDABLE,THREAD 
Primary KEY(pet:PetID),PRIMARY 
Record  RECORD,PRE() 


---

Database Drivers and Interfaces 
145 
Name     CSTRING(21) 
Owner    CSTRING(21) 
Species  CSTRING(21) 
Sex      STRING(1) 
Birth    DATE 
Death    DATE 
PetID    LONG             !Server side auto inc 
        END 
   END 
 
## CODE
  OPEN(Pet) 
  Pet{PROP:ServerAutoInc, 7} = 1  ! indicate which field receives which value 
  Pet:Name = 'test autoinc' 
  Pet:Owner = 'Pierre' 
  Pet:Species = 'Dog' 
  Pet:Sex = 'M' 
  Pet:Birth = DEFORMAT('2005-12-12', @d10) 
  Pet{PROP:ServerAutoInc}         ! arms automatic updating 
  ADD(Pet)  ! PetID now has the Auto incremented value 
  Pet:PetID = 0 
  Pet:Name = 'test no autoinc' 
  Pet:Owner = 'Pierre' 
  Pet:Species = 'Dog' 
  Pet:Sex = 'M' 
  Pet:Birth = DEFORMAT('2005-12-12', @d10) 
  ADD(Pet)  ! PetID will not have the auto incremented value. 
 
 
Application/Dictionary Implementation 
 
There are essentially two steps involved to activate the retrieval of a server side auto-
incrementing value. 
 


---

Database Drivers 
146 
 
 
1. In the Dictionary, identify the column in the Column Properties User Options, with one of two 
option types: 
 
To identify a column in the dictionary as a server side Identity column, add the following user 
option:  
IsIdentity = TRUE 
 
This results in the following statement being generated by the template: 
 
FileLabel{PROP:ServerAutoInc, FieldNumber} = 1 
 
The supported values for IsIdentity are TRUE,True or 1 (it is not case sensitive). 
 
Remember, the column you identify must exist on the server as one that possesses the "Identity" 
characteristic. 
 
If you are returning more than one column in your own SQL code, use the ServerAutoIncColumn 
user option as follows: 
 
ServerAutoIncColumn=m 
 
where m is the SQL query column. 
 
This results in the following statement being generated by the template: 
 
FileLabel{PROP:ServerAutoInc, FieldNumber} = m 
 


---

Database Drivers and Interfaces 
147 
This essentially associates a column in the dictionary with a Server Side Auto-Incrementing 
Column. You may also need to add the needed SQL SELECT statement in the /AUTOINC driver 
string. For example: 
 
## /AUTOINC=SELECT LAST_INSERT_ID()
 
An Identity or ServerAutoIncColumn column cannot be used in a key with the auto number 
feature active. The template will display an error message, if you do this. 
In addition, server side auto incrementing columns are NOT supported for BLOB, MEMO, or 
GROUP data types, and any data element using the OVER attribute. 
 
Template Considerations 
When using this new feature with Clarion template chain applications, the trigger support needs 
to be enabled in order to use the IsIdentity and ServerAutoIncColumn field options. This option is 
found in the Global Properties File Options. 
 
This is necessary because all of the above template support is generated in the FileManager’s 
PreInsert method. 
 
 
 
 


---

Database Drivers 
148 
VIEW support for aggregate functions 
 
The SQL view engine supports PROP:GroupBy and PROP:Having.  These properties allow you 
to add respectively GROUP BY and HAVING SQL clauses to your SELECT statement.   
 
  
PROP:GroupBy must be set first to allow PROP:Having to be generated. 
 
See Also: Runtime SQL Properties for Views using SQL Drivers  
 
Example: 
 
## PROGRAM
 
  MAP 
  END 
 
## EMP       FILE,DRIVER('ORACLE'),NAME('EMP'),PRE(EMP)
## P_EKY_EMP  KEY(EMP:EMPNO),NOCASE,OPT,PRIMARY
## KEY_DEP    KEY(EMP:DEPTNO),DUP,NOCASE,OPT
Record     RECORD 
EMPNO       SHORT         !Emp-no 
ENAME       CSTRING(11)   !Employee name 
JOB         CSTRING(10)   !Job 
HIREDATE    DATE          !Hiredate 
MGR         SHORT         !Manager 
SAL         PDECIMAL(7,2) !Salary 
COMM        PDECIMAL(7,2) !Commisison 
## DEPTNO      BYTE
           END 
          END 
 
MyView VIEW(EMP) 
        PROJECT(EMP:Mgr) 
        PROJECT(EMP:Sal) 
       END 
 
## CODE


---

Database Drivers and Interfaces 
149 
## OPEN(EMP)
    OPEN(MyView) 
    MyView{'EMP:Sal',PROP:Name} = 'sum(sal)' 
    MyView{PROP:GroupBy} = 'Mgr' 
    MyView{PROP:Having} = 'sum(sal) > 100000' 
    SET(MyView) 
    NEXT(MyView) 
 
The example code above is the equivalent to "SELECT mgr, sum(sal) FROM EMP GROUP BY 
mgr HAVING sum(sal) > 100000" 
 
In other words, this code will return a list of all Manager IDs and the total salary of their 
subordinates if their subordinates make a total of more than 100000. 
 
 


---

Database Drivers 
150 
Date and Time Column Considerations 
A common practice in some SQL databases (MSSQL, Oracle, and others) is to define a 
composite DateTime column (i.e., one column representing two pieces of data). In order for 
Clarion to separate the date and time information for processing, an import of this DateTime 
column type into the Dictionary Editor results in the following type of data structure: 
 
Orderdate       STRING(8)               !original column name from SQL  
Orderdate_GROUP GROUP, OVER(Orderdate)  !structure created by Clarion 
Orderdate_DATE   DATE                   !use this column to reference date info 
Orderdate_TIME   TIME                   !use this column to ref time info 
                       END 
 
No matter what type of SQL/ADO/ODBC driver you are using, Clarion will detect and convert 
these composite DateTime columns for you automatically.  
  
MSSQL TIMESTAMP fields are now flagged as READONLY by the Dictionary Synchronizer. 
 
  
Know your back end!  For example, the SMALLDATETIME and DATETIME data types of MS-
SQL are treated equally, with both only being able to store the minimum of either the precision of 
the Clarion TIME field or the backend data type.  So, in the case of the SMALLDATETIME data 
type, the seconds and hundredths of a second are discarded, using the SMALLDATETIME rule 
that > 29.99 is rounded up to the next minute. 
Another note; If you don't need the time portion, you can just use a "Date" type field (as long as 
no one else is writing to the "Time" portion from another application). Otherwise, you 
will need to be aware that the time portion is not zero when filtering, sorting, etc. 
 
  
If you do not use the time part of a timestamp field then you can safely change the Clarion coumn 
definition from: 
 
TSField STRING(8) 
 
TSFieldGroup GROUP,OVER(TSField) 
DateFld       DATE 
TimeFld       TIME 
             END 
to 
TSField      DATE 
 


---

Database Drivers and Interfaces 
151 
Synchronizer Considerations 
When using the dictionary synchronizer, the READONLY attribute will be set by the MSSQL 
synchroniser for UNIQUEID and TIMESTAMP fields only.  The SQL Anywhere synchronizer sets 
it for fields that have a default value of TIMESTAMP. 
 
ODBC Extended Time Information 
If you define a single TIME field in your Clarion file definition, the ODBC driver (and all ODBC 
based drivers) will use the ODBC TIME_STRUCT structure to get and set the field.  This structure 
only supports passing the hours, minutes and seconds. 
 
If your backend stores more information than this in the time field (i.e., fractions of a second), you 
must use a timestamp structure to access the field for accurate indexing.  When a timestamp 
structure is used, then the driver uses an ODBC TIMESTAMP_STRUCT to communicate with the 
backend.   
 
Example: 
 
Orderdate       STRING(8)               !original column name from SQL  
Orderdate_GROUP GROUP, OVER(Orderdate)  !structure created by Clarion 
Orderdate_DATE   DATE                   !use this column to reference date info 
Orderdate_TIME   TIME                   !use this column to ref time info 
                      END 
 


---

Database Drivers 
152 
Clarion Functions used in SQL Filter Statements 
The following diagram shows in detail the conversion of supported Clarion functions with Clarion 
6.3 and prior versions to their SQL equivalents. 
 
 
With the new PROP:ServerCaseInsensitive set to 0 in version 6.3, the SQL behavior is 
equivalent to Clarion 6.2 
 
 
Clarion Code: 
UPPER(var) 
6.3 SQL Drivers 
Var 
6.3 Oracle 
Var 
6.2 SQL Drivers 
{fn UCASE(var)} 
6.2 Oracle 
UPPER(var) 
 
 
Clarion Code: 
LOWER(var) 
6.3 SQL Drivers 
Var 
6.3 Oracle 
Var 
6.2 SQL Drivers 
{fn LCASE(var)} 
6.2 Oracle 
LOWER(var) 
 
 
Clarion Code: 
NOT var 
6.3 SQL Drivers 
NOT var 
6.3 Oracle 
NOT var 
6.2 SQL Drivers 
NOT var 
6.2 Oracle 
NOT var 
 
 
Clarion Code: 
"SUB(var, 1, LEN(var) = constant" 
6.3 SQL Drivers 
var LIKE 'constant%' 
6.3 Oracle 
var LIKE 'constant%' 
6.2 SQL Drivers 
var LIKE 'constant%' 
6.2 Oracle 
var LIKE 'constant%' 
 
 
 
 


---

Database Drivers and Interfaces 
153 
Clarion Code: 
"MATCH(s1, s2, Match:Simple) <> 0" 
6.3 SQL Drivers 
s1 = s2 
6.3 Oracle 
s1 = s3 
6.2 SQL Drivers 
s1 = s4 
6.2 Oracle 
s1 = s5 
 
 
Clarion Code: 
"MATCH(UPPER(s1), UPPER(s2), Match:Simple) <> 0" 
6.3 SQL Drivers 
s1 = s2 
6.3 Oracle 
s1 = s3 
6.2 SQL Drivers 
{fn UCASE(s1)} = {fn UCASE(s2)} 
6.2 Oracle 
UPPER(s1) = UPPER(s2) 
 
 
Clarion Code: 
"MATCH(s1, s2, Match:Wild) <> 0" 
6.3 SQL Drivers 
s1 LIKE s2 (with ? Replaced with _ and * with %) 
6.3 Oracle 
s1 LIKE s2 (with ? Replaced with _ and * with %) 
6.2 SQL Drivers 
s1 LIKE s2 (with ? Replaced with _ and * with %) 
6.2 Oracle 
s1 LIKE s2 (with ? Replaced with _ and * with %) 
 
 
Clarion Code: 
"MATCH(UPPER(s1), UPPER(s2), Match:Wild) <> 0" 
6.3 SQL Drivers 
s1 LIKE s2 (with ? Replaced with _ and * with %) 
6.3 Oracle 
s1 LIKE s2 (with ? Replaced with _ and * with %) 
6.2 SQL Drivers 
{fn UPPER(s1)} LIKE s2  
 
(s2 is upper cased and ? replaced with _ and * with %) 
6.2 Oracle 
UPPER(s1) LIKE s2  
 
(s2 is upper cased and ? replaced with _ and * with %) 
 
 
Clarion Code: 
"MATCH(s1, s2, Match:Soundex) <> 0" 
6.3 SQL Drivers 
{fn SOUNDEX(s1)} = s2 
6.3 Oracle 
SOUNDEX(s1) = s2 
6.2 SQL Drivers 
{fn SOUNDEX(s1)} = s2 
6.2 Oracle 
SOUNDEX(s1) = s2 
 
 
 
 


---

Database Drivers 
154 
Clarion Code: 
"MATCH(UPPER(s1), UPPER(s2), Match:Soundex) <> 0" 
6.3 SQL Drivers 
{fn SOUNDEX(s1)} = s2 
6.3 Oracle 
SOUNDEX(s1) = s2 
6.2 SQL Drivers 
{fn SOUNDEX({fn UPPER(s1)})} = {fn UPPER(s2)}  
6.2 Oracle 
SOUNDEX(UPPER(s1)) = UPPER(s2) 
 
 
Clarion Code: 
Constant with non-displayable character 
6.3 SQL Drivers 
Non-displayable characters are converted to: 
 
{fn CHAR(ordinal value of character)} 
6.3 Oracle 
Non-displayable characters are converted to: 
 
CHAR(ordinal value of character) 
6.2 SQL Drivers 
Non-displayable characters are converted to: 
 
{fn CHAR(ordinal value of character)} 
6.2 Oracle 
Non-displayable characters are converted to: 
 
CHAR(ordinal value of character) 
 
 
Clarion Code: 
INSTRING('substring', var, instring(string, var,1,1) <> 0 
Clarion Code: 
INSTRING('substring', var, instring(string, var,1) <> 0 
Clarion Code: 
INSTRING('substring', var, instring(C, var) <> 0 
 
(where C is a single character string) 
6.3 SQL Drivers 
var LIKE '%string%' 
6.3 Oracle 
var LIKE '%string%' 
6.2 SQL Drivers 
var LIKE '%string%' 
6.2 Oracle 
var LIKE '%string%' 
 
 
Clarion Code: 
NULL(field) = 0 or <> 1 
6.3 SQL Drivers 
field IS NOT NULL 
6.3 Oracle 
field IS NOT NULL 
6.2 SQL Drivers 
field IS NOT NULL 
6.2 Oracle 
field IS NOT NULL 
 
 
Clarion Code: 
NULL(field) = 1 or <> 0 
6.3 SQL Drivers 
field IS NULL 
6.3 Oracle 
field IS NULL 
6.2 SQL Drivers 
field IS NULL 
6.2 Oracle 
field IS NULL 
 
 


---

Database Drivers and Interfaces 
155 
Clarion Code: 
date fields 
6.3 SQL Drivers 
{d yyyy-mm-dd} 
6.3 Oracle 
"TO_DATE('dd-mm-yyy', 'DD-MM-YYYY')" 
6.2 SQL Drivers 
{d yyyy-mm-dd} 
6.2 Oracle 
"TO_DATE('dd-mm-yyy', 'DD-MM-YYYY')" 
 
 
Clarion Code: 
time fields 
6.3 SQL Drivers 
{t hh:mm:ss} 
6.3 Oracle 
not supported by Oracle 
6.2 SQL Drivers 
{t hh:mm:ss} 
6.2 Oracle 
not supported by Oracle 
 
 
Clarion Code: 
timestamp fields 
6.3 SQL Drivers 
{ts yyyy-mm-dd hh:mm:ss} 
6.3 Oracle 
"TO_DATE('dd-mm-yyy hh:mm:ss', 'DD-MM-YYYY HH:MI:SS')" 
6.2 SQL Drivers 
{ts yyyy-mm-dd hh:mm:ss} 
6.2 Oracle 
"TO_DATE('dd-mm-yyy hh:mm:ss', 'DD-MM-YYYY HH:MI:SS')" 
 
 


---

Database Drivers 
156 
## CHECKFORNULL
The CHECKFORNULL field switch applies to all SQL drivers 
 
Usage: 
 
In the External Name attribute: 
‘field name | CHECKFORNULL’ 
 
When browsing through a table, it is sometimes necessary for the driver to request all rows 
that are at, or before, the current row. It does this by generating a WHERE clause. For 
example:  
WHERE (field1 <= value) AND (field1 < value OR field2 <= value2) 
 
The above example is for a two component key. For more components, the WHERE clause 
gets longer, and this will work well in most cases. However, in SQL, if a field has a NULL 
value, then field < value is false, field = value is false, and field > value is also false. So, if you 
are sorting on field components that contain NULL values, you need to set the external field 
name of the field to  
 
‘field name | CHECKFORNULL’ 
 
This will force the driver to generate: 
WHERE ((field1 <= value OR field1 IS NULL)) AND ((field1 < value OR field1 IS NULL) OR field2 <= value2) 
 
So, in this example, the WHERE clause will also return rows that contain NULL values, instead of 
rejecting them. 
 
 


---

Database Drivers and Interfaces 
157 
Optimizing SET processing using the WHERE driver 
string 
 
Regarding SQL databases, standard SET(key,key) processing is not always the most efficient 
approach. This is because the SET(key,key) statement sets the starting part of the search, but 
not the ending part of the search. 
 
Consider this code sequence: 
 
CLEAR(PHO:Record) 
PHO:CategoryID = 1 
SET(PHO:FK_CategoryKey,PHO:FK_CategoryKey) 
## LOOP
  IF Access:Photos.Next() <> LEVEL:Benign 
## BREAK
  END 
  IF PHO:CategoryID <> 1 
## BREAK
  END 
END 
 
To achieve better performance use the following sequence: 
 
CLEAR(PHO:Record) 
PHO:CategoryID = 1 
SET(PHO:FK_CategoryKey,PHO:FK_CategoryKey) 
SEND(Photos, '/WHERE CategoryId = ''' & PHO:CategoryID & '''') 
!Eliminates PHO:CategoryID checking 
## LOOP
  IF Access:Photos.Next() <> LEVEL:Benign 
## BREAK
  END 
END 
 
For the best performance, use the following sequence: 
 
CLEAR(PHO:Record) 
PHO:CategoryID = 1 
SET(PHO:FK_CategoryKey)   !SET(KEY,KEY) not needed 


---

Database Drivers 
158 
SEND(Photos, '/WHERE CategoryId = ''' & PHO:CategoryID & '''') 
## LOOP
  IF Access:Photos.Next() <> LEVEL:Benign 
## BREAK
  END 
END 
 
All of the filtering you need is defined and optimized in the /WHERE driver string via the SEND 
command. 
If you notice that the backend is doing a full table scan, this would indicate that a design problem 
is possible on the backend database.  Clarion simply sends a SELECT statement to the server.  It 
does NOT tell the server how to fulfill that SELECT.  That decision is left up to the server.  For 
example, if you send to the server: 
 
SELECT * FROM MyTable WHERE myField > 23 ORDER BY myField 
 
If there is no corresponding index on the server, then the server has no choice but to do a full 
table scan.  In that case, instead of rewriting all of the Clarion code to use a Prop:SQL statement, 
the time would be better spent on optimizing the database design. 
 
Using PROP:Where (or SEND(FILE, '/WHERE.....')) can limit the result set you get, and even 
eliminate using a key in the SET statement.  Clarion does this by setting or adding to the WHERE 
clause containing your condition, greatly reducing the load on the server.   
Note: Do not use the standard clarion field name syntax (e.g., pre:columnname). 
 
For example: 
 
  SET(MyFile) 
  MyFile{PROP:WHERE} = 'CUSTOMERID = ' & LOC:CUSTOMERID 
## LOOP
## NEXT(MYFILE)
## IF ERRORCODE() THEN BREAK.
    ! process record here 
  END 
 
will retrieve all the MYFILE records for a single customer. 
 
## SET(MYF:K_DATE)
## MYFILE{PROP:WHERE} = 'CUSTOMERID = ' & LOC:CUSTOMERID
 
will do the same, but order them by the date (whatever is in MYF:K_DATE). 


---

Database Drivers and Interfaces 
159 
 
Using PROP:Where also eliminates the hassle of handling "field alignment" when using 
PROP:SQL to retrieve records.  It accomplishes what you would get if you intend to do the 
equivalent of a "SELECT *". 
 
You can also improve performance by using a BUFFER statement, like this: 
 
  BUFFER(MyFile, 20) 
## SET(MYF:K_DATE)
## MYFILE{PROP:WHERE} = 'CUSTOMERID = ' & LOC:CUSTOMERID
 
 
 


---

Database Drivers 
160 
Performance Considerations 
Generally, Clarion's development environment (Data Dictionary Import Wizard, Database Drivers, 
and templates) produces optimized, high performance, SQL applications. 
This section describes some of the issues involved in producing these optimized applications. 
You should be aware of these issues so you can maintain a high level of performance as you 
take more control of the development process. 
Define Only the Fields You Use 
With the SQL Accelerator drivers you only need to define the fields that you actually use in the 
Clarion Data Dictionary. This reduces both the overhead within your Clarion application and 
network traffic.  
For example, if your SQL table contains 200 columns but only three are needed for a particular 
program, retrieving only those three fields dramatically reduces the amount of data sent over the 
network. If each column contains 20 bytes, then three columns would require only 60 bytes to be 
transferred whereas all 200 columns requires a 4,000 byte transfer. 
After you have imported the table definition into your Clarion Data Dictionary, use the Dictionary 
Editor's Columns / Key Definition dialog to delete the fields/columns you don't use. 
Matching Clarion Keys to SQL Constraints and Indexes 
Generally, the Clarion KEY definition need not exactly match an index in the SQL database. The 
Clarion KEY simply serves to supply the appropriate ORDER BY clause for driver generated 
SELECT statements. 
However, if the Clarion KEY does not match an SQL key or index, then the SQL server must build 
a temporary logical view every time you access the table using the unmatched KEY. This can be 
very slow for large files.  
The best way to guarantee the Clarion KEYs have a matching SQL constraint or index, is to 
import the table, view, or synonym definition into the Clarion Data Dictionary. See Import the 
Table Definitions. 
 
Most, but not all, SQL servers sort case insensitively.  So, for example,  when you issue the 
following SELECT statement: 
 
SELECT Name FROM table ORDER BY Name 
 
You will get back: 
 
Alan 
arthur 
Brian 
chris 
James 
 
And not: 


---

Database Drivers and Interfaces 
161 
 
arthur 
chris 
Alan 
Brian 
James 
 
If a key does not have the Case Sensitive option checked in the dictionary editor, then the SQL 
Accelerator is forced to issue a SELECT statement with ORDER BY UPPER(key component) and 
WHERE clauses including calls to the UPPER function.  In most cases this is not necessary and 
may impact on performance, depending on the sophistication of your server.  A more advanced 
server will notice the unnecessary calls to UPPER and ignore them.  A less advanced server will 
not notice them and probably do a full table scan to process the SELECT statement. 
 
Filter (Contracting) Locators 
Using Filter Locators on your BrowseBox controls rather than Incremental or Step Locators can 
reduce the volume of data sent between client and server. See BrowseBox Control Template for 
more information on Filter Locators. 
Approximate Record Count 
By default, the Clarion templates generate code to count the total number of records to be 
processed for a report. This total record count allows for an accurate progress bar display during 
report generation. However, for large tables, the resulting SELECT COUNT(*) can be very slow. 
Therefore, for large reports, we recommend providing an approximate record count to suppress 
the SELECT COUNT(*) as follows: 
1. In the Application Tree dialog, RIGHT-CLICK the (Report) procedure, then choose 
Properties from the popup menu. This opens the Procedure Properties dialog. 
2. Press the Report Properties button to open the Report Properties dialog. 
3. In the Approx. Record Count field, type an approximate record count for the report, 
such as 5000. 
4. Press the OK button to close the Report Properties dialog. 
5. Press the OK button again to return to the Application Tree dialog. 
6. Press the 
 button to save your work. 
Fixed Thumbs and Movable Thumbs 
By default, Clarion's code generation Wizards use Fixed Thumbs when Browsing SQL tables 
because Movable Thumbs can cause major performance slow downs on large tables in Clarion / 
SQL applications. For this reason, we recommend that you specify Fixed Thumbs for your 
manually place BrowseBox controls as follows: 
1. In the Application Tree dialog, RIGHT-CLICK the Browse procedure, then choose 
Extensions from the popup menu. This opens the Extension and Control Templates 
dialog. 
2. In the list box, select Browse on ..., then press the Scroll Bar Behavior button. This 
opens the Scroll Bar Behavior dialog. 
3. In the Scroll Bar Type drop-down list, select Fixed Thumb, then press the OK button. 


---

Database Drivers 
162 
4. Press the OK button again to return to the Application Tree dialog. 
5. Press the Save button 
 to save your work. 
SQL Batch Transaction Processing  
Most SQL databases operate in auto-commit mode. This means that any operation that updates 
a table (ADD, PUT, or DELETE) executes an implicit COMMIT. This can be very slow for a series 
(batch) of updates.  
To optimize batch processes, surround any batch processing in a transaction frame (that is, with 
LOGOUT and COMMIT). The LOGOUT command prevents any subsequent implicit COMMITs 
until the transaction frame ends with either a COMMIT or a ROLLBACK. For example: 
  LOGOUT(.1,OrderDetail)              !Begin Transaction 
   DO ErrHandler                      !always check for errors 
  LOOP X# = 1 TO RECORDS(DetailQue)   !Process stored detail records 
   GET(DetailQue,X#)                  !Get one from the QUEUE 
    DO ErrHandler                     !check for errors 
   Det:Record = DetailQue             !Assign to record buffer 
   ADD(OrderDetail)                   !and add it to the file 
    DO ErrHandler                     !check for errors 
  END 
  COMMIT                              !Terminate good transaction 
 
 ErrHandler ROUTINE                   !Error routine 
  IF NOT ERRORCODE() THEN EXIT.       !Bail out if no error 
  ROLLBACK                            !Rollback the bad transaction 
  MESSAGE('Transaction Error - ' & ERROR())!Log the error 
  RETURN                              !and get out 
You may want to issue intermittent calls to COMMIT and LOGOUT to save data at regular 
intervals. See the Language Reference for more information. 
 


---

Database Drivers and Interfaces 
163 
Using Embedded SQL 
You can use Clarion's property syntax (PROP:SQL and PROP:SQLRowSet) to send SQL 
statements to the backend SQL server, within the normal execution of your program. For 
backward compatibility, you can also use the SEND function to send SQL statements; however, 
we recommend using the property syntax.  
  
When you issue a SELECT or CALL statement using PROP:SQL or any statement using 
PROP:SQLRowSet, the returned columns must match the fields declared in the named file or 
view. In addition, if you use VIEW{Prop:SQL} to issue a SELECT statement, the fields in the 
SELECT must be ordered based on the field order in the file definition, not the PROJECT  
sequence. 
## PROP:SQL
You can use Clarion's property syntax (PROP:SQL) to send SQL statements to the backend SQL 
server, within the normal execution of your program. You can send any SQL statements 
supported by the SQL server.  
This capability lets your program do backend operations independent of the SQL Accelerator 
driver's generated SQL. For example, multi-record updates can often be accomplished more 
efficiently with a single SQL statement than with a template generated Process procedure which 
updates one record at a time. In cases like these it makes sense for you to take control and send 
custom SQL statements to the backend, and PROP:SQL lets you do this. 
If you issue an SELECT or CALL statement, you use NEXT(file) to retrieve the result set one row 
at a time, into the file's record buffer. The FILEERRORCODE() and FILEERROR() functions 
return any error code and error message set by the back-end SQL server. 
You may also query the contents of PROP:SQL to get the last SQL statement issued by the file 
driver. 
Examples: 
SQLFile{PROP:SQL}='SELECT field1,field2 FROM table1'     | 
           & 'WHERE field1 > (SELECT max(field1)'  | 
           & 'FROM table2'                            !Returns a result set you
  
                                                      ! get one row at a time 
                                                      ! using NEXT(SQLFile) 
 
SQLFile{PROP:SQL}='CALL GetRowsBetween(2,8)'          !Call stored procedure 
 
SQLFile{PROP:SQL}='CREATE INDEX ON table1(field1 DESC)' !No result set 
  
SQLFile{PROP:SQL}='GRANT SELECT ON mytable TO fred'   !DBA tasks 
 
SQLString=SQLFile{PROP:SQL}                           !Get last SQL statement 


---

Database Drivers 
164 
PROP:SQLRowSet 
If you want to execute an SQL statement that returns a result set, you have two options.  If you 
need to execute a SELECT or CALL statement you can use PROP:SQL.  However, if you want to 
issue an other SQL statement that returns a result set, you must use PROP:SQLRowSet.  You 
must use NEXT(file|view) to retrieve the rows returned by the SQL statement.  
SEND and SQL 
You can use the Clarion SEND procedure to send an SQL command to the backend database. 
This is provided for backward compatibility with early versions of Clarion. We recommend using 
the property syntax to send SQL statements to the backend database. 
Examples: 
SEND(SQLFile,'SELECT field1,field2 FROM table1'| 
       & 'WHERE field1 > (SELECT max(field1)'  | 
       & 'FROM table2') ! Returns a result set you  
                        ! get one row at a time 
                        ! using NEXT(SQLFile) 
 
SEND(SQLFile,'CALL GetRowsBetween(2,8)')   !Call stored procedure 
 
SEND(SQLFile,'CREATE INDEX ON table1(field1 DESC)') !No result set 
Using Embedded SQL for Batch Updates 
SQL does a good job of handling batch processing procedures such as: printing reports, 
displaying a screen full of table rows, or updating a group of table rows. 
The SQL Accelerator drivers take full advantage of this when browsing a table or printing. 
However, they do not always use it to its best advantage with the Process template or in code 
which loops through a table to update multiple records. Therefore, when doing batch updates to a 
table, it can be much more efficient to execute an embedded SQL statement than to rely on the 
code generated by the Process template. 
For example, to use PROP:SQL to increase all Salesman salaries by 10% you could: 
 SQLFile   FILE,DRIVER('Oracle'),NAME(SalaryFile) 
 Record     RECORD 
 SalaryAmount  PDECIMAL(5,2),NAME('JOB') 
            END 
           END 
 
## CODE
  SqlFile{PROP:SQL} = 'UPDATE SalaryFile SET '&| 
## 'SALARY=SALARY * 1.1 WHERE JOB=''S'''
The names used in the SQL statement are the SQL table names, not the Clarion field names. 
PROP:SQLFilter 
You can use PROP:SQLFilter to filter your VIEWs using native SQL code rather than Clarion 
code. 
When you use PROP:SQLFilter, the SQL filter is passed directly to the server. As such it cannot 
contain the name of variables or functions that the server is not aware of; that is the filter 
expression must be valid SQL syntax with valid SQL column names. For example: 
VIEW{PROP:SQLFilter} = 'Date = TO_DATE(''01-MAY-1996'',''DD-MON-YYYY'')' 
or 


---

Database Drivers and Interfaces 
165 
VIEW{PROP:SQLFilter} = 'StrField LIKE ''AD%''' 
Combining VIEW Filters and SQL Filters 
When you use PROP:SQLFilter, the SQL filter may replace any filter specified for the VIEW, or it 
may be in addition to a filter specified for the VIEW. Prefix the SQL filter with a plus sign (+) to 
append the SQL filter to the VIEW filter specified. For example: 
VIEW{PROP:SQLFilter} = '+ StrField LIKE ''AD%''' 
When you append the SQL filter by using the plus sign, the logical end result of the filtering 
process is (View Filter) AND (SQL Filter). 
Omit the plus sign (+) to replace the Clarion filter with the SQL filter. When you replace the 
Clarion filter with the SQL filter by omitting the plus sign, the logical end result of the filtering 
process is simply (SQL Filter). 
Calling a Stored Procedure 
To call a stored procedure the following SQL syntax is used to build the SQL calling statements. 
 
[output_bound_field = ] call_type [([parameter[,parameter]…])] 
  
call_type 
CALL or NORESULTCALL 
parameter  
constant or bound_field 
constant must conform to the syntax of your backend.  Normally numerics and 
strings are the same as Clarion.  For ODBC systems, date constants are in the 
format {d 'yyyy-mm-dd'}, time constants are {t 'hh:mm:ss'} and time stamp 
constants are {ts 'yyy-mm-dd hh:mm:ss'}. 
bound_field is either an output_bound_field or output_bound_field '['bind_type']' 
output_bound_field 
&variable (This must be a variable that you have 
previously bound using the BIND function) 
bind_type 
IN, OUT, INOUT, BINARY (valid on all SQL drivers, 
except Oracle) [BINARY] on a parameter indicates that 
this should be bound as a binary field. See the example 
code below to see how this can be used.  
 
## CALL
To call a stored procedure you use property syntax to issue the SQL syntax 'CALL 
storedprocedure.' 
Example: 
MyFile{PROP:SQL} = 'CALL SelectRecordsProcedure (&MyVar[INOUT])' 
 
## NORESULTCALL


---

Database Drivers 
166 
The SQL Accelerator drivers also allow the syntax 'NORESULTCALL storedprocedure' for stored 
procedures that do not return a result set. 
Example: 
MyFile{PROP:SQL} = 'NORESULTCALL SelectRecordsProcedure (&MyVar[INOUT])' 
 
Return Values (bind_type) 
The Acclerator drivers support return codes, output parameters, and in/out parameters for stored 
procedures. These are defined using IN, OUT, and INOUT. IN declares a variable as input, OUT 
declares a variable as output, and INOUT declares a variable as both input and output. You can 
also have your stored procedures return a result set.  
 
When you issue a {PROP:SQL} = '&return = call storedProcedure' against MSSQL, the field 
bound to return will not hold the result of the procedure call until all records have been retrieved 
via calls to NEXT(file) 
The BINARY switch is used to signal the driver to pass the data in the bound field as binary data 
rather than character data. See the example below. 
Example: 
MyFile   FILE,DRIVER('ODBC') 
Record    RECORD 
ErrorCode  LONG 
ErrorMsg   STRING(100) 
          END 
         END 
## CODE
 OPEN(MyFile) 
 MyFile{PROP:SQL} = 'CALL ProcWithResultSet' 
 NEXT(MyFile) 
## IF ~ERRORCODE()
  IF MyFile.ErrorCode THEN STOP(MyFileErrorMsg). 
 END 
 
 
The above example shows how to return a result set. The result set must match the fields 
declared in the named file or view. The storedprocedure ProcWithResultSet includes a 
final select statement that results with the set of requested data. 
  
Example: 
## PROGRAM
MAP 
 CallProc(STRING) 
END 
 
MyFile  FILE,DRIVER('MSSQL') 
Record   RECORD 
c         LONG 
         END 
        END 
Ret   LONG 


---

Database Drivers and Interfaces 
167 
Out   STRING(10) 
 
## CODE
 
BIND('RetCode', Ret) 
BIND('Out', Out) 
CallProc('&RetCode = CALL StoredProcTest(''1'',&Out)') 
MESSAGE(Return value of StoredProcTest =' & Ret) 
MESSAGE(Output parameter of StoredProcTest =' & Out) 
  
CallProc PROCEDURE(Str) 
## CODE
MyFile{PROP:SQL} = Str 
 
  
The above example shows how to return an output parameter.  
 
  
 
Example: 
## PROGRAM
 
  MAP 
  END 
 
  PRAGMA('link(C%V%MSS%X%%L%.LIB)') 
 
SQLFile FILE,DRIVER('MSSQL'),NAME('SYSFILES') 
## REC      RECORD
## ID        LONG
## NAME      CSTRING(100)
         END 
        END 
 
## TS              STRING(8)
## CODE
    OPEN(SQLFile) 
    SQLFile{PROP:SQL} = 'DROP PROCEDURE tstest' 
    SQLFile{PROP:SQL} = 'CREATE PROCEDURE tstest @ts as timestamp AS '& | 
                        ' return' 
## BIND('TS',TS)
## TS='<0><0><0><0><0><0><5H><0DDH>'
    SQLFile{PROP:SQL}='NORESULTCALL TSTEST(&TS[IN][BINARY])' 
 


---

Database Drivers 
168 
  
The above example shows how to use the IN and BINARY switches. 
 
For a more specific example tailored to MSSQL, refer to the MSSQL Accelerator topic. 
 


---

Database Drivers and Interfaces 
169 
General Rules for Browsing SQL-Based Tables 
This topic presents some general programming rules that need to be followed when browsing 
SQL-based tables within your generated applications.  In the explanations that follow each rule, 
the pseudo-SQL code is shown to demonstrate how the SQL driver processes the table from 
within the Clarion program. 
 
  
 
Rule Number One:  
You should not design a browse procedure using an SQL table without any 
key defined.  The simple reason is that SQL does not support the concept 
of descending order with no order. 
 
Explanation: 
What you are asking for (in pseudo SQL) is 
 
To fill the first page 
and 
Select a row: 
SELECT * FROM table 
 
SELECT * FROM table WHERE pkfield = value  
(pkfield is the primary key field) 
 
To fill from current record forward: 
SELECT * FROM table WHERE pkfield >= value 
 
To fill from current record backwards: 
SELECT * FROM table WHERE pkfield < value  DESC??? 
  
Without the DESC you will get the fields in the same order as going forward. 
 
 
 
Rule Two: 
You not only have to have a key defined, but the sort order has to be 
unique. 
 
Explanation: 
Let us use a simple table example with two fields F1 and F2 with contents of 
 


---

Database Drivers 
170 
## F1  F2
1   1 
1   2 
1   3 
2   1 
2   2 
2   3 
3   1 
 
Now if you have a browse on this table ordered on F1 only, the above sequence would produce 
the following results. 
 
First, we fill the Browse: 
SELECT F1, F2 FROM table ORDER BY F1 
 
Our expected result set will look like this: 
 
## F1  F2
1   1 
1   2 
1   3 
2   1 
2   2 
2   3 
3   1 
 
Next, we select the fifth row: 
SELECT F1, F2 FROM table WHERE F1=2 and F2=2 
 
With the record selected, we fill from the current record forward: 
SELECT F1, F2 FROM table WHERE F1>=2 ORDER BY F1 
 
Normally you will get a result set looking like: 
 
## F1  F2
2   1 
2   2 
2   3 
3   1 


---

Database Drivers and Interfaces 
171 
 
But the driver knows that we are starting on F1=2 and F2=2, so it only returns a result set of: 
 
## F1  F2
2   2 
2   3 
3   1 
 
Next, the browse needs to fill from the current record backwards.   This generates: 
SELECT F1, F2 FROM table WHERE F1 <= 2 ORDER BY F1 DESC 
 
Which would normally give a result set of: 
 
## F1  F2
2   1 
2   2 
2   3 
1   1 
1   2 
1   3 
 
Notice that this sort is not the same as reversing the original sort: 
 
## F1  F2
2   3 
2   2 
2   1 
1   3 
1   2 
1   1 
 
Again, since the driver knows that you are actually starting from F1=2, F2=2 so you get a result 
set of: 
 
## F1  F2
2   2 
2   3 
1   1 
1   2 


---

Database Drivers 
172 
1   3 
 
Notice that F1=2, F2=3 is retrieved when asking for either forward or backwards results.  This 
means you may end up with a browse screen looking like this: 
 
## F1  F2
1   3 
1   2 
1   1 
2   3 <<<<<<< result returned by backward retrieve 
2   2 
2   3 <<<<<<< result returned by forward retrieve 
3   1 
 
The only way to stop this ghosting effect is to make sure that all your browses always use 
a unique sort sequence. In addition any other optional sort sequences should also include 
a unique component. 
 
For example, if you had a unique EmployeeID component, and another Name key based on 
LastName and FirstName, add the unique EmployeeID as the third component of the name key. 


---

Database Drivers and Interfaces 
173 
Runtime SQL Properties for Views using SQL Drivers 
The SQL View Engine allows you to specify SQL that will be substituted for a column in a 
SELECT statement using the following syntax: 
 
view{'field_label',PROP:Name} = SQLString  
where SQLString is any SQL valid within a SELECT statement. 
Example: 
## PROGRAM
  MAP 
  END 
 
## EMP       FILE,DRIVER('ORACLE'),NAME('EMP'),PRE(EMP)
## P_EKY_EMP  KEY(EMP:EMPNO),NOCASE,OPT,PRIMARY
## KEY_DEP    KEY(EMP:DEPTNO),DUP,NOCASE,OPT
Record     RECORD 
EMPNO       SHORT !Emp-no 
ENAME       CSTRING(11) !Employee name 
JOB         CSTRING(10) !Job 
HIREDATE    DATE !Hiredate 
MGR         SHORT !Manager 
SAL         PDECIMAL(7,2) !Salary 
COMM        PDECIMAL(7,2) !Commisison 
## DEPTNO      BYTE
           END 
          END 
 
MyView VIEW(EMP) 
        PROJECT(EMP:EmpNo) 
       END 
 
## CODE
## OPEN(EMP)
    OPEN(MyView) 
    MyView{'EMP:EmpNo',PROP:NAME} = 'count(*)' 
    SET(MyView) 
    NEXT(MyView) 
 
This example will produce the equivalent of "SELECT count(*) FROM EMP". 
 


---

Database Drivers 
174 
Debugging Your SQL Application 
All of the SQL Accelerator drivers (and ISAM drivers as well) can create a log file documenting 
Clarion I/O statements they process, the corresponding SQL statements, and the SQL return 
codes. 
You can generate system-wide logs and on-demand logs (conditional logging based on your 
program logic via property syntax). 
System-wide Logging 
There is an utility/example application --Trace.EXE. You can run this from the Clarion Start Menu 
option. A compiled version is installed in the .\BIN directory and the source .APP is installed in the 
\Examples\DriverTrace directory. This utility allows you to easily set tracing options for each file 
driver and for the VIEW engine.  
These tracing options are stored in DRIVERS.INI in the 
CSIDL_APPDATA\SoftVelocity\Clarion\<clarion_version> folder.   
For system-wide logging, you can add the following to your DRIVERS.INI file: 
[CWdriver] 
Profile=[1|0] 
Details=[1|0] 
Trace=[1|0] 
TraceFile=[Pathname] 
where driver is the database driver name (for example [CWTopSpeed]). Neither the INI section 
name [CWdriver] nor the INI entry names are case sensitive. 
Profile=1 (PROP:Profile) tells the driver to include the Clarion I/O statements in the log file;  
Profile=0 tells the driver to omit Clarion I/O statements. The Profile switch must be turned on for 
the Details switch to have any effect. 
Details=1 (PROP:Details) tells the driver to include record buffer contents in the log file; 
however, if the file is encrypted, you must turn on both the Details switch and the 
ALLOWDETAILS switch to log record buffer contents (see ALLOWDETAILS). Details=0 tells the 
driver to omit record buffer contents. The Profile switch must be turned on for the Details switch to 
have any effect. 
Trace=1 tells the driver to include all calls to the back-end file system, including the generated 
SQL statements and their return codes, in the log file. Trace=0 omits these calls. The Trace 
switch generally generates log information that helps to debug the SQL drivers, but is normally 
not particularly useful to the developer. 
TraceFile names the log file to write to. If TraceFile is omitted the driver writes the log to 
driver.log in the current directory. Pathname is the full pathname or the filename of the log file to 
write. If no path is specified, the driver writes the specified file to the current directory. 
  
To view the trace details in your system debugger, name the target trace file DEBUG:.  
Logging opens the named logfile for exclusive access. If the file exists, the new log data is 
appended to the file. 
On Demand Logging 
For on-demand logging you can use property syntax within your program to conditionally turn 
various levels of logging on and off. The logging is effective for the target table and any view for 
which the target table is the primary table. 


---

Database Drivers and Interfaces 
175 
file{PROP:Profile}=Pathname   !Turns Clarion I/O logging on 
file{PROP:Profile}=''         !Turns Clarion I/O logging off 
PathName = file{PROP:Profile} !Queries the name of the log file 
file{PROP:Log}=string         !Writes the string to the log file 
file{PROP:Details}=1          !Turns Record Buffer logging on 
file{PROP:Details}=0          !Turns Record Buffer logging off 
where Pathname is the full pathname or the filename of the log file to create. If you do not specify 
a path, the driver writes the log file to the current directory. 
You can also accomplish on demand logging with a SEND() command and the LOGFILE  driver 
string. See LOGFILE for more information. 
Language Level Error Checking 
You can use the FILEERROR() and FILEERRORCODE() functions to capture messages and 
codes returned from the backend server to the SQL Accelerator driver. See the Language 
Reference for more information on these functions. 
See Also: 
PROP:Profile , PROP:Details , ALLOWDETAILS , PROP:LOG , PROP:LOGSQL 
 
 


---

Database Drivers 
176 


---

Database Drivers and Interfaces 
177 
SQL Driver Strings 
There are switches or "driver strings" you can set to control the way your application creates, 
reads, and writes files with a specific driver. Driver strings are simply messages or parameters 
that are sent to the file driver at run-time to control its behavior. See Common Driver Features--
Driver Strings for an overview of these runtime Database Driver switches and parameters. 
 
  
A forward slash precedes all SQL driver strings. The slash allows the driver to distinguish 
between driver strings and SQL statements sent with the SEND function. 
The SQL Accelerator Drivers support the following Driver Strings: 
## ALLOWDETAILS
## APPENDBUFFER
## AUTOINC
## BINDCOLORDER
## BINDCONSTANTS
## BUSYHANDLING
## BUSYMESSAGE
## BUSYRETRIES
## CLIPSTRINGS
## FASTCOLUMNFETCH
## FORCEUPPERCASE
## GATHERATOPEN
## GETINFO
## IGNORETRUNCATION
## ISOLATIONLEVEL
## JOINTYPE
## LOGFILE
## NESTING
## ODBCCALL
## ORDERINSELECT
## PREAUTOINC
## TURBOSQL
## USEINNERJOIN
## VERIFYVIASELECT
## WHERE
## ZERODATE
## ZEROISNULL
 


---

Database Drivers 
178 
## APPENDBUFFER
 
DRIVER('SQLDriver', '/APPENDBUFFER = size ' ) 
[ Buffer" = ] SEND(file, 'APPENDBUFFER [ = size ]' ) 
 
By default, APPEND adds records to the file one at a time. To get better performance over a 
network you can tell the driver to build up a buffer of records then send all of them to the SQL 
back end at once. Size is the number of records you want to allocate for the buffer. SEND returns 
the number of records that will fit in the buffer. 
 
## AUTOINC
 
DRIVER('SQLDriver', '/AUTOINC = "SQL statement" ' ) 
[ Buffer" = ] SEND(file, 'AUTOINC [ = SQL statement ]' ) 
 
The AUTOINC driver string is used to specify an SQL statement that you want executed for 
retrieving a server side auto-incrementing field. 
The Dictionary Editor contains a Driver String Options dialog in the Table Properties to allow 
easy entry of this string. 
See Also:     Server side auto-incrementing values  


---

Database Drivers and Interfaces 
179 
## BINDCOLORDER
 
DRIVER('SQLDriver', '/BINDCOLORDER = [0 | 1 | 2]' ) 
 
(Valid for all drivers except Oracle) 
When executing a SELECT statement the driver has to do the following: 
 
1. Compile the SELECT statement 
2. Bind memory locations for the columns to be returned 
3. Bind memory locations for the WHERE clause 
4. Executes the SELECT statement 
5. Fetch the data 
 
The order that these are executed is not completely fixed. The compile (Step 1) must be done 
first and the fetch (Step 5) last. However, the other three steps can be executed in any order. 
If BINDCOLORDER is set to 0, the order is 1, 2, 3, 4, 5. 
If BINDCOLORDER is set to 1, the order is 1, 3, 2, 4, 5. 
If BINDCOLORDER is set to 2, the order is 1, 3, 4, 2, 5.  
 
The default is 0 for all supported driver except MySQL, which has a default setting of 2. 
 
## BINDCONSTANTS
 
DRIVER('SQLDriver', '/BINDCONSTANTS = TRUE | FALSE ' ) 
[ Bind" = ] SEND(file, '/BINDCONSTANTS [ = TRUE | FALSE ]' ) 
 
(NOTE: Not valid for ORACLE Accelerator) 
By default (BINDCONSTANTS=TRUE) the SQL Accelerator binds memory locations instead of 
generating text equivalents for constant values.  However, some back ends get confused when 
doing this. So if you find that your SQL based BrowseBox will not scroll, or your backend returns 
incorrect results for a BrowseBox you can turn off binding of constant values by setting 
BINDCONSTANTS to FALSE. 
 


---

Database Drivers 
180 
## BUSYHANDLING
 
DRIVER('SQLDriver', '/BUSYHANDLING = 1|2|3|4 ' ) 
[ Busy" = ] SEND(file, '/ BUSYHANDLING [ = 1|2|3|4 ]' ) 
file{PROP:BusyHandling} = 1|2|3|4 
 
Valid for all SQL drivers and ODBC except for Oracle. 
BUSYHANDLING is used to set the strategy for handling busy connections with MSSQL and 
ODBC drivers. This setting is system wide, so once you set it (regardless of which table) it is set 
for all tables on all threads. 
 
  
The BUSYHANDLING switch must be set PRIOR to opening any tables. 
MSSQL/ODBC does not allow more than one statement per connection to be active at any one 
time.  If you attempt to issue two statements on separate threads, MSSQL/ODBC will return an 
error message of "[Microsoft][ODBC SQL Server Driver]Connection is busy with results for 
another hstmt". 
There are three different strategies the ODBC and MSSQL drivers use to avoid this error: 
1. Raise a separate connection per thread 
2. Lock the connection while a statement operation is being processed 
3. Retry when the error occurs. 
The advantage of using one connection per thread is that once a thread is opened, no slowdown 
will occur. The disadvantages of using one connection per thread is that you cannot use 
connection dependant temporary tables. Also, the first time you have a new thread open the 
connection needs to be raised, which may be slow. The driver pools connections, so this slow 
down only occurs when you have more threads open than you previously had during the running 
of the application. 
The advantages of locking connections is that you can use connection dependant temporary 
tables and starting new threads will not be slowed down.  However, all statement operations will 
be slowed down a bit so as the lock can be obtained and released. 
The advantages of looping when the busy error occurs are the same as for the locking strategy, 
plus you do not have the slow down caused by locking and releasing the connection.  However, 
MSSQL does not return a unique error code for the busy error.  So the driver is forced to use the 
error text to detect the busy error.  This text will change depending on the language your user's 
MSSQL is set up to use.  So you will need to either hope that your users are all using the English 
version of MSSQL or tell the driver what the error string is for each user. 


---

Database Drivers and Interfaces 
181 
To set which strategy the driver should use: 
1 
indicates that the driver should do nothing about the error. This would be used 
when an application is only single threaded. 
2 
indicates to use the one connection per thread strategy. 
  
The BUSYHANDLING=2 setting forces multiple connections. Basically, if you 
want to use BUSYHANDLING=2 and MSSQL and transaction processing 
together, then you must keep a file open on the program’s main thread. 
 
3 
indicates to use the retry on busy strategy.  This is the default driver behavior. 
4 
indicates to use the connection locking strategy. 
 
See Also:     BUSYMESSAGE, BUSYRETRIES  
 
## BUSYMESSAGE
 
DRIVER('SQLDriver', '/BUSYMESSAGE = str ' ) 
[ Busy" = ] SEND(file, '/ BUSYMESSAGE [ = str ]' ) 
file{PROP:BusyMessage} = str 
 
 
Valid for MSSQL and ODBC drivers only. The str parameter indicates the message to use when a 
busy connection is detected. 
Use this driver string to set the string the driver should look for to detect a busy connection.  The 
default message the driver looks for is "[Microsoft][ODBC SQL Server Driver]Connection is busy 
with results for another hstmt". 
MSSQL and ODBC do not return a unique error code for the busy connection error.  Therefore, 
the driver is forced to use default error text to detect the busy error.  This text changes depending 
on the language your user's MSSQL is set up to use. BUSYMESSAGE allows the programmer to 
detect a consistent busy message, regardless of language version of MS SQL or ODBC that is 
used. 
 


---

Database Drivers 
182 
## BUSYRETRIES
 
DRIVER('SQLDriver', '/BUSYRETRIES = n ' ) 
[ Busy" = ] SEND(file, '/ BUSYRETRIES [ = n ]' ) 
file{PROP:BusyRetries} = n 
 
 
Valid for MSSQL and ODBC drivers only. The n parameter indicates the number of retries 
(default = 20). 
BUSYRETRIES is used to set the number of times to retry a connection that is busy. This is the 
default busy strategy (attempt a retry) that is used for MSSQL/ODBC. 
 
See Also:     BUSYHANDLING, BUSYMESSAGE  
 
## CLIPSTRINGS
 
DRIVER('SQLDriver', '/CLIPSTRINGS = TRUE | FALSE ' ) 
[ Clipped" = ] SEND(file, '/CLIPSTRINGS [ = TRUE | FALSE ]' ) 
 
(NOTE: Not valid for ORACLE Accelerator) 
By default (CLIPSTRINGS=TRUE), the SQL driver CLIPs strings before sending them to the 
backend server (see CLIP in the Language Reference). To send the full (unclipped) string, set 
## CLIPSTRINGS=FALSE.
 
## FASTCOLUMNFETCH
 
DRIVER('SQLDriver', '/FASTCOLUMNFETCH = TRUE | FALSE ' ) 
[ Fetch" = ] SEND(file, '/FASTCOLUMNFETCH [ = TRUE | FALSE ]' ) 
 
(NOTE: Not valid for ORACLE Accelerator) 
By default, the SQL driver will attempt to use the extended fetch abilities of a back end to retrieve 
column information.  Some back ends support extended fetch, but not when fetching column 
information.  To stop these back ends from crashing or returning invalid errors when opening a 
file,  you can set  /FASTCOLUMNFETCH=FALSE . 
 


---

Database Drivers and Interfaces 
183 
## FORCEUPPERCASE
 
DRIVER('SQLDriver', '/FORCEUPPERCASE = TRUE | FALSE ' ) 
[ Uppered" = ] SEND(file, '/FORCEUPPERCASE [ = TRUE | FALSE ]' ) 
 
(NOTE: Valid only for the SQLAnywhere driver) 
By default (FORCEUPPERCASE=FALSE), the SQL Driver passes the table name in mixed case 
to the SQLColumns function to verify the existence of the table. However, some backends require 
the table name to be passed in  uppercase. To pass the table name in uppercase, set 
FORCEUPPERCASE=TRUE. See also VERIFYVIASELECT. 
 
## GATHERATOPEN
 
DRIVER('SQLDriver', '/GATHERATOPEN = TRUE | FALSE ' ) 
 
(NOTE: Not valid for ORACLE Accelerator) 
By default the driver delays gathering field information until it is required. However, some 
backends (like Sybase 11) perform poorly under these conditions. Setting GATHERATOPEN to 
TRUE forces the driver to gather most of the field information when the file is opened, whihc 
avoids a slowdown during program execution.  
 


---

Database Drivers 
184 
## GETINFO
 
Result = filelabel{PROP:GETINFO, property} 
 
(NOTE: Not valid for ORACLE Accelerator) 
Use this property to retrieve information about a connection to any ODBC (or SQL) data source. 
This property is basically a wrapper to the SQLGetInfo ODBC API. The data returned is 
dependent of the "request" and can be returned in a string form or a long. When it is a LONG, the 
value needs to be "interpreted" using a bitmask. 
 
The full list of available ODBC properties can be found in ODBCATTR.INC: 
 
## SQL_ACTIVE_CONNECTIONS             EQUATE(0)
## SQL_ACTIVE_STATEMENTS              EQUATE(1)
## SQL_DATA_SOURCE_NAME               EQUATE(2)
## SQL_DRIVER_HDBC                    EQUATE(3)
## SQL_DRIVER_HENV                    EQUATE(4)
## SQL_DRIVER_HSTMT                   EQUATE(5)
## SQL_DRIVER_NAME                    EQUATE(6)
## SQL_DRIVER_VER                     EQUATE(7)
## SQL_FETCH_DIRECTION                EQUATE(8)
## SQL_ODBC_API_CONFORMANCE           EQUATE(9)
## SQL_ODBC_VER                       EQUATE(10)
## SQL_ROW_UPDATES                    EQUATE(11)
## SQL_ODBC_SAG_CLI_CONFORMANCE       EQUATE(12)
## SQL_SERVER_NAME                    EQUATE(13)
## SQL_SEARCH_PATTERN_ESCAPE          EQUATE(14)
## SQL_ODBC_SQL_CONFORMANCE           EQUATE(15)
 
## SQL_DBMS_NAME                      EQUATE(17)
## SQL_DBMS_VER                       EQUATE(18)
## SQL_ACCESSIBLE_TABLES              EQUATE(19)
## SQL_ACCESSIBLE_PROCEDURES          EQUATE(20)
## SQL_PROCEDURES                     EQUATE(21)
## SQL_CONCAT_NULL_BEHAVIOR           EQUATE(22)
## SQL_CURSOR_COMMIT_BEHAVIOR         EQUATE(23)
## SQL_CURSOR_ROLLBACK_BEHAVIOR       EQUATE(24)
## SQL_DATA_SOURCE_READ_ONLY          EQUATE(25)
## SQL_DEFAULT_TXN_ISOLATION          EQUATE(26)
## SQL_EXPRESSIONS_IN_ORDERBY         EQUATE(27)


---

Database Drivers and Interfaces 
185 
## SQL_IDENTIFIER_CASE                EQUATE(28)
## SQL_IDENTIFIER_QUOTE_CHAR          EQUATE(29)
## SQL_MAX_COLUMN_NAME_LEN            EQUATE(30)
## SQL_MAX_CURSOR_NAME_LEN            EQUATE(31)
## SQL_MAX_OWNER_NAME_LEN             EQUATE(32)
## SQL_MAX_PROCEDURE_NAME_LEN         EQUATE(33)
## SQL_MAX_QUALIFIER_NAME_LEN         EQUATE(34)
## SQL_MAX_TABLE_NAME_LEN             EQUATE(35)
## SQL_MULT_RESULT_SETS               EQUATE(36)
## SQL_MULTIPLE_ACTIVE_TXN            EQUATE(37)
## SQL_OUTER_JOINS                    EQUATE(38)
## SQL_OWNER_TERM                     EQUATE(39)
## SQL_PROCEDURE_TERM                 EQUATE(40)
## SQL_QUALIFIER_NAME_SEPARATOR       EQUATE(41)
## SQL_QUALIFIER_TERM                 EQUATE(42)
## SQL_SCROLL_CONCURRENCY             EQUATE(43)
## SQL_SCROLL_OPTIONS                 EQUATE(44)
## SQL_TABLE_TERM                     EQUATE(45)
## SQL_TXN_CAPABLE                    EQUATE(46)
## SQL_USER_NAME                      EQUATE(47)
## SQL_CONVERT_FUNCTIONS              EQUATE(48)
## SQL_NUMERIC_FUNCTIONS              EQUATE(49)
## SQL_STRING_FUNCTIONS               EQUATE(50)
## SQL_SYSTEM_FUNCTIONS               EQUATE(51)
## SQL_TIMEDATE_FUNCTIONS             EQUATE(52)
## SQL_CONVERT_BIGINT                 EQUATE(53)
## SQL_CONVERT_BINARY                 EQUATE(54)
## SQL_CONVERT_BIT                    EQUATE(55)
## SQL_CONVERT_CHAR                   EQUATE(56)
## SQL_CONVERT_DATE                   EQUATE(57)
## SQL_CONVERT_DECIMAL                EQUATE(58)
## SQL_CONVERT_DOUBLE                 EQUATE(59)
## SQL_CONVERT_FLOAT                  EQUATE(60)
## SQL_CONVERT_INTEGER                EQUATE(61)
## SQL_CONVERT_LONGVARCHAR            EQUATE(62)
## SQL_CONVERT_NUMERIC                EQUATE(63)
## SQL_CONVERT_REAL                   EQUATE(64)
## SQL_CONVERT_SMALLINT               EQUATE(65)
## SQL_CONVERT_TIME                   EQUATE(66)
## SQL_CONVERT_TIMESTAMP              EQUATE(67)


---

Database Drivers 
186 
## SQL_CONVERT_TINYINT                EQUATE(68)
## SQL_CONVERT_VARBINARY              EQUATE(69)
## SQL_CONVERT_VARCHAR                EQUATE(70)
## SQL_CONVERT_LONGVARBINARY          EQUATE(71)
## SQL_TXN_ISOLATION_OPTION           EQUATE(72)
## SQL_ODBC_SQL_OPT_IEF               EQUATE(73)
 
! ODBC SDK 1.0 Additions 
## SQL_CORRELATION_NAME               EQUATE(74)
## SQL_NON_NULLABLE_COLUMNS           EQUATE(75)
 
! ODBC SDK 2.0 Additions 
## SQL_DRIVER_HLIB                    EQUATE(76)
## SQL_DRIVER_ODBC_VER                EQUATE(77)
## SQL_LOCK_TYPES                     EQUATE(78)
## SQL_POS_OPERATIONS                 EQUATE(79)
## SQL_POSITIONED_STATEMENTS          EQUATE(80)
## SQL_GETDATA_EXTENSIONS             EQUATE(81)
## SQL_BOOKMARK_PERSISTENCE           EQUATE(82)
## SQL_STATIC_SENSITIVITY             EQUATE(83)
## SQL_FILE_USAGE                     EQUATE(84)
## SQL_NULL_COLLATION                 EQUATE(85)
## SQL_ALTER_TABLE                    EQUATE(86)
## SQL_COLUMN_ALIAS                   EQUATE(87)
## SQL_GROUP_BY                       EQUATE(88)
## SQL_KEYWORDS                       EQUATE(89)
## SQL_ORDER_BY_COLUMNS_IN_SELECT     EQUATE(90)
## SQL_OWNER_USAGE                    EQUATE(91)
## SQL_QUALIFIER_USAGE                EQUATE(92)
## SQL_QUOTED_IDENTIFIER_CASE         EQUATE(93)
## SQL_SPECIAL_CHARACTERS             EQUATE(94)
## SQL_SUBQUERIES                     EQUATE(95)
## SQL_UNION                          EQUATE(96)
## SQL_MAX_COLUMNS_IN_GROUP_BY        EQUATE(97)
## SQL_MAX_COLUMNS_IN_INDEX           EQUATE(98)
## SQL_MAX_COLUMNS_IN_ORDER_BY        EQUATE(99)
## SQL_MAX_COLUMNS_IN_SELECT          EQUATE(100)
## SQL_MAX_COLUMNS_IN_TABLE           EQUATE(101)
## SQL_MAX_INDEX_SIZE                 EQUATE(102)
## SQL_MAX_ROW_SIZE_INCLUDES_LONG     EQUATE(103)


---

Database Drivers and Interfaces 
187 
## SQL_MAX_ROW_SIZE                   EQUATE(104)
## SQL_MAX_STATEMENT_LEN              EQUATE(105)
## SQL_MAX_TABLES_IN_SELECT           EQUATE(106)
## SQL_MAX_USER_NAME_LEN              EQUATE(107)
## SQL_MAX_CHAR_LITERAL_LEN           EQUATE(108)
## SQL_TIMEDATE_ADD_INTERVALS         EQUATE(109)
## SQL_TIMEDATE_DIFF_INTERVALS        EQUATE(110)
## SQL_NEED_LONG_DATA_LEN             EQUATE(111)
## SQL_MAX_BINARY_LITERAL_LEN         EQUATE(112)
## SQL_LIKE_ESCAPE_CLAUSE             EQUATE(113)
## SQL_QUALIFIER_LOCATION             EQUATE(114)
 
 
## IGNORETRUNCATION
 
DRIVER('SQLDriver', '/IGNORETRUNCATION = TRUE | FALSE ' ) 
filelabel{PROP:IGNORETRUNCATION} = TRUE | FALSE 
 
 
(NOTE: Not valid for ORACLE Accelerator) 
You can declare your string data to be a different size in Clarion than on the server.  For 
example, you can define a CHAR(10000) as CSTRING(50) if all you are interested in is the 
first 50 characters of the data.  However, doing this will generate an ODBC warning about 
string truncation. 
By default, Clarion treats this as a normal error.  If you want to ignore this warning, you can set 
\IGNORETRUNCATION=TRUE, or alternatively, use filelabel{PROP:IgnoreTruncation} = 1. 


---

Database Drivers 
188 
## ISOLATIONLEVEL
 
DRIVER('SQLDriver', '/ISOLATIONLEVEL = number' ) 
number = SEND(file,'/ISOLATIONLEVEL = number') 
file{PROP:IsolationLevel} = number 
number = file{PROP:IsolationLevel} 
 
(NOTE: Not valid for ORACLE Accelerator) 
The following terms are used to define transaction isolation levels: 
Dirty Read 
Transaction 1 changes a row. Transaction 2 reads the changed row 
before transaction 1 commits the change.  If transaction 1 rolls back the 
change, transaction 2 will have read a row that is considered to have 
never existed. 
Nonrepeatable Read 
Transaction 1 reads a row. Transaction 2 updates or deletes that row 
and commits this change.  If transaction 1 attempts to reread the row, it 
will receive different row values or discover that the row has been 
deleted. 
Phantom 
Transaction 1 reads a set of rows that satisfy some search criteria. 
Transaction 2 inserts a row that matches the search criteria. If 
transaction 1 reexecutes the statement that read the rows, it receives a 
different set of rows. 
The number parameter must be one of the following values: 
1 
Dirty reads, nonrepeatable reads, and phantoms are possible. 
2 
Dirty reads are not possible. Nonrepeatable reads and phantoms are 
possible. 
4 
Dirty reads and nonrepeatable reads are not possible. Phantoms are 
possible. 
8 
Transactions are serializable. Dirty reads, nonrepeatable reads, and 
phantoms are not possible. 
16 
Transactions are serializable, but higher concurrency is possible than with 
8. Dirty reads are not possible.  
Typically, 8 is implemented by using locking protocols that reduce  concurrency and 16 is 
implemented by using a non-locking protocol such as record versioning. Oracle's Read 
Consistency isolation level is an example of 16. 
By default, the ODBC driver sets the transaction isolation level to what is set in the data source.  
The other SQL based drivers set it to 1. 
The return number is the current value of the isolation level.  A zero return indicates the file is not 
connected to a database. 
IsolationLevel uses the ODBC isolation level standard. This may not be the same as the isolation 
levels documented on the target driver’s native back end.  For example, with Sybase's ASA, the 
documented isolation levels are 0, 1, 2 and 3 and they correspond to  
 
 


---

Database Drivers and Interfaces 
189 
ODBC level 
Sybase Level 
1 
0 
2 
1 
4 
2 
8 
3 
16 
N/A 
 
FAQs: 
Does PROP:LOGOUTISOLATION work only on the FILE LEVEL or is it on the Database level? 
How does PROP:LOGOUTISOLATION deal with multiple tables on a transaction frame, when 
one isolation level is different from another? 
Isolation levels work at a connection level.  So they apply to all files opened using the same 
OWNER attribute. 
 
How can you remove the ODBC cursor after a LOGOUT no matter what isolation level you 
choose (i.e., GET(file,0)) - does this remove a cursor? 
The ODBC cursor is maintained throughout the life of the file (e.g., until PROP:Disconnect or the 
end of a thread for threaded files.) 
 


---

Database Drivers 
190 
## JOINTYPE
 
DRIVER('SQLDriver', '/JOINTYPE = Watcom | DB2 | Microsoft | FirstSQL | Inner | Partial | 
None' ) 
[ Join" = ] SEND(file, '/JOINTYPE [ = Watcom | DB2 | Microsoft | FirstSQL | Inner | Partial | 
None ]' ) 
 
(NOTE: Not valid for ORACLE Accelerator) 
The SQL standard does not support joins to more than one child (or parent). Most vendors 
consider this limitation unacceptable and have extended the standard. However, they have done 
so in different ways. The SQL driver attempts to determine the join type used by the backend, but 
if it does not get it right, then you should use the JOINTYPE driver string in the primary file of the 
view. Note that specifying Inner is normally slower than Watcom, DB2, Microsoft, Partial or 
FirstSQL. Specifying None is slower than Inner, but will work with all backends because the join is 
done on the client. 
When using ODBC, the ODBC 3.0 standard does support multiple joins, so ODBC 3.0 compliant 
drivers should not require this switch. 
## JOINTYPE=DB2
This is the join syntax used by IBM's DB2.  This generates ANSI compliant outer joins.  The Base 
Normal Form for the relevant DB2 specification is: 
from-clause ::= 
  FROM <table-ref> 
 
table-ref::=  
    <single-table> | 
    <joined-table> 
 
single-table ::= 
table-name AS correlation-name 
 
joined-table ::= 
   <table-ref> LEFT OUTER JOIN <single-table> ON join-condition 
 
## JOINTYPE=MICROSOFT
This is the join syntax specified by the ODBC 2.0 spec.  The Base Normal Form for the relevant 
ODBC spec is: 
from-clause ::= 
    FROM <table-ref> | 
    FROM <odbc-joined-table> 
 
table-ref ::= 
    <single-table> | 
    <joined-table> 
 
single-table ::= 
    table-name AS correlation-name 
 
odbc-joined-table ::= 
    {oj <joined-table> } 
 
joined-table ::= 


---

Database Drivers and Interfaces 
191 
    <single-table> LEFT OUTER JOIN <table-ref> ON join-condition 
 
## JOINTYPE=WATCOM
This is the join syntax used by SQL Anywhere and is a merger of the ODBC and ANSI 
specifications.  The Base Normal Form for this syntax is: 
from-clause ::= 
    FROM <table-ref> | 
    FROM <odbc-joined-table> 
 
table-ref ::= 
    <single-table> | 
    <joined-table> 
 
single-table ::= 
    table-name AS correlation-name 
 
odbc-joined-table ::= 
    {oj <joined-table> } 
 
joined-table ::= 
    <table-ref> LEFT OUTER JOIN <single-table> ON join-condition 
 
## JOINTYPE=FIRSTSQL
This is the join syntax used by FirstSQL and is not recommended to be used with any other file 
format. 
## JOINTYPE=PARTIAL
This format supports nested outer joins with the limitation that the column names in the ON 
clause of the outer join must be in the same order as their respective table names in the OUTER 
JOIN clause. 
The Base Normal Form for this format is: 
from-clause ::= 
    FROM <single-table> | 
    FROM <odbc-joined-table> 
 
single-table ::= 
    table-name AS correlation-name 
 
odbc-joined-table ::= 
    {oj <joined-table> } 
 
joined-table ::= 
    <single-table> LEFT OUTER JOIN <table-ref> ON join-condition | 
    (<joined-table>) LEFT OUTER JOIN <table-ref> ON join-condition | 
 
table-ref ::= 
    <single-table> | 
    <joined-table> 
 
## JOINTYPE=INNER
This is a format that should work with any database, but is likely to be very slow. 
## JOINTYPE=NONE


---

Database Drivers 
192 
This indicates to perform the join on the client. 
 


---

Database Drivers and Interfaces 
193 
## MULTIPLEACTIVERESULTSETS
 
DRIVER('SQLDriver', '/MULTIPLEACTIVERESULTSETS = TRUE | FALSE ' ) 
[ Mars" = ] SEND(file, '/ MULTIPLEACTIVERESULTSETS [ = TRUE | FALSE ]' ) 
 
  
(NOTE: Only valid for ODBC and MSSQL Accelerators) 
 
The ODBC and MSSQL drivers default to FALSE (using MARS (Multiple Active Result Sets)) 
whenever MS-SQL Server 2005 is detected. MARS is defined as the ability to have more than 
one pending request under a given SQL Server connection. For most cases this will directly 
translate to the ability to have more than one default result set outstanding while other operations 
can execute within the same session. 
 
If you need to enable the MARS support, set this driver string to TRUE. It can be turned on by 
accessing the driver string dialog, or by using a SEND statement prior to the table being opened. 
This is a connection-wide switch, which means that all files with the same OWNER will have the 
same MARS support based on the first file that is opened on that connection. 
 
If all tables are closed and a PROP:Disconnect is issued successfully, you will need to SEND the 
/MULTIPLEACTIVERESULTSETS = TRUE again before the first table is opened. 
 
When MARS is set to ON, the BusyHandling switch is still active, but should not be needed.  
The driver's default behavior is to retry whenever the busy message is encountered, but a busy 
message should never happen with MULTIPLEACTIVERESULTSETS on (or active). 
 
Setting this switch ON to backends that do not support MARS have no adverse effect. The driver 
will detect if the backend does not support MARS and ignore the switch in this case. 
 
See Also: BUSYHANDLING  
 
## NESTING
 
DRIVER('SQLDriver', '/NESTING = TRUE | FALSE ' ) 
[ Nest" = ] SEND(file, '/NESTING [ = TRUE | FALSE ]' ) 
 
(NOTE: Not valid for ORACLE Accelerator) 
Some SQL drivers do not support parent->child->grandchild style views. The SQL driver attempts 
to determine if this is supported. If the driver does not get it right and the backend does not 
support these type of views, then you need to set NESTING=FALSE.  This causes the join to be 
done on the client. 


---

Database Drivers 
194 
## ODBCCALL
 
DRIVER('SQL Driver', '/ODBCCALL = TRUE | FALSE ' ) 
[ Call" = ] SEND(file, '/ODBCCALL [ = TRUE | FALSE ]' ) 
 
By default (ODBCCALL = True) the SQL Accelerator reformats your CALL statements to match 
the ODBC standard call syntax. To disable this automatic reformatting, set ODBCCALL=FALSE. 
 
## ORDERINSELECT
 
DRIVER('SQLDriver', '/ORDERINSELECT= TRUE | FALSE' ) 
[ OIS" = ] SEND(file, '/ORDERINSELECT [ = TRUE | FALSE ]' ) 
 
(NOTE: Not valid with the Oracle Accelerator) 
Some backends require that any fields used in the ORDER BY clause also appear in the 
SELECT statement. By setting this property to true the driver will make sure this rule is applied for 
all views regardless of the fields projected.  You can also read PROP:OrderInSelect to get its 
current value 
 
 
## PREAUTOINC
 
DRIVER('SQLDriver', '/PREAUTOINC = [TRUE/FALSE] ' ) 
[ Buffer" = ] SEND(file, 'PREAUTOINC [ = TRUE/FALSE ]' ) 
 
 
The /PREAUTOINC driver string is used to inform the target table as to when a server side auto-
incrementing field is incremented in regards to the SQL SELECT statement when an Insert action 
is active. When the string is set to TRUE, (except Oracle), the SQL code is issued after the 
SELECT,.  For Oracle, it is issued before the SELECT (when set to TRUE). TRUE is the driver’s 
strings default setting (e.g., if it omitted, it is implicitly TRUE). 
 
The Dictionary Editor contains a Driver String Options dialog in the Table Properties to allow easy 
entry of this string. 
See Also:     Server side auto-incrementing values  
 


---

Database Drivers and Interfaces 
195 
## TURBOSQL
 
DRIVER('SQLDriver', '/TURBOSQL = TRUE | FALSE ' ) 
[ Nest" = ] SEND(file, '/TURBOSQL [ = TRUE | FALSE ]' ) 
 
(NOTE: Not valid for the ORACLE Accelerator) 
The SQL drivers (except Oracle) now support the driver string /TURBOSQL.  If this is set to 
TRUE, the driver will not verify that all of the columns of the target table exist on the server at 
OPEN.  This may increase performance with some applications, but has the disadvantage that 
the program may crash if an expected column is deleted from the table on the server. 
When using the /TURBOSQL switch,  error checking should still be implemented.  For example, 
you will still get an error if you fail to connect to the server. 
 
You can use this switch to simply define a buffer on the application side that will receive a 
prop:sql resultset without the need to define a view with valid column name and data type. 
 
Example: 
 
MyResult  FILE, DRIVER('MSSQL', '/TURBOSQL=TRUE') 
Record     RECORD 
Col1        STRING(20) 
Col2        STRING(20) 
Col3        LONG 
           END 
          END 
 
 
## CODE
 OPEN(MyResult) 
 MyResult{prop:SQL} = | 
'SELECT products.ProductID,products.ProductName,products.Qty from PRODUCTS' 
 
The driver will match the resultset with the application buffer (MyResult) using the ordinal order 
for the matching field.  
 
Using the above code, the driver will assume that the resultant columns are text fields.  If you 
want to return binary data in the fields you will need to define your column like this: 
 
Col1  STRING(20),NAME('col4 | BINARY') 
 


---

Database Drivers 
196 
  
The TURBOSQL switch disables data collection done by the driver the first time a table is 
opened. This is fine if the table is ONLY used for receiving the results of PROP:SQL calls. 
However, if ANY normal Clarion I/O is done (via either views or standard Clarion File I/O calls), 
this switch should not be used. If the switch is used in combination with standard Clarion I/O calls, 
then the driver will have insufficient information to return properly converted data (i.e., CAST 
specifications) resulting in scrambled (corrupted) data and possible GPFs. 
 
 
## USEINNERJOIN
 
DRIVER('SQLDriver', '/USEINNERJOIN= TRUE | FALSE' ) 
[ Join" = ] SEND(file, '/USEINNERJOIN [ = TRUE | FALSE ]' ) 
 
By default (USEINNERJOIN = True) the SQL Accelerator generates the following ANSI SQL for 
inner joins: 
 SELECT ... FROM table1 INNER JOIN table2 ON table1.field=table2.field 
However, not all backends support ANSI SQL. The driver provides an alternative syntax for inner 
joins. To generate the following alternative syntax, set USEINNERJOIN=FALSE: 
 SELECT ... FROM table1, table2 WHERE table1.field=table2.field 
 
## UNICODE
 
DRIVER('SQLDriver', '/UNICODE= TRUE | FALSE' ) 
[ Join" = ] SEND(file, '/UNICODE[ = TRUE | FALSE ]' ) 
 
By default (UNICODE = False) all STRING fields are considered to contain ANSI characters.  The 
CREATE statement will attempt to create char fields, or the equivalent for the SQL backend.  All 
data retrieval and storage functions will inform the database server that the data being passed 
contains standard ANSI characters. 
If UNICODE=TRUE, then all STRING fields are considered to contain UTF-16 characters.  The 
CREATE statement will create an nchar (or equivalent) row with size equal to the field’s size 
divided by 2.  Eg STRING(20) will create an nchar(10).  All data retrieveal and storage functions 
will inform the database server that the data being passed contains UTF-16 characters. 
To enable UNICODE support for a single field, use the “| UNICODE” NAME modifier for the field. 
 
  
Clarion pads all STRING fields with spaces.  It is the responsibility of the programmer to make 
sure that any STRING field that the driver treats as UNICODE is padded with UNICODE spaces 
(U+0020).  Due to Windows use of little-endian, a UNICODE space is <020H><00H>.  If you do 
not pad your string with UNICODE spaces, the server will interpret the end of your string as being 
padded with the UNICODE character U+2020(†). 


---

Database Drivers and Interfaces 
197 
 
## VERIFYVIASELECT
 
DRIVER('SQL Driver', '/VERIFYVIASELECT = TRUE | FALSE' ) 
[ Verify" = ] SEND(file, '/VERIFYVIASELECT [ = TRUE | FALSE ]' ) 
 
VERIFYVIASELECT lets the SQL Driver use an alternative, sometimes faster, method to validate 
fields when opening a table. By default (VERIFYVIASELECT=FALSE), the SQL Driver uses the 
SQLColumns function to validate fields. However, some backends (particularly SQL Anywhere) 
can validate fields faster using a SELECT statement. To verify fields using the SELECT 
statement, set VERIFYVIASELECT to TRUE. 
VERIFYVIASELECT defaults to TRUE for SQL Anywhere backends. 
 


---

Database Drivers 
198 
WHERE (SQL Driver String) 
 
[ Where" = ] SEND (file, '/WHERE [ where-clause ]' ) 
 
The SQL Accelerator drivers automatically build SQL WHERE clauses when your Clarion code 
contains a SET followed by a NEXT or PREVIOUS. You can customize the driver generated 
WHERE clause by using the WHERE driver string. You can also set the WHERE driver string at 
runtime with the use of PROP:WHERE. PROP:WHERE is a write-only property. 
The SEND must be executed after the SET statement and before the NEXT or PREVIOUS 
statement.  
  
The SET statement clears any WHERE clause set by the SEND statement. 
Because the SQL driver's generated SELECT statement is not compiled until the NEXT or 
PREVIOUS statement, the SEND function posts no error code and returns no result. For 
example: 
Orders  FILE,PRE(Ord),DRIVER('ODBC'),NAME('Ord') 
NameDate KEY(+Ord:NameId,-Ord:Date) 
Record   RECORD 
Name      STRING(12),NAME('NameId') 
Date      DATE,NAME('OrderDate') 
Type      STRING(1),NAME('OrderType') 
Details   STRING(20),NAME('OrderDetails') 
         END 
        END 
## CODE
 Ord:Name = 'SMITH' 
 SET(Ord:NameDate,Ord:NameDate) 
 SEND(Orders, '/WHERE OrderType = "M"')  
## LOOP
    NEXT(Orders) 
    !...some processing 
 END 
This generates a SELECT statement similar to: 
SELECT NameId,OrderDate,OrderType,OrderDetails FROM Orders 
  WHERE (NameID >= 'SMITH') AND (OrderType = 'M') 
 


---

Database Drivers and Interfaces 
199 
## ZERODATE
 
DRIVER('SQLDriver', '/ZERODATE = NULL | 0  | 1 | yyyymmdd' ) 
[ Nulls" = ] SEND(file, '/ZERODATE [ = NULL | 0  | 1 | yyyymmdd' ' ) 
 
 
(Not valid for the Oracle driver)  
 
ZERODATE defines how the target driver should generate a WHERE clause for cleared DATE  
and TIME fields and replaces the /ZEROISNULL driver string. 
ZERODATE=NULL is equivalent to ZEROISNULL=TRUE and is the default behavior.   
ZERODATE=0 is equivalent to ZEROISNULL=FALSE. 
ZERODATE=1 indicates that a cleared date will be generated as 01/01/0001 and a cleared time 
is generated as 0. 
ZERODATE=yyyymmdd indicates that a cleared date will be generated as mm/dd/yyyy and a 
cleared time is generated as 0. 
If both ZERODATE and ZEROISNULL are specified in the driver string, the last one will be used. 
If you use the driver string editor in the dictionary editor, it will automatically convert 
ZEROISNULL to the equivalent ZERODATE. 
 
  
This driver string is meant for how the field is updated and how it is retrieved.  When you do a 
SET(key,key) on a key with a date component that has been cleared, the driver uses this setting 
to generate the SELECT .. WHERE clause. 
 
For example:   
 
Setting ZERODATE=NULL generates: 
SELECT * WHERE datefield NOT NULL  
 
Setting ZERODATE=0 generates: 
SELECT * WHERE datefield > 0  
 
Setting ZERODATE=1 generates: 
SELECT * WHERE datefield > 01/01/0001 
 
This feature is not supported for Oracle drivers.  
 


---

Database Drivers 
200 
## ZEROISNULL
 
DRIVER(''SQLDriver'', '/ZEROISNULL = TRUE | FALSE' ) 
[ Nulls" = ] SEND(file, '/ZEROISNULL [ = TRUE | FALSE ]' ) 
 
(NOTE: Not valid for ORACLE Accelerator) 
ZEROISNULL lets the SQL Accelerator Drivers set DATE and TIME fields to zero (0) rather than 
null. By default (ZEROISNULL=TRUE), the SQL Accelerator Drivers assumes a DATE or TIME 
field with a value of zero (0) should be a null value in the backend database, and adjusts the 
values to NULL when writing to the backend. To allow the driver to set DATE and TIME fields to 
zero rather than null, set ZEROISNULL to FALSE. 
See Also: ZERODATE  
 


---

Database Drivers and Interfaces 
201 


---

Database Drivers 
202 
SQL Driver Properties 
You can use Clarion's property syntax to query and set certain SQL Accelerator driver properties. 
These properties are described below. 
## PROP:ALIAS
PROP:AlwaysRebind  
PROP:ConnectString  
PROP:DBMSver  
PROP:Details  
PROP:Disconnect  
PROP:hdbc  
PROP:henv  
PROP:hstmt  
PROP:Inner  
PROP:LogonScreen  
PROP:Log  
PROP:LogFile  
PROP:LoginTimeout  
PROP:LogSQL  
PROP:OrderAllTables  
PROP:OrderInSelect  
PROP:Profile  
PROP:QuoteString  
## PROP:SQL
PROP:SQLFilter  
PROP:SQL_Join  
PROP:SQLOrder  


---

Database Drivers and Interfaces 
203 
PROP:Alias 
PROP:Alias is a read/write file property that sets or returns the alias the SQL Accelerator driver 
uses when generating SELECT statements for a view. It will return an empty string if PROP:Alias 
has not previously been called to set the alias. PROP:Alias only returns a value previously set 
using PROP:Alias. For example: 
Customer{PROP:Alias} = 'C'                !set new table alias 
OldAlias" = Customer{PROP:Alias} = ''     !use default alias 
 
If you have not used PROP:Alias to set the alias of a file, the SQL driver generates an SQL 
statement which uses an Alias of "A" for the first file in the View, "B" for the second etc.  If you 
wish to use the SQL() directive in Prop:Filter, your filter has to be compatible with the previously 
generated SQL statement – e.g., you need use A/B/etc. as the file prefixes. 
Setting a file's property will set it for as long as that file is in scope.  For non-threaded files this 
means for the duration of the program.  For threaded files it means for the duration of the thread. 
You can use file{PROP:Alias} to specify what alias the driver should use when constructing 
SELECT statements for views. 
If the file has the THREAD attribute, then it refers to the current thread.  If it does not, then it is 
global. 
See Also:     PROP:SQL  
 
PROP:AlwaysRebind 
PROP:AlwaysRebind sets or returns the toggle that controls whether the SQL  Accelerator 
rebinds memory locations when a NULL state changes. 
For all backends except MSSQL, PROP:AlwaysRebind defaults to 0 or False, so the SQL driver 
does not rebind memory locations when a NULL state changes. However, some SQL backends 
(including MSSQL) do not recheck the null state, so they must have the memory location rebound 
to force the change of null state. Setting PROP:AlwaysRebind to 1 or True tells the SQL 
Accelerator to do this extra binding. 
 
PROP:ConnectString 
PROP:ConnectString returns an SQL database's connection information. For example: 
AFileOwner STRING(256) 
AFile      FILE,DRIVER('ODBC'),OWNER(AFileOwner) 
 
## CODE
 AFileOwner='DataSource' 
 OPEN(Afile) 
## IF NOT ERRORCODE()
   AFileOwner=AFile{PROP:ConnectString} 
  END 
 


---

Database Drivers 
204 
PROP:DBMSver 
Good for all SQL Drivers except Oracle. 
File{PROP:DBMSver} returns a character string indicating the version of the DBMS accessed by 
the driver. The version is of the form ##.##.####, where the first two digits are the major version, 
the next two digits are the minor version, and the last four digits are the release version.  
 
PROP:Details 
See the Details switch described in the Debugging Your SQL Application section. 
Details=1 tells the driver to include record buffer contents in the log file; however, if the file is 
encrypted, you must turn on both the Details switch and the ALLOWDETAILS switch to log record 
buffer contents (see ALLOWDETAILS). Details=0 tells the driver to omit record buffer contents. 
The Profile switch must be turned on for the Details switch to have any effect. 
 
PROP:Disconnect 
PROP:Disconnect CLOSEs any open files in the target file's database, then disconnects the 
application from the database. 
Example: 
 
FileLabel{PROP:Disconnect} !No equal sign needed 
 
PROP:DriverTracing 
 
If this property is set to '', then all driver tracing for all file drivers is disabled.  No INI file or 
registry entry will be read.  However file specific settings set via SEND commands or file 
property settings will still take effect. 
 
Example: 
SYSTEM{PROP:DriverTracing} = ''   !disable all driver tracing 
SYSTEM{PROP:DriverTracing} = '1'  !enable all driver tracing 
 


---

Database Drivers and Interfaces 
205 
PROP:GroupBy, PROP:Having 
The SQL view engine supports PROP:GroupBy and PROP:Having.  These properties allow you 
to add respectively GROUP BY and HAVING clauses to your SELECT statement.  Note that 
PROP:GroupBy must be set first to allow PROP:Having to be generated. 
 
Example: 
 
## PROGRAM
 
  MAP 
  END 
 
## EMP       FILE,DRIVER('ORACLE'),NAME('EMP'),PRE(EMP)
## P_EKY_EMP  KEY(EMP:EMPNO),NOCASE,OPT,PRIMARY
## KEY_DEP    KEY(EMP:DEPTNO),DUP,NOCASE,OPT
Record     RECORD 
EMPNO       SHORT         !Emp-no 
ENAME       CSTRING(11)   !Employee name 
JOB         CSTRING(10)   !Job 
HIREDATE    DATE          !Hiredate 
MGR         SHORT         !Manager 
SAL         PDECIMAL(7,2) !Salary 
COMM        PDECIMAL(7,2) !Commisison 
## DEPTNO      BYTE
           END 
          END 
 
MyView VIEW(EMP) 
    PROJECT(EMP:Mgr) 
    PROJECT(EMP:Sal) 
       END 
 
## CODE
## OPEN(EMP)
   OPEN(MyView) 
   MyView{'EMP:Sal',PROP:Name} = 'sum(sal)' 
   MyView{PROP:GroupBy} = 'Mgr' 
   MyView{PROP:Having} = 'sum(sal) > 100000' 
   SET(MyView) 
   NEXT(MyView) 
 
The example code above is the equivalent to "SELECT mgr, sum(sal) FROM EMP GROUP BY 
mgr HAVING sum(sal) > 100000" 
 
In other words, this code will return a list of all Manager IDs and the total salary of their 
subordinates if their subordinates make a total of more than 100000. 


---

Database Drivers 
206 
PROP:hdbc 
 
(NOTE: Not valid for ORACLE Accelerator) 
PROP:hdbc returns the current hdbc used by the SQL driver. Thus ?MyFile{PROP:hdbc} may be 
used for ODBC API calls requiring hdbc.  
 
PROP:henv 
 
(NOTE: Not valid for ORACLE Accelerator) 
PROP:henv returns the current henv (environment handle) used by the SQL driver. Thus 
?MyFile{PROP:henv} may be used for ODBC API calls requiring henv. For example, for the 
SQLDataSources function: 
rc# = SQLDataSources(Myfile{PROP:henv},SQL_FETCH_NEXT,ODBC:driver, | 
                     drvLen,drvlen,ODBC:Description,desclen,desclen) 
 
PROP:Hint  
The HINT driver string is valid for Oracle and MS-SQL drivers.. 
 
PROP:hstmt 
 
(NOTE: Not valid for ORACLE Accelerator) 
PROP:hstmt returns the current hstmt used by the SQL driver. Thus ?MyFile{PROP:hstmt} may 
be used for ODBC API calls requiring hstmt. For example, the SQLDescribeCol function:  
Myfile{PROP:SQL} = 'Select * from ATable' 
rc# = SQLDescribeCol(Myfile{PROP:hstmt},Num,Name,Max,NameL, | 
                     Type,Def,Scale,Null) 
 
PROP:Inner 
 
PROP:Inner is a writable property for SQL Accelerator drivers. This is useful for testing the ODBC 
USEINNERJOIN driver string. See PROP:Inner in the Language Reference for more information. 
PROP:INNER is read-only for non-SQL views and read/write for SQL based views. 
 
PROP:IsolationLevel 
 
PROP:IsolationLevel is used to define transaction isolation levels. See ISOLATIONLEVEL  
 


---

Database Drivers and Interfaces 
207 
PROP:LogonScreen 
PROP:LogonScreen sets or returns the value that determines whether the driver automatically 
prompts for logon information. By default, PROP:LogonScreen=TRUE, and the driver displays a 
logon window if no connect string is supplied. If set to FALSE, and there is no connect string, the 
OPEN(file) fails and FILEERRORCODE() returns a driver specific error code.  For example: 
AFile FILE,DRIVER('SQLAnywhere') 
!file declaration with no userid and password 
      END 
## CODE
 AFile{PROP:LogonScreen}=True   !enable auto login screen 
 OPEN(Afile) 
 
In the above example, the logon screen uses the SQLAnywhere Connect dialog. Consult your 
specific database documentation for more information on this dialog. The end-user's ability to use 
the connect dialog will depend on the security surrounding the specific database. For example, 
the end-users may have access rights to a named database that they can access with the 
database’s client software, but they may not have access rights to other files that comprise the 
database.  
 
 
PROP:LogonScreen is valid for all SQL based drivers.  
 
PROP:Log 
PROP:Log writes a designated string value to the log file. For example: 
AFile FILE,DRIVER('ODBC'),OWNER('DataSource') 
## CODE
 OPEN(Afile) 
## IF NOT ERRORCODE()
  AFile{PROP:Log}='AFile opened:'&CLOCK() 
 END 
 
PROP:LogFile 
 
Same as PROP:Profile  -- for backward compatibility. 
 


---

Database Drivers 
208 
PROP:LoginTimeout 
 
(NOTE: Not valid for ORACLE Accelerator) 
PROP:LoginTimeout sets a time limit in seconds for an SQL database's login screen. If the user 
does not respond in the allotted time, the connection fails and the login is aborted. The default is 
to wait indefinitely for user input. Some servers do not support this feature and may ignore the 
instruction. For example: 
AFile FILE,DRIVER('SQL Driver'),OWNER('DataSource') 
## CODE
 OPEN(Afile) 
## IF NOT ERRORCODE()
  AFile{PROP:LoginTimeOut}=60 !allow 1 minute for login 
 END 
 
 
PROP:LogSQL 
A FILE property specifically used for SQL based tables, and turns on or off logging of calls to the 
backend for SQL drivers. A value of 1 turns on logging, a value of 0 turns off logging. 
Example: 
filelabel{PROP:LogSQL} = 1   !turn on logging 
filelabel{PROP:LogSQL} = 0   !turn off logging 
 
PROP:MaxStatements 
 
PROP:MaxStatements sets or returns the maximum amount of SQL statements that can be 
generated (open) on a single connection.  A connection must be active before implementing this 
property. 
number = file{PROP:MaxStatements}  !return allowable 
file{PROP:MaxStatements} = 32767   !set allowable 


---

Database Drivers and Interfaces 
209 
PROP:Name (SQL Properties) 
All of the SQL Accelerator Drivers now support the following syntax: 
view{'field_label',PROP:Name} = string  
to change the field's name in the generated SQL. This is normally a name that will be used for a 
field in a SELECT statement. 
Example: 
## PROGRAM
  MAP 
  END 
 
## EMP       FILE,DRIVER('ORACLE'),NAME('EMP'),PRE(EMP)
## P_EKY_EMP   KEY(EMP:EMPNO),NOCASE,OPT,PRIMARY
## KEY_DEP     KEY(EMP:DEPTNO),DUP,NOCASE,OPT
Record      RECORD 
EMPNO         SHORT !Emp-no 
ENAME         CSTRING(11) !Employee name 
JOB           CSTRING(10) !Job 
HIREDATE      DATE !Hiredate 
MGR           SHORT !Manager 
SAL           PDECIMAL(7,2) !Salary 
COMM          PDECIMAL(7,2) !Commisison 
## DEPTNO        BYTE
            END 
          END 
 
v VIEW(EMP) 
    PROJECT(EMP:EmpNo) 
  END 
 
## CODE
## OPEN(EMP)
    OPEN(v) 
## CODE
## OPEN(EMP)
    OPEN(v) 
    v{PROP:Order}=SQL(1) 
    v{'EMP:EmpNo',PROP:NAME} = 'count(*)' 
    SET(v) 
    NEXT(v) 
    MESSAGE(EMP:EmpNo) 
 
This example will produce the equivalent of "SELECT count(*) FROM EMP". 
 
 
See Also: PROP:SQL , PROP:Order  
 


---

Database Drivers 
210 
PROP:OrderAllTables 
Setting PROP:OrderAllTables to True forces the SQL Accelerator driver to use linking fields and 
secondary files' key component fields, as well as the primary file's key component fields, in the 
ORDER BY clause it sends to the server. You may need this switch if you are using a Clarion 
VIEW that joins multiple tables. By default (View{PROP:OrderAllTables}=FALSE), the SQL 
Accelerator driver includes only the primary file's key components in the ORDER BY clause it 
sends to the SQL server. For example: 
BRW1::View:Browse  VIEW(Customer) 
                       PROJECT(CUST:CustNo) 
                       PROJECT(CUST:Name) 
                       PROJECT(CUST:Zip) 
                       PROJECT(CUST:CustNo) 
                       JOIN(ORD:ByCustomer,CUST:CustNo) 
                         PROJECT(ORD:OrderNo) 
                         PROJECT(ORD:OrderDate) 
                       END 
                     END 
## CODE
  ?BRW1::View:Browse{PROP:OrderAllTables} = TRUE 
Accessing this VIEW then generates a SELECT statement similar to: 
 SELECT CustNo,Name,Zip,OrderNo,OrderDate FROM Customer,Ord 
   WHERE (Customer.CustNo = Ord.CustNo) 
  ORDER BY CustNo,OrderNo 
 
PROP:OrderInSelect 
(NOTE: Not valid for ORACLE Accelerator) 
Some SQL backends require that any fields used in the ORDER BY clause also appear in the 
SELECT statement. By setting this property to TRUE (1) the driver will make sure that this rule is 
applied for all views regardless of the fields that you project. 
 
PROP:Profile 
When you are tracing file driver activity and writing actions to an external log file, setting 
PROP:Profile to a valid logfile name alerts the driver to include Clarion I/O statements in the log 
file. Also, see the Profile switch described in the Debugging Your SQL Application section. 
In the DRIVERS.INI file in the CSIDL_APPDATA\SoftVelocity\Clarion\<clarion_version> folder, 
Profile=1 tells the driver to include the Clarion I/O statements in the log file;  Profile=0 tells the 
driver to omit Clarion I/O statements. The Profile switch must be turned on for the Details switch 
(described below) to have any effect. 
Details=1 tells the driver to include record buffer contents in the log file; however, if the file is 
encrypted, you must turn on both the Details switch and the /ALLOWDETAILS switch to log 
record buffer contents (see ALLOWDETAILS). Details=0 tells the driver to omit record buffer 
contents. The Profile switch must be turned on for the Details switch to have any effect. 
 
  
/ALLOWDETAILS is only valid as a parameter of the DRIVER attribute (Driver Options field 
in the File Properties dialog). It is not valid with the SEND command. 
See Also: PROP:Details , PROP:LOG , PROP:LOGSQL  


---

Database Drivers and Interfaces 
211 
PROP:QuoteString 
(NOTE: Not valid with Oracle Accelerator.) 
PROP:QuoteString sets or returns the column name delimiter (typically a quote) that the SQL 
Accelerator Driver uses to surround column names within its generated SQL statements. Different 
backends require different delimiter characters. 
You can use PROP:QuoteString to build your own dynamic SQL statements. Note that you must 
enclose any column names that are also SQL reserved words in the correct delimiter character. 
See Using Embedded SQL. 
Some backends do not correctly return the delimiter character. For those backends you should 
set the value of PROP:QuoteString before using it. 
 
PROP:ServerCaseInsensitive 
In previous versions of Clarion, the SQL file drivers assumed that your SQL server was set up to 
support case sensitive searches.  This required a modification of all case insensitive keys defined 
in the data dictionary to achieve optimum performance. 
The SQL drivers now assume that the server is set up with case insensitive searches, and no 
longer generate UPPER calls in the SQL code when requested by the Clarion code.  To turn off 
this behavior (force generation of UPPER calls), use PROP:ServerCaseInsensitive.  When this 
file property is active (1), you will make the file driver behave as in previous versions (prior to 6.3). 
  
This property only needs to be set once per connection and can only be done after a connection 
to the database has been established 
Example: 
Customer{PROP:ServerCaseInsensitive} = 1  
!server searches are now case insensitive. 
 


---

Database Drivers 
212 
## PROP:SQL
You can use Clarion's property syntax (PROP:SQL) to execute SQL statements in your program 
code by using PROP:SQL and naming the FILE or imported SQL VIEW in the data dictionary as 
the target within the normal execution of your program. This is only valid when using an SQL file 
driver (such as the ODBC, Scalable SQL, or Oracle drivers). You can send any SQL statements 
supported by the SQL server.  
This capability lets your program do backend operations independent of the SQL Accelerator 
driver's generated SQL. For example, multi-record updates can often be accomplished more 
efficiently with a single SQL statement than with a template generated Process procedure that 
updates one record at a time. In cases like these it makes sense for you to take control and send 
custom SQL statements to the backend, and PROP:SQL lets you do this. 
If you issue an SQL statement that returns a result set (such as an SQL SELECT statement), you 
use NEXT(file) to retrieve the result set one row at a time, into the file's record buffer. The FILE 
declaration receiving the result set must have at least the same number of fields as the SQL 
SELECT statement returns. If the Clarion ERRORCODE procedure returns 90, the 
FILEERRORCODE() and FILEERROR() functions return any error code and error message set 
by the back-end SQL server. In order to return a valid result set, you must also begin your 
statement with either SELECT or CALL.  If you need to return a result set and your statement 
does not begin with either SELECT or CALL, then use PROP:SQLRowSet 
You may also query the contents of PROP:SQL to get the last SQL statement issued by the file 
driver. 
Example: 
SQLFile{PROP:SQL}='SELECT field1,field2 FROM table1' | 
           & 'WHERE field1 > (SELECT max(field1)'    | 
           & 'FROM table2'         !Returns a result set you  
                                   ! get one row at a time 
                                   ! using NEXT(SQLFile) 
 
SQLFile{PROP:SQL}='CALL GetRowsBetween(2,8)'            !Call stored procedure 
 
SQLFile{PROP:SQL}='CREATE INDEX ON table1(field1 DESC)' !No result set 
  
SQLFile{PROP:SQL}='GRANT SELECT ON mytable TO fred'     !DBA tasks 
 
SQLString=SQLFile{PROP:SQL}                             !Get last SQL statement 


---

Database Drivers and Interfaces 
213 
## SEND
You can also use the Clarion SEND procedure to send an SQL command to the backend 
database. This is provided for backward compatibility with early versions of Clarion. We 
recommend using the property syntax to send SQL statements to the backend database. 
Example: 
SEND(SQLFile,'SELECT field1,field2 FROM table1'     | 
       & 'WHERE field1 > (SELECT max(field1)'  | 
       & 'FROM table2') ! Returns a result set you  
                        ! get one row at a time 
                        ! using NEXT(SQLFile) 
 
SEND(SQLFile,'CALL GetRowsBetween(2,8)')   !Call stored procedure 
 
SEND(SQLFile,'CREATE INDEX ON table1(field1 DESC)') !No result set 
SQL does a good job of handling batch processing procedures such as: printing reports, 
displaying a screen full of table rows, or updating a group of table rows. 
The SQL Accelerator drivers take full advantage of this when browsing a table or printing. 
However, they do not always use it to its best advantage with the Process template or in code 
which loops through a table to update multiple records. Therefore, when doing batch updates to a 
table, it can be much more efficient to execute an embedded SQL statement than to rely on the 
code generated by the Process template. 
For example, to use PROP:SQL to increase all Salesman salaries by 10% you could: 
 SQLFile   FILE,DRIVER('Oracle'),NAME(SalaryFile) 
 Record     RECORD 
 SalaryAmount  PDECIMAL(5,2),NAME('JOB') 
            END 
           END 
## CODE
  SqlFile{PROP:SQL} = 'UPDATE SalaryFile SET '&| 
## 'SALARY=SALARY * 1.1 WHERE JOB=''S'''
  
The names used in the SQL statement are the SQL table names, not the Clarion field names. 
See Also: Using Embedded SQL, PROP:SQLRowSet. 
 


---

Database Drivers 
214 
PROP:SQLFilter 
  
Although still valid in this release, this statement should be replaced by the more versatile SQL() 
statement. 
  
You can use PROP:SQLFilter to filter your VIEWs using native SQL code rather than Clarion 
code. This is only appropriate when using an SQL file driver (such as the ODBC, Scalable SQL, 
or Oracle drivers). If the first character of the PROP:SQLFilter expression is a plus sign (+), the 
PROP:SQLFilter expression is appended to any existing PROP:Filter expression and both are 
used. Omitting the plus sign replaces the existing PROP:Filter expression with the 
PROP:SQLFilter. 
When you use PROP:SQLFilter, the SQL filter is passed directly to the server. As such it cannot 
contain the names of tables, variables, or functions that the server is not aware of; that is the filter 
expression must be valid SQL syntax with valid SQL table and column names. For example: 
View{PROP:SQLFilter} = 'Date = TO_DATE(''01-MAY-1996'',''DD-MON-YYYY'')' 
or 
View{PROP:SQLFilter} = 'StrField LIKE ''AD%''' 
Note that the SQL Accelerator incorporates the PROP:SQLFilter expression into the WHERE 
clause of a generated SELECT statement. The generated SELECT statement may reference one 
or more tables by aliases. If your filter also references tables (e.g., Customer.Name < 'T'), you 
must use the same alias names generated by the SQL Accelerator. By default, the SQL 
Accelerator uses the next letter of the alphabet as the alias name. For example, the Accelerator 
uses 'A' as the alias for the first table in the generated SELECT statement, then 'B' for the next 
table, and so on. You can use PROP:Alias to control the alias names generated by the SQL 
Accelerator. See PROP:Alias for more information. 
 Combining VIEW Filters and SQL Filters 
When you use PROP:SQLFilter, the SQL filter may replace any filter specified for the VIEW, or it 
may be in addition to a filter specified for the VIEW. Prefix the SQL filter with a plus sign (+) to 
append the SQL filter to the existing VIEW filter. For example: 
View{PROP:SQLFilter} = '+ StrField LIKE ''AD%''' 
When you append the SQL filter by using the plus sign, the logical end result of the filtering 
process is (View Filter) AND (SQL Filter). 
Omit the plus sign (+) to replace the Clarion filter with the SQL filter. When you replace the 
Clarion filter with the SQL filter by omitting the plus sign, the logical end result of the filtering 
process is simply (SQL Filter). 
See Also:  PROP:Filter for additional information. 
 


---

Database Drivers and Interfaces 
215 
PROP:SQLJoinExpression 
You can use PROP:SQLJoinExpression to structure your VIEWs using native SQL code rather 
than Clarion code. 
  
Using PROP:SQLJoinExpression may hurt performance in some circumstances. 
When you use PROP:SQLJoinExpression, the SQL join expression is passed directly to the 
server. As such it cannot contain the name of variables or functions that the server is not aware 
of; that is the join expression must be valid SQL syntax with valid SQL column names. For 
example: 
View{PROP:SQLJoinExpression} = 'TO_DATE - FROM_DATE' 
Combining VIEW Orders and SQL Orders 
When you use PROP:SQLJoinExpression, the SQL join expression may replace any the join 
specified for the VIEW, or it may be in addition to the join specified for the VIEW. Prefix the SQL 
join with a plus sign (+) to concatenate the SQL join expression to the existing VIEW join 
expression. For example: 
View{PROP:SQLOrder} = '+ TO_DATE - FROM_DATE' 
When you concatenate the SQL join by using the plus sign, the result set contains first the Clarion 
joined values, then the SQL joined values. 
Omit the plus sign (+) to replace the Clarion join expression with the SQL join expression. 
  
PROP:SQLJoinExpression only affects the JOIN portions of the VIEW declaration; it does 
not affect the PROJECT portions. 


---

Database Drivers 
216 
PROP:SQLOrder 
You can use PROP:SQLOrder to sort your VIEWs using native SQL code rather than Clarion 
code. 
 
  
Using PROP:SQLOrder may hurt performance in some circumstances. 
When you use PROP:SQLOrder, the SQL order is passed directly to the server. As such it cannot 
contain the name of tables, variables, or functions that the server is not aware of; that is the order 
expression must be valid SQL syntax with valid SQL column names. For example: 
View{PROP:SQLOrder} = 'TO_DATE - FROM_DATE' 
Note that the SQL Accelerator incorporates the PROP:SQLOrder expression into the ORDERBY 
clause of a generated SELECT statement. The generated SELECT statement may reference one 
or more tables by aliases. If your order expression also references tables (e.g., Customer.Name < 
'T'), you must use the same aliase names generated by the SQL Accelerator. By default, the 
SQL Accelerator uses the next letter of the alphabet as the alias name. For example, the 
Accelerator uses 'A' as the alias for the first table in the generated SELECT statement, then 'B' for 
the next table, and so on. You can use PROP:Alias to control the alias names generated by the 
SQL Accelerator. See PROP:Alias for more information. 
 Combining SQL Orders and VIEW Orders 
When you use PROP:SQLOrder, the SQL order may replace any order specified for the VIEW, or 
it may be in addition to the order specified for the VIEW. Prefix the SQL order with a plus sign (+) 
to append the SQL order to the existing VIEW order. For example: 
View{PROP:SQLOrder} = '+ TO_DATE - FROM_DATE' 
When you append the SQL order by using the plus sign, the result set is ordered first by the 
Clarion order expression, then by the SQL order expression. 
Omit the plus sign (+) to replace the Clarion order with the SQL order. 
See Also:      PROP:Order  
 


---

Database Drivers and Interfaces 
217 
PROP:SQLRowSet 
You can use Clarion's property syntax (PROP:SQLRowSet) to execute SQL statements that 
return result sets in your program code by using PROP:SQLRowSet and naming the FILE or 
imported SQL VIEW in the data dictionary as the target within the normal execution of your 
program. This is only valid when using an SQL file driver (such as the ODBC, Scalable SQL, or 
Oracle drivers). You can send any SQL statements that return results supported by the SQL 
server.  
After issuing the SQL statement, you use NEXT(file) to retrieve the result set one row at a time, 
into the file's record buffer. The FILE declaration receiving the result set must have at least as 
many fields as the SQL SELECT statement returns. If the Clarion ERRORCODE procedure 
returns 90, the FILEERRORCODE() and FILEERROR() functions return any error code and error 
message set by the back-end SQL server. 
Example: 
SQLiteFile{PROP:SQLRowSet}='PRAGMA table_list' ! get the list of tables in file 
## LOOP
  NEXT(SQLiteFile) 
  … 
END 
f{PROP:SQLRowSet} = 'WITH q AS (SELECT COUNT(*) FROM f) SELECT * FROM q' 
  NEXT(f) 
 
  
The names used in the SQL statement are the SQL table names, not the Clarion field names. 
See Also: Using Embedded SQL, PROP:SQLRowSet. 
 


---

Database Drivers 
218 
PROP:TraceFile 
 
SYSTEM{PROP:TraceFile} = INIFilename 
 
A SYSTEM property that specifies the INI file that file drivers will read to get driver tracing settings 
from.  The drivers will look in the [CW<drivername>] section for specific settings. 
 
If PROP:TraceKey and PROP:TraceFile are both set, PROP:TraceFile is ignored.  If neither 
PROP:TraceKey or PROP:TraceFile are specified, then DRIVERS.INI in the 
CSIDL_APPDATA\SoftVelocity\Clarion\<clarion_version> folder is used. 
 
  
These properties must be set before ANY file I/O calls are done. 
 
PROP:TraceKey 
 
SYSTEM{PROP:TraceKey} = keyName 
 
A SYSTEM property that specifies the Registry key that the file drivers will read to get driver 
tracing settings from.  The drivers will look at entries in the keyName\<driverName> key for 
driver tracing settings.   
 
Valid values in the key are 
 
Name 
Type 
Possible Values 
Profile 
## DWORD
0 or 1 
Details 
## DWORD
0 or 1 
Trace 
## DWORD
0 or 1 
TraceFile 
## STRING
Pathname 
 
If PROP:TraceKey and PROP:TraceFile are both set, then PROP:TraceFile is ignored.  If 
neither PROP:TraceKey or PROP:TraceFile is specified, then DRIVERS.INI in the 
CSIDL_APPDATA\SoftVelocity\Clarion\<clarion_version> folder is used. 
 
 
These properties must be set before ANY file I/O calls are done. 
 


---

Database Drivers and Interfaces 
219 
MSSQL Accelerator 
Overview 
MSSQL Server 
For complete information on the MSSQL database system, please review Microsoft's SQL Server 
documentation. 
MSSQL Accelerator 
The MSSQL Accelerator is one of several SoftVelocity SQL Accelerator drivers. These SQL 
Drivers share a common code base and many common features such as SoftVelocity's unique, 
high speed buffering technology, common driver strings, and SQL logging capability. See SQL 
Accelerators for information on these common features. 
The MSSQL Accelerator converts standard Clarion file I/O statements and function calls into 
optimized SQL statements, which it sends to the backend MSSQL server for processing. This 
means you can use the same Clarion code to access both MSSQL tables and other file systems 
such as TopSpeed files. It also means you can use Clarion template generated code with your 
SQL databases. 
All the common behavior of all the SQL Accelerators is documented in the SQL Accelerators 
section.  The MSSQL Accelerator is based on the ODBC Accelerator and inherits all features of 
the ODBC Accelerator.  All the common behavior of the SQL Accelerators that are derived from 
the ODBC Accelerator is documented in the ODBC Accelerator section.  All behavior specific to 
this driver is noted here. 


---

Database Drivers 
220 
MSSQL Import Wizard--Login Dialog 
Clarion's Dictionary Editor Import Wizard lets you import MSSQL table definitions into your 
Clarion Data Dictionary. When you select the MSSQL Accelerator from the driver drop-down list, 
the Import Wizard opens the Login/Connection dialog. The Login/Connection dialog collects 
the connection information for the MSSQL database. 
  
If you are using a Trusted Connection (Integrated NT Security), you must establish a 
connection to the NT workstation running the MSSQL Server before you can connect to 
the MSSQL database and import table definitions. You  can verify your connection by 
running the MSSQL ISQL_w Server utility installed with your MSSQL Client software. 
Fill in the following fields in the Login/Connection dialog: 
Servername 
Select the workstation running the MSSQL database to import from. If the 
Servername list is empty, you may type in the name. See your DBA or 
network administrator for information on how the server is specified. 
Username 
For Standard Security, type your MSSQL Username. For Trusted Security 
(Integrated NT Security) no Username is required. See your server 
documentation or your DBA for information on applicable Usernames and 
security methods. 
Password 
For Standard Security, type your MSSQL Password. For Trusted Security 
(Integrated NT Security) no Password is required. See your server 
documentation or your DBA for information on applicable Passwords and 
security methods. 
Database 
Select the MSSQL database that contains the tables or views to import. If 
the Database list is empty, you may type in the name. See your server 
documentation or your DBA for information on database names. 
Filter 
Optionally, provide a filter expression to limit the list of tables and views to 
import. The filter expression queries the dbo.sysobjects table. The filter 
expression is limited to 1024 characters in length.Tip: The filter is case 
sensitive, so type your filter value accordingly. 
 


---

Database Drivers and Interfaces 
221 
Following is a list of the column names (and their Clarion datatypes) you can reference in your 
filter expression. Generally, filtering on MSSQL system tables requires not only an intimate 
knowledge of the MSSQL system tables, but also of the MSSQL stored procedures. For example, 
to filter on table owner: 
uid = user_id('DBO') 
See your SQL server documentation for information on the MSSQL system tables and stored 
procedures. 
 
name 
## CSTRING(31)
id 
## LONG
uid 
## SHORT
type 
## STRING(2)
userstat 
## SHORT
sysstat 
## SHORT
indexdel 
## SHORT
schema_ver 
## SHORT
refdate 
## STRING(8)
crdate 
## STRING(8)
version 
## LONG
deltrig 
## LONG
Instrig 
## LONG
updtrig 
## LONG
Seltrig 
## LONG
category 
## LONG
Cache 
## SHORT
 
Next > 
Press this button to open the Import Wizard's Import List dialog. 
 


---

Database Drivers 
222 
MSSQL Import Wizard--Import List Dialog 
When you press the Next > button, the Import Wizard opens the Import List dialog. The Import 
List dialog lists the importable items. 
Highlight the table or view whose definition to import, then press the Finish button to import. The 
Import Wizard adds the definition to your Clarion Data Dictionary, then opens the File Properties 
dialog to let you modify the default definition. 
Import additional tables or views by repeating these steps. After all the items are imported, return 
to the Dictionary Editor where you can define relationships and delete any columns not used in 
your Clarion application. See SQL Accelerators--Define Only the Fields You Use. 
  
You can use the Clarion Enterprise Edition Dictionary Synchronizer to import an entire 
database, including table relationships, in a single pass. 


---

Database Drivers and Interfaces 
223 
MSSQL Connection Information and Driver 
Configuration--File Properties 
Typically, you add MSSQL support to your application by importing the table definitions into your 
Clarion Data Dictionary. The Import Wizard automatically fills in the File Properties dialog with 
default values based on the imported item. However, you can use the Owner Name field in the File 
Properties dialog to further configure the way the MSSQL Accelerator accesses the data. 
The OWNER attribute for MSSQL takes the format: 
server,<database>,<uid>,<pwd><;LANGUAGE=language><;APP=name><;WSID=name> 
 
## LANGUAGE
The language used by MSSQL Server. 
APP 
The name of the application. 
## WSID
The workstation ID. Typically, this is the network name 
of the computer on which the application resides. 
See your MSSQL Server documentation for information on these settings. 
The MSSQL driver uses ODBC to communicate with the MSSQL engine.  When more than one 
ODBC Driver for MSSQL is installed on a machine the driver will choose to use the “SQL Server 
Native Client” driver before the “SQL Server” driver.  To force the driver to use a specific ODBC  
Driver you add to the Windows Registry the String Value “Dll” to the key 
HKEY_LOCAL_MACHINE\Software\SoftVelocity\MSSQL.  You set this value to the name of the 
ODBC Driver.  For Example, set the value to “SQL Server Native Client 10.0” to force the MSQL 
driver to use the 10.0 Driver even when the 11.0 driver is available. 
  
Type an exclamation point (!) followed by a variable name in the Owner Name field to 
specify a variable rather than hard coding the OWNER attribute . For example: 
!GLO:SQLOwner. 


---

Database Drivers 
224 
MSSQL Accelerator Performance Considerations 
The MSSQL Accelerator uses cursors. The MSSQL Server will not use an Index with a cursor, 
but it will use a Unique Constraint with a cursor. Therefore we recommend using Unique 
Constraints rather than Indexes wherever possible. 
 
 
MSSQL Connection Tips 
 
MS SQL Driver connecting using TCP/IP and a Managed Client 
When using a TCP/IP connection string and a managed client, you may encounter the following 
error window on connectiong. 
  
This error happens when using SQL managed client tries to connect to a server using TCP/IP 
and the default port used by the managed client is wrong. Set up the correct port name using the 
MSSQL configuration utility. 


---

Database Drivers and Interfaces 
225 
  


---

Database Drivers 
226 
MSSQL Accelerator Calling a Stored Procedure 
Stored procedures can return an output parameter and return results. These can only be returned 
if the file is opened in Read-Only mode (10H). The output parameters and return results are not 
available until all records have been retrieved by a SELECT statement. 
## PROGRAM
MAP 
 CheckError(STRING) !Check for errorcodes 
 CallProc(STRING)   !Call Stored Procedure 
END 
 
MyFile FILE,DRIVER('MSSQL') 
Record  RECORD 
c        LONG 
        END 
       END 
 
Ret       LONG 
In        SHORT(10) 
Out       STRING(10) 
CreateReq BYTE(FALSE) 
 
## CODE
BIND('Ret',Ret) 
CheckError('BIND Ret') 
BIND('Out',Out) 
CheckError('BIND Out') 
BIND('In',In) 
CheckError('BIND In') 
 
MyFile{PROP:SQL} = 'DROP TABLE SProctable' 
MyFile{PROP:SQL} = 'CREATE TABLE SProctable (c INT)' 
 
!Give MyFile initial data 
OPEN(MyFile) 
CheckError('Open') 
MyFile.c=5 
ADD(MyFile) 
CheckError('Add 5') 
MyFile.c=7 
ADD(MyFile) 
CheckError('Add 7') 
MyFile.c=8 
ADD(MyFile) 
CheckError('Add 8') 
 
!Initialize and Create Stored Procedures 
MyFile{PROP:SQL} = 'DROP PROC SProc1' 
MyFile{PROP:SQL} = 'DROP PROC SProc2' 
MyFile{PROP:SQL} = 'DROP PROC SFunc1' 
MyFile{PROP:SQL} = 'DROP PROC SFunc2' 
MyFile{PROP:SQL} = 'DROP PROC SFunc3' 
CallProc('CREATE PROC SFunc1 @input VARCHAR(10),@output VARCHAR(10) '& |  
 'OUTPUT  AS SELECT @output = CHAR(ASCII('')'')+c) FROM SProctable ' & | 
  'WHERE c=7 ' & RETURN ASCII(@input) ') 
CallProc('CREATE PROC SFunc2 @sin INT, @strin VARCHAR(10) AS ' & | 
 ' SELECT c FROM SProctable RETURN @sin + ASCII(@strin)') 
CallProc('CREATE PROC SFunc3 @input VARCHAR(10) AS ' & | 
 ' RETURN ASCII(@input) ') 


---

Database Drivers and Interfaces 
227 
CallProc('CREATE PROC SProc1 @inp INT AS ' & | 
 ' INSERT INTO SProctable values(@inp) ') 
CallProc('CREATE PROC SProc2 @inp INT AS ' & | 
 ' INSERT INTO SProctable values(@inp) ' & | 
 ' SELECT c FROM SProctable') 
CLOSE(MyFile) 
 
!Open MyFile in Read-Only mode 
OPEN(MyFile,10H) 
 
!Call Stored Procedure passing input value using NORESULTCALL 
!sets output parameter 
CallProc('&Ret = NORESULTCALL SFunc3(''1'')') 
IF Ret ~= VAL('1') 
  MESSAGE('Ret of NORESULTCALL SFunc3 =' & Ret) 
END 
 
!Call Stored Procedure passing input value, sets output parameter  
CallProc('&Ret = CALL SFunc3(10)') 
IF Ret ~= VAL('1') 
  MESSAGE('Ret of SFunc3 =' & Ret) 
END 
 
!Call Stored Procedure passing input value, no return values  
CallProc('CALL SProc1(10)') 
 
!Call Stored Procedure passing input value, return return code 
CallProc('CALL SProc1(&in[IN])') 
 
!Call Stored Procedure passing input value, return output parameter 
CallProc('&Ret = CALL SFunc1(''1'',&out)') 
IF Ret ~= VAL('1') 
  MESSAGE('Ret of SFunc1 =' & Ret) 
END 
IF out ~= CHR(VAL(')')+7) 
  MESSAGE('out of SFunc1 =' & out) 
END 
 
!Call Stored Procedure passing input value, return return code 
CallProc('CALL SProc2(&in[IN])') 
 
NEXT(MyFile) 
CheckError('Next SProc2') 
!Call Stored Procedure passing input values, return output parameter 
CallProc('&Ret = CALL SFunc2(7, '')'')') 
## LOOP WHILE ~ERRORCODE()
  NEXT(MyFile) 
END 
IF Ret ~= VAL(')')+7 
  MESSAGE('out of SFunc2 =' & out) 
END 
MESSAGE('Done') 
 
!Check for errorcodes 
CheckError PROCEDURE(Msg) 
## CODE
## IF ERRORCODE()
## IF ERRORCODE() = 90
  MESSAGE(Msg & ' ' & FILEERRORCODE() & ':' & FILEERROR()) 
## ELSE


---

Database Drivers 
228 
  MESSAGE(Msg & ' ' & ERRORCODE() & ':' & ERROR()) 
 END 
END 
 
!CallProc calls the stored procedures using the PROP:SQL statement 
CallProc PROCEDURE(Str) 
## CODE
MyFile{PROP:SQL} = Str 
CheckError(Str) 
 


---

Database Drivers and Interfaces 
229 
MSSQL Accelerator Using Embedded SQL 
Calling Stored Procedures 
Stored procedures can return an output parameter and return results. These can only be returned 
if the file is opened in Read-Only mode (10H). The return result of a stored procedure is not 
available until all records have been retrieved from any SELECT statement in the stored 
procedure. 
 
## PROGRAM
  MAP 
   CheckError(STRING) !Check for errorcodes 
   CallProc(STRING)   !Call Stored Procedure 
  END 
 
MyFile FILE,DRIVER('MSSQL'),NAME('SProctable') 
Record  RECORD 
c        LONG 
        END 
       END 
 
Ret       LONG 
In        SHORT(10) 
Out       STRING(10) 
CreateReq BYTE(FALSE) 
 
## CODE
  BIND('Ret',Ret) 
  CheckError('BIND Ret') 
  BIND('Out',Out) 
  CheckError('BIND Out') 
  BIND('In',In) 
  CheckError('BIND In') 
 
  MyFile{PROP:SQL} = 'DROP TABLE SProctable' 
  MyFile{PROP:SQL} = 'CREATE TABLE SProctable (c INT)' 
 
  !Give MyFile initial data 
  SHARE(MyFile) 
  CheckError('Open') 
  MyFile.c=5 
  ADD(MyFile) 
  CheckError('Add 5') 
  MyFile.c=7 
  ADD(MyFile) 
  CheckError('Add 7') 
  MyFile.c=8 
  ADD(MyFile) 
  CheckError('Add 8') 
 


---

Database Drivers 
230 
  !Initialize and Create Stored Procedures 
  MyFile{PROP:SQL} = 'DROP PROC SProc1' 
  MyFile{PROP:SQL} = 'DROP PROC SProc2' 
  MyFile{PROP:SQL} = 'DROP PROC SFunc1' 
  MyFile{PROP:SQL} = 'DROP PROC SFunc2' 
  MyFile{PROP:SQL} = 'DROP PROC SFunc3' 
  CallProc('CREATE PROC SFunc1 @input VARCHAR(10),@output VARCHAR(10) OUTPUT AS ' &| 
              'SELECT @output = CHAR(ASCII('')'')+c) FROM SProctable  WHERE c=7 ' &| 
              'RETURN ASCII(@input) ') 
 
  CallProc('CREATE PROC SFunc2 @sin INT, @strin VARCHAR(10) AS ' & | 
   ' SELECT c FROM SProctable RETURN @sin + ASCII(@strin)') 
 
  CallProc('CREATE PROC SFunc3 @input VARCHAR(10) AS ' & | 
   ' RETURN ASCII(@input) ') 
 
  CallProc('CREATE PROC SProc1 @inp INT AS ' & | 
   ' INSERT INTO SProctable values(@inp) ') 
 
  CallProc('CREATE PROC SProc2 @inp INT AS ' & | 
   ' INSERT INTO SProctable values(@inp) ' & | 
   ' SELECT c FROM SProctable') 
 
  !Call Stored Procedure passing input value using NORESULTCALL 
  !sets output parameter 
  CallProc('&Ret = NORESULTCALL SFunc3(''1'')') 
  IF Ret ~= VAL('1') 
    MESSAGE('Ret of NORESULTCALL SFunc3 =' & Ret) 
  END 
 
  !Call Stored Procedure passing input value, no return values 
  CallProc('CALL SProc1(10)') 
 
  !Call Stored Procedure passing input value, return return code 
  CallProc('CALL SProc1(&in[IN])') 
 
  !Call Stored Procedure passing input value, return output parameter 
  ret = 0 
  CallProc('&Ret = CALL SFunc1(''1'',&out)') 
  IF Ret ~= VAL('1') 
    MESSAGE('Ret of SFunc1 =' & Ret) 
  END 
  IF out ~= CHR(VAL(')')+7) 
    MESSAGE('out of SFunc1 =' & out) 
  END 
 
  !Call Stored Procedure passing input value, return return code 
 
  CallProc('CALL SProc2(&in[IN])') 
 
  NEXT(MyFile) 
  CheckError('Next SProc2') 
 
  ret = 0 
  !Call Stored Procedure passing input values, return output parameter 
  CallProc('&Ret = CALL SFunc2(7, '')'')') 
  IF Ret ~= 0 
    MESSAGE('out of SFunc2 before fetches =' & Ret) 
  END 
## LOOP WHILE ~ERRORCODE()
    NEXT(MyFile) 
  END 


---

Database Drivers and Interfaces 
231 
  IF Ret ~= VAL(')')+7 
    MESSAGE('out of SFunc2 =' & Ret) 
  END 
  MESSAGE('Done') 
  !Check for errorcodes 
 
CheckError PROCEDURE(Msg) 
## CODE
## IF ERRORCODE()
## IF ERRORCODE() = 90
      HALT(1, Msg & ' ' & FILEERRORCODE() & ':' & FILEERROR()) 
## ELSE
      HALT(1, Msg & ' ' & ERRORCODE() & ':' & ERROR()) 
    END 
  END 
 
  !CallProc calls the stored procedures using the PROP:SQL statement 
CallProc PROCEDURE(Str) 
## CODE
    MyFile{PROP:SQL} = Str 
    CheckError(Str) 
 


---

Database Drivers 
232 
MSSQL Accelerator Driver Strings 
There are switches or "driver strings" you can set to control the way your application creates, 
reads, and writes files with a specific driver. Driver strings are simply messages or parameters 
that are sent to the file driver at run-time to control its behavior. See Common Driver Features--
Driver Strings for an overview of these runtime Database Driver switches and parameters. 
  
A forward slash preceeds all SQL Accelerator driver strings. The slash allows the driver to 
distinguish between driver strings and SQL statements sent with SEND. 
In addition to the standard SQL Driver Strings, the MSSQL Accelerator supports the following 
Driver Strings: 
## AUTOINCUSESSCOPEIDENTITY
## HINT
## LOGONSCREEN
## GATHERATOPEN
## SAVESTOREDPROC
## TRUSTEDCONNECTION
 
 
 


---

Database Drivers and Interfaces 
233 
## AUTOINCUSESSCOPEIDENTITY
MSSQL has three ways of returning the auto-incremented field:  @@IDENTITY, 
SCOPE_IDENTITY() and IDENT_CURRENT( 'table_name' ).  All have problems. 
IDENT_CURRENT( 'table_name' ) is pretty useless as it returns the current identity regardless of 
which user last updated the table.  So as soon as another user does an ADD between the calls to 
ADD and getting IDENT_CURRENT you get the wrong value. 
@@IDENTITY gives you the last identity value set by this connection.  This works fine unless you 
have an insert trigger that inserts other records that have identity fields.  Then you end up getting 
the identity field for the wrong table.  The default server side auto increment system uses this 
variable. 
SCOPE_IDENTITY() returns the identity set by the statement executed on this statement handle.  
Before Clarion 10, the file driver could not use this because the INSERT statement executed by 
the driver and the SELECT used to retrieve the incremented value where executed on different 
statement handles.  So SCOPE_IDENTITY() always returned 0. 
As of Clarion 10, If you add the driver string /AUTOINCUSESSCOPEIDENTITY=TRUE to the 
driver string of a file, the driver will use SCOPE_IDENTITY() using the same statement handle as 
the INSERT to retrieve the auto-incremented value. 
Example: 
tzi FILE,DRIVER('MSSQL','/AUTOINC=''SELECT @@identity'' 
/TRUSTEDCONNECTION=TRUE'),PRE(tzi),OWNER(ownerVariable),NAME('tz') 
pk  
KEY(tzi:id) 
## RECORD
Id  
 
## LONG
Name 
 
## STRING(20)
END 
END 
tzs FILE,DRIVER('MSSQL','/ AUTOINCUSESSCOPEIDENTITY=TRUE 
/TRUSTEDCONNECTION=TRUE'),PRE(tzs),OWNER(ownerVariable),NAME('tz') 
pk  
KEY(tzs:id) 
## RECORD
Id  
 
## LONG
Name 
 
## STRING(20)
END 
END 
## CODE
tzi{PROP:SQL} = 'DROP TABLE TZ' 
tzi{PROP:SQL} = 'DROP TABLE TY' 
tzi{PROP:SQL} = 'CREATE TABLE TZ (id int IDENTITY(1,1) PRIMARY KEY, name 
varchar(20) NOT NULL)' 
tzi{PROP:SQL} = 'CREATE TABLE TY (id int IDENTITY(100,5) PRIMARY KEY, name 
varchar(20) NOT NULL)' 
tzi{PROP:SQL} = 'CREATE TRIGGER Ztrig ON TZ FOR INSERT AS BEGIN INSERT TY 
## VALUES ('''') END'
OPEN(tzi) 
tzi{PROP:ServerAutoInc, 1} = 1 
OPEN(tzs) 
tzs{PROP:ServerAutoInc, 1} = 1 
tzi:name = 'Lisa' 
ADD(tzi) 
tzi:name = 'Mike' 
ADD(tzi) 
tzi:name = 'Carla' 
ADD(tzi) 
tzi{PROP:ServerAutoInc} = 1 
tzi:name = 'Rosalie' 
ADD(tzi) 


---

Database Drivers 
234 
MESSAGE(ERRORCODE() & ':' & tzi:id) ! tzi:id will be 115 
tzs:name = 'Ilka' 
tzs{PROP:ServerAutoInc} = 1 
ADD(tzs) 
MESSAGE(ERRORCODE() & ':' & tzs:id) !tzs:id will be 5 
 
## HINT
You can tell MSSQL Accelerator to generate MSSQL hints by using the HINT driver string, 
DRIVER ('MSSQL','/HINT=hint') 
by using /HINT in the key name,  
Key KEY(fieldlist),NAME('name /HINT=[&]hint') 
with SEND,  
SendReturn = SEND (file,' /HINT=[&]hint') 
or with the PROP:Hint property,  
file{PROP:Hint} = '[&]hint' 
HintString = file{PROP:Hint} 
The square brackets [] above are used to show that the ampersand (&) is optional. 
You can either override the base hint or concatenate a hint. If the first character after the = in the 
KEY hint is an ampersand (&), MSSQL Accelerator concatenates the hint onto the FILE hint, 
otherwise it overrides the FILE hint. 
If the first character after the = in the SEND hint is an ampersand (&) or the first character of a 
hint property is an ampersand, MSSQL Accelerator concatenates the hint onto the current hint 
(the FILE hint and the KEY hint), otherwise it overrides the FILE and KEY hint. 
You can also use PROP:Hint to return the hint that is in use (or will be in use if called after a SET, 
but before the first NEXT or PREVIOUS statement.) 
Example: 
 AFile DRIVER('MSSQL','/hint=COST') 
 AKey KEY(field),NAME('KeyName /HINT=&FIRST_ROWS') 
 SEND(AFile,'/HINT=FIRST_ROWS') 
 AFile{PROP:Hint} = 'FIRST ROWS' 
 
LOGONSCREEN (MSSQL Accelerator) 
 
## DRIVER('MSSQL', '/LOGONSCREEN = TRUE | FALSE ' )
[ AutoLogon" = ] SEND(file, '/LOGONSCREEN [ = TRUE | FALSE ]' ) 
 
See Also: PROP:LogonScreen. 
 
GATHERATOPEN (MSSQL Accelerator) 
 
## DRIVER('MSSQL', '/GATHERATOPEN = TRUE | FALSE ' )
By default the driver delays gathering field information until it is required. However, some 
backends (like Sybase 11) perform poorly under these conditions. Setting GATHERATOPEN to 


---

Database Drivers and Interfaces 
235 
TRUE forces the driver to gather most of the field information when the file is opened, which 
avoids a slowdown during program execution.  


---

Database Drivers 
236 
SAVESTOREDPROC (MSSQL Accelerator) 
 
## DRIVER('MSSQL', '/SAVESTOREDPROC= TRUE | FALSE ' )
[ SaveProc" = ] SEND(file, '/SAVESTOREDPROC [ = TRUE | FALSE ]' ) 
When the MSSQL Accelerator sends SQL statements to the MSSQL server, the server creates a 
temporary stored procedure on the server and executes it.  The stored procedure is reused on 
subsequent executions of the same SQL statement.  By default, (SAVESTOREDPROC=TRUE), 
and these stored procedures remain on the server until connection to the server is dropped.  
To remove the procedures as soon as possible, set SAVESTOREDPROC=FALSE.  Note that this 
is something done by MSSQL and may vary with different versions of MSSQL.  For complete 
details on how MSSQL optimizes your code please refer to the documentation of the specific 
version of MSSQL you are using in the section dealing with calling MSSQL via ODBC. 
 
TRUSTEDCONNECTION (MSSQL Accelerator) 
 
## DRIVER('MSSQL', '/TRUSTEDCONNECTION = TRUE | FALSE ' )
[ Trusted" = ] SEND(file, '/TRUSTEDCONNECTION [ = TRUE | FALSE ]' ) 
By default (TRUSTEDCONNECTION=FALSE), the MSSQL Accelerator requests a standard 
connection to SQL Server. To connect using SQL Server integrated security, set 
## TRUSTEDCONNECTION=TRUE.
  
To set the connection type, you must issue the TRUSTEDCONNECTION switch before the 
connection is made to the server. 


---

Database Drivers and Interfaces 
237 
MSSQL Accelerator Driver Properties 
You can use Clarion's property syntax to query and set certain MSSQL Accelerator driver 
properties. In addition to the standard SQL Accelerator properties (see SQL Accelerators--SQL 
Accelerator Properties), the MSSQL Accelerator supports the following properties. 
 
PROP:LogonScreen (MSSQL Accelerator) 
PROP:LogonScreen sets or returns the toggle that determines whether the driver automatically 
prompts for logon information. By default (PROP:LogonScreen=True), the driver does display a 
logon window if no connect string is supplied. If set to False and there is no connect string, the 
OPEN(file) fails and FILEERRORCODE() returns '28000.' For example: 
Afile  FILE,DRIVER('MSSQL') 
!file declaration with no userid and password 
       END 
## CODE
 AFile{PROP:LogonScreen}=True   !enable auto login screen 
 OPEN(Afile) 
The automatic logon screen lets prompts for the following connection information. Consult your 
MSSQL documentation for more information on these prompts: 
Server 
Select the workstation running the MSSQL database to import 
from. If the Server list is empty, you may type in the name. See 
your DBA or network administrator for information on how the 
server is specified. 
Logon ID 
For Standard Security, type your MSSQL Username. For 
Trusted Security (Integrated NT Security) no Username is 
required. See your server documentation or your DBA for 
information on applicable Usernames and security methods. 
Password 
For Standard Security, type your MSSQL Password. For Trusted 
Security (Integrated NT Security) no Password is required. See 
your server documentation or your DBA for information on 
applicable Passwords and security methods. 
Options 
Press this button to enable the following prompts. See your 
MSSQL Server documentation for information on these prompts. 
Database 
Select the MSSQL database that contains the tables or views to 
access. If the Database list is empty, you may type in the name. 
See your server documentation or your DBA for information on 
database names. 
Language 
The language used by MSSQL Server. 
Application Name 
The name of the application. 
WorkStation ID 
The workstation ID. Typically, this is the network name of the 
computer on which the application resides. 
 


---

Database Drivers 
238 
MSSQL Supported Commands and Attributes 
 
 
File Attributes 
Supported 
 
## CREATE
Y 
 
DRIVER(filetype [,driver string]) 
Y 
 
## NAME
Y 
 
## ENCRYPT
N 
 
OWNER(password) 
Y1 
 
## RECLAIM
N 
 
PRE(prefix) 
Y 
 
## BINDABLE
Y 
 
## THREAD
Y 
 
EXTERNAL(member) 
Y 
 
DLL([flag]) 
Y 
 
OEM 
N 
 
## LOCALE
N 
 
 
File Structures 
Supported 
 
## INDEX
Y 
 
KEY 
Y 
 
## MEMO
N 
 
## BLOB
Y 
 
## RECORD
Y 
 
 
Index, Key, Memo Attributes 
Supported 
 
## BINARY
N 
 
DUP 
Y 
 
## NOCASE
Y 
 
OPT 
N 


---

Database Drivers and Interfaces 
239 
 
## PRIMARY
Y 
 
## NAME
Y 
 
Ascending Components 
Y 
 
Descending Components 
Y 
 
Mixed Components 
Y 
 
 
Field Attributes 
Supported 
 
DIM 
N 
 
## OVER
Y 
 
## NAME
Y 
 
 
File Procedures 
Supported 
 
BOF(file) 
N 
 
BUFFER(file) 
Y 
 
BUILD(file) 
Y 
 
BUILD(key) 
Y 
 
BUILD(index) 
Y3 
 
BUILD(index, components) 
Y3 
 
BUILD(index, components, filter) 
N 
 
BYTES(file) 
Y 
 
CLOSE(file) 
Y 
 
COPY(file, new file) 
N 
 
CREATE(file) 
Y 
 
DUPLICATE(file) 
Y 
 
DUPLICATE(key) 
Y 
 
EMPTY(file) 
Y 
 
EOF(file) 
N 
 
FLUSH(file) 
N 
 
LOCK(file) 
N 


---

Database Drivers 
240 
 
NAME(label) 
Y 
 
OPEN(file, access mode) 
Y 
 
PACK(file) 
N 
 
POINTER(file) 
N 
 
POINTER(key) 
N 
 
POSITION(file) 
N 
 
POSITION(key) 
Y 
 
RECORDS(file) 
Y 
 
RECORDS(key) 
Y 
 
REMOVE(file) 
Y 
 
RENAME(file, new file) 
N 
 
SEND(file, message) 
Y 
 
SHARE(file, access mode) 
Y 
 
STATUS(file) 
Y 
 
STREAM(file) 
N 
 
UNLOCK(file) 
N 
 
 
Record Access 
Supported 
 
ADD(file) 
Y 
 
ADD(file, length) 
N 
 
APPEND(file) 
Y 
 
APPEND(file, length) 
N 
 
DELETE(file) 
Y 
 
GET(file,key) 
Y 
 
GET(file, filepointer) 
N 
 
GET(file, filepointer, length) 
N 
 
GET(key, keypointer) 
N 
 
HOLD(file) 
N 
 
NEXT(file) 
Y 


---

Database Drivers and Interfaces 
241 
 
NOMEMO(file) 
N 
 
PREVIOUS(file) 
Y 
 
PUT(file) 
Y 
 
PUT(file, filepointer) 
N 
 
PUT(file, filepointer, length) 
N 
 
RELEASE(file) 
N 
 
REGET(file,string) 
N 
 
REGET(key,string) 
Y 
 
RESET(file,string) 
N 
 
RESET(key,string) 
Y 
 
SET(file) 
Y 
 
SET(file, key) 
N 
 
SET(file, filepointer) 
N 
 
SET(key) 
Y 
 
SET(key, key) 
Y 
 
SET(key, keypointer) 
N 
 
SET(key, key, filepointer) 
N 
 
SKIP(file, count) 
Y 
 
WATCH(file) 
Y 
 
 
Transaction Processing 
Supported 
 
LOGOUT(timeout, file, ..., file) 
Y4 
 
## COMMIT
Y 
 
## ROLLBACK
Y 
 
 
Null Data Processing 
Supported 
 
NULL(field) 
Y 
 
SETNULL(field) 
Y 
 
SETNULL(file,field) 
Y 


---

Database Drivers 
242 
 
SETNONNULL(field) 
Y 
Notes 
1      We recommend using a variable password that is lengthy and contains special characters 
because this more effectively hides the password value from anyone looking for it. For 
example, a password like "dd....#$...*&" is much more difficult to "find" than a password 
like "SALARY." 
{bmc TipBox.BMP}  
To specify a variable instead of the actual password in the Owner Name field of the 
File Properties dialog, type an exclamation point (!) followed by the variable name. 
For example: !MyPassword. 
2      See also PROP:LOGOUT in the Language Reference. 
3      BUILD(index) sets internal driver flags to guarantee the driver generates the correct 
ORDER BY clause. The driver does not call the backend server. 
4      Whether LOGOUT also LOCKs the table depends on the server's configuration for 
transaction processing. See your server documentation. 
 


---

Database Drivers and Interfaces 
243 
MSSQL Accelerator Synchronizer Server 
Clarion's Enterprise Edition includes the MSSQL Synchronizer Server and the Data Dictionary 
Synchronizer. The Dictionary Synchronizer uses the Synchronizer Server to gather complete 
information about an MSSQL database. 
The MSSQL Synchronizer Server is one of several used by the Dictionary Synchronizer. All the 
common behavior of all the SQL Accelerators is documented in the SQL accelerators section. All 
behavior specific to this driver is noted here. 
 MSSQL Accelerator Synchronizer Login Dialog 
Clarion's Dictionary Synchronizer Wizard (Enterprise Edition) lets you import an entire MSSQL 
database definition into your Clarion Data Dictionary in a single pass. During this process, the 
Synchronizer Wizard opens an MSSQL login dialog. This dialog collects the connection 
information for the MSSQL database. 
  
If you are using a Trusted Connection (Integrated NT Security), you must establish a 
connection to the NT workstation running the MSSQL Server before you can connect to 
the MSSQL database and import table definitions. You  can verify your connection by 
running the MSSQL ISQL_w Server utility installed with your MSSQL Client software. 
Fill in the following fields in the login dialog: 
Host 
Select the workstation running the MSSQL database to import from. If 
the Host list is empty, you may type in the name. See your DBA or 
network administrator for information on how the host is specified. 
Database 
Select the MSSQL database that contains the tables or views to 
import. If the Database list is empty, you may type in the name. See 
your server documentation or your DBA for information on database 
names. 
Username 
For Standard Security, type your MSSQL Username. For Trusted 
Security (Integrated NT Security) no Username is required. See your 
server documentation or your DBA for information on applicable 
Usernames and security methods. 
Password 
For Standard Security, type your MSSQL Password. For Trusted 
Security (Integrated NT Security) no Password is required. See your 
server documentation or your DBA for information on applicable 
Passwords and security methods. 
Include 
System Files 
Select this option to include system tables in the list of importable 
objects. 
Exclude 
System Files 
Select this option to exclude system tables from the list of importable 
objects. 
Other Filter 
Select this option to provide a filter expression to limit the list of tables 
and views to import. The filter expression queries the dbo.sysobjects 
table. The filter expression is limited to 1024 characters in length. 
 
  
The filter is case sensitive, so type your filter value accordingly. 


---

Database Drivers 
244 
Following is a list of the column names (and their Clarion datatypes) you can reference in your 
filter expression. Generally, filtering on MSSQL system tables requires not only an intimate 
knowledge of the MSSQL system tables, but also of the MSSQL stored procedures. For example, 
to filter on table owner: 
    uid = user_id('DBO') 
See your SQL server documentation for information on the MSSQL system tables and stored 
procedures. 
 
name 
## CSTRING(31)
id 
## LONG
uid 
## SHORT
type 
## STRING(2)
userstat 
## SHORT
sysstat 
## SHORT
indexdel 
## SHORT
schema_ver 
## SHORT
refdate 
## STRING(8)
crdate 
## STRING(8)
version 
## LONG
deltrig 
## LONG
instrig 
## LONG
updtrig 
## LONG
seltrig 
## LONG
category 
## LONG
cache 
## SHORT
 
 


---

Database Drivers and Interfaces 
245 
ODBC Accelerator Driver 
 
ODBC:Overview 
The ODBC Acclerator Driver is one of several SoftVelocity SQL Accelerator drivers. These SQL 
Drivers share a common code base and many common features such as SoftVelocity's unique, 
high speed buffering technology, common driver strings, and SQL logging capability. See SQL 
Accelerator Drivers for information on these common features. 
The ODBC Accelerator Driver converts standard Clarion file I/O statements and function calls into 
optimized SQL statements, which it sends to the backend SQL server for processing. This means 
you can use the same Clarion code to access both SQL tables and other file systems such as 
TopSpeed files. It also means you can use Clarion template generated code with your SQL 
databases. 
The ODBC Accelerator Driver is slightly different from the other SQL drivers in that it is a generic 
SQL driver. It is not specific to a particular SQL server, but, in fact, works with any database or 
file system that supports the ODBC standard. This includes SQL systems such as AS400, 
Informix, MSSQL, Oracle, Scalable SQL, SQL Anywhere, Sybase, and many non-SQL systems 
as well (dBase, Excel, FoxPro, etc.). This chapter describes special issues and considerations 
that arise when using the ODBC Accelerator Driver to access data. 
All the common behavior of all the SQL Accelerator drivers is documented in the SQL Accelerator 
Drivers chapter. All behavior specific to the ODBC driver is noted in this chapter. 
 
  
Make sure you have the latest ODBC drivers from your database server provider, as well 
as the end users of your applications. 
 
What is ODBC? 
ODBC (Open DataBase Connectivity) is a Windows "strategic interface" for accessing data from 
a variety of Relational Database Management Systems (RDBMS) across a variety of networks 
and platforms. 
The ODBC standard was developed and is maintained by Microsoft, which publishes an ODBC 
Software Development Kit (SDK), geared for use with its Visual C++ product. ODBC support is 
another way in which Clarion provides an extensible platform for you to create applications. 
Over the years Microsoft has modified what they call ODBC. It used to be that you would first 
download their ODBC manager. Next, you would download and install any database specific 
ODBC drivers that you need. 
Recently, many different layers of database software have surfaced. You can find ADO, RDO, 
OLE DB, and many more. Microsoft has merged all of these technologies into one complete 
installation package called MDAC (Microsoft Data Access Components). Basically it consists of 
several components that provide various database technologies; including ODBC. MDAC is a 
royalty-free redistributable package that you can install on any Windows machine without cost. 
 


---

Database Drivers 
246 
ODBC Pros and Cons 
 
Using ODBC offers the following advantages: 
• 
ODBC is an excellent choice in a Client-Server environment, especially if the Server is a 
native Structured Query Language (SQL) DBMS. It lets you add Client-Server support to 
your application, without having to do much more than choose a file driver. ODBC was 
specifically designed to create a non-vendor-specific method of connecting front end 
applications to back end services. With ODBC, the Server can handle much of the work, 
especially for SQL JOIN and PROJECT operations, thereby speeding up your 
application. 
• 
Existing ODBC drivers cover a great many types of databases. There are ODBC drivers 
available for databases for which Clarion may not have a native driver--for example, for 
Microsoft Excel and Lotus Notes files. 
• 
ODBC is already widespread. Major application suites such as Microsoft Office install 
ODBC drivers for file formats such as dBase and Microsoft Access. Keep in mind that 
many ODBC back end drivers have been updated and you should obtain the latest 
releases. 
• 
ODBC is platform independent. One of Microsoft's prime objectives in establishing ODBC 
was to support easier access to legacy systems, or corporate environments where data 
resides on diverse platforms or multiple DBMS's. As long as an ODBC driver and back 
end are available, it doesn't matter whether you use Microsoft's NetBEUI, SPX/IPX, 
DECNet or others; your application can connect to the DBMS and access the data. 
Given that there are many drivers available, and that the standard was developed by the 
company that developed Windows, you might consider using ODBC as the driver of choice for all 
your Windows applications. Yet, when deciding whether to use an ODBC driver or a Clarion 
native database driver, you must also consider possible disadvantages: 
• 
ODBC adds a layer--the ODBC Driver Manager--between your application and the 
database. When accessing files on a local hard drive, this generally results in slower 
performance. The driver manager must translate the application's ODBC API call to an 
SQL statement before any data access occurs. 
• 
ODBC uses SQL to communicate with the back end database. Although this can be very 
efficient when communicating with Client/Server database engines, it is normally less 
efficient than direct record access when using a file system designed around single 
record access, such as xBase or Btrieve. 
• 
The information required by the ODBC database manager to connect to a data source 
varies from one ODBC driver to another. Unlike the selection of Clarion file drivers, where 
file operations are virtually transparent, you may need to do some work to gather the 
information required to use a particular ODBC driver. This chapter provides a few tips 
that might make it easier. 
• 
ODBC is not included with Windows. When distributing your application, you'll need to 
install MDAC (Microsoft Data Access Components) into the end user's system, available 
for download at Microsoft’s web site. 
Given the pros and cons, we recommend using the native Clarion file drivers when both a native 
driver and an ODBC driver exist for the same file format. 
 


---

Database Drivers and Interfaces 
247 
How ODBC Works 
 
When you use ODBC to access data, four components must cooperate to make it work: 
1. Your application calls the ODBC driver manager, and sends it the appropriate requests 
for data, with the ODBC API. 
Clarion does this for you transparently, using the CLAODBX.DLL (32-bit) application 
extension. When hand-coding, be sure to include this library in the project. When 
distributing your application, be sure to deploy this file with your .EXE file (unless you 
produce a one-piece .EXE). 
2. The ODBC driver manager receives the API calls, check the Windows Registry for 
information on the data source, then loads the ODBC "back-end" driver. 
The actual "interface" to the driver manager is a file called ODBC32.DLL, which the 
Microsoft setup program places in the \Windows\System directory. This is the ODBC 
Administrator, which then loads other libraries to do its work. 
3. The ODBC "backend" driver is another library (.DLL) which contains the executable code 
for accessing the data. 
Various third-parties supply "backend" drivers. For example, Lotus Development Corp. 
supplies the ODBC driver for Lotus Notes. Microsoft Office distributes an ODBC SDK 
containing drivers for most of their database products. 
4. The data source is either a data file (usually when ODBC is used for local data access), 
or a remote DBMS, such as an Oracle database. 
The data source has a descriptive name; for example, "Microsoft Access Databases." 
The name serves as the section name in the ODBC.INI file. 
The ODBC driver manager must know the exact data source name so that it can load the 
right driver to access the data. Therefore, it's vitally important that you know the precise 
data source name.  
 


---

Database Drivers 
248 
ODBC Data Types 
 
 
Notes: 
C 
The Clarion data type can be used to manipulate the ODBC data type. CREATE does create 
the ODBC data type.  
• 
The Clarion type can be used to manipulate the ODBC data type, however, CREATE does 
NOT create the ODBC data type.  
1 
Clarion LONG, SHORT, and BYTE can be used with ODBC DECIMAL and NUMERIC data 
types if the ODBC field does not have any decimal places.  
2 
ODBC TIMESTAMP fields can be manipulated using a STRING(8) followed by a GROUP 
over it which contains only a DATE field and a TIME field. 
Example: 
  TimeStampField STRING(8),NAME('TimeStampField') 
  TimeStampGroup GROUP,OVER(TimeStampField) 
  TimeStampDate   DATE 
  TimeStampTime   TIME 
                 END 
CREATE creates a TIMESTAMP field if you use a similar structure. 
3 
Some loss of precision may occur. 
4 
Rounding errors may occur. 


---

Database Drivers and Interfaces 
249 
5 
CREATE attempts to create a TINYINT for a BYTE. If the backend does not support 
TINYINT, CREATE treats BYTE as a SHORT. CREATE attempts to create a SMALLINT for a 
SHORT. If the backend does not support SMALLINT, CREATE treats SHORT as a LONG. 
CREATE attempts to create an INTEGER for a LONG. If the backend does not support 
INTEGER, CREATE creates a decimal field. 
 
 
Your backend database may contain data types that are not listed here. These data types 
are converted to ODBC data types by the backend database. Consult your backend 
database documentation to determine which ODBC data type is used. 
 
 


---

Database Drivers 
250 
Importing from ODBC Data Sources 
Clarion's Dictionary Editor Import Wizard lets you import table definitions into your Clarion Data 
Dictionary. 
When you select the ODBC Accelerator Driver from the driver drop-down list, the Import Wizard 
opens the Data Sources dialog. Select an existing Data Source, then press the Next button to 
import its definition. 
If the data source is not defined, you can add it by pressing the New button, then following the 
ODBC instructions provided by the file system you wish to access.  
When you have selected a data source, press the Next button to import its definition. This imports 
the ODBC table definition and opens the File Properties dialog, allowing you to modify file 
attributes if needed. 
 


---

Database Drivers and Interfaces 
251 
ODBC Driver Configuration--Table Properties 
 
Typically, you add SQL support to your application by importing the SQL or ODBC table, view, 
and synonym definitions into your Clarion Data Dictionary. The Import Wizard automatically fills in 
the Table Properties dialog with default values based on the imported item. However, there are 
several prompts in the Table Properties dialog you can use to further configure the way the 
ODBC Accelerator Driver accesses the data. These Table Properties prompts, and their uses, are 
described below. 
Owner Name 
Typically, the Import Wizard places the SQL database connection information (Host, Username, 
Password, etc.) in the Owner Name field. 
Some backend databases may require additional connection information which you can supply in 
the Owner Name field. This information follows the password and is separated by semicolons, 
using the syntax: keyword=value;keyword=value. 
For example, when accessing a Sybase database with the ODBC driver, this would appear as: 
DataSource,UserID,PassWord,DATABASE=DataBaseName;APP=APPName 
Consult your appropriate SQL Server's documentation for information on these keywords, their 
uses and effects. 
 


---

Database Drivers 
252 
ODBC Column Configuration--Column Properties 
Typically, you add SQL support to your application by importing the SQL or ODBC table, view, 
and synonym definitions into your Clarion Data Dictionary. The Import Wizard automatically fills in 
the Column Properties dialog with default values based on the imported item. However, there are 
some special switches in the Column Properties dialog you can use to further configure the way 
the SQL Accelerator Driver accesses the data. These Column Properties switches are described 
below. 
  
When adding attributes to the External Name feature, make sure to separate the column 
name from the appropriate switch (i.e., columnname | switch). The spaces separating each 
value are required. These switches are also case sensitive. 
External Name 
## | BINARY
Adding the BINARY switch to the External Name tells the ODBC driver to store the data 
in binary format.  This is useful when storing images or non-printable characters.  Valid 
only with STRING data types. 
## | NOWHERE
Adding the NOWHERE switch to the External Name tells the ODBC driver to exclude the 
field from any WHERE clauses it sends to the backend server. This is necessary for 
certain backends when WATCH is in effect. Some backends do not allow certain data 
types in a where clause, but they fail to advise the ODBC Accelerator Driver of this 
restriction. The NOWHERE switch lets you manually advise of the restriction when 
WATCH causes the ODBC driver to generate. 
## | READONLY
Adding the READONLY switch to the External Name tells the ODBC driver not to insert 
the field when the record is added OR updated. This is necessary for certain back ends 
that do not allow auto incrementing key fields to be set to null. Some back ends do not 
allow auto incrementing key fields to be set to null, but they fail to advise the ODBC 
Accelerator Driver of this restriction. The READONLY switch lets you manually advise of 
the restriction. 
## | UNICODE
Adding the UNICODE switch to the External Name tells the ODBC driver to treat the 
data in the field as Unicode.  The CREATE statement will attempt to create the row as a 
Unicode row.  All data retrieval and storage commands will treat the contents of the field 
as Unicode data.  See the UNICODE driver string for more details.  This switch is only 
valid for STRING fields and is ignored for fields with other data types. 
## | WRITABLE
Adding the WRITABLE switch to the External Name tells the ODBC driver to insert the 
field when the record is added OR updated. This allows you to force the driver to write 
data even when the backend advises the ODBC Accelerator Driver that data cannot be 
written to this field. 
## | ZERONOTNULL
Adding the ZERONOTNULL switch to the External Name tells the ODBC driver to not 
set the field to NULL when the value is zero. the data in binary format.  This is useful 
when you need to store midnight for time or a zero date.  Valid only with DATE, TIME and 
TimeStamp data types. 
 
 


---

Database Drivers and Interfaces 
253 
ODBC Key Configuration--Key Properties 
Typically, you add SQL support to your application by importing the SQL or ODBC table, view, 
and synonym definitions into your Clarion Data Dictionary. The Import Wizard automatically fills in 
the Key Properties dialog with default values based on the imported item.  
There are no special switches or attributes available for the ODBC Key Properties. 


---

Database Drivers 
254 
Debugging Your ODBC Application 
 
When you use the ODBC Accelerator Driver, the ODBC Administrator can create a log file 
documenting all calls made by the ODBC Accelerator Driver. It includes the actual SQL 
statements made by the ODBC driver to the data source, and includes any errors posted. This 
administrator logging slows down your program considerably, so it should only be activated 
during testing. Additionally, the log file can grow to large proportions very quickly, so you should 
turn logging off and delete the log file after using it. 
Besides "snooping" on the actual SQL statements generated by the driver, you can zero in on 
any errors. For example, if the application is unable to connect, you can open the log file, scroll to 
the bottom of the file, then work up until you find the word "SQLError."  
See Microsoft's ODBC documentation (ODBCINST.HLP--ODBC Options Dialog Box) for 
instructions on using the ODBC Administrator logs. 
 
ODBC:Driver Strings 
There are switches or "driver strings" you can set to control the way your application creates, 
reads, and writes files with a specific driver. Driver strings are simply messages or parameters 
that are sent to the file driver at run-time to control its behavior. See Common Driver Features--
Driver Strings for an overview of these runtime Database Driver switches and parameters. 
 
 
A forward slash preceeds all SQL driver strings. The slash allows the driver to distinguish 
between driver strings and SQL statements sent with the SEND function. 
There are no Driver Strings specific to ODBC, the ODBC Accelerator Driver supports all the SQL 
Accelerator Driver Strings. 
See Also: SQL Accelerator Driver Strings . 
 
ODBC:Driver Properties 
 
There are no driver properties specific to ODBC, the ODBC Accelerator Driver supports all the 
SQL Accelerator Driver properties.  
See Also: SQL Accelerator Driver Properties 


---

Database Drivers and Interfaces 
255 
ODBC:Supported Commands and Attributes 
 
 
File Attributes 
Supported 
 
## CREATE
Y 
 
DRIVER(filetype [,driver string]) 
Y 
 
## NAME
Y 
 
## ENCRYPT
N 
 
OWNER(password) 
Y2 
 
## RECLAIM
N 
 
PRE(prefix) 
Y 
 
## BINDABLE
Y 
 
## THREAD
Y6 
 
EXTERNAL(member) 
Y 
 
DLL([flag]) 
Y 
 
OEM 
N3 
 
## LOCALE
N 
 
File Structures 
Supported 
 
## INDEX
Y3 
 
KEY 
Y3 
 
## MEMO
N 
 
## BLOB
Y 
 
## RECORD
Y 
 
 
Index, Key, Memo Attributes 
Supported 
 
## BINARY
N7 
 
DUP 
Y 
 
## NOCASE
Y 
 
OPT 
N 
 
## PRIMARY
Y 


---

Database Drivers 
256 
 
## NAME
Y 
 
Ascending Components 
Y 
 
Descending Components 
Y 
 
Mixed Components 
Y 
 
 
Field Attributes 
Supported 
 
DIM 
N 
 
## OVER
Y 
 
## NAME
Y 
 
 
File Procedures 
Supported 
 
BOF(file) 
N 
 
BUFFER(file) 
Y 
 
BUILD(file) 
Y 
 
BUILD(key) 
Y 
 
BUILD(index) 
Y8 
 
BUILD(index, components) 
Y8 
 
BUILD(index, components, filter) 
N 
 
BYTES(file) 
Y 
 
CLOSE(file) 
Y 
 
COPY(file, new file) 
N 
 
CREATE(file) 
Y 
 
DUPLICATE(file) 
Y 
 
DUPLICATE(key) 
Y 
 
EMPTY(file) 
Y 
 
EOF(file) 
N 
 
FLUSH(file) 
N 
 
LOCK(file) 
N 
 
NAME(label) 
Y 


---

Database Drivers and Interfaces 
257 
 
OPEN(file, access mode) 
Y 
 
PACK(file) 
N 
 
POINTER(file) 
N 
 
POINTER(key) 
N 
 
POSITION(file) 
N 
 
POSITION(key) 
Y 
 
RECORDS(file) 
Y 
 
RECORDS(key) 
Y 
 
REMOVE(file) 
Y 
 
RENAME(file, new file) 
N 
 
SEND(file, message) 
Y 
 
SHARE(file, access mode) 
Y 
 
STATUS(file) 
Y 
 
STREAM(file) 
N 
 
UNLOCK(file) 
N 
 
 
Record Access 
Supported 
 
ADD(file) 
Y 
 
ADD(file, length) 
N 
 
APPEND(file) 
Y 
 
APPEND(file, length) 
N 
 
DELETE(file) 
Y 
 
GET(file,key) 
Y 
 
GET(file, filepointer) 
N 
 
GET(file, filepointer, length) 
N 
 
GET(key, keypointer) 
N 
 
HOLD(file) 
N 
 
NEXT(file) 
Y 
 
NOMEMO(file) 
N 


---

Database Drivers 
258 
 
PREVIOUS(file) 
Y4 
 
PUT(file) 
Y 
 
PUT(file, filepointer) 
N 
 
PUT(file, filepointer, length) 
N 
 
RELEASE(file) 
N 
 
REGET(file,string) 
N 
 
REGET(key,string) 
Y 
 
RESET(file,string) 
N 
 
RESET(key,string) 
Y 
 
SET(file) 
Y4  
 
SET(file, key) 
N 
 
SET(file, filepointer) 
N 
 
SET(key) 
Y 
 
SET(key, key) 
Y 
 
SET(key, keypointer) 
N 
 
SET(key, key, filepointer) 
N 
 
SKIP(file, count) 
Y 
 
WATCH(file) 
Y 
 
 
Transaction Processing 
Supported 
 
LOGOUT(timeout, file, ..., file) 
Y9 
 
## COMMIT
Y 
 
## ROLLBACK
Y 
 
 
Null Data Processing 
Supported 
 
NULL(field) 
Y 
 
SETNULL(field) 
Y 
 
SETNULL(file,field) 
Y 
 
SETNONNULL(field) 
Y 


---

Database Drivers and Interfaces 
259 
Notes 
1      The Clarion ODBC file driver supports the listed items, however, the underlying file 
system may not support all of these items. 
2      We recommend using a variable password that is lengthy and contains special characters 
because this more effectively hides the password value from anyone looking for it. For 
example, a password like "dd....#$...*&" is much more difficult to "find" than a password 
like "SALARY." 
 
 
To specify a variable instead of the actual password in the Owner Name field of the 
File Properties dialog, type an exclamation point (!) followed by the variable name. 
For example: !MyPassword. 
3      International sorting is assumed to be done by the underlying file system. As such the 
OEM attribute and the .ENV file are ignored. 
4      PREVIOUS is not supported in file order. 
5      See also PROP:Logout in the Language Reference. 
6      THREADed files do not consume additional file handles for each thread that accesses the 
file. 
7      BUILD(index) sets internal driver flags to guarantee the driver generates the correct 
ORDER BY clause. The driver does not call the backend server. 
8      Whether LOGOUT also LOCKs the table depends on the server's configuration for 
transaction processing. See your server documentation.. 
 
Microsoft Access and ODBC 
ODBC Driver that ships with Access 2.0 
The ODBC driver that ships with Access 2.0 only works with other Microsoft Office applets. To get 
a general purpose driver that works with the Clarion ODCB Accelerator Driver, you need to 
purchase the ODBC Desktop Driver Kit 2.0 from Microsoft. 
 
ODBC Caveats 
Attempting to access some ODBC commands during a DLL unload phase may cause ODBC to 
crash. Any destructor of a global object is called during the DLL unload phase. 
Therefore you cannot perform any commands that will cause the file drivers to access the ODBC 
API inside destructors of global objects. 
 
  
This ODBC limitation does not apply to Windows Vista. 
 


---

Database Drivers 
260 
Oracle Accelerator 
 
Oracle Accelerator Overview 
Oracle Server 
For complete information on the Oracle database system, please refer to your Oracle 
documentation. 
Oracle Accelerator 
Oracle Accelerator is one of several SoftVelocity SQL Accelerators. These SQL drivers share a 
common code base and many common features such as SoftVelocity's unique, high speed 
buffering technology, common driver strings, and SQL logging capability. See SQL Accelerators 
for information on these common features. 
The Oracle Accelerator converts standard Clarion file I/O statements and function calls into 
optimized SQL statements, which it sends to the backend Oracle server for processing. This 
means you can use the same Clarion code to access both Oracle tables and other file systems 
such as TopSpeed files. It also means you can use Clarion template generated code with your 
SQL databases. 
All the common behavior of all the SQL Accelerators is documented in the SQL Accelerators 
section. All behavior specific to this driver is noted here. 
SoftVelocity's Oracle Accelerator automatically works with Oracle versions 7.0 and higher. At 
runtime, the driver initially tries to load the latest Oracle Client DLLs. If they are not available, it 
tries to load earlier versions. 
 
 
Personal Oracle 8.0 and higher only works with 32-bit programs.  


---

Database Drivers and Interfaces 
261 
Oracle Accelerator System Requirements 
Hardware 
You can run the Clarion development environment on any system that meets the minimum 
system requirements for Microsoft Windows (all versions). 
Software 
To develop Windows programs with Oracle Accelerator, you must have Oracle version 7.0 or 
higher. 
The minimum configuration is to install the Oracle Instant client, which would contain the following 
DLLs: 
## OCI.DLL
oracnnzsbb11.dll 
oraociicus11.dll 
These files reference version 11. One other file is required if you are using non-Western 
languages. 
These .DLLs must be in a directory that is in your system PATH. 
You will not be able to define or import Oracle files in your Clarion data dictionary until the 
Oracle DLLs are installed in a directory that is in your system PATH. 
 
The Oracle driver requires that you have a valid Oracle client installed on both the development 
and user machines. Oracle clients come in two versions: a regular client and an "Instant" client. 
The regular client supports TNSNAMES (see Oracle documentation). The Instant client requires 
you to specify full connection parameters to the Oracle server (IP address, Port, SID (Server ID)), 
but is much smaller and easier to deploy. 
 


---

Database Drivers 
262 
Oracle Accelerator Installation 
To install the Oracle Accelerator file driver: 
1. 
Install the required Oracle components. 
See System Requirements--Software. 
2. 
Run A:SETUP where A: is the drive letter of the drive containing the Oracle Accelerator 
install disk. 
Follow the instructions on your screen. Install Oracle Accelerator to the directory that 
already contains Clarion. 
The setup program installs Oracle Accelerator according to your selections. When 
everything is installed, the setup program offers to open the Oracle Accelerator on-line 
help file. This file contains late breaking information about the Oracle Accelerator file 
driver. 
3. 
Please read the late breaking information. 
When you have finished reading, close the file. 
4. 
Register the Oracle Accelerator driver with the Clarion development environment. 
 
 
Registering the Oracle Accelerator 
You must register the Oracle Accelerator driver with the Clarion development environment before 
you can use it. 
To register Oracle Accelerator: 
1. 
Start the Clarion development environment. 
2. 
Choose Setup  Database Driver Registry. 
3. 
Press the Add button. 
4. 
Highlight CLAORA.DLL (by default, in the ..\BIN directory) in the list box, then press the 
OK button. This registers the Oracle Accelerator driver. 
5. 
Press the OK button. 


---

Database Drivers and Interfaces 
263 
Oracle Accelerator Table Import Wizard--Login Dialog 
Clarion's Dictionary Editor Import Wizard lets you import Oracle table definitions into your Clarion 
Data Dictionary. When you select the Oracle Accelerator from the driver drop-down list, the 
Import Wizard opens the Login/Connection dialog. The Login/Connection dialog collects the 
connection information for the Oracle database. 
Notes: 
1. 
Before you can connect to the SQL database and import table definitions, the 
database must be started and must be accessible from your computer. 
 
2. 
Only those indexes directly associated with the table as CONSTRAINTs are 
imported by the Oracle Accelerator driver. If you need more indexes, simply define 
them manually. 
 
3. 
If the Oracle database INDEX flag is set to OFF, the Oracle Accelerator Import 
Wizard does not import CONSTRAINTS. 
Fill in the following fields in the Login/Connection dialog: 
Host 
Select the Oracle host that contains the tables or views to import. If the 
Host list is empty, you may type in the host (a blank host specifies the 
Oracle 8 Personal database). See your DBA or network administrator for 
information on how the host is specified. For example, type 2: to connect to 
the local Personal  Oracle (7.2 and earlier) database. X: prefixes an IPX 
host and TNS: prefixes a TCP/IP host. For Personal Oracle 8, leave the 
Host field blank. 
Username 
Type your Oracle Username. See your server documentation or your DBA 
for information on applicable Usernames. 
Password 
Type your Oracle Password. See your server documentation or your DBA 
for information on applicable Passwords. 
Optionally, you type a complete connect string in the Username field using either of the following 
syntaxes: 
 
username/password@Protocol:dbname 
or 
 
username@Protocol:dbname,password 
For example, type: 
 
scott/tiger@2:production1 
 
in the Username field. Or, you may type just your username and the database name in the 
Username field, and type your password in the Password field.  
For example, type: 
scott@2:production1 
in the Username field, then type 
tiger 
in the Password field. The Import Wizard displays the password as a series of asterisks. See 
your Oracle documentation for more information on Oracle connect string syntax. 
 
 


---

Database Drivers 
264 
Filter 
Optionally, provide a filter expression to limit the list of tables and views to 
import. The filter expression queries the ALL_CATALOG view. For 
example the filter: OWNER='SCOTT' returns only the tables which have 
SCOTT as the OWNER. . The filter expression is limited to 1024 
characters in length. 
  
The filter is case sensitive, so type your filter value accordingly. 
Following is a list of the ALL_CATALOG column names (and their Clarion datatypes) you can 
reference in your filter expression. See your Oracle documentation for more in formation on these 
columns. 
## OWNER
## CSTRING(31)
## TABLE_NAME
## CSTRING(31)
## TABLE_TYPE
## CSTRING(12)
 
Next > 
Press this button to open the Import Wizard's Import List dialog. 
 
Oracle Accelerator Table Import Wizard--Import List 
Dialog 
When you press the Next > button, the Import Wizard opens the Import List dialog. The Import 
List dialog lists the importable items. 
Highlight the table, view, or synonym whose definition you wish to import, then press the Finish 
button to import. The Import Wizard adds the definition to your Clarion Data Dictionary, then 
opens the File Properties dialog to let you modify the imported definition. 
Import additional tables by repeating these steps. After all the items are imported, return to the 
Dictionary Editor where you can define relationships and delete any columns not used in your 
Clarion application. See SQL Accelerators--Define Only the Fields You Use. 
  
You can use the Enterprise Edition Dictionary Synchronizer to import an entire database, 
including relationships, in a single pass. 


---

Database Drivers and Interfaces 
265 
Oracle Accelerator Performance Considerations 
See SQL Accelerators--Performance Considerations for more information on performances 
issues common to all SQL Accelerators, including Oracle Accelerator. 
 
Oracle Accelerator Automatic Login Dialog 
The Oracle Accelerator Login dialog lets the user specify Username, Password and Database. 
In the Database drop-down list, select from previously selected Oracle hosts. The list of 
previously entered databases as well as the last UserID is stored in the Windows registry in the 
HKEY_CURRENT_USER/Software/SoftVelocity/Oracle tree as follows: 
/Software/SoftVelocity/Oracle/UserID    the last UserID 
/Software/SoftVelocity/Oracle/HostMRU   the last selected database 
/Software/SoftVelocity/Oracle/HostCount number of databases in the list 
/Software/SoftVelocity/Oracle/Host1     database name 
/Software/SoftVelocity/Oracle/Host2     database name 
/Software/SoftVelocity/Oracle/Hostn     database name 
If the Database list is empty, you may simply type in the database name. For example, type 2: to 
connect to the local Personal database. The 2: indicates a local host; X: indicates an IPX host 
and TNS: indicates a TCP/IP host. 
Alternatively, you may also supply a connect string (containing the database name) in the 
Username field. The Oracle connect string syntax is: 
username/password@Protocol:dbname 
or 
username@Protocol:dbname,password 
See your Oracle documentation for more information on Oracle connect string syntax. 
If the Username field is not long enough, you may continue the entry in the Password field, 
because the Oracle Accelerator driver simply concatenates these fields and forwards their 
contents to the Oracle server. 


---

Database Drivers 
266 
Oracle Accelerator Generating Unique Key Values 
For many database applications, you will want to automatically generate unique key values for 
your database records. An Oracle Sequence is simply a sequence number generator. You can 
select the next number from the Sequence whenever you add a new record.  
Generally, we recommend using Oracle Sequences whenever possible to generate your unique 
key values. Sequences are more efficient because you never get a clash, and you need only two 
(2) database calls to add your new record.  
Oracle Sequences: 
To use Oracle Sequences: 
1. 
Define an Oracle Sequence for the auto incremented key. 
See your Oracle documentation: 
 CREATE SEQUENCE GlobalSequence 
## INCREMENT BY 1
## START WITH 1
## NOMAXVALUE
## MINVALUE 1
## NOCYCLE
## CACHE 30;
 
2. 
Declare your Clarion file to use the Oracle Sequence like this: 
OracleFile FILE,DRIVER('Oracle', '/AUTOINC=SELECT Myseq.nextVal') 
## RECORD
SomeData     STRING 
autoIncFld   PDECIMAL(31) 
            END 
           END 
 
3. 
Use PROP:ServerAutoInc before adding your data to the file using normal Clarion or 
ABC syntax.  The file driver will automatically get the sequence number and store it in the 
appropriate field.: 
 
   OPEN(OracleFile) 
   OracleFile{PROP:ServerAutoInc, 2} = 1 !Set the 2nd field as the receiving 
field 
   OracleFile{PROP:ServerAutoInc} ! tell the driver that the next ADD needs 
auto-inc 
   ADD(OracleFile) 
   ! This will first put the nextval sequence value into  
   ! OracleFile.autoIncFld and then do a normal ADD call. 


---

Database Drivers and Interfaces 
267 
Oracle Accelerator Driver Strings 
There are switches or "driver strings" you can set to control the way your application creates, 
reads, and writes files with a specific driver. Driver strings are simply messages or parameters 
that are sent to the file driver at run-time to control its behavior.  See SQL Accelerators for more 
information on SQL driver strings. 
In addition to the common SQL Accelerator driver strings, Oracle Accelerator supports the 
following driver strings as well. 
 
## HINT
You can tell Oracle Accelerator to generate Oracle hints by using the HINT driver string, 
 DRIVER('Oracle','/HINT=hint') 
by using /HINT in the key name,  
 Key KEY(fieldlist),NAME('name /HINT=[&]hint') 
with SEND,  
 SendReturn = SEND (file,' /HINT=[&]hint') 
or with the PROP:Hint property,  
 file{PROP:Hint} = '[&]hint' 
 HintString = file{PROP:Hint} 
The square brackets [] above are used to show that the ampersand (&) is optional. 
You can either override the base hint or concatenate a hint. If the first character after the = in the 
KEY hint is an ampersand (&), Oracle Accelerator concatenates the hint onto the FILE hint, 
otherwise it overrides the FILE hint. 
If the first character after the = in the SEND hint is an ampersand (&) or the first character of a 
hint property is an ampersand, Oracle Accelerator concatenates the hint onto the current hint (the 
FILE hint and the KEY hint), otherwise it overrides the FILE and KEY hint. 
You can also use PROP:Hint to return the hint that is in use (or will be in use if called after a SET, 
but before the first NEXT or PREVIOUS statement.) 
Example: 
 AFile DRIVER('Oracle','/hint=COST') 
 AKey KEY(field),NAME('KeyName /HINT=&FIRST_ROWS') 
 SEND(AFile,'/HINT=FIRST_ROWS') 
 AFile{PROP:Hint} = 'FIRST ROWS' 
 
 


---

Database Drivers 
268 
## LOGON SCREEN
 
DRIVER('Oracle', '/LOGONSCREEN = TRUE | FALSE ' ) 
 
  
LOGONSCREEN sets the toggle that determines whether the driver automatically prompts for 
logon information. By default, the driver displays a logon window if no connect string is supplied. 
If set to FALSE and there is no connect string, an ERRORCODE of 90 is returned. 
The logon screen elements are contained within the file driver logic. 
The end-user's ability to use the connect dialog will depend on the security surrounding the 
Oracle database.  
 
## PERSONAL
The Personal Oracle 7.1 Server behaves differently than other Oracle servers. When using 
Personal Oracle 7.1 you should inform Oracle Accelerator so it can tailor the generated SQL 
especially for Personal Oracle 7.1. For example:  
 DRIVER ('Oracle','/PERSONAL') 
or 
 SEND (Myfile,'/PERSONAL') 
 
 
Notes: 
The /PERSONAL switch is not required for Personal Oracle 7.2 (Personal Oracle for 
Windows 95). 
Personal Oracle 8.0 only works with 32-bit programs. 
 
## USEASYNCHRONOUSCALLS
The Oracle driver supports reading ahead asynchronously using the BUFFER statement. This 
may give performance gains when using this variation of the BUFFER statement. For example, 
you may have a large report where you need to read a lot of records and do some client side 
processing. It would improve performance to use the BUFFER's read ahead facility to get data 
in at the same time you are processing it. However, to enable this feature, all other commands 
will run slower (become asynchronous). 
By default the asynchronous read ahead feature of the BUFFER statement is disabled. To 
enable this feature set /USEASYNCHRONOUSCALLS=TRUE 
 


---

Database Drivers and Interfaces 
269 
## WHERE
In addition to WHERE driver string supported by all the SQL Accelerator drivers, Oracle 
Accelerator supports the following special WHERE driver string. 
/Where in the FILE Definition 
When a FILE declaration references more than one Oracle table, you must tell the Oracle server 
which columns link the tables together. A /WHERE in the FILE definition specifies the connecting 
fields between two or more Oracle tables. For example: 
OrdBrowse FILE,DRIVER('ORACLE','/WHERE Orders.AccNum=Customer.AccNum'),| 
          NAME('Orders,Customer'),PRE(Orb),BINDABLE,THREAD 
 OrdbKey  KEY(-Orb:OrderNumber),NAME('OrdbKey'),PRIMARY 
 Record       RECORD,PRE() 
 OrderNumber   LONG,NAME('OrderNum') 
 AccountNumber LONG,NAME('Orders.AccNum') 
 ShipTo        STRING(32),NAME('ShipTo') 
 Name          STRING(31),NAME('Name') 
              END 
          END 
 
  
If you use the templates to generate your application, you will not need this technique. The 
templates automatically generate VIEWs when more than one table is referenced. 


---

Database Drivers 
270 
Oracle Accelerator Driver Properties 
You can use Clarion's property syntax to query and set certain Oracle Accelerator driver 
properties. See SQL Accelerators--SQL Accelerator Properties. 
 
 
 
Oracle Accelerator --Using Embedded SQL 
You can use Clarion's property syntax (PROP:SQL) to send SQL and PL/SQL statements to the 
Oracle server within the normal execution of your program. For backward compatibility, you can 
also use SEND to send SQL and PL/SQL statements; however, we recommend using the 
property syntax. 
See SQL Accelerators for more information on using embedded SQL. 
 
## PL/SQL
PL/SQL is Oracle's procedural language extension to Oracle's SQL language. Because PL/SQL 
statements are managed by the same engine that manages SQL statements, PL/SQL statements 
may be incorporated into your Clarion programs in the same manner as SQL statements. For 
example: 
 SQLFile     FILE,DRIVER('Oracle'),NAME(SalaryFile) 
 Record       RECORD 
 SalaryAmount  PDECIMAL(5,2),NAME('JOB') 
              END 
             END 
## CODE
  SqlFile{PROP:SQL} =                               | 
## 'DECLARE '                                      &|
     'TempPhoneArea clarionclient.PhoneArea%type; '&| 
     'CURSOR AreaCursor IS '                       &| 
       'SELECT PhoneArea  '                        &| 
      'FROM ClarionClient '                        &| 
      'WHERE PhoneArea = 305; '                    &| 
## 'BEGIN  '                                       &|
     'OPEN AreaCursor; '                           &| 
## 'LOOP '                                       &|
      'FETCH AreaCursor INTO TempPhoneArea; '      &| 
      'EXIT WHEN AreaCursor%NOTFOUND; '            &| 
       'UPDATE ClarionClient '                     &| 
      'SET PhoneArea = 954; '                      &| 
## 'END LOOP; '                                  &|
     'CLOSE AreaCursor; '                          &| 
## 'COMMIT WORK; '                               &|
## 'END;'
 


---

Database Drivers and Interfaces 
271 
Calling a Stored Procedure 
 
The Oracle driver can now call stored procedures and stored functions that return result sets. 
This feature is supported for Oracle 8 or later client versions. In addition, although you can use 
these clients to access older versions of the Oracle server, this feature is only supported with 
Server Version 7 or later. 
 
Example: 
file{PROP:SQL} = 'CALL GrantAccessProcedure' 
 
 
DLL Coding Practices 
Clarion applications that make use of DLLs must avoid calling certain file functions for Oracle 
tables in the constructors of static instances of classes declared in the EXE or DLLs, with the 
following exceptions: 
- NAME(File) 
- SEND(File, String) 
- File{PROP:xxx} (get and set) 
- Key{PROP:xxx} (get and set) 
This is complete list. Any attempt to call any other file function in the constructors of static 
instances of classes can cause an "Oracle could not be found" error on attempt to load the Oracle 
client-side DLL. 
ABC templates generate an instance of the DLLInitializer class for every DLL and provide embed 
points to enter custom code in the constructor. The constructor for the "data" DLL indirectly calls 
Init methods for every generated instance of the FileManager class. This method makes calls to 
the file functions from the list given above. Code entered in the provided embed points or added 
by 3rd party templates should not use calls to other file functions from DLLInitializer.Construct. 
 


---

Database Drivers 
272 
Oracle Accelerator Troubleshooting 
 Clarion Won't Accept Oracle File Driver 
Clarion's Dictionary Editor allows you to select the Oracle file driver only if Oracle is installed on 
your machine. That is, the Oracle DLLs must be installed in a directory in your path before 
Clarion's Dictionary Editor will recognize the Oracle driver. Attempting to run the Oracle example 
program will produce error windows that tell you which DLLs are missing. 
 Oracle Not Available (-1034) 
If you receive this error (Oracle error number -1034), make sure the Oracle server is properly 
installed and is available to the client. 
 Unable to allocate memory on user side (-1019) 
This message may indicate some of the required Oracle DLLs are not installed to a directory in 
your system path. See System Requirements--Software. 
 Unable to spawn new ORACLE (-9352) 
This message may indicate the Oracle database is not started. Start the Oracle database and 
retry. 
 Could Not Log On:Oracle Accelerator  
This message may indicate an invalid username, password, or servername. It may also indicate 
that the Oracle server is not installed or is otherwise not available. Make sure the Oracle server is 
properly installed and is available to the client. 
 Invalid Field Type Descriptor: Oracle Accelerator  
The Clarion error: Invalid Field Type Descriptor is generated at runtime if you supply a field name 
in the field's NAME attribute that does not match any field name in the Oracle table. By turning 
logging on (see /LOGFILE) you can re-run your program and receive a list of valid field names in 
the log file. Use the dictionary import facility to import the field descriptions into your Clarion data 
dictionary to avoid this problem. 
 Unexpected End of SQL Command (-921) 
If you receive this error (Oracle error number -921), make sure that the SQL Select statement 
selects the same number of columns as the receiving Clarion FILE structure declares. 
This error may also occur when a CREATE statement generates incorrect SQL statements when 
the last field is OVER a previous field. Change the file layout so the last field declared is not 
declared OVER a previous field. 
 File Not Found:Oracle Accelerator  
If you receive this error (or Oracle error number 942--Table or View Does Not Exist), check that 
the file name you are passing to the Oracle driver is valid. The most common occurrence of this 
error is when the name of the Oracle table is not correct. If the table is owned by another user, 
you must explicitly identify the owner as follows:  
owner.table 
 Error 47:Oracle Accelerator  
An Error 47 indicates there is a field defined in your Clarion data dictionary that does not exist on 
the Oracle server. To identify the field, use /LOGFILE. 


---

Database Drivers and Interfaces 
273 
 Internal Error 02: WSLDIAL:Oracle Accelerator  
Use the Project Editor dialog to add the ..\LIBSRC\ORALOON.RSC file to your application's 
Library, object and resource files. 
To add resource files to your project: 
1. 
From the Application Tree dialog, press the Project button. 
2. 
Highlight Library, object and resource files, then CLICK on the Add File button. 
3. 
Navigate to the ..\LIBSRC folder, then select the resource file (ORALOON.RSC) from the 
Windows File dialog. 
4. 
Press the OK button to return to the Project Editor dialog. 
 No Interface Driver Connected(-03121) 
This indicates you have not entered a correct database name. Be sure to enter the correct 
database name in the Host or Database field. 
Oracle could not be found 
See DLL Coding Practices  
 


---

Database Drivers 
274 
Oracle Accelerator Supported Commands and Attributes 
 
File Attributes 
Supported 
 
## CREATE
Y1 
 
DRIVER(filetype [,driver string]) 
Y 
 
## NAME
Y 
 
## ENCRYPT
N 
 
OWNER(password) 
Y 
 
## RECLAIM
N 
 
PRE(prefix) 
Y 
 
## BINDABLE
Y 
 
## THREAD
Y 
 
EXTERNAL(member) 
Y 
 
DLL([flag]) 
Y 
 
OEM 
Y2 
 
## LOCALE
N 
 
File Structures 
Supported 
 
## INDEX
Y 
 
KEY 
Y 
 
## MEMO
N 
 
## BLOB
Y 
 
## RECORD
Y 
 
 
Index, Key, Memo Attributes 
Supported 
 
## BINARY
N 
 
DUP 
Y 
 
## NOCASE
Y 
 
OPT 
Y 
 
## PRIMARY
Y 
 
## NAME
Y 


---

Database Drivers and Interfaces 
275 
 
Ascending Components 
Y 
 
Descending Components 
Y 
 
Mixed Components 
Y 
 
 
Field Attributes 
Supported 
 
DIM 
N 
 
## OVER
Y 
 
## NAME
Y 
 
 
File Procedures 
Supported 
 
BOF(file) 
N 
 
BUFFER(file) 
Y 
 
BUILD(file) 
Y 
 
BUILD(key) 
Y 
 
BUILD(index) 
Y3 
 
BUILD(index, components) 
Y3 
 
BUILD(index, components, filter) 
N 
 
BYTES(file) 
Y10 
 
CLOSE(file) 
Y 
 
COPY(file, new file) 
N 
 
CREATE(file) 
Y1 
 
DUPLICATE(file) 
Y 
 
DUPLICATE(key) 
Y 
 
EMPTY(file) 
Y 
 
EOF(file) 
N 
 
FLUSH(file) 
N 
 
LOCK(file) 
N 
 
NAME(label) 
Y 
 
OPEN(file, access mode) 
Y 


---

Database Drivers 
276 
 
PACK(file) 
N 
 
POINTER(file) 
N 
 
POINTER(key) 
N 
 
POSITION(file) 
Y14 
 
POSITION(key) 
Y11 
 
RECORDS(file) 
Y 
 
RECORDS(key) 
Y12 
 
REMOVE(file) 
Y 
 
RENAME(file, new file) 
N 
 
SEND(file, message) 
Y 
 
SHARE(file, access mode) 
Y 
 
STATUS(file) 
Y 
 
STREAM(file) 
N 
 
UNLOCK(file) 
N 
 
 
Record Access 
Supported 
 
ADD(file) 
Y 
 
ADD(file, length) 
N 
 
APPEND(file) 
Y4 
 
APPEND(file, length) 
N 
 
DELETE(file) 
Y 
 
GET(file,key) 
Y 
 
GET(file, filepointer) 
Y5 
 
GET(file, filepointer, length) 
N 
 
GET(key, keypointer) 
N 
 
HOLD(file) 
Y6 
 
NEXT(file) 
Y 
 
NOMEMO(file) 
N 
 
PREVIOUS(file) 
Y7 


---

Database Drivers and Interfaces 
277 
 
PUT(file) 
Y 
 
PUT(file, filepointer) 
N 
 
PUT(file, filepointer, length) 
N 
 
RELEASE(file) 
N 
 
REGET(file,string) 
Y8 
 
REGET(key,string) 
Y8 
 
RESET(file,string) 
N 
 
RESET(key,string) 
Y9 
 
SET(file) 
Y 
 
SET(file, key) 
N 
 
SET(file, filepointer) 
N 
 
SET(key) 
Y 
 
SET(key, key) 
Y 
 
SET(key, keypointer) 
N 
 
SET(key, key, keypointer) 
N 
 
SKIP(file, count) 
Y 
 
WATCH(file) 
Y 
 
 
Transaction Processing 
Supported 
 
LOGOUT(timeout, file, ..., file) 
Y 
 
## COMMIT
Y 
 
## ROLLBACK
Y 
 
 
Null Data Processing 
Supported 
 
NULL(field) 
Y 
 
SETNULL(field) 
Y13 
 
SETNULL(file,field) 
Y 
 
SETNONNULL(field) 
Y 
Notes 


---

Database Drivers 
278 
1          CREATE(file) does not work for every data type. See Supported Data Types for more 
information. 
2          Adding the OEM attribute causes the driver to generate calls to NLSSORT for string fields 
in a sort sequence (either key components or PROP:Order components). 
3          The BUILD(dynamic index) and BUILD(index) statements do not perform any disk action. 
They only initialize internal Oracle driver structures to track key order access and allow 
SELECT statements to be built when you issue SET(key) or SET(key,key) statements 
referencing the index. 
4          The APPEND statement behaves identically to the ADD statement, that is, keys are 
updated by the APPEND statement. 
5          The GET(file, filepointer) statement is unsupported for all values of filepointer except 
filepointer = 0. In this case, the record position is cleared and ERRORCODE 35 is 
returned. 
6          Apart from the holding records, the HOLD statement has another use. Normally, the driver 
will not reread the record when you execute a RESET/NEXT to the current record. 
Executing a HOLD statement before the RESET/NEXT forces the driver to reread the 
record from disk. 
7          You can't execute a PREVIOUS after a SET(file) statement. You can only examine the file 
in a forward order. 
8          The REGET statement only works if you have a unique key defined for the file 
9          The RESET(key,position)/NEXT(file) statement sequence is optimized to retrieve the 
record from the driver's internal buffer if the code is resetting to the current record. To 
force the driver to reread the record from disk, execute a HOLD statement before the 
RESET/NEXT sequence. This optimization is not in effect within a transaction frame. 
10        The BYTES(file) function returns the number of records in the file or the number of bytes 
in the last record accessed. Following an OPEN statement, the BYTES function returns 
the number of records in the file. After the file has been accessed by GET, NEXT, ADD, 
or PUT, the BYTES function returns the size of the last record accessed. 
11        The POSITION(key) function returns (1 + size of the key components + the size of the 
components of the file's primary key). This formula is true even if the first unique key is 
the same key you are positioning on. If no primary key is defined, then the first unique 
key is considered the primary key. 
If there is no unique key, POSITION(key) returns 1 + size of the key components. In this 
case RESET(key) will reposition to the first occurrence of the key value, since there is no 
way of uniquely identifying a record. Therefore, the RESET may position on a different 
record. 
12        The RECORDS(key) function returns the number of UNIQUE occurrences of the first 
element of the key. This is the same as doing an SQL statement of: 
SELECT COUNT ( DISTINCT key_field1) FROM table 
13        SETNULL(field) clears the contents of the field. 
14        The returned POSITION can only be used with REGET(file,position) and only for unique 
keys. 


---

Database Drivers and Interfaces 
279 
Oracle Accelerator Data Types 
The following table matches Clarion data types to their corresponding Oracle data types. 
  
Generally, you should not have to do any manual matching of data types. Rather, you 
simply import file definitions from your Oracle database into your Clarion data dictionary. 
The Oracle Accelerator driver automatically selects the proper data types (see Importing 
Oracle Files to a Data Dictionary). 
Oracle data type 
Clarion data type 
## CHAR
## STRING
## VARCHAR2
## CSTRING
## NUMBER
## REAL
NUMBER(n,p) 
## PDECIMAL
NUMBER(n,0) 
## BYTE1,SHORT2,USHORT3,LONG4
## LONG
## STRING+GROUP+SHORT5
## LONG RAW
## STRING+GROUP+SHORT5
## DATE
DATE or STRING+DATE+TIME6 
RAW 
## STRING
## ROWID
## STRING(18)
Data Type Notes: 
1          CREATE will create a NUMBER(3,0). 
2          CREATE will create a NUMBER(5,0). 
3          CREATE will create a NUMBER(5,0). 
4          CREATE will create a NUMBER(10,0). 
5          Clarion can access Oracle LONG and LONG RAW data types by using a STRING and a 
GROUP overlaying the STRING. The GROUP consists of a SHORT and a STRING. The 
SHORT holding the length of the total data (including the length of the SHORT). For 
example: 
 
Comments  STRING(1024),NAME('COMMENTS') !Oracle LONG field 
COMMENTS_GROUP  GROUP,OVER(Comments) 
## COMMENTS_LENGTH  USHORT
## COMMENTS_DATA    STRING(1022)
                END 
 
You cannot use the CREATE statement to create rows of type LONG or LONG RAW. 
6          Clarion can access Oracle DATE data types by using either a DATE or a STRING with a 
GROUP overlaying the STRING. 
If you use a Clarion DATE field, the TIME component of the field is not readable and is 
set to 0 when writing the field. You may use a CREATE statement to create the table. For 
example: 
 
StartDate    DATE,NAME('START_DATE')   !Oracle DATE field 
 


---

Database Drivers 
280 
If you use a Clarion STRING with an overlaid GROUP, the GROUP consists of a DATE 
and a TIME field. You may not use a CREATE statement to create the table. For 
example: 
 
OraDate   STRING(8),NAME('START_DATE') !Oracle DATE field 
StartDate_Group GROUP,OVER(OraDate) 
StartDate        DATE 
StartTime        TIME 
                END 
 
  
Your Clarion application should generally reference the DATE field (StartDate), and should 
not reference the STRING field (OraDate) or the GROUP field (StartDate_Group).  
However, if the Oracle date stamp is part of the key, you must include the STRING field 
(not the DATE field) as a key component in your Clarion data dictionary. 
7          Oracle ROWID data types are read and written as a STRING(18) of format 
BBBBBBBB.RRRR.FFFF. Where B, R, and F are hexadecimal numbers representing 
block, row, and file number respectively. See your Oracle documentation for more 
information. 
CREATE will not create a ROWID row. 


---

Database Drivers and Interfaces 
281 


---

Database Drivers 
282 
Pervasive SQL Accelerator Driver 
 
The Pervasive SQL Server 
For complete information on the Pervasive SQL database system, please review Pervasive 
Software's documentation. 
Pervasive SQL requires that the 16-bit ODBC support files are also installed. 
The Pervasive SQL Driver 
The Pervasive SQL Driver is one of several SoftVelocity SQL Accelerator drivers. These SQL 
Drivers share a common code base and many common features such as SoftVelocity's unique, 
high speed buffering technology, common driver strings, and SQL logging capability. See SQL 
Accelerator Drivers for information on these common features. 
The Pervasive SQL Driver converts standard Clarion file I/O statements and function calls into 
optimized SQL statements, which it sends to the backend Pervasive SQL server for processing. 
This means you can use the same Clarion code to access both Pervasive SQL tables and other 
file systems such as TopSpeed files. It also means you can use Clarion template generated code 
with your SQL databases. 
All the common behavior of all the SQL Accelerators is documented in the SQL Accelerators 
section.  The Pervasive SQL Driver is based on the ODBC Accelerator and inherits all features of 
the ODBC Accelerator.  All the common behavior of the SQL Accelerators that are derived from 
the ODBC Accelerator is documented in the ODBC Accelerator section.  All behavior specific to 
this driver is noted here. 
 
Pervasive SQL Import Wizard—Import List Dialog 
 
When you press the Next > button, the Import Wizard opens the Import List dialog. The Import 
List dialog lists the importable items. 
Highlight the table whose definition to import, then press the Finish button to import. The Import 
Wizard adds the definition to your Clarion Data Dictionary, then opens the File Properties dialog 
to let you modify the default definition. 
Import additional tables by repeating these steps. After all the items are imported, return to the 
Dictionary Editor where you can define relationships and delete any columns not used in your 
Clarion application. See SQL Accelerator Drivers--Define Only the Fields You Use. 
 


---

Database Drivers and Interfaces 
283 
Pervasive SQL Import Wizard--Login Dialog 
 
Clarion's Dictionary Editor Import Wizard lets you import Pervasive SQL table definitions into your 
Clarion Data Dictionary. When you select the Pervasive SQL Accelerator Driver from the driver 
drop-down list, the Import Wizard opens the Login/Connection dialog. The Login/Connection 
dialog collects the connection information for the Pervasive SQL database. 
 
 
Before you can connect to the SQL database and import table definitions, the database 
must be started and must be accessible from your computer. 
Fill in the following fields in the Login/Connection dialog: 
Database Name 
Select the Pervasive SQL database that contains the tables to 
import. If the Database Name list is empty, you may type in the 
name. See your server documentation for information on how the 
database is specified. The specification may depend on where the 
database server is located (remote or local), and on the network 
protocol (TCP/IP, IPX, etc.) used to access it. 
DDF Directory 
Press the Browse button to select the pathname or directory 
containing the database DDF files. 
Database Directory 
Press the Browse button to select the pathname or directory 
containing the database. 
 
 
Specify either the Database Name or the DDF directory, but not both. 
Owner Names 
Optionally, type a comma separated list of names the Pervasive 
SQL driver tries when opening encrypted Btrieve files. If a 
name contains a comma or space, it must be surrounded by 
single quotes. 
Refresh table list 
Check this box to refresh the list of tables to import when you 
press the Next > button. Clear the box to improve performance 
when the database is likely to be unchanged between imports. 
Disconnect after 
Import or Cancel 
Check this box to disconnect from the server after importing the 
(last) definition. Generally, you should clear this box when 
importing multiple definitions in order to maintain your 
connection to the server between imports.  
Next > 
Press this button to open the Import Wizard's Import List 
dialog. 
 


---

Database Drivers 
284 
Connection Information and Driver Configuration--File 
Properties 
 
Typically, you add Pervasive SQL support to your application by importing the table definitions 
into your Clarion Data Dictionary. The Import Wizard automatically fills in the File Properties 
dialog with default values based on the imported item. However, you can use the Owner Name 
field in the File Properties dialog to further configure the way the Pervasive SQL Driver accesses 
the data. 
Pervasive SQL allows some information in addition to the database identification in the Owner 
Name field. This information appears alternatively as: 
Database[,Owners;Switches] 
or 
DDF=DDFPath[|Datapath][,Owners;Switches] 
Where Database is the name of a Pervasive SQL database. DDFPath is a path to a set of DDF 
(Btrieve data dictionary) files. Datapath is the path to the corresponding data files. If omitted, 
Datapath defaults to DDFPath. Owners is a comma separated list of names to try when opening 
encrypted Btrieve files. If a name contains a comma or space, it must be surrounded by single 
quotes. Switches is a semicolon separated list of assignments. Valid switches are: 
## CREATEDDF=[0|1|2]
Where 0 creates a new DDF file, 1 replaces the existing DDF file, and 2 removes the existing 
DDF File. 
 
## NOTE:
The CREATEDDF switch is provided primarily for use during initial installation to allow you to 
build new DDF files. You should never use this switch for existing databases.  
 


---

Database Drivers and Interfaces 
285 
Pervasive SQL:Supported Commands and Attributes 
 
 
File Attributes 
Supported 
 
## CREATE
Y 
 
DRIVER(filetype [,driver string]) 
Y 
 
## NAME
Y 
 
## ENCRYPT
N 
 
OWNER(password) 
Y1 
 
## RECLAIM
N 
 
PRE(prefix) 
Y 
 
## BINDABLE
Y 
 
## THREAD
Y 
 
EXTERNAL(member) 
Y 
 
DLL([flag]) 
Y 
 
OEM 
N 
 
 
File Structures 
Supported 
 
## INDEX
Y 
 
KEY 
Y 
 
## MEMO
N 
 
## BLOB
Y 
 
## RECORD
Y 
 
 
Index, Key, Memo Attributes 
Supported 
 
## BINARY
N3 
 
DUP 
Y 
 
## NOCASE
Y 
 
OPT 
N 
 
## PRIMARY
Y 


---

Database Drivers 
286 
 
## NAME
Y 
 
Ascending Components 
Y 
 
Descending Components 
Y 
 
Mixed Components 
Y 
 
 
Field Attributes 
Supported 
 
DIM 
N 
 
## OVER
Y 
 
## NAME
Y 
 
 
File Procedures 
Supported 
 
BOF(file) 
N 
 
BUFFER(file) 
Y 
 
BUILD(file) 
Y 
 
BUILD(key) 
Y 
 
BUILD(index) 
Y3 
 
BUILD(index, components) 
Y3 
 
BUILD(index, components, filter) 
N 
 
BYTES(file) 
Y 
 
CLOSE(file) 
Y 
 
COPY(file, new file) 
N 
 
CREATE(file) 
Y 
 
DUPLICATE(file) 
Y 
 
DUPLICATE(key) 
Y 
 
EMPTY(file) 
Y 
 
EOF(file) 
N 
 
FLUSH(file) 
N 
 
LOCK(file) 
N 
 
NAME(label) 
Y 


---

Database Drivers and Interfaces 
287 
 
OPEN(file, access mode) 
Y 
 
PACK(file) 
N 
 
POINTER(file) 
N 
 
POINTER(key) 
N 
 
POSITION(file) 
N 
 
POSITION(key) 
Y 
 
RECORDS(file) 
Y 
 
RECORDS(key) 
Y 
 
REMOVE(file) 
Y 
 
RENAME(file, new file) 
N 
 
SEND(file, message) 
Y 
 
SHARE(file, access mode) 
Y 
 
STATUS(file) 
Y 
 
STREAM(file) 
N 
 
UNLOCK(file) 
N 
 
 
Record Access 
Supported 
 
ADD(file) 
Y 
 
ADD(file, length) 
N 
 
APPEND(file) 
Y 
 
APPEND(file, length) 
N 
 
DELETE(file) 
Y 
 
GET(file,key) 
Y 
 
GET(file, filepointer) 
N 
 
GET(file, filepointer, length) 
N 
 
GET(key, keypointer) 
N 
 
HOLD(file) 
N 
 
NEXT(file) 
Y 
 
NOMEMO(file) 
N 


---

Database Drivers 
288 
 
PREVIOUS(file) 
Y 
 
PUT(file) 
Y 
 
PUT(file, filepointer) 
N 
 
PUT(file, filepointer, length) 
N 
 
RELEASE(file) 
N 
 
REGET(file,string) 
N 
 
REGET(key,string) 
Y 
 
RESET(file,string) 
N 
 
RESET(key,string) 
Y 
 
SET(file) 
Y 
 
SET(file, key) 
N 
 
SET(file, filepointer) 
N 
 
SET(key) 
Y 
 
SET(key, key) 
Y 
 
SET(key, keypointer) 
N 
 
SET(key, key, filepointer) 
N 
 
SKIP(file, count) 
Y 
 
WATCH(file) 
Y 
 
 
Transaction Processing 
Supported2 
 
LOGOUT(timeout, file, ..., file) 
Y4 
 
## COMMIT
Y 
 
## ROLLBACK
Y 
 
 
Null Data Processing 
Supported 
 
NULL(field) 
Y 
 
SETNULL(field) 
Y 
 
SETNULL(file,field) 
Y 
 
SETNONNULL(field) 
Y 


---

Database Drivers and Interfaces 
289 
Notes 
1      We recommend using a variable password that is lengthy and contains special characters 
because this more effectively hides the password value from anyone looking for it. For 
example, a password like "dd....#$...*&" is much more difficult to "find" than a password 
like "SALARY." 
 
 
To specify a variable instead of the actual password in the Owner Name field of the 
File Properties dialog, type an exclamation point (!) followed by the variable name. 
For example: !MyPassword. 
2      See also PROP:Logout in the Language Reference. 
3      BUILD(index) sets internal driver flags to guarantee the driver generates the correct 
ORDER BY clause. The driver does not call the backend server. 
4      Whether LOGOUT also LOCKs the table depends on the server's configuration for 
transaction processing. See your server documentation. 
 


---

Database Drivers 
290 
SQLAnywhere Accelerator 
  
Overview 
SQLAnywhere Server 
For complete information on the SQLAnywhere database system, please review Sybase's 
SQLAnywhere documentation. 
SQLAnywhere Accelerator 
The SQLAnywhere Accelerator is one of several SoftVelocity SQL Accelerators. These SQL 
Accelerators share a common code base and many common features such as SoftVelocity's 
unique, high speed buffering technology, common driver strings, and SQL logging capability. See 
SQL Accelerators for information on these common features. 
The SQLAnywhere Accelerator converts standard Clarion file I/O statements and function calls 
into optimized SQL statements, which it sends to the backend SQLAnywhere server for 
processing. This means you can use the same Clarion code to access both SQLAnywhere tables 
and other file systems such as TopSpeed files. It also means you can use Clarion template 
generated code with your SQL databases. 
All the common behavior of all the SQL Accelerators is documented in the SQL Accelerators 
section.  The SQLAnywhere Accelerator is based on the ODBC Accelerator and inherits all 
features of the ODBC Accelerator.  All the common behavior of the SQL Accelerators that are 
derived from the ODBC Accelerator is documented in the ODBC Accelerator section.  All 
behavior specific to this driver is noted here. 
 
Start the SQLAnywhere Client 
Clarion's Dictionary Synchronizer Wizard (Enterprise Edition) lets you import an entire 
SQLAnywhere database definition into your Clarion Data Dictionary in a single pass. Before you 
can connect to the SQLAnywhere database and import table definitions, you must start the 
database client software. 
  
Before you can connect to the SQLAnywhere database and import table definitions, you 
must start the database client software. 
If you have not started the client software, Clarion issues the unable to start database engine 
message. 


---

Database Drivers and Interfaces 
291 
SQLAnywhere Import Wizard--Login Dialog 
Clarion's Dictionary Editor Import Wizard lets you import SQLAnywhere table definitions into your 
Clarion Data Dictionary. When you select the SQLAnywhere Accelerator from the driver drop-
down list, the Import Wizard opens a login dialog. This dialog collects the connection information 
for the SQLAnywhere database. 
Fill in the following fields in the Login/Connection dialog: 
Database 
Select the SQLAnywhere engine that contains the tables to import. If the 
Database list is empty, you may type in the name. See your server 
documentation or your DBA for information on database engines. 
Username 
For Standard Security, type your Username. For Trusted Security 
(Integrated NT Security) no Username is required. See your server 
documentation or your DBA for information on applicable Usernames and 
security methods. 
Password 
For Standard Security, type your Password. For Trusted Security 
(Integrated NT Security) no Password is required. See your server 
documentation or your DBA for information on applicable Passwords and 
security methods. 
Filter 
Optionally, provide a filter expression to limit the list of tables and views to 
import. The filter expression queries the SYSCATALOG view. The filter 
expression is limited to 1024 characters in length. The filter is case 
sensitive, so type your filter value accordingly. 
 
Following is a list of the column names (and their Clarion datatypes) you can reference in 
your filter expression. See your SQLAnywhere documentation for information on these fields. 
## CREATOR
## STRING(128)
## TNAME
## STRING(128)
## DBSPACENAME
## STRING(128)
## TABLETYPE
## STRING(10)
## NCOLS
## LONG
## PRIMARY_KEY
## STRING(1)
## CHECK
## STRING(32767)
## REMARKS
## STRING(32767)
 
Disconnect from Server 
when Import is finished 
Check this box to disconnect from the server after 
importing (or canceling). Generally, you should clear this 
box when importing multiple definitions in order to 
maintain your connection to the server between imports.  
Next > 
Press this button to open the Import Wizard's Import 
List dialog. 
 


---

Database Drivers 
292 
SQLAnywhere Import Wizard—Import List Dialog 
 
When you press the Next > button, the Import Wizard opens the Import List dialog. The Import 
List dialog lists the importable items. 
Highlight the table whose definition to import, then press the Finish button to import. The Import 
Wizard adds the definition to your Clarion Data Dictionary, then opens the File Properties dialog 
to let you modify the default definition. 
Import additional tables by repeating these steps. After all the items are imported, return to the 
Dictionary Editor where you can define relationships and delete any columns not used in your 
Clarion application. See SQL Accelerators--Define Only the Fields You Use. 
 
SQLAnywhere Connection Info/Driver Configuration--
File Properties 
Typically, you add SQLAnywhere support to your application by importing the table definitions 
into your Clarion Data Dictionary. The Import Wizard automatically fills in the File Properties 
dialog with default values based on the imported item.  
The OWNER attribute for SQLAnywhere Accelerator takes the format: 
engine,username,password 
 
The SQLAnywhere driver uses ODBC to communicate with the SQLAnywhere engine.  When 
more than one ODBC Driver for SQLAnywhere is installed on a machine the driver will choose to 
use the “Sybase SQL Anywhere” driver first.  To force the driver to use a specific ODBC  Driver 
you add to the Windows Registry the String Value “Dll” to the key 
HKEY_LOCAL_MACHINE\Software\SoftVelocity\SQLAnywhere.  You set this value to the name 
of the ODBC Driver.  For Example, set the value to “SQL Server Native Client 10.0” to force the 
MSQL driver to use the 10.0 Driver even when the 11.0 driver is available. 
 
 
Type an exclamation point (!) followed by a variable name in the Owner Name field of the 
File Properties dialog to specify a variable connect string rather than hard coding the 
connect string (OWNER attribute) . For example: !GLO:ConnectString. 
 


---

Database Drivers and Interfaces 
293 
SQLAnywhere Accelerator Driver Strings 
There are switches or "driver strings" you can set to control the way your application creates, 
reads, and writes files with a specific driver. Driver strings are simply messages or parameters 
that are sent to the file driver at run-time to control its behavior. See Common Driver Features--
Driver Strings for an overview of these runtime Database Driver switches and parameters. 
 
A forward slash preceeds all SQL Accelerator driver strings. The slash allows the driver to 
distinguish between driver strings and SQL statements sent with SEND. 
In addition to the standard SQL Driver Strings, the SQLAnywhere Accelerator supports the 
following Driver Strings: 
## LOGONSCREEN
## GATHERATOPEN
 
LOGONSCREEN (SQLAnywhere Accelerator) 
 
DRIVER('SQLAnywhere', '/LOGONSCREEN = TRUE | FALSE ' ) 
[ AutoLogon" = ] SEND(file, '/LOGONSCREEN [ = TRUE | FALSE ]' ) 
 
See Also:     PROP:LogonScreen. 
 
GATHERATOPEN (SQLAnywhere Accelerator) 
 
DRIVER('SQLAnywhere', '/GATHERATOPEN = TRUE | FALSE ' ) 
By default the driver delays gathering field information until it is required. However, some 
backends (like Sybase 11) perform poorly under these conditions. Setting GATHERATOPEN to 
TRUE forces the driver to gather most of the field information when the file is opened, whihc 
avoids a slowdown during program execution.  


---

Database Drivers 
294 
SQLAnywhere Accelerator Driver Properties 
You can use Clarion's property syntax to query and set certain SQLAnywhere Accelerator driver 
properties. In addition to the standard SQL Acclerator properties (see SQL Accelerators--SQL 
Accelerator Properties), the SQLAnywhere Accelerator supports the following properties. 
 
PROP:LogonScreen (SQLAnywhere Accelerator ) 
PROP:LogonScreen sets or returns the toggle that determines whether the driver automatically 
prompts for logon information. By default (PROP:LogonScreen=True), the driver does display a 
logon window if no connect string is supplied. If set to False and there is no connect string, the  
OPEN(file) fails and FILEERRORCODE() returns '28000.' For example: 
AFile FILE,DRIVER('SQLAnywhere') 
!file declaration with no userid and password 
      END 
## CODE
 AFile{PROP:LogonScreen}=True   !enable auto login screen 
 OPEN(Afile) 
The logon screen is the SQLAnywhere Connect dialog. Consult your SQLAnywhere 
documentation for more information on this dialog. The end-user's ability to use the connect 
dialog will depend on the security surrounding the SQLAnywhere database. For example, the 
end-users may have access rights to a named database (sademo) that they can access with the 
SQLAnywhere client software, but they may not have access rights to the *.db files that comprise 
the database. The SQLAnywhere connect dialog requires *.db files rather than database name.  
 


---

Database Drivers and Interfaces 
295 
Using Embedded SQL(SQLAnywhere Accelerator ) 
You can use Clarion's property syntax (PROP:SQL) to send SQL statements to the backend SQL 
server within the normal execution of your program. See SQL Accelerators--Using Embedded 
SQL for more information. 
 
Calling a Stored Procedure (SQLAnywhere Accelerator ) 
For SQLAnywhere NORESULTCALL is more efficient than CALL. 


---

Database Drivers 
296 
SQLAnywhere Accelerator Supported File Commands 
and Functions 
 
 
File Attributes 
Supported 
 
## CREATE
Y 
 
DRIVER(filetype [,driver string]) 
Y 
 
## NAME
Y 
 
## ENCRYPT
N 
 
OWNER(password) 
Y1 
 
## RECLAIM
N 
 
PRE(prefix) 
Y 
 
## BINDABLE
Y 
 
## THREAD
Y 
 
EXTERNAL(member) 
Y 
 
DLL([flag]) 
Y 
 
OEM 
N 
 
## LOCALE
N 
 
File Structures 
Supported 
 
## INDEX
Y 
 
KEY 
Y 
 
## MEMO
N 
 
## BLOB
Y 
 
## RECORD
Y 
 
 
Index, Key, Memo Attributes 
Supported 
 
## BINARY
N3 
 
DUP 
Y 
 
## NOCASE
Y 
 
OPT 
N 


---

Database Drivers and Interfaces 
297 
 
## PRIMARY
Y 
 
## NAME
Y 
 
Ascending Components 
Y 
 
Descending Components 
Y 
 
Mixed Components 
Y 
 
 
Field Attributes 
Supported 
 
DIM 
N 
 
## OVER
Y 
 
## NAME
Y 
 
 
File Procedures 
Supported 
 
BOF(file) 
N 
 
BUFFER(file) 
Y 
 
BUILD(file) 
Y 
 
BUILD(key) 
Y 
 
BUILD(index) 
Y3 
 
BUILD(index, components) 
Y3 
 
BUILD(index, components, filter) 
N 
 
BYTES(file) 
Y 
 
CLOSE(file) 
Y 
 
COPY(file, new file) 
N 
 
CREATE(file) 
Y 
 
DUPLICATE(file) 
Y 
 
DUPLICATE(key) 
Y 
 
EMPTY(file) 
Y 
 
EOF(file) 
N 
 
FLUSH(file) 
N 
 
LOCK(file) 
N 


---

Database Drivers 
298 
 
NAME(label) 
Y 
 
OPEN(file, access mode) 
Y 
 
PACK(file) 
N 
 
POINTER(file) 
N 
 
POINTER(key) 
N 
 
POSITION(file) 
N 
 
POSITION(key) 
Y 
 
RECORDS(file) 
Y 
 
RECORDS(key) 
Y 
 
REMOVE(file) 
Y 
 
RENAME(file, new file) 
N 
 
SEND(file, message) 
Y 
 
SHARE(file, access mode) 
Y 
 
STATUS(file) 
Y 
 
STREAM(file) 
N 
 
UNLOCK(file) 
N 
 
 
Record Access 
Supported 
 
ADD(file) 
Y 
 
ADD(file, length) 
N 
 
APPEND(file) 
Y 
 
APPEND(file, length) 
N 
 
DELETE(file) 
Y 
 
GET(file,key) 
Y 
 
GET(file, filepointer) 
N 
 
GET(file, filepointer, length) 
N 
 
GET(key, keypointer) 
N 
 
HOLD(file) 
N 
 
NEXT(file) 
Y 


---

Database Drivers and Interfaces 
299 
 
NOMEMO(file) 
N 
 
PREVIOUS(file) 
Y 
 
PUT(file) 
Y 
 
PUT(file, filepointer) 
N 
 
PUT(file, filepointer, length) 
N 
 
RELEASE(file) 
N 
 
REGET(file,string) 
N 
 
REGET(key,string) 
Y 
 
RESET(file,string) 
N 
 
RESET(key,string) 
Y 
 
SET(file) 
Y 
 
SET(file, key) 
N 
 
SET(file, filepointer) 
N 
 
SET(key) 
Y 
 
SET(key, key) 
Y 
 
SET(key, keypointer) 
N 
 
SET(key, key, filepointer) 
N 
 
SKIP(file, count) 
Y 
 
WATCH(file) 
Y 
 
 
Transaction Processing 
Supported 
 
LOGOUT(timeout, file, ..., file) 
Y4 
 
## COMMIT
Y 
 
## ROLLBACK
Y 
 
 
 


---

Database Drivers 
300 
 
Null Data Processing 
Supported 
 
NULL(field) 
Y 
 
SETNULL(field) 
Y 
 
SETNULL(file,field) 
Y 
 
SETNONNULL(field) 
Y 
Notes: 
1      We recommend using a variable password that is lengthy and contains special characters 
because this more effectively hides the password value from anyone looking for it. For 
example, a password like "dd....#$...*&" is much more difficult to "find" than a password 
like "SALARY."  To specify a variable instead of the actual password in the Owner 
Name field of the File Properties dialog, type an exclamation point (!) followed by 
the variable name. For example: !MyPassword. 
2      See also PROP:Logout in the Language Reference. 
3      BUILD(index) sets internal driver flags to guarantee the driver generates the correct 
ORDER BY clause. The driver does not call the backend server. 
4      Whether LOGOUT also LOCKs the table depends on the server's configuration for 
transaction processing. See your server documentation. 


---

Database Drivers and Interfaces 
301 
SQLAnywhere Accelerator - Synchronizer Server 
Clarion's Enterprise Edition includes the SQLAnywhere Synchronizer Server and the Data 
Dictionary Synchronizer. The Dictionary Synchronizer uses the Synchronizer Server to gather 
complete information about an SQLAnywhere database. 
The SQLAnywhere Synchronizer Server is one of several used by the Dictionary Synchronizer. 
All the common behavior of all the SQL Accelerators is documented in the SQL accelerators 
section. All behavior specific to this driver is noted here. 


---

Database Drivers 
302 
SQLite File Driver 
 
Overview 
SQLite is a very portable file format particularly useful for data that needs to be accessible locally 
from various devices include PCs running various operating systems or smart phones. 
SQLite is not designed for multi-user access.  It is not a client/server system like most SQL 
systems.  There is no engine that needs to be installed.  It is much more like the TopSpeed Driver 
than MSSQL. 
To run a Clarion program that uses the SQLite driver all that you need are the Clarion libraries 
that you use, plus sqlite3.dll.  This can be downloaded from www.sqlite.org.  The driver requires 
version 3.3.1 or later of sqlite3.dll. 
SQLite stores all tables and keys in a single data file. 
SQLite does not support stored procedures.  
Warning: 
Although the SQLite driver supports DECIMAL and PDECIMAL data types, the SQLite data 
format does not properly support these.  It stores the values as binary numbers.  Normally this will 
not cause any problems.  You may encounter problems if you use SQL code to retrieve data and 
in this SQL code use rounding functions.  For example,  ROUND(9.95,1)  evaluates to 10, not 9.9 
as expected.  This only affects any SQL code.  It does not affect standard Clarion code. 
Tip: 
ADD() is very fast with SQLite when you use it within a transaction.  If you need to add a lot of 
data it is recommended to issue a LOGOUT statement followed by the ADD calls and when 
completed issue a COMMIT. 
Note: 
When building a project that uses the SQLite driver the project system will copy sqlite3.dll to the 
destination folder.  If the dll cannot be found a warning is generated.  To avoid this warning either 
place this dll in a folder listed in the [Copy] section of your redirection file, or turn off “Copy 
Referenced Dlls” in the properties for the project; or edit <Application 
Data>\SoftVelocity\Clarion\<Clarion Version>\LibCopyList.xml file and remove the dll entry 
named C%V%LIT.DLL. 
SQLite Accelerator Supported Commands and 
Attributes 
 
File Attributes 
Supported 
## CREATE
Y 
DRIVER(filetype [,driver string]) 
Y 
## NAME
Y 
## ENCRYPT
N 
OWNER(password) 
Y1 
## RECLAIM
N 
PRE(prefix) 
Y 
 
## BINDABLE
Y 
## THREAD
Y 


---

Database Drivers and Interfaces 
303 
 
EXTERNAL(member) 
Y 
DLL([flag]) 
Y 
OEM 
N 
 
## LOCALE
N 
File Structures 
Supported 
## INDEX
Y 
 
KEY 
Y 
## MEMO
N 
## BLOB
Y 
## RECORD
Y 
Index, Key, Memo Attributes 
Supported 
## BINARY
Y 
DUP 
Y 
## NOCASE
Y 
OPT 
N 
## PRIMARY
Y 
## NAME
Y 
Ascending Components 
Y 
Descending Components 
Y 
 
Mixed Components 
Y 
Field Attributes 
Supported 
DIM 
N 
## OVER
Y 
## NAME
Y 
 
File Procedures 
Supported 
BOF(file) 
N 
BUFFER(file) 
N 
 
BUILD(file) 
Y 
BUILD(key) 
Y 
BUILD(index) 
Y3 
BUILD(index, components) 
Y3 
BUILD(index, components, filter) 
N 
BYTES(file) 
Y 
CLOSE(file) 
Y 
COPY(file, new file) 
N 
 
CREATE(file) 
## Y7,8
DUPLICATE(file) 
Y 
DUPLICATE(key) 
Y 
EMPTY(file) 
Y 
EOF(file) 
N 
FLUSH(file) 
N 
LOCK(file) 
N 
NAME(label) 
Y 
OPEN(file, access mode) 
Y6 
PACK(file) 
N 
POINTER(file) 
N 
POINTER(key) 
N 
POSITION(file) 
N 
POSITION(key) 
Y 
RECORDS(file) 
Y 
 
RECORDS(key) 
Y 
REMOVE(file) 
Y 


---

Database Drivers 
304 
 
RENAME(file, new file) 
N 
SEND(file, message) 
Y 
SHARE(file, access mode) 
Y 
STATUS(file) 
Y 
STREAM(file) 
N 
UNLOCK(file) 
N 
 
Record Access 
Supported 
ADD(file) 
Y 
ADD(file, length) 
N 
APPEND(file) 
Y 
APPEND(file, length) 
N 
DELETE(file) 
Y 
GET(file,key) 
Y 
GET(file, filepointer) 
N 
GET(file, filepointer, length) 
N 
GET(key, keypointer) 
N 
HOLD(file) 
N 
NEXT(file) 
Y 
NOMEMO(file) 
N 
 
PREVIOUS(file) 
Y 
PUT(file) 
Y 
PUT(file, filepointer) 
N 
PUT(file, filepointer, length) 
N 
RELEASE(file) 
N 
 
REGET(file,string) 
N 
REGET(key,string) 
Y 
RESET(file,string) 
N 
RESET(key,string) 
Y 
SET(file) 
Y 
 
SET(file, key) 
N 
SET(file, filepointer) 
N 
SET(key) 
Y 
SET(key, key) 
Y 
SET(key, keypointer) 
N 
SET(key, key, filepointer) 
N 
 
SKIP(file, count) 
Y 
 
WATCH(file) 
Y 
Transaction Processing 
Supported 
LOGOUT(timeout, file, ..., file) 
## Y2,4,5
## COMMIT
Y 
## ROLLBACK
Y 
Null Data Processing 
Supported 
NULL(field) 
Y 
SETNULL(field) 
Y 
SETNULL(file,field) 
Y 
SETNONNULL(field) 
Y 
Notes 
1  
The OWNER is the name of the SQLite database file that the table is stored in. 
2  
See also PROP:Logout in the Language Reference. 
3  
BUILD(index) sets internal driver flags to guarantee the driver generates the correct 
ORDER BY clause. The driver does not call the backend server. 


---

Database Drivers and Interfaces 
305 
4  
You cannot logout threaded and non-threaded files at the same time.  All files in the 
LOGOUT statement must be in the same database table. 
5  
Doing SET;NEXT;LOGOUT;NEXT is not supported. 
6  
If OPEN fails with ERRORCODE 47 (InvalidFileErr), and you have file logging turned on 
(See the “Database Driver System-wide Logging”), the log file will have the name of the 
field that could not be found in the table on disk and a list of names of columns in the 
table on disk. 
7  
CREATE converts Clarion data types to SQLite Data types using the following table 
8 
A PRIMARY KEY AUTOINCREMENT constraint will be added to a field definition if 
/AUTOINC=TRUE is specified in the driver string and the field is the key component of 
the primary key and there is only one key component for the primary key and the field 
type is LONG. 
 
Clarion Data Type 
SQLite Data Type 
## STRING
## CHAR
## CSTRING
## VARCHAR
## STRING(8);GROUP
## OVER(STRING);DATE;TIME
## DATETIME
## DATE
## DATE
## PDECIMAL
## NUMBER
## DECIMAL
## NUMBER
## BYTE
## TINYINT
## SHORT
## SMALLINT
## LONG
## INTEGER
## SREAL
## FLOAT
## REAL
## REAL
## BLOB
## CLOB
## BLOB,BINARY
## BLOB
 
SQLite Accelerator Driver Strings 
The SQLite Driver supports the following standard SQL driver strings: 
## ALLOWDETAILS
## AUTOINC1
## NOPRIMARY
## USEPRIMARY


---

Database Drivers 
306 
## WHERE
 
Note 1: The AUTOINC driver string for SQLite is in the form ‘AUTOINC  = TRUE | FALSE’.  If 
AUTOINC is set to TRUE and there is a primary key on the table that has only one component 
and that component is of type LONG, then the CREATE statement will create an 
AUTOINCREMENT PRIMARY KEY constraint on that component and ADD will retrieve the value 
for that field set by SQLite. 
 
SQLite Accelerator Properties 
PROP:CreateDB 
 
PROP:CreateDB is a command property.  This command property tells the SQL Accelerator to 
create the SQLite Database file that is specified in the OWNER attribute of the file. 
If the database file already exists, this command does nothing.  The existing database file will not 
be destroyed. 
You can also create a database by issuing a CREATE statement for any table in that database.  If 
the database does not exist, it will be created and the table will also be created in the database. 
You would use this property if you are using SQL statements to create the database rather than 
the Clarion CREATE statement. 
Example: 
sqlTable FILE,DRIVER(‘SQLite’),OWNER(‘MyDatabase.sqlite’) 
 
## RECORD
 
  END 
 
END 
## CODE
  sqlTable{PROP:CreateDB}  ! Will create the file MyDatabase.sqlite 
  IF ERRORCODE() ! test to see if the create worked 
 
Updating data with SQLite 
You can access the same SQLite file from multiple processes.  However, only one process can 
write to the file at the same time.  Once a process has written to any table in the SQLite database 
file that process is the only process that can write to any table in that database.  
 
SQLite and Multithreading 
SQLite does not work well in a multi-threading environment.  It is designed to be used on a single 
thread only.  The Clarion file driver overcomes this limitation as much as possible.  To make this 
work the driver has one limitation on usage.  Only one thread can be accessing the SQLite 
database while a transaction is active.  If another thread attempts to access an SQLite database 
and another thread is in the middle of a transaction, the non-transacting thread will wait until the 
transaction is completed. 
 
SQLite Accelerator Error Handling 
FILERRORCODE() can be used to obtain the error code returned from SQLite. 


---

Database Drivers and Interfaces 
307 
Below is a table with all the error codes that FILEERRORCODE() will return after a call to an 
SQLite file.  For programs designed to target non-English speaking users or ones that wish to 
change the error messages, the table also includes the CLAMSGerrornumber values that must 
be used in the env file. 
## FILEERRORCODE
## CLAMSG
Error 
Number 
Message 
1 
4201 
SQL error or missing database 
2 
4202 
Internal logic error in SQLite 
3 
4203 
Access permission denied 
4 
4204 
Callback routine requested an abort 
5 
4205 
The database file is locked 
6 
4206 
A table in the database is locked 
71 
4207 
A malloc() failed 
82 
4208 
Attempt to write a readonly database 
9 
4209 
Operation terminated by sqlite3_interrupt() 
10 
4210 
Some kind of disk I/O error occurred 
11 
4211 
The database disk image is malformed 
12 
4212 
Unknown opcode in sqlite3_file_control() 
13 
4213 
Insertion failed because database is full 
14 
4214 
Unable to open the database file 
15 
4215 
Database lock protocol error 
16 
4216 
Database is empty 
17 
4217 
The database schema changed 
18 
4218 
String or BLOB exceeds size limit 
19 
4219 
Abort due to constraint violation 
20 
4220 
Data type mismatch 
21 
4221 
Library used incorrectly 
22 
4222 
Uses OS features not supported on host 


---

Database Drivers 
308 
232 
4223 
Authorization denied 
24 
4224 
Auxiliary database format error 
25 
4225 
2nd parameter to sqlite3_bind out of range 
26 
4226 
File opened that is not a database file 
80 
4280 
Could not load sqlite3.dll : (%1) %2 
You can download the dll from www.sqlite.org3 
81 
4281 
Could not find the procedure %1 in sqlite3.dll4 
82 
4282 
No OWNER attribute specified 
100 
4300 
sqlite3_step() has another row ready 
101 
4301 
sqlite3_step() has finished executing 
 
Notes: 
1: 
ERRORCODE() will return 8, NoMemErr 
2:  
ERRORCODE() will return 5, NoAccessErr 
3: 
%1 will be substituted with the error code returned from the operating system.  %2 will be 
substituted with the matching error message.  If you set a replacement string, you do not 
need to have %1 or %2 in your string. 
4: 
%1 will be substituted with the name of the missing procedure 


---

Database Drivers and Interfaces 
309 
ADO Interface 
 
What is ADO? 
ADO is a Microsoft technology, and stands for ActiveX Data Objects. It is a high-level 
programming interface used to access data in a database. ADO is designed as an easy-to-use 
application level interface to Microsoft's low-level data access interface, OLE DB. 
 
The Clarion ADO classes and templates were created to provide access to the MS ADO 
database connectivity layer.  While not specifically a database driver, it is accessed in a similar 
manner.  As such, intrinsic data file operations will not function and require that the provided class 
methods and templates be used. 
 
ADO is automatically installed with Microsoft IIS as an Active X component. ADO is a common 
way to access a database from inside a web page (like an ASP page). For example, to connect to 
a database inside an ASP page: 
 
1. 
Create an ADO connection to a database  
2. 
Open the database connection  
3. 
Create an ADO recordset  
4. 
Open the recordset  
5. 
Extract the data you need from the recordset  
6. 
Close the recordset  
7. 
Close the connection 
 
The important thing to note here is the specific opening and closing of the database 
connection. Failure to specifically close an ADO connection can result in memory leakage. 
 
 


---

Database Drivers 
310 
ADO Requirements 
 
The use of Clarion with ADO requires that you have installed the Microsoft Data Access 
Components (MDAC) interface, which is a free download from the Microsoft web site. You must 
have Version 2.62 or later installed. 
 
The general flow of using the new ADO interface in Clarion: 
 
1. 
Import your ADO tables using the Dictionary Editor. 
2. 
Add the ADO Global Extension to your application 
3. 
Add your various ADO procedures as necessary. 
 
 
ADO Logging 
 
The ADO Synchronizer supports trace logging. Logging can only be turned on via the 
DRIVERS.INI file in the CSIDL_APPDATA\SoftVelocity\Clarion\<clarion_version> folder. 
 
The section in the DRIVERS.INI is called 
## [CWADOSYNCHRONISER]
 
Two possible settings in this section are: 
 
Trace=0|1 
TraceFile=filename 
 
Trace must be set to 1 to turn on logging 
 
TraceFile specifies the file you want to log to.  If not supplied then the log is 
## ADOSYNCHRONISER.LOG
 
The DrvTrace example application has been updated to support logging of the ADO 
Synchronizer. 
 
  
This logging is active during the synchronization process with the Dictionary Editor. It is not to be 
confused with the normal trace logging that can be active in your application at runtime. 
 


---

Database Drivers and Interfaces 
311 
 
Index 
32-bit applications .................................... 251 
6.3 Features ............................................. 144 
## ACS ........................................................... 25
## ADO ......................................................... 300
ADO - Date and Time Columns ............... 145 
ADO Logging ........................................... 301 
ADO Requirements ................................. 301 
## ALIAS ....................................................... 197
## ALL_CATALOG ....................................... 253
## ALLOWDETAILS ..................................... 173
## ALLOWREAD ............................................ 25
## ALWAYSQUOTE ....................................... 15
AlwaysRebind .......................................... 198 
## APPENDBUFFER.............................. 25, 174
## ASCII ................................................... 5, 7, 8
Database Driver ........................................... 5 
Driver Strings ............................................... 7 
Supported Commands and Attributes ......... 8 
auto numbered keys ................................ 256 
## AUTOINC ................................................. 174
## BALANCEKEYS ........................................ 25
Basic .................................................... 15, 16 
Driver Strings ............................................. 15 
Supported Commands and Attributes ....... 16 
Basic Database Driver ............................... 10 
BINARY driver switch .............................. 242 
BINARY switch on bound parameters ..... 165 
## BINDCOLORDER .................................... 174
## BINDCONSTANTS .................................. 175
Browsing SQL Tables .............................. 149 
Btrieve .................................................. 28, 33 
Client/Server .............................................. 33 
Collating Sequence ................................... 33 
Driver Properties ........................................ 20 
Error Codes ............................................... 33 
File Sharing ............................................... 33 
File Structure ............................................. 33 
KEY Definitions ......................................... 33 
Keys and Indexes ..................................... 33 
Page Size .................................................. 33 
Record Lengths ......................................... 33 
Record Pointers ........................................ 33 
Supported Commands and Attributes....... 28 
Transaction Framing ................................. 33 
Btrieve Database Driver ............................ 20 
Btrieve Driver Strings ................................ 25 
## BUFFERS ............................... 51, 65, 75, 97
## BUSYHANDLING.................................... 175
## BUSYMESSAGE .................................... 176
## BUSYRETRIES ....................................... 177
## C60ORA.DLL .......................................... 253
## CALL ....................................................... 165
Calling a stored procedure ...................... 165 
Calling a Stored Procedure ............. 261, 286 
Oracle ..................................................... 261 
SQLAnywhere ......................................... 286 
Calling a Stored Procedure (SQLAnywhere 
Accelerator ) ............................................ 286 
## CHECKFORNULL................................... 145
Choosing the Right Database Driver .......... 1 
Clarion Database Driver ........................... 38 
Clarion Driver Strings ................................ 41 
Clarion Functions used in SQL Filter 
Statements .............................................. 149 
Clarion Other ............................................. 44 
Clarion Supported Commands and 
Attributes ................................................... 42 
## CLIP ............................................................ 7
Clipper ........................................... 51, 53, 55 


---

Database Drivers 
312 
Driver Strings ............................................. 51 
Other .......................................................... 55 
Supported Commands and Attributes ....... 53 
Clipper Database Driver ............................ 48 
## CLIPSTRINGS ......................................... 178
## COMMA ..................................................... 15
Common Database Driver Features ............ 1 
## COMPRESS .............................................. 25
ConnectString .......................................... 198 
## CTRLZISEOF ........................................ 7, 15
Database Driver System Wide Logging....... 1 
Database Name .......................213, 229, 292 
Scalable SQL ................................... 213, 292 
Scalable SQL ........................................... 229 
Database Name, SQLAnywhere ............. 281 
Date and Time Column Considerations .. 145 
dBaseIII ................................................ 65, 67 
Driver Strings ............................................. 65 
Other .......................................................... 67 
DBaseIII ..................................................... 65 
Supported Commands and Attributes ....... 65 
dBaseIII Database Driver .......................... 61 
dbaseIV ...................................................... 75 
Driver Strings ............................................. 75 
dBaseIV ............................................... 77, 79 
Other .......................................................... 79 
Supported Commands and Attributes ....... 77 
dBaseIV Database Driver .......................... 73 
DBMSver ................................................. 198 
Debugging Your ODBC Application......... 244 
Debugging Your SQL Application ............ 147 
DECIMALCheck....................................... 113 
## DELETED ......................... 41, 51, 65, 75, 97
Details property - SQL ............................. 199 
Disconnect ............................................... 199 
DLL Coding Practices .............................. 263 
## DOS ..................................................... 89, 90
Driver Strings ............................................ 89 
Supported Commands and Attributes....... 90 
DOS Database Driver ............................... 85 
Driver Properties ............................. 228, 284 
## MSSQL ................................................... 228
SQLAnywhere ......................................... 284 
Driver Strings 2, 7, 15, 25, 41, 51, 65, 75, 89, 
97, 113, 245 
## ACS ........................................................... 25
## ALLOWREAD ........................................... 25
## ALWAYSQUOTE ...................................... 15
## APPENDBUFFER ..................................... 25
## BALANCEKEYS ........................................ 25
## BUFFERS ............................... 51, 65, 75, 97
## CLIENTID .................................................. 25
## CLIP ............................................................ 7
## COMMA .................................................... 15
## COMPRESS ............................................. 25
## CTRLZISEOF ........................................ 7, 15
DECIMALCheck ...................................... 113 
## DELETED ......................... 41, 51, 65, 75, 97
## ENDOFRECORD .................................. 7, 15
## ENDOFRECORDINQUOTE ..................... 15
## FIELDDELIMITER..................................... 15
## FILEBUFFERS ................................ 7, 15, 89
## FIRSTROWHEADER ................................ 15
## FLAGS .................................................... 113
## FREESPACE ............................................ 25
## FULLBUILD ............................................. 113
## HELD ........................................................ 41
## IGNORESTATUS.............. 41, 51, 65, 75, 97
## LACS ......................................................... 25
## MAINTAINHEADERTIME ......................... 41
## MEMO ....................................................... 25
## MSSQL ................................................... 223
## ODBC ...................................................... 245
## OMNIS ...................................................... 65


---

Index 
313 
Oracle ...................................................... 257 
## PAGESIZE ................................................. 25
## PNM ......................................................... 113
## PREALLOCATE......................................... 25
## QUICKSCAN ................................... 7, 15, 89
## QUOTE ...................................................... 15
## RECOVER ........................ 41, 51, 65, 75, 97
SQLAnywhere .......................................... 283 
## TAB .............................................................. 7
## TCF .......................................................... 113
## TRUNCATE ............................................... 25
## ZEROY2K ................................51, 65, 75, 97
Driver Tracing .......................................... 147 
DriverTracing ........................................... 199 
## PROP ....................................................... 199
Embedded SQL ............................... 165, 206 
Oracle ...................................................... 261 
## ENDOFRECORD................................... 7, 15
## ENDOFRECORDINQUOTE ...................... 15
## FASTCOLUMNFETCH ............................ 178
Field Switch - SQL ................................... 145 
## FIELDDELIMITER ..................................... 15
## FILEBUFFERS ................................ 7, 15, 89
## FILTER ............................................ 213, 292
## FIRSTROWHEADER ................................ 15
## FLAGS ..................................................... 113
## FORCEUPPERCASE .............................. 178
FoxPro ......................................... 97, 99, 101 
Driver Strings ............................................. 97 
Other ........................................................ 101 
Supported Commands and Attributes ....... 99 
FoxPro / FoxBase Database Driver ........... 91 
## FREESPACE ............................................. 25
## FULLBUILD ............................................. 113
Future Oracle Releases ........................... 132 
## GATHERATOPEN ...................179, 227, 284
GATHERATOPEN (MSSQL Accelerator) 227 
GATHERATOPEN (SQLAnywhere 
Accelerator) ............................................. 284 
General Information for all SQL Drivers . 149 
General Rules for Browsing SQL-Based 
Tables ..................................................... 149 
## GETINFO ................................................ 179
hdbc ........................................................ 200 
## HELD ........................................................ 41
henv ........................................................ 201 
## HINT ................................................ 226, 258
Oracle ..................................................... 258 
How ODBC Works .................................. 238 
hstmt ....................................................... 201 
## IGNORESTATUS.............. 41, 51, 65, 75, 97
## IGNORETRUNCATION .......................... 180
Import Wizard .......................................... 213 
Scalable SQL .......................................... 213 
Import Wizard, Oracle ............................. 253 
Import Wizard, SQLAnywhere ................ 281 
Importing from ODBC Data Sources ...... 240 
## INNER ..................................................... 201
IPX host .......................................... 253, 256 
## ISOLATIONLEVEL.................................. 183
## JOINTYPE .............................................. 184
Key Properties dialog .............................. 256 
## LACS ......................................................... 25
local host ................................................. 256 
Log .......................................................... 202 
## LOGFILE ......................................... 186, 202
Logging - Database Drivers ........................ 1 
Logging Driver Activity ............................ 147 
LoginTimeout .......................................... 202 
logon ....................................................... 229 
## MSSQL ................................................... 229
SQLAnywhere ......................................... 285 
## LOGON SCREEN ................................... 258
## LOGONSCREEN .................................... 201
## MSSQL ................................................... 227


---

Database Drivers 
314 
LOGONSCREEN (MSSQL Accelerator) . 227 
LOGONSCREEN (SQLAnywhere 
Accelerator) ............................................. 284 
## MAINTAINHEADERTIME .......................... 41
MARS Support ......................................... 188 
## MEMO ........................................................ 25
Microsoft Access and ODBC ................... 246 
## MSSQL ............................................ 227, 228
Driver Properties ...................................... 228 
Driver Strings ........................................... 223 
## LOGONSCREEN ..................................... 227
## SAVESTOREDPROC .............................. 227
## TRUSTEDCONNECTION ....................... 228
MSSQL Accelerator ................................. 262 
MSSQL Accelerator Calling a Stored 
Procedure ................................................ 218 
MSSQL Accelerator Connection Information 
and Driver Configuration--File Properties 216 
MSSQL Accelerator Driver Properties ..... 228 
MSSQL Accelerator Driver Strings .......... 223 
MSSQL Accelerator Performance 
Considerations ......................................... 217 
MSSQL Accelerator SQL Import Wizard--
Import List Dialog ..................................... 214 
MSSQL Accelerator SQL Import Wizard--
Login Dialog ............................................. 213 
MSSQL Accelerator Supported File 
Commands and Functions ....................... 229 
MSSQL Accelerator Synchronizer Server
 ................................................................. 230 
MSSQL Accelerator Using Embedded SQL
 ................................................................. 220 
MSSQL Connection Tips ......................... 218 
MSSQL logon .......................................... 229 
## MULTIPLEACTIVERESULTSETS .......... 188
## NESTING ................................................. 189
## NORESULTCALL .................................... 165
NOWHERE driver switch ......................... 242 
ODBC Accelerator Driver ........................ 230 
ODBC Caveats ........................................ 250 
ODBC Column Configuration--Column 
Properties ................................................ 242 
ODBC Connection Information and Driver 
Configuration ................................... 242, 243 
Column Configuration ............................. 242 
Key Properties ........................................ 243 
ODBC Data Types .................................. 239 
ODBC Driver Properties ......................... 245 
ODBC Driver Strings ............................... 245 
ODBC Key Configuration--Key Properties
 ................................................................ 243 
ODBC Supported Commands and Attributes
 ................................................................ 245 
## ODBCCALL ............................................. 190
## OMNIS ...................................................... 65
Optimization of SQL Expressions ........... 149 
Optimizing SET processing using the 
WHERE driver string ............................... 153 
Oracle ..................................................... 256 
auto numbered keys ............................... 256 
sequence numbers ................................. 256 
Unique Key Values ................................. 256 
Oracle Accelerator .................................. 132 
Oracle Accelerator Automatic Login Dialog
 ................................................................ 256 
Oracle Accelerator Data Types ............... 265 
Oracle Accelerator Driver Properties ...... 260 
Oracle Accelerator Driver Strings ........... 257 
Oracle Accelerator Generating Unique Key 
Values ..................................................... 256 
Oracle Accelerator Installation ................ 252 
Oracle Accelerator Overview .................. 251 
Oracle Accelerator Performance 
Considerations ........................................ 255 
Oracle Accelerator Supported Commands 
and Attributes .......................................... 265 
Oracle Accelerator System Requirements
 ................................................................ 251 
Oracle Accelerator Table Import Wizard—
Import List Dialog .................................... 254 


---

Index 
315 
Oracle Accelerator Table Import Wizard—
Login Dialog ............................................. 253 
Oracle Accelerator Troubleshooting ........ 270 
Oracle Accelerator --Using Embedded SQL
 ................................................................. 261 
Oracle connection .................................... 253 
Oracle CONSTRAINTs ............................ 253 
Oracle Driver Strings ............................... 257 
Oracle hints .............................................. 258 
Oracle indexes ......................................... 253 
Oracle linking fields ................................. 259 
Oracle login .............................................. 253 
Oracle Login Dialog ................................. 256 
Oracle Personal ....................................... 259 
Oracle Sequences ................................... 256 
Oracle Server ........................................... 251 
Oracle version .......................................... 251 
Oracle versions ........................................ 132 
OrderAllTables ......................................... 204 
## ORDERINSELECT .......................... 190, 205
## PAGESIZE ................................................. 25
## PASSWORD ............................................ 256
Password, SQLAnywhere ........................ 281 
## PATH
Oracle ...................................................... 251 
Performance Considerations ................... 154 
## PERSONAL ............................................. 259
Oracle ...................................................... 259 
PERSONAL Oracle ................................. 259 
Pervasive SQL Accelerator Driver ........... 250 
Pervasive SQL Connection Information and 
Driver Configuration--File Properties ....... 274 
Pervasive SQL Import Wizard--Import List 
Dialog ....................................................... 273 
Pervasive SQL Import Wizard--Login Dialog
 ................................................................. 274 
Pervasive SQL Overview ......................... 273 
Pervasive SQL Supported Commands and 
Attributes .................................................. 281 
## PL/SQL ................................................... 261
## PNM ........................................................ 113
Port Specification for SQL ...................... 165 
## PREALLOCATE ........................................ 25
## PREAUTOINC ........................................ 190
Profile ...................................................... 205 
## PROP ..... 175, 176, 177, 179, 180, 190, 192,
199, 201, 203, 206, 226, 229 
Alias ........................................................ 197 
AlwaysRebind ......................................... 198 
BusyHandling .......................................... 175 
BusyMessage ......................................... 176 
BusyRetries ............................................. 177 
ConnectString ......................................... 198 
DBMSver ................................................. 198 
Details ..................................................... 199 
Disconnect .............................................. 199 
FullBuild .................................................. 276 
GetInfo .................................................... 179 
GroupBy .......................................... 169, 199 
Having ............................................. 169, 199 
hdbc ........................................................ 200 
henv ........................................................ 201 
Hint .................................................. 201, 226 
Hint, Oracle ............................................. 201 
hstmt ....................................................... 201 
## IGNORETRUNCATION .......................... 180
## INNER ..................................................... 201
IsolationLevel .......................................... 201 
Log .......................................................... 202 
LogFile .................................................... 202 
LoginTimeout .......................................... 202 
LogonScreen ........................................... 201 
LogonScreen (MSSQL Accelerator) ....... 229 
LogonScreen (SQLAnywhere Accelerator )
 ................................................................ 285 
LogonScreen, MSSQL ............................ 229 
LogonScreen, SQLAnywhere ................. 285 


---

Database Drivers 
316 
LogSQL .................................................... 203 
Name ....................................................... 160 
OrderAllTables ......................................... 204 
OrderInSelect ................................... 190, 205 
Profile - SQL ............................................ 205 
QuoteString .............................................. 205 
ServerCaseInsensitive ............................. 206 
## SQL .......................................................... 206
SQLFilter .................................................. 207 
SQLJoinExpression ................................. 209 
SQLOrder ................................................ 210 
## WHERE ................................................... 192
PROP:CreateDB ...................................... 297 
protocol .................................................... 256 
local, IPX, TCP/IP .................................... 256 
## QUICKSCAN ................................... 7, 15, 89
## QUOTE ...................................................... 15
QuoteString .............................................. 205 
readme ..................................................... 252 
READONLY driver switch ........................ 242 
## RECOVER ........................ 41, 51, 65, 75, 97
Registering the Oracle Accelerator.......... 253 
Registering the Oracle Driver in Clarion .. 252 
## SAVESTOREDPROC .............................. 227
## MSSQL .................................................... 227
SAVESTOREDPROC (MSSQL Accelerator)
 ................................................................. 227 
Scalable SQL - see Pervasive SQL......... 250 
Server Side Auto incrementing ................ 144 
ServerCaseInsensitive ............................. 206 
Setup ....................................................... 252 
## SQL .................................................. 165, 206
SQL - Date and Time Columns ............... 145 
SQL - Specify Port ................................... 165 
SQL Accelerator Driver List ..................... 138 
SQL Accelerator Drivers .......................... 107 
Supported Commands and Attributes ..... 165 
SQL Browse Tips .................................... 149 
SQL Driver Behavior ............................... 138 
SQL Driver Properties ............................. 195 
SQL Driver Strings .................................. 170 
SQL Drivers ............................................ 138 
SQL Field Properties .............................. 145 
SQL statements .............................. 132, 281 
Oracle ..................................................... 132 
Scalable SQL .......................................... 281 
SQL Views .............................................. 160 
SQLAnywhere ......................................... 284 
Driver Properties ..................................... 284 
Driver Strings .......................................... 283 
SQLAnywhere Accelerator ..................... 235 
SQLAnywhere Accelerator  Synchronizer 
Server ..................................................... 287 
SQLAnywhere Accelerator Connection 
Information and Driver Configuration--File 
Properties ................................................ 283 
SQLAnywhere Accelerator Driver Properties
 ................................................................ 284 
SQLAnywhere Accelerator Driver Strings283 
SQLAnywhere Accelerator Overview ..... 281 
SQLAnywhere Accelerator SQL Import 
Wizard--Import List Dialog ...................... 282 
SQLAnywhere Accelerator SQL Import 
Wizard--Login Dialog .............................. 281 
SQLAnywhere Accelerator Supported File 
Commands and Functions ...................... 286 
SQLAnywhere Accelerator Synchronizer 
Login Dialog ............................................ 292 
SQLAnywhere logon ............................... 285 
SQLFilter ................................................. 207 
SQLite Accelerator Driver Strings ........... 296 
SQLite Accelerator Supported Commands 
and Attributes .......................................... 293 
SQLite Data types ................................... 296 
SQLite File Driver.................................... 293 
SQLJoinExpression ................................ 209 
SQLOrder ................................................ 210 


---

Index 
317 
Start the SQLAnywhere Client ................. 281 
Stored Procedure - SQLAnywhere .......... 286 
Stored procedures ................................... 165 
Synchronization - SQL Date/Time Imports
 ................................................................. 145 
## TAB .............................................................. 7
## TCF .......................................................... 113
TCP/IP host ..................................... 253, 256 
TIME - Extended ODBC .......................... 145 
## TIMESTAMP ............................................ 145
TopSpeed ................................113, 115, 117 
Driver Strings ........................................... 113 
Other ........................................................ 117 
Supported Commands and Attributes ..... 115 
TopSpeed  Overview ............................... 111 
TopSpeed Database Driver ..................... 276 
TopSpeed Database Recovery Utility...... 122 
TopSpeed File Errors .............................. 122 
TopSpeed Files - Multi-Tables ................. 276 
## TPSFIX .................................................... 122
TPSFIX Command Line Parameters ....... 131 
## TRACE ..................................................... 147
TraceFile .................................................. 211 
## PROP ....................................................... 211
TraceKey ................................................. 212 
## PROP ....................................................... 212
## TRUNCATE ............................................... 25
## TRUSTEDCONNECTION ....................... 228
## MSSQL ................................................... 228
## TRUSTEDCONNECTION (MSSQL
Accelerator) ............................................. 228 
## TURBOSQL ............................................ 190
## USEASYNCHRONOUSCALLS .............. 259
## USEINNERJOIN ..................................... 192
Username ....................................... 253, 256 
Username, SQLAnywhere ...................... 281 
Using Embedded SQL ............................ 165 
Using Embedded SQL(SQLAnywhere 
Accelerator ) ............................................ 285 
Using SQL Tables in your Clarion 
Application .............................................. 165 
Variable file names ......... 216, 229, 283, 286 
## MSSQL ........................................... 216, 229
Scalable SQL .......................................... 283 
Scalable SQL .......................................... 286 
## VERIFYVIASELECT ............................... 192
Version - DBMS ...................................... 198 
View Support for SQL ..................... 160, 169 
What is ADO? ......................................... 300 
What is ODBC ......................................... 237 
## WHERE ................................................... 192
Oracle ..................................................... 259 
## ZERODATE ............................................ 193
## ZEROISNULL ......................................... 194
## ZEROY2K ............................... 51, 65, 75, 97
 
 
