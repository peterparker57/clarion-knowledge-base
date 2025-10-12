 
 
 
 
 
 
 
 
 
 
 
 
 
 
 


---



---

3 
 
COPYRIGHT SoftVelocity Inc. All rights reserved. 
 
 
This publication is protected by copyright and all rights are reserved by SoftVelocity Inc.. It 
may not, in whole or part, be copied, photocopied, reproduced, translated, or reduced to any 
electronic medium or machine-readable form without prior consent, in writing, from 
SoftVelocity Inc.. 
 
 
This publication supports Clarion. It is possible that it may contain technical or typographical 
errors. SoftVelocity Inc. provides this publication ―as is,‖ without warranty of any kind, either 
expressed or implied. 
 
 
 
 
 
 
 
SoftVelocity Inc. 
www.softvelocity.com 
 
 
 
This document supports Clarion ReportWriter 
 
 
 
 
Trademark Acknowledgements: 
SoftVelocity is a trademark of SoftVelocity Inc.  
Clarion 
 
Btrieve 
 
Microsoft Windows, and Visual Basic are registered trademarks of Microsoft Corporation. 
All other products and company names are trademarks of their respective owners. 
 
 
 
 
 
Printed in the United States of America (0610) 
 
 


---

4 
ReportWriter 
 
 
 
 
Table of Contents 
Clarion ReportWriter ........................................................................................................................ 1 
Feature Summary ........................................................................................................................ 1 
Database Design Fundamentals ..................................................................................................... 3 
Database Fundamentals .............................................................................................................. 3 
Anatomy of a Database ............................................................................................................. 3 
File Systems and File Drivers .................................................................................................... 4 
Data Types ................................................................................................................................ 5 
Sorting Data: Keys and Indexes ................................................................................................ 7 
Relationships Between Files  .................................................................................................. 10 
Summary  ............................................................................................................................... 11 
IDE Components  ........................................................................................................................... 13 
Quick Tour of Key ReportWriter Components ............................................................................ 13 
Report Writer Menu Commands ................................................................................................. 14 
Tool Box ...................................................................................................................................... 18 
Field List ...................................................................................................................................... 19 
Group and Sort ............................................................................................................................ 20 
Expression Editor ........................................................................................................................ 21 
External Functions Editor ............................................................................................................ 23 
FilterString Editor......................................................................................................................... 24 
Library Explorer ........................................................................................................................... 27 
Previewer Toolbar ....................................................................................................................... 28 
Property Grid ............................................................................................................................... 30 
Report Explorer ........................................................................................................................... 31 
Report Designer .......................................................................................................................... 33 
Smart Tags .................................................................................................................................. 34 
Total Types - Summary Editor .................................................................................................... 36 
Quick Start Lessons  ...................................................................................................................... 39 
Quick Start Lessons - Introduction .............................................................................................. 39 
Creating Your First Report .......................................................................................................... 41 
Creating Your First Report .......................................................................................................... 41 
Editing a Report .......................................................................................................................... 52 
Relational Reports ....................................................................................................................... 57 
Multi-up Mailing Labels ............................................................................................................... 79 
Reports Wizard  ............................................................................................................................. 93 
Reports Wizard............................................................................................................................ 93 
Reports Wizard - Create a New Dataset ..................................................................................... 94 
Reports Wizard - File Schematic ................................................................................................ 95 
Reports Wizard - Edit Paths ........................................................................................................ 96 
Reports Wizard - Choose Columns ............................................................................................ 96 
Reports Wizard - Grouping Levels .............................................................................................. 97 


---

5 
Table Of Contents 
 
 
Reports Wizard - Report Layout.................................................................................................. 98 
Reports Wizard - Styles .............................................................................................................. 99 
Reports Wizard - Report Title and Finish  ................................................................................ 101 
Advanced Controls  ...................................................................................................................... 103 
Pivot Grid Control  ................................................................................................................ 103 
Using the Pivot Grid Control  ................................................................................................ 106 
Chart Control  ........................................................................................................................... 110 
Using the Chart Wizard  ........................................................................................................ 110 
Chart using a Dynamic Series  ................................................................................................. 124 
Chart using a Static Series  .................................................................................................. 133 
Subreport Control  .................................................................................................................... 140 
Subreport Control  ................................................................................................................ 140 
Advanced Topics  ........................................................................................................................ 143 
Programmer's Guide to ReportWriter  ...................................................................................... 143 
Integrating the Report Engine into Clarion Win32 Applications  ............................................... 144 
Integrating the Report Engine into Clarion.NET Applications  .................................................. 148 
Using the ReportWriter engine from Clarion Win32  ................................................................ 149 
LoadReportLibrary(Load either a REPXL or TXR report library) .......................................... 149 
PrintReport (print a report)  ................................................................................................... 150 
SetPreview (Set report's preview on or off )  ........................................................................ 151 
SetPrinter (Set printer for report)  ......................................................................................... 152 
SetReportFilter(Set Report Filter)  ........................................................................................ 153 
SetReportOrder(Set Report Sort Order)  .............................................................................. 155 
SetVariable (Set a value to a runtime variable)  ................................................................... 156 
UnloadReportLibrary (Unload a ReportWriter Report Library)  ............................................. 157 
Methods only valid with TXR files  ........................................................................................ 158 
Methods only valid with REPXL files .................................................................................... 177 
Using the ReportWriter engine from Clarion.NET .................................................................... 189 
ExportCSV(Export report to a CSV file)  ............................................................................... 189 
ExportHTML(Export report to an HTML file)  ........................................................................ 190 
ExportImage(Export report to an image file)  ........................................................................ 191 
ExportMht(Export report to MHT file)  ................................................................................... 192 
ExportPDF(Export report to PDF)  ........................................................................................ 193 
ExportPDF (Export to PDF with user options)  ..................................................................... 194 
ExportRTF(Export report to a RTF file)  ................................................................................ 196 
ExportText(Export report to Text)  ........................................................................................ 197 
ExportXls(Export report to XLS format)  ............................................................................... 198 
GetReportList(Extract Reports in Library)  ............................................................................ 199 
LoadLibrary(Load Report Library)  ........................................................................................ 200 
OpenReport(Open a report from the Report Library - REPXL file)  ...................................... 201 
PreviewReport(Open Report into Previewer)  ....................................................................... 202 
PrintReport(Send Report to Printer)  ..................................................................................... 203 


---

6 
ReportWriter 
 
 
PrintReportWithDialog(Send Report with Printer Dialog)  ..................................................... 204 
SetOrder (Set Report Sort Order)  ........................................................................................ 205 
SetParameter(Set Report Parameter)  ................................................................................. 206 
SetReportFilter(Set Report Filter)  ........................................................................................ 207 
Scripting  .................................................................................................................................. 209 
Report Writer Scripting ......................................................................................................... 209 
Distribution (of Reports)  .............................................................................................................. 211 
Distributing your Reports  ......................................................................................................... 211 
Using the Runtime Print Engine  .............................................................................................. 213 
How To - FAQs  ........................................................................................................................... 217 
How To - FAQs  ........................................................................................................................ 217 
Adding a Data Source to a Report ........................................................................................... 217 
Adding Images to a Report  ...................................................................................................... 219 
Binding Data to a Report  ......................................................................................................... 221 
Conditionally Change a Control's Appearance  ........................................................................ 227 
Converting your Legacy Reports  ............................................................................................. 231 
Copying and Reusing an Existing Report  ................................................................................ 232 
Changing Connection String of a Data Source ........................................................................ 233 
Creating a Newspaper-style Report  ........................................................................................ 234 
Creating a Runtime Field (adding a report parameter)  ............................................................ 235 
Display Values from a Database (Bind Report Elements to Data)  .......................................... 237 
FormatString and Clarion Picture Editor  .................................................................................. 240 
Lines, Boxes, Circles and Shapes  ........................................................................................... 245 
Placing Text on a Report  ......................................................................................................... 246 
Suppressing a line from printing when empty .......................................................................... 246 
Shipping Examples  ..................................................................................................................... 247 
Shipping Examples  .................................................................................................................. 247 
Shipping Examples  .................................................................................................................. 249 
APPENDIX A - Print and Display Formatting  .............................................................................. 251 
Picture Tokens  ........................................................................................................................ 251 
Numeric and Currency Pictures  ............................................................................................... 252 
Scientific Notation Pictures  ...................................................................................................... 254 
Date Pictures  ........................................................................................................................... 255 
Time Pictures  .......................................................................................................................... 257 
Pattern Pictures  ....................................................................................................................... 259 
Key-in Template Pictures  ........................................................................................................ 260 
String Pictures  ......................................................................................................................... 262 
APPENDIX B - Clarion Functions  ............................................................................................... 263 
Bit Manipulation Functions  ...................................................................................................... 263 
Date / Time Procedures and Functions  ................................................................................... 266 
DOS Procedures and Functions  .............................................................................................. 270 
File Functions  .......................................................................................................................... 271 


---

7 
Table Of Contents 
 
 
Mathematical Functions  ........................................................................................................... 272 
Trigonometric Functions  .......................................................................................................... 276 
String Functions  ...................................................................................................................... 279 
APPENDIX C - Database Drivers  ............................................................................................... 289 
APPENDIX C - Database Drivers  ............................................................................................ 290 
ASCII Files  .............................................................................................................................. 291 
BASIC Files  ............................................................................................................................. 292 
Btrieve Files  ............................................................................................................................. 293 
Clarion Files ............................................................................................................................. 295 
Clipper Files ............................................................................................................................. 296 
dBase III Files  .......................................................................................................................... 298 
dBase IV Files  ......................................................................................................................... 300 
DOS Files  ................................................................................................................................ 302 
FoxPro and FoxBase Files  ...................................................................................................... 303 
ODBC—Open Data Base Connectivity  ................................................................................... 305 
Pervasive SQL  ........................................................................................................................ 309 
TopSpeed Files  ....................................................................................................................... 311 
APPENDIX D - Glossary  ............................................................................................................. 313 
APPENDIX D - Glossary  ......................................................................................................... 324 
Technical Support  ....................................................................................................................... 335 
Product Information  ................................................................................................................. 335 
Product Information  ................................................................................................................. 336 
System Requirements  ............................................................................................................. 337 
The Install Program  ................................................................................................................. 338 
Where to Find More Information  .............................................................................................. 339 
Index  ........................................................................................................................................... 341


---



---

1 
 
 
Clarion ReportWriter 
 
We suggest you start with the Report Wizard Quick Start lesson. 
 
ReportWriter features enable you to: 
 
 
 
Import a Clarion Database Dictionary containing multiple related data files, even if they 
have different file formats. ReportWriter can read TopSpeed, Clarion, Btrieve and 
Btrieve SQL (Pervasive), MSSQL, dBase III or IV, FoxPro, Clipper, ODBC, ASCII, 
BASIC, and DOS files. 
 
Sort data any way you choose and retrieve only those records you select. 
 
Perform mathematical calculations on your data. 
 
Create "error-proof" formulas, conditions, and calculated fields with the Calculated 
Field Editor. 
 
Create "runtime" entry fields—values you enter just before you run a report. These 
values can even be used to perform computations or filters on your data. 
 
Print and export to multiple file formats – automatically attach them to email and send! 
 
Use memo fields and image fields. 
 
Protect your reports and databases with passwords. 
 
Modify your reports to print dates, text, and numbers in any format. 
 
Organize any type of information. You can make a wide variety of reports including: 
inventory reports, payable and receivable reports, customer, client, and vendor 
reports, mailing list labels, form letters, personnel reports... The list goes on and on. 
 
Easily print on labels or pre-printed forms. 
 
Control your report‘s pagination easily, for example, printing a section of your report on 
its own page. 
 
Design reports in a WYSIWYG (What You See, Is What You Get) Designer. All of your 
report‘s elements are shown right on the screen. 
 
Create multiple detail bands. You can print a different detail band for different 
situations, in the same report. 
 
Run a report directly from a Windows Icon or shortcut. You can even supply 
passwords and runtime field values through an Initialization File (.INI). 
 
Immediate Results—Build Your Reports in minutes. 
 
Clarion ReportWriter for Windows‘ Report Wizards will build a report from a Clarion 
dictionary, a data file, or a database. Specify a few options, and your report is ready 
for the printer. 


---

ReportWriter 
2 
 
 
 
 
Database Design Fundamentals 
 
Database Fundamentals 
 
Anatomy of a Database 
A database is a collection of information (data) in a system of files, records, and fields. The 
database is maintained by one or more computer programs or applications. 
The basic unit of data storage is a field. A field is a storage place for information of a similar 
type. For example, one field might store a last name and another field might hold a telephone 
number. You may see the term column used interchangeably with field in documentation. 
A group of different fields that are logically related make up a record. A record contains all the 
information related to one subject. For example, all the fields containing information concerning 
one student (name, address, telephone number, student number, etc.) makes up one student‘s 
record. This would be similar to a file folder a school might keep for each student. Some   
people also refer to a record as a row. 
A collection of logically related records make up a file. Using the same example, a collection of 
all students‘ records makes up the student body file. This would be similar to the file cabinets 
where students‘ folders are kept. The term table is often used to describe a file. 
Another way of looking at this is as a table or spreadsheet: 
 
 
 
 
In this format, the entire table is a file, each row is a record, and columns represent fields. 
A database is a collection of related files (tables). This is similar to a bank of file cabinets 
where the entire school records are kept. One file cabinet might hold the files with students‘ 
personal data, another with class enrollment information, and another with faculty information. 
A database is a collection of tables with defined relationships between them. Effective 
database design breaks the data into related files that are joined together through linking 
fields. This will be covered in detail later in this section. 
 
 
Summary: 
 One or more fields(columns) combine to form a record(row). 
 One or more records(rows) combine to form a file(table). 
 A collection of related files (tables) is a database. 


---



---

ReportWriter 
4 
 
 
 
 
File Systems and File Drivers 
 
There are several data file formats used on PCs. These are the actual physical storage 
formats written to disk by programs that maintain the data files. Through the use of 
SoftVelocity‘s file driver technology, Clarion ReportWriter supports many of them. File drivers 
enable ReportWriter to read these different file formats. ReportWriter also allows file drivers to 
be added as they are needed. 
 
The file drivers provided with ReportWriter, include: TopSpeed, Clarion, MSSQL, ODBC, 
Btrieve, Clipper, dBase III & IV, FoxPro, ASCII, BASIC, and DOS. When you need to read data 
from another file system, you can add new file drivers. Call SoftVelocity‘s Sales department at 
(877) 733-4555 or (954)785-4555 to inquire about the availability of any specific file driver you 
need. 
 
Each file system has its own features and limitations. See the Database Drivers 
Appendix for more information. 


---

Database Design Fundamentals 
5 
 
 
 
 
Data Types 
Fields can store many different types of data, but each individual field may hold only one type. 
When a field is defined, its data type is specified. This enables it to efficiently store that type of 
data. For example, to store a number from 0 to 100, using a field defined as a single BYTE 
takes less space than one defined as a decimal number field (a byte can hold an unsigned 
whole number between 0 and 255). 
ReportWriter supports the following data types: 
Alphanumeric: 
## STRING
A field designed to hold a specific number of alphanumeric and other ASCII 
characters. 
## PSTRING
A field designed to hold a character string, with a leading length byte included in 
the number of bytes declared for the string. This is the type used by the Pascal 
language and the "LSTRING" data type of the Btrieve Record Manager. 
## CSTRING
A field designed to hold a character string terminated by a null character—ASCII 
zero (0). This is the type used in the "C" language and the "ZSTRING" data type 
of the Btrieve Record Manager. 
 
Integers (whole numbers) 
## BYTE
A field designed to hold an unsigned (positive) integer from 0 to 255. 
## SHORT
A field designed to hold a value from -32,768 to 32,767. 
## USHORT
A variation of the SHORT field data type. USHORT is a two-byte field designed to 
hold a value from 0 to 65,535. Negative numbers are not allowed in a USHORT 
field. 
## LONG
A field designed to hold a value from -2,147,483,648 to 2,147,483,647. 
## ULONG
A variation of the LONG field data type. ULONG is a four-byte field designed to 
hold a value from 0 to 4,294,967,295. Negative numbers are not allowed in a 
ULONG field. 
 
 
Floating Point (Real) Numbers (numbers with fractional portion) 
## REAL
A field designed to hold an eight-byte signed floating-point number with 15 
significant digits. 
## SREAL
A field designed to hold a four-byte signed floating-point number with 6 
significant digits. An SREAL field uses the Intel 8087 short real (single precision) 
format. 
## BFLOAT8
A variation on the REAL data type, a BFLOAT8 field is designed to hold an 
eight-byte signed floating point number using the Microsoft BASIC (double 
precision) format. 
## BFLOAT4
A variation on the REAL data type, a BFLOAT4 field is designed to hold a four- 
byte signed floating point number using the Microsoft BASIC (single precision) 
format. 
 
Packed Decimal Numbers 
 
## DECIMAL
A field designed to hold a signed packed decimal format value from - 
9,999,999,999,999,999,999,999,999,999,999    to 
9,999,999,999,999,999,999,999,999,999,999. 


---

ReportWriter 
6 
 
 
 
 
## PDECIMAL
A field designed to hold a signed decimal number in the Btrieve and 
IBM/EBCDIC packed decimal type of format. The only difference between a 
DECIMAL and a PDECIMAL is the place it stores the sign. 
 
Other Data Types 
## DATE
A four-byte field designed to hold a date variable in Btrieve Record Manager 
format. 
## TIME
A four-byte field designed to hold a time variable in Btrieve Record Manager 
format. 
## GROUP
A field made up of two or more fields. For example, a GROUP field called 
PhoneNumber could be made up of two fields: AreaCode and Phone. A Group 
Field gives you the option of using the entire group or any of its components. 
## PICTURE
Although PICTURE is not a data type, when selected, PICTURE declares a 
STRING data type with a picture token (such as @P###P) defining the number of 
characters in the string. The picture token used for the field declaration is entered 
in the Record Picture field. This is useful for data fields whose storage picture  
and display picture must be different. 
 
Next: Sorting Data: Keys and Indexes 


---

Database Design Fundamentals 
7 
 
 
 
 
Sorting Data: Keys and Indexes 
 
 
One of the most powerful aspects of a computerized database is the ability to sort data in 
many different ways. To do this manually requires multiple copies of record forms, many file 
folders, and many file cabinets. It would also require a lot of time spent filing each copy in 
different places for each sort order. 
Sorting computer records in a database merely requires the definition of keys or indexes. Keys 
and indexes declare sort orders other than the physical order of the records within the data file. 
In some file systems the keys are kept in separate disk files, in others they are contained   
within the same file as the data. TopSpeed‘s file driver technology handles these differences 
transparently. 
Keys and indexes are functionally equivalent. The only difference is the way they are 
maintained by an application. 
 
A key is dynamically maintained by the application. Every time a record is added, 
modified, or deleted, the sort sequence is updated, if necessary. 
 
An index is a sort sequence that reflects the contents of a data file at a particular time. 
An index is not dynamically maintained, it is only built when specified. Indexes are 
useful to create sort sequences that are infrequently used, such as month-end or year- 
end processes. 
A dynamic index is a sort sequence created at runtime. The user-defined sorts in ReportWriter 
are dynamic indexes. They are defined for a specific report and are automatically built each 
time that report runs. 
Using the student file example discussed earlier, suppose you wanted to sort the students‘ 
records two ways: by name alphabetically, and by name within each major. This produces two 
alternate sorts. 
 
 
The first example uses a one-component key: the student name. 
 
 
Sorted Alphabetically by Name 
 
 
 


---

ReportWriter 
8 
 
 
 
 
 
The second example uses two components in the key: major and student name. A key can 
contain one or more fields, allowing sorts within sorts. 
 
 
Sorted by major, alphabetically within major 
 
 
 
 
 
 
Ascending and Descending Sort Orders 
Some file systems support both ascending and descending order for keys or components of 
keys. Other file systems only support ascending order, which means the data can only be 
sorted from lowest to highest. 
ReportWriter allows you to create a user-defined sort sequence, in either ascending or 
descending order, no matter what file system you are using. This feature overcomes the 
limitation of some file systems‘ ascending-only keys. Descending order keys can be useful. For 
example, if the records are sorted on a date field, you might want to see the most recent   
record first. 
ReportWriter also gives you the ability to "mix and match" ascending and descending sort 
orders in user-defined sorts. For example, you could sort the student records by descending 
graduation year (the most recent first), and alphabetically (ascending) within those years. 
 
 
By Graduation Year (descending), alphabetically within year 


---

Database Design Fundamentals 
9 
 
 
 
 
 
 
Using Keys as Range Limits 
 
 
Suppose you want to create a class enrollment report from a database containing records for 
the past fifteen years. All you are interested in (for purposes of this report) is the last three 
years. You can dramatically reduce processing time if you use a subset of the data file that 
only contains the records from the last three years. 
Two steps are needed to accomplish this: 
 
First, define a key to sort the data by the date of each course. 
 
Next, define the range limits you are interested in. A range limit specifies a subset of 
the entire file to process. Only those records that fall within the range limits are 
considered. 
In this example, only one-fifth of the records are processed (assuming that each year‘s course 
offerings are the same). Reducing the number of records to consider by 80% reduces 
processing time by the same amount. 
ReportWriter also lets you create multiple ranges. This allows you to specify a subset of  
the records, with more than one range of records in the subset. For example, the student 
records might be sorted by the student‘s home state. If you wanted to consider just the records 
of students from New York and New Jersey, those two ranges could be specified. 
This could also be accomplished with a record filter, but using a subset of the data file reduces 
processing time. 
 
 
See Also: Group and Sort 
 
 
Next: Relationships Between Files 


---

ReportWriter 
10 
 
 
 
 
Relationships Between Files 
 
One goal of relational database design is reducing data redundancy. The basic rule is that data 
should be located in only one place. This is beneficial in two ways. First, it reduces storage 
space requirements. Second, it makes the database easier to maintain. To reach this goal,  
data files are broken up into separate, related files through a process called data   
normalization. 
 
The first step is to move any repeating groups into separate files. For example, if a student 
could take a maximum of six classes, you could design the student file to contain six class 
fields (for class1, class2, class3, etc.). But, not all of these fields would be used in each record. 
If one student is taking six courses, all would be used, but if another student only took one 
class, there would be five empty fields in his record. For that reason, the class fields are  
moved into a separate file, eliminating the need to reserve space for empty fields. 
 
The next step is to move any redundant data into separate files. Every field in the student file 
must be dependant on the primary key (Student Number). The student‘s name, address, and 
phone number would remain in the student file. But the student‘s major‘s data would be moved 
to a separate file. This eliminates the need to repeat the Major‘s Description Field for each 
student that has that Major. To accomplish this, a Major number field is added to the student 
file and is used to create a link to the Majors file. 
 
Once data storage is "normalized," related information is linked by ensuring a field in one file is 
identical to a field in the other. These common fields create the relations between files. A 
linking field could be a student number, a course code, or a classroom number. Any field (or 
group of fields) that uniquely identifies a record in the primary file can be used as a link. 
 
Examples of these relations can be found in the example of the school database: 
 
 
One teacher teaches many classes (One-to-Many). 
 
 
Many students would have one major (Many-to-One). 
 
 
Next: Database Fundamentals Summary 


---

Database Design Fundamentals 
11 
 
 
 
 
Summary 
 
A database is a collection of information (data) in a system of fields, records, and files. 
 
Each data item should be stored in only one place. 
 
One or more fields makes up a record. One or more records make up a file. A 
collection of related files make up a database. 
 
ReportWriter can access many different file systems through the use of file drivers. 
 
Although not all file drivers support both ascending and descending sort orders, 
ReportWriter lets you create either type in user defined sorts. 
 
Keys and indexes declare sort orders other than the physical order of the records 
within the data file. 
 
A key can contain more than one field, allowing sorts within sorts. 
 
Files are joined together in relationships through common fields containing identical 
data. 
 
Fields can store many different types of data, but each individual field is specified to 
hold only one type. 
 
Range Limits enable you to process a subset of records, which reduces processing 
time. 


---



---

13 
 
 
IDE Components 
 
Quick Tour of Key ReportWriter Components 
 
 
This section provides a brief description of the common Report Writer components: 
 
 
 


---

14 
ReportWriter 
 
 
 
 
Report Writer Menu Commands 
 
File Menu 
 
Button/Menu Command 
What it Does 
 
Open 
Opens a Report Library 
 
Save 
Saves the current Report Library. 
 
New 
Creates a New Report Library 
 
Add Report 
Adds a new blank report. 
 
Add With Wizard 
Adds a new report using a detailed wizard. 
 
Add existing Report 
Adds a new report via import of an existing report or legacy 
reports from earlier versions. 
 
Recent Files 
Displays a list of libraries and reports last accessed. Select one 
to open. 
 
Exit 
Closes Report Writer 
 
 
 
Edit Menu 
 
Button/Menu Command 
What it Does 
 
Undo 
Undo the last action. 
 
Redo 
Reapply the last action. 
 
Cut 
Deletes the selected text from the document and places it in the 
clipboard. 
 
Copy 
Places a copy of the selected text from the document into the 
clipboard. 
 
Paste 
Pastes text from the clipboard into the active document, at the 
insertion point. 
 
Delete 
Deletes the selected text from the document and does not place 
it in the clipboard. 
 
Select All 
Selects all controls in the active report. 


---

15 
IDE Components 
 
 
 
 
View Menu – View Tabs 
 
Button/Menu Command 
What it Does 
 
Designer 
Selects the Report Designer. Only visible when a report is 
opened. 
 
Preview 
Opens the Report Previewer. Only visible when a report is 
opened. 
 
HTML View 
Selects the Report HTML View. Only visible when a report is 
opened. 
 
 
 
View Menu - Toolbars 
 
Button/Menu Command 
What it Does 
 
Toolbar 
Opens the main Toolbar, which duplicates all options in the 
IDE File menu.. 
 
Report Settings 
Opens the Report Settings toolbar, which provides access to 
the Parameter Collection Editor, Report (Band) Editor, Printer 
Setup, Report Filter (FilterString Editor), Calculated Field Editor, 
and the External Functions Editor. 
 
Formatting 
Opens the Formatting Toolbar, which controls text font, colors, 
and justification. 
 
Layout 
Opens the Layout Toolbar, which offers 24 different types of 
alignment options. 
 
Status Bar 
Opens the Status Bar, which displays tool tips and other 
related info at the bottom of the page. 
 
Zoom Toolbar 
Opens the Zoom Toolbar, which controls Zoom In, Zoom Out 
and specific zoom percentage control. 
 
Customize 
Allows you to add additional views to the IDE Menu. 
 
 
 
View Menu - Windows 
 
Button/Menu Command 
What it Does 
 
Tool Box 
Opens the Control Tool Box, allowing you to populate report 
controls as needed. 
 
Group and Sort 
Displays the Group and Sort window, which allows dynamic 
sorting and grouping of the selected report. . 


---

16 
ReportWriter 
 
 
 
 
Property Grid 
Displays the Property Grid, which provides detailed 
information of the report component currently selected. 
 
Report Explorer 
Opens the Report Explorer, which provides a hierarchal view 
of all report bands and controls contained within them. 
 
Library Explorer 
Opens the Library Explorer, which provides a view of the 
active library and all reports that are contained within it. 
 
Field List 
Displays a list of all datasets contained in the active report 
library. In addition, computed fields and parameters are also 
displayed. 
 
 
 
Format Menu 
 
Button/Menu Command 
What it Does 
 
Foreground Color 
Controls the control‘s foreground text color. A color dialog is 
displayed for easy selection. 
 
Background Color 
Controls the control‘s background text color. A color dialog is 
displayed for easy selection. 
 
Font 
Set the selected control(s) font style. Select from Bold, Italics, 
or Underline. 
 
Justify 
Set the selected control(s) justification. Choices are Left, Right, 
Center, or Full(Justify). 
 
Align 
Set the selected controls‘ alignment. Align Left, Right, Center, 
Top, Bottom, Middles, or snap to Grid. The control with black 
handles is the base control from which all others are aligned. 
 
Make Same Size 
Set the selected controls‘ size. The control with black handles is 
the base control from which all others are sized. Size by the 
control width, grid, height, or both width and height. 
 
Horizontal Spacing 
Set the selected controls‘ horizontal (left to right) spacing. The 
control with black handles is the base control from which all 
others are sized. You can increase or decrease spacing, space 
all controls equally, or simply remove all spacing. 
 
Vertical Spacing 
Set the selected controls‘ vertical (top to bottom) spacing . The 
control with black handles is the base control from which all 
others are sized. You can increase or decrease spacing, space 
all controls equally, or simply remove all spacing. 
 
Center in Form 
Center a selected control or controls within the parent band that 
it is contained within. Center horizontally or vertically. 
 
Order 
If one control is on top of another, you can send it to the back or 


---

17 
IDE Components 
 
 
 
 
bring it to the front. This determines which control will be 
displayed first. 
 
 
Help Menu 
 
Button/Menu Command 
What it Does 
 
Contents 
Displays the ReportWriter Help (this document). 
 
About Clarion Report 
Writer 
Contains company, version, and licensing information. 


---

18 
ReportWriter 
 
 
 
 
Tool Box 
 
 
The Tool Box contains all of the available controls that you can use on your reports. Here is a 
brief summary of each control, and how it is used. 
 
Label 
Allows inserting single-line or multi-line text into a report. Note that this text 
may be either static, or dynamically populated from a report's data source. 
Check Box 
Intended to display a True/False or Checked/Unchecked/Indeterminate state 
in a report. 
Rich Text 
Intended to display, enter and manipulate formatted text. You can enter and 
format its text at design time, load it from an external file, or bind this control 
to a data field. 
Picture Box 
Displays an image in a report. Use this control to insert images of different 
types into your reports. 
Panel 
Used to contain other report controls. Use it to group controls together and 
to make their manipulation easier. 
Group Box 
Also used to group other report controls. 
Table 
Inserts a table (containing rows and cells). This control is invaluable if you 
need to show your data in tabular form. 
Line 
Draws vertical, horizontal or diagonal lines in a report. 
Shape 
Embeds any simple graphics into a report. There are 23 different shapes 
available with this control. 
Bar Code 
Allows you to insert many different bar code types into a report. Currently 
there are 20 different symbology types. 
Zip Code 
Allows the insertion of numbers representing a zip code into a report. 
Chart 
Used to represent your data in a graphical view. For more information, refer 
to the Chart Control section. 
Pivot Grid 
Represents data from an underlying data source in a cross-tabulated form to 
create cross-tab reports. 
Page Info 
Displays auxiliary information in a report, for example, page numbers, the 
current date or user information. 
Page Break 
Serves to mark the place where a report should start a new page. Use as an 
alternative to setting the Page Break property. 
Cross-band 
Line 
A line control, which draws itself through the report bands. 
Cross-band 
Box 
A box control, which draws itself through the report bands. 
Subreport 
Used to insert one report into another. For example, this control may be  
used when a subreport contains some basic information which must be used 
in other reports. This control is also intended to create master-detail reports. 
For more information on how this can be done, refer to the Creating 
Subreports topic. 


---

19 
IDE Components 
 
 
 
 
Field List 
This window displays the schema of the data used in your report. 
 
 
 
 
 
Also, this window may be used to bind existing report controls to data, or to create new bound 
report controls. To do this, simply click the desired field item in the Field List window and then 
drag and drop it onto the report band, or a bindable report control. 
 
 
Right-click and drag to report for optional field type selection. For example, using the TEA:ZIP 
field shown above, you can right-click and drag and drop to the report, and a selection of 
possible controls to assign is displayed: 
 
 
 


---

ReportWriter 
20 
 
 
 
 
Group and Sort 
The Group and Sort panel controls the dynamic grouping and sorting options of the active 
report. 
 
 
 
 
 
This panel is automatically displayed each time the Report Designer is opened. It can be 
floating as shown above or docked anywhere in the ReportWriter IDE. 
 
 
This dialog eliminates the need to manually add group header and footer bands. After adding a 
sort element, check the Show Header and/or Show Footer check box to dynamically create a 
Group Header or Footer for the selected element. 
 
 
Note: With regards to the ReportWriter, Grouping and Sorting are very similar. The only 
difference is that adding a Group implicitly adds a Group Header by default. 
 
 
See Also: Sorting Data: Keys and Indexes 


---

IDE Components 
21 
 
 
 
 
Expression Editor 
 
The Expression Editor helps you to quickly generate a syntactically correct expression. You 
can use the Expression Editor to create computed (or calculated) fields. 
 
A computed field receives the value of an expression. In other words, a computed field is the 
receiving end of a simple assignment statement: variable = expression. For example, a 
computed field called GrossPrice might receive the result of adding two fields called BasePrice 
and Tax. 
 
You can use a computed field wherever the report needs the result of a calculation. 
 
The Expression Editor dialog gives you access to data dictionary fields, as well as runtime 
fields and report specific fields (parameters), and facilitates creating syntactically correct 
expressions. This is its prime advantage: automatic syntax checking. 
 
To create an expression, you press buttons and make selections to add expression 
components to the Statement box. You can also type in your expression and check the syntax 
after. 
 
The Expression property is available from the CalculatedField Collection Editor: 
 
 
 
 
 
1. Press the ellipsis button. This opens the Expression Editor. 


---

ReportWriter 
22 
 
 
 
 
 
 
 
2. In the Statement text box on top, create your formula. 
 
You can manually type in the expression, use the Expression Editor's buttons, or both. The  
first component of an expression must be an operand, a left parenthesis, or a unary minus (the 
negative sign). For example, select the Fields category and choose a variable, press the 
Multiply by (X) button, and then select the Clarion Built-In Functions category to choose a 
Clarion built-in function. 
 
If the syntax is incorrect, a message box will appear that identifies the column position of your 
error. 
 
3. Press the OK button to save your expression and close the editor. 


---

IDE Components 
23 
 
 
 
 
External Functions Editor 
The External Functions Editor is used to add functions located in external DLLs to your report. 
Press the Add button to add an external function to the list. This function will be accessible 
from the Expression Editor for use in Calculated Fields, and the Calculated Field in turn 
available in the Field List for population. 
 
 
The following property options are available: 
 
 
Description 
Enter descriptive text that will describe in detail what the external function is intended to do. 
 
Entry Point 
Valid for Win32 libraries only. Enter the Entry Point name the function requires. 
 
Note: The Entry Point is the value of the functions NAME attribute. If the NAME attribute 
is not used, you must provide the unique mangled name found in the library’s Export 
file. 
 
Name 
Enter the Name of the function that will actually be used in the expression 
 
Number of parameters 
Enter the number of parameters that the function requires. Your expression must include the 
same number of parameters 
 
Path 
Select the path and filename of the DLL to use. 


---

ReportWriter 
24 
 
 
 
 
FilterString Editor 
 
This section describes the capabilities provided by the Filter Editor, which allows users to 
visually build filters: 
 
The Filter Editor is used to edit filter criteria. To create and customize filter criteria, use the 
 
and 
 buttons embedded into the control and context menus supported by the editor's 
elements: 
 
 
 
 
 
A filter condition group is a set of conditions combined by the same logical operator. 
 
Add Conditions 
 
To add a condition to a logical group, do one of the following: 
 
 
Focus any condition within the group or the group's logical operator and then press 
INSERT or ADD on the keyboard. 
 
 
Click the 
 button for the group. 
 
 
Click the group's logical operator and select Add Condition. 
 
To add a condition or a group of conditions that have been copied to the clipboard, press 
CTRL+V or SHIFT+INSERT. The new condition will be added to the focused group. 
 
 
Delete Conditions 
 
To delete a condition, do one of the following: 
 
 
Focus the condition and press DELETE or SUBTRACT. 
 
 
Click the 
 button. 
 
 
To delete a group of conditions, do one of the following: 
 
 
Focus the group's logical operator and press DELETE or SUBTRACT 
 
 
Click the group's logical operator and select Remove Group. 


---

IDE Components 
25 
 
 
 
 
To delete all conditions, do one of the following: 
 
 
Focus the topmost logical operator and press DELETE or SUBTRACT. 
 
 
Click the topmost logical operator and select Clear All. 
 
To cut a condition/group of conditions to the clipboard, focus this condition or the group's 
logical operator and press CTRL+X or SHIFT+DELETE. 
 
 
Clipboard Operations 
 
To copy a condition or a group of conditions to the clipboard, focus this condition or the group's 
logical operator and press CTRL+C or CTRL+INSERT. 
 
To cut a condition or a group of conditions to the clipboard, focus this condition or the group's 
logical operator and press CTRL+X or SHIFT+DELETE. 
 
To paste a condition or a group of conditions from the clipboard to the focused group, press 
CTRL+V or SHIFT+INSERT. 
 
 
Change a Column in a Filter Condition 
 
To change a condition's column, invoke the column list by doing one of the following: 
 
 
Click the current column. 
 
 
Focus the current column via the keyboard and press SPACE or ALT+DOWN 
## ARROW.
 
Then, choose the required column from the list that will be invoked 
 
 
Change an Operator in a Filter Condition 
 
To change a condition's operator, invoke the operator list by doing one of the following: 
 
 
Click the condition's current operator. 
 
 
Focus the current operator via the keyboard and press SPACE or ALT+DOWN 
## ARROW
 
Then, choose the required operator from the list that will be invoked 
 
 
Edit a Condition's Value 
 
To edit a condition's value, click the operand value and type text. 
 
To activate the operand value's edit box without changing the value, click the value or focus 
the operand value via the keyboard and press F2, SPACE, ENTER or ALT+DOWN 
 
To close the active edit box, press ENTER. 
 
To discard changes to the value and close the active edit box, press ESC. 
 
 
Navigation 
 
To focus a specific filter condition or a group's operator within the Filter Editor, do one of the 
following: 
 
 
Click the target element. 


---

ReportWriter 
26 
 
 
 
 
 
Use arrow keys to move focus via the keyboard. 


---

IDE Components 
27 
 
 
 
 
Library Explorer 
The Library Explorer is used to display the active library and its available reports. All reports 
are shown in a simple tree control. Using the popup menu, right click on any report to open it, 
rename it, remove it, or copy it: 
 
 
 
 
 
Right-clicking on the Library node displays an alternate menu: 
 
 
 
 
 
Essentially the choices shown above mirror the same options found in the IDE File menu. 


---

ReportWriter 
28 
 
 
 
 
 
 
Previewer Toolbar 
 
 
The Previewer toolbar contains a feature rich set of options to apply to your active report: 
 
 
 
Search 
Search your report for any text. You can set the search criteria to Match 
                              Case, Match Whole Word, or Search Up. 
 
Open 
Open any Previewer File Format (*.prnx) that you have previously 
saved. 
 
 
Save 
Save the current Preview to an external file. The native format of the 
Previewer file uses an extension of PRNX. 
 
 
Print 
Displays the Printer Dialog prior to printing. 
 
 
 
QuickPrint 
Prints to the default printer directly. No Printer dialog is diplayed. 
 
 
 
PageSetup 
Controls Paper Size and default printer paper source, paper orientation, 
and default margins. 
 
 
Scale 
Allows you to scale your report as either a percentage of the actual 
size, or the number of pages to display in width. 
 
 
HandTool 
Changes your cursor from the default arrow to a "hand" cursor. You can 
click and drag your preview page up or down as needed. 
 
 
Magnifier 
Changes your default cursor to a "magnifier" cursor, where clicking on a 
selected area of the preview page activates an instant zoom to that 
particular detail. 
 
Zoom Out 
Dynamically increases the size of the viewing area of the report, 
resulting in smaller text display. 
 
 
Percentage        Serves a dual purpose. Using the drop list you can instantly modify the 
zoom setting. In addition the percentage value always reflects the size 
of the current Zoom Out or Zoom In setting. 
 
Zoom In 
Dynamically decreases the size of the viewing area of the report, 
resulting in larger text display. 
 
 
Page Navigation 
Use these buttons to move to the First Page, Previous Page, Next 
Page, or Last Page respectively. 


---

IDE Components 
29 
 
 
 
 
 
 
Multiple Pages 
Using this setting, you can view more than one page in the Preview 
window. Moving the mouse inside of the Multiple Pages window 
increases the available matrix to display. 
 
Background 
Color 
 
Sets the background color of the report. 
 
 
Watermark 
Allows you to set a watermark for the active report. Add color or text or 
picture or a combination of the three. Set the transparency depth, what 
pages to watermark, and whether to position it on top of or below the 
text. 
 
Export Document 
Export the active report to one of the following file formats: PDF 
(Portable Document Format), HTML (Hypertext Markup Language), 
MHT (MIME HTML), RTF (Rich Text Format) , Excel, CSV (Comma 
Separated Values), text, and any of the following image formats (BMP, 
EMF, WMF, GIF, JPEG, PNG, TIFF). Each option has a variety of 
export options, like encoding and other format variations. 
 
Send via Email 
Exports the file and attaches it to your default email client, ready to 
send. Export the active report to one of the following file formats: PDF 
(Portable Document Format), MHT (MIME HTML), RTF (Rich Text 
Format) , Excel, CSV (Comma Separated Values), text, and any of the 
following image formats (BMP, EMF, WMF, GIF, JPEG, PNG, TIFF). 
Each option has a variety of export options, like encoding and other 
format variations. 


---

ReportWriter 
30 
 
 
 
 
Property Grid 
The Property Grid is used to change the properties of the report elements (bands and controls) 
as needed. All modifiable elements of controls, bands, and the report itself are displayed here: 
 
 
 
 
 
At the top of the Property Grid, a drop list of all report controls is displayed. You can use this 
control to quickly select a control you are looking for in a very large report. 
 
The Property Grid can be sorted by categorized or alphabetical view of all properties. 
 
Some properties are simple entry control values, while others provide an ellipsis to select 
external values to apply to the property. Examples of this might be a Font setting, or selecting 
the name of a file. 
 
Finally, at the bottom of the Property Grid is a concise and accurate description of the property 
and in some cases what it is used for. 


---

IDE Components 
31 
 
 
 
 
Report Explorer 
The Report Explorer provides a detailed view of all bands and control used in the active report. 
Selecting an element in the Report Explorer selects an element in the Report Worksheet. 
 
 
 
 
 
The Report Explorer provides easy navigation through report elements. You can use it when 
building a report to quickly access all the elements of a report and their properties, and to see 
the whole report's structure. 


---

ReportWriter 
32 
 
 
 
 
Right-clicking on any component in the Report Explorer provides you with a wide selection of 
useful elements. The items displayed are dependent on what element you have selected. For 
example, if you highlight the main Report node, and right-click: 
 
 
 


---

IDE Components 
33 
 
 
 
 
Report Designer 
 
 
This topic contains information about the basic principles of creating reports with Report 
Designer. 
 
The Report Designer allows you to create new reports from scratch, specify a data source, and 
output them to a variety of different formats. In addition to report editing capabilities, it allows 
you to display its Print Preview and send its output to a printer or export it to a file on disk. 


---

ReportWriter 
34 
 
 
 
 
Smart Tags 
The smart tag feature enables report controls and bands to display context-sensitive 
information and commands. The most common and useful elements of the target report 
component is displayed. 
 
To invoke a smart tag, you first need to select any report element, and then to click the smart 
tag icon (looks like a right arrow) of the currently selected report element. Then, the smart tag 
panel is invoked on the right side of the smart tag icon, allowing you to quickly adjust the 
selected report element. 
 
 
The smart tag feature is available for the following report elements. 
 
 
Report 
A report's smart tag icon is located at the top left corner of the report designer. 
 
 
 
 
 
Report Bands 
A report band's smart tag icon is located on the band strip right next to the caption. For 
instance, the smart tag for the Report Header band is shown in the image below. 
 
 
 


---

IDE Components 
35 
 
 
 
 
Report Controls 
A control's smart tag icon is located at the top right corner of the control. For instance, the 
smart tag for the label is shown in the image below. 
 
 
 
 
 
Each control's smart tag prompts will vary based on the control type. For example, here is the 
picture box: 
 
 
 


---

ReportWriter 
36 
 
 
 
 
Total Types - Summary Editor 
"Total" Fields in the Clarion ReportWriter can be found in the Summary Editor. 
 
 
There are 21 Summary Functions listed. 
 
Avg 
Calculates the average of all the values within the specified summary region 
(group, page or report). 
 
Count 
Counts the number of values within the specified summary region (group, 
page or report). 
 
Custom 
Calculates the custom summary using the XRLabel.SummaryReset, 
XRLabel.SummaryRowChanged and XRLabel.SummaryGetResult events. 
 
DAvg 
Calculates the average of all the distinct values within the specified 
summary region (group, page or report). 
 
DCount 
Counts the number of distinct values within the specified summary region 
(group, page or report). 
 
DStdDev 
Calculates the standard deviation of all the distinct values within the 
specified summary region (group, page or report). 
 
DStdDevP 
Calculates the standard population deviation of all the distinct values within 
the specified summary region (group, page or report). 
 
DSum 
Calculates the total of all the distinct values within the specified summary 
region (group, page or report). 
 
DVar 
Calculates the amount of variance for all the distinct values within the 
specified summary region (group, page or report). 
 
DVarP 
Calculates the population variance of all the distinct values within the 
specified summary region (group, page or report). 
 
Max 
Calculates the maximum of all the values within the specified summary 
region (group, page or report). 
 
Median 
Finds the middle number within a sequence. If the total number of elements 
is odd, this function returns the value of a middle number in a sequence. If 
the total number of elements is even, this function returns the arithmetical 
mean of the two middle numbers. 
 
Min 
Calculates the minimum of all the values within the specified summary 
region (group, page or report). 
 
Percentage 
Calculates the percent ratio of the current data row's value to the total of all 
the values within the specified summary region (group, page or report). 
 
RecordNumber 
Returns the current record number in the datasource within the specified 
summary region (group, page or report). This means for instance, if the 
summary is calculated for a group, then the record number is calculated 
only within that group, and is reset every time a new group is started. 


---

IDE Components 
37 
 
 
 
 
RunningSum 
Summarizes all the values, which were printed before the current data row, 
with the current data row's value. 
 
StdDev 
Calculates the standard deviation of all the values within the specified 
summary region (group, page or report). 
 
StdDevP 
Calculates the standard population deviation of all the values within the 
specified summary region (group, page or report). 
 
Sum 
Calculates the total of all the values within the specified summary region 
(group, page or report). 
 
Var 
Calculates the amount of variance for all the values within the specified 
summary region (group, page or report). 
 
VarP 
Calculates the population variance of all the values within the specified 
summary region (group, page or report). 


---

 
 
 


---

39 
 
 
Quick Start Lessons 
 
Quick Start Lessons - Introduction 
In the following Quick Start lessons, you will create some sample reports from existing data 
files. These lessons should only take two to three hours to complete. 
 
 
 
The starting files are in the Examples\ReportWriter\REPXL Reports\RWTutor\School\ 
subdirectory (unless you specified another base installation directory during installation). 
 
 
The completed lessons are located in: 
Examples\ReportWriter\REPXL     Reports\RWTutor\School\Solution. 
 
 
 
After completing these Quick Start lessons, you will know how to: 
• Start ReportWriter 
• Create a Report Library based on a Data Set 
• Create reports 
• Design the report‘s layout 
• Place fields 
• Format data using calculated Fields 
• Place page headers on a report 
• Use horizontal and vertical lines to separate elements of a report 
• Preview a report 
• Print a report 
• Save a report 
• Copy and modify reports 
• Change a report‘s sort order 
• Move and Delete controls 
• Use the Label Wizard to create Mailing Labels 


---

40 
ReportWriter 
 
 
 


---

Quick Start Lessons 
41 
 
 
 
 
Creating Your First Report 
 
 
Starting ReportWriter 
After installing ReportWriter: Choose Start > Clarion 7 > ReportWriter. 
 
 
 
Creating your First Report 
 
 
Step 1 - Create an empty report library 
From the IDE Menu, select File > New, or press the New Toolbar button as shown below (you 
can also press CTRL + N) 
 
 
 
All reports that you will create will be stored in a report library. Navigate to the … 
ReportWriter\REPXL Reports\RWTutor\School\ folder, and name your first library 
GettingStarted. A library named GettingStarted.repxl will be created. 
 
 
 
All new libraries created with ReportWriter use a file extension of *.REPXL 
 
 
Step 2 - Create your first report 
There are three ways to create a new report. We will use the Add With Wizard option in this 
Quick Start lesson. 
 
 
 
1. File > Add Report 
Create a report from scratch. A blank report is created for you, and from there you can build 
the report from the ground on up. 


---

ReportWriter 
42 
 
 
 
 
 
2. File > Add with Wizard 
In this Getting Started section, we will use this option. This option is the fastest way to kick 
start a report design. 
 
 
3. File > Add Existing Report 
This option allows you to import an existing report created from another library. 
All report that you create are saved in associated REPX files. This option allows you to import 
an existing report file into your active library. 
 
 
 
Step 3 - Select your first report type 
 
 
As we stated in Step 2, let's use the Add with Wizard option to create our first report. From 
the IDE Menu, select File > Add with Wizard. You can also use the toolbar button shown 
here: 
 
 
 
The opening wizard window is now displayed: 
 
 
 
You have two types of reports available via the Reports Wizard; Standard and Label Reports. 
In this section we will select the Standard Report option, and then press the Next button. 


---

Quick Start Lessons 
43 
 
 
 
 
 
 
Step 4 – Get the data that your report will use 
 
 
Before we continue with our report design, the first and most important requirement for the 
report is to identify the data that will be used. After selecting the type of report we will create, 
the following dialog is displayed: 
 
 
 
 
 
The dataset name is simply the name we will use to identify our data source. As our Report 
Library grows with new reports, it will be very likely that we will have multiple datasets available 
for different reports. When specifying the dataset name you need to avoid special characters, 
such as: whitespace, !, #, %, $, ^, &, *, (, ), -, +, =, \, /, etc. 
 
 
Since we will be creating a "Student List" report in this example, enter Students in the Enter a 
dataset name entry, and then accept the default Clarion Data Source (Dictionary) option as 
shown above. The Standard Data Source is used to connect to ODBC and SQL data sources 
(or essentially any data that does not use a Clarion dictionary), and will be covered in more 
detail later in this document. For now, we will be using a Clarion dictionary, so press the Next 
button to continue. 
 
 
 
Data Dictionaries (DCT) files are a data repository of tables to use in your reports. They are 
created using the Clarion 7 product produced by SoftVelocity. In the core ReportWriter 
product, we have provided several sample DCTs in the lessons and examples. 


---

ReportWriter 
44 
 
 
 
 
In the next dialog, press the Configure File Schema (e.g., Dictionary) button to select your 
dictionary. 
 
 
In the …ReportWriter REPXL Reports\RWTutor\School folder, select the SCHOOL.DCT 
dictionary file. 
 
 
After the dictionary is selected, the File Schematic dialog is now displayed: 
 
 
 
 
 
 
Press the Add button in the File Schematic dialog, and select the Students file as shown 
below: 
 
 
 
 
 
Press OK to add the Students file to the File Schematic window. 


---

Quick Start Lessons 
45 
 
 
 
 
That is all that we wish to add right now. In this Getting Started, we will create a simple 
"Student List". 
 
 
 
In the File Schematic window, press the Paths button. The following dialog is now displayed: 
 
 
 
This dialog is useful when your data is located in a different location from the report library. 
Press the ellipsis to the far right of the Students row and select the path as shown above. 
Additionally, check the Store As Relative checkbox. This makes the path relative to the report 
library, and allows later for easier distribution of your reports to a different folder or a machine. 
Press OK to close the Edit Paths window and return to the File Schematic window. 
 
 
 
In the File Schematic window, press OK to return to the Select Dictionary dialog, and then 
press the Next button to proceed to the "Choose Columns... dialog as shown here: 
 
 
 


---

ReportWriter 
46 
 
 
 
 
Use the arrow keys to move your columns to print from the left side to the right. When you are 
satisfied with your selections, press the Next button. 
 
 
The next dialog allows you to create Group Breaks in your reports, which will be generated 
when the column that you select changes. 
 
 
 
In our simple Getting Started example, no grouping is needed at this time. Press the Next 
button to continue. 
 
 
Step 5 – Set up your layout and style 
 
 
Note: 
If you had selected any Grouping options, the next dialog would be a list of Summary options. 
This dialog will be explained in more detail in the Summary Options section of this document. 
 
 
The next dialog that you should see is the Report Layout: 


---

Quick Start Lessons 
47 
 
 
 
 
 
Columnar layout displays the fields you specified in a single column display. A visual image of 
the layout is displayed to the left as shown above. 
 
 
Tabular layout displays the fields you specified across the page in a single row. The field width 
option will try to fit all of the fields on a single page. 
 
 
Justified layout measures the size of each field that you specified and will wrap the columns 
to the next line to fit all information neatly. 
 
 
More layout options are also available if you had selected report grouping. Each of these 
layouts will be covered in more detail in the Layout Options section in this document. 
 
 
In addition, you can also select the orientation of your report in this dialog. Select from Portrait 
or Landscape. 
 
 
Select the default Columnar layout and press the Next button to continue. 
 
 
The next dialog in the Reports Wizard allows you to set one of several predefined styles, as 
shown as follows: 


---

ReportWriter 
48 
 
 
 
 
 
 
As shown above, select from one of the different default styles for your report. After selecting a 
style (we chose Casual), press Next to continue. We are almost finished! 
 
 
The last dialog presented is provided to simply provide a title for your report. 


---

Quick Start Lessons 
49 
 
 
 
 
 
 
Step 6 – Final Touches and Preview 
After you give your report a descriptive name, press the Finish button to complete your report. 
If prompted to save your changes, press the Yes button. Let's name our new report: 
StudentList.Repx. This is the default file format for each of your reports. 
 
 
At this time, access the Library Explorer and optionally give your report a descriptive name: 
 
 
 
 
 
The Design Worksheet should now be displayed: 


---

ReportWriter 
50 
 
 
 
 
 
 
At this time, you can fine tune your report if necessary. For example, you might want to change 
the report prompts to use a more descriptive name. To do this, simply double-click on the 
prompts that you wish to edit and make the necessary changes. 
 
 
 
To Preview your report, press the Preview button (tab) located on the View Tabs: 
 
 
 
This will open the Previewer and the many options of the Previewer toolbar. You can search 
through your report, add watermarks, but most important, redirect the output to a variety of file 
formats in addition to simply printing the report. 
 
 
Step 7 – Output Options 
 
 
To print the report, press the Print button: 
 
 
 


---

Quick Start Lessons 
51 
 
 
 
 
Note that there are two print buttons available. The button with the question mark allows you to 
select a printer prior to printing. The other button simply uses your default printer and prints 
immediately. 
 
 
To export the report to a designated file format: 
 
 
 
To attach the document to your default email client: 
 
 
 
Next: Editing a Report 


---

ReportWriter 
52 
 
 
 
 
 
 
Editing a Report 
This topic documents some common tasks used when editing a report, and continues from the 
Creating Your First Report topic: 
 
 
 
If you choose to skip the first lesson, no problem. 
In the ReportWriter\REPXL Reports\RWTutor\School\Solution folder, there is a copy of the 
GettingStarted REPXL library, and you can load this and continue with this lesson. 
 
 
Task One: Changing the Format of a Data Field 
What if you need to change the display of any report element? For example, what if you need 
to change the length of a picture? 
 
 
In the Report Designer: 
1. Click on the STU:LASTNAME control's smart tag as shown below: 
 
 
 
 
 
2. CLICK on the Format String entry box and type @S30 to increase the picture length. 
 
 
3. Press the Smart Tag button again to close the Label Tasks window. 
 
 
More information regarding Clarion Picture tokens can be found in the Picture Tokens section 
of this document. 


---

Quick Start Lessons 
53 
 
 
 
 
Task Two: Deleting Fields and Controls from a report 
Let's delete the controls for the Student First and Last Name and their associated prompts. 
Our intention is to create a new calculated Field that joins the two fields together. 
 
 
1. CLICK on the STU:LastName control, then press DELETE (or RIGHT-CLICK on the 
control and choose Delete from the popup menu). 
 
 
 
 
 
2. CLICK on the STU:FirstName control, then press DELETE (or RIGHT-CLICK on the 
control and choose Delete from the popup menu). 
 
This removes the two fields that you will replace with the calculated field. Next, you will delete 
one Column heading and modify the other. 
 
3. CLICK on the label control that says "First Name," then press DELETE. 
4. Finally, DOUBLE-CLICK on the Label control that says "STU:LastName" . This 
enables in-place editing. Edit it to read "Name." 
 
 
Since the calculated field prints each Student‘s full name, you only need the single column 
heading. 


---

ReportWriter 
54 
 
 
 
 
Task Three: Creating a Calculated Field 
Next, create a calculated field that removes the trailing spaces from the Last Name, then add a 
comma, a space, and the first name. 
1. Press the 
 button on the toolbar. 
The Calculated Field Collection Editor window appears. 
2. Press the Add button. A default calculatedField1 appears in the Members list. 
3. In the Properties (Name) entry box, type FullName. 
This provides a unique label that ReportWriter uses to reference the calculated field. 
4. In the Expression property, press the ellipsis button to open the Expression Editor to 
create the calculated field‘s formula. 
The Expression Editor appears. The Expression Editor helps you to quickly generate a 
syntactically correct expression. 
5. Highlight Clarion Built-In Functions in the list box on the left, then highlight CLIP(string) 
in the list box on the right, then DOUBLE-CLICK to add to the formula worksheet at the 
top. 
 
 
 
 
 
The CLIP function removes trailing spaces from a field. Remove the single quotes in the 
parentheses shown above, and then leave your cursor between the parentheses for the next 
step. 
6. Highlight Fields in the list box on the left, then highlight STU:LastName in the list box 
on the right, and then DOUBLE-CLICK to add to the formula worksheet at the top. 
These two steps remove the trailing spaces from the LastName field. 


---

Quick Start Lessons 
55 
 
 
 
 
7. Press the END key to move the cursor to the end of the expression, then enter & in 
the Formula Worksheet. 
This inserts the concatenation operator into the expression to append one string to 
another. 
8. To the right of the concatenation operator, type a single quote followed by a comma 
followed by a space followed by another single quote. 
This inserts ‗, ‗ into the expression. 
9. Press the END key to move the cursor to the end of the expression, then enter & in 
the Formula Worksheet. 
10. Highlight Fields in the list box on the left, then highlight STU:FirstName in the list box 
on the right, and then DOUBLE-CLICK to add to the formula worksheet at the top. 
 
 
 
 
 
This completes the expression. As you become familiar with expression syntax you can simply 
type in your expression or any portion of it. 
 
 
11. Press the OK buttons on the Expression Editor and the CalculatedField Collection 
Editor dialogs. 
This returns you to the Report Designer. The calculated field you just created will 
appear in the Field List, ready to populate in the next Task. 


---

ReportWriter 
56 
 
 
 
 
Task Four: Populating a Calculated Field 
1. Open the Field List (or choose View > Windows > Field List). 
The Field List appears. This toolbox allows you to quickly place controls on your report. 
ReportWriter‘s toolboxes are adjustable—you can resize and reposition them by clicking-
and-dragging any edge or corner of the toolbox. 
2. Highlight FullName , then DRAG to the location of the report where you want to place 
the field. 
The point of the Arrow on the mouse cursor positions the upper left corner of the field. 
This should be in the location formerly occupied by the STU:LastName field. 
 
 
Your report is complete. You can preview the report to see the result. 
 
 
1. Click the Preview tab on the View Tabs to run the report in Preview Mode. 
 
 
 
 
 
The Report Preview appears, displaying the first page of your report. 
2. Use the Page button on the toolbar to turn pages. 
3. When you are finished, press the Designer button on the View Tabs to exit the Report 
Preview. 
 
 
This returns you to the Report Designer. 
4. Press the Save button on the toolbar to save the Report Library. 
 
 
 
 
You can find the solution to this section (GettingStarted2.REPXL) in the following folder: 
ReportWriter\REPXL    Reports\RWTutor\School\Solution 
 
 
Next Lesson: Relational Reports 


---

Quick Start Lessons 
57 
 
 
 
 
 
 
Relational Reports 
The reports in the first Quick Start lesson used a single file. The reports in this lesson use 
multiple files, using ReportWriter‘s Relational capabilities. ReportWriter directly accesses data 
files in a Relational manner when you specify related files in the File Schematic. 
When creating relational reports, a little planning in advance can save a lot of time. 
 
 
Planning 
To start, visualize your report. 
 
What data will print on the report? 
 
What files will provide the data? 
 
Is a user-defined sort order necessary? 
 
Which records should be grouped together? 
 
How should it look? 
 
 
Let‘s take these questions one-by-one. 
 
 
What data will print on the report? 
In this lesson, you will create an enrollment report. For this report, you want the Course 
Description and the Complete Description from the Courses file: 
 
Course Description 
Complete Description 
 
 
Next, the report should show the specific classes for each course. This comes from the 
Classes file: 
 
 
RoomNumber 
Scheduled Time 
Teacher Name 
Class Number 
 
 
Next, the report should contain the information for each student enrolled in the class. This 
comes from the Enrollment file: 
 
Student Number 
Student Name 
Midterm Grade 
FinalExam 
TermPaper 
 
 
Finally, the report should also provide: 
 
 
A Final Grade for each student 
The number of Students in each class 
The number of Students in each course 
The Average Grade for each Class 


---

ReportWriter 
58 
 
 
 
 
 
What files will provide the data? 
 
 
This report uses three related files to define the basic report structure and two lookup files to 
access more information. 
 
 
The basic report structure: 
 
 
 
In addition, the teacher file allows a lookup through the teacher number link field. This lets you 
print the teacher‘s name at the top of each Class. 
 
 
 
The Student file allows a lookup through the Student number link field. This lets you print the 
student‘s name on each detail (enrollment) band. 
 
 
 
Is a user-defined sort order necessary? 
The Course file has an established key sorting the records by Course Description. This allows 
you to create the report of Courses in alphabetical order. The report accesses the class 
records, sorted by course, allowing the records to be grouped together. The Enrollment file 
contains a key sorted by Class Number, allowing the records to be grouped together. These 
keys provide the sort orders necessary for the report. 
 
 
Which records should be grouped together? 
"Group Breaks" place records together in groups based on the value contained in one or more 
of the record‘s fields. This gives you a Group Header band and allows you to make a Group 
Footer band. These bands allow you to print at the beginning or end of each group of records. 
In this report, you want all the records for each Course grouped together. The key sorting the 
Course records by Course Description contains the component we need for the group break 
(Course Description). 
You also want to group Enrollment records for each Class together. In other words, the report 
accesses the Enrollment records, sorted by Class, breaking on each Class. 
A group break occurs each time the Course Description field‘s value changes. Within that 
break, another break occurs each time the Class Number changes. 
This record grouping goes hand-in-hand with the last question: 


---

Quick Start Lessons 
59 
 
 
 
 
How should it look? 
You want the report to contain print bands as illustrated here: 
 
 
Header(COU:Description) 
Header(CLA:ClassNumber) 
DETAIL(ENR:StudentNumber) 
Footer(CLA:ClassNumber) 
Footer(COU:Description) 
 
 
When you use the Report Wizard and specify these Group Breaks, you‘ll get a corresponding 
header for each Group Break. You can also create footers for any of these Group Breaks to 
produce a report that prints subtotals for each Class and each Course. 
In addition, you only want to print classes and courses with students enrolled. To exclude 
"empty" classes, you will use the Exclude Nulls option. 
You have finished the planning stage. You can begin designing the report. 
 
 
Creating the Relational Library and Report 
First, let's create a new library and report. 
1. If it‘s not already running, start ReportWriter. 
2. From the IDE tool bar, press the New button. 
3. In the New Library dialog, let's call our new library RelationalEx. Create the library in 
the … ReportWriter\REPXL Reports\RWTutor\School folder. 
 
 
4. Let‘s add a report using the Report Wizard. Select File > Add with Wizard to begin 
creating the new report. This wizard will create the report for you, basing the report 
layout on what you specify on its screens. 
5. In the starting window, select Standard Report as the Report Type. 
 
 
 
 
 
In the next window, we will create a new Dataset. A Dataset contains the columns and tables 
that you will use in your report. 
6. Enter School as the Dataset name, and select Clarion Dictionary as the Type of Data 
Source: 
 
 
 


---

ReportWriter 
60 
 
 
 
 
 
7. Press the Next > button to proceed, and then press the Configure File Schema 
button on the next window to select the Clarion Dictionary (SCHOOL.DCT) and tables. 
 
 
Specifying the File Schematic 
The files you need to create this report are: COURSES, CLASSES, and ENROLLMENT (you‘ll 
add the TEACHERS and STUDENTS files later). Specify these files in the schematic. 
1. After selecting the SCHOOL.DCT, press the Add button. 
The Select File window appears. Since you imported the data dictionary, several files now 
appear. 
 
 
 
 
 
2. Highlight COURSES, then press the OK button. 
This places the COURSES file in the file schematic. 
3. With COURSES highlighted, press the Add button. 
The Select File window appears, the window displays two sections: Related Files and Other 
Files. This allows you to select a related file, or select another for which you can create an ad 
hoc (user-defined) relation. User Defined Relations are covered in the next topic. 
4. Highlight the CLASSES file that is attached to the Related Files branch, then press the 
OK button. 
This places the CLASSES file in the file schematic. Note that it is attached to the COURSES 
file. 
5. With CLASSES highlighted, press the Add button. 


---

Quick Start Lessons 
61 
 
 
 
 
The Select File window appears, this time displaying the Related Files for the CLASSES file. 
6. Highlight the ENROLLMENT file that is attached to the Related Files branch, then 
press the OK button. 
 
 
 
 
 
For now, the File Schematic is complete (we‘ll add more tables later in this lesson). 
7. Press the OK button to close the File Schematic and then press the Next > button to 
proceed to the next wizard window. 
The Choose columns to display in your report window appears. 
 
 
Populating Fields 
In this dialog, you specify the fields to place on the report. You select fields by adding them to 
the Selected Fields list. The drop-down list above the Available Fields list allows you to 
select the file in the schematic from which you want to populate fields. 
1. In the Available Fields list, highlight COU:Description, and press the 
 button. 
The COU:Description field appears in the list to the right. 
2. In the Available Fields list, highlight COU:CompleteDescription, then press the 
 
button. 
The COU:CompleteDescription field also appears in the list to the right. 
3. Press the 
 button to populate the following fields in the Classes file. 
 
 
## CLA:CLASSNUMBER
## CLA:TEACHERNUMBER
## CLA:ROOMNUMBER
## CLA:SCHEDULEDTYPE
 
 
The fields selected in the Classes file now appear in the list to the right. 
 
4. Press the 
 button to populate the following fields in the Enrollment file. 
## ENR:STUDENTNUMBER
## ENR:MIDTERMEXAM
## ENR:FINALEXAM
## ENR:TERMPAPER
 
 
All the fields in the Enrollment file now appear in the list to the right. 


---

ReportWriter 
62 
 
 
 
 
The Fields to Populate should look like the illustration below: 
 
5. Press the Next > button. 
The Sort Order window appears. 
 
 
Specifying the Grouping 
In this window, you specify the grouping (group breaks) for a report. 
1. Highlight DESCRIPTION (COU:Description), then press the 
 button. 
This will group all related records for a Course together. 
2. Highlight CLASSNUMBER (CLA:ClassNumber), then press the 
 button. 
This will group all related records for a Class together. 
The Grouping Levels window should appear as pictured below: 


---

Quick Start Lessons 
63 
 
 
 
 
 
 
3. Press the Next > button. 
The SummaryOptions window appears. At this time, we will not specify any summary fields, 
and will do so later in the lesson. 
4. Press the Next > button again to proceed to the report layout dialog. 
 
 
Specify the Report Layout 
This window lets you specify a default report layout and orientation. For this lesson, you will 
use the default settings. 
1. Verify that the Layout is set to Stepped. 
2. Verify that the Orientation is set to Portrait. 


---

ReportWriter 
64 
 
 
 
 
 
 
3. Press the Next > button again to proceed to the report Style dialog. 


---

Quick Start Lessons 
65 
 
 
 
 
Specify the Report Style 
This window lets you specify a default report style, essentially selecting a font style. For this 
lesson, use the default Bold setting. 
 
 
 
1.   Press the Next > button again to proceed to the report Style dialog. 
 
 
Specify the Report Title 
Our last wizard window lets you specify a Report Title. 
1. In the What title do you want for your report? field, type Enrollment Report.   
This creates a cover page for your report. If you leave this blank, the wizard creates no title 
page. 
2. Press the Finish button to complete the Report Wizard. 
Let‘s tidy up a few more things. 
Give the Report a more descriptive Name 
In the Library Explorer, locate the xtraReport1 report that you just created. Let‘s give it a better 
name, so that when more reports are added to the library they will be easier to distinguish. 
1.   Click on the xtraReport1 report, and rename it EnrollmentReport as shown below: 
 
 
 


---

ReportWriter 
66 
 
 
 
 
 
 
At this point, you can press the 
 
tab to preview the report. When you are 
finished previewing, press the 
tab to return to the Report Designer. 
 
 
 
Let‘s clean up the report now in the next section, and at the same time demonstrate some 
important report design concepts. 
 
 
 
Conditional Detail Printing 
 
You can use conditional detail bands to print a band only when a specific condition is true. If 
you previewed the report, you may have noticed blank records printing in the detail band. 
Adding a filter condition to the band can suppress those blank details. 
 
 
 
 
 
1. In the ReportWriter toolbar, select the Report Filter option as shown here: 
 
 


---

Quick Start Lessons 
67 
 
 
 
 
2. In the FilterString Editor, enter the following condition as shown: 
 
 
 
 
Preview your report at this time, and notice that any course with no enrollments will not be 
printed. 
 
 
Variable Length Memos on Reports 
The COU:Description has a MEMO field populated on it. This is a MEMO field in the data file. 
Memo fields are generally used to store data of varying lengths. One record may contain 
several lines of text in its Memo, while another may contain a few words. Typically, you will 
want your report to adjust to the size of the Memo. If it were a fixed size, you would have blank 
areas on the report. 
The Report Wizard automatically created the Group Header Band to handle the varying length 
of the Memo Field. When you previewed the report, you probably noticed that some course 
descriptions were long and others were brief. The report printed with no noticeable "gaps." 
This is accomplished with a special property setting. First the TEXT control for the Memo field 
is set to Can Grow. This specifies that the Text control expands to accommodate all the data 
in the memo. 
 
 
To examine the properties used to produce this effect: 
1.   RIGHT-CLICK on COU:CompleteDescription, then select Properties. 
Notice that Can Grow is set to Yes. 
 
 
 
 
 
Using this property, you can create expanding Memos and Bands in any report. 
 
 
Cosmetic Enhancements for the Report 
The report is fully functional now, but you can improve it with little effort using some of 
ReportWriter‘s cosmetic features. 
Before we move to the next section, let‘s move a few controls around to improve the report‘s 
appearance. 


---

ReportWriter 
68 
 
 
 
 
 
We have cleaned up and moved some items in this report for you. In the Solution folder, load 
the RelationalEx.repxl library and continue to the next section. 
 
 
 
Relational Report after cosmetic modifications 
 
 
 
 
Creating Group Footers with Total Fields 
Before total fields can be placed on a report, they must be defined. Total fields are report- 
specific. This means they are specific to one report and are calculated at runtime. There are 
two total fields you want for this report: One to count the number of students in a Course, the 
other to count the total number of students in a Class. These two total fields are similar. The 
only difference is the point where each resets to zero. One resets after each Class, the other 
resets after each Course. 
 
 
Create the Group Footers 
Open the Group and Sort window, and check the Show Footer check box for each of the 
Group breaks that were already defined: 


---

Quick Start Lessons 
69 
 
 
 
 
 
 
This creates a Group Footer bands for COU:Description (the group break specified on the 
Course Description) and for CLA:ClassNumber (the group break specified on the Class 
Number). 
 
 
 
You can also view all bands defined in the Band Properties dialog, and change the band 
names if needed. 
 
 
 
 
 
Create the Total Fields 
Next, create total fields to count the number of students in each class and the number of 
students in each Course. 
1. From the Field List, drag the ENR:StudentNumber field to the 
CourseDescriptionGroupFooter band (GroupFooter2). 
2. Highlight the Smart Tag of the ENR:StudentNumber , and press the Summary ellipsis 
as shown below: 


---

ReportWriter 
70 
 
 
 
 
 
 
 
3. In the Summary Editor, set the Summary Function to Count, and the Summary 
Running to Group as shown here: 
 
 
 


---

Quick Start Lessons 
71 
 
 
 
 
Create another total field to count the students in each class 
1. From the Field List, drag the ENR:StudentNumber field to the ClassNumberGroup 
Footer band (GroupFooter1). 
2. Highlight the Smart Tag of the ENR:StudentNumber , and press the Summary ellipsis. 
3. In the Summary Editor, set the Summary Function to Count, and the Summary 
Running to Group as shown here: 
 
 
Populating String Controls to Identify the Totals 
You‘ll want to identify these total fields by printing some text. A simple String control with some 
text will suffice. 
1. In the Control Toolbox, drag a Label to the left of each the total fields that you just 
populated. 
2. Double click in the Label Control, and type Students Enrolled, then press Enter. 
3. In the second label, double click again, and type Total Students:, then press Enter. 
If you preview the report at this time, you should see something that looks like this: 
 
 
 
 
Adding Lookup Fields 
Next you will add some fields from "lookup" files to provide more understandable data. For 
example, for each Class you are printing a Teacher Number that uniquely identifies a teacher. 
But it will be more understandable to print the teachers‘ names on the report. 


---

ReportWriter 
72 
 
 
 
 
Adding the Lookup files to the File Schematic 
1. Press the 
 button on the toolbar. 
This displays the File Schematic. 
 
 
 
 
 
2. With Classes highlighted, press the Add button. 
The Select File window appears, displaying two sections: Related Files and Other Files. 
3. Highlight the Teachers file that is attached to the Related Files branch, then press the 
OK button. 
This places the Teachers file in the file schematic. Notice it is attached to the Classes  
file by a single arrow. This indicates that it is a Many-to-One relationship—Teachers is a 
Parent file of the Classes file. 
Next add the Students file. 
4. With Enrollment highlighted, press the Add button. 
The Select File window appears, displaying two sections: Related Files and Other Files. 
5. Highlight the Students file that is attached to the Related Files branch, then press the 
OK button. 
This places the Students file in the file schematic. Notice it is attached to the Enrollment 
file by a single arrow, indicating it is a Many-to-One relationship—Students is a Parent 
file of the Enrollment file. 
6. Press the OK button to close the File Schematic. 
 
 
 
Populating fields from the Lookup files 
These data fields are populated in the same manner as any other field. 
1. From the Field List, drag the Tea:LastName field to the ClassNumberGroupHeader 
band (GroupHeaderBand2). 
2. From the Field List, drag the Tea:FirstName field to the ClassNumberGroupHeader 
band (GroupHeaderBand2). 
You should also place the FirstName field in the CLA:ClassNumber Group Header band 
beneath or next to the LastName field. 


---

Quick Start Lessons 
73 
 
 
 
 
3. From the Field List, drag the STU:LastName in the list, then DROP on the location of 
the report where you want to place the field. 
You should place the LastName field in the detail band to the left of the 
ENR:StudentNumber field. 
Your report now prints the desired information. If you want to, preview the report to see the 
results. 
 
 
Adding a calculated field 
There is only one item left from the original plan for the report—printing each student‘s final 
grade. The Final Grade is a weighted calculation, based on each individual grade (Midterm 
Exam, Final Exam, and Term Paper). The developer who designed this database did not store 
the grade in the student file because it is easily calculated using the data already stored in the 
file. To store the final grade in the student file would waste space (data redundancy). 
This college has a standard formula for computing a student‘s final grade—the Mid-Term 
Exam is worth 25%, the Final Exam is worth 25%, and the Term Paper is worth 50%. 
To print the final grade, create a calculated field using this formula: 
(ENR:MidTermExam * 0.25) + (ENR:FinalExam * 0.25) + (ENR:TermPaper * 0.5) 
 
 
Create the calculated Field 
Next create the calculated field to calculate the final grade for each student. 
1. Create the calculated field. Open the CalculatedFields Collection Editor by pressing 
the 
 button on the toolbar. 
 
 
 
 
 
2. Press the Add button to add a new calculated field. In the window above, change the 
name of the new field to FinalGrade as shown. 
3. Click on the ellipsis button located to the right of the Expression property. This will 
open the expression editor as shown: 


---

ReportWriter 
74 
 
 
 
 
 
 
 
 
4. Enter the expression as shown above, and press OK to close the Expression Editor, 
and then press OK again to close the CalculatedFields Collection Editor. 
5. Finally, open the Field List again. Above the data fields you should now see a 
FinalGrade calculated field: 
 
 
 
 
 
6. Drag the FinalGrade calculated field to the far right of the detail band. At this time, you 
can also add a new Final Grade heading above it. 
 
 
Your report should now look something like this: 
 
 
 
 
 
 
Cosmetic Enhancements for the Report 


---

Quick Start Lessons 
75 
 
 
 
 
The report is fully functional now, but you can improve it with little effort using some of 
ReportWriter‘s cosmetic features. 
 
 
 
If you‘d like to start with the report that we have created to this point. Access the 
RelationalEx2.repxl report library in the ReportWriter Solution folder. 
 
 
 
 
Grouping Controls using a Group Box 
The GROUP control allows you to reference a group of controls as one entity. When you set 
properties for the GROUP, all controls within that group inherit the setting unless you explicitly 
set it for the control. This allows you to modify properties for several controls at once. 
Another use for a Group box is to create a box around a group of controls and optionally 
provide text to identify the group. An example is illustrated below: 
 
 
 
 
 
For this report, putting fields within a group box can also eliminate the need for prompts next to 
the Teacher fields. The Group Box text identifies the data. 
1. If the Control Tool Box is not active, select View > Windows > Tool Box from the 
Main Menu. 
This displays the Control Toolbox. 
2. Click and Drag the Group Box control to the GroupHeaderBand2 at a location where 
you want to place the Group Box (somewhere on the right side, and you may need to 
make more room). 
3. 
CLICK and DRAG the Tea:LastName, Tea:FirstName, and CLA:TeacherNumber fields 
into the group box. 
4. Resize the group box as needed by clicking and dragging its handles. 
5. Delete the Teacher Number: prompt (String control). 
6. 
RIGHT-CLICK on the group box, and select Properties. 
7. In the Text property, type Teacher, then close the Property List. 
The text now appears at the top of the Group Box. Next, create a Group box for the Class 
information. 
 
 
Create a Group Box for the Class information 
1. From the Control Toolbox, click and drag the Group Box control to the 
GroupHeaderBand2 at a location at the location where you want to place the Group 
Box (somewhere on the left side). 
2. 
CLICK and DRAG the CLA:ClassNumber, CLA:RoomNumber, and CLA:ScheduledTime 
fields into the group box. 
3. Resize the group box as needed by clicking and dragging its handles. 


---

ReportWriter 
76 
 
 
 
 
4. Delete the associated prompts (String controls). 
5. 
RIGHT-CLICK on the group box, and select Properties. 
6. In the Text property, type Class, then close the Property List. 
The text now appears at the top of the Group Box. 
 
 
Using Different Fonts 
Different font properties can make elements of your report stand out. ReportWriter allows you 
to specify the font‘s Typeface, Size, Color, and Style. Use any combination you desire to 
create the report you want. 
For this report, you want to make the font on a Course Description larger and Bold. That will 
make a better Group Header and distinguish it from the other elements of the report. 
In the groupHeaderBand1 Header Band: 
1. Delete the String Control that says Course Description: 
You won‘t need the prompt to identify the fields. 
2. Move the COU:Description field all the way to the left by clicking and dragging it with 
the mouse. 
3. 
RIGHT-CLICK on the COU:Description field, then choose Properties. The Choose Font 
dialog appears. This dialog allows you to modify all of the Font Properties at the same 
time. 
4. Locate the Font property in the Property Grid. Click on the ellipsis button to open the 
Font dialog. This dialog allows you to modify all of the Font Properties at the same 
time. 
5. Select Arial as the Font, Bold as the Font Style, and 20 as the Size, and then press 
the OK button. 
6. Move the COU:CompleteDescription field down (so it is not obscured) by clicking and 
dragging it with the mouse. 
 
 
Using Background colors 
You can also use background colors to enhance elements on your report. If you have a color 
printer, you can print the background colors. On a non-color printer, the colors are converted to 
greyscale by the printer‘s driver. For this report, a grey background would be nice on the 
COU:Description Header Band. 
In the Header Band containing COU:Description: 
 
 
1. 
RIGHT-CLICK on the Header band, then select Properties. 
Make sure you RIGHT-CLICK on an unused portion of the band. 
2. In the Property Grid, press the drop list next to Background Color. 
A standard windows color dialog appears. 
3. 
CLICK on the LightGrey box in the Web Colors, then press the OK button. 
4. Press the Close button on the Property List. 
 
 
The band now has a grey background color. Controls on a band take on the band‘s properties 
unless a property is explicitly set for a control. Therefore, the controls on this band take on the 
background color of the band. 


---

Quick Start Lessons 
77 
 
 
 
 
Controlling Pagination 
There are two Page Break and a Keep Together property settings which control the manner 
in which report elements span pages (pagination). Using these pagination options, you can 
create a report that prints in an organized manner and ensures that every page is 
understandable. 
 
 
Page Break Before the Band 
Specifies to print the structure on a new page. To reset the page number to a value you 
specify, type it in the Page Before field. To force a Page Before without resetting the page 
number, specify -1. 
 
Page Break After the Band 
Specifies to print the structure, then force a new page. To reset the page number to a value 
you specify, type it in the Page After field. To force a Page After without resetting the page 
number, specify -1. 
 
Keep Together 
Prevents 'orphan' or ‗widow‘ elements in a printout. An 'orphaned' print element is one which 
prints on a following page, separated from its related items. Keep Together specifies that the 
previous element must print on the same page. When placing subtotals or totals in a band, use 
this property to insure they print with at least one member of the column above it when a page 
break occurs. 
 
A 'widowed' print element is one which prints, but then is separated from the succeeding 
elements by a page break. Keep Together specifies that the next element must print on the 
same page, else page overflow puts them both on the next. 
 
 
For this report, use a combination of these properties to control the report‘s pagination. This 
time use the floating Property list to set the properties. 
1. RIGHT-CLICK on the COU:Description Header band, and select Properties. 
2. In the Property Grid, set the Page Break property to Before the Band. 
This forces a page break before each group header, ensuring that each new course 
starts at the top of a page. 
3. RIGHT-CLICK on the ClassNumberGroupFooter band, and select Properties. 
4. In the Keep Together property, select Yes. 
This ensures that each course footer prints with at least one prior element of the report 
(the CLA:ClassNumber footer). 
The report is complete. Preview the report, then close it. 


---

ReportWriter 
78 
 
 
 
 
Congratulations! You have completed the second lesson. 
 
 
Summary 
 When creating relational reports, a little planning in advance can save a lot of time. 
 When you import a Clarion Data Dictionary, ReportWriter imports file relationships defined 
in the dictionary. 
 When defining the file schematic for your report, you add related files to the currently 
highlighted file. 
 The Sort Order dialog allows you to specify the order in which records print and set group 
breaks to group records together. 
 To exclude "empty" records, use the Filter option. 
 The Report Wizard automatically handles the varying length of Memo fields by setting the 
Auto Expand property on the Text control and not setting the Fixed property on the band. 
 Group Footers print after all Detail bands for a group print. 
 Relations allow you to lookup values from a parent file to print on a report. 
 Group Boxes allow you to group controls together. 
 Background colors and Fonts allow you to highlight elements of your report. 
 Control pagination using the Page Break and Keep Together properties. 


---

Quick Start Lessons 
79 
 
 
 
 
 
 
Multi-up Mailing Labels 
Follow these steps to design a report to print mailing labels. ReportWriter‘s Label Wizard 
simplifies the job and allows you to choose from various types of labels. For this report you will 
use the same file (STUDENTS.TPS) but you will create a user defined key to sort the records 
in ZIP code order. 
 
 
Opening an Existing Report Library 
 
 
Create this report in the same Report Library as the other reports in our QuickStart lessons. 
1. If it is not already running, start ReportWriter. 
 
 
2. If the GettingStarted Report Library is not open, press the 
 button on the toolbar 
(or choose File 
Open or CTRL + O). 
The Open dialog appears allowing you to select recently used Report Libraries. 
3. Highlight GettingStarted.repxl, then press the Open button. The Report Library opens. 
 
 
Creating the Multi-up Label Report 
Multi-up columns allow two or more records to be printed side-by-side, instead of one below 
the other. You can use the multi-up column feature to print a report with all or part of the report 
in multi-column format. By printing records side-by-side, the report uses fewer lines, and can 
conserve paper and produce a more concise report. 
 
 
How multi-up columns work 
A multi-up column simply has a band defined as a fraction of the paper width. For example, if a 
band is defined to be half of the paper width, it prints two columns. If it is defined as a third of 
the paper width, it prints three columns. 
In a two column band, records are printed in the following sequence: 
1 
2 
3 
4 
 
5 
6 
 
7 
… 
 
 
Using the Label Wizard 
4. On the ReportWriter IDE window, press the Add with Wizard button. 
 
 
 


---

ReportWriter 
80 
 
 
 
 
5. Select the Label Report Report Type, and press the Next button 
 
 
 
 
 
The Label Information window appears. 
 
 
 
 
 
Define the Label 
The Label Definition window allows you to select one of a number of standard labels that are 
widely available. You can also define your own custom size. 
6. In the Label Products drop list, select Avery Standard. 
7. In the Product Number drop list, select 5160 Address. 
This specifies Avery 5160 labels (a popular Avery product which has 30 labels per sheet). 
8. Press the Next > button. 
 
 
Customize the Label's Options 
The Label Options window appears. Use this dialog to adjust any margins or paper type if 
needed. 
9. Press the Finish button. 


---

Quick Start Lessons 
81 
 
 
 
 
 
Your report worksheet should now look like this: 
 
 
 
 
 
The next step is to define the data that we need to attach to the label report. 
 
 
Set the data that your report will use. 
 
 
10. In the upper left corner of the report worksheet, click on the smart tag button shown 
below to open the Report Tasks window: 
 
 
 
 
 
Think of the Report Tasks window as a shortcut to common or popular properties found in the 
Property Grid. 
11. In the Report Tasks window, select the drop list of the Data Source, and click on the 
Add New Data Source link as shown here: 


---

ReportWriter 
82 
 
 
 
 
 
 
The Reports Wizard Dataset dialog is now opened: 
 
 
 
 
 
The dataset name is simply the name we will use to identify our data source. As our Report 
Library grows with new reports, it will be very likely that we will have multiple datasets available 
for different reports. The only requirement for the dataset name is that spaces are not  
permitted. 
 
 
12. Since we will be creating a "Student Labels" report in this example, enter Students in 
the Enter a dataset name entry, and then accept the default Clarion Data Source 
(Dictionary) option as shown above. The Standard Data Source is used to connect 


---

Quick Start Lessons 
83 
 
 
 
 
to ODBC and SQL data sources (or essentially any data that does not use a Clarion 
dictionary), and will be covered in more detail later in this document. For now, we will 
be using a Clarion dictionary, so press the Next button to continue. 
 
 
13. In the next dialog, press the Configure File Schema button to select your dictionary. 
 
 
14. In the ReportWriter\REPXL Reports\RWTutor\School folder, select the SCHOOL.DCT 
dictionary file. 
 
 
After the dictionary is selected, the File Schematic dialog is now displayed: 
 
 
 
 
 
 
15. Press the Add button in the File Schematic dialog, and select the Students file as 
shown below: 


---

ReportWriter 
84 
 
 
 
 
 
 
16. Press OK to add the Students file to the File Schematic window. 
That is all that we wish to add right now. In this Getting Started, we will create a simple 
"Student List". 
 
 
17. In the File Schematic window, press the Paths button. The following dialog is now 
displayed: 
 
 
 


---

Quick Start Lessons 
85 
 
 
 
 
18. This dialog is useful when your data is located in a different location from the report 
library. Since our data is located in the same folder as our report library, Press Cancel 
to close the Edit Paths window and return to the File Schematic window. 
 
 
19. Press OK to close the File Schematic window, and then press the Finish button to 
close the Reports Wizard dialog. 
 
 
20. We are now back to the Report Tasks window. Close this window by clicking on the 
Smart Tag button. In the next section, we will populate our student data on the report 
worksheet. 
 
 
This would be a good time to take a break and review what we have done. 
 
 
 
We created a new label style report in an existing report library. 
 
We attached a Data Source to use in the report. 
 
 
 
 
Create some Calculated Fields 
 
 
For the labels, you want two calculated fields: 
 
One to remove trailing spaces from the student‘s first name, then add a space and the 
student‘s last name. 
 
The other to remove trailing spaces from the student‘s City, then add a comma, a 
space, the State, another space, then the ZIPCode. 
 
 
1. Press the Calculated button on the toolbar as shown below. 
 
 
 
 
 
2. The Calculated Field Collection Editor window appears. Press the Add button to 
add a new calculated fields: 
3. In the (Name) entry box, type FullName. 


---

ReportWriter 
86 
 
 
 
 
 
 
This provides a unique label that ReportWriter uses to reference the calculated field. 
 
 
4. Press the ellipsis button to the right of the Expression Property to use the 
Expression Editor to create the calculated field‘s formula. You may need to click on 
the Expression property to actually see the ellipsis button. 
 
 
The Expression Editor appears. This editor helps you quickly generate a syntactically correct 
expression. 


---

Quick Start Lessons 
87 
 
 
 
 
 
 
5. Highlight Clarion Built-in Functions in the list box on the left, then highlight CLIP(string) 
in the list box on the right, then DOUBLE-CLICK to add to the expression box. 
 
 
The CLIP function removes trailing spaces. 
6. Highlight Fields in the list box on the left, then highlight STU:FirstName in the list box 
on the right. Delete the single quotes in the CLIP parameter, and then DOUBLE- 
CLICK to add to the expression box. 


---

ReportWriter 
88 
 
 
 
 
 
 
These two steps remove the trailing spaces from the STU:FirstName field. 
7. Press the END key to move the cursor to the end of the expression, then TYPE & ‘ ‘ & 
to the end of the CLIP expression: 
 
 
 
 
 
This inserts the concatenation operator into the expression to append one string to another, 
separated by a space for better clarity. 
 
 
8. Highlight Fields in the list box on the left, then highlight STU:LastName in the list box 
on the right, then DOUBLE-CLICK to add to the expression box. 
 
 
 
 
 
9. Press the OK button to verify your expression and close the window. 
This completes the expression for the name. 
Create the Second Calculated Field 
 
 
This calculated field removes trailing spaces from the student‘s City, then adds a comma and 
space, the State, another two spaces, then the ZIP Code. 
 
 
10. Create the Calculated field in the same manner as before. 
Your Calculated Field should appear as shown below: 


---

Quick Start Lessons 
89 
 
 
 
 
 
 
11. Finally, press the Save button at this time to save your report changes. 
 
 
Populate the Calculated and Data Fields 
Now the calculated fields and existing data fields are ready for you to place on the report. 
 
 
1. CLICK on the Field List window if already opened (or choose View 
Windows 
 
Field List. The Field Selection List appears. This window allows you to quickly place 
data fields on your report. 
 
 
 
 
 
2. CLICK on FullName in the list, then DRAG to the location of the report where you want 
to place the field. 


---

ReportWriter 
90 
 
 
 
 
You should place the FullName field near the top left of the label area. 
 
 
3. CLICK on STU:Address in the list, then DRAG to the location of the report where you 
want to place the field. 
You should place the STU:Address field just below the FullName field. 
 
 
4. CLICK on STU:Address2 in the list, then DRAG to the location of the report where you 
want to place the field. 
You should place the STU:Address2 just to the right of the STU:Address field. 
 
 
5. CLICK on CityStateZip in the list, then DRAG to the location of the report where you 
want to place the field. 
You should place the CityStateZip field below the STU:Address field. 
 
 
Your report is complete. 
6. Preview the report to see the results. 
 
 
 
 
 
Sort by ZipCode 
 
 
Finally, let‘s change the label report to sort by zip code 
 
 
7. In the Group and Sort box below the report worksheet, press the Add a Sort button, 
and select the STU:Zip field as shown below: 


---

Quick Start Lessons 
91 
 
 
 
 
 
 
8. Preview the report to see the results. 
This completes this lesson. Congratulations!


---



---

93 
 
 
 
 
 
Reports Wizard 
Reports Wizard 
 
Use the Add with Wizard option to create your first report. From the IDE Menu, select File > 
Add with Wizard. You can also use the toolbar button shown here: 
 
 
 
The opening wizard window is now displayed: 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
You have two types of reports available via the Reports Wizard; Standard and Label Reports. 
Selecting the Standard report will prompt you to create a dataset. If you select the Label type 
report, the dataset information is added after the report is created. 


---

94 
ReportWriter 
 
 
 
 
Reports Wizard - Create a New Dataset 
 
 
In this dialog we begin to identify the data that your report will use. 
 
 
Before we continue with our report design, the first and most important requirement for the 
report is to identify the data that will be used. After selecting the type of report we will create, 
the following dialog is displayed: 
 
 
 
The dataset name is simply the name we will use to identify our data source. As our Report 
Library grows with new reports, it will be very likely that we will have multiple datasets available 
for different reports. The only requirement for the dataset name is that spaces are not  
permitted. 
 
 
Since we will be creating a "Student List" report in this example, enter Students in the Enter a 
dataset name entry, and then accept the default Clarion Data Source (Dictionary) option as 
shown above. The Standard Data Source is used to connect to ODBC and SQL data sources 
(or essentially any data that does not use a Clarion dictionary), and will be covered in more 
detail later in this document. For now, we will be using a Clarion dictionary, so press the Next 
button to continue. 
 
 
In the next dialog, press the Configure File Schema button to select your dictionary. 


---

95 
Reports Wizard 
 
 
 
 
Reports Wizard - File Schematic 
 
 
After the dictionary is selected, the File Schematic dialog is now displayed: 
 
 
 
 
 
 
Press the Add button in the File Schematic dialog, and select the Students file as shown 
below: 
 
 
 
Press OK to add the Students file to the File Schematic window. 
That is all that we wish to add right now. In this Getting Started, we will create a simple 
"Student List". 
 
 
In the File Schematic window, press the Paths button. The following dialog is now displayed: 


---

96 
ReportWriter 
 
 
 
 
Reports Wizard - Edit Paths 
 
 
 
This dialog is useful when your data is located in a different location from the report library. 
Press the ellipsis to the far right of the Students row and select the path as shown above. 
Press OK to close the Edit Paths window and return to the File Schematic window. 
 
 
A relative path is set relative to the library root folder. Setting a relative path makes it easier to 
move the entire application to another directory on the server without having to update the 
code. 
 
 
Press OK to return to the Select Dictionary dialog, and then press the Next button to proceed 
to the "Choose Columns... dialog as shown here: 
 
 
Reports Wizard - Choose Columns 
 


---

97 
Reports Wizard 
 
 
 
 
Use the arrow keys to move your columns to print from the left side to the right. When you are 
satisfied with your selections, press the Next button. 
 
 
Reports Wizard - Grouping Levels 
 
 
The next dialog allows you to create Group Breaks in your reports, which will be generated 
when the column that you select changes. 
 


---

98 
ReportWriter 
 
 
 
 
Reports Wizard - Report Layout 
Set up your layout and style 
 
 
Note: 
If you had selected any Grouping options, the next dialog would be a list of Summary options. 
This dialog will be explained in more detail in the Summary Options section of this document. 
 
 
The next dialog that you should see is the Report Layout: 
 
Columnar layout displays the fields you specified in a single column display. A visual image of 
the layout is displayed to the left as shown above. 
 
 
Tabular layout displays the fields you specified across the page in a single row. The field width 
option will try to fit all of the fields on a single page. 
 
 
Justified layout measures the size of each field that you specified and will wrap the columns 
to the next line to fit all information neatly. 
 
 
More layout options are also available if you had selected report grouping. Each of these 
layouts will be covered in more detail in the Layout Options section in this document. 
 
 
In addition, you can also select the orientation of your report in this dialog. Select from Portrait 
or Landscape. 
 
 
Select the default Columnar layout and press the Next button to continue. 


---

99 
Reports Wizard 
 
 
 
 
Reports Wizard - Styles 
 
 
The next dialog in the Reports Wizard allows you to set one of several predefined styles, as 
shown as follows: 
 
 
 
As shown above, select from one of the different default styles for your report. After selecting a 
style (we chose Casual), press Next to continue. We are almost finished! 


---



---

101 
 
 
Reports Wizard - Report Title and Finish 
Final Touches and Preview 
 
 
The last dialog presented is provided to simply provide a title for your report. 
 
After you give your report a descriptive name, press the Finish button to complete your report. 
The Design Worksheet should now be displayed: 


---

ReportWriter 
102 
 
 
Advanced Controls 
 
 
Pivot Grid Control 
See Also: Using the Pivot Grid Control 
 
 
The Pivot Grid control displays data from an underlying data source in a cross-tabulated form 
to create cross-tab reports. It calculates summaries and summary totals against specific fields, 
and displays the summary values within data cells. 
 
 
There is a built-in designer allowing you to easily customize the Pivot Grid. It can be invoked 
using the control's Smart Tag: 
 
 
 
 
 
The Pivot Grid displays data in a manner similar to Pivot Tables in Microsoft Excel. Column 
headers display unique values from one data field, say, car models. Row headers display 
unique values from another field, say, dates. Each cell displays a summary for the 
corresponding row and column values. By specifying different data fields, you can see the total 
number of cars sold on a particular date, or the total number of deals, etc. This way, you get a 
really compact layout for data analysis. 
In the Property Grid, the Pivot Grid control's properties are divided into the following groups. 
 
 
Appearance 
 
Appearance 
Allows you to define the appearance properties (such as Background Color, Foreground Color, 
Font, etc.) for the Pivot Grid's elements (Cell, Field Value, Filter Separator, Header Group   
Line, etc.). 
 
Formatting Rules 
Invokes the Formatting Rules Editor allowing you to choose which rules should be applied to 
the control during report generation, and define the precedence of the applied rules. To learn 
more on this, refer to Conditionally Change a Control's Appearance. 
 
Styles 
Allows you to invoke the Styles Editor, which is intended to manage and customize the 
control's styles, which then can be assigned to the Pivot Grid's elements. 


---



---

ReportWriter 
104 
 
 
 
 
Behavior 
 
Anchor Vertically 
Specifies the vertical anchoring style of the Pivot Grid, so that after page rendering it stays 
attached to the top control, bottom control, or both. 
 
Keep Together 
Specifies whether the contents of the control can be horizontally split across pages. In other 
words, if the control occupies more space than remains on the page, this property specifies 
whether this Pivot Grid should be split between the current page and the next, or whether it will 
be printed entirely on the next page. This property is in effect only when a Pivot Grid's content 
does not fit on the current page. If it does not fit on the next page either, then the Pivot Grid will 
be split despite this property's value. 
 
Scripts 
This property contains events, which you can handle by the required scripts. For more 
information on scripting, refer to Handle Events via Scripts. 
 
Visible 
Specifies whether the control should be visible in print preview. 
 
 
Data 
 
Data Adapter 
Determines a data adapter that will populate a Pivot Grid's data source which is assigned via 
the Data Source property. It is automatically set to the appropriate value, when the Data 
Member property is defined. To learn more on this, refer to Cross-Tab Report. 
 
Data Member 
Determines the data source member which supplies data to a Pivot Grid. To learn more on 
this, refer to Cross-Tab Report. 
 
 
Usually, it is not necessary to specify the Data Member property when binding a Pivot Grid to 
data. This property should only be set directly if the dataset contains more than one table. 
 
Data Source 
Determines a Pivot Grid's data source. To learn more on this, refer to Cross-Tab Report. 
 
Fields 
Invokes the Pivot Grid Field Collection Editor, allowing you to manage and fully customize a 
Pivot Grid's fields. 
 
OLAP Connection String 
Specifies a connection string to a cube in an Microsoft Analysis Services database. A sample 
connection string is shown below: 
 
OLAPConnectionString="Provider=msolap;Data Source=localhost;Initial 
Catalog=Adventure Works DW;Cube Name=Adventure Works;Query Timeout=100;" 
 
A connection string can be built via the Connection String Editor. To invoke it, click the ellipsis 
button for the OLAP Connection String property. 
 
To represent information from the bound cube, create specific Pivot Grid fields, and bind them 
to the required fields in the data source. 
 
If the OLAP Connection String property is set to a valid string, the value of the Data Source 
property is cleared. Setting the Data Source property to a valid object clears the OLAP 
Connection String property. 


---

Advanced Controls 
105 
 
 
 
 
Prefilter 
When this property is expanded in the Property Grid, you can set its Enabled property to Yes, 
and use the Criteria property to invoke the Pivot Grid Prefilter dialog. 
 
This dialog allows you to build complex filter criteria with an unlimited number of filter 
conditions, combined by logical operators. It provides a set of logical operators that 
significantly simplify the process of creating filters for text, numeric and date-time fields. 
 
 
The Prefilter is not supported in OLAP mode. 
 
 
Design 
 
(Name) 
Determines a control's name, by which it can be accessed in the Report Explorer, Property 
Grid or via scripts. 
 
 
Layout 
 
Location 
Specifies the control's location, in report measurement units. 
 
Size 
Specifies the control's size, in report measurement units. 
 
 
Navigation 
 
Bookmark and Parent Bookmark 
These properties are intended for the creation of a hierarchical structure within a report called 
a document map. For an explanation and help, refer to Add Bookmarks. 
 
 
Options 
 
Data Field Options 
Allows you to customize the options which control the presentation of the data fields. 
 
Data Options 
Allows you to define whether a Pivot Grid's fields must be case sensitive or not. 
 
Print Options 
Allows you to customize the print options of a Pivot Grid. 
 
View Options 
Allows you to customize the Pivot Grid's display options 
 
 
See Also: Using the Pivot Grid Control 


---

ReportWriter 
106 
 
 
 
 
Using the Pivot Grid Control 
 
This topic shows you how to create a cross-tab report using a Pivot Grid control. 
 
 
Step 1: Create a pivot grid and bind it to data 
 
 
1. Create a new report. 
 
2. Drop the Pivot Grid control from the Toolbox onto the report's Detail band. 
 
 
 
 
 
To bind the grid to a data source, click its Smart Tag, and in the invoked actions list, expand  
the Data Source drop-down selector and click Add New DataSource. The Report Wizard dialog 
will appear. 
 
 
 
 
 
The wizard will guide you through the process of assigning a data source to the grid. For 
detailed instructions on the wizard's steps, refer to the Binding a Report to Data topic, as this 
process is similar. 


---

Advanced Controls 
107 
 
 
 
 
After the data source assignment, the created dataset is assigned to the grid's Data Source 
property. Also, set its Data Member property, to define from which table or view of your 
dataset the grid should obtain data. Then, the Data Adapter property will be automatically 
defined. This means that the grid is bound to the data. 
 
 
 
 
 
 
 
Note that after these steps, the Report’s Data Source property must be set to None. 
Otherwise, the grid will be repeated as many times as there are records in the data source. 
 
 
 


---

ReportWriter 
108 
 
 
 
 
Step 2 - Manage the grid's fields. 
 
Click the grid's Smart Tag, and in the invoked actions list, click the Run Designer… link. The 
Property Editor will appear. 
 
 
 
 
 
In this editor, click the Retrieve Fields button, and switch to the Layout section in the 
navigation bar on the left. 
 
Drag & drop the required fields to the Row Fields, Column Fields and Data Items areas. 
Click Apply and close the editor. 
The cross-tab report is now ready. Switch to the Preview Tab, and view the result. 


---

Advanced Controls 
109 
 
 
 
 
 


---

ReportWriter 
110 
 
 
 
 
Chart Control 
 
Using the Chart Wizard 
 
The chart wizard dialog is used to quickly and easily create a new chart, or modify an existing 
one. By default, it is automatically displayed when you populate a Chart control on your report. 
 
Two Groups are shown to the left of the Chart Wizard. Pages are displayed just to the right of 
the Groups section. 
 
To navigate through the Chart Wizard's pages, use the navigation bar or Previous and Next 
buttons. 
 
To complete the chart, use the Finish button, or the Cancel button to cancel all changes. 
 
 
The Chart Wizard contains the following pages. 
 
 
 
 
Construction Group 
 
Chart Type Page 
 
The Chart Type Page is used to simply select a chart type. 
 
 


---

Advanced Controls 
111 
 
 
 
 
The Drop list at the top is used to filter chart type for selection. Simply cick on a Chart Type to 
select it. 
 
The following chart filters are available: 
 
 
All Chart Types. 
 
Bar (Bar, Stacked Bar, 100% Stacked Bar, 3D Bar, 3D Stacked Bar, 3D 100% 
Stacked Bar and Manhattan Bar). 
 
Point and Line (Point, Line, Step Line, 3D Spline, Line, 3D Step Line and 3D Spline). 
 
Pie (Pie, Doughnut, 3D Pie and 3D Doughnut). 
 
Area (Area, Stacked Area, 100% Stacked Area, Spline Area, Spline Area Stacked, 
100% Stacked Spline Area, 3D Area, 3D Stacked Area, 3D 100% Stacked Area, 3D 
Spline Area, 3D Spline Stacked Area and 3D 100% Stacked Spline Area). 
 
Radar and Polar (Radar Point, Radar Line, Radar Area, Polar Point, Polar Line and 
Polar Area). 
 
Range Bar and Gantt (Range Bar, Side by Side Range Bar, Gantt and Side by Side 
Gantt). 
 
Financial (Stock and Candle Stick). 
 
 
 
 
Appearance Page 
 
In the Appearance Page, you use it to perform two tasks; Choose a palette to color a series 
using the Palette Editor, and choose the style specifying the chart's appearance using the  
Style Editor. There is also a Chart preview area that shows a visual representation of the chart 
that you selected. 
 
 
 
 
 
 
 
 
Series Page 
 
The Series Page is used to perform four essential tasks: 
 
 
Create or remove a series of points. 
 
 
Define the series name, visibility and view type. 
 
 
Customize additional series options, point and legend point options. 
 
 
Enable and customize the Top N Values feature. 


---

ReportWriter 
112 
 
 
 
 
 
 
 
Series list 
This list displays all available series. You can click list entries to access properties of the 
corresponding series. To switch between series, use the 
 and 
 buttons. 
 
Series management buttons 
Use the Add, Copy and Remove buttons to manage the series collection. 
 
Main series properties 
Choose whether the selected series should be visible, define its name, and select a view type. 
 
Options tabs 
The following tabs are available on this page: 
 
Options 
Purpose 
Series 
Specifies argument and value scale types, point sort order and legend text. 
Top N 
Specifies whether the Top N Values feature is enabled, and allows you to 
control this feature's options. 
Point 
Specifies the format of values displayed in chart labels. 


---

Advanced Controls 
113 
 
 
 
 
Legend 
Point 
Specifies the format of values displayed in the chart legend. 
 
 
 
 
 
 
Data Page 
 
In the Data Page the following tasks are accomplished: 
 
 
Provide data for a chart; 
 
 
Bind a chart or individual series to a data source; 
 
 
Customize an argument and a value scale type; 
 
 
Customize the view type of auto-generated series; 
 
 
Apply data filtering and sorting. 
 
 
The necessary data needed for a chart is defined using the following tabs. 
 
 
Points Tab 
Use it to manually enter data points for series. 
 
 
 
 
Valid Argument and Value entries must correspond to the Argument scale type and the Value 
scale type, selected for the appropriate series on the Series Page. Otherwise, an error 
message will be invoked. 
 
 
Series Binding Tab 
Use it to provide specific data binding options for each series. 


---

ReportWriter 
114 
 
 
 
 
 
 
 
The following illustration demonstrates how it works. 
 
 
 
 
Auto-created Series Tab 
Use it to specify data columns used to generate series, as well as the series view type and 
other options like sorting, filtering and name template. 


---

Advanced Controls 
115 
 
 
 
 
Presentation Group 
 
Chart Page 
 
The Chart Page is used to define a chart's background color, background image and border. 
 
 
 
Chart preview area 
Previews a chart's layout. 
 
Options tabs 
The following tabs are available on this page: 
 
Appearance 
Specifies a chart's background color, fill style and background image. 
 
Border 
Specifies border visibility and color. 
 
 
 
Diagram Page 
 
In the Diagram Page you can: 
 
 
Rotate a diagram 
 
Define a diagram's padding 
 
Add or remove secondary axes 
 
Add or remove panes 
 
Define panes' layout direction 


---

ReportWriter 
116 
 
 
 
 
 
 
Chart preview area 
Previews a chart's layout. 
 
Options tabs 
The following tabs are available on this page. 
 
General 
Choose whether a diagram should be rotated, set its padding values, and (if it contains 
several panes) define the panes' layout direction. 
 
Elements 
Add or remove secondary axes and panes. 
 
 
 
Panes Page 
 
Used to customize the panes properties. 


---

Advanced Controls 
117 
 
 
 
 
 
 
Chart preview area 
Previews a chart's layout. 
 
Pane selector 
Specifies a pane to be customized. 
 
Options tabs 
The following tabs are available on this page. 
 
General 
Determines whether the selected pane should be visible, specifies its name, size mode and 
size value. 
 
Appearance 
Specifies a pane's background color and fill style, and its background image. 
 
Border 
Determines whether a pane's border should be visible, and defines its color. 
 
Shadow 
Determines whether a pane's shadow should be visible, and defines its color and size. 
 
 
 
Axes Page 
 
In the Axis Page, you can: 
 
 
Customize axes properties. 
 
Add a constant line and a strip line to an axis. 


---

ReportWriter 
118 
 
 
 
 
 
 
 
Chart preview area 
Previews a chart's layout. 
 
 
You can select an axis to be modified on the chart preview area directly. 
 
Axis selector 
Specifies an axis to be customized. 
 
Options tabs 
The following tabs are available on this page. 
 
General 
Specifies visibility, position, range and format properties. 
 
Appearance 
Defines color, thickness and interlacing options. 
 
Elements 
Customizes title, tick marks and grid lines properties. 
 
Labels 
Specifies position and text for automatically created labels, or allows custom labels to be 
defined. 


---

Advanced Controls 
119 
 
 
 
 
Strips 
Allows you to create strips, define their visibility, name, limits, appearance, etc. 
 
Constant Lines 
Allows you to create constant lines, define their visibility, name, value, legend text, 
appearance, title, etc. 
 
 
 
 
 
Series Views Page 
 
In the Series Views Page, you can: 
 
 
Customize series view properties. 
 
Add or remove financial indicators (Fibonacci indicators or trendlines) and customize 
their properties. 
 
 
 
Chart preview area 
Previews a chart's layout. 
 
 
You can select a series to be modified directly on the chart preview area. 
 
Series selector 
Specifies a series to be customized. 


---

ReportWriter 
120 
 
 
 
 
Options tabs 
The following tabs are available on this page. 
 
General 
Specifies a series bar's width, distance, color, transparency, etc. 
 
Appearance 
Specifies a fill style and borders properties. 
 
Shadow 
Specifies whether a series' shadow should be visible, determines its color and size. 
 
Fibonacci Indicators 
Allows you to add or remove Fibonacci indicators of a required kind (Fibonacci Arcs, 
Fibonacci Fans or Fibonacci Retracement). Specifies their points' arguments and value 
levels. Determines whether to display additional levels. Specifies the appearance of the 
indicators' lines and labels. 
 
Trendlines 
Allows you to add or remove trendlines. Determines whether to extrapolate them to infinity. 
Specifies their points' arguments and value levels. Defines their color, dash style and 
thickness. 
 
 
 
Point Labels Page 
 
In the Points Label Page, you can customize the point labels' properties. 
 
 


---

Advanced Controls 
121 
 
 
 
 
Chart preview area 
Previews a chart's layout. 
 
 
You can select point labels to be modified directly on the chart preview area. 
 
Series selector 
Specifies a series to be customized. 
 
Options tabs 
The following tabs are available on this page. 
 
General 
Specifies whether labels should be visible and shown for zero values, and determines their 
text settings. 
 
Appearance 
Specifies a labels' background color, border and fill style. 
 
Shadow 
Specifies whether a labels' shadow should be visible, and defines its color and size. 
 
 
 
Chart Titles Page 
 
In the Chart Titles page, you can customize the chart titles' properties. 
 
 


---

ReportWriter 
122 
 
 
 
 
Chart preview area 
Previews a chart's layout. 
 
 
You can select chart titles to be modified on the chart preview area directly. 
 
Titles management section 
Allows you to add or remove titles from the titles list, and choose a title to be customized. 
 
Options tabs 
The following tabs are available on this page. 
 
Text 
Sets a text for the selected chart title. 
 
General 
Specifies the selected title's visibility, alignment and text. 
 
 
 
Legend Page 
 
In the legend Page, you can customize the chart legend's properties. 
 
 
 
Chart preview area 
Previews a chart's layout. 


---

Advanced Controls 
123 
 
 
 
 
 
You can select the legend directly on the chart preview area. 
 
Options tabs 
The following tabs are available on this page. 
 
General 
Specifies legend visibility, direction, alignment, spacing and limits. 
 
Appearance 
Specifies legend background color and background image. 
 
Marker 
Specifies visibility and dimensions of legend markers. 
 
Text 
Specifies legend text antialiasing, color and font. 
 
Border 
Specifies visibility, color and thickness of legend borders. 
 
Shadow 
Specifies visibility, color and size of the legend shadow. 
 
 
 
 
 
See Also: 
 
Chart using a Dynamic Series 
Chart using a Static Series 


---

ReportWriter 
124 
 
 
 
 
Chart using a Dynamic Series 
 
This topic shows you how to create a report with a Chart control bound to data. In this 
example, all series will be auto-created by a chart using the series template, which specifies 
common data binding properties for all series. 
 
This is possible because the data for all series (the series names along with series points' 
arguments and values) are stored in the same data table. Also, in this example, the series view 
type and certain other settings should be the same for all the series created. 
 
In this example we'll use the TeamYearTotal table located in the Bowling Clarion Data 
Dictionary (Bowling.DCT). This table contains the yearly total pins statistics for league teams. 
 
 
Phase 1: Create a chart and bind it to data 
 
1. Create a new report. 
 
2. Drop the Chart control from the Toolbox onto the report's Detail 
band. 
 
 
 
In this instance, the Chart Wizard may be invoked (if its Show wizard every time a new chart 
is added option is checked). In this example, we don't need to use the wizard, so click Cancel 
to close the wizard's window and manually customize the chart. 
 
1.   To bind the chart to a data source, click its Smart Tag, and in the 
invoked actions list, expand the Data Source drop-down selector and 
click Add New DataSource. The Report Wizard dialog will appear. 
 
 
 
The wizard will guide you through the process of assigning a data source to the chart. In this 
example, our data source (named BowlingTeamTotals) will be bound to a Clarion Dictionary 
(Bowling.DCT) as shown below: 


---

Advanced Controls 
125 
 
 
 
 
 
Note that the table name shown above used in the Data Source is the TeamYearTotal table. 
Now, the created dataset is assigned to the chart's Data Source property. Also, set its Data 
Member property, to define from which table or view of your dataset the chart should obtain 
data. Then, the chart's Data Adapter property will be automatically set, as well. This means 
that the chart is bound to the data. 
 
 
 
 
After setting the data source for the Chart control, the report's Data Source property must be 
set to None. Otherwise, the chart will be blank at the preview, and be repeated as many times 
as there are records in the data source. You can set this easily using the Report‘s Smart Tag 
as shown below: 


---

ReportWriter 
126 
 
 
 
 
 
 
 
Phase II: Specify a series data member and adjust a series template 
 
In this example, the chart will represent the data as different series, series points and their 
values, so all series will be created using a series template which is common to all series. The 
following steps demonstrate how this is done. 
 
To specify the data field which should provide data for the series names, you need to first set 
the Series Data Member property value. 
 
 
 
Next, adjust the series template which is accessed via the chart's Series Template property. 
Set the Argument Data Member property. 


---

Advanced Controls 
127 
 
 
 
 
 
 
Finally, define the value of the Value Data Members property, indicating the data fields from 
which the series obtains the data values of its points. 


---

ReportWriter 
128 
 
 
 
 
 
 
 
Phase III: Customize the chart 
 
Adjust the Series Name Template 
 
By default, the name for every series which is automatically generated by the chart using its 
Series Data Member property's value, is obtained directly from an appropriate data field in the 
bound data source. However, it may also be necessary to add some prefixes or postfixes to 
these names. So, you may customize the Series Name Template object returned by the Series 
Name Template property, to add some text to the beginning or to the end of every series  
name. For instance, here we set the Series Name Template.Begin Text property to "Pins in ". 


---

Advanced Controls 
129 
 
 
 
 
 
 
Customize Series Labels 
 
Set the Series Template.Label.Visible property to No, to hide labels for all series points, and 
prevent a chart from being crowded with numerous overlapping labels. 


---

ReportWriter 
130 
 
 
 
 
 
 
Customize Axis Labels 
 
Initially, all axis labels (which in this example show the names of the US regions) are lined up 
and overlap, so the chart looks unprofessional. To avoid this, select the X-Axis (which is also 
accessed via the Chart Control Diagram.Axis X property) and set its Label.Staggered 
property to Yes. 


---

Advanced Controls 
131 
 
 
 
 
 
 
If required, it is possible to customize many other properties for the chart, which are not 
described here. 
 
The chart is now ready. Switch to the Preview Tab, and view the result. 


---

ReportWriter 
132 
 
 
 
 
 
 
 
For an additional method to bind a chart to data, refer to the Chart using a Static Series help 
topic. 


---

Advanced Controls 
133 
 
 
 
 
 
Chart using a Static Series 
 
This topic contains details on how to create a report with a Chart control bound to data, so that 
a particular series has its own data source, and other pertinent settings. 
 
This example describes how to construct a chart of products and their prices for a chosen 
category using the data from the Microsoft Northwind database (the sample nwind.mdb 
database). In this example, the series' data have a single data source to simplify the project. 
But since the series can be bound to data independently, different data sources can be used 
for different series, if necessary. 
 
To create a chart, follow the steps below. 
 
1. Create a new report. 
 
2. Drop the Chart control from the Toolbox onto the report's Detail band. 
 
 
 
 
 
The Chart Wizard may be invoked (if its Show wizard every time a new chart is added 
option is enabled). In this example, we don't need to use the wizard, so click Cancel to close 
the wizard's window and manually customize the chart. 
 
3. To bind the chart to a data source, click its Smart Tag, and in the invoked actions list, 
expand the Data Source drop-down selector and click Add New DataSource. The 
Report Wizard dialog will appear. 


---

ReportWriter 
134 
 
 
 
 
 
 
The wizard will guide you through the process of assigning a data source to the chart. For 
detailed instructions on the wizard's steps, refer to the Binding Data to a Report topic, as this 
process is similar. In our example, we will be using the Products table from the Northwind 
database. 
 
4. The created dataset is assigned to the chart's Data Source property. Also, set its Data 
Member property, to define from which table or view of your dataset the chart should 
obtain data. Then, the chart's Data Adapter property will be automatically defined. This 
means that the chart is bound to the data. 
 
 
 
 
 
After these steps, the report's Data Source property must be set to None. Otherwise, the chart 
will be blank at the preview, and repeated as many times as there are records in the data 
source. 


---

Advanced Controls 
135 
 
 
 
 
 
 
 
5. To add a series to the chart and specify its data binding properties, use the Series 
Collection Editor. It can be invoked either via the Property Grid, or via the Series... link 
in the chart's Smart Tag. 


---

ReportWriter 
136 
 
 
 
 
 
In the editor, create a series by clicking the Add... button and selecting the Bar view. 
Switch to the Properties tab at the right of the editor's window. 
Set the series' Data Source property to the created dataset, define the Argument Data 
Member and Value Data Members properties. 


---

Advanced Controls 
137 
 
 
 
 
 
 
Click Copy, to create another series with the same properties, and set its View property to 
Point. 
 
 
To save the changes and quit the editor, click Close. 
 
 
6. You may note now that there are too many data points, and the chart looks messy. 
The chart's Data Filters property is intended to limit the number of data points shown 
by applying a filtering criterion. Select Series1 in the chart by mouse click, then in the 
Property Grid locate the Data Filters item and click its ellipsis button, to invoke the 
Data Filter Collection Editor. 


---

ReportWriter 
138 
 
 
 
 
 
 
Click Add to add a criterion, and define its properties as shown here. 
 
 
 
To save the changes and quit the editor, click Close. 
 
Repeat the same actions for Series2, i.e. choose its Data Filters property, add a filter and 
define its Column Name and Value. 
 
7. To improve the chart's appearance, make the following corrections. 
 
o 
Remove the chart's legend, as it shows the same data for the series. To do 
this, select the legend item in the chart, and in the Property Grid, set its 
Visible property to No. 
 
o 
The point labels for Series1 are unnecessary, so select the label and set its 
Visible property to No. 
 
o 
Customize the Series2 marker's appearance. Replace the default circle with 
the upside-down triangle by the View.Point Marker Options.Kind property 
and set its Size to 12. 


---

Advanced Controls 
139 
 
 
 
 
 
 
Rotate the X-axis labels for better readability. Select the AxisX item in the chart by mouse 
click, and adjust properties for its labels (via the Label property). For instance, if the Angle 
property is 20 and the Antialiasing property is set to Yes, the labels look neat. 
 
 
 
If required, it is possible to customize many other properties for the chart, which are not 
described here. 
 
The chart is now ready. Switch to the Preview Tab, and view the result. 
 
 
To learn about another method of binding a chart to data, refer to the Chart using Dynamic 
Series tutorial. 


---

ReportWriter 
140 
 
 
 
 
Subreport Control 
 
Subreport Control 
 
The Subreport control allows you to include other reports into a current report. 
There are two essential reasons for using subreports. 
The first is to reuse reports. This can be practical if there is a particular report structure that 
has to be included in all reports, and the report must have a consistent appearance and 
functionality. A good example is a report header that contains the company information, the 
logo, the date etc. 
 
The second reason for using subreports is for a creation of master-detail reports (reports with 
hierarchically linked data). 
 
 
 
In the Property Grid, the Subreport's properties are divided into the following groups. 
 
Appearance 
 
Formatting Rules 
Invokes the Formatting Rules Editor allowing you to choose which rules should be applied to 
the control during report generation, and define the precedence of the applied rules. To learn 
more on this, refer to the Conditionally Change a Control's Appearance help topic. 
 
 
 
Behavior 
 
Can Shrink 
Determines whether a Subreport's height should be decreased if its contents don't completely 
fill the control. 
 
Use this property to specify whether the height of the Subreport control should be taken into 
account when generating a report. This may be required, because usually the mutual location 
of report controls is considered when generating a report document. But, as the Subreport 
control actually represents a report itself, the height of a Subreport normally should not be 
taken into account in the generated report document. 
 
Also, note that there is no Can Grow option for the Subreport control, as it always increases its 
height depending on its contents. 
 
Scripts 
This property contains events, which you can handle by the required scripts. For more 
information on scripting, refer to ReportWriter Scripting. 
 
Visible 
Specifies a value indicating whether the current control should be printed (when set to Yes) or 
hidden (No) on report generation. 
 
 
 
Data 
 
Report Source 
Determines a report to be included as a subreport. 
 
If report classes of the application that invoked the Report Designer are compiled into one 
assembly, then they are available as items in this combo box. 
 
 


---

Advanced Controls 
141 
 
 
 
 
Design 
 
(Name) 
Determines a control's name, by which it can be accessed in the Report Explorer, Property 
Grid or via scripts. 
 
 
 
Layout 
 
Location 
Specifies the control's location, in report measurement units. 
 
Size 
Specifies the control's size, in report measurement units. 
 
 
The Subreport isn't limited by the visible size of the control. The size of its actual content is 
taken into account when rendering the subreport on the page. Note that depending on its 
contents, its width is unlimited and its height is increased. 


---



---

143 
 
 
Advanced Topics 
 
Programmer's Guide to ReportWriter 
 
This section documents methods Clarion programmers can use to extend ReportWriter‘s 
capabilities, including how to incorporate ReportWriter‘s print engine into an application and 
techniques to add external libraries to ReportWriter. This chapter is intended only for Clarion 
programmers and the techniques require the Clarion and/or Clarion.NET development 
environment. 
 
If you are an end user of ReportWriter but not a programmer, you can benefit by reading this 
chapter only if you intend to program with Clarion or hire a Clarion developer. If you have 
purchased a copy of ReportWriter to use with a program developed with Clarion, you can 
contact that developer to request custom libraries to add the functionality you want. Reading 
this chapter, may help you determine what is possible or give you some ideas to discuss with 
the programmer. 
 
Integrating the Report Engine into Clarion Win32 Applications 
Integrating the Report Engine into Clarion.NET Applications 


---

144 
ReportWriter 
 
 
 
 
Integrating the Report Engine into Clarion Win32 Applications 
 
To access the Report Writer from your Clarion Win32 projects: 
 
1. Include RWPRLIB.INC in your source code. In applications use the After Global 
INCLUDEs global embed. 
 
2. Include the C70PRLB.LIB library in your project (or C%V%prlb%X%.lib to include a 
generic reference that will work in future versions of Clarion). 
 
The Win32 interface supports calling the legacy Win32 Report Writer Engine as well as the 
new .NET Report Writer Engine. Existing programs do not need to be changed. Which engine 
is used is controlled by calls to ReportEngine.LoadReportLibrary. If you pass the name of a 
TXR file to this method, then the Win32 Report Engine is used. If you pass the name of a 
REPXL file to this method, then the .NET Report Engine is used. 
 
After including the needed libraries and adding the necessary INCLUDE statement: 
 
 
Instantiate a ReportEngine object in your code. In applications use the Global Data 
embed and instantiate as follows: 
 
 
REObjectName 
ReportEngine 
 
 
Where REObjectName is the name of the instantiated object. 
 
After the ReportEngine object is instantiated, call any of the methods using the following 
syntax: 
 
 
REObjectName. methodname 
 
 
The ReportWriter Report Engine is supplied in two versions: 
Executable 
## C70PRNT.EXE
Dynamic Link Library 
## C70PRLB.DLL
The Report Engine is easily driven programmatically as a Dynamic Link Library 
(C70PRLB.DLL). It contains a simple object oriented interface that enables: 
 
 
 
Report libraries (i.e. TXR files) to be read and reports printed. 
 
The report preview to be replaced by user code. 
 
The record fetch mechanism to be tailored to user requirements. 
 
 
There is one class, ReportEngine, defined in RWPRLIB.INC which handles all the above 
functionality. To show how easy it can be to print a report from a Clarion program, the following 
is a full program that prints Report1 from RWDEMO1.TXR: 
 
## PROGRAM
MAP 
END 
## INCLUDE(‘RWPRLIB.INC’)
RE  ReportEngine 
! declare ReportEngine object 
## CODE
RE.LoadReportLibrary(‘RWDEMO1.TXR’) ! load report library 
RE.PrintReport(‘Report1’) 
! print report 


---

145 
Advanced Topics 
 
 
 
 
 
Clarion applications that incorporate the Report Engine as a Dynamic Linked Library must 
have the Run-Time Library linked in Standalone mode. The C70PRLB.DLL should not be 
referenced by a Local or Externally linked application. This will cause a multiple reference to 
the same Runtime library, and can cause a potential conflict with multiple heap allocations. 
You can use the Local mode only if the Clarion application is executed without an existing 
window structure. 
 
 
 
 
 
 
The ReportEngine class was designed to be backwards compatible. However, some of the 
methods that were available via the Win32 Report Engine are not available when calling the 
.NET Report Engine. Also, many features of the .NET Report Engine are not available when 
calling the Win32 Report Engine. 
 
The ReportEngine class contains the following methods which are valid regardless of if you 
load a TXR or a REPXL file: 
 
 
LoadReportLibrary(Load Report Library) 
PrintReport(Send Report to Printer) 
SetVariable(Set Report Parameter) 
SetPreview(Set if the Report Preview Dialog should appear) 
SetPrinter(Specify which printer should be used) 
SetReportFilter(Set Report Filter) 
SetReportOrder(Set Report Sort Order) 
UnloadReportLibrary(Unloads the current library) 
 
 
The ReportEngine class contains the following methods which are only valid if you load a 
TXR file: 
 
 
AttachOpenFile(Called to open a file) 
EndReport(Called when the report finishes) 
GetNextPageNumber(Get the number that will be printed on the next page) 
GetOpenMode(Get how the data files will be opened) 
Next(Get the next record) 
PrintAction(Perform the print) 
PrintHook(Method called when printing a report) 
ReadReportLibrary(Load the report library) 
Reset(Resets the view to the start) 
ResolveVariableFilename(Specify value for a variable filename) 
SetNextPageNumber(Set the page number to print on the next page) 


---

146 
ReportWriter 
 
 
 
 
SetNumberOfCopies(Set the number of copies to print) 
SetOpenMode(Set how the data files will be opened) 
SetPageRange(Set the range of pages to print) 
 
 
In addition to the above methods, the ReportEngine class also exposes the following 
members that can be used when overriding the PrintHook method 
 
ReportName 
The name of the current report 
 
Report 
The current report 
 
View 
VIEW structure used to access data for the current 
report 
 
PagesToPreview 
The number of pages to preview. 0 = no preview, -1 = 
all pages 
 
 
 
The ReportEngine class contains the following methods which are valid only when 
referencing a REPXL file: 
 
 
ExportCSV (Export report to a CSV file) 
ExportHTML (Export report to an HTML file) 
ExportImage (Export report to an image file) 
ExportMht (Export report to MHT file) 
ExportPDF (Export to PDF with user options) 
ExportPDF (Export report to PDF)  
ExportRTF (Export report to a RTF file) 
ExportText (Export report to Text) 
ExportXls (Export report to XLS format) 
GetReportList (List all reports in the library) 
UsePrinterDialog (When PrintReport is called the Printer Selection Dialog is displayed) 


---

147 
Advanced Topics 
 
 
 
 
Conceptual Example: 
 
 
C  ReportEngine !Create an instance of the ReportEngine 
## CODE
IF C.LoadReportLibrary('rwdemo1.repxl') 
C.SetPrinter() 
IF NOT C.PrintReport('Report1') 
MESSAGE('Failed to print to default printer') 
END 
C.SetPreview(1) 
C.SetPrinter('Microsoft XPS Document Writer') 
IF NOT C.PrintReport('Report1') 
MESSAGE('Failed to print to the XPS Document Writer') 
END 
C.UsePrinterDialog() 
C.SetReportFilter('Report1', '[STU:Number] > 20') 
C.SetReportOrder('Report1', 'STU:FirstName-') 
IF NOT C.PrintReport('Report1') 
MESSAGE('Failed to print with dialog and other stuff') 
END 
! The following code uses the same order and filter set above 
IF NOT C.ExportCSV('Report1', 'Report1.csv') 
MESSAGE('Failed to export to CSV') 
END 
IF NOT C.ExportHTML('Report1', 'Report1.html') 
MESSAGE('Failed to export to HTML') 
END 
IF NOT C.ExportImage('Report1', 'Report1.bmp', ImageFormat:Bmp) 
MESSAGE('Failed to export to BMP') 
END 
IF NOT C.ExportMht('Report1', 'Report1.mht') 
MESSAGE('Failed to export to MHT') 
END 
IF NOT C.ExportPdf('Report1', 'Report1.pdf') 
MESSAGE('Failed to export to Simple PDF') 
END 
IF NOT C.ExportRTF('Report1', 'Report1.rtf') 
MESSAGE('Failed to export to RTF') 
END 
IF NOT C.ExportText('Report1', 'Report1.txt') 
MESSAGE('Failed to export to text') 
END 
IF NOT C.ExportXls('Report1', 'Report1.xls') 
MESSAGE('Failed to export to Excel') 
END 
## ELSE
MESSAGE('Failed to open report library') 
END 


---

148 
ReportWriter 
 
 
 
 
Integrating the Report Engine into Clarion.NET Applications 
 
Calling your ReportWriter reports from any Clarion.NET application or project is a simple 
matter of adding an assembly. 
 
The SoftVelocity Report Previewer assembly contains built-in methods that you can use to 
control the manner in which reports print from your application. 
 
To work with the ReportWriter engine in Clarion# and C# projects you need to add an 
assembly reference to your project for the SoftVelocity.ReportPreviewer.dll assembly, and 
then create an instance of the ClarionReport class. 
 
After creating an instance of the ClarionReport class you can then load a Report Library, open 
any report contained in the library, and then call any of the methods listed below to print, 
preview or export the report using the following syntax: 
 
 
MyReportInstance.methodname 
 
 
The RptPreviewer class contains the following methods: 
 
 
Methods used to access reports: 
LoadLibrary(Load Report Library) 
GetReportList(Extract Reports in Library) 
OpenReport(Open a report from the Report Library - REPXL file) 
 
 
Methods for previewing and printing: 
PreviewReport(Open Report into Previewer) 
PrintReport(Send the report to the default Printer) 
PrintReport(Send the report to the specified Printer) 
PrintReportWithDialog(Send Report with Printer Dialog) 
 
Methods for filtering, ordering, and setting parameters: 
SetOrder(Set Report Sort Order) 
SetParameter(Set Report Parameter) 
SetReportFilter(Set Report Filter) 
 
Methods for exporting the report: 
ExportCSV(Export report to a CSV file) 
ExportHTML(Export report to an HTML file) 
ExportImage(Export report to an image file) 
ExportMht(Export report to MHT file) 
ExportPDF (Export to PDF with user options) 
ExportPDF(Export report to PDF) 
ExportRTF(Export report to a RTF file) 
ExportText(Export report to Text) 
ExportXls(Export report to XLS format) 


---

149 
Advanced Topics 
 
 
 
 
Using the ReportWriter engine from Clarion Win32 
 
LoadReportLibrary(Load either a REPXL or TXR report library) 
 
 
 
LoadReportLibrary(fullPathToLibrary, [, password ]) 
 
 
 
fullPathToLbrary 
A STRING containing the target REPXL or TXR file that identifies 
the report library to load. 
 
password 
Valid for TXR files only. The report library‘s password (if needed). 
If omitted, no password is passed to the report library. 
 
 
 
 
LoadReportLibrary detects that the specified report library file (*.REPXL or *.TXR) exists, 
changes to its directory and loads it. LoadReportLibrary returns TRUE if report exists and 
was successfully loaded, otherwise FALSE is returned 
 
 
The ReportWriter Win32 interface supports calling the legacy Win32 Report Writer Engine as 
well as the new .NET Report Writer Engine. Existing programs do not need to be changed. 
Which engine is used is controlled by calls to LoadReportLibrary. If you pass the name of a 
TXR file to this method, then the Win32 Report Engine is used. If you pass the name of a 
REPXL file to this method, then the .NET Report Engine is used. 
 
 
Return Value: 
## BOOLEAN
 
 
Example: 
 
 
## PROGRAM
MAP 
END 
## INCLUDE('RWPRLIB.INC')
RE ReportEngine 
## CODE
IF RE.LoadReportLibrary('rwdemo1.txr') 
! first load the report 
IF NOT RE.PrintReport('Report1') 
! run preview/print (report1) 
MESSAGE('Print Failed') 
END 
RE.UnloadReportLibrary 
## ELSE
MESSAGE('Load Failed') 
END 


---

ReportWriter 
150 
 
 
 
 
PrintReport (print a report) 
 
 
 
PrintReport ( reportname ),PROC,VIRTUAL 
 
 
PrintReport 
Print a report in the current report library (.TXR or .REPXL) file. 
 
reportname 
The name or number of the report to print. If an empty string (‗‘), a list of 
available reports is displayed allowing the user to select a report. 
PrintReport prints the specified report in the current report library (.TXR or .REPXL) file. The 
report can go directly to the printer or to a report preview (see SetPreview). 
This method returns TRUE if there were no errors during printing. 
Return Data Type: 
## SIGNED
Example: 
 
## PROGRAM
MAP 
END 
## INCLUDE('RWPRLIB.INC')
RE ReportEngine 
## CODE
IF RE.LoadReportLibrary('rwdemo1.txr') 
! first load the report 
IF NOT RE.PrintReport('Report1') 
! run preview/print (report1) 
MESSAGE('Print Failed') 
END 
RE.UnloadReportLibrary 
## ELSE
MESSAGE('Load Failed') 
END 
 
 
 
See Also: 
LoadReportLibrary, SetPreview 


---

Advanced Topics 
151 
 
 
 
 
SetPreview (Set report's preview on or off ) 
 
 
 
SetPreview( [ numberofpages ] ),VIRTUAL 
 
 
SetPreview 
Sets the report‘s preview mode. 
 
numberofpages 
The number of pages to preview. If omitted, all pages are previewed. 
 
 
 
 
SetPreview sets the report‘s preview mode. This defines whether a preview dialog is 
displayed before printing. 
 
If numberofpages is omitted (or negative) then preview is enabled for all pages of report. If 
numberofpages is 0, preview is disabled. This is the default after loading a report library. If 
numberofpages is positive only that number of pages display in the preview (although all 
pages will print). 
 
LoadReportLibrary must be called before attempting to use this method. The SetPreview 
method should be called before calling the PrintReport method. 
 
The value persists until a new report library is loaded or the UnloadReportLibrary method is 
called. 
 
Example: 
 
## PROGRAM
MAP 
END 
## INCLUDE('RWPRLIB.INC')
 
RE ReportEngine 
 
## CODE
IF RE.LoadReportLibrary('rwdemo1.txr')! first load the report 
RE.SetPreview(5) 
! after library loaded/before printin 
g 
IF NOT RE.PrintReport('Report1') 
! run preview/print (report1) 
MESSAGE('Print Failed') 
END 
RE.UnloadReportLibrary 
## ELSE
MESSAGE('Load Failed') 
END 
 
See Also: 
LoadReportLibrary, PrintReport, UnloadReportLibrary 


---

152 
ReportWriter 
 
 
 
 
SetPrinter (Set printer for report) 
 
 
 
SetPrinter( printerdef ),VIRTUAL 
 
 
SetPrinter 
Sets the report‘s printer. 
 
printerdef 
The printer name (device) as defined in the Windows Print Manager. 
 
 
 
 
SetPrinter sets the report‘s printer. The printerdef must match a definition in the Windows 
Print Manager. 
 
LoadReportLibrary must be called before attempting to use this method. The SetPrinter 
method should be called before calling the PrintReport method. 
 
The value persists until a new report library is loaded or the UnloadReportLibrary method is 
called. 
 
Example: 
 
 
## PROGRAM
MAP 
END 
## INCLUDE('RWPRLIB.INC')
RE ReportEngine 
## CODE
IF RE.LoadReportLibrary('rwdemo1.txr') ! first load the report 
RE.SetPrinter(‘hp4mv’) 
! after library loaded/before printi 
ng 
IF NOT RE.PrintReport('Report1') 
! run preview/print (report1) 
MESSAGE('Print Failed') 
END 
RE.UnloadReportLibrary 
## ELSE
MESSAGE('Load Failed') 
END 
 
 
See Also: 
LoadReportLibrary, PrintReport, UnloadReportLibrary 


---

153 
Advanced Topics 
SetReportFilter(Set Report Filter) 
 
 
 
SetReportFilter(reportname, filterString) 
 
 
 
reportname 
A STRING that identifies the name of the report to filter. 
 
filterString 
A string containing fields used to filter the report. For REPXL files only ,the 
fields defined in the filter string must be enclosed in brackets. 
 
 
 
 
SetReportFilter sets a filter based on the filterString. 
 
 
For REPXL files only ,the fields defined in the filter string must be enclosed in brackets: 
[filterstring] 
Example: 
## [PRO:COST]
 
 
The filter expression can use logical operators: AND, OR, NOT, LIKE. The use of LIKE follows 
the form; 
 
 
[PRO:DESCRIPTION] Like \'c%\' 
 
 
Single quotes in the filterString are preceded with the backslash ( \ ). 
 
 
If the filterString uses a "Parameter Field" it must be enclosed in brackets and must include the 
"Parameters." prefix before its name. 
Example: 
[Parameters.DiscountAmount] 
 
If the file has a prefix, the Filter expression requires the use of [ ] as in [prefix:fieldname]. String 
values on the right hand side of the expression must be enclosed in single quotes. 
 
 
LIKE can use either % or * for a wildcard at front or back of the value. 
Example: 
LIKE '%test', LIKE '*test', LIKE '%est%' 
 
 
The IN operator takes a list of values enclosed in parentheses. 
Example: 
LastName IN ('Bagley','Cade'), Zipcode IN (33062, 33358) 
Sample Filter Strings: 


---

154 
ReportWriter 
 
 
 
 
## ‘[PRO:COST] > 100’
!Cost is greater than 100 
 
 
## ‘[CUS:STATE] = ‘FL’’
 
 
!FILTER USING RUNTIME Parameters (the Parameter in the example is named "ID") 
‘[PEO:ID] < [Parameters.ID]’ 
!Note: The text of both 'Parameters' and 'ID' are case sensitive 
 
 
 
For TXR files only, brackets are NOT required when referencing field names in the 
filterstring. 
 
 
 
Implementation: 
You need to open the library only (using LoadReportLibrary) prior to applying the 
SetReportFilter method.. 
 
 
Example: 
## !WHEN REFERENCING A REPXL FILE:
RE.SetReportFilter('Customer List', '[CUS:CustomerNumber] > 5') 
 
## !WHEN REFERENCING A TXR FILE:
RE.SetReportFilter('Customer List', 'CUS:CustomerNumber > 5') 
 
 
 
See Also: 
LoadReportLibrary 


---

155 
Advanced Topics 
SetReportOrder(Set Report Sort Order) 
 
 
 
SetReportOrder(reportname, order) 
 
 
 
reportname 
A STRING that identifies the name of the report to filter. 
 
order 
A STRING containing a comma delimited list of fully qualified field names. 
When referncing a REPXL file, the field names must be enclosed in 
brackets. 
 
 
 
 
SetReportOrder sets a new sort order for the report. First, it removes any existing sort order. 
Each field name in the order parameter may have a plus or minus sign appended to it, to 
indicate either an ascending or descending sort order. 
 
 
For example: 
## ‗CUS:COUNTRY-,ORD:INVOICENUMBER+‘
 
 
If neither plus or minus sign is appended, the field is sorted ascending by default. 
 
 
Implementation: 
The report library must be opened prior to applying SetReportOrder (using 
LoadReportLibrary). 
 
 
Example: 
## !TXR FILE USAGE
RE.SetReportOrder('Customer List', 'Cus:FirstName-') 
 
## !REPXL FILE USAGE
RE.SetReportOrder('Customer List', '[Cus:FirstName-]') 
 
 
 
See Also: 
LoadReportLibrary 


---

156 
ReportWriter 
 
 
 
 
 
SetVariable (Set a value to a runtime variable) 
 
 
 
SetVariable( variablename , value, <description>, <visible>) 
 
 
SetVariable 
Sets a value to a runtime variable in a report. 
 
variablename 
The label of the runtime variable in the report. When referencing a REPXL 
file, the variable name must be enclosed in brackets. 
 
value 
The value to set to the runtime variable. 
 
description 
An optional STRING description to display for the variable when displayed in 
the variable dialog. 
 
Visible 
An optional Boolean flag to indicate if the variable should be displayed or 
not. The default value is FALSE 
 
 
SetVariable sets a value to a runtime variable in a report. The parameter used must already 
be defined in the report. You cannot assign a value to a non-existing parameter. 
 
 
Implementation: 
LoadReportLibrary must be called before attempting to use this method. The SetVariable 
method should be called to set a variable‘s value before calling the PrintReport method. 
The values persist until a new report library is loaded or the UnloadReportLibrary method is 
called. 
 
 
Example: 
 
## PROGRAM
MAP 
END 
## INCLUDE('RWPRLIB.INC')
RE ReportEngine 
## CODE
IF RE.LoadReportLibrary('rwdemo1.txr')! first load the report 
RE.SetVariable('UserName','Jimmy','User 
Name',TRUE) 
! after library loaded/before printing 
## !USE BRACKETS IF REFERENCING A REPXL FILE. FOR EXAMPLE
!RE.SetVariable('[UserName]','Jimmy','User Name',TRUE) 
IF NOT RE.PrintReport('Report1') 
! run preview/print (report1) 
MESSAGE('Print Failed') 
END 
RE.UnloadReportLibrary 
## ELSE
MESSAGE('Load Failed') 
END 
 
 
See Also: 
LoadReportLibrary, PrintReport, UnloadReportLibrary 


---

157 
Advanced Topics 
 
 
 
 
UnloadReportLibrary (Unload a ReportWriter Report Library) 
 
 
 
UnloadReportLibrary( ),VIRTUAL 
 
 
 
 
 
 
This method has been deprecated in this release and is only documented for 
compatibility with older ReportWriter versions. 
 
 
UnloadReportLibrary is a VIRTUAL method used to unload the current report library (.TXR or 
.REPXL) file. The intention of this method is to free resources allocated to a report library and 
clear any parameters set. It generally does not need to be called as it is automatically invoked 
by either loading a new report library or when the ReportEngine object is freed. 
 
This method returns TRUE if the specified TXR loads with no errors. 
 
Return Data Type:    SIGNED 
 
Example: 
 
 
## PROGRAM
MAP 
END 
## INCLUDE('RWPRLIB.INC')
RE ReportEngine 
## CODE
IF RE.LoadReportLibrary('rwdemo1.txr') 
! first load the report 
IF NOT RE.PrintReport('Report1') 
! run preview/print (report1) 
MESSAGE('Print Failed') 
END 
RE.UnloadReportLibrary 
## ELSE
MESSAGE('Load Failed') 
END 
 
 
 
See Also:    LoadReportLibrary 


---

158 
ReportWriter 
 
 
 
 
Methods only valid with TXR files 
Methods unique to working with TXR reports 
 
The ReportEngine class contains the following methods which are only valid when called from 
a Win32 application (Clarion 7 and greater) and when referencing a TXR report: 
 
 
AttachOpenFile(Called to open a file) 
EndReport(Called when the report finishes) 
GetNextPageNumber(Get the number that will be printed on the next page) 
GetOpenMode(Get how the data files will be opened) 
Next(Get the next record) 
PrintAction(Perform the print) 
PrintHook(Method called when printing a report) 
ReadReportLibrary(Load the report library) 
Reset(Resets the view to the start) 
ResolveVariableFilename(Specify value for a variable filename) 
SetNextPageNumber(Set the page number to print on the next page) 
SetNumberOfCopies(Set the number of copies to print) 
SetOpenMode(Set how the data files will be opened) 
SetPageRange(Set the range of pages to print) 
UsePrinterDialog (Open Printer Dialog) 
 
In addition to the above methods, the ReportEngine class also exposes the following 
members that can be used when overriding the PrintHook method 
 
ReportName 
The name of the current report 
 
Report 
The current report 
 
View 
VIEW structure used to access data for the current 
report 
 
PagesToPreview 
The number of pages to preview. 0 = no preview, -1 = 
all pages 


---

159 
Advanced Topics 
 
 
 
 
Advanced Techniques - Replacing Record Fetch 
Replacing Record Fetch 
For the advanced control of reports, you can derive the ReportEngine class and override the 
record fetch helper routines Reset and Next. This powerful engine allows for database access 
that cannot be specified using views. By using bound functions and variables it is possible to 
divorce the report from any database access entirely. 
Reset must initialize the file access so that the subsequent call to Next will return the first 
record that is to printed. It should return the number of records to print (if known) or -1 if not 
known or it is unreasonable to calculate. 
Next must fetch the next record to make it available for printing (via PrintAction). It must 
return Level:Benign if successful. Level:Notify if no more records are available or Level:Fatal if 
there has been an error. 
Example: 
 
## PROGRAM
MAP 
StopOnError 
END 
 
## INCLUDE('RWPRLIB.INC')
## INCLUDE('ABERROR.INC')
 
## Q QUEUE,PRE(Q),BINDABLE
Title STRING(40),NAME('BookTitle') 
Author STRING(30),NAME('BookAuthor') 
END 
 
QPos SHORT 
 
RE CLASS(ReportEngine) 
Reset 
PROCEDURE(),LONG,VIRTUAL ! returns records to process 
Next 
PROCEDURE(),BYTE,VIRTUAL ! returns 0 if finished 
END 
 
## CODE
Q:Title = 'Valis' 
Q:Author = 'Philip K. Dick' 
## ADD(Q)
Q:Title = 'At Swim Two Birds' 
Q:Author = 'Flann O''Brien' 
## ADD(Q)
Q:Title = 'Roads to Freedom' 
Q:Author = 'John Paul Sartre' 
## ADD(Q)
Q:Title = 'The Painted Bird' 
Q:Author = 'Jerzy Kosinski' 
## ADD(Q)
Q:Title = 'Staring at the Sun' 
Q:Author = 'Julian Barnes' 
## ADD(Q)
 
## BIND(Q)
RE.LoadReportLibrary('rwdemo2.txr') ! Load report 
library RE.SetPreview() 
! enable preview 
RE.PrintReport('Report2') 
! Print report 
StopOnError 
RE.UnloadReportLibrary 
StopOnError 


---

ReportWriter 
160 
 
 
 
 
 
StopOnError PROCEDURE 
## CODE
## IF ERRORCODE() = 90 THEN
## STOP(CLIP(FILEERROR()) & ' (' & CLIP(FILEERRORCODE()) & ')')
## ELSIF ERRORCODE()<>0 THEN
## STOP(CLIP(ERROR()) & ' (' & ERRORCODE() & ')')
END 
 
RE.Reset PROCEDURE 
## CODE
QPos = 0 
## RETURN RECORDS(Q)
 
RE.Next PROCEDURE 
## CODE
QPos += 1 
IF QPos>RECORDS(Q) THEN 
RETURN Level:Notify 
END 
GET(Q,QPos) 
RETURN Level:Benign 


---

Advanced Topics 
161 
 
 
 
 
AttachOpenFile (Attach an open file to a report) 
 
 
 
AttachOpenFile( label) ,VIRTUAL 
 
 
AttachOpenFile 
Attaches an open file to the report and overrides the report‘s file. 
 
label 
The label of the file. 
 
 
 
 
AttachOpenFile attaches an open file to the report and override the report‘s file. This allows 
you to replace the file specified in the report library with an open file. The label passed is the 
name of the file to replace. The function should return the FILE if it is required to be replaced, 
or should ‗pass-on‘ the call to PARENT.AttachOpenFile if not. 
 
This function need only be called in when the file to print is different from the file specified in  
the report library. You must ensure the FILE returned is already OPEN. The print engine does 
not open it. If the file definition is different to the original file specified in the report, then the all 
field names used must match in name and prefix. If the name and prefix do not match then you 
will need to BIND the fields used. 
 
Return Data Type: 
## FILE
Example: 
 
RE CLASS(ReportEngine) 
AttachOpenFile PROCEDURE(STRING label),*FILE,VIRTUAL ! To attach my own 
file END 
 
RE.AttachOpenFile 
PROCEDURE(STRING label) 
## CODE
IF label='students' 
! file to override 
RETURN students2 
! new file to attach 
END 
RETURN Parent.AttachOpenFile(label) ! leave others default 


---

ReportWriter 
162 
 
 
 
 
EndReport(Called when the report finishes) 
 
 
 
 
EndReport( ),VIRTUAL 
 
 
 
 
 
EndReport is one of the four helper functions used with PrintHook to allow you to "take over" 
some of the ReportEngine‘s internal functions and to control it in any way needed. This method 
is only valid during the PrintHook call. 
 
EndReport is called to simply close the report. It is only valid when processing TXR files. 
 
Implementation: 
 
EndReport should be called before any clean up of variables and objects is performed. 
 
Return Data Type: 
None 
 
Example: 
 
 
MyEngine.PrintHook 
## PROCEDURE(),SIGNED,VIRTUAL
## CODE
## LOOP
SELF.Reset() 
! Reset files/view 
## LOOP
CASE SELF.Next() 
! Record fetch 
OF Level:Notify 
## RETURN TRUE
OF Level:Fatal 
## RETURN FALSE
END 
SELF.PrintAction() 
! Print detail(s) 
END 
END 
SELF.EndReport() 
! Close the report 
 
 
See Also: PrintHook 


---

Advanced Topics 
163 
 
 
 
 
GetNextPageNumber (Get the next page number for report) 
 
 
 
 
GetNextPageNumber( pagenum ),VIRTUAL 
 
 
 
GetNextPageNumber 
Gets the number of the next page of a report. 
Pagenum 
The number of the next page. 
 
 
 
GetNextPageNumber retrieves the number (pagenum) of the next page that would print after 
the report. In other words one more than the last page of a report. This is useful when used in 
conjunction with SetNextPageNumber by allowing you access to the page number to use for 
the starting number of the next report. 
 
Implementation: 
 
LoadReportLibrary must be called before attempting to use this method. The 
GetNextPageNumber method should be called after calling the PrintReport method. 
 
Return Data Type:    LONG 
 
Example: 
 
 
## PROGRAM
MAP 
END 
## INCLUDE('RWPRLIB.INC')
RE ReportEngine 
## CODE
IF RE.LoadReportLibrary('rwdemo1.txr') 
! first load the report 
IF NOT RE.PrintReport('Report1') 
! run preview/print (report1) 
MESSAGE('Print Failed') 
## ELSE
RE.SetNextPageNumber(RE.GetNextPageNumber()) 
IF NOT RE.PrintReport('Report2') 
! run preview/print (report1) 
MESSAGE('Print Failed') 
END 
END 
RE.UnloadReportLibrary 
## ELSE
MESSAGE('Load Failed') 
END 
 
 
See Also:    LoadReportLibrary, PrintReport, UnloadReportLibrary, SetNextPageNumber 


---

164 
ReportWriter 
GetOpenMode(Get how the data files will be opened) 
 
 
 
GetOpenMode( ) 
 
 
 
 
GetOpenMode returns values set by the SetOpenMode method. If SetOpenMode has not 
been called, GetOpenMode returns 0. 
 
 
Return Data Type: 
## SIGNED
 
 
See Also: SetOpenMode 


---

165 
Advanced Topics 
Next(Get the next record) 
Next( ),VIRTUAL 
 
 
 
Next is one of the four helper functions used with PrintHook to allow you to "take over" some 
of the ReportEngine‘s internal functions and control it in any way needed. This method is only 
valid during the PrintHook call. 
 
For the advanced control of reports, you can derive the ReportEngine class and override the 
record fetch Reset and Next helper methods. The ReportEngine class allows for database 
access that cannot be specified using views. By using bound functions and variables it is 
possible to divorce the report from any database access entirely. 
 
 
Implementation: 
 
Next must fetch the next record to make it available for printing (via PrintAction). It must 
return Level:Benign if successful. Level:Notify if no more records are available or Level:Fatal if 
there has been an error. 
 
Return Data Type: 
## BYTE
 
Example: 
 
 
MyEngine.PrintHook 
## PROCEDURE(),SIGNED,VIRTUAL
## CODE
## LOOP
SELF.Reset() 
! Reset files/view 
## LOOP
CASE SELF.Next() 
! Record fetch 
OF Level:Notify 
## RETURN TRUE
OF Level:Fatal 
## RETURN FALSE
END 
SELF.PrintAction() 
! Print detail(s) 
END 
END 
SELF.EndReport() 
! Close the report 
 
 
See Also: PrintHook 
Advanced Techniques 


---

166 
ReportWriter 
 
 
 
PrintAction(Perform the print) 
 
 
 
 
PrintAction( ),VIRTUAL 
 
 
 
 
 
PrintAction is one of the four helper functions used with PrintHook to allows you to "take 
over" some of the ReportEngine‘s internal functions to allow you to control it in any way 
needed. This method is only valid during the PrintHook call. 
 
Implementation: 
 
PrintAction is called to simply print the record successfully retrieved from the Next method. It 
is only valid when processing TXR files. 
 
 
Return Data Type: 
None 
 
Example: 
 
 
LOOP RecordsPerCycle TIMES 
CASE SELF.Next() 
! Record fetch 
OF Level:Notify 
POST(Event:CloseWindow) 
! Finished (ok) 
## BREAK
OF Level:Fatal 
POST(Event:CloseWindow) 
! Finished (failed) 
Ok = False 
## BREAK
END 
 
SELF.PrintAction() 
! Print detail(s) 
RecordsProcessed += 1 
 
IF PreviewPages<>0 THEN 
IF (RECORDS(PrintPreviewQueue) >= PreviewPages) THEN 
PreviewPages = 0 
! Preview limit reached 
! NB there may be more pages than asked for! 
DO PrintPreview 
! So start preview 
IF NOT DoPrint THEN 
BREAK ALoop 
! Cancel (i.e. no print wanted) 
END 
! Otherwise continue loop 
END 
END 
 
END 
## !LOOP
See Also: PrintHook 
Advanced Techniques 


---

167 
Advanced Topics 
PrintHook(Method called when printing a report) 
PrintHook( ),VIRTUAL 
 
 
 
The Report Engine allows you to "take over" some of its internal functions to allow you to 
control it in any way needed. This is achieved by ‗taking over‘ the virtual PrintHook for your 
own class. 
 
MyEngine CLASS(ReportEngine) 
PrintHook 
## PROCEDURE(),SIGNED,VIRTUAL
END 
 
 
PrintHook is called from within the PrintReport method after the report definition is created. It 
is the PrintHook method‘s job to read the data from the file(s) and then print the details to the 
report. It does this by calling the following four helper functions: 
 
Reset 
PROCEDURE(),LONG,VIRTUAL ! returns records to process 
Next 
PROCEDURE(),BYTE,VIRTUAL ! returns Level:Notify at end 
PrintAction 
## PROCEDURE(),VIRTUAL
! called after next 
EndReport 
## PROCEDURE(),VIRTUAL
! call to close report 
! and using the following properties of the ReportEngine 
class: ReportName 
STRING(FILE:MaxFilePath) 
Report 
## &WINDOW
View 
## &VIEW
PagesToPreview 
## LONG
! 0 = no preview 
! -1 = all pages 
 
 
These methods and properties are only available during the PrintHook call. They are cannot be 
validly used at any other time. 
PrintHook returns a signed integer that you can use to flag that the report has been processed 
successfully. 
 
Return Data Type: 
## SIGNED
 
Example: 
 
The simplest PrintHook implementation (without preview) would be: 
 
MyEngine.PrintHook 
## PROCEDURE(),SIGNED,VIRTUAL
## CODE
## LOOP
SELF.Reset() 
! Reset files/view 
## LOOP
CASE SELF.Next() 
! Record fetch 
OF Level:Notify 
## RETURN TRUE
OF Level:Fatal 
## RETURN FALSE
END 
SELF.PrintAction() 
! Print detail(s) 
END 
END 
SELF.EndReport() 
! Close the report 


---

168 
ReportWriter 
 
 
 
 
 
This cycles through the records calling PrintAction for every record fetch. 
To include print preview, the code is considerably more complex but you can easily use the 
ABC Library (ABBROWSE and ABREPORT) to aid you in implementation. 
See RWDEMO2.CLW in the shipping examples for a model implementation including the 
handling of the progress window. 
 
 
See Also: PrintReport 


---

169 
Advanced Topics 
ReadReportLibrary (Read a Report Library into buffer) 
 
 
 
ReadReportLibrary( buffer, count) ,VIRTUAL 
 
 
ReadReportLibrary 
Reads a Report Library into buffer. 
 
buffer 
The buffer to hold the report library read. 
 
count 
The value to supply for the variable. 
 
 
 
 
ReadReportLibrary reads a Report Library into the buffer. This allows you to load a report 
library from a data element instead of a .TXR file (e.g., from a database). The function will be 
called by LoadReportLibrary to read the library in 64 KB chunks. A derived ReadReportLibrary 
should copy the contents of the report library into the supplied buffer and return the amount 
read. When the library has been fully read the function should return 0. 
Valid only fore TXR files. 
Return Data Type: 
## SHORT
Example: 
## PROGRAM
MAP 
END 
## INCLUDE('RWPRLIB.INC')
 
## NL EQUATE('<13,10>')
 
TestReport STRING( | 
## '[REPORTS]'
## & NL & |
'Report1 
REPORT,FONT(''Arial'',10),PRE(Report1),THOUS,AT(1000,1662,6500,8338)'&NL&| 
## '_REPORT_ BREAK'
## & NL & |
## '_TOTALS_
## BREAK'
## & NL & |
'Detail1 
DETAIL,FONT(''Arial'',8,0),AT(0,0,,1031)' 
## & NL & |
' 
STRING(@s20),USE(stu:FirstName),AT(51,0)' 
## & NL & |
' 
STRING(@s20),USE(stu:LastName),AT(1565,0)' 
## & NL & |
' 
STRING(@s12),USE(stu:Telephone),AT(3079,0)' 
## & NL & |
' 
## END'
## & NL & |
' 
## END'
## & NL & |
' 
## END'
## & NL & |
' 
## FOOTER,AT(1000,9000,,1000)'
## & NL & |
' 
STRING(@n5),PAGENO,AT(813,396,323)' 
## & NL & |
' 
STRING(''Page:''),AT(396,396)' 
## & NL & |
' 
## END'
## & NL & |
' 
## END'
## & NL & |
## '[FILES]'
## & NL & |
'students FILE,PRE(stu),DRIVER(''TOPSPEED''),NAME(''students.tps'')' & NL & | 
'KeyStudentNumber KEY(stu:Number),NOCASE,OPT'                  
## & NL & |
'MajorKey  KEY(stu:Major,stu:LastName,stu:FirstName),DUP,NOCASE,OPT'    & NL & 
| 


---

ReportWriter 
170 
 
 
 
 
'KeyLastName KEY(stu:LastName),DUP,NOCASE' 
## & NL & |
'KeyGradYear KEY(-stu:GradYear,stu:LastName,stu:FirstName),DUP,NOCASE,OPT' & NL & 
| 'Photo 
## MEMO(64000),BINARY'
## & NL & |
'  Record RECORD' 
## & NL & |
'Number 
## LONG'
## & NL & |
'FirstName 
## STRING(20)'
## & NL & |
'LastName 
## STRING(20)'
## & NL & |
'Address 
## STRING(20)'
## & NL & |
'Address2 
## STRING(20)'
## & NL & |
'City 
## STRING(20)'
## & NL & |
'State 
## STRING(2)'
## & NL & |
'Zip 
## LONG'
## & NL & |
'Telephone 
## STRING(12)'
## & NL & |
'Major 
## LONG'
## & NL & |
'GradYear 
## LONG'
## & NL & |
' 
## END'
## & NL & |
' 
## END'
## & NL & |
## NL & |
## '[REPORTVIEWS]'
## & NL & |
'Report1 VIEW(students),ORDER(''UPPER(stu:LastName)''),KEY(stu:KeyLastName)'&NL& 
| ' 
## END'
## & NL )
 
RE CLASS(ReportEngine) 
ReadReportLibrary 
PROCEDURE(*CSTRING buffer,USHORT count),SHORT,VIRTUAL 
Pos 
## SHORT
END 
 
## CODE
RE.Pos = 0 
RE.LoadReportLibrary('') 
RE.SetPreview() 
RE.SetNextPageNumber(10) 
RE.PrintReport('Report1') 
RE.UnloadReportLibrary 
 
RE.ReadReportLibrary 
PROCEDURE(*CSTRING buffer,USHORT count) 
! return report definition 
cntr USHORT 
i SHORT 
## CODE
cntr = SIZE(TestReport)-SELF.Pos 
IF cntr>count THEN cntr=count. 
LOOP i = 1 TO cntr 
SELF.Pos += 1 
buffer[i-1] = TestReport[SELF.Pos] 
END 
RETURN cntr 
!will return zero at end 


---

171 
Advanced Topics 
Reset(Resets the view to the start) 
 
 
 
 
Reset( ),VIRTUAL 
 
 
 
 
 
Reset is one of the four helper functions used with PrintHook to allow you to "take over" some 
of the ReportEngine‘s internal functions and control it in any way needed. This method is only 
valid during the PrintHook call. 
 
For the advanced control of reports, you can derive the ReportEngine class and override the 
record fetch Reset and Next helper methods. The ReportEngine class allows for database 
access that cannot be specified using views. By using bound functions and variables it is 
possible to divorce the report from any database access entirely. 
 
 
Implementation: 
 
Reset must initialize the file access so that the subsequent call to Next will return the first 
record that is to printed. It should return the number of records to print (if known) or -1 if not 
known or it is unreasonable to calculate. 
 
Return Data Type: 
## LONG
 
Example: 
 
 
MyEngine.PrintHook 
## PROCEDURE(),SIGNED,VIRTUAL
## CODE
## LOOP
SELF.Reset() 
! Reset files/view 
## LOOP
CASE SELF.Next() 
! Record fetch 
OF Level:Notify 
## RETURN TRUE
OF Level:Fatal 
## RETURN FALSE
END 
SELF.PrintAction() 
! Print detail(s) 
END 
END 
SELF.EndReport() 
! Close the report 
 
 
See Also: PrintHook 
Advanced Techniques 


---

172 
ReportWriter 
 
 
 
 
ResolveVariableFilename (Specify value for a variable filename) 
 
 
 
ResolveVariableFilename ( vname, value) ,VIRTUAL 
 
 
ResolveVariableFilename 
Resolves a variable filename used in a report. 
 
vname 
The label of the variable. 
 
value 
The value to supply for the variable. 
 
 
 
 
ResolveVariableFilename resolves a variable filename used in a report. This can be used for 
filenames that were specified to be variables in the dictionary used to create a report library. 
Using this function, you can avoid the dialog prompting for the variable name. This function 
should return TRUE if the variable name is recognized and value set to the filename, otherwise 
it should return FALSE. 
 
 
Return Data Type: 
## SIGNED
Example: 
 
RE CLASS(ReportEngine) 
ResolveVariableFilename PROCEDURE(STRING vname,*STRING value),SIGNED,VIRTUAL 
END 
 
RE.ResolveVariableFilename PROCEDURE(STRING vname,*STRING 
value) CODE 
IF label='!avariable' 
value = 'c:\examples\test.tps' 
## RETURN TRUE
END 
## RETURN FALSE


---

173 
Advanced Topics 
SetNextPageNumber (Set the next page number for report) 
 
 
 
SetNextPageNumber ( pagenum ),VIRTUAL 
 
 
SetNextPageNumber 
Sets the number of the next page of a report. 
 
pagenum 
The number of the next page. 
 
 
 
 
SetNextPageNumber sets the number (pagenum) of the next page of a report. This defines 
the value printed for the first and following (sequentially increasing) page numbers. This allows 
to reports to be printed using sequential page numbering 
 
LoadReportLibrary must be called before attempting to use this method. The 
SetNextPageNumber method should be called before calling the PrintReport method. 
 
The value persists until a new report library is loaded or the UnloadReportLibrary method is 
called. 
 
Example: 
 
 
## PROGRAM
MAP 
END 
## INCLUDE('RWPRLIB.INC')
RE ReportEngine 
## CODE
IF RE.LoadReportLibrary('rwdemo1.txr') ! first load the report 
RE.SetNextPageNumber(23) 
! after library loaded/before printi 
ng 
IF NOT RE.PrintReport('Report1') 
! run preview/print (report1) 
MESSAGE('Print Failed') 
END 
RE.UnloadReportLibrary 
## ELSE
MESSAGE('Load Failed') 
END 
 
 
 
See Also: 
LoadReportLibrary, PrintReport, UnloadReportLibrary, GetNextPageNumber 


---

174 
ReportWriter 
 
 
 
 
 
SetNumberOfCopies (Set number of copies to print for report) 
 
 
 
SetNumberOfCopies ( numcopies ),VIRTUAL 
 
 
SetNumberOfCopies 
Sets the number of copies to print for a report. 
 
numcopies 
The number of copies. 
 
 
 
SetNumberOfCopies sets the number of copies (numcopies) to print for a report. If this 
method is not called, one copy prints (the default). This may not be supported on all printers. 
 
LoadReportLibrary must be called before attempting to use this method. The 
SetNumberOfCopies method should be called before calling the PrintReport method. 
 
The value persists until a new report library is loaded or the UnloadReportLibrary method is 
called. 
 
Example: 
 
 
## PROGRAM
MAP 
END 
## INCLUDE('RWPRLIB.INC')
RE ReportEngine 
## CODE
IF RE.LoadReportLibrary('rwdemo1.txr') ! first load the report 
RE.SetNumberOfCopies(3) 
! after library loaded/before printi 
ng 
IF NOT RE.PrintReport('Report1') 
! run preview/print (report1) 
MESSAGE('Print Failed') 
END 
RE.UnloadReportLibrary 
## ELSE
MESSAGE('Load Failed') 
END 
 
 
 
See Also: 
LoadReportLibrary, PrintReport, UnloadReportLibrary 


---

175 
Advanced Topics 
 
 
 
 
SetOpenMode(Set how the data files will be opened) 
 
 
 
SetOpenMode( FileOpenMode ) 
 
 
 
SetOpenMode 
Set how files will be opened that are used in the report 
 
FileOpenMode 
A SIGNED integer that sets the file open mode. 
 
 
 
 
SetOpenMode is used to set the file open mode for data files referenced in the target report. 
This method is valid for TXR files only. The method is ignored for REPXL files. 
The FileOpenMode follows the existing documentation as follows: 
 
Dec 
Hex 
Access 
 
User Access: 
0 
0h 
Read Only 
1 
1h 
Write Only 
2 
2h 
Read/Write 
 
Other's Access: 
 
0 
0h 
Any Access (FCB compatibility mode) 
16 
10h 
Deny All 
32 
20h 
Deny Write 
48 
30h 
Deny Read 
64 
40h 
Deny None 
 
Implementation: 
 
SetOpenMode should be called prior to the SetPreview or PrintReport methods. 
 
Return Data Type: 
None 
 
Example: 
 
C.SetOpenMode(0) 
!Set files for read only access 
IF NOT C.PrintReport('Report1') 
MESSAGE('Failed to print with dialog and other stuff') 
END 
IF NOT C.ExportCSV('Report1', 'Report1.csv') 
MESSAGE('Failed to export to CSV') 
END 
 
 
See Also: GetOpenMode 


---

176 
ReportWriter 
 
 
 
 
SetPageRange (Set range of pages for report) 
 
 
 
SetPageRange( frompage [, topage ] ),VIRTUAL 
 
 
SetPageRange 
Sets the range of pages for a report. 
 
frompage 
The first page to include. 
 
topage 
The last page to include. 
 
 
 
 
SetPageRange sets the range of pages for a report. The frompage defines the beginning page 
of the report and the topage defines the ending page of the report. If the topage is omitted the 
report prints to the end. If this method is not called all pages print (the default). 
 
LoadReportLibrary must be called before attempting to use this method. The SetPageRange 
method should be called before calling the PrintReport method. 
 
The value persists until a new report library is loaded or the UnloadReportLibrary method is 
called. 
 
Example: 
 
 
## PROGRAM
MAP 
END 
## INCLUDE('RWPRLIB.INC')
 
RE ReportEngine 
 
## CODE
IF RE.LoadReportLibrary('rwdemo1.txr')! first load the report 
RE.SetPageRange(33,70) 
! after library loaded/before printin 
g 
IF NOT RE.PrintReport('Report1') 
! run preview/print (report1) 
MESSAGE('Print Failed') 
END 
RE.UnloadReportLibrary 
## ELSE
MESSAGE('Load Failed') 
END 
 
See Also: 
LoadReportLibrary, PrintReport, UnloadReportLibrary 


---

177 
Advanced Topics 
 
 
 
 
Methods only valid with REPXL files 
ExportCSV(Export report to a CSV file) 
 
 
 
ExportCSV (reportname, exportPathName, < runit>) 
 
 
 
exportPathName 
A string containing the full path and filename with extension. 
 
runIt 
A BOOLEAN value that when TRUE starts the process to open 
the generated CSV file. 
 
 
 
 
ExportCSV exports a report to the specified file path in CSV (comma separated value) format. 
 
 
Implementation: 
You need to open the library only using LoadReportLibrary prior to using the export method.. 
 
 
Example: 
RE.ExportCSV('Customer List', 'Exports\Report1.csv') 
 
 
See Also:  LoadReportLibrary 


---

178 
ReportWriter 
 
 
 
 
 
ExportHTML(Export report to an HTML file) 
 
 
 
ExportHTML (reportname, exportPathName, < runit>) 
 
 
 
reportname 
A STRING that identifies the name of the report to export. 
exportPathName 
A string containing the full path and filename with extension. 
runIt 
A BOOLEAN value that when TRUE starts the process to open the 
generated HTML file. 
 
 
 
 
ExportHTML exports a report to the specified file path in HTML format. 
 
 
Implementation: 
You need to open the library only using LoadReportLibrary prior to using the export method. 
 
 
Example: 
 
IF NOT RE.ExportHTML('Customer List', 'Report1.html') 
MESSAGE('Failed to export to HTML') 
END 
 
 
 
See Also:  LoadReportLibrary 


---

179 
Advanced Topics 
 
 
 
 
ExportImage(Export report to an image file) 
 
 
 
ExportImage (reportname, exportPathName, , imageFormat, < runit>) 
 
 
reportname 
A STRING that identifies the name of the report to export. 
exportPathName 
A string containing the full path and filename with extension. 
imageFormat 
A built-in number equate that represents the following image 
formats: 
 
ImageFormat:BMP 
## EQUATE(1)
ImageFormat:PNG 
## EQUATE(2)
ImageFormat:JPEG 
## EQUATE(3)
ImageFormat:EMF 
## EQUATE(4)
ImageFormat:WMF 
## EQUATE(5)
ImageFormat:GIF 
## EQUATE(6)
ImageFormat:TIFF    EQUATE(7) 
 
 
 
runIt 
A BOOLEAN value that when TRUE starts the process to open the 
Image in the default viewer. 
 
 
 
 
ExportImage exports a report to the specified file path in the imageFormat specified. 
 
 
Implementation: 
You need to open the library using LoadReportLibrary before calling any export methods. 
 
 
Example: 
 
IF NOT RE.ExportImage('Customer List', 'Report1.bmp', ImageFormat:Bmp) 
MESSAGE('Failed to export to BMP') 
END 
 
 
 
See Also: LoadReportLibrary 


---

ReportWriter 
180 
 
 
 
 
ExportMht(Export report to MHT file) 
 
 
 
ExportMHT (reportname, exportPathName, < runit>) 
 
 
 
reportname 
A STRING that identifies the name of the report to export. 
exportPathName 
A string containing the full path and filename with extension. 
runIt 
A BOOLEAN value that when TRUE starts the process to open the 
MHT file in the default viewer. 
 
 
 
 
ExportMht exports a report to the specified file path in MHT format. This method overwrites 
any files present at the specified path that have the same file name without any warnings. 
 
 
Implementation: 
You need to open the library only using LoadReportLibrary before using the export method. 
 
 
Example: 
 
IF NOT RE.ExportMHT('Customer List', 'Report1.MHT') 
MESSAGE('Failed to export to MHT') 
END 
 
 
 
See Also: 
LoadReportLibrary 


---

181 
Advanced Topics 
 
 
 
 
ExportPDF(Export report to PDF) 
 
 
 
ExportPDF (reportname, exportPathName, < runit>) 
 
 
 
reportname 
A STRING that identifies the name of the report to export. 
exportPathName 
A string containing the full path and filename with extension. 
runIt 
A BOOLEAN value that when TRUE starts the process to open the 
PDF file using the default setting. 
 
 
 
 
ExportPDF exports a report to PDF to the specified file path. You can optionally open PDF 
into the default viewer. 
 
 
Implementation: 
You need to open the library only (using LoadReportLibrary) prior to using the export method. 
 
 
Example: 
 
IF NOT RE.ExportPDF('Customer List', 'Report1.pdf') 
MESSAGE('Failed to export to Simple PDF') 
END 
 
 
 
See Also: LoadReportLibrary 


---

182 
ReportWriter 
 
 
 
 
 
ExportPDF (Export to PDF with user options) 
 
 
 
 
ExportPDF(reportname, exportPathName, compress, app, author, keywords, subject, title, 
imageQuality, pageRange, runit) 
 
 
 
reportname 
A STRING that identifies the name of the report to export. 
 
exportPathName 
A string containing the full path and filename with extension. 
 
Compress 
A BOOLEAN value that when TRUE will compress the resulting PDF file; 
otherwise false exports the PDF as uncompressed. The default is TRUE. 
 
app 
A string that represents an Application name 
 
author 
A string designating the author name 
 
keywords 
A string which contains keywords 
 
subject 
A string that names the PDF subject 
 
title 
A string that names the PDF title 
 
imageQuality 
An Integer within the range of 1-5 to specify the quality and the size of 
images when they are exported to PDF format 
 
 
1 = Lowest - resulting Jpeg image quality is the lowest (the resulting PDF 
file size is the smallest). 
 
 
2 = Low - resulting Jpeg image quality is low (the resulting PDF file size is 
small). 
 
 
3 = Medium - resulting Jpeg image quality is medium (the resulting PDF 
file size is also medium). 
 
 
4 = High - resulting Jpeg image quality is high (the resulting PDF file size 
is big). 
 
 
5 = Highest - resulting Jpeg image quality is the highest (the resulting 
PDF file size is the biggest) 
 
 
pageRange 
A string that specifies page ranges separated by commas. For example: 
"1,3,6-12" 
 
runIt 
A BOOLEAN value that when TRUE starts the process to open PDF 
using the default PDF viewer. 
 
 
 
 
ExportPDF is used to export a report to PDF to the specified file path and using the user 
specified options. It also optionally opens PDF into default viewer. 
 
 
Implementation: 


---

183 
Advanced Topics 
 
 
 
 
You need to open the library only (using LoadReportLibrary) prior to using the export method. 
 
 
 
Example: 
 
IF NOT RE.ExportPDF('TestingPDF.pdf', TRUE, 
'RWExport','SVSupport','PDF','MySubject','MyTitle',4,'1',TRUE) 
MESSAGE('Failed to export to Simple PDF') 
END 
 
 
 
See Also: 
LoadReportLibrary 


---

184 
ReportWriter 
 
 
 
 
ExportRTF(Export report to a RTF file) 
 
 
 
ExportRTF (reportname, exportPathName, < runit>) 
 
 
 
reportname 
A STRING that identifies the name of the report to export. 
exportPathName 
A string containing the full path and filename with extension. 
runIt 
A BOOLEAN value that when TRUE starts the process to open the 
generated HTML file. 
 
 
 
 
ExportRTF exports a report to the specified file path in RichText format. 
 
 
Implementation: 
You need to open the library only (using LoadReportLibrary) prior to using the export method. 
 
 
Example: 
 
IF NOT RE.ExportRTF('Customer List', 'Report1.RTF') 
MESSAGE('Failed to export to RTF') 
END 
 
 
 
See Also: 
LoadReportLibrary 


---

185 
Advanced Topics 
 
 
 
 
ExportText(Export report to Text) 
 
 
 
ExportText (reportname, exportPathName, < runit>) 
 
 
 
reportname 
A STRING that identifies the name of the report to export. 
exportPathName 
A string containing the full path and filename with extension. 
runIt 
A BOOLEAN value that when TRUE starts the process to open text 
file in the default viewer. 
 
 
 
 
ExportText exports a report to the specified file path in Text format. 
 
 
Implementation: 
You need to open the library only (using LoadReportLibrary) prior to using this export 
method. 
 
 
Example: 
 
IF NOT RE.ExportText('Customer List', 'Report1.TXT') 
MESSAGE('Failed to export to Text') 
END 
 
 
 
See Also: 
LoadReportLibrary 


---

186 
ReportWriter 
ExportXls(Export report to XLS format) 
ExportXls (reportname, exportPathName, < runit>) 
reportname 
exportPathName 
runIt 
A STRING that identifies the name of the report to export. 
A string containing the full path and filename with extension. 
A BOOLEAN value that when TRUE starts the process to open the 
XLS file using the default setting. 
 
 
 
ExportXls exports a report to the specified file path in XLS format. 
 
 
Implementation: 
You need to open the library only (using LoadReportLibrary) prior to using the export method. 
 
 
Example: 
 
IF NOT RE.ExportXLS('Customer List', 'Report1.XLS') 
MESSAGE('Failed to export to XLS Format') 
END 
 
 
 
See Also:  LoadReportLibrary 


---

187 
Advanced Topics 
 
 
 
 
 
GetReportList(Extract Reports in Active Library) 
 
 
 
GetReportList(PrintPreviewFileQueue returnedList) 
 
 
GetReportList 
Extract report names from active library 
 
returnedlist 
a reference to PrintPreviewFileQueue 
 
 
 
 
GetReportList reads the list of reports found in the active (loaded) Library (repxl file). It adds 
the list of reports found in the current Library to the passed queue 
If the library has not be loaded using the LoadReportLibrary method, GetReportList the 
queue passed will be empty. 
 
Return Value: 
None 
Example: 
C 
reports 
ReportEngine 
PrintPreviewFileQueue 
 
Window WINDOW('RW Test'),AT(,,260,100),GRAY 
BUTTON('Run Tests'), AT(86,33), USE(?BUTTON1) 
END 
## CODE
OPEN(Window) 
## ACCEPT
IF EVENT() = EVENT:Accepted AND ACCEPTED() = ?BUTTON1 
DoTests() 
## BREAK
END 
END 
CLOSE(Window) 
 
DoTests 
## PROCEDURE()
## CODE
IF C.LoadReportLibrary('rwdemo1.repxl') 
C.GetReportList(reports) 
END 
 
 
 
See Also: 
LoadReportLibrary 


---

188 
ReportWriter 
 
 
 
 
UsePrinterDialog (Open Printer Dialog) 
 
 
 
UsePrinterDialog( ) 
 
 
 
 
UsePrinterDialog sends the active report to a designated printer, but first opens the operating 
system‘s Printer Dialog window, allowing the user to direct the report to a target printer. 
 
 
Implementation: 
When PrintReport is called a dialog will be displayed to allow the user to select which printer 
to use. This will override previous calls to SetPrinter. 
 
 
Example: 
 
!Source to call REPXL interface 
IF RE.LoadReportLibrary('InvoiceReports.repxl') !Open the library 
RE.UsePrinterDialog() 
RE.PrintReport('Customer List') 
!Show report to print 
## ELSE
MESSAGE('Failed to open report library') 
END 
 
 
See Also: PrintReport, SetPrinter 


---

189 
Advanced Topics 
 
 
 
 
Using the ReportWriter engine from Clarion.NET 
 
ExportCSV(Export report to a CSV file) 
 
 
 
ExportCSV (exportPathName, runIt) 
 
 
 
exportPathName 
A string containing the full path and filename with extension. 
 
runIt 
A BOOLEAN value that when TRUE starts the process to open 
the generated CSV file. 
 
 
 
 
ExportCSV exports a report to the specified file path in CSV (comma separated value) format. 
 
 
Implementation: 
You must have the library and report opened with the LoadLibrary and OpenReport methods. 
Prior to using any export methods. 
 
 
Example: 
SELF.rpt.ExportCSV('ExportReport.csv', TRUE) 
 
 
See Also: LoadLibrary, OpenReport 


---

ReportWriter 
190 
 
 
 
 
ExportHTML(Export report to an HTML file) 
 
 
 
ExportHTML (exportPathName, runIt) 
 
 
 
exportPathName 
A string containing the full path and filename with extension. 
 
runIt 
A BOOLEAN value that when TRUE starts the process to open the 
generated HTML file. 
 
 
 
 
ExportHTML exports a report to the specified file path in HTML format. 
 
 
Implementation: 
You must have the library and report opened with the LoadLibrary and OpenReport methods 
prior to using the export method. 
 
 
Example: 
SELF.rpt.ExportHTML('MyReport.htm', TRUE) 
 
 
See Also: LoadLibrary, OpenReport 


---

Advanced Topics 
191 
 
 
 
 
ExportImage(Export report to an image file) 
 
 
 
Clarion# prototype: 
ExportImage (exportPathName, imageFormat, runIt) 
 
 
 
exportPathName 
A string containing the full path and filename with extension. 
 
imageFormat 
An ENUM containing one of the following values; 
ImageFormat.BMP 
ImageFormat.PNG 
ImageFormat.JPEG 
ImageFormat.EMF 
ImageFormat.WMF 
ImageFormat.GIF 
ImageFormat.TIFF 
 
runIt 
A BOOLEAN value that when TRUE starts the process to open the 
Image in the default viewer. 
 
 
 
 
ExportImage exports a report to the specified file path in the imageFormat specified. 
 
 
Implementation: 
You must have the library and report opened with the LoadLibrary and OpenReport methods. 
Prior to using any of the export methods. 
 
 
Example: 
SELF.rpt.ExportImage('MyReport.png', ImageFormat.Png, TRUE) 
 
 
See Also: LoadLibrary, OpenReport 


---

ReportWriter 
192 
 
 
 
 
 
ExportMht(Export report to MHT file) 
 
 
 
ExportMHT (exportPathName, runIt) 
 
 
 
exportPathName 
A string containing the full path and filename with extension. 
 
runIt 
A BOOLEAN value that when TRUE starts the process to open the 
MHT file in the default viewer. 
 
 
 
 
ExportMht exports a report to the specified file path in MHT format. This method overwrites 
any files present at the specified path that have the same file name without any warnings. 
 
 
Implementation: 
You must have the library and report opened with the LoadLibrary and OpenReport methods 
prior to using the export method. 
 
 
Example: 
SELF.rpt.ExportMHT('MyReport.MHT', TRUE) 
 
 
See Also: LoadLibrary, OpenReport 


---

193 
Advanced Topics 
 
 
 
 
ExportPDF(Export report to PDF) 
 
 
 
ExportPDF (exportPathName, runIt) 
 
 
 
exportPathName 
A string containing the full path and filename with extension. 
 
runIt 
A BOOLEAN value that when TRUE starts the process to open the 
PDF file using the default setting. 
 
 
 
 
ExportPDF exports a report to PDF to the specified file path. You can optionally open PDF 
into the default viewer. 
 
 
Implementation: 
You must have the library and report opened with the LoadLibrary and OpenReport methods 
prior to using the export method. 
 
 
Example: 
SELF.rpt.ExportPDF('TestingPDF.pdf', TRUE) 
 
 
See Also: LoadLibrary, OpenReport 


---

194 
ReportWriter 
 
 
 
 
ExportPDF (Export to PDF with user options) 
 
 
 
 
ExportPDF( exportPathName, compress, app, author, keywords, subject, title, imageQuality, 
pageRange, runit) 
 
 
 
exportPathName 
A string containing the full path and filename with extension. 
 
Compress 
A BOOLEAN value that when TRUE will compress the resulting PDF file; 
otherwise false exports the PDF as uncompressed. The default is TRUE. 
 
app 
A string that represents an Application name 
 
author 
A string designating the author name 
 
keywords 
A string which contains keywords 
 
subject 
A string that names the PDF subject 
 
title 
A string that names the PDF title 
 
imageQuality 
You must use the appropriate ENUM as follows: 
 
PdfJpegImageQuality.Lowest 
PdfJpegImageQuality.Low 
PdfJpegImageQuality.Medium 
PdfJpegImageQuality.High 
PdfJpegImageQuality.Highest 
 
 
pageRange 
A string that specifies page ranges separated by commas. For example: 
"1,3,6-12" 
 
runIt 
A BOOLEAN value that when TRUE starts the process to open PDF 
using the default PDF viewer. 
 
 
 
 
ExportPDF is used to export a report to PDF to the specified file path and using the user 
specified options. It also optionally opens PDF into default viewer. 
 
 
Implementation: 
Prior to using ExportPDF, you must have the library and report opened with the LoadLibrary 
and OpenReport methods. 
 
 
The imageQuality parameter requires you to first add the following reference to your project: 
DevExpress.Utils.v9.1 
 
 
Next, reference the assembly with the following USING directive: 
 
 
USING DevExpress.XtraPrinting 


---

195 
Advanced Topics 
 
 
 
 
Example: 
 
SELF.rpt.ExportPDF('TestingPDF.pdf', TRUE, 
'RWExport','SVSupport','PDF','MySubject','MyTitle', 
PdfJpegImageQuality.High,'1',TRUE) 
 
See Also: LoadLibrary, OpenReport 


---

196 
ReportWriter 
ExportRTF(Export report to a RTF file) 
ExportRTF (exportPathName, runIt) 
exportPathName 
runIt 
A string containing the full path and filename with extension. 
A BOOLEAN value that when TRUE starts the process to open the 
generated HTML file. 
 
 
 
ExportRTF exports a report to the specified file path in RichText format. 
 
 
Implementation: 
You must have the library and report opened with the LoadLibrary and OpenReport methods. 
Prior to using the export method. 
 
 
Example: 
SELF.rpt.ExportRTF('MyReport.RTF', TRUE) 
 
 
See Also: LoadLibrary, OpenReport 


---

197 
Advanced Topics 
 
 
 
 
 
ExportText(Export report to Text) 
 
 
 
ExportText (exportPathName, runIt) 
 
 
 
exportPathName 
A string containing the full path and filename with extension. 
 
runIt 
A BOOLEAN value that when TRUE starts the process to open text 
file in the default viewer. 
 
 
 
 
ExportText exports a report to the specified file path in Text format. 
 
 
Implementation: 
You must have the library and report opened with the LoadLibrary and OpenReport methods. 
Prior to opening the export method. 
 
 
Example: 
SELF.rpt.ExportText('MyReport.TXT', TRUE) 
 
 
See Also: LoadLibrary, OpenReport 


---

198 
ReportWriter 
ExportXls(Export report to XLS format) 
ExportXls (exportPathName, runIt) 
exportPathName 
runIt 
A string containing the full path and filename with extension. 
A BOOLEAN value that when TRUE starts the process to open the 
XLS file using the default setting. 
 
 
 
ExportXls exports a report to the specified file path in XLS format. 
 
 
Implementation: 
You must have the library and report opened with the LoadLibrary and OpenReport methods. 
Prior to using this export method. 
 
 
Example: 
SELF.rpt.ExportXLS('MyReport.XLS', TRUE) 
 
 
See Also: LoadLibrary, OpenReport 


---

199 
Advanced Topics 
 
 
 
 
GetReportList(Extract Reports in Library) 
 
 
 
GetReportList() 
 
 
GetReportList 
Extract report names from active library 
 
 
 
 
GetReportList reads the list of reports found in the active (loaded) Library (repxl file). It adds 
the list of reports found in the current Library to the assigned string array. 
 
 
Return Value: 
a STRING array 
 
 
Example: 
 
!programmatically open the report library 
reportFolderName = System.IO.Directory.GetCurrentDirectory() 
!concatenetate the full path to the Repxl file 
reportFolderName = ReportDir & 
'Reports\MailLabels.Repxl') 
SELF.rpt.LoadLibrary(reportFolderName) 
reportList OF string[] = SELF.rpt.GetReportList()!STRING array of reports in active library 
 
 
 
 
See Also: 
LoadLibrary 


---

ReportWriter 
LoadLibrary(Load Report Library) 
200 
 
 
 
LoadLibrary( fullPathToLibrary ) 
 
 
fullPathToLbrary 
A STRING containing the target REPXL file that identifies the report 
library to load. 
 
 
 
 
LoadLibrary detects that the specified report library file (*.REPXL) exists, changes to its 
directory and loads it. LoadReport returns TRUE if report exists and was successfully loaded, 
otherwise FALSE is returned 
 
 
Return Value: 
## BOOLEAN
 
 
Examples: 
 
 
 
!let the user select the Report Library to open 
fd OF OpenFileDialog = NEW OpenFileDialog() 
fd.Filter = 'repxl files (*.repxl)| *.repxl' 
IF (fd.ShowDialog() = DialogResult.OK) 
!OpenFileDialog.FileName returns the full path & filename 
SELF.rpt.LoadLibrary(fd.FileName) 
!open the Report Library 
END 
 
!programmatically open the report library 
reportFolderName = System.IO.Directory.GetCurrentDirectory() 
!concatenetate the full path to the Repxl file 
reportFolderName = ReportDir & 'Reports\MailLabels.Repxl') 
SELF.rpt.LoadLibrary(reportFolderName) 
!open the Report Library 
 
 
 
See Also: OpenReport 


---

Advanced Topics 
201 
 
 
 
 
OpenReport(Open a report from the Report Library - REPXL file) 
 
 
 
OpenReport(ReportID) 
 
 
 
ReportID 
An integer representing the numeric position of the report in the active 
library. 
 
 
 
 
OpenReport opens a report identified by the numeric position contained in the active (loaded) 
report library. OpenReport returns TRUE if the report was successfully loaded, otherwise 
FALSE if there is no loaded library or the report ID is out of range (does not exist). 
 
 
Return Value: 
## BOOLEAN
 
 
See Also: 
Load Library 


---

202 
ReportWriter 
PreviewReport(Open Report into Previewer) 
PreviewReport() 
 
 
 
PreviewReport opens the active report (opened using the OpenReport method) 
PreviewReport returns TRUE if the report was successfully loaded, otherwise FALSE if there 
is no loaded library or opened report. 
 
 
Return Value: 
## BOOLEAN
 
 
See Also: 
OpenReport 


---

203 
Advanced Topics 
 
 
 
 
 
PrintReport(Send Report to Printer) 
 
 
 
PrintReport( <targetPrinter>) 
 
 
targetPrinter 
An optional string containing the name of the specific printer to use to direct 
the report. 
 
 
 
 
PrintReport sends the active report to the designated printer. If the targetPrinter parameter is 
omitted, the system default printer is used. 
Return Data Type: 
None 
 
 
Example: 
 
!Get the name of the file to open from the ListBox. 
SELF.repID = Self.rpts_listBox.SelectedIndex 
TRY 
SELF.rpt.OpenReport(self.repID) 
SELF.rpt.PrintReport() 
CATCH(Exception ex) 
MessageBox.Show('Error opening report: '& ex.Message) 
END 
SELF.label1.Text = 'Active Report: ' & self.rpts_listBox.SelectedItem.ToString() 
 
 
 
 
See also: 
OpenReport(Open a report from the REPXL file) 


---

204 
ReportWriter 
PrintReportWithDialog(Send Report with Printer Dialog) 
PrintReportWithDialog( ) 
 
 
 
PrintReportWithDialog sends the active report to a designated printer, but first opens the 
operating system‘s Printer Dialog window, allowing the user to direct the report to a target 
printer. 
 
 
Example: 
 
!Get the name of the file to open from the ListBox. 
SELF.repID = Self.rpts_listBox.SelectedIndex 
TRY 
SELF.rpt.OpenReport(self.repID) 
SELF.rpt.PrintReportWithDialog() 
CATCH(Exception ex) 
MessageBox.Show('Error opening report: '& ex.Message) 
END 
SELF.label1.Text = 'Active Report: ' & self.rpts_listBox.SelectedItem.ToString() 
 
 
 
 
See also: 
OpenReport(Open a report from the REPXL file) 


---

205 
Advanced Topics 
 
 
 
 
SetOrder (Set Report Sort Order) 
 
 
 
SetOrder(order) 
 
 
order                      A string containing a comma delimited list of fully qualified field names. 
Field names must be enclosed in brackets. 
 
 
 
 
SetOrder sets a new sort order for the report. First, it removes any existing sort order. Each 
field name in the order parameter may have a plus or minus sign appended to it, to indicate 
either an ascending or descending sort order. 
 
 
For example: 
## ‗CUS:COUNTRY-,ORD:INVOICENUMBER+‘
 
 
If neither plus or minus sign is appended, the field is sorted ascending by default. 
 
 
Implementation: 
You must have the library and report opened with the LoadLibrary and OpenReport methods. 
 
 
Example: 
 
 
SELF.rpt.SetOrder('[Cus:FirstName-]') 
## !OR:
SELF.rpt.SetOrder(SELF.txtOrder.Text) 
 
!Allow 
user-defined 
order 
 
 
 
See Also: LoadLibrary, OpenReport 


---

206 
ReportWriter 
 
 
 
 
SetParameter(Set Report Parameter) 
 
 
 
SetParameter(name, value, description, visible) 
 
 
name 
The parameter name assigned in the target report. 
 
value 
The value to assign to the report parameter. The value type is determined by 
the parameter‘s Value property assigned. 
 
description 
A STRING description that describes the parameter to the end user. 
 
visible 
A BOOLEAN value that sets whether the parameter is shown in the parameter 
dialog (is visible to the user). 
 
 
 
 
SetParameter sets a named parameter‘s value, description and visibility to the end user at 
report runtime. 
The parameter used must already be defined in the report. You cannot assign a value to a 
non-existing parameter. 
 
 
Implementation: 
You must have the library and report opened with the LoadLibrary and OpenReport methods. 
 
 
Example: 
 
IF (SELF.visibleCheck.Checked) 
Visible = TRUE 
## ELSE
Visible = FALSE 
END 
SELF.rpt.SetParameter(SELF.txtName.Text, 
SELF.txtValue.Text,SELF.txtDescription.Text, visible) 
 
 
 
See Also: LoadLibrary, OpenReport 


---

207 
Advanced Topics 
 
 
 
 
SetReportFilter(Set Report Filter) 
 
 
 
SetReportFilter(filterString) 
 
 
 
filterString 
A string containing fields used to filter the report. For REPXL files only ,the 
fields defined in the filter string must be enclosed in brackets. 
 
 
 
 
SetReportFilter sets a filter based on the filterString. 
 
 
For REPXL files only ,the fields defined in the filter string must be enclosed in brackets: 
[filterstring] 
Example: 
## [PRO:COST]
 
 
The filter expression can use logical operators: AND, OR, NOT, LIKE. The use of LIKE follows 
the form; 
 
 
[PRO:DESCRIPTION] Like \'c%\' 
 
 
Single quotes in the filterString are preceded with the backslash ( \ ). 
 
 
If the filterString uses a "Parameter Field" it must be enclosed in brackets and must include the 
"Parameters." prefix before its name. 
Example: 
[Parameters.DiscountAmount] 
 
If the file has a prefix, the Filter expression requires the use of [ ] as in [prefix:fieldname]. String 
values on the right hand side of the expression must be enclosed in single quotes. 
 
 
LIKE can use either % or * for a wildcard at front or back of the value. 
Example: 
LIKE '%test', LIKE '*test', LIKE '%est%' 
 
 
The IN operator takes a list of values enclosed in parentheses. 
Example: 
LastName IN ('Bagley','Cade'), Zipcode IN (33062, 33358) 
Sample Filter Strings: 
## ‘[PRO:COST] > 100’
!Cost is greater than 100 


---

208 
ReportWriter 
 
 
 
 
## ‘[CUS:STATE] = ‘FL’’
 
 
!FILTER USING RUNTIME Parameters (the Parameter in the example is named "ID") 
‘[PEO:ID] < [Parameters.ID]’ 
!Note: The text of both 'Parameters' and 'ID' are case sensitive 
 
 
 
For TXR files only, brackets are NOT required when referencing field names in the 
filterstring. 
 
 
 
Implementation: 
You must have the library and report opened with the LoadLibrary and OpenReport methods. 
Prior to applying the SetReportFilter method. 
 
 
Example: 
SELF.rpt.SetReportFilter('[CUS:CustomerNumber] > 5') 
 
 
See Also: LoadLibrary, OpenReport 


---

209 
Advanced Topics 
 
 
 
 
Scripting 
 
Report Writer Scripting 
A powerful scripting engine is included in ReportWriter. Support is provided for Clarion#, C#,  
J# and Visual Basic. These scripts can be used in a wide variety of Report Events. Your power 
and extensibility of your report design is virtually unlimited now. 
Start by designating the scripting language in the Report control: 
 
 
 
 
 
Next, choose an event where your script can be added. 
 
 
 
 
 
As the report is previewed, the script is compiled and executed during the specified report 
event. 


---

ReportWriter 
210 
 
 
 
 
Scripting Syntax Rules for Clarion# 
Refer to the following Clarion# code example: 
 
OnBeforePrint PROCEDURE(System.Object sender, System.Drawing.Printing.PrintEventArgs 
e),PRIVATE INLINE 
## CODE
label12.Text = SELF.GetCurrentColumnValue('PUB:CITY').ToString() 
END 
 
 
1. You must use SELF to refer to any of the ReportWriter methods. 
2. The GetCurrentColumnValue() method is used to read a field‘s value. 
3. In a report using a Clarion Dictionary data source; refer to a field using the following 
syntax: 
PREFIX:LABEL !(UPPER CASE is required) 
4. In a report using a Standard Data Source, refer to a field using an exact match of the field 
name case. 
If there is any error in the field name case, a Null Referenced Error will be posted. 


---

211 
 
 
Distribution (of Reports) 
 
Distributing your Reports 
 
 
To distribute reports to computers which do not have ReportWriter installed, you must first 
install the 2.0 .NET Framework runtimes, and then provide the following files to the program 
directory: 
 
 
 
Your Report Library file 
(name.TXR or name.REPXL) 
 
 
The runtime Print 
Engine 
 
 
The Runtime Library 
file: 
 
## C70PRNT.EX
E 
## C70RUN.DLL
 
Any Data Files the report uses. 
File Driver(s): 
The appropriate File Driver for the format of your data files (one or more from the list below): 
 
 
File 
Library 
 
## ASCII
## C70ASCX.DLL
 
## BASIC
## C70BASX.DLL
 
Btrieve 
## C70BTRX.DLL
 
Clarion 
## C70CLAX.DLL
 
Clipper 
## C70CLPX.DLL
 
dBase III 
## C70DB3X.DLL
 
dBase IV 
## C70DB4X.DLL
 
DOS 
## C70DOSX.DLL
 
FoxPro 
## C70FOXX.DLL
 
## ODBC
## C70ODBX.DLL
 
## MSSQL
## C70MSS.DLL
 
Pervasive 
## C70SCAX.DLL
 
TopSpeed 
## C70TPSX.DLL
 
 
 
Other Clarion DLLs (found in the Clarion BIN folder) 
C70asl.DLL 
C70cbc.DLL 
C70cpxml.DLL 
C70def.DLL 
## C70PRLIB.DLL
C70prnet.DLL 
 
 
 
 
Other related assemblies (also found in the Clarion BIN folder) 


---

ReportWriter 
212 
 
 
 
 
Aga.Controls.DLL 
Clarion.asl.DLL 
Clarion.Core.DLL 
Clarion.Options.DLL 
ClarionDRV.DLL 
DataDictionary.DLL 
DataDictionaryFile.DLL 
DevExpress.Data.v9.1.DLL 
DevExpress.Utils.v9.1.DLL 
DevExpress.XtraBars.v9.1.DLL 
DevExpress.XtraEditors.v9.1.DLL 
DevExpress.XtraPrinting.v9.1.DLL 
DevExpress.XtraReports.v9.1.DLL 
DevExpress.XtraTreeList.v9.1.DLL 
IPSharpCode.Core.DLL 
IPSharpCode.SharpDevelop.DLL 
IPSharpCode. SharpDevelop.Dom.DLL 
Log4net.DLL 
SoftVelocity.Clarion.FileIO.DLL. 
SoftVelocity.Clarion.Runtime.Classes.DLL. 
SoftVelocity.Clarion.Runtime.Procedures.DLL 
SoftVelocity.DataDictionary.Design 
SoftVelocity.ReportPreviewer.DLL 
SoftVelocity.RWClasses.DLL 
 
 
 
Install the Print engine and all other supporting files in a single directory. The Report Library 
and data files can be in the same directory or any other directory. You can also use search 
paths to "point" the library to the location of the data files. 
Optionally, you can set up Program Manager Icons or Shortcuts to run individual reports. 


---

Distribution (of Reports) 
213 
 
 
 
 
Using the Runtime Print Engine 
Legacy and current Clarion ReportWriter Report Library files (.TXR and .REPXL files 
respectfully) are redistributable along with the print engine (C70PRNT.EXE) and its supporting 
DLLs. This allows you to distribute the files needed for end users to print or preview reports. It 
does not allow any modifications to reports. 
To design reports, each user must own a separate copy of Clarion ReportWriter for Windows. 
You can purchase ReportWriter from SoftVelocity for resale to your clients or to include with 
your application as part of a complete solution. This allows your customers to modify your 
reports or create new ones. 
 
 
 
ReportWriter (C70RW.EXE) is not redistributable. Each user must purchase a separate copy. 
See Distributing your Reports for details on deploying Report Libraries and the necessary 
supporting files. 
The print engine (C70PRNTX.exe) is distributable. This lets you create reports and distribute 
Report Libraries (.TXR files) along with the print engine to multiple users. These users will be 
able to run reports, preview them, and print them. However, they will not be able to modify the 
reports. 
You can pass information to the print engine on the command line or through an Initialization 
(.INI) file. This tells the print engine which Report Library to use, which report to execute, plus 
any desired options. 
Print Engine Command Line Parameters 
 
 
C70PRNT [ | ReportLibraryFile | ] [ ReportLabel ] [ optionlist ] 
 
| 
INIFilename 
| ] 
 
 
## C70PRNT
The 32-bit print engine—C70PRNTX.EXE. 
 
ReportLibraryFile 
The full path and filename of the Report Library File (.TXR). 
 
INIFilename 
The Initialization file containing all the information to pass to the print 
engine. 
 
ReportLabel 
The label of the report within the Report Library. If omitted, a simple list 
box displayed with list of available reports. 
 
optionlist 
A list of optional parameters for the print engine. 
 
 
C70PRNT.EXE is a stand-alone executable file. You can install the file on any computer to 
execute reports. You can create Shortcuts to run from the Desktop. 
You can use the print engine in many ways to run reports. By associating .TXR or .REPXLfiles 
with C70PRNT.EXE, you can enable Windows Explorer double-click functionality. For   
example, if C70PRNT.EXE is associated with .TXR files, double-clicking on a Report Library  
file in Explorer opens the Report Library with the print engine and displays a list of reports. This 
also allows drag and drop functionality. By dragging a .TXR file onto a print engine icon or 
shortcut, you can open the report library and display a list of its reports. 


---

ReportWriter 
214 
 
 
 
 
You can also provide optional parameters on the command line or through an Initialization file. 
/Pstring 
The report‘s password. For example: /P"bat123" specifies the 
password is bat123. 
 
/W[n] 
Preview (n pages). If n is omitted, all pages will appear. For example: 
/W specifies to run in Preview mode. Another example: /W4 specifies 
to run in Preview Mode and only show the first four pages. 
 
/Dprinterdef 
The Printer Name (device) as specified in the Windows Print Manager. 
For example /D"HP LaserJet 4/4M PostScript" specifies the HP 
LaserJet printer. 
 
/Rs-e 
The report‘s page range where s is the Start page and e is the End 
page. For example: /R6-10 specifies to print pages 6 through 10 
inclusive. 
 
/Cn 
The number of copies to print is n. For example: /C6 specifies to print 
6 copies of the report. 
 
/D? 
Specifies to display the standard printer dialog allowing users to select 
the target printer and/or the range of pages. 
 
/D?"caption text"    Specifies to display the standard printer dialog allowing users to select 
the target printer and/or the range of pages displaying the caption text 
on the title bar. 
 
/Vvarname=value 
This assigns values to runtime variables. There cannot be spaces on 
either side of the equal sign (=). You can specify more than one 
matched pair on the command line. For example: /Vx=3 or 
/Vproduct="Widgit". 
 
/Iininame 
The Initialization file to use. 
 
 
Examples: 
## C70PRNTX
## C70PRNTX ORDERS.TXR
## C70PRNTX   C:\REPORTS\ORDERS.TXR
C70PRNTX ORDERS.TXR Invoice 
C70PRNTX ORDERS.TXR SalesReport /VCustNumber=23 
C70PRNTX ORDERS.TXR MonthlySalesReport /P"theboss" 
C70PRNTX /Iinvoice.ini 
C70PRNTX /Iinvoice.ini SalesReport /VCustNumber=23 


---

Distribution (of Reports) 
215 
 
 
 
 
Using C70PRNTX with an Initialization File 
The Initialization file is either (in order of priority): 
 
The Initialization file set by the /I command line parameter. 
 
The Initialization file with the same name as the Report Library being printed. 
 
C70PRNTX.INI found by the Windows .INI search path. 
In the Initialization file, there are three sections: [Run], [Variables], and [Paths]. These contain 
values for the command line options. Any values specified on the command line override INI 
file values. 
 
 
INI File Format: 
[Run] 
LIBRARY=libname 
! same as 1st parameter 
REPORT=repname 
! same as 2nd parameter 
PASSWORD=password 
! same as /P 
PREVIEW=n 
! same as /Wn (if omitted all pages are previewed) 
DEVICE=device 
! same as /D 
RANGE=s-e 
! same as /R 
COPIES=n 
! same as /C 
## DEVICE=?
! same as /D? 
DEVICE=?"Caption Text" 
! same as /D?"Caption Text" 
[Variables] 
variablename=value 
! same as /Vvariablename=value 
[Paths] 
mask=dirpath 
 
 
INI File Example: 
[Run] 
## LIBRARY=C:\C70\EXAMPLES\RWTUTOR\RWTUTOR.TXR
REPORT=StudentLabels 
PASSWORD=SoftVelocity 
## PREVIEW=5
## RANGE=6-10
## COPIES=6
DEVICE=?"Specify Target Printer" 
[Variables] 
MajorCode=5 
[Paths] 
## *.TPS=C:\C70\RWTUTOR


---

 
 
 


---

217 
 
 
 
 
 
How To - FAQs 
How To - FAQs 
This section contains some common report tasks that you may need to perform. 
 
 
Adding a Data Source to a Report 
 
 
If you create or add a report to an existing library, you will need to associate the report with a 
data source. 
To do this: 
 
 
Open the Smart Tag dialog of the Report as shown: 
 
 
 
 
The Data Source is empty. Select the drop list to open the dialog shown above. 
Click on the Add New DataSource link. 
 
 
This will open up the Data Source dialog that you see when using the Report Wizard. You can 
now proceed to add a custom data source to your custom report. 


---

218 
ReportWriter 
 
 
 
 
 
Summary 
• When creating relational reports, a little planning in advance can save a lot of time. 
• When you import a Clarion Data Dictionary, ReportWriter imports file relationships defined in 
the dictionary or you can create user-defined relations. 
• Link Fields define the relationship between files. 
• When defining the file schematic for your report, you add related files to the currently 
highlighted file. 
• The Sort Order dialog lets you specify the order in which records print and set group breaks to 
group records together. 
• To exclude "empty" records, use the Exclude Nulls option. 
• The Report Wizard automatically handles the varying length of Memo fields by setting the 
Auto Expand property on the Text control and not setting the Fixed property on the band. 
• Group Footers print after all Detail bands for a group print. 
• Relations allow you to lookup values from a parent file to print on a report. 
• Group Boxes allow you to group controls together. 
• Background colors and Fonts allow you to highlight elements of your report. 
• Control pagination using the Page Before, Page After, With Next, and With Prior 
properties. 


---

219 
How To - FAQs 
 
 
 
 
Adding Images to a Report. 
Adding an image to a report in the Clarion ReportWriter is easy. You can add a static image 
(like your company logo) to your reports using the picture box. For example: 
 
 
 
If your image is static: 
 
 
Press the ellipsis button next to the Image property, and select the image to display. If the 
image is stored on a web page, you can alternately select an Image URL. 
 
 
Image Sizing for a Picture Box control is set as follows: 
 
Normal 
The image is placed in the upper-left corner of the picture box control. The 
image is clipped if it's larger than the picture box control which contains it. 
Stretch 
Image 
The image within the picture box control is stretched or shrunk as appropriate 
to fit the size of the picture box control. 
Auto-Size 
The picture box control's size is adjusted to that of the image it contains. 
Center 
Image 
The image is displayed in the center of the picture box control. If the image is 
larger than the picture box control, the outside edges are clipped. 
Zoom 
Image 
The image is sized proportionally (without clipping), so that it's best fitted to  
the image control. If the height and width ratio of the image control is the same 
as the image's ratio it will be resized to exactly fit into the image control. 
Otherwise the closest fitting side (height or width) of the image will be sized to 
the control and the other side (height or width) of the image sized 
proportionally (leaving empty space). 
 
 
The Anchor Vertically property contains 4 options, and controls how the image will be 
anchored with respect to the report band if resizing of the band is necessary: 
 
None 
A control is not anchored to any edge of the band. 
Top 
A control is anchored to the top edge of the band. 
Bottom 
A control is anchored to the bottom edge of the band. 
Both 
A control is anchored to both the top and bottom edges of the band. 
 
 
If your image is dynamic: 


---

ReportWriter 
220 
 
 
 
 
What if your image is dynamic and stored in a file for each record or row read?   
In this situation, first identify the field or column containing the image information. 
Next, use the Field Box to right-click and drag the image field to your report as shown here: 
 
 
 
 
 
Note: 
You can also use a Rich Text control to display an image. 


---

How To - FAQs 
221 
 
 
 
 
Binding Data to a Report 
The main purpose of the Report Designer is to create and customize data-aware reports. This 
means that a report gets data from an external data source (many types of which are 
supported), to which the report is bound, and the report's controls represent the corresponding 
data fields from that data source. 
To bind a report to data, execute the following steps. 
1. Create a new report. If you use the wizard to create the report, you will be guided to 
select your report‘s data from either a Clarion Dictionary or a Standard Data Source. 
For a detailed description using the wizard, see the Creating and Editing Reports help 
topic. 
In this topic, we will show you how you bind data using a Standard Data Source from a report 
not created using the wizard.. 
2. To bind the report to data, click its Smart Tag. In the invoked actions list, expand the 
Data Source drop-down list and click Add New DataSource. 
 
 
 
 
 
3. A dialog appears allowing you to define a name for the dataset being created. 


---

ReportWriter 
222 
 
 
 
 
 
 
4. On the next page, specify the database to be used. If it is absent in the drop-down 
selector containing existing connections, click New Connection..., to invoke the Data 
Link Properties dialog. 


---

How To - FAQs 
223 
 
 
 
 
 
 
5. In this dialog's Provider tab, choose your data provider. Then, switch to the 
Connection tab, to specify the path to your data source. 


---

ReportWriter 
224 
 
 
 
 
 
 
6. Click Ok, then Next. 
 
 
The next page allows you to select tables to be obtained from the database. 


---

How To - FAQs 
225 
 
 
 
 
 
 
7. Select the required table and click Finish. 
 
 
 
If you choose several tables, the Report Designer creates a data relationship between them (if 
possible), used to create the master-detail reports. 
 
 
After performing the steps above, the report's Data Source, Data Member and Data Adapter 
properties are defined. This means that the report is bound to the data. 


---

ReportWriter 
226 
 
 
 
 
 
 
After binding a report to a dataset, you also need to bind each data-aware report control to a 
data field. Please refer to the Display Values from a Database (Bind Report Elements to Data) 
topic for details. 


---

How To - FAQs 
227 
 
 
 
 
Conditionally Change a Control's Appearance 
 
This tutorial describes the steps to conditionally change a control's appearance. 
Examine the following report created using the Northwind Products table: 
 
 
Select the report by clicking anywhere over the blank area around its bands, and in the 
Property Grid, locate the Formatting Rules Sheet property and click its ellipsis button. The 
invoked Formatting Rule Sheet Editor is intended to manage and customize formatting rules, 
which then can be defined for the report's bands and controls. 
 
In this dialog, create a new formatting rule (by using the button), locate its Condition property 
and, again, click its ellipsis button. 
 
 
 
In the invoked Condition Editor, define the required Boolean condition. In this tutorial, we will 
format fields if the UnitInStock value is less than 10. 


---

ReportWriter 
228 
 
 
 
 
 
 
To save the condition and close the dialog, click OK. 
Next, define the formatting to be applied. 


---

How To - FAQs 
229 
 
 
 
 
 
 
Select the band or control to which the formatting rule must be applied (in this example it is the 
Detail band), and in the Property Grid, locate its Formatting Rules property and click its 
ellipsis button. In the now visible Formatting Rules Editor, move the formatting rule from left 
to right (using the > button), which means that the rule is to be applied. 


---

ReportWriter 
230 
 
 
 
 
 
 
Also, it is possible to customize the precedence of formatting rules, by using the up and down 
arrow buttons at the right of the dialog. So, the rules are applied in the same order that they 
appear in the list, and the last rule in the list has the highest priority. 


---

How To - FAQs 
231 
 
 
 
 
Converting your Legacy Reports 
The Clarion 7 ReportWriter has an easy migration path for your legacy ReportWriter library 
files. These library files (in TXR format) can be easily opened by doing the following: 
From the ReportWriter IDE Menu: 
1. Select File > Open 
2. From the Open dialog, select the TXR type from the Files of Type: 
 
 
 
 
 
The Convert Report Library dialog is displayed: 
 
 
 
 
 
3. Specify the new library name to convert, and then specify an existing dictionary to use, 
or if one is not available, designate the converter to create a new one. 
After any DCT conversion that might be needed, your TXR reports will now be imported into 
the new ReportWriter. 


---

ReportWriter 
232 
 
 
 
 
Copying and Reusing an Existing Report 
Many times, your hard work at designing one particular report will need to be reused in a new 
report. To save time and effort, the report will bee to be copied to a new report name. 
 
 
1. To do this, open and access the Library Explorer. 
2. Right-click on the report to copy, and select the Copy Report option. 
3. Move your mouse to any blank area of the Library Explorer, and right-click again. 
4. From the popup menu, select Paste Report. 


---

How To - FAQs 
233 
 
 
 
 
Changing Connection String of a Data Source 
ReportWriter provides for two ways to connect to your report‘s data; you can use a Clarion 
Dictionary or a Standard Data Source. 
 
Once a Standard Data Source has been created, you may need to change the Connection 
String information on occasion when your reports are distributed. 
 
To do this, access the Report‘s Properties via the Properties Grid. 
 
Access the Data Adapter > SelectCommand > Connection > ConnectionString property, 
as shown below: 
 
 
 


---

ReportWriter 
234 
 
 
 
 
Creating a Newspaper-style Report. 
To create a newspaper style report, there are only two properties in the Detail Band that you 
need to modify. 
 
 
Select the Detail band, and access either the Property Grid or use the Smart Tags as shown 
below: 
 
 
 
 
 
Set the Multi-Column Mode to either Use Column Count or Use Column Width. 
Set the Multi-Column Direction to either Across and Down or Down and Across, which 
determines how the data will; flow in the report. For a newspaper style, select First Down, then 
Across. 
Finally set either the Column Count or the Column Width, based on the Multi-Column Mode 
that you selected. 


---

How To - FAQs 
235 
 
 
 
 
Creating a Runtime Field (adding a report parameter) 
Runtime fields (or report parameters) can be useful to help you filter your data or specify a 
value that will be used to calculate other values (e.g., a calculated field). 
 
 
There are two ways to add parameters to your report: 
 
 
1. In the Report Settings toolbar, click on the Parameters toolbar button: 
 
2. In the Field List you can also right-click over the Parameters section, and click Add 
Parameter the popup menu. Right-click again and select Edit Parameters… to 
display the following dialog: 
 
 
The Parameter Collection Editor is displayed. 
 
 
 
 
 
The following properties are available: 
 
 
Name 
Give your parameter a name that describes its intended use (i.e. StartDate) 
Description 
Enter an optional description that explains its intended use (i.e. Use in Report Filter) 
Parameter Type 
Enter the type of parameter data used. Select from the following: 
String 
Used for alphanumeric entries 
DateTime 
Use for Date or Time entry 
Int32 
Use for a standard integer (whole number) 


---

ReportWriter 
236 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Value 
Float 
Represents a single-precision 32-bit number with values ranging from negative 
3.402823e38 to positive 3.402823e38. 
Double 
Represents a double-precision 64-bit number with values ranging from negative 
1.79769313486232e308 to positive 1.79769313486232e308 
Decimal 
Represents decimal numbers ranging from positive 
79,228,162,514,264,337,593,543,950,335 to negative 
79,228,162,514,264,337,593,543,950,335. 
Boolean 
Used for TRUE/FALSE parameters. 
These data types are using standard .NET data types. 
Enter a default value if needed to initialize the parameter. 
Visible 
Set to Yes to prompt the user when the report runs to enter a value. Set to No if you plan to 
use this parameter behind the scenes without user intervention. 


---

How To - FAQs 
237 
 
 
 
 
Display Values from a Database (Bind Report Elements to Data) 
 
Report elements can either display static information or dynamic data fetched from the bound 
database. Data-bound elements are indicated in the Report Designer using a little database 
icon in the top-right corner. 
 
 
 
Sometimes you may work with a report that is missing some information. For instance, you 
may have an employee list that doesn't display birth dates. If the database contains this 
information, you can easily add it to your report using one of the methods described below. 
 
 
Using the Field List 
 
To bind an existing report element, click the desired field item in the Field List window, and 
then drag and drop it onto the element. The yellow database icon inside the control will then 
appear. 
 
 
 
To add a new data-bound report element, simply drag the desired field item from the Field List 
window onto a report band. This will create a Label bound to the selected data field. 
 
A more flexible way to create data-bound elements is to right-click a Field List item, and then 
drag and drop it onto a report. This will invoke the context menu shown in the image below. 
Simply choose the element type that will represent your data, and it will be automatically 
created and bound to the selected data field. 
 
 


---

ReportWriter 
238 
 
 
 
 
 
Using the Smart Tag 
 
Click an element's Smart Tag, and in the invoked menu, expand the Data Binding drop-down 
list and select the required data field. 
 
 
 
 
Using the Property Grid 
 
Click an element to show it's properties in the Property Grid. Expand the (Data Bindings) 
branch that holds the bindable attributes. Specify a data field for the required attribute (e.g. 
Text). 


---

How To - FAQs 
239 
 
 
 
 
 


---

ReportWriter 
240 
 
 
 
 
 
 
FormatString and Clarion Picture Editor 
Some controls let you specify a picture token that provides a special format for displaying and 
printing variables. 
There is a great variety and diversity of picture token syntax which depends on the type of data 
you format: strings, numbers, currency, scientific, dates, times, etc. 
The Format String dialog lets you quickly and easily build an appropriate picture token without 
memorizing picture token syntax. Invoke this easy to use dialog by pressing the ellipsis (...) 
button beside the Format String prompt. 
 
 
 
 
 
Select the Clarion Picture category, and press the Edit button to open the Edit Picture dialog: 
 
 
Example 
An example of the print or display format currently specified in the dialog. What 
you see is what you get. 
 
Picture 
The picture token currently specified. This picture token produces the example 
above. 
 
Type 
Choose the type of data to format from this drop-down list. Choose from String, 
Numeric and Currency, Scientific Notation, Date, Time, Pattern, and Key-in 
Template. 
 
 
String 
String picture tokens specify a length, with no other formatting. 
 
Length 
Specify the length of the string. This length also determines the width of the control 
if the width is not otherwise specified. 


---

How To - FAQs 
241 
 
 
 
 
Numeric and Currency 
Numeric and currency picture tokens specify a length, plus conventional formatting to convey 
positive and negative values, various currencies, etc. For more information see the Print and 
Display Formatting appendix. 
 
 
Size               The total number of digits, plus any formatting characters. For example, 
$22.25- is 4 digits + 3 formatting characters for a size of 7. 
 
Decima
l Digits 
 
The number of digits to the right of the decimal. 
 
Currency 
Choose from None, Leading, and Trailing. None shows no currency symbol. 
Leading puts the currency symbol to the left of the number and Trailing puts the 
symbol right of the number. 
 
Symbol 
The currency symbol to print or display: either a dollar sign ($) or a string 
constant. 
 
Negative 
Sign 
 
Specify how negative values print. 
 
Bracket 
Negatives surrounded by parentheses. 
Leading 
Negatives get a leading minus sign. 
Trailing 
Negatives get a trailing minus sign. 
None 
No negative sign prints or displays. 
 
Decimal Separator 
Specify the character inserted between the integer and fractional portion of the value. 
 
 
Period 
Period is the separator. 
 
Comma 
Comma is the separator. 
 
None 
No separator prints or displays. 
 
Grouping 
Specify the character inserted at every third digit to aid readability. 
 
Comma 
Comma is the separator. 
Period 
Period is the separator. 
Space 
Space is the separator. 
Hyphen 
Hyphen is the separator. 
 
Leading Character 
Specify the character to represent leading zeros. 
 
 
Clip 
Remove leading zeros so that any leading format characters abut the left most 
digit. 
 
Zero 
Leading zeros print or display as zeros (0). 
Space 
Leading zeros print or display as spaces ( ). 
Asterisk 
Leading zeros print or display as asterisks (*). 
 
Blank when zero 


---

ReportWriter 
242 
 
 
 
 
Check this box to print or display nothing when the value is zero. 
 
 
Scientific 
Scientific Notation picture tokens let you print or display very large or very small numbers with 
a decimal format raised by a power of ten. The print or display format takes the form - 
9.99e+999. For more information see the Print and Display Formatting appendix. 
Number of Characters The total number of characters, including the 7 format characters. For 
example, -1.96e+007 requires 10 characters. 
Leading Digits The number of digits to the left of the decimal point (typically 1). 
 
 
Decimal Separator 
Specify the character inserted at every third digit to aid readability. 
 
 
Period 
Period is the separator. 
Comma 
Comma is the separator. 
Space 
A Space is the separator. 
 
Separator 
Specify the character inserted between the integer and fractional portion of the value. 
Period 
Period is the separator. 
 
Comma 
Comma is the separator. 
 
 
Blank when zero 
Check this box to print or display nothing when the value is zero. 
Date 
Date Notation picture tokens let you print or display dates in a number of different formats. 
Choose the format you want from the Format drop-down list. For more information see the 
Print and Display Formatting appendix. 
Format 
Choose the format you want from the drop-down list. What you see is what you get except for 
the Windows Short and Windows Long formats. Additionally, the separator character and 
leading zeros may be specified independent of the chosen format. 
 
 
Windows Short 
Uses the short date format specified in Windows Control Panel or Regional Settings control 
panel. 
Windows Long 
Uses the long date format specified in Windows Control Panel or Regional Settings control 
panel. 
 
 
Separator 
Choose from Standard (/), Period (.), Dash (-), Space ( ), and Comma (,). 
 
Leading 
Character 
 
Specify the character to represent leading zeros. 
 
Zero 
Leading zeros print or display as zeros (0). 
 
Blank 
Remove leading zeros. 


---

How To - FAQs 
243 
 
 
 
 
Asterisk 
Leading zeros print or display as asterisks (*). 
 
Blank when 
zero 
 
Check this box to print or display nothing when the value is zero. 
 
 
Time 
Time Notation picture tokens let you print or display times in a number of different formats. 
Choose the format you want from the Format drop-down list. For more information see the 
Print and Display Formatting appendix. 
Format 
Choose the format you want from the drop-down list. What you see is what you get except for 
the Windows Short and Windows Long formats. Additionally, the separator character and 
leading zeros may be specified independent of the chosen format. 
 
 
Windows Short 
Uses the time format specified in Windows Control Panel or Regional Settings control panel. 
Windows Long 
Uses the time format specified in Windows Control Panel or Regional Settings control panel. 
 
 
Separator 
Choose from Standard (:), Period (.), Dash (-), Space ( ), and Comma (,). 
 
Leading 
Character 
 
Specify the character to represent leading zeros. 
 
Zero 
Leading zeros print or display as zeros (0). 
 
Blank 
Remove leading zeros. 
 
Blank when 
zero 
 
Check this box to print or display nothing when the value is zero. 
 
Pattern 
Pattern picture tokens let you build custom print or display formats for various numbers: phone 
numbers, social security numbers, room numbers, dates, times, measurements, etc. For more 
information see the Print and Display Formatting appendix. 
 
 
Picture 
Type the picture token between the ‗P‘s according to the Legend below. Your 
picture token can include any displayable characters, including all the standard 
keyboard characters. 
 
At runtime, the constants in the picture token display just as they appear in the token. The left 
angle (<) and the pound sign (#) resolve into the individual digits from the display variable. 
Legend: 
< 
integer, blank if zero 
 
# 
Integer 
 
Constant 
(any displayable char except < and #) 
 
 
Blank when zero 
Check this box to print or display nothing when the value is zero. 


---

ReportWriter 
244 
 
 
 
 
 
If you want to use a lowercase p in your picture, use an uppercase P at the start and end of 
your picture token. If you want to use an uppercase P in your picture, use a lowercase p at the 
start and end of your picture token. 
 
 
 
Key-in Template 
Pattern picture tokens let you build custom edit formats for STRINGs, CSTRINGs and 
PSTRINGs containing mixed alphanumeric characters. Although Key-in tokens affect output as 
well as input, their primary purpose is to provide custom field editing and validation on input 
when using Runtime fields. 
Picture 
Type the picture token between the ‗K‘s according to the Legend below. Your picture token can 
include any characters (displayable or not), including all the standard keyboard characters. 
Legend: 
< 
accept an integer, blank if zero 
 
# 
accept an integer 
 
? 
accept any character (even non-display) 
 
^ 
accept an upper case character 
 
_ 
accept a lower case character 
 
| 
input may stop here 
 
Constant 
(any displayable char except <#?^_| or \) 
 
\ 
display next char (lets you display <#?^_| and \) 
 
 
Only alphabetic characters 
Check this box to accept only alphabetic characters. 
 
 
Blank when zero 
Check this box to print or display nothing when the value is zero. 
 
If you want to use a lowercase k in your picture, use an uppercase K at the start and end of 
your picture token. If you want to use an uppercase K in your picture, use a lowercase k at the 
start and end of your picture token. 
For more information see the Print and Display Formatting appendix. 


---

How To - FAQs 
245 
 
 
 
 
 
 
Lines, Boxes, Circles and Shapes 
Lines, boxes, and ellipses can be used to separate groups or place borders around certain 
items to make them stand out. Good use of these controls improves the report‘s readability. 
To place a Line on a Report: 
1. Drag the Line control from the Toolbox, and drop on the report at the location where you 
want the line to appear. 
2. Adjust the line length by dragging the handles, as needed. 
 
 
To place a Box or Ellipses on a Report: 
1. Drag the Shape control from the Toolbox, and drop on the report at the location where you 
want the line to appear. 
2. Modify the Shape property to select the type of Shape that you want. 
There are currently 23 Shape types available. 
Arrow - Left,Right,Top,Bottom 
Brace 
Bracket 
Cross 
Ellipse 
Hexagon 
Line - Vertical, Horizontal, Slant, BackSlant 
Octagon 
Pentagon 
Polygon 
Rectangle 
Star - 3, 4, 5, 6, and 8 point 
Triangle 
 
3. Adjust the shape size by dragging the handles as needed. 


---

ReportWriter 
246 
 
 
 
 
Placing Text on a Report 
Constant or literal text can be used as report titles, page headers or footers, column headings, 
group headers, or report final page footers. Text can be placed on a report by using either the 
Label or the Rich Text Control. 
 
 
Suppressing a line from printing when empty 
On occasion, you may have a field with null values, and you wish to suppress that line from 
printing on a report. 
1. RIGHT-CLICK on the target field, then choose Properties. 
Select the Process Null Values property, and change to Suppress and Shrink. This specifies 
that the field will not print if its value is zero or null. 
This property allows you to skip fields and print to a static height area; in other words, it lets 
you print professional looking labels. 


---

247 
 
 
 
 
 
Shipping Examples 
Shipping Examples 
The Clarion ReportWriter organizes the shipping examples and lessons into 5 distinct sub- 
folders. This section describes the contents therein. 
 
 
All of the shipping ReportWriter examples use the following folder hierarchy: 
 
 
 
 
 
REPXL Reports 
This folder contains all new examples and lessons that use the REPXL report libraries. 
 
 
Examples 
 
 
The following examples are available: 
 
 
ABCReps 
Three reports that demonstrates created and using a calculated field, attaching 
an image to a report, and working with an RTF (Rich Text Format) control. 
 
ExtFunc 
Demonstrates using an external library function and then applying it to a 
calculated field and using it in a report. 
 
Invoice Demonstrates simple reports, mailing label reports, a Customer List that uses 
calculated fields, a multi-file relational invoice report, and a multi-file relational 
invoice report using a filter. 
 
Products 
A single report that demonstrates the use of scripting to read an image file name 
stored in a STRING field and display it in a picture box. 
 
 
IntegratingREPXL 
This folder contains a single application solution that demonstrates how to use the 
ReportEngine in Clarion programs. 
 
 
## RWTUTOR
Contains all of the lessons that are included in this document. 
 
 
TXR Reports 
This folder contains examples and lessons that use the TXR report library format. 
 
 
IntegratingTXR 
Contains a set of hand coded projects that demonstrate how to use and manipulate the 
ReportWriter library engine with TXR report libraries. 


---

248 
ReportWriter 
 
 
 
 
 
The shipping Clarion 7 Invoice example demonstrates the use of the ReportWriter library 
engine with TXR files from an application. See the core help examples for more information. 
 
 
RWTutor 
This folder contains the old set of example TXR files that were used in the Clarion 6 
ReportWriter. 


---

249 
 
 
Shipping Examples 
 
 
Shipping Examples 
The Clarion ReportWriter organizes the shipping examples and lessons into 5 distinct sub- 
folders. This section describes the contents therein. 
 
 
All of the shipping ReportWriter examples use the following folder hierarchy: 
 
 
 
 
 
REPXL Reports 
This folder contains all new examples and lessons that use the REPXL report libraries. 
 
 
Examples 
 
 
The following examples are available: 
 
 
ABCReps 
Three reports that demonstrates created and using a calculated field, attaching 
an image to a report, and working with an RTF (Rich Text Format) control. 
 
ExtFunc 
Demonstrates using an external library function and then applying it to a 
calculated field and using it in a report. 
 
Invoice Demonstrates simple reports, mailing label reports, a Customer List that uses 
calculated fields, a multi-file relational invoice report, and a multi-file relational 
invoice report using a filter. 
 
Products 
A single report that demonstrates the use of scripting to read an image file name 
stored in a STRING field and display it in a picture box. 
 
 
IntegratingREPXL 
This folder contains a single application solution that demonstrates how to use the 
ReportEngine in Clarion programs. 
 
 
## RWTUTOR
Contains all of the lessons that are included in this document. 
 
 
TXR Reports 
This folder contains examples and lessons that use the TXR report library format. 
 
 
IntegratingTXR 
Contains a set of hand coded projects that demonstrate how to use and manipulate the 
ReportWriter library engine with TXR report libraries. 


---

ReportWriter 
250 
 
 
The shipping Clarion 7 Invoice example demonstrates the use of the ReportWriter library 
engine with TXR files from an application. See the core help examples for more information. 
 
 
RWTutor 
This folder contains the old set of example TXR files that were used in the Clarion 6 
ReportWriter. 


---

251 
 
 
APPENDIX A - Print and Display Formatting 
 
Picture Tokens 
ReportWriter uses picture tokens to provide a masking format for printing and displaying 
variables. Picture tokens define the way a field prints on a report. 
There are seven types of picture tokens: 
Numeric and currency 
Scientific notation 
Date 
Time 
Pattern 
Key-in template 
String 
 
 
Key-in Template picture tokens are used for data entry only, so they only apply to Runtime 
Fields. 


---

ReportWriter 
252 
 
 
 
 
Numeric and Currency Pictures 
@N [currency] [sign] [fill] size [grouping] [places] [sign] [currency] [B] 
 
@N 
All numeric and currency pictures begin with @N. 
currency 
Either a dollar sign ($) or a string constant enclosed in tildes (~). When it 
precedes the sign indicator and there is no fill indicator, the currency symbol 
"floats" to the left of the high order digit. If there is a fill indicator, the currency 
symbol remains fixed in the left-most position. If the currency indicator follows 
the size and grouping, it appears at the end of the number displayed. 
sign 
Specifies the display format for negative numbers. If a hyphen precedes the fill 
and size indicators, negative numbers will display with a leading minus sign. If a 
hyphen follows the size, grouping, places, and currency indicators, negative 
numbers will display with a trailing minus sign. If parentheses are placed in both 
positions, negative numbers will be displayed enclosed in parentheses. 
fill 
Specifies leading zeros, spaces, or asterisks (*) in any leading zero positions 
and suppresses grouping. If the fill indicator is omitted, leading zeros are 
suppressed and grouping is enabled. 
0 (zero) produces leading zeroes 
_ (underscore) produces leading spaces 
* (asterisk) produces leading asterisks 
size 
The size is required to specify the total number of significant digits to display, 
including the number of digits in the places indicator and any formatting 
characters. 
grouping 
A grouping symbol, other than a comma (the default), can be placed to the right 
of the size indicator to specify a three digit group separator. 
. (period) produces periods 
- (hyphen) produces hyphens 
_ (underscore) produces spaces 
places 
Specifies the decimal separator symbol and the number of decimal digits. The 
number of decimal digits must be less than the size indicator. The decimal 
separator may be a period (.), grave accent (‗), or the letter "v" (used only for 
STRING field storage declarations—not for display). 
. (period) produces a period 
‗ (grave accent) produces a comma 
v produces no decimal separator 
B 
Specifies that the format displays as blank whenever its value is zero. This may 
be upper or lower case (B or b). 
The numeric and currency pictures format numeric values for screen display or in reports. If 
the value is greater than the maximum value the picture can display, a string of asterisks is 
displayed. 


---

APPENDIX A - Print and Display Formatting 
253 
 
 
 
 
Examples: 
 
Numeric 
Result 
Format 
@N9 
4550000 
Nine digits, group with commas (default) 
## @N_9B
4550000 
Nine digits, no grouping, leading blanks if zero 
## @N09
4550000 
Nine digits, leading zero 
## @N*9
***45,000 
Nine digits, asterisk fill, group with commas 
## @N9_
4 550 000 
Nine digits, group with spaces 
## @N9.
4.550.000 
Nine digits, group with periods 
 
Decimal 
Result 
Format 
## @N9.2
4550.75 
Two decimal places, period decimal separator 
## @N_9.2B
4550.75 
Two decimal places, period decimal separator, no grouping, blank 
if zero 
## @N_9‗2
4550,75 
Two decimal places, comma decimal separator 
## @N9.‗2
4.550,75 
Comma decimal separator, group with periods 
## @N9_‗2
4 550,75 
Comma decimal separator, group with spaces 
 
Signed 
Result 
Format 
## @N-9.2B
-2347.25 
Leading minus sign, blank if zero 
## @N9.2-
-2347.25 
Trailing minus sign 
## @N(10.2)
-2347.25 
Enclosed in parens when negative 
 
Dollar 
Result 
Format 
## @N$9.2B
$2,347.25 
Leading dollar sign, blank if zero 
## @N$10.2-
-$2,347.25 
Leading dollar sign, trailing minus when negative 
## @N$(11.2)
$(2,347.25) 
Leading dollar sign, in parens when negative 
 
Currency 
Result 
Format 
## @N12_‗2~ F~
## 1 5430,50 F
France 
## @N~L. ~12‗
## L. 1.430.050
Italy 
## @N~£~12.2
£1,240.50 
United Kingdom 
@N~kr~12‗2 
kr1.430,50 
Norway 
## @N~DM~12‗2
## DM1.430,50
Germany 
## @N12_‗2~
mk~ 
1 430,50 mk 
Finland 
@N12‗2~ kr~ 
1.430,50 kr 
Sweden 


---

ReportWriter 
254 
 
 
 
 
Scientific Notation Pictures 
 
 
@Em.n[B] 
 
@E 
All scientific notation pictures begin with @E. 
m 
Determines the total number of characters in the format provided by the picture. 
n 
Indicates the number of digits that appear to the left of the decimal point. 
B 
Specifies that the format displays as blank when the value is zero. 
 
The scientific notation picture formats very large or very small numbers. The format is a 
decimal number raised by a power of ten. 
 
 
Examples: 
 
Picture 
Value 
Result 
## @E9.0
1,967,865 
.20e+007 
## @E12.1
1,967,865 
1.9679e+006 
## @E12.1B
0 
## @E12.1
-1,967,865 
-1.9679e+006 
## @E12.1
.000000032 
3.2000e-008 


---

APPENDIX A - Print and Display Formatting 
255 
 
 
 
 
 
 
Date Pictures 
 
 
@Dn [s] [B] [direction [range] ] 
 
@D 
All date pictures begin with @D. 
n 
Determines the date picture format. Date picture formats range from 1 through 18. 
A leading zero (0) indicates a zero-filled day or month. 
s 
A separation character between the month, day, and year components. If omitted, 
the slash ( / ) appears. 
. (period) Produces periods 
‗ (grave accent) Produces commas 
- (hyphen) Produces hyphens 
_ (underscore) Produces spaces 
B 
Specifies that the format displays as blank when the value is zero. 
direction 
A right or left angle bracket (> or <) that specifies the "Intellidate" direction (> 
indicates future, < indicates past) for the range parameter. Valid only on date 
pictures with two-digit years. 
range 
An integer constant in the range of zero (0) to ninety-nine (99) that specifies the 
"Intellidate" century for the direction parameter. Valid only on date pictures with 
two-digit years. If omitted, the default value is 80. 
 
Dates may be stored in numeric variables (usually LONG), a DATE field (for Btrieve 
compatibility), or in a STRING declared with a date picture. A date stored in a numeric variable 
is called a "Clarion Standard Date." The stored value is the number of days since December 
28, 1800. The date picture token converts the value into one of the date formats. 
The century for dates in any picture with a two-digit year is resolved using "Intellidate" logic. 
Date pictures that do not specify direction and range parameters assume the date falls in the 
range of the next 20 or previous 80 years. The direction and range parameters allow you to 
change this default. The direction parameter specifies whether the range specifies the future or 
past value. The opposite direction then receives the opposite value (100-range) so that any 
two-digit year results in the correct century. 
For example, the picture @D1>60 specifies using the appropriate century for each year 60 
years in the future and 40 years in the past. If the current year is 1996, when the user enters 
"5/01/40," the date is in the year 2040, and when the user enters "5/01/60," the date is in the 
year 1960. 
 
 
Example: 
 
Picture 
Format 
Result 
@D1 
mm/dd/yy 
10/31/59 
## @D1>40
mm/dd/yy 
10/31/59 !This defaults to 1959 
## @D01
mm/dd/yy 
01/01/95 
@D2 
mm/dd/yyyy 
10/31/1959 
@D3 
mmm dd, yyyy 
## OCT 31,1959
@D4 
mmmmmmmmm dd, yyyy 
October 31, 1959 


---

ReportWriter 
256 
 
 
 
 
@D5 
dd/mm/yy 
31/10/59 
@D6 
dd/mm/yyyy 
31/10/1959 
@D7 
dd mmm yy 
## 31 OCT 59
@D8 
dd mmm yyyy 
## 31 OCT 1959
@D9 
yy/mm/dd 
59/10/31 
## @D10
yyyy/mm/dd 
1959/10/31 
## @D11
yymmdd 
## @D12
yyyymmdd 
19591031 
## @D13
mm/yy 
10/59 
## @D14
mm/yyyy 
10/1959 
## @D15
yy/mm 
59/10 
## @D16
yyyy/mm 
1959/10 
## @D17
Windows Control Panel setting for 
Short Date 
## @D18
Windows Control Panel setting for 
Long Date 
 
Alternate separators 
 
## @D1.
mm.dd.yy 
Period separator 
## @D2-
mm-dd- 
yyyy 
Dash separator 
## @D5_
dd mm yy 
Underscore produces space separator 
## @D6‗
dd,mm,yyyy 
Grave accent produces comma separator 


---

APPENDIX A - Print and Display Formatting 
257 
 
 
 
 
Time Pictures 
 
 
@Tn[s][B] 
 
@T 
All time pictures begin with @T. 
n 
Determines the time picture format. Time picture formats range from 1 through 6. 
s 
A separation character. Colon ( : ) characters appear between the hour, minute, and 
second components of certain time picture formats. The following s indicators provide 
an alternate separation character for these formats. 
. 
(period) produces periods 
‘ 
(grave accent) produces commas 
- 
(hyphen) produces hyphens 
_ 
(underscore) produces spaces 
? 
(question mark) internationalized time 
B 
Specifies that the format displays as blank when the value is zero. 
 
Times may be stored in a numeric variable (usually a LONG), a TIME field (for Btrieve 
compatibility), or in a STRING declared with a time picture. A time stored in a numeric variable 
is called a "Standard Time." The stored value is the number of hundredths of a second since 
midnight. The picture token converts the value to one of the six time formats. 
Time pictures using the ? separation character produces a time with the separation characters 
specified by DOS‘ Country.SYS file, based upon the country code. 
Time pictures containing alphabetic characters (@T3, @T6) may not be used for data entry. 
 
 
Example: 
 
Picture 
Format 
Result 
@T1 
hh:mm 
17:30 
@T2 
hhmm 
1730 
@T3 
hh:mmXM 
## 5:30PM
@T4 
hh:mm:ss 
17:30:00 
@T5 
hhmmss 
173000 
@T6 
hh:mm:ssXM 
## 5:30:00PM
@T7 
Windows Control Panel setting for short time 
@T8 
Windows Control Panel setting for long time 
 
Alternate separators: 
 
## @T1.
hh.mm 
Period separator 
## @T1-
hh-mm 
Dash separator 


---

ReportWriter 
258 
 
 
 
 
## @T3_
hh mmXM 
Underscore produces space separator 
## @T4‗
hh,mm,ss 
Grave accent produces comma separator 


---

APPENDIX A - Print and Display Formatting 
259 
 
 
 
 
Pattern Pictures 
 
 
@P[<][#][x]P[B] 
 
@P 
All pattern pictures begin with the @P delimiter and end with the P delimiter. The case 
of the delimiters must be the same. 
< 
Specifies an integer position that is blank when zero. 
# 
Specifies an integer position. 
x 
Represents optional display characters. These characters appear in the final result 
string. 
P 
All pattern pictures must end with P. If a lower case @p delimiter is used, the ending 
P delimiter must also be lower case. 
B 
Specifies that the format displays as blank when the value is zero. 
 
Pattern pictures contain optional integer positions and optional edit characters. Any character 
other than < or # is considered an edit character which will appear in the formatted picture 
string. The @P and P delimiters are case sensitive. Therefore, an upper case "P" can be 
included as an edit character if the delimiters are both lower case "p" and vice versa. 
Pattern pictures do not recognize decimal points in order to permit the period to be used as an 
edit character. Therefore, the value formatted by a pattern picture should be an integer. If a 
floating point value is formatted by a pattern picture, only the integer portion of the number will 
appear in the result. 
 
 
Example: 
 
Picture 
Value Entered 
Result 
## @P###-##-####P
215846377 
215-84-6377 
## @P<#/##/##P
103159 
10/31/59 
## @P(###)###-####P
3057854555 
(305)785-4555 
## @P###/###-####P
7854555 
000/785-4555 
@p<#:##PMp 
530 
## 5:30PM
## @P<#‘ <#"P
506 
5' 6" 
@P<#lb. <#oz.P 
902 
9lb. 2oz. 
## @P4##A-#P
112 
## 411A-2
## @PA##.C#P
312.45 
## A31.C2


---

ReportWriter 
260 
 
 
 
 
 
 
Key-in Template Pictures 
 
 
@K[@] [#] [<] [x] [\] [?] [^] [_] [|]K[B] 
 
@K 
All key-in template pictures begin with the @K delimiter and end with the K delimiter. 
The case of the delimiters must be the same. 
@ 
Specifies only uppercase and lowercase alphabetic characters. 
# 
Specifies an integer 0 through 9. 
< 
Specifies an integer that is blank for high order zeros. 
x 
Represents optional constant display characters (any displayable character). These 
characters appear in the final result string. 
\ 
Indicates the following character is a display character. This allows you to include any 
of the picture formatting characters (@,#,<,\,?,^,_,|) within the string as a display 
character. 
? 
Specifies any character may be placed in this position. 
^ 
Specifies only uppercase alphabetic characters in this position. 
_ 
Specifies only lowercase alphabetic characters in this position. 
| 
Allows the operator to "stop here" if there are no more characters to input. Only the 
data entered and any display characters up to that point will be in the string result. 
K 
All key-in template pictures must end with K. If a lower case @k delimiter is used, the 
ending K delimiter must also be lower case. 
B 
Specifies that the format displays as blank when the value is zero. 
 
Key-in pictures may contain integer positions ( # < ), alphabet character positions ( @ ^ _ ), 
any character positions ( ? ), and display characters. Any character other than a formatting 
indicator is considered a display character, which appears in the formatted picture string. The 
@K and K delimiters are case sensitive. Therefore, an upper case "K" may be included as a 
display character if the delimiters are both lower case "k" and vice versa. 
Key-in pictures are used specifically with STRING, PSTRING, and CSTRING fields to allow 
custom field editing control and validation. Using a key-in picture containing any of the 
alphabet indicators ( @ ^ _ ) on a numeric entry field produces unpredictable results. 
Using the Insert typing mode for a key-in picture could produce unpredictable results. 
Therefore, key-in pictures always receive data entry in Overwrite mode, even if the INS 
attribute is present. 
 
 
Example: 
 
Picture 
Value Entered 
Result String 
## @K###-##-####K
215846377 
215-84-6377 
## @K#####|-####K
33064 
33064 
## @K#####|-####K
330643597 
33064-3597 
## @K<# ^^^ ##K
## 10AUG59
## 10 AUG 59


---

APPENDIX A - Print and Display Formatting 
261 
 
 
 
 
## @K(###)@@@-##\@##K
305abc4555 
(305)abc-45@55 
## @K###/?##-####K
7854555 
000/785-4555 
@k<#:##^Mk 
## 530P
## 5:30PM
## @K<#‘ <#"K
506 
5' 6" 
## @K4#_#A-#K
1g12 
41g1A-2 


---

ReportWriter 
262 
 
 
 
 
String Pictures 
 
 
@Slength 
 
 
@S 
All string pictures begin with @S. 
length 
Determines the number of characters in the picture format. 
 
A string picture describes an unformatted string of a specific length. 
 
 
Example: 
 
 
Name STRING(@S20) !A 20 character string field 


---

263 
 
 
APPENDIX B - Clarion Functions 
 
 
Bit Manipulation Functions 
Date and Time Functions 
DOS Functions 
File Based Function 
Mathematical Functions 
Trigonometric Functions 
String Functions 
 
 
Bit Manipulation Functions 
BAND (return bitwise AND) 
BAND(value,mask) 
 
 
## BAND
Performs bitwise AND operation. 
 
value 
A numeric constant, variable, or expression for the bit value to be compared to the 
bit mask. The value is converted to a LONG data type prior to the operation, if 
necessary. 
 
mask 
A numeric constant, variable, or expression for the bit mask. The mask is 
converted to a LONG data type prior to the operation, if necessary. 
 
 
The BAND function compares the value to the mask, performing a Boolean AND operation on 
each bit. The return value is a LONG integer with a one (1) in the bit positions where the value 
and the mask both contain one (1), and zeroes in all other bit positions. 
BAND is usually used to determine whether an individual bit, or multiple bits, are on (1) or off 
(0) within a variable. 
 
 
Return Data Type: 
## LONG
 
 
Example: 
BAND(0110b,0010b) ! returns 0010b 0110b = 6, 0010b = 2 
 
 
 


---

264 
ReportWriter 
 
 
 
 
BOR (return bitwise OR) 
 
 
BOR(value,mask) 
 
 
BOR 
Performs bitwise OR operation. 
 
value 
A numeric constant, variable, or expression for the bit value to be compared to the 
bit mask. The value is converted to a LONG data type prior to the operation, if 
necessary. 
 
mask 
A numeric constant, variable, or expression for the bit mask. The mask is 
converted to a LONG data type prior to the operation, if necessary. 
 
 
The BOR function compares the value to the mask, performing a Boolean OR operation on 
each bit. The return value is a LONG integer with a one (1) in the bit positions where the value, 
or the mask, or both, contain a one (1), and zeroes in all other bit positions. 
BOR is usually used to unconditionally turn on (set to one), an individual bit, or multiple bits, 
within a variable. 
 
 
Return Data Type: 
## LONG
 
 
Example: 
BOR(0110b,0010b) ! returns 0110b 0110b = 6, 0010b = 2 
 
 
 
 
BXOR (return bitwise exclusive OR) 
 
 
BXOR(value,mask) 
 
 
## BXOR
Performs bitwise exclusive OR operation. 
 
value 
A numeric constant, variable, or expression for the bit value to be compared to the 
bit mask. The value is converted to a LONG data type prior to the operation, if 
necessary. 
 
mask 
A numeric constant, variable, or expression for the bit mask. The mask is 
converted to a LONG data type prior to the operation, if necessary. 
 
 
The BXOR function compares the value to the mask, performing a Boolean XOR operation on 
each bit. The return value is a LONG integer with a one (1) in the bit positions where either the 
value or the mask contain a one (1), but not both. Zeroes are returned in all bit positions where 
the bits in the value and mask are alike. 
BXOR is usually used to toggle on (1) or off (0) an individual bit, or multiple bits, within a 
variable. 
 
 
Return Data Type: 
## LONG
 
 
Example: 
BXOR(0110b,0010b) 
! returns 0100b, 0110b = 6, 0100b = 4, 0010b = 2 


---

265 
APPENDIX B - Clarion Functions 
 
 
 
BSHIFT (return shifted bits) 
 
 
BSHIFT(value,count) 
 
 
## BSHIFT
Performs the bit shift operation. 
 
value 
A numeric constant, variable, or expression. The value is converted to a LONG 
data type prior to the operation, if necessary. 
 
count 
A numeric constant, variable, or expression for the number of bit positions to be 
shifted. If count is positive, value is shifted left. If count is negative, value is 
shifted right. 
 
 
The BSHIFT function shifts a bit value by a bit count. The bit value may be shifted left (toward 
the high order), or right (toward the low order). Zero bits are supplied to fill vacated bit 
positions when shifting. 
 
 
Return Data Type: 
## LONG
 
 
Example: 
BSHIFT(0110b,1) 
! returns 1100b 
BSHIFT(0110b,-1) ! returns 0011b 


---

266 
ReportWriter 
 
 
 
 
 
 
Date / Time Procedures and Functions 
 
 
Standard Date 
A Clarion standard date is the number of days that have elapsed since December 28, 1800. 
The range of accessible dates is from January 1, 1801 (standard date 4) to December 31, 
9999 (standard date 2,994,626). Date functions will not return correct values outside the limits 
of this range. The standard date calendar also adjusts for each leap year within the range of 
accessible dates. Dividing a standard date by modulo 7 gives you the day of the week: zero = 
Sunday, one = Monday, etc. 
 
 
Standard Time 
A Clarion standard time is the number of hundredths of a second that have elapsed since 
midnight, plus one (1). The valid range is from 1 (defined as midnight) to 8,640,000 (defined as 
11:59:59:99). A standard time of one is exactly equal to midnight (which allows a zero value to 
be used to detect no time entered). Although time is expressed to the nearest hundredth of a 
second, the system clock is only updated 18.2 times a second (approximately every 5.5 
hundredths of a second). 
 
 
 
 
TODAY (return system date) 
 
 
## TODAY( )
 
 
The TODAY function returns the DOS system date as a standard date. The range of possible 
dates is from January 1, 1801 (standard date 4) to December 31, 2099 (standard date 
109,211). 
 
 
Return Data Type: 
## LONG
 
 
Example: 
## TODAY() + 1
!Today‘s date plus one (tomorrow) 
 
 
 
 
CLOCK (return system time) 
 
 
## CLOCK( )
 
 
The CLOCK function returns the time of day from the operating system time in standard time 
(expressed as hundredths of a second since midnight). Although the time is expressed to the 
nearest hundredth of a second, the system clock is only updated 18.2 times a second 
(approximately every 5.5 hundredths of a second). 
 
 
Return Data Type: 
## LONG
 
 
Example: 
## CLOCK()
! The system time 


---

267 
APPENDIX B - Clarion Functions 
 
 
 
DATE (return standard date) 
 
 
DATE(month,day,year) 
 
 
## DATE
Return standard date. 
 
month 
A numeric constant, variable, or expression for the month. 
 
day 
A numeric constant, variable, or expression for the day of the month. 
 
year 
A numeric constant, variable or expression for the year. The valid range for a year 
value is 00 through 99 (which assumes the range 1900 - 1999), or 1801 through 
2099. 
 
 
The DATE function returns a standard date for a given month, day, and year. The month and 
day parameters allow out-of-range values. A month value of 13 is interpreted as January of the 
next year. A day value of 32 in January is interpreted as the first of February. Consequently, 
DATE(12,32,87), DATE(13,1,87), and DATE(1,1,88) all produce the same result. 
 
 
Return Data Type: 
## LONG
 
 
Example: 
DATE(Hir:Month,Hir:Day,Hir:Year) !Compute hire date 
 
 
See Also: 
Standard Date 
 
 
 
 
DAY (return day of month) 
 
 
DAY(date) 
 
 
DAY 
Returns day of month. 
 
date 
A numeric constant, variable, expression, or the label of a STRING, CSTRING, or 
PSTRING variable declared with a date picture token. The date must be a 
standard date. A variable declared with a date picture token is automatically 
converted to a standard date intermediate value. 
 
 
The DAY function computes the day of the month (1 to 31) for a given standard date. 
 
 
Return Data Type: 
## LONG
 
 
Example: 
## DAY(TODAY())
!Get the day from today‘s date 
## DAY(TODAY()+2)
!Calculate the return day 
 
See Also: 
Standard Date 


---

268 
ReportWriter 
 
 
 
 
 
 
 
MONTH (return month of date) 
 
 
MONTH(date) 
 
 
## MONTH
Returns month in year. 
 
date 
A numeric constant, variable, expression, or the label of a STRING, CSTRING, or 
PSTRING variable declared with a date picture token. The date must be a 
standard date. A variable declared with a date picture token is automatically 
converted to a standard date intermediate value. 
 
 
The MONTH function returns the month of the year (1 to 12) for a given standard date. 
 
 
Return Data Type: 
## LONG
 
 
Example: 
MONTH(DueDate) 
! The month from the date 
 
 
See Also: 
Standard Date 
 
 
 
 
YEAR (return year of date) 
 
 
YEAR(date) 
 
 
## YEAR
Returns the year. 
 
date 
A numeric constant, variable, expression, or the label of a string variable declared 
with a date picture, containing a standard date. A variable declared with a date 
picture is automatically converted to a standard date intermediate value. 
 
 
The YEAR function returns a four digit number for the year of a standard date (1801 to 2099). 
 
 
Return Data Type: 
## LONG
 
 
Example: 
YEAR(LastOrd) < YEAR(TODAY()) ! Last order date not from this year 
 
 
See Also: 
Standard Date 
 
 
 


---

269 
APPENDIX B - Clarion Functions 
 
 
 
 
AGE (return age from base date) 
 
 
AGE(birthdate [,base date]) 
 
 
AGE 
Returns elapsed time. 
 
birthdate 
A numeric expression for a standard date. 
 
base 
date 
 
A numeric expression for a standard date. If this parameter is omitted, the system 
date from DOS is used for the computation. 
 
The AGE function returns a string containing the time elapsed between two dates. The age 
return string is in the following format: 
 
1 to 60 days 
- ‗nn DAYS‘ 
61 days to 24 
months 
2 years to 999 
years 
 
- ‗nn MOS‘ 
 
- ‗nnn YRS‘ 
 
Return Data Type: 
## STRING
 
 
Example: 
Emp:Name & ‗is ‗ & AGE(Emp:DOB,TODAY()) & ‗ old today.‘ 


---

ReportWriter 
270 
 
 
 
 
DOS Procedures and Functions 
PATH (return current DOS directory) 
## PATH( )
 
 
The PATH function returns a string containing the current drive and directory. 
 
 
Return Data Type: 
## STRING


---

APPENDIX B - Clarion Functions 
271 
 
 
 
 
File Functions 
EMPTY(evaluate record value) 
EMPTY(‗filelabel‘) 
 
 
## EMPTY
Returns TRUE if a record exists. 
 
filelabel 
The label of the file to evaluate. 
 
 
The EMPTY function checks for the existence of a record at the detail level. If the filelabel 
contains a record when the detail prints, the result will be TRUE. The function returns a BYTE 
containing zero (FALSE) or one (TRUE). 
This function is useful to provide a condition for a second detail band which you want to print 
only when no records exist for that level. For example, you want to print a band with "No 
orders for this customer" when a customer has no orders. 
 
 
Return Data Type: 
## BYTE
 
 
Example: 
IF Condition: 
EMPTY(‗Orders‘) ! Are there more Order records at this point? 


---

ReportWriter 
272 
 
 
 
 
 
 
Mathematical Functions 
ABS (return absolute value) 
ABS(expression) 
 
ABS 
Returns absolute value. 
expression 
A constant, variable, or expression. 
 
The ABS function returns the absolute value of an expression. The absolute value of a number 
is always positive (or zero). 
 
 
Return Data Type: REAL or DECIMAL 
 
 
Example: 
ABS(A - B) ! Absolute value of the difference 
 
 
 
 
INRANGE (check number within range) 
 
 
INRANGE(expression,low,high) 
 
## INRANGE
Return number in valid range. 
expression 
A numeric constant, variable, or expression. 
low 
A numeric constant, variable, or expression of the lower boundary of the 
range. 
high 
A numeric constant, variable, or expression of the upper boundary of the 
range. 
 
The INRANGE function compares a numeric expression to an inclusive range of numbers. If 
the value of the expression is within the range, the function returns the value 1 for "true." If the 
expression is greater than the high parameter, or less than the low parameter, the function 
returns a zero for "false." 
 
 
Return Data Type: 
## LONG
 
 
Example: 
 
 
If Formula: 
INRANGE(Date % 7,1,5) ! Is this a weekday? 
 
 
 


---

APPENDIX B - Clarion Functions 
273 
 
 
 
 
INT (truncate fraction) 
 
 
INT(expression) 
 
INT 
Return integer. 
expression 
A numeric constant, variable, or expression. 
 
The INT function returns the integer portion of a numeric expression. No rounding is 
performed, and the sign remains unchanged. 
 
 
Return Data Type: 
REAL or DECIMAL 
 
 
Example: 
## INT(8.5)
! returns 8 
## INT(-5.9)
! returns -5 
 
 
 
 
LOGE (return natural logarithm) 
 
 
LOGE(expression) 
 
## LOGE
Returns the natural logarithm. 
expression 
A numeric constant, variable, or expression. If the value of the expression is 
less than zero, the return value is zero. The natural logarithm is undefined for 
values less than zero. 
 
The LOGE (pronounced "log-e") function returns the natural logarithm of a numeric 
expression. The natural logarithm of a value is the power to which e must be raised to equal 
that value. The value of e is 2.71828182846. 
 
 
Return Data Type: 
## REAL
 
 
Example: 
## LOGE(2.71828182846)
! returns 1 
 
## LOGE(1)
! returns 0 
 
LOGE(Val) 
! Get the natural log of Val 
 
 
 


---

ReportWriter 
274 
 
 
 
 
LOG10 (return base 10 logarithm) 
 
 
LOG10(expression) 
 
## LOG10
Returns base 10 logarithm. 
expression 
A numeric constant, variable, or expression. If the value of the expression is 
zero or less, the return value will be zero. The base 10 logarithm is undefined 
for values less than or equal to zero. 
 
The LOG10 (pronounced "log ten") function returns the base 10 logarithm of a numeric 
expression. The base 10 logarithm of a value is the power to which 10 must be raised to equal 
that value. 
 
 
Return Data Type: 
## REAL
 
 
Example: 
 
 
## LOG10(10)
! returns 1 
 
## LOG10(1)
! returns 0 
 
LOG10(Var) 
! The base ten logarithm of a variable named Var 
 
 
 
 
RANDOM (return random number) 
 
 
RANDOM(low,high) 
 
## RANDOM
Returns random integer. 
low 
A numeric constant, variable, or expression for the lower boundary of the range. 
high 
A numeric constant, variable, or expression for the upper boundary of the range. 
 
The RANDOM function returns a random integer between the low and high parameter values, 
inclusively. The low and high parameters may be any numeric expression, but only their 
integer portion is used for the inclusive range. 
 
 
Return Data Type: 
## LONG
 
 
Example: 
 
 
## RANDOM(1,49)
!Pick number between 1 and 49 for Lotto 
 
 
 


---

APPENDIX B - Clarion Functions 
275 
 
 
 
 
ROUND (return rounded number) 
 
 
ROUND(expression,order) 
 
## ROUND
Returns rounded value. 
expression 
A numeric constant, variable, or expression. 
order 
A numeric expression with a value equal to a power of ten, such as 1, 10, 100, 
0.1, 0.001, etc. If the value is not an even power of ten, the next lowest power 
is used; 0.55 will use 0.1 and 155 will use 100. 
 
The ROUND function returns the value of an expression rounded to a power of ten. If the order 
is a LONG or DECIMAL Base Type, then rounding is performed as a BCD operation. Note that 
if you want to round a real number larger than 1e30, you should use ROUND(num,1.0e0), and 
not ROUND(num,1). The ROUND function is very efficient ("cheap") as a BCD operation and 
should be used to compare REALs to DECIMALs at decimal width. 
 
 
Return Data Type: 
DECIMAL or REAL 
 
 
Example: 
 
 
## ROUND(5163,100)
!returns 5200 
 
## ROUND(657.50,1)
!returns 658 
 
## ROUND(51.63594,.01)
!returns 51.64 
 
ROUND(Price / Rate,.01) 
! Round the commission to the nearest cent 
 
 
 
 
SQRT (return square root) 
 
 
SQRT(expression) 
 
## SQRT
Returns square root. 
expression 
A numeric constant, variable, or expression. If the value of the expression is 
less than zero, the return value is zero. 
 
The SQRT function returns the square root of the expression. If X represents any positive real 
number, the square root of X is a number that, when multiplied by itself, produces a product 
equal to X. 
 
 
Return Data Type: 
## REAL
 
 
Example: 
## SQRT(X^2 + Y^2)
! The distance from 0,0 to x,y (pythagorean theorem) 


---

ReportWriter 
276 
 
 
 
 
 
 
Trigonometric Functions 
Trigonometric functions return values representing angles and ratios of the sides of a right 
triangle. Angles are expressed in radians. PI is a constant which represents the ratio of the 
circumference and radius of a circle. There are 2*PI radians (or 360 degrees) in a circle. 
The following equates provide high precision constants for PI and the conversion factors 
between degrees and radians. To use these conversion constants in ReportWriter, you can 
create calculated fields and assign them these values. 
 
PI 
3.1415926535898 
!The value of PI 
Rad2Deg 
57.295779513082 
!Number of degrees in a radian 
Deg2Rad 
.0174532925199 
!Number of radians in a degree 
 
 
 
 
SIN (return sine) 
 
 
SIN(radians) 
 
SIN 
Returns sine. 
radians 
A numeric constant, variable or expression for the angle expressed in radians. 
 
The SIN function returns the trigonometric sine of an angle measured in radians. The sine is 
the ratio of the length of the angle‘s opposite side divided by the length of the hypotenuse. 
 
 
Return Data Type: 
## REAL
 
 
Example: 
SIN(RadianField) 
! The sine of RadianField 
 
 
 
 
COS (return cosine) 
 
 
COS(radians) 
 
COS 
Returns cosine. 
radians 
A numeric constant, variable or expression for the angle in radians. 
The COS function returns the trigonometric cosine of an angle measured in radians. The 
cosine is the ratio of the length of the angle‘s adjacent side divided by the length of the 
hypotenuse. 
 
 
Return Data Type: 
## REAL
 
 
Example: 
COS(RadianField) 
! The cosine of RadianField 


---

APPENDIX B - Clarion Functions 
277 
 
 
 
 
 
 
 
 
TAN (return tangent) 
 
 
TAN(radians) 
 
TAN 
Returns tangent. 
Radians 
A numeric constant, variable or expression for the angle in radians. 
 
The TAN function returns the trigonometric tangent of an angle measured in radians. The 
tangent is the ratio of the angle‘s opposite side divided by its adjacent side. 
 
 
Return Data Type: 
## REAL
 
 
Example: 
TAN(RadianField) 
! The tangent of RadianField 
 
 
 
 
ASIN (return arcsine) 
 
 
ASIN(expression) 
 
## ASIN
Returns inverse sine. 
Expression 
A numeric constant, variable, or expression for the value of the sine. 
 
The ASIN function returns the inverse sine. The inverse of a sine is the angle that produces 
the sine. The return value is the angle in radians. 
 
 
Return Data Type: 
## REAL
 
 
Example: 
ASIN(SineAngle) 
! The Arcsine of SineAngle 
 
 
See Also: 
SIN 
 
 
 


---

ReportWriter 
278 
 
 
 
 
ACOS (return arccosine) 
 
 
ACOS(expression) 
 
## ACOS
Returns inverse cosine. 
expression 
A numeric constant, variable, or expression for the value of the cosine. 
 
The ACOS function returns the inverse cosine. The inverse of a cosine is the angle that 
produces the cosine. The return value is the angle in radians. 
 
 
Return Data Type: 
## REAL
 
 
Example: 
ACOS(CosineAngle) 
! The Arccosine of CosineAngle 
 
 
See Also: 
COS 
 
 
 
 
ATAN (return arctangent) 
 
 
ATAN(expression) 
 
## ATAN
Returns inverse tangent. 
expression 
A numeric constant, variable, or expression for the value of the tangent. 
 
The ATAN function returns the inverse tangent. The inverse of a tangent is the angle that 
produces the tangent. The return value is the angle in radians. 
 
 
Return Data Type 
## REAL
 
 
Example: 
ATAN(TangentAngle) 
! The Arctangent of TangentAngle 
 
 
See Also: 
TAN 


---

APPENDIX B - Clarion Functions 
279 
 
 
 
 
 
 
String Functions 
 
 
ALL (return repeated characters) 
 
 
ALL(string [,length]) 
 
ALL 
Returns repeated characters. 
string 
A string expression containing the character sequence to be repeated. 
length 
The length of the return string. If omitted the length of the return string is 255 
characters. 
 
The ALL function returns a string containing repetitions of the character sequence string. 
 
 
Return Data Type: 
## STRING
 
 
Example: 
## ALL(‗*‘,25)
! 25 asterisks 
 
 
 
 
BEGINSWITH (evaluate beginning of string) 
 
 
BEGINSWITH(string,substring) 
 
## BEGINSWITH
Returns TRUE if the string begins with the substring. 
string 
A string expression containing the character sequence to evaluate. 
substring 
A string expression containing the character sequence to compare. 
 
The BEGINSWITH function compares the beginning of the string with the substring. If the 
string begins with an exact match of the substring, the result will be TRUE. The BEGINSWITH 
function is case-sensitive. The function returns a BYTE containing zero (FALSE) or one 
(TRUE). Leading spaces are not ignored. 
 
 
Return Data Type: 
## BYTE
 
 
Example: 
If Formula: 
BEGINSWITH(CUS:Name,‘Ajax‘) ! Does Customer name start with ‗Ajax‘ ? 
 
 
 


---

ReportWriter 
280 
 
 
 
 
CENTER (return centered string) 
 
 
CENTER(string [,length]) 
 
## CENTER
Returns centered string. 
string 
A string constant, variable or expression. 
length 
The length of the return string. If omitted, the length of the string parameter 
is used. 
 
The CENTER function first removes leading and trailing spaces from a string, then pads it with 
leading and trailing spaces to center it within the length, and returns a centered string. 
 
 
Return Data Type:    STRING 
 
 
Example: 
## CENTER(‗ABC‘,5)
!returns ‗ ABC ‗ 
## CENTER(‗ABC
‗) !returns ‗ ABC ‗ 
CENTER(‗    ABC‘)         !returns ‗ ABC ‗ 
 
 
 
 
CHR (return character from ASCII) 
 
 
CHR(code) 
 
CHR 
Returns the display character. 
code 
A numeric expression containing a numeric ASCII character code. 
 
The CHR function returns the ANSI character represented by the ASCII character code 
parameter. 
 
 
Return Data Type: 
## STRING
 
 
Example: 
## CHR(122)
! Get lower case z 
## CHR(65)
! Get upper case A 
 
 
 


---

APPENDIX B - Clarion Functions 
281 
 
 
 
 
CLIP (return string without trailing spaces) 
 
 
CLIP(string) 
 
## CLIP
Removes trailing spaces. 
string 
A string expression. 
 
The CLIP function removes trailing spaces from a string. The return string is a substring with 
no trailing spaces. CLIP is frequently used with the concatenation operator in string 
expressions. 
 
 
Return Data Type: STRING 
 
 
Example: 
CLIP(Last) & ‗, ‗ & CLIP(First) & Init & ‗.‘ !Full name in military order 
 
 
 
 
CONTAINS(evaluate string) 
 
 
CONTAINS(string,substring) 
 
## CONTAINS
Returns TRUE if the string contains the substring. 
string 
A string expression containing the character sequence to evaluate. 
substring 
A string expression containing the character sequence to compare. 
 
The CONTAINS function checks for the existence of the substring within the string. If the string 
contains an exact match of the substring, the result will be TRUE. The CONTAINS function is 
case-sensitive. The function returns a BYTE containing zero (FALSE) or one (TRUE). 
 
 
Return Data Type: 
## BYTE
 
 
Example: 
IF Condition: 
CONTAINS(CUS:Name,‘ere‘) ! Does Customer name contain with ‗ere‘ ? 
 
 
 


---

ReportWriter 
282 
 
 
 
 
DEFORMAT (remove formatting from numeric string) 
 
 
DEFORMAT(string [,picture]) 
 
## DEFORMAT
Removes formatting characters from a numeric string. 
string 
A string expression containing a numeric string. 
picture 
A picture token or the label of a CSTRING, STRING, or PSTRING 
variable containing a picture token. CSTRING is more efficient than a 
STRING or a PSTRING). If omitted, the picture for the string parameter is 
used. If the string parameter was not declared with a picture token, the 
return value will contain only characters that are valid for a numeric 
constant 
 
The DEFORMAT function removes formatting characters from a numeric string, returning only 
the numbers contained in the string. When used with a date or time picture (except those 
containing alphabetic characters), it returns a STRING containing the Clarion Standard Date or 
Time. 
 
 
Return Data Type: 
## STRING
 
 
Example: 
‗ATDT1‘ & DEFORMAT(Phone,@P(###)###-####P) & ‗<13,10>‘ 
! Phone number for modem to dial 
DEFORMAT(dBaseDate,@D1) !Clarion Standard date from mm/dd/yy string 
 
 
See Also: 
## FORMAT
 
 
 
 
ENDSWITH (evaluate end of string) 
 
 
ENDSWITH(string,substring) 
 
## ENDSWITH
Returns TRUE if the string ends with the substring. 
string 
A string expression containing the character sequence to evaluate. 
substring 
A string expression containing the character sequence to compare. 
 
The ENDSWITH function compares the end of the string with the substring. If the string ends 
with an exact match of the substring, the result will be TRUE. The ENDSWITH function is case-
sensitive and ignores trailing spaces. The function returns a BYTE containing zero (FALSE) or 
one (TRUE). 
 
 
Return Data Type: 
## BYTE
 
 
Example: 
If Formula: 
ENDSWITH(CUS:Name,‘ing‘) ! Does Customer name end with ‗ing‘ ? 


---

APPENDIX B - Clarion Functions 
283 
 
 
 
 
 
 
 
 
FORMAT (format numbers into a picture) 
 
 
FORMAT(value,picture) 
 
## FORMAT
Returns a formatted numeric string. 
value 
A numeric expression for the value to be formatted. 
picture 
A picture token or the label of a STRING, CSTRING, or PSTRING variable 
containing a picture token (CSTRING is more efficient than STRING or 
## PSTRING).
 
The FORMAT function returns a numeric string formatted according to the picture parameter. 
 
 
Return Data Type: STRING 
 
 
Example: 
FORMAT(Emp:SSN,@P###-##-####P) ! Format the soc-sec-nbr 
 
 
FORMAT(DEFORMAT(Phone,@P###-###-####P),@P(###)###-####P) 
! Change phone format from dashes to parens 
 
 
See Also: DEFORMAT 
 
 
 


---

ReportWriter 
284 
 
 
 
 
INSTRING (search for substring) 
 
 
INSTRING(substring,string [,step] [,start]) 
 
## INSTRING
Searches for a substring in a string. 
substring 
A string constant, variable, or expression that contains the string for which to 
search. 
string 
A string constant, or the label of the STRING, CSTRING, or PSTRING variable 
to be searched. 
step 
A numeric constant, variable, or expression which specifies the step length of 
the search. A step of 1 searches for the substring beginning at every character 
in the string, a step of 2 starts at every other character, and so on. If step is 
omitted, the step length defaults to the length of the substring. 
start 
A numeric constant, variable, or expression which specifies where to begin the 
search of the string. If omitted, the search starts at the first character position. 
 
The INSTRING function steps through a string, searching for the occurrence of a substring. If 
the substring is found, the function returns the step number on which the substring was found. 
If the substring is not found in the string, INSTRING returns zero. 
 
 
Return Data Type: LONG 
 
 
Example: 
INSTRING(‗DEF‘,‘ABCDEFGHIJ‘,1,1) ! returns 4 
INSTRING(‗DEF‘,‘ABCDEFGHIJ‘,2,1) ! returns 0 
INSTRING(‗DEF‘,‘ABCDEFGHIJ‘,2,2) ! returns 2 
INSTRING(‗DEF‘,‘ABCDEFGHIJ‘,3,1) ! returns 2 
 
See Also: 
## BEGINSWITH, ENDSWITH, CONTAINS
 
 
 


---

APPENDIX B - Clarion Functions 
285 
 
 
 
 
LEFT (return left justified string) 
 
 
LEFT(string [,length]) 
 
## LEFT
Left justifies a string. 
string 
A string constant, variable, or expression. 
length 
A numeric constant, variable, or expression for the length of the return string. 
If omitted, length defaults to the length of the string. 
 
The LEFT function returns a left justified string. Leading spaces are removed from the string. 
 
 
Return Data Type: 
## STRING
 
 
Example: 
LEFT(CompanyName) !Left justify the company name 
 
 
 
 
LEN (return length of string) 
 
 
LEN(string) 
 
LEN 
Returns length of a string. 
string 
A string constant, variable, or expression. 
 
The LEN function returns the length of a string. If the string parameter is the label of a variable, 
the function will return the declared length of the variable. Numeric variables are automatically 
converted to STRING intermediate values. 
 
 
Return Data Type: 
## LONG
 
 
Example: 
 
 
If Formula: 
LEN(CLIP(Title) & ‗ ‗ & CLIP(First) & ‗ ‗ & CLIP(Last)) > 30 
! is length more than 30 characters? 
 
 
True Formula: 
CLIP(Title) & ‗ ‗ & SUB(First,1,1) & ‗. ‗ & Last ! use first initial 
 
 
Else Formula: 
CLIP(Title) & ‗ ‗ & CLIP(First) & ‗ ‗ & CLIP(Last) ! use full name 
 
 
 


---

ReportWriter 
286 
 
 
 
 
LOWER (return lower case) 
 
 
LOWER(string) 
 
## LOWER
Converts a string to all lower case. 
string 
A string constant, variable, or expression for the string to be converted. 
 
The LOWER function returns a string with all letters converted to lower case. 
 
 
Return Data Type: 
## STRING
 
 
Example: 
SUB(Name,1,1) & LOWER(SUB(Name,2,19)) !Make the rest of the name lower case 
 
 
 
 
NUMERIC (check numeric string) 
 
 
NUMERIC(string) 
 
## NUMERIC
Validates all numeric string. 
string 
A string constant, variable, or expression. 
 
The NUMERIC function returns the value 1 (true) if the string contains a valid numeric value. It 
returns zero (false) if the string contains non-numeric characters. Valid numeric characters are 
the digits 0 through 9, a leading minus sign, and a decimal point. 
 
 
Return Data Type:    LONG 
 
 
Example: 
 
 
If Formula: 
NUMERIC(PartNumber)                  ! If part number is numeric 
 
 
 
 
RIGHT (return right justified string) 
 
 
RIGHT(string [,length]) 
 
## RIGHT
Right justifies a string. 
string 
A string constant, variable, or expression. 
length 
A numeric constant, variable, or expression for the length of the return string. 
If omitted, the length is set to the length of the string. 


---

APPENDIX B - Clarion Functions 
287 
 
 
 
 
The RIGHT function returns a right justified string. Trailing spaces are removed, then the string 
is right justified and returned with leading spaces. 
 
 
Return Data Type: 
## STRING
 
 
Example: 
RIGHT(Message) 
!Right justify the message 
 
 
 
 
SUB (return substring of string) 
 
 
SUB(string,position,length) 
 
SUB 
Returns a portion of a string. 
string 
A string constant, variable or expression. 
Position 
An integer constant, variable, or expression. If positive, it points to a character 
position relative to the beginning of the string. If negative, it points to the 
character position relative to the end of the string (i.e., a position value of -3 
points to a position 3 characters from the end of the string). 
length 
A numeric constant, variable, or expression of number of characters to return. 
 
The SUB function parses out a sub-string from a string by returning length characters from the 
string, starting at position. 
The SUB function is similar to the "string slicing" operation on STRING, CSTRING, and 
PSTRING variables, but is less flexible and efficient. "String slicing" is more flexible because it 
may be used on both the destination and source sides of an assignment statement, while the 
SUB function can only be used as the source. It is more efficient because it takes less memory 
than individual character assignments or the SUB function. 
To take a "slice" of a string, the beginning and ending character numbers are separated by a 
colon (:) and placed in the implicit array dimension position within the square brackets ([]) of  
the string. The position numbers may be integer constants, variables, or expressions. If 
variables are used, there must be at least one blank space between the variable name and the 
colon separating the beginning and ending number (to prevent PREfix confusion). 
 
 
Return Data Type: 
## STRING
 
 
Example: 
## SUB(‗ABCDEFGHI‘,1,1)
! returns ‗A‘ 
SUB(‗ABCDEFGHI‘,-1,1) ! returns ‗I‘ 
## SUB(‗ABCDEFGHI‘,4,3)
! returns ‗DEF‘ 
 
 
 


---

ReportWriter 
288 
 
 
 
 
UPPER (return upper case) 
 
 
UPPER(string) 
 
## UPPER
Returns all upper case string. 
string 
A string constant, variable, or expression for the string to be converted. 
 
The UPPER function returns a string with all letters converted to upper case. 
 
 
Return Data Type: 
## STRING
 
 
Example: 
UPPER(Name) 
!Make the name upper case 
 
 
 
 
VAL (return ASCII value) 
 
 
VAL(character) 
 
VAL 
Returns ASCII code. 
character 
A one-byte string containing a character. 
 
The VAL function returns the ASCII code of a character. 
 
 
Return Data Type: 
## LONG
 
 
Example: 
## VAL(‗A‘)
! returns 65 
VAT(‗z‘) 
! returns 122 


---

289 
 
 
APPENDIX C - Database Drivers 
 
 
Clarion ReportWriter for Windows achieves database independence with its built-in driver 
technology, enabling you to access data from virtually any file system and print reports from 
that data. Many file drivers are available and more are being added. All of the file drivers read 
and write in the file system‘s native format without temporary files or import/export routines. 
Often, your Report Library‘s purpose is accessing data in its original format. For those times, 
you just import the file definition from the data file using the appropriate file driver. 
ReportWriter accesses data from these different systems in the same manner; simply choose 
the correct file driver from the drop-down list when importing the file definition, and don‘t worry 
about it. 
If you are deploying Report Libraries to end users, you must include the appropriate file 
driver(s) for the data files the Report Library accesses. Consult the appropriate section of this 
appendix for the Database Driver‘s filename. 
To use a database driver, you must deploy the File Driver DLL for the format of your data files 
(one or more from the list below): 
 
## ASCII
## C70ASC.DLL
## BASIC
## C70BAS.DLL
Btrieve 
## C70BTR.DLL
Clarion 
## C70CLA.DLL
Clipper 
## C70CLP.DLL
dBase III 
## C70DB3.DLL
dBase IV 
## C70DB4.DLL
DOS 
## C70DOS.DLL
FoxPro 
## C70FOX.DLL
## ODBC
## C70ODB.DLL
Pervasive 
## C70SCA.DLL
TopSpeed 
## C70TPS.DLL


---

290 
ReportWriter 
 
 
 
 
APPENDIX C - Database Drivers 
 
 
Clarion ReportWriter for Windows achieves database independence with its built-in driver 
technology, enabling you to access data from virtually any file system and print reports from 
that data. Many file drivers are available and more are being added. All of the file drivers read 
and write in the file system‘s native format without temporary files or import/export routines. 
Often, your Report Library‘s purpose is accessing data in its original format. For those times, 
you just import the file definition from the data file using the appropriate file driver. 
ReportWriter accesses data from these different systems in the same manner; simply choose 
the correct file driver from the drop-down list when importing the file definition, and don‘t worry 
about it. 
If you are deploying Report Libraries to end users, you must include the appropriate file 
driver(s) for the data files the Report Library accesses. Consult the appropriate section of this 
appendix for the Database Driver‘s filename. 
To use a database driver, you must deploy the File Driver DLL for the format of your data files 
(one or more from the list below): 
 
## ASCII
## C70ASC.DLL
## BASIC
## C70BAS.DLL
Btrieve 
## C70BTR.DLL
Clarion 
## C70CLA.DLL
Clipper 
## C70CLP.DLL
dBase III 
## C70DB3.DLL
dBase IV 
## C70DB4.DLL
DOS 
## C70DOS.DLL
FoxPro 
## C70FOX.DLL
## ODBC
## C70ODB.DLL
Pervasive 
## C70SCA.DLL
TopSpeed 
## C70TPS.DLL


---

APPENDIX C - Database Drivers 
291 
 
 
 
 
ASCII Files 
The ASCII driver reads standard ASCII files without field delimiters. This is often used for 
mainframe data import/export with an ASCII flat-file. A carriage-return/line-feed delimits 
records. The ASCII driver does not support keys. 
ASCII database driver: 
## C70ASC.DLL
 
 
 
Due to its lack of relational features and security (anyone can view and change an ASCII file 
using Notepad), it‘s unlikely you‘ll see the ASCII driver used to store large data files. But it can 
help you create a report from a text file. 
 
 
Supported Data Types 
## STRING
## GROUP
 
 
File Specifications/Maximums 
File Size:          4,294,967,295 bytes 
Records per File: 
4,294,967,295 bytes 
Record Size:                65,520 bytes 
Field Size: 
65,520 bytes 
Fields per Record: 
65,520 bytes 
Keys/Indexes per 
File: 
n/a 
 
Key Size: 
n/a 
 
Memo fields per 
File: 
 
n/a 
 
Memo Field Size: 
n/a 
 
Open Data Files: 
Operating system dependent 


---

ReportWriter 
292 
 
 
 
 
BASIC Files 
The BASIC file driver reads comma-delimited ASCII files. Quotes ( " " ) surround strings, 
commas delimit fields, and a carriage-return/line-feed delimits records. The original BASIC 
programming language defined this 5file format. The Basic driver does not support keys. 
 
 
 
The Basic file format provides a common file format for sharing data with spreadsheet and 
mail-merge programs. A common file extension used for these files is *.CSV, which stands for 
"comma separated values." 
BASIC database driver: 
## C70BAS.DLL
 
 
Supported Data Types 
 
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
 
File Specifications/Maximums 
 
File Size:              4,294,967,295 bytes 
Records per File:    4,294,967,295 bytes 
Record Size:                     65,520 bytes 
Field Size: 
65,520 bytes 
 
Fields per Record: 
65,520 bytes 
Keys/Indexes per File: 
n/a 
Key Size: 
n/a 
 
Memo fields per File: 
0 
 
Memo Field Size: 
n/a 
 
Open Data Files: 
Operating system dependent 


---

APPENDIX C - Database Drivers 
293 
 
 
 
 
Btrieve Files 
This file driver reads Btrieve files using low-level direct access. 
Under Clarion, the Btrieve file driver is implemented by using .DLLs and an .EXE supplied by 
Pervasive Software (formerly Btrieve Technologies, Inc.). For an application to use a Btrieve 
file driver, you must purchase a 32-bit Btrieve engine from Pervasive Software. 
A single file normally holds the data and all keys. Data filenames default to a *.DAT file 
extension. By default, the driver stores memos in a separate file, or optionally in the data file 
itself, given the appropriate driver string. 
KEYs are dynamic, and automatically update when the data file changes. 
INDEXes are stored separately from data files. INDEX files receive a temporary file name, and 
are deleted when the program terminates normally. INDEXes are static—they are not 
automatically updated when the data file changes. The application must create or update index 
files. 
The Btrieve file format stores minimal file structure information in the file. The driver validates 
your description against the information in the file. It is possible to successfully open a Btrieve 
file that has key definitions that do not exactly match your definition. 
Btrieve database driver:
 
## C70BTR.DL
L Data Types 
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
STRING,LVAR or NOTE (see below) 
 
## BYTE,NAME(‗LOGICAL‘)
## LOGICAL*
## USHORT,NAME(‗LOGICAL‘)
## LOGICAL*
## PDECIMAL,NAME(‗MONEY‘)             MONEY*
STRING(@N0n-),NAME(‗STS‘) 
## SIGNED TRAILING SEPARATE*
## DECIMAL*


---

ReportWriter 
294 
 
 
 
 
 
File Specifications/Maximums 
File Size: 
4,000,000,000 bytes 
Records per File: 
Limited by the size of the file 
 
Record Size 
 
Client-based: 
65,520 bytes variable length 
 
Server based: 
54K variable length 
 
Field Size: 
65,520 bytes 
Fields per Record: 
65,520 bytes 
Keys/Indexes per 
File: 
 
256 with NLM6. 
Client Btrieve v6.15 
24 with NLM5 
 
Page Size 
Max Key Segments 
512 
8 
1,024 
23 
1,536 
24 
2,048 
54 
4,096 
119 
This is the total number of components. If you have a multi component key built from three 
fields, this counts as three indexes when counting the number of allowed indexes. 
 
 
Key Size: 
255 bytes 
 
Memo fields per 
File: 
 
System memory dependent 
 
Memo field size: 
65,520 bytes 
 
Open Files: 
Operating system dependent 


---

APPENDIX C - Database Drivers 
295 
 
 
 
 
 
 
Clarion Files 
The Clarion file driver is compatible with the file system originally used by the Clarion for DOS 
3.1 and Clarion Professional Developer 2.1 products. 
Keys and Indexes exist as separate files from the data file. Keys are dynamic—they are 
automatically updated as the data file changes. The default file extension for a key file is *.K##. 
Indexes are static—they do not automatically update, the application must update them. 
The driver stores records as fixed length. It stores memo fields in a separate file. The memo 
file defaults to the first eight characters of the File Label plus an extension of .MEM. 
Clarion database driver: 
## C70CLA.DLL
 
 
 
By avoiding the ASCII-only file formats of many other popular PC database application 
development systems, the Clarion file format provides a more secure means of storing data. 
 
 
Data Types: 
## BYTE
## DECIMAL
 
## SHORT
STRING (255 byte maximum) 
 
## LONG
## MEMO
 
## REAL
## GROUP
 
 
If you do not have the file definition in a Clarion Data Dictionary or Report Library, use the File 
Import Utility in Clarion ReportWriter for Windows to define your files. 
 
 
Maximum File Specifications: 
File Size: 
limited only by disk space 
Records per File: 
4,294,967,295 
Record Size: 
65,520 bytes 
 
Field Size: 
65,520 bytes 
Fields per Record: 
65,520 bytes 
Keys/Indexes per 
File: 
251 
 
Key Size: 
245 bytes 
Memo fields per 
1 
File: 
Memo Field Size: 
65,520 bytes 
Open Data Files: 
Operating system dependent 


---

ReportWriter 
296 
 
 
 
 
Clipper Files 
The Clipper file driver is compatible with Clipper Summer ‗87 and Clipper 5.0. The default data 
file extension is *.DBF. 
Keys and Indexes exist as separate files from the data file. Keys are dynamic—they 
automatically update as the data file changes. Indexes are static—they do not automatically 
update, the application must update them. The default file extension for the index file is *.NTX. 
The driver stores records as fixed length. It stores memo fields in a separate file. The memo 
file name takes the first eight characters of the File Label plus an extension of .DBT. 
Clipper database driver: 
## C70CLP.DLL
 
 
 
As a popular xBase database application development system, Clipper provides a common file 
format for many installed business applications and their data files. Use the Clipper driver to 
access these files in their native format. 
 
 
Data Types 
The xBase file format stores all data as ASCII strings. You may either specify STRING types 
with declared pictures for each field, or specify native Clarion data types, which the driver 
converts automatically. 
 
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
If your application reads and writes to existing files, a pictured STRING will suffice. 
 
 
 
If you do not have the file definition in a Clarion Data Dictionary or Report Library, use the File 
Import Utility in Clarion ReportWriter for Windows to define your files. 
 
 
File Specifications/Maximums 
File Size: 
2,000,000,000 bytes 
Records per File: 
1,000,000,000 
Record Size: 
4,000 bytes (Clipper ‗87) 
 
8,192 bytes (Clipper 5.0) 
 
Field Size: 
 
Character: 
254 bytes (Clipper ‗87) 
 
2048 bytes (Clipper 5.0) 
 
Date: 
8 bytes 
 
Logical: 
1 byte 


---

APPENDIX C - Database Drivers 
297 
 
 
 
 
Numeric: 
20 bytes including decimal point 
 
Memo: 
65,520 bytes (see note) 
Fields per Record: 
1024 
Keys/Indexes per 
File: 
 
Key Sizes 
No Limit 
 
Character: 
100 bytes 
 
Numeric, Date: 
8 bytes 
 
Memo fields per 
File: 
 
Dependent on available memory 
 
Open Files: 
Operating system dependent 
Miscellaneous: 
Boolean Evaluation 
Clipper allows a logical field to accept one of nine possible values (y,Y,n,N,t,T,f,F or a space 
character). The space character is neither true nor false. When using a logical field from a 
preexisting database in a logical expression, account for all these possibilities. Remember that 
when a STRING field is used as an expression, it is true if it contains any data and false if it is 
equal to zero or blank. Therefore, to evaluate a Logical field‘s truth, the expression should be 
true if the field contains any of the "true" characters (T,t,Y, or y). For example, if a Logical field 
were used to specify a product as taxable or nontaxable, the expression to evaluate its truth 
would be: 
(If Condition): 
Taxable=‘T’ OR Taxable=‘t’ OR Taxable=‘Y’ OR Taxable=‘y’ 
 
 
Large MEMOs 
Clarion supports MEMO fields up to a maximum of 64K. If you have an existing file which 
includes a memo greater than 64K, you can use the file but not the large MEMOs. 
 
 
International Sort Sequence 
Clarion‘ Clipper driver supports international sort orders, however, to maintain compatibility 
with Clipper‘s international sort order, remove the CLADIGRAPH= line from 
..\CLARION7\BIN\C70ee.ENV file. 


---

ReportWriter 
298 
 
 
 
 
dBase III Files 
The dBase3 file driver is compatible with dBase III. The default data file extension is *.DBF. 
Keys and Indexes exist as separate files from the data file. Keys are dynamic—they 
automatically update as the data file changes. Indexes are static—they do not automatically 
update, the application must update them. The default file extension for the index file is *.NDX. 
International sort orders are supported. 
The driver stores records as fixed length. It stores memo fields in a separate file. The memo 
file name takes the first eight characters of the File Label plus an extension of .DBT. 
dBase III database driver 
## C70DB3.DLL
Data Types 
The xBase file format stores all data as ASCII strings. You may either specify STRING types 
with declared pictures for each field, or specify native Clarion types, which the driver converts 
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
If your application reads and writes to existing files, a pictured STRING will suffice. 
 
 
File Specifications/Maximums: 
File Size: 
2,000,000,000 bytes 
 
Records per File: 
1,000,000,000 
 
Record Size: 
4,000 bytes 
Field Size 
Character: 
254 bytes 
Date: 
8 bytes 
Logical: 
1 byte 
Numeric: 
20 bytes including decimal point 
Memo: 
64K (see note) 
Fields per Record: 
128 
 
Keys/Indexes per File: 
No Limit 
Key Sizes 
Character: 
100 bytes 
Numeric, Date: 
8 bytes 
 
Memo fields per File: 
Dependent on available memory 
Open Files: 
Operating system dependent 


---

APPENDIX C - Database Drivers 
299 
 
 
 
 
Miscellaneous: 
 
 
Boolean Evaluation 
dBase III allows a logical field to accept one of nine possible values (y,Y,n,N,t,T,f,F or a space 
character). The space character is neither true nor false. When using a logical field from a 
preexisting database in a logical expression, account for all these possibilities. Remember that 
when a STRING field is used as an expression, it is true if it contains any data and false if it is 
equal to zero or blank. Therefore, to evaluate a Logical field‘s truth, the expression should be 
true if the field contains any of the "true" characters (T,t,Y, or y). For example, if a Logical field 
were used to specify a product as taxable or nontaxable, the expression to evaluate its truth 
would be: 
(If Condition): 
Taxable=‘T’ OR Taxable=‘t’ OR Taxable=‘Y’ OR Taxable=‘y’ 
 
 
Large MEMOs 
Clarion supports MEMO fields up to a maximum of 64K. If you have an existing file which 
includes a memo greater than 64K, you can use the file but not modify the large MEMOs. 
You can determine when your application encounters a large MEMO by detecting when the 
memo pointer variable is non-blank, but the memo appears to be blank. Error 47 (Bad Record 
Declaration) is posted, and any modification to the MEMO field is ignored. 
 
 
International Sort Sequence 
Clarion‘ dBaseIII driver supports international sort orders, however, to maintain compatibility 
with dBaseIII‘s international sort order, remove the CLADIGRAPH= line from 
\CLARION6\BIN\C70ee.ENV file. 


---

ReportWriter 
300 
 
 
 
 
 
 
dBase IV Files 
The dBase4 file driver is compatible with dBase IV. The default data file extension is *.DBF. 
Keys and Indexes exist as separate files from the data file. Keys are dynamic—they 
automatically update as the data file changes. Indexes are static—they do not automatically 
update, the application must update them. The default file extension for the index file is *.NDX. 
dBase IV supports multiple index files, whose extension is *.MDX. The miscellaneous section 
describes procedures for using .MDX files. 
The driver stores records as fixed length. It stores memo fields in a separate file. The memo 
file name takes the first eight characters of the File Label plus an extension of .DBT. 
dBase IV database driver: 
## C70DB4.DLL
 
 
 
dBase IV was never as widely adopted as dBase III. Choose this driver only when you must 
share data with an end-user using dBase IV. 
 
 
Data Types 
The xBase file format stores all data as ASCII strings. You may either specify STRING types 
with declared pictures for each field, or specify native Clarion types, which the driver converts 
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
If your application reads and writes to existing files, a pictured STRING will suffice. 
 
 
If you do not have the file definition in a Clarion Data Dictionary or Report Library, use the File 
Import Utility in Clarion ReportWriter for Windows to define your files. 
File Specifications/Maximums 
File Size: 
2,000,000,000 bytes 
 
Records per File: 
1,000,000,000 
 
Record Size: 
4,000 bytes 
Field Size 
Character 
254 bytes 
Date: 
8 bytes 
Logical: 
1 byte 
Numeric: 
20 bytes including decimal point 
Float: 
20 bytes including decimal point 
Memo: 
64K (see note) 


---

APPENDIX C - Database Drivers 
301 
 
 
 
 
Fields per Record: 
512 
 
Keys/Indexes per File: 
 
## .NDX:
No Limit 
 
## .M DX
47 tags per .MDX files 
Key Sizes: 
Character: 
100 bytes 
Numeric, Date: 
8 bytes 
 
Memo fields per File: 
Dependent on available 
memory 
 
Open Files: 
Operating system dependent 
 
 
Miscellaneous: 
 
 
International Sort Sequence 
dBase IV sorts as if there were no diacritics in a field, thus A is sorted the same as Ä. If two 
words are identical except for diacritic characters, then the words are sorted as though the 
diacritic character was greater than the normal character. For example Äa < Ab < Äb whereas 
a CLADIGRAPH of ÄAE will sort as Ab < Äa < Äb. Solution- if the same file is used in Clarion 
and dBase IV, issue a BUILD statement rebuild the keys before updating the file (reading the 
file causes no problems). 
 
 
Boolean Evaluation 
dBase IV allows a logical field to accept one of 11 possible values (1,0,y,Y,n,N,t,T,f,F or a 
space character). The space character is neither true nor false. When using a logical field from 
a preexisting database in a logical expression, account for all these possibilities. Remember 
that when a STRING field is used as an expression, it is true if it contains any data and false if 
it is equal to zero or blank. Therefore, to evaluate a Logical field‘s truth, the expression should 
be true if the field contains any of the "true" characters (T,t,Y, or y). For example, if a Logical 
field were used to specify a product as taxable or nontaxable, the expression to evaluate its 
truth would be: 
(If Condition): 
Taxable=‗1‘ OR Taxable=‗T‘ OR Taxable=‗t‘ OR Taxable=‗Y‘ OR Taxable=‗y‘ 
 
 
Large MEMOs 
Clarion supports MEMO fields up to a maximum of 64K. If you have an existing file which 
includes a memo greater than 64K, you can use the file but not modify the large MEMOs. 
You can determine when your application encounters a large MEMO by detecting when the 
memo pointer variable is non-blank, but the memo appears to be blank. Error 47 (Bad Record 
Declaration) is posted, and any modification to the MEMO field is ignored. 


---

ReportWriter 
302 
 
 
 
 
DOS Files 
The DOS file driver reads and writes any binary, byte-addressable files. Neither fields nor 
records are delimited. When reading a record, the driver reads the number of bytes defined in 
the file‘s RECORD structure, unless a length parameter is specified. 
This file driver performs forward sequential processing only. No key or transaction processing 
functions are supported. 
 
Due to its limitations, the main function of this driver is as a disk editor for binary files. 
DOS database driver 
## C70DOS.DLL
 
Data Types 
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
## BFLOAT4
 
File Specifications/Maximums: 
File Size: 
4,294,967,295 
Records per File: 
4,294,967,295 
Record Size: 
64K 
Field Size: 
64K 
Fields per Record: 
64K 
Keys/Indexes per File: 
n/a 
Key Size: 
n/a 
Memo fields per File: 
n/a 
Memo Field Size: 
n/a 
Open Data Files: 
Operating system dependent 


---

APPENDIX C - Database Drivers 
303 
 
 
 
 
 
 
FoxPro and FoxBase Files 
 
 
The FoxPro file driver is compatible with FoxPro and FoxBase. The default data file extension 
is *.DBF. 
The default index file extension is *.IDX. The default Memo file extension is .FBT. FoxPro also 
supports multiple index files, whose default extension is *.CDX. The miscellaneous section 
describes the procedures for using the .CDX files. 
FoxPro database driver: 
## C70FOX.DLL
 
 
Data Types 
The xBase file format stores all data as ASCII strings. 
FoxPro data type 
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
If your application reads and writes to existing files, a pictured STRING will suffice. 
 
 
 
If you do not have the file definition in a Clarion Data Dictionary or Report Library, use the File 
Import Utility in Clarion ReportWriter for Windows to define your files. 
 
 
File Specifications/Maximums 
File Size: 
2,000,000,000 bytes 
Records per File: 
1,000,000,000 bytes 
Record Size: 
4,000 bytes 
Field Size: 
Character: 
254 bytes 
Date: 
8 bytes 
Logical: 
1 byte 
Numeric: 
20 bytes including decimal point 
Float: 
20 bytes including decimal point 
Memo: 
65,520 bytes (see note) 
Fields per Record: 
512 
Keys/Indexes per File: 
No Limit 
Key Sizes: 
Character: 
100 bytes (.IDX) 


---

ReportWriter 
304 
 
 
 
 
254 bytes (.CDX) 
Numeric, Date: 
8 bytes 
Memo fields per File: 
Dependent on available memory 
Open Files: 
Operating system dependent 
 
Miscellaneous: 
 
 
Boolean Evaluation 
FoxPro and FoxBase allow a logical field to accept one of 11 possible values 
(0,1,y,Y,n,N,t,T,f,F or a space character). The space character is neither true nor false. When 
using a logical field from a preexisting database in a logical expression, account for all these 
possibilities. Remember that when a STRING field is used as an expression, it is true if it 
contains any data and false if it is equal to zero or blank. Therefore, to evaluate a Logical 
field‘s truth, the expression should be true if the field contains any of the "true" characters 
(1,T,t,Y, or y). For example, if a Logical field were used to specify a product as taxable or 
nontaxable, the expression to evaluate its truth would be: 
(If Condition): 
Taxable=‗1‘ OR Taxable=‗T‘ OR Taxable=‗t‘ OR Taxable=‗Y‘ OR Taxable=‗y‘ 
 
 
Large MEMOs 
Clarion supports MEMO fields up to a maximum of 64K. If you have an existing file which 
includes a memo greater than 64K, you can use the file but not modify the large MEMOs. 
You can determine when your application encounters a large MEMO by detecting when the 
memo pointer variable is non-blank, but the memo appears to be blank. Error 47 (Bad Record 
Declaration) is posted, and any modification to the MEMO field is ignored. 


---

APPENDIX C - Database Drivers 
305 
 
 
 
 
ODBC—Open Data Base Connectivity 
ODBC (Open DataBase Connectivity) is a Windows "strategic interface" for accessing data 
from a variety of Database Management Systems (DBMS) and data file formats, across a 
variety of networks and platforms. ODBC offers the same end result as the file driver libraries 
which ship with Clarion ReportWriter for Windows—file driver independence—though in a 
somewhat different manner. 
The ODBC standard was developed and is maintained by Microsoft, which publishes an ODBC 
Software Development Kit (SDK) for use with its Office products, as well as its Visual Basic   
and Visual C++ products. ODBC support is another way in which Clarion ReportWriter for 
Windows provides an extensible platform for you to create reports. 
 
 
ODBC database driver: 
## C70ODB.DLL
 
 
ODBC Pro’s and Con’s 
 
Using ODBC offers the following advantages: 
 
ODBC is an excellent choice in a Client-Server environment, especially if the Server is a native 
Structured Query Language (SQL) DBMS. It allows you to use Client-Server support in your 
reports, without having to do much more than choose a file driver. ODBC was specifically 
designed to create a non-vendor-specific method of connecting front end applications to back 
end services. With ODBC, the Server can handle much of the work, especially for SQL JOIN 
and PROJECT operations, thereby speeding up processing. 
 
Existing ODBC drivers cover a great many types of databases. There are ODBC drivers 
available for databases for which Clarion may not have a native driver—for example, Microsoft 
Excel and Lotus Notes files. 
 
ODBC is already widespread. Major application suites such as Microsoft Office install ODBC 
drivers for file formats such as dBase and Microsoft Access. Keep in mind that many ODBC 
back end drivers have been updated and you should obtain the latest releases. 
 
ODBC is platform independent. One of Microsoft‘s prime objectives in establishing ODBC was 
to support easier access to legacy systems, or corporate environments where data resides on 
diverse platforms or multiple DBMS‘s. As long as an ODBC driver and back end are available, 
it doesn‘t matter whether you use Microsoft‘s NetBEUI, SPX/IPX, DECNet or others; your 
Report Library can connect to the DBMS and access the data. 
 
Given that there are many drivers available, and that the standard was developed by the 
company that developed Windows, you might consider using ODBC as the driver of choice for 
all your Windows applications. Yet, when deciding whether to use an ODBC driver or a Clarion 
ReportWriter for Windows native database driver, you must also consider possible 
disadvantages: 
 
ODBC adds a layer—the ODBC Driver Manager—between ReportWriter and the database. 
When accessing files on a local hard drive, this generally results in slower performance. The 
driver manager must translate ReportWriter‘s ODBC API call to an SQL statement before any 
data access occurs. 
 
ODBC uses SQL to communicate with the back end database. Although this can be very 
efficient when communicating with Client/Server database engines, it is normally less efficient 
than direct record access when using a file system designed around single record access, 
such as xBase or Btrieve. 
 
The information required by the ODBC database manager to connect to a data source varies 
from one ODBC driver to another. Unlike the selection of Clarion file drivers, where file 
operations are virtually transparent, you may need to do some work to gather the information 
required to use a particular ODBC driver. Many ODBC drivers come with a Help (.HLP) file 


---

ReportWriter 
306 
 
 
 
 
which documents special settings (usually stored in ODBC.INI); but the burden is on you to 
solve any problems with third-party ODBC drivers. 
 
ODBC is not included with Windows. When distributing your reports, you‘ll need to install the 
ODBC drivers and the ODBC driver manager into the end user‘s system. This requires the 
ODBC SDK from Microsoft. In some cases, the back end server may have already provided a 
distribution kit which installs the ODBC driver on the workstation. 
 
The normal Microsoft setup program that installs the ODBC driver manager adds an applet to 
the end user‘s Control Panel window for managing ODBC. It‘s very easy for an end user to use 
this tool to change the settings in the ODBC.INI file. The end user can unwittingly remove or 
modify the settings for the back end ODBC driver which would make it impossible for 
ReportWriter to connect to the data file. Additionally, since most ODBC drivers store the data 
directory in ODBC.INI, it‘s very easy for the end user to change it, again introducing a possible 
problem for ReportWriter . 
 
Given the pros and cons, we recommend using the native Clarion ReportWriter for Windows 
file drivers when both a native driver and an ODBC driver exist for the same file format. 
 
 
How ODBC Works 
When you use ODBC to access data, four components must cooperate to make it work: 
ReportWriter calls the ODBC driver manager, and sends it the appropriate requests for data, 
with the ODBC API. 
 
Clarion does this for you transparently, using either the C70ODB.DLL (16-bit) application 
extension. When distributing your reports, be sure to include this file. 
 
The ODBC driver manager receives the API calls, checks ODBC.INI for information on the 
data source, then loads the ODBC "back-end" driver. 
 
The actual "interface" to the driver manager is a file called ODBCADM.EXE, which the 
Microsoft setup program places in the \Windows\System directory. This is the ODBC 
Administrator, which then loads other libraries to do its work. 
 
The ODBC "back-end" driver is another library (.DLL) which contains the executable code for 
accessing the data. 
 
Various third-parties supply "back-end" drivers. For example, Lotus Development Corp. 
supplies the ODBC driver for Lotus Notes. Microsoft Office distributes an ODBC SDK 
containing drivers for most of their database products. 
 
The data source is either a data file (usually when ODBC is used for local data access), or a 
remote DBMS, such an Oracle 7 database. 
 
The data source has a descriptive name; for example, "Microsoft Access Databases." The 
name serves as the section name in the ODBC.INI file. 
 
The ODBC driver manager must know the exact data source name so that it can load the right 
driver to access the data. Therefore, it‘s vitally important that you know the precise data source 
name. 
 
 
Importing ODBC File Definitions—the Basics 
 
Using ODBC data sources only requires choosing Clarion ReportWriter‘s ODBC driver and 
importing the file definition. You may also need to provide the parameters in the OWNER and 
NAME attributes of the FILE declaration. 
 
 


---

APPENDIX C - Database Drivers 
307 
 
 
 
 
When creating a report for ODBC tables, importing the file definitions provides this information 
in the appropriate fields. 
 
The following introduces the basics. Of course, you must also be sure that the field data types 
in your dictionary match the variable formats supported by the DBMS you‘re connecting to. 
 
1. Create or open a Report Library file. 
2. Create a report. 
3. Select the Standard Data Source (see Adding a Data Source to a Report section for 
more information). 
The Choose a data connection dialog appears. 
4. Press the New Connection button to open the Data Link Properties list. 
5. Select a OLE DB Provider, then press the Next button. 
6. Enter the appropriate Connection information, and then press the Test Connection 
button to verify your connection information. 
7. Press OK to return to the Choose a data connection dialog. 
8. Press the Next button to proceed to select your tables to use for your report. 
 
 
Data Types 
 
 
ODBC data type 
Clarion data type 
 
## CHAR
## STRING, CSTRING
 
## VARCHAR
## STRING, CSTRING
 
## LONG VARCHAR
## STRING, CSTRING
 
## DECIMAL
## DECIMAL,    BYTE1,SHORT1,LONG1,PDECIMAL
## NUMERIC
## PDECIMAL,    BYTE1,SHORT1,LONG1,DECIMAL
## SMALLINT
## SHORT
 
## INTEGER
## LONG
 
## REAL
## SREAL
 
## FLOAT
## REAL
 
## DOUBLE PRECISION
## REAL
 
BIT 
## BYTE
 
## TINYINT
## BYTE
 
## BIGINT
## DECIMAL,PDECIMAL
 
## BINARY
## STRING
 
## VARBINARY
## STRING
 
## LONGBINARY
## STRING
 
## DATE
## DATE
 
## TIME
## TIME
 
## TIMESTAMP
## STRING2
 
 
Notes: 


---

ReportWriter 
308 
 
 
 
 
1. Clarion LONG, SHORT, and BYTE can be used with ODBC DECIMAL and NUMERIC 
data types if the ODBC field does not have any decimal places. 
2. ODBC TIMESTAMP fields can be manipulated using a STRING(8) followed by a 
GROUP over it which contains only a DATE field and a TIME field. 
 
 
Example: 
 
 
TimeStampField 
STRING(8),NAME(‘TimeStampField’) 
TimeStampGroup GROUP,OVER(TimeStampField) 
TimeStampDate 
## DATE
TimeStampTime 
## TIME
END 
CREATE() will create a TIMESTAMP field if the you use a similar structure. 
Note: 
Your back-end database may contain data types that are not listed here. These data types are 
converted to ODBC data types by the back-end database. Consult you back-end database‘s 
documentation to determine which ODBC data type is used. 


---

APPENDIX C - Database Drivers 
309 
 
 
 
 
Pervasive SQL 
Pervasive SQL Server 
For complete information on the Pervasive SQL database system, please review Pervasive 
Software‘s documentation. 
Pervasive database driver: 
## C70SCA.DLL
 
 
Pervasive SQL Driver 
The Pervasive SQL Driver is one of several SoftVelocity SQL Accelerator drivers. These SQL 
Drivers share a common code base and many common features such as SoftVelocity‘s 
unique, high speed buffering technology, common driver strings, and SQL logging capability. 
The Pervasive SQL Driver converts standard Clarion file I/O statements and function calls into 
optimized SQL statements, which it sends to the backend Pervasive SQL server for 
processing. 
 
 
SQL Import Wizard—Login Dialog 
The Import Wizard lets you import Pervasive SQL table definitions into your Report Libraries. 
When you select the Pervasive SQL Accelerator Driver from the driver drop-down list, the 
Import Wizard opens the Login/Connection dialog. The Login/Connection dialog collects the 
connection information for the Pervasive SQL database. 
Fill in the following fields in the Login/Connection dialog: 
 
 
Database Name 
Select the Pervasive SQL database that contains the tables to import. If the Database Name 
list is empty, you may type in the name. 
See your DBA or your server documentation for information on how the database is specified. 
 
 
DDF Directory 
Press the Browse button to select the pathname or directory containing the database DDF 
files. 
 
 
Database Directory 
Press the Browse button to select the pathname or directory containing the database. 
 
You may specify either the Database Name or the DDF directory, but not both. 
 
 
User Name 
The user login ID for the named database. 
Password 
The user password for the named database. 
 
 
Owner Names 
Optionally, type a comma separated list of names the Pervasive SQL driver tries when opening 
encrypted Btrieve files. If a name contains a comma or space, it must be surrounded by single 
quotes. 
Refresh table list 


---

ReportWriter 
310 
 
 
 
 
Check this box to refresh the list of tables to import when you press the Next > button. Clear  
the box to improve performance when the database is likely to be unchanged between imports. 
Disconnect after Import or Cancel 
Check this box to disconnect from the server after importing the (last) definition. Generally, you 
should clear this box when importing multiple definitions in order to maintain your connection to 
the server between imports. 
Next > 
Press this button to open the Import Wizard‘s Import List dialog. 
 
 
SQL Import Wizard—Import List Dialog 
When you press the Next > button, the Import Wizard opens the Import List dialog. The Import 
List dialog lists the importable items. Highlight the table whose definition to import, then press 
the Finish button to import. The Import Wizard adds the definition to your Clarion Data 
Dictionary, then opens the File Properties dialog to let you modify the default definition. Import 
additional tables by repeating these steps. 


---

APPENDIX C - Database Drivers 
311 
 
 
 
 
TopSpeed Files 
The TopSpeed Database file system is a high-performance, high-security, proprietary file 
driver for Clarion development tools. 
Data tables, keys, indexes and memos can all be stored together in a single file. The default 
file extension is *.TPS. A separate "Transaction Control File" takes the *.TCF extension. 
The TopSpeed driver can optionally store multiple tables in a single DOS file. This allows you 
to open as many data tables, keys, and indexes as necessary using a single DOS file handle. 
This feature may be especially useful when there are a large number of small tables, or when 
a group of related files are normally accessed together. All keys, indexes, and memos are 
stored internally. 
In addition, the TopSpeed file system supports the BLOB data type (Binary Large OBject), a 
field which is completely variable-length and may be greater than 64K in size. A BLOB must be 
declared before the RECORD structure. Memory for a BLOB is dynamically allocated and de- 
allocated as necessary. For more information, see BLOB in the Language Reference. 
TopSpeed database driver: 
## C70TPS.DLL
 
 
 
This driver offers speed, security, and takes up fewer resources on the end user‘s system. 
 
 
Data Types 
## BYTE
## DECIMAL
 
## SHORT
## STRING
 
## USHORT
## CSTRING
 
## LONG
## PSTRING
 
## ULONG
## MEMO
 
## SREAL
## GROUP
 
## REAL
## BLOB
 
 
 
If you do not have the file definition in a Clarion Data Dictionary or Report Library, use the File 
Import Utility in Clarion ReportWriter for Windows to define your files. 
Maximum File Specifications: 
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
Tables per DOS File : Limited only by the maximum DOS file size-- 
approximately 2^32 bytes (4,294,967,296). 
Concurrent Users per File: 1024 


---

 
 
 


---

313 
 
 
APPENDIX D - Glossary 
 
 
All definitions should be considered general terms, except where otherwise indicated. The 
context for definitions marked (Clarion) pertain to the Clarion language or the Clarion 
development environment. Likewise for (SQL), which applies to generalized Structured Query 
Language usage. 
 
access key 
(Clarion) A specified key or index to set the order for processing 
records in a procedure. 
Alias 
An alternate name for a data file, which allows multiple, independent 
operations on it. Clarion provides a separate record buffer for each 
alias, increasing the performance of the separate operations. 
ANSI character 
set 
Character set standardized by the American National Standards 
Institute. Many ANSI characters are different then the corresponding 
ASCII character set. The ANSI set contains more non-English 
characters. The standard Microsoft Windows character set is the ANSI 
character set. 
Append 
Add a record to a data file, usually without updating a key or index. 
Application 
A computer program designed for a specific type of work; the terms 
"application" and "program" are interchangeable. In general, when 
referring to a Windows program, "application" is the preferable term. 
Array 
A ordered series or group of dimensioned values or data items. 
ASCII character 
set 
Character set standardized as the American Standard Code for 
Information Interchange. The standard IBM PC character set. 
assignment 
statement 
A statement placing a value in a variable; for example, A = 6 places the 
value 6 in variable "A." 
auto-increment 
field 
(Clarion) A key field which stores a value which increases with each 
successive record, and is generally not available to the end user. The 
application places the value in the field immediately upon appending 
the record. 
Band 
An element of the report which prints at a specific time. 
binary memo 
(Clarion) A memo field suitable for holding non-ASCII contents, such as 
images. 
Bind 
(Clarion) A statement which allows a variable name to be used in a 
dynamic expression which is assembled and processed at run-time. 
Bitmap 
A binary file representation of a graphic or picture; raster format defines 
the image by absolute pixels. Popular bitmap formats supported by 
Clarion include .BMP, .GIF, .ICO, .PCX, .JPG. Sometimes refers 
specifically to the .BMP file format, an uncompressed, but widely 
supported file format. 
## BLOB
(Binary Large OBject) A variable length field which may exceed the 64K 
limit and is suitable for holding non-ASCII contents, such as images. 
Boolean 
A logical expression which evaluates to true or false, one or zero. 
Border or Line 
Color 
The color designated for the outside line of a graphical control. 


---

314 
ReportWriter 
 
 
 
 
 
break field 
(Clarion) A field or variable monitored when processing a report 
structure. When the value in the field changes while sequentially 
processing records, the print engine processes the next element in the 
report structure (usually the group footer). 
case sensitive 
A characteristic indicating whether a command treats text typed with 
capital (uppercase) letters differently than those typed with lower case, 
or a combination of both. 
case structure 
A control structure which branches execution to a statement (or group 
of statements) based upon a single condition or expression. 
character string 
An alphanumeric data type. 
check box 
A control consisting of a small square or diamond, in which an end user 
indicates a on/off, yes/no, or true/false choice. 
Clarion standard 
date 
(Clarion) The number of days elapsed since December 28, 1800; the 
valid range is from Jan. 1, 1801 through Dec. 31, 2099. 
Click 
To place the mouse pointer on a control or window, then press and 
release the left mouse button. 
Client 
A system attached to a network that accesses shared network 
resources. 
client application 
A program that makes requests of a server application using a defined 
interface such as DDE, RPC, or NetBIOS. 
client server 
architecture 
A network configuration by which linked workstations request services 
from a dedicated program running on a server. 
client server 
networking 
A network architecture in which shared resources are concentrated on 
powerful server machines and the attached desktop systems fulfill the 
role of clients, making requests across the network for centralized 
information. 
Clipboard 
A temporary storage area in memory for holding data, maintained by 
Windows. 
color dialog 
Standard Windows dialog for choosing color. 
Column 
(SQL) Generally refers to a list of database field contents arranged by 
records. 
common file 
dialog 
A standard Windows dialog for displaying drives, directories, and file 
names. 
Concatenate 
Append two string data elements to form a longer string comprised of 
both. 
conditional 
statement 
An IF statement which branches subsequent execution based on a 
logical condition. 
Constant 
A static value. 
control alignment 
The "Snap-To" behavior, as found in the Report Designers, by which 
you may "line up" report elements. 
control properties 
(Clarion) Attributes which determine the appearance and functionality 
of a report control. 
Criteria 
(SQL) An expression containing a condition which limits the records for 
processing. 


---

315 
APPENDIX D - Glossary 
 
 
 
 
current directory 
The default DOS subdirectory, in which Windows or DOS searches for 
files not identified with a fully qualified file name. 
current record 
(Clarion)The current database record in the record buffer. 
Cursor 
The mouse pointer. Changing the cursor "shape" can indicate the type 
of action or selection the end user can effect on a given control or 
window. 
data dictionary 
(Clarion) ASCII file describing the individual data files which comprise 
the database, their structure, keys, relations, and other information 
describing how an application will process the contents of the 
database. 
data file 
Generally, a collection of data elements in an organized format, usually 
arranged by records (rows) and fields (columns). 
data type 
A physical description of the type of storage supported by a variable; 
what sort of values it can hold. 
Database 
A structured collection of data, contained in one or more data files, plus 
the key files and other information which describes the order and 
relations of the data elements. 
Database 
administrator 
(DBA) A person responsible for designing and maintaining a multi-user 
database system. 
database 
definition file 
(*.DDF). A Btrieve file, separate from the data file, containing the 
database structure. Equivalent to the header contained internally in 
most other PC database file formats. 
database design 
The process of planning and describing the most efficient application or 
system for storing and managing data for a specific project. 
database driver 
A collection of functions and procedures contained in a dynamic link 
library, supporting low level access to a specific database file format. 
database integrity 
Under the relational model, database integrity consists of two general 
rules: 
1.Each database file or table must have a primary key serving as a 
unique identifier for all records.2.When a table has a foreign key 
matching the primary key of another table, each value in the foreign key 
must either equal a value in the primary key of the other table, or be 
null. 
dataset 
The dataset name is simply the name we will use to identify our data 
source. As our Report Library grows with new reports, it will be very 
likely that we will have multiple datasets available for different reports. 
When specifying the dataset name you need to avoid special 
characters, such as: whitespace, !, #, %, $, ^, &, *, (, ), -, +, =, \, /, etc. 
dBase format 
PC database file format popularized by dBase III. 
## DBMS
Database Management System: generic term for a program that 
enables a system to perform all the functions associated with managing 
a database. 
Default 
An assumed state or action, which the end user accepts or executes 
with little or no action. 
Delimiter 
A character marking the boundaries of one database field from another. 
dependent entity 
(SQL) A set of data elements dependent on other related entities in the 
database to identify them.. 


---

316 
ReportWriter 
 
 
 
 
desktop 
The screen area in which all windows, dialog boxes, and icons appear. 
DETAIL structure 
(Clarion) The portion of a report structure which usually conveys the 
main data within the printed report. The application loops through, 
updates, and prints the detail band controls with the contents of all the 
records being processed. 
Disabled 
A window, menu, or control visible but prevented from gaining focus. 
double-click 
To press and release the left mouse button twice, quickly. Executes the 
default action on a selection. 
drag 
To press the left mouse button, then move the mouse while continuing 
to hold the button down. Usually a visual cue indicates a process such 
as moving a selected object, or rubber-banding a region. Releasing the 
button completes the action. 
drag and drop 
To select an object in a window or dialog box, press down the left 
mouse button, move the mouse while continuing to hold the button 
down, then release the button when the pointer is on top of another 
object. When drag and drop is supported by the program(s), the action 
generally indicates the dropped object is to be processed in some way 
by the recipient object. 
drop down list 
A list box control which only displays only the current selection when 
closed. When the user opens the list box, it expands to include 
additional choices. 
dynamic link 
library 
(DLL) A library of shared functions that applications link to at run-time, 
as opposed to compile time. 
encryption 
The storage on disk of data in scrambled or encrypted form, such that 
an unauthorized user may not access the data in an intelligible format. 
Excel format 
File format used by the Microsoft Excel spreadsheet application. Note: 
an ODBC driver exists for this format, and is available in the Microsoft 
ODBC 2.0 Software Development Kit. 
exclusive access 
Opening a DOS file so that no other user in a multi-user environment 
may update the same file. 
executable 
A standard .EXE application file capable of being launched by the 
Microsoft Windows shell. 
expression 
A mathematical formula containing any valid combination of variables, 
functions, operators, and constants. 
extension 
A file name suffix; up to three characters in the DOS file system. 
Windows 3.1 matches document files to their application via the 
[Extensions] section in the WIN.INI file. 
external name 
(Clarion)An attribute which holds the native format name (such as a 
DOS file name) for a given data element. ReportWriter refers to the file 
by the Clarion label. 
field 
A basic data element or category which names all the values in a 
column of data within a database file or table. 
file handle 
An operating system pointer to a file. The "FILES=" line in the 
CONFIG.SYS file sets the system limit on the total number of allowable 
open files at one time. 
fill color 
The color designated for the inside of a graphical control. 


---

317 
APPENDIX D - Glossary 
 
 
 
 
filter 
An expression which isolates a subset of records for an operation. 
folder 
A logical container implemented by the shell, within which the user may 
group a collection of items. Analogous to a file directory. 
font 
The family name of related type face files. For example, "Times New 
Roman" is the font name, and "Times New Roman plain," "Times New 
Roman Italic," "Times New Roman Bold," and "Times New Roman Bold 
Italic" are the styles, which are stored in separate files. 
font dialog 
A standard Windows dialog for picking a typeface, style, size, and 
optionally, the text color. 
font style 
Character formatting applied to a font face, such as bold, italic, or bold 
italic. 
foreign key 
(SQL) A key in one table (database file) whose values match the 
primary key of another table. 
form 
A window that displays a single record for editing. By convention there 
is a separate entry box for each field displayed, and fields are stacked 
in a vertical arrangement. 
form letter 
A mail merge document containing "boiler-plate" text, in which controls 
reference fields from which to obtain information when creating letters 
to individuals. 
form report style 
A report format generally containing field labels and values arranged in 
a vertical format. 
Designer 
(Clarion) A specialized window which allows you to visually define the 
formatting for a report in "WYSIWYG" fashion. 
function 
(Clarion) A specialized procedure which returns a value. The function 
declaration may optionally define parameters which are passed when 
calling the function. A function may be used within calculated or 
conditional fields. 
GIF image 
Graphics Interchange File format; an image format popularized by 
CompuServe. Generally acknowledged to offer the best compression 
ration for 256 color or less images. Attention: should you use the word 
"GIF" anywhere within an application or program, you must add a 
trademark notice: "GIF (Graphics Interchange Format) is a trademark of 
CompuServe Information Services." 
grayed 
A visual cue to the user that the window, menu, or control is 
unavailable or disabled. 
grid snap 
A series of coordinates, represented by dots, such as those used by 
the Report Designer, to force controls to exact positioning. 
groupbox 
A rectangular line frame with a label at upper left, used to define related 
controls. 
I-beam 
A special cursor usually indicating the end user can type text into an 
edit control. 
I/O 
Input/Output. The process of moving information into and out of the 
system. 
icon 
A graphical representation of a physical object in the system, such as a 
printer. Also, any small image representing an action, concept or 
program, as when an icon appears on a command button. The normal 
icon file format carries the .ICO extension; one of its main features is 


---

318 
ReportWriter 
 
 
 
 
built-in support for transparency. 
identifier 
A label uniquely identifying a variable or other program element. 
independent 
entity 
(SQL) A set of data elements sharing a set of properties independent of 
other related entities in the database. Independent entities have unique 
identifiers, and therefore, primary keys. 
index file 
An external key file ordered according to the contents of a specified 
field or expression. An index file usually must be manually updated 
when adding, deleting, or changing records. 
INI file 
A Windows Initialization file in ASCII format. The .INI file is divided into 
sections separated by an identifier enclosed in square brackets. 
Variables and their values follow, each pair separated by a carriage 
return, with an equal sign between the variable name and its value. 
Values may be stored as strings or integers. 
insertion point 
The point in a document at which the next characters typed by the end 
user will appear. 
interface 
The communication between the computer and the user; it presents 
information to the user and accepts the user‘s input. 
## ISAM
Indexed Sequential Access Method; a database organization in which 
data files are ordered by keys, and may be retrieved in the sequence of 
the keys. 
join 
A join takes two database files (or tables) and creates a new, wider 
table consisting of all possible concatenated records (or rows). 
JPG image 
A true-color graphics file format featuring 24-bit color storage. It usually 
provides for adjustable lossy compression, which allows for greater 
compression but loss of some resolution. 
key 
An indexed file ordered according to the contents of a specified field or 
fields. Keys are usually dynamically updated whenever the value in a 
key field changes. 
key-in template 
picture 
(Clarion) A formatting option, which restricts and verifies end user 
keyboard input according to a specified character pattern applied upon 
a variable. 
keyboard 
accelerator 
A hot-key combination which directly executes a command. 
label 
(Clarion) A unique identifier for a variable, procedure, function, routine, 
or data structure. 
lock 
A concurrency control mechanism to prevent more than one user from 
updating the same record at the same time. 
locked field or 
record 
A field or record currently being updated by one user within a multi-user 
database, such that an attempt by another user to update the same 
record at the same time will fail. 
logical operator 
A true/false or bitwise comparison of two values; logical operators are: 
=, >, <, <>, >=, <+, NOT, AND, OR, and XOR. 
lookup table or 
lookup file 
A database file on one side of a one to many relation, upon which a 
variable is searched for, and a corresponding field in the related table is 
returned. 
many-to-many 
relationship 
A connection between two data entities in which there may exist many 
corresponding values in the foreign key in one database file or table, to 


---

319 
APPENDIX D - Glossary 
 
 
 
 
many corresponding values in the foreign key of another table. Usually 
implemented via a "join" file breaking them into two 1:Many relations. 
many-to-one 
relationship 
A connection between two data entities in which there may exist many 
corresponding values in the foreign key in one database file or table, to 
only one value in the primary key of another "look-up" table. The 
relationship implicitly describes the direction of the relation. Also called 
a child-parent relation. 
memo 
A free-form, variable length text field, suitable for storing very long 
strings. In most PC file formats, the memo is stored in a file separate 
from the fixed-length database fields. A binary memo field is a 
specialized type of memo field suitable for storing binary information 
such as graphics. 
message box 
A standard windows element, usually consisting of a short message 
string, an OK button, often a standard icon such as "stop" or 
"information." It may optionally contain additional buttons such as 
"Cancel," and "Retry." 
metafile 
In Windows, the representation of a graphic or line art in vector (device 
independent) format; defines the image as a series of lines and curves, 
allowing for smooth resizing. Clarion supports the .WMF (Windows 
Metafile) vector format. The metafile is actually a stored collection of 
the commands which instruct the GDI (Windows Graphics Device 
Interface) to display the graphic on the output device. 
minimize box 
A window control which resizes a window to iconic size, usually at the 
bottom of the desktop, or if a child window, to iconic size, usually at the 
bottom of the application window. 
mnemonic access 
key 
The underlined letter in the command names on Microsoft Windows 
menus. When a user activates a pull down menu, the key executes the 
command. 
multi-user 
database 
A database system designed so that more than one user can access a 
file or record at the same time. The system requires concurrency 
checking so that two users don‘t attempt to update the same record at 
the same time. 
natural join 
(SQL) A join which takes two database files (or tables) and creates a 
new, wider table consisting of all possible concatenated records (or 
rows), where the new table contains two identical columns, one of 
which is dropped. 
nested queries 
(SQL) A single query consisting of both an outer and inner query.  
Allows for more efficient retrieval of data from large tables by combining 
multiple operations into one. 
nesting 
Placing one operation inside another, such as nesting a function within 
another by specifying the nested function as a parameter of the first. 
normalization 
The representation of data entities in their simplest forms, for the 
purpose of quickest access and most efficient storage. The 
normalization process includes the elimination of redundant data 
groups, and the elimination of redundant data elements. 
null value 
A zero or empty value. 
## ODBC
The Open Database Connectivity standard supported by many 
Windows applications. Provides a standard API for accessing multiple 
database file formats via replaceable file drivers, and Client/Server 


---

ReportWriter 
320 
 
 
 
 
support. The ODBC SDK is published by Microsoft. 
## ODBC
Administrator 
A redistributable Microsoft application for adding, maintaining or 
deleting individual ODBC drivers within a system. Usually located in the 
Windows\System directory, the executable file name is 
## ODBCADM..EXE.
ODBC Control 
Panel applet 
A Windows Control Panel interface to the ODBC administrator. 
ODBC driver 
A driver library containing the individual functions supporting standard 
ODBC calls for a particular file format. 
one-to-many 
relationship 
A connection between two data entities in which there may exist one 
corresponding value in the primary key of one database file or table, to 
many identical values in the foreign key of another table. The 
relationship implicitly describes the direction of the relation. For 
example, the relation of states to cities implies a state may have many 
cities. Also called a parent-child relation. 
one-to-one 
relationship 
A connection between two data entities in which there may exist one 
and only one corresponding value in the primary key of one database 
file or table, to a single identical value in the foreign key of another 
table. For example, the relation of customer name to internet address. 
The data is usually split into two separate tables for storage savings; all 
customers have names, but only a minority have internet addresses. 
origin 
The upper left corner of a window or control, expressed in x,y 
coordinates (0,0). 
orphan 
A portion of text or data separated from its complementary preceding 
data by a page break 
outer join 
(SQL) A join which includes all records from one database file, and only 
those records from another in which the values in a selected field (or 
fields) match those in the first. 
overlay 
(Clarion) A variable or field sharing the same location as another. Acts 
as a data "re-declaration, and provides more efficient storage. Most 
useful in "either/or" situations when a variable and its overlay are of 
similar types but use different pictures. 
page footer 
The section of a report composed after the last detail that will fit on a 
page has been composed. 
Page Form 
(Clarion) A report element defined once, when first composing the 
report, then printed on all pages of the report. 
page header 
The section of a report composed before the first detail to print on a 
page. 
page overflow 
In Clarion, the point at which the report library composes enough data  
to complete a page; the library will either send the page to the Windows 
spooler at that point, or first check to verify there are no "widows," if the 
application so specifies. 
palette 
The table of available colors which a given window may user for 
painting. 
parameter 
An argument or optional variable passed to a procedure. 
PCX image 
A standard graphics file format, offering moderate compression, 
originally developed by the Zsoft corporation. The Windows Paintbrush 
accessory supports this format. 


---

APPENDIX D - Glossary 
321 
 
 
 
 
pel 
Equivalent to pixel; abbreviation for picture element. The smallest 
screen unit addressed in graphic mode; a dot. 
picture token 
(Clarion) A formatting string, which specifies a specific "picture" or 
masking format for displaying and editing variables. The picture token 
begins with the "@" character. 
pixel 
Equivalent to pel; abbreviation for picture element. The smallest screen 
unit addressed in graphic mode; a dot. 
point size 
A measurement expressed in points; one point equals 1/72nd inch, or 
1/28 centimeter. 
pointer 
The mouse cursor. Or, an index entry which locates or "points" to the 
corresponding data record. 
popup menu 
A menu that appears disconnected from other visual elements. 
Windows 95 and Clarion frequently displays popup menus when the 
user clicks the right mouse button. By convention, the menu is 
associated with the item clicked on. 
prefix 
(Clarion) A short identifying string for a data structure. Provides a 
method for resolving variable names when, for example, two database 
files include fields whose names are the same. 
primary key 
(SQL) A database field or expression which uniquely identifies each 
record in the table or database file. 
print job 
One complete task sent to the Windows print spooler (accessible from 
Print Manager). 
print structure 
(Clarion) The parts of a report structure, which include the group break 
structure, detail, header, footer, and form. 
printer driver 
An external library file containing low level instructions and functions by 
which the Windows GDI library sends specific commands to the printer. 
printer font 
A typeface resident in the printer‘s RAM. 
progress bar 
A control that displays a graphic representation of a dynamic value by 
progressively coloring in a rectangle as the value changes. 
prompt 
A text label which normally appears near a screen control, to identify 
the control. 
property 
An attribute of a window, control, or other object. 
property list 
A dialog intended to allow the convenient grouping of closely related 
items in a single place. 
query 
(SQL) An operation upon a database table which results in another 
table or subset of the first. 
range constraint 
A bounds for a database operation limiting the operation to a set of 
records for which a given field falls within specified starting and ending 
values. 
## RECORD
(Clarion) A data structure representing one row in a database table. 
referential 
integrity 
The process by which an application "follows through" on an update to 
a key field in one file, to check its related record in another file. This 
maintains valid parent-child relationships within the database. 
relationship 
A logical link between records in data files based upon a duplicate 
(linking) field. 


---

ReportWriter 
322 
 
 
 
 
restore button 
A window control which resizes a window from a maximized state to the 
last size prior to maximizing. 
rich text format 
## (RTF)
A common word processing file format, originally designed for 
transportability between word processing systems across different 
operating systems. The default format for the source document for the 
Windows help file format. 
scope 
A range of records selected for a given operation. Also, the 
"boundaries" beyond which a given variable is unavailable to another 
procedure or function. 
scroll bar 
Standard window control for changing the view of data within a window, 
displaying more of a document or application controls than currently 
visible. 
select 
To indicate to the system that the next command should act upon an on 
screen object, by placing the mouse cursor over it and pressing the left 
mouse button. 
## SELECT
statement 
(SQL) A statement setting the fields and tables for viewing, and for 
subsequent operations. 
sequential access 
The ability to manipulate all the records in a database file or table in the 
sequence defined by the key or index. 
server 
A remote computer providing data storage or services to other linked 
computers. 
## SHARE.EXE
The MS-DOS executable responsible for supporting multi-user access 
to a single file. 
sort 
Physically rearrange all database records in a specified order, and 
store the results in a new database file or table. 
SQL 
Structured Query Language; a database language for maintaining a 
relational database; most often-used in mainframe and client/server 
applications. 
static text 
A window control which displays a string constant, and never receives 
focus; primarily used for labeling other controls or displaying 
information and instructions. 
status bar 
An area of a window, usually found at the bottom, in which the program 
can display prompts and information. 
stream mode 
A special mode for several of the Clarion database drivers which 
optimizes file input/output. 
swap file 
A system file maintained by Windows for maintaining virtual memory as 
required by the system. 
syntax 
A rule specifying the specific format of a language statement. 
system colors 
The default colors shared by all custom Windows palettes. 
system date 
The date maintained by the system clock. 
table 
(SQL) A structured collection of data, consisting of a row of fields or 
column headings plus zero or more rows of data. Each row contains 
exactly one value for each of the fields. Within ReportWriter, the table 
corresponds to a specific FILE structure. 
tabular report 
A listing of data labels and their corresponding values, arranged in a 
row of column labels, followed by additional rows of data arranged by 


---

APPENDIX D - Glossary 
323 
 
 
 
 
column. 
tag 
For file drivers (such as FoxPro and dBase IV) supporting multiple 
indexes within the same index file, the indicator marking an individual 
index. 
text control 
A multi-line edit control which automatically supports word wrap. 
text file 
An ASCII file. 
text justification 
A paragraph alignment style which lines up the edges of the paragraph 
at left, right, left and right, or centers the entire line. 
third normal form 
A test or measure of how closely a database meets relational theory 
tests for data normalization. 
thumb 
The box control on a scroll bar. 
toolbar 
A horizontal or vertically arranged group of command buttons, and/or 
other controls, generally remaining accessible the entire time a 
program executes. 
validity check 
An executable code procedure which checks end user input against an 
expression defining acceptable values for a given field. 
vector font 
A Pervasive typeface, such as a TrueType font. 
vector graphic 
A binary file representation of a graphic or line art; defines the image as 
a series of lines and curves, allowing for smooth resizing. Clarion 
supports the .WMF (Windows Metafile) vector format. 
view 
A virtual file containing selected fields from one or more related 
database files. 
virtual table 
A data table or view which exists in memory only, constructed from one 
or more tables or data files which may exist on disk. 
widow 
A portion of text or data separated from its complementary following 
data by a page break. 
Wizard 
A series of dialogs that guide the user through a process, supplying 
defaults and limiting the user options to only those still available after 
each decision point, thereby controlling and simplifying the process 
from the user‘s perspective. 
X axis 
The horizontal axis. Used for locating controls; the leftmost pixel in a 
window is position zero. 
Y axis 
The vertical axis. Used for locating controls; the upper pixel in a window 
is position zero. 


---

ReportWriter 
324 
 
 
 
 
APPENDIX D - Glossary 
All definitions should be considered general terms, except where otherwise indicated. The 
context for definitions marked (Clarion) pertain to the Clarion language or the Clarion 
development environment. Likewise for (SQL), which applies to generalized Structured Query 
Language usage. 
 
access key 
(Clarion) A specified key or index to set the order for processing 
records in a procedure. 
Alias 
An alternate name for a data file, which allows multiple, independent 
operations on it. Clarion provides a separate record buffer for each 
alias, increasing the performance of the separate operations. 
ANSI character 
set 
Character set standardized by the American National Standards 
Institute. Many ANSI characters are different then the corresponding 
ASCII character set. The ANSI set contains more non-English 
characters. The standard Microsoft Windows character set is the ANSI 
character set. 
Append 
Add a record to a data file, usually without updating a key or index. 
Application 
A computer program designed for a specific type of work; the terms 
"application" and "program" are interchangeable. In general, when 
referring to a Windows program, "application" is the preferable term. 
Array 
A ordered series or group of dimensioned values or data items. 
ASCII character 
set 
Character set standardized as the American Standard Code for 
Information Interchange. The standard IBM PC character set. 
assignment 
statement 
A statement placing a value in a variable; for example, A = 6 places the 
value 6 in variable "A." 
auto-increment 
field 
(Clarion) A key field which stores a value which increases with each 
successive record, and is generally not available to the end user. The 
application places the value in the field immediately upon appending 
the record. 
Band 
An element of the report which prints at a specific time. 
binary memo 
(Clarion) A memo field suitable for holding non-ASCII contents, such as 
images. 
Bind 
(Clarion) A statement which allows a variable name to be used in a 
dynamic expression which is assembled and processed at run-time. 
Bitmap 
A binary file representation of a graphic or picture; raster format defines 
the image by absolute pixels. Popular bitmap formats supported by 
Clarion include .BMP, .GIF, .ICO, .PCX, .JPG. Sometimes refers 
specifically to the .BMP file format, an uncompressed, but widely 
supported file format. 
## BLOB
(Binary Large OBject) A variable length field which may exceed the 64K 
limit and is suitable for holding non-ASCII contents, such as images. 
Boolean 
A logical expression which evaluates to true or false, one or zero. 
Border or Line 
Color 
The color designated for the outside line of a graphical control. 


---

APPENDIX D - Glossary 
325 
 
 
 
 
 
break field 
(Clarion) A field or variable monitored when processing a report 
structure. When the value in the field changes while sequentially 
processing records, the print engine processes the next element in the 
report structure (usually the group footer). 
case sensitive 
A characteristic indicating whether a command treats text typed with 
capital (uppercase) letters differently than those typed with lower case, 
or a combination of both. 
case structure 
A control structure which branches execution to a statement (or group 
of statements) based upon a single condition or expression. 
character string 
An alphanumeric data type. 
check box 
A control consisting of a small square or diamond, in which an end user 
indicates a on/off, yes/no, or true/false choice. 
Clarion standard 
date 
(Clarion) The number of days elapsed since December 28, 1800; the 
valid range is from Jan. 1, 1801 through Dec. 31, 2099. 
Click 
To place the mouse pointer on a control or window, then press and 
release the left mouse button. 
Client 
A system attached to a network that accesses shared network 
resources. 
client application 
A program that makes requests of a server application using a defined 
interface such as DDE, RPC, or NetBIOS. 
client server 
architecture 
A network configuration by which linked workstations request services 
from a dedicated program running on a server. 
client server 
networking 
A network architecture in which shared resources are concentrated on 
powerful server machines and the attached desktop systems fulfill the 
role of clients, making requests across the network for centralized 
information. 
Clipboard 
A temporary storage area in memory for holding data, maintained by 
Windows. 
color dialog 
Standard Windows dialog for choosing color. 
Column 
(SQL) Generally refers to a list of database field contents arranged by 
records. 
common file 
dialog 
A standard Windows dialog for displaying drives, directories, and file 
names. 
Concatenate 
Append two string data elements to form a longer string comprised of 
both. 
conditional 
statement 
An IF statement which branches subsequent execution based on a 
logical condition. 
Constant 
A static value. 
control alignment 
The "Snap-To" behavior, as found in the Report Designers, by which 
you may "line up" report elements. 
control properties 
(Clarion) Attributes which determine the appearance and functionality 
of a report control. 
Criteria 
(SQL) An expression containing a condition which limits the records for 
processing. 


---

ReportWriter 
326 
 
 
 
 
current directory 
The default DOS subdirectory, in which Windows or DOS searches for 
files not identified with a fully qualified file name. 
current record 
(Clarion)The current database record in the record buffer. 
Cursor 
The mouse pointer. Changing the cursor "shape" can indicate the type 
of action or selection the end user can effect on a given control or 
window. 
data dictionary 
(Clarion) ASCII file describing the individual data files which comprise 
the database, their structure, keys, relations, and other information 
describing how an application will process the contents of the 
database. 
data file 
Generally, a collection of data elements in an organized format, usually 
arranged by records (rows) and fields (columns). 
data type 
A physical description of the type of storage supported by a variable; 
what sort of values it can hold. 
Database 
A structured collection of data, contained in one or more data files, plus 
the key files and other information which describes the order and 
relations of the data elements. 
Database 
administrator 
(DBA) A person responsible for designing and maintaining a multi-user 
database system. 
database 
definition file 
(*.DDF). A Btrieve file, separate from the data file, containing the 
database structure. Equivalent to the header contained internally in 
most other PC database file formats. 
database design 
The process of planning and describing the most efficient application or 
system for storing and managing data for a specific project. 
database driver 
A collection of functions and procedures contained in a dynamic link 
library, supporting low level access to a specific database file format. 
database integrity 
Under the relational model, database integrity consists of two general 
rules: 
1.Each database file or table must have a primary key serving as a 
unique identifier for all records.2.When a table has a foreign key 
matching the primary key of another table, each value in the foreign key 
must either equal a value in the primary key of the other table, or be 
null. 
dataset 
The dataset name is simply the name we will use to identify our data 
source. As our Report Library grows with new reports, it will be very 
likely that we will have multiple datasets available for different reports. 
When specifying the dataset name you need to avoid special 
characters, such as: whitespace, !, #, %, $, ^, &, *, (, ), -, +, =, \, /, etc. 
dBase format 
PC database file format popularized by dBase III. 
## DBMS
Database Management System: generic term for a program that 
enables a system to perform all the functions associated with managing 
a database. 
Default 
An assumed state or action, which the end user accepts or executes 
with little or no action. 
Delimiter 
A character marking the boundaries of one database field from another. 
dependent entity 
(SQL) A set of data elements dependent on other related entities in the 
database to identify them.. 


---

APPENDIX D - Glossary 
327 
 
 
 
 
desktop 
The screen area in which all windows, dialog boxes, and icons appear. 
DETAIL structure 
(Clarion) The portion of a report structure which usually conveys the 
main data within the printed report. The application loops through, 
updates, and prints the detail band controls with the contents of all the 
records being processed. 
Disabled 
A window, menu, or control visible but prevented from gaining focus. 
double-click 
To press and release the left mouse button twice, quickly. Executes the 
default action on a selection. 
drag 
To press the left mouse button, then move the mouse while continuing 
to hold the button down. Usually a visual cue indicates a process such 
as moving a selected object, or rubber-banding a region. Releasing the 
button completes the action. 
drag and drop 
To select an object in a window or dialog box, press down the left 
mouse button, move the mouse while continuing to hold the button 
down, then release the button when the pointer is on top of another 
object. When drag and drop is supported by the program(s), the action 
generally indicates the dropped object is to be processed in some way 
by the recipient object. 
drop down list 
A list box control which only displays only the current selection when 
closed. When the user opens the list box, it expands to include 
additional choices. 
dynamic link 
library 
(DLL) A library of shared functions that applications link to at run-time, 
as opposed to compile time. 
encryption 
The storage on disk of data in scrambled or encrypted form, such that 
an unauthorized user may not access the data in an intelligible format. 
Excel format 
File format used by the Microsoft Excel spreadsheet application. Note: 
an ODBC driver exists for this format, and is available in the Microsoft 
ODBC 2.0 Software Development Kit. 
exclusive access 
Opening a DOS file so that no other user in a multi-user environment 
may update the same file. 
executable 
A standard .EXE application file capable of being launched by the 
Microsoft Windows shell. 
expression 
A mathematical formula containing any valid combination of variables, 
functions, operators, and constants. 
extension 
A file name suffix; up to three characters in the DOS file system. 
Windows 3.1 matches document files to their application via the 
[Extensions] section in the WIN.INI file. 
external name 
(Clarion)An attribute which holds the native format name (such as a 
DOS file name) for a given data element. ReportWriter refers to the file 
by the Clarion label. 
field 
A basic data element or category which names all the values in a 
column of data within a database file or table. 
file handle 
An operating system pointer to a file. The "FILES=" line in the 
CONFIG.SYS file sets the system limit on the total number of allowable 
open files at one time. 
fill color 
The color designated for the inside of a graphical control. 


---

ReportWriter 
328 
 
 
 
 
filter 
An expression which isolates a subset of records for an operation. 
folder 
A logical container implemented by the shell, within which the user may 
group a collection of items. Analogous to a file directory. 
font 
The family name of related type face files. For example, "Times New 
Roman" is the font name, and "Times New Roman plain," "Times New 
Roman Italic," "Times New Roman Bold," and "Times New Roman Bold 
Italic" are the styles, which are stored in separate files. 
font dialog 
A standard Windows dialog for picking a typeface, style, size, and 
optionally, the text color. 
font style 
Character formatting applied to a font face, such as bold, italic, or bold 
italic. 
foreign key 
(SQL) A key in one table (database file) whose values match the 
primary key of another table. 
form 
A window that displays a single record for editing. By convention there 
is a separate entry box for each field displayed, and fields are stacked 
in a vertical arrangement. 
form letter 
A mail merge document containing "boiler-plate" text, in which controls 
reference fields from which to obtain information when creating letters 
to individuals. 
form report style 
A report format generally containing field labels and values arranged in 
a vertical format. 
Designer 
(Clarion) A specialized window which allows you to visually define the 
formatting for a report in "WYSIWYG" fashion. 
function 
(Clarion) A specialized procedure which returns a value. The function 
declaration may optionally define parameters which are passed when 
calling the function. A function may be used within calculated or 
conditional fields. 
GIF image 
Graphics Interchange File format; an image format popularized by 
CompuServe. Generally acknowledged to offer the best compression 
ration for 256 color or less images. Attention: should you use the word 
"GIF" anywhere within an application or program, you must add a 
trademark notice: "GIF (Graphics Interchange Format) is a trademark of 
CompuServe Information Services." 
grayed 
A visual cue to the user that the window, menu, or control is 
unavailable or disabled. 
grid snap 
A series of coordinates, represented by dots, such as those used by 
the Report Designer, to force controls to exact positioning. 
groupbox 
A rectangular line frame with a label at upper left, used to define related 
controls. 
I-beam 
A special cursor usually indicating the end user can type text into an 
edit control. 
I/O 
Input/Output. The process of moving information into and out of the 
system. 
icon 
A graphical representation of a physical object in the system, such as a 
printer. Also, any small image representing an action, concept or 
program, as when an icon appears on a command button. The normal 
icon file format carries the .ICO extension; one of its main features is 


---

APPENDIX D - Glossary 
329 
 
 
 
 
built-in support for transparency. 
identifier 
A label uniquely identifying a variable or other program element. 
independent 
entity 
(SQL) A set of data elements sharing a set of properties independent of 
other related entities in the database. Independent entities have unique 
identifiers, and therefore, primary keys. 
index file 
An external key file ordered according to the contents of a specified 
field or expression. An index file usually must be manually updated 
when adding, deleting, or changing records. 
INI file 
A Windows Initialization file in ASCII format. The .INI file is divided into 
sections separated by an identifier enclosed in square brackets. 
Variables and their values follow, each pair separated by a carriage 
return, with an equal sign between the variable name and its value. 
Values may be stored as strings or integers. 
insertion point 
The point in a document at which the next characters typed by the end 
user will appear. 
interface 
The communication between the computer and the user; it presents 
information to the user and accepts the user‘s input. 
## ISAM
Indexed Sequential Access Method; a database organization in which 
data files are ordered by keys, and may be retrieved in the sequence of 
the keys. 
join 
A join takes two database files (or tables) and creates a new, wider 
table consisting of all possible concatenated records (or rows). 
JPG image 
A true-color graphics file format featuring 24-bit color storage. It usually 
provides for adjustable lossy compression, which allows for greater 
compression but loss of some resolution. 
key 
An indexed file ordered according to the contents of a specified field or 
fields. Keys are usually dynamically updated whenever the value in a 
key field changes. 
key-in template 
picture 
(Clarion) A formatting option, which restricts and verifies end user 
keyboard input according to a specified character pattern applied upon 
a variable. 
keyboard 
accelerator 
A hot-key combination which directly executes a command. 
label 
(Clarion) A unique identifier for a variable, procedure, function, routine, 
or data structure. 
lock 
A concurrency control mechanism to prevent more than one user from 
updating the same record at the same time. 
locked field or 
record 
A field or record currently being updated by one user within a multi-user 
database, such that an attempt by another user to update the same 
record at the same time will fail. 
logical operator 
A true/false or bitwise comparison of two values; logical operators are: 
=, >, <, <>, >=, <+, NOT, AND, OR, and XOR. 
lookup table or 
lookup file 
A database file on one side of a one to many relation, upon which a 
variable is searched for, and a corresponding field in the related table is 
returned. 
many-to-many 
relationship 
A connection between two data entities in which there may exist many 
corresponding values in the foreign key in one database file or table, to 


---

ReportWriter 
330 
 
 
 
 
many corresponding values in the foreign key of another table. Usually 
implemented via a "join" file breaking them into two 1:Many relations. 
many-to-one 
relationship 
A connection between two data entities in which there may exist many 
corresponding values in the foreign key in one database file or table, to 
only one value in the primary key of another "look-up" table. The 
relationship implicitly describes the direction of the relation. Also called 
a child-parent relation. 
memo 
A free-form, variable length text field, suitable for storing very long 
strings. In most PC file formats, the memo is stored in a file separate 
from the fixed-length database fields. A binary memo field is a 
specialized type of memo field suitable for storing binary information 
such as graphics. 
message box 
A standard windows element, usually consisting of a short message 
string, an OK button, often a standard icon such as "stop" or 
"information." It may optionally contain additional buttons such as 
"Cancel," and "Retry." 
metafile 
In Windows, the representation of a graphic or line art in vector (device 
independent) format; defines the image as a series of lines and curves, 
allowing for smooth resizing. Clarion supports the .WMF (Windows 
Metafile) vector format. The metafile is actually a stored collection of 
the commands which instruct the GDI (Windows Graphics Device 
Interface) to display the graphic on the output device. 
minimize box 
A window control which resizes a window to iconic size, usually at the 
bottom of the desktop, or if a child window, to iconic size, usually at the 
bottom of the application window. 
mnemonic access 
key 
The underlined letter in the command names on Microsoft Windows 
menus. When a user activates a pull down menu, the key executes the 
command. 
multi-user 
database 
A database system designed so that more than one user can access a 
file or record at the same time. The system requires concurrency 
checking so that two users don‘t attempt to update the same record at 
the same time. 
natural join 
(SQL) A join which takes two database files (or tables) and creates a 
new, wider table consisting of all possible concatenated records (or 
rows), where the new table contains two identical columns, one of 
which is dropped. 
nested queries 
(SQL) A single query consisting of both an outer and inner query.  
Allows for more efficient retrieval of data from large tables by combining 
multiple operations into one. 
nesting 
Placing one operation inside another, such as nesting a function within 
another by specifying the nested function as a parameter of the first. 
normalization 
The representation of data entities in their simplest forms, for the 
purpose of quickest access and most efficient storage. The 
normalization process includes the elimination of redundant data 
groups, and the elimination of redundant data elements. 
null value 
A zero or empty value. 
## ODBC
The Open Database Connectivity standard supported by many 
Windows applications. Provides a standard API for accessing multiple 
database file formats via replaceable file drivers, and Client/Server 


---

APPENDIX D - Glossary 
331 
 
 
 
 
support. The ODBC SDK is published by Microsoft. 
## ODBC
Administrator 
A redistributable Microsoft application for adding, maintaining or 
deleting individual ODBC drivers within a system. Usually located in the 
Windows\System directory, the executable file name is 
## ODBCADM..EXE.
ODBC Control 
Panel applet 
A Windows Control Panel interface to the ODBC administrator. 
ODBC driver 
A driver library containing the individual functions supporting standard 
ODBC calls for a particular file format. 
one-to-many 
relationship 
A connection between two data entities in which there may exist one 
corresponding value in the primary key of one database file or table, to 
many identical values in the foreign key of another table. The 
relationship implicitly describes the direction of the relation. For 
example, the relation of states to cities implies a state may have many 
cities. Also called a parent-child relation. 
one-to-one 
relationship 
A connection between two data entities in which there may exist one 
and only one corresponding value in the primary key of one database 
file or table, to a single identical value in the foreign key of another 
table. For example, the relation of customer name to internet address. 
The data is usually split into two separate tables for storage savings; all 
customers have names, but only a minority have internet addresses. 
origin 
The upper left corner of a window or control, expressed in x,y 
coordinates (0,0). 
orphan 
A portion of text or data separated from its complementary preceding 
data by a page break 
outer join 
(SQL) A join which includes all records from one database file, and only 
those records from another in which the values in a selected field (or 
fields) match those in the first. 
overlay 
(Clarion) A variable or field sharing the same location as another. Acts 
as a data "re-declaration, and provides more efficient storage. Most 
useful in "either/or" situations when a variable and its overlay are of 
similar types but use different pictures. 
page footer 
The section of a report composed after the last detail that will fit on a 
page has been composed. 
Page Form 
(Clarion) A report element defined once, when first composing the 
report, then printed on all pages of the report. 
page header 
The section of a report composed before the first detail to print on a 
page. 
page overflow 
In Clarion, the point at which the report library composes enough data  
to complete a page; the library will either send the page to the Windows 
spooler at that point, or first check to verify there are no "widows," if the 
application so specifies. 
palette 
The table of available colors which a given window may user for 
painting. 
parameter 
An argument or optional variable passed to a procedure. 
PCX image 
A standard graphics file format, offering moderate compression, 
originally developed by the Zsoft corporation. The Windows Paintbrush 
accessory supports this format. 


---

ReportWriter 
332 
 
 
 
 
pel 
Equivalent to pixel; abbreviation for picture element. The smallest 
screen unit addressed in graphic mode; a dot. 
picture token 
(Clarion) A formatting string, which specifies a specific "picture" or 
masking format for displaying and editing variables. The picture token 
begins with the "@" character. 
pixel 
Equivalent to pel; abbreviation for picture element. The smallest screen 
unit addressed in graphic mode; a dot. 
point size 
A measurement expressed in points; one point equals 1/72nd inch, or 
1/28 centimeter. 
pointer 
The mouse cursor. Or, an index entry which locates or "points" to the 
corresponding data record. 
popup menu 
A menu that appears disconnected from other visual elements. 
Windows 95 and Clarion frequently displays popup menus when the 
user clicks the right mouse button. By convention, the menu is 
associated with the item clicked on. 
prefix 
(Clarion) A short identifying string for a data structure. Provides a 
method for resolving variable names when, for example, two database 
files include fields whose names are the same. 
primary key 
(SQL) A database field or expression which uniquely identifies each 
record in the table or database file. 
print job 
One complete task sent to the Windows print spooler (accessible from 
Print Manager). 
print structure 
(Clarion) The parts of a report structure, which include the group break 
structure, detail, header, footer, and form. 
printer driver 
An external library file containing low level instructions and functions by 
which the Windows GDI library sends specific commands to the printer. 
printer font 
A typeface resident in the printer‘s RAM. 
progress bar 
A control that displays a graphic representation of a dynamic value by 
progressively coloring in a rectangle as the value changes. 
prompt 
A text label which normally appears near a screen control, to identify 
the control. 
property 
An attribute of a window, control, or other object. 
property list 
A dialog intended to allow the convenient grouping of closely related 
items in a single place. 
query 
(SQL) An operation upon a database table which results in another 
table or subset of the first. 
range constraint 
A bounds for a database operation limiting the operation to a set of 
records for which a given field falls within specified starting and ending 
values. 
## RECORD
(Clarion) A data structure representing one row in a database table. 
referential 
integrity 
The process by which an application "follows through" on an update to 
a key field in one file, to check its related record in another file. This 
maintains valid parent-child relationships within the database. 
relationship 
A logical link between records in data files based upon a duplicate 
(linking) field. 


---

APPENDIX D - Glossary 
333 
 
 
 
 
restore button 
A window control which resizes a window from a maximized state to the 
last size prior to maximizing. 
rich text format 
## (RTF)
A common word processing file format, originally designed for 
transportability between word processing systems across different 
operating systems. The default format for the source document for the 
Windows help file format. 
scope 
A range of records selected for a given operation. Also, the 
"boundaries" beyond which a given variable is unavailable to another 
procedure or function. 
scroll bar 
Standard window control for changing the view of data within a window, 
displaying more of a document or application controls than currently 
visible. 
select 
To indicate to the system that the next command should act upon an on 
screen object, by placing the mouse cursor over it and pressing the left 
mouse button. 
## SELECT
statement 
(SQL) A statement setting the fields and tables for viewing, and for 
subsequent operations. 
sequential access 
The ability to manipulate all the records in a database file or table in the 
sequence defined by the key or index. 
server 
A remote computer providing data storage or services to other linked 
computers. 
## SHARE.EXE
The MS-DOS executable responsible for supporting multi-user access 
to a single file. 
sort 
Physically rearrange all database records in a specified order, and 
store the results in a new database file or table. 
SQL 
Structured Query Language; a database language for maintaining a 
relational database; most often-used in mainframe and client/server 
applications. 
static text 
A window control which displays a string constant, and never receives 
focus; primarily used for labeling other controls or displaying 
information and instructions. 
status bar 
An area of a window, usually found at the bottom, in which the program 
can display prompts and information. 
stream mode 
A special mode for several of the Clarion database drivers which 
optimizes file input/output. 
swap file 
A system file maintained by Windows for maintaining virtual memory as 
required by the system. 
syntax 
A rule specifying the specific format of a language statement. 
system colors 
The default colors shared by all custom Windows palettes. 
system date 
The date maintained by the system clock. 
table 
(SQL) A structured collection of data, consisting of a row of fields or 
column headings plus zero or more rows of data. Each row contains 
exactly one value for each of the fields. Within ReportWriter, the table 
corresponds to a specific FILE structure. 
tabular report 
A listing of data labels and their corresponding values, arranged in a 
row of column labels, followed by additional rows of data arranged by 


---

ReportWriter 
334 
 
 
 
 
column. 
tag 
For file drivers (such as FoxPro and dBase IV) supporting multiple 
indexes within the same index file, the indicator marking an individual 
index. 
text control 
A multi-line edit control which automatically supports word wrap. 
text file 
An ASCII file. 
text justification 
A paragraph alignment style which lines up the edges of the paragraph 
at left, right, left and right, or centers the entire line. 
third normal form 
A test or measure of how closely a database meets relational theory 
tests for data normalization. 
thumb 
The box control on a scroll bar. 
toolbar 
A horizontal or vertically arranged group of command buttons, and/or 
other controls, generally remaining accessible the entire time a 
program executes. 
validity check 
An executable code procedure which checks end user input against an 
expression defining acceptable values for a given field. 
vector font 
A Pervasive typeface, such as a TrueType font. 
vector graphic 
A binary file representation of a graphic or line art; defines the image as 
a series of lines and curves, allowing for smooth resizing. Clarion 
supports the .WMF (Windows Metafile) vector format. 
view 
A virtual file containing selected fields from one or more related 
database files. 
virtual table 
A data table or view which exists in memory only, constructed from one 
or more tables or data files which may exist on disk. 
widow 
A portion of text or data separated from its complementary following 
data by a page break. 
Wizard 
A series of dialogs that guide the user through a process, supplying 
defaults and limiting the user options to only those still available after 
each decision point, thereby controlling and simplifying the process 
from the user‘s perspective. 
X axis 
The horizontal axis. Used for locating controls; the leftmost pixel in a 
window is position zero. 
Y axis 
The vertical axis. Used for locating controls; the upper pixel in a window 
is position zero. 


---

335 
 
 
 
 
 
Product Information 
Registering This Product 
Technical Support 
In the developer version, your serial number for either Clarion 7 or Clarion.NET is used as your 
registration number. 
 
 
For the stand alone end user version, a serial number is provided for each install. 
 
 
Distribution Policy 
 
 
 
ReportWriter (RepoertWriter.EXE) is not redistributable. Each user must purchase a separate 
copy. 
See the Distributing your Reports topic for details on deploying Report Libraries and the 
necessary supporting files. 


---

336 
ReportWriter 
 
 
 
 
Product Information 
Registering This Product 
In the developer version, your serial number for either Clarion 7 or Clarion.NET is used as your 
registration number. 
 
 
For the stand alone end user version, a serial number is provided for each install. 
 
 
Distribution Policy 
 
 
 
ReportWriter (RepoertWriter.EXE) is not redistributable. Each user must purchase a separate 
copy. 
See the Distributing your Reports topic for details on deploying Report Libraries and the 
necessary supporting files. 


---

337 
Technical Support 
 
 
 
 
System Requirements 
You can run Clarion ReportWriter on any system that meets the minimum system 
requirements for Microsoft Windows. 
In addition, the Microsoft .NET 2.0 runtime is required. (Clarion will install this if it is not 
detected) 


---

338 
ReportWriter 
 
 
 
 
The Install Program 
The Install program, on CD-ROM or via download, decompresses and copies the ReportWriter 
files to your hard drive. 
For all the target operating systems, it provides you with options for installing the various 
components, such as the example files. 
 
 
It also creates Shortcuts on the Start Menu for the ReportWriter environment and 
documentation. 
 
 
Starting the Install 
To start the ReportWriter Install program, simply run the install executable program. A wizard 
with options will be displayed. 
 
 
Install Options 
After starting Setup, you‘ll see a screen displaying a number of options. 
1. Choose the Setup options by checking the boxes for the portions you want to install, 
then press the OK button. 
2. Specify the target drive and directory, then press the OK button. Setup installs the 
main components of ReportWriter to subdirectories below the target directory you 
specify in the dialog. 
 
 
The ReportWriter Setup program installs all files to the target directory and subdirectories 
beneath it. It installs no files to any other directory. 
 
 
During the installation, progress bars display as Setup copies the files. 
 
 
3. Choose Yes or No when Setup asks whether to display the Readme help file. 
4. Press the Finish button when the Install program has completed. 
 
 
 
Starting Clarion ReportWriter: 
 
 
To start ReportWriter: 
 
 
Run ReportWriter from the Program Menu, or locate and run ReportWriter.EXE 
The Clarion ReportWriter environment appears, ready for you to begin work. 


---

339 
Technical Support 
 
 
 
 
Where to Find More Information 
 
 
Important: if any part of the on-line help text conflicts with the printed documentation, 
the on screen help takes precedence. SoftVelocity Inc. makes every reasonable effort to 
ensure the printed documentation is up to date. However, lead-time required by printers may 
create a lag in the documentation; while we can update the help files that ship concurrently 
with a product revision, printed materials must ‗catch up‘ later. 
 
 
Technical Support 
Help can be obtained from several different Internet newsgroups. Our web site, 
www.softvelocity.com, details the available technical support plans. 
 
 
Usenet Newsgroup--comp.lang.clarion 
You can participate in the Clarion Usenet Newsgroup on the Internet--comp.lang.clarion. In this 
newsgroup, Clarion programmers from around the world exchange ideas and techniques. Log 
into your News Server and subscribe to comp.lang.clarion. If your news server does not carry 
the feed, you should contact your Internet provider. 
 
 
SoftVelocity's product newsgroups 
SoftVelocity's internal news server offers newsgroups for all SoftVelocity products. To 
subscribe to these groups use news.softvelocity.com as the news server. There are several 
newsgroups you can subscribe to on this server. 
 
 
SoftVelocity's Web Site: 
You can find other Clarion resources on the Internet by visiting SoftVelocity's site on the World 
Wide Web: 
 
 
http://www.softvelocity.com 
 
 
Paid Technical Support 
Paid telephone technical support is available. Refer to the SoftVelocity web site for the most up 
to date information on the available technical support plans. 


---

ReportWriter 
340 
 
 
 


---

Technical Support 
341 
 
 
 
 
 
 
## ABS  ......................................................... 272
## ACOS  ...................................................... 276
Advanced Controls  .................................. 103 
## AGE  ........................................................ 266
aggregate field  .......................................... 36 
## ALL .......................................................... 279
ANSI character set  .................................. 324 
array  ........................................................ 324 
ASCII character set  ................................. 324 
ASCII Files  .............................................. 291 
## ASIN  ....................................................... 276
assignment statement  ............................. 324 
## ATAN  ...................................................... 276
AttachOpenFile Attach an open file to a 
report  ................................................... 161 
Average  .................................................... 36 
## BAND ...............................................263, 324
BASIC Files  ............................................. 292 
## BEGINSWITH  ......................................... 279
## BFLOAT4  .................................................... 5
## BFLOAT8  .................................................... 5
binary memo  ........................................... 324 
Binding Data to a Report  ......................... 221 
Boolean  ................................................... 324 
## BOR  ........................................................ 263
Border or Line Color  ................................ 324 
Boxes  ...................................................... 245 
## BSHIFT  ................................................... 263
Btrieve Files  ............................................ 293 
## BXOR  ...................................................... 263
## C70PRNT.EXE  ....................................... 213
case sensitive  ......................................... 324 
case structure  ......................................... 324 
## CENTER  ................................................. 279
Changing a Field Picture  ........................... 52 
Changing Connection String of a Data 
Source  ................................................. 233 
Chart using a Dynamic Series ................. 124 
Chart using a Static Series ...................... 133 
Index 
Chart Wizard ........................................... 110 
check box ................................................ 324 
## CHR ........................................................ 279
Clarion Files ............................................ 295 
click ......................................................... 324 
client application ..................................... 324 
client server networking .......................... 324 
## CLIP ........................................................ 279
clipboard ................................................. 324 
Clipper Files ............................................ 296 
## CLOCK .................................................... 266
column .................................................... 324 
Computed Field Creation .......................... 52 
Conditionally Change a Control s 
Appearance ......................................... 227 
## CONTAINS ............................................. 279
control alignment  .................................... 324 
Copying and reusing an Existing Report 232 
## COS ........................................................ 276
Count......................................................... 36 
Creating a Runtime Field adding a report 
parameter ............................................ 235 
criteria  .................................................... 324 
## CSTRING .................................................... 5
currency picture ...................................... 240 
current record  ......................................... 324 
cursor  ..................................................... 324 
data file  ................................................... 324 
data type ..................................................... 5 
database ..................................................... 3 
database design  ..................................... 324 
dataset  ................................................... 324 
## DATE .................................................. 5, 266
Date Notation .......................................... 240 
date pictures............................................ 255 
## DAY  ........................................................ 266
dBase III Files ......................................... 298 
dBase IV Files  ........................................ 300 
## DBMS  ..................................................... 324


---

ReportWriter 
342 
 
 
 
 
## DECIMAL ..................................................... 5
## DEFORMAT ............................................. 279
Deleting a Control ...................................... 52 
Designer .................................................. 324 
Display Values from a Database Bind  
Report Elements to Data ...................... 237 
Distributing your Reports .................211, 213 
Distribution Policy ............................335, 336 
DOS Files ................................................ 302 
double ...................................................... 324 
drag .......................................................... 324 
dynamic link library .................................. 324 
Ellipses .................................................... 245 
## EMPTY .................................................... 271
encryption ................................................ 324 
EndReport Called when the report finishes162 
## ENDSWITH .............................................. 279
Excel format ............................................. 324 
exclusive access ...................................... 324 
ExportCSV Export report to a CSV file .... 189 
ExportHTML Export report to an HTML file190 
ExportImage Export report to an image file191 
ExportMht Export report to MHT file ........ 192 
ExportPDF Export report to PDF ............. 193 
ExportPDF Export to PDF with user    
options .................................................. 194 
ExportRTF Export report to a RTF file ..... 196 
ExportText Export report to Text.............. 197 
ExportXls Export report to XLS format ..... 198 
Expression Editor ....................................... 21 
extension ................................................. 324 
External Functions Editor ........................... 23 
external name .......................................... 324 
Features Summary ...................................... 1 
field ......................................................3, 324 
file ................................................................ 3 
File Drivers...........................................4, 213 
file formats ................................................... 4 
FilterString Editor ....................................... 24 
font dialog ................................................ 324 
font style .................................................. 324 
form .......................................................... 324 
form report style ...................................... 324 
## FORMAT ................................................. 279
FoxBase Files ......................................... 303 
GetNextPageNumber ............................. 182 
GetNextPageNumber Get the next page 
number for report ................................. 163 
GetOpenMode Get how the data files will 
be opened ........................................... 164 
GetReportList Extract Reports in Active 
Library ................................................. 187 
GetReportList Extract Reports in Library 199 
GIF image ............................................... 324 
grayed ..................................................... 324 
## GROUP ....................................................... 5
Group and Sort ......................................... 20 
## I 324
identifier................................................... 324 
Importing Legacy Reports ....................... 231 
index............................................................ 7 
Initialization File ...................................... 213 
## INRANGE ................................................ 272
insertion point .......................................... 324 
## INSTRING ............................................... 279
## INT .......................................................... 272
interface .................................................. 324 
## ISAM ....................................................... 324
Key .............................................. 7, 240, 260 
keyboard accelerator .............................. 324 
Label Definition ......................................... 79 
## LEFT ....................................................... 279
Legacy Reports ....................................... 231 
## LEN ......................................................... 279
Lines........................................................ 245 
LoadLibrary Load Report Library ............ 200 
LoadReportLibrary .......................... 149, 182 
## LOG10 .................................................... 272
## LOGE ...................................................... 272
## LONG .......................................................... 5
## LOWER ................................................... 279
mailing labels ............................................ 79 
Many ......................................................... 10 
Max ........................................................... 36 


---

343 
Index 
 
 
## MEMORY  ................................................ 270
Menu Command Summary ........................ 14 
message box  ........................................... 324 
Min ............................................................. 36 
minimize box  ........................................... 324 
## MONTH .................................................... 266
Multi ...................................................79, 324 
nested queries  ........................................ 324 
nesting  .................................................... 324 
Next Get the next record.......................... 165 
normalization  .......................................... 324 
null value  ................................................. 324 
## NUMERIC ................................................ 279
numeric pictures ...................................... 252 
## ODBC ...................................................... 305
ODBC Administrator  ............................... 324 
One ....................................................10, 324 
origin  ....................................................... 324 
outer join  ................................................. 324 
page footer  .............................................. 324 
page header  ............................................ 324 
palette  ..................................................... 324 
## PATH ....................................................... 270
Pattern picture ......................................... 240 
pattern pictures ........................................ 259 
## PDECIMAL  ................................................. 5
pel  ........................................................... 324 
pictur  ....................................................... 324 
## PICTURE ..................................................... 5
Picture Editor ........................................... 240 
Pivot Grid Control .................................... 103 
pointer  ..................................................... 324 
popup menu  ............................................ 324 
prefix  ....................................................... 324 
PreviewReport Open Report into 
Previewer ............................................. 202 
Print Engine ............................................. 213 
print job  ................................................... 324 
print structure  .......................................... 324 
PrintAction Perform the print .................... 166 
printer driver  ............................................ 324 
 
 
PrintHook Method called when printing a 
report ................................................... 167 
PrintReport .............................................. 182 
PrintReport print a report ........................ 150 
PrintReport Send Report to Printer ......... 203 
PrintReportWithDialog Send Report with 
Printer Dialog ....................................... 204 
Programmer s Interface to Clarion for 
Windows .............................................. 144 
progress bar ............................................ 324 
prompt ..................................................... 324 
Property List ............................................ 324 
## PSTRING .................................................... 5
query ....................................................... 324 
Quick Start .......................................... 39, 40 
## RANDOM ................................................ 272
range constraint ...................................... 324 
Range Limits ............................................... 7 
ReadReportLibrary Read a Report Library 
into buffer ............................................ 169 
## REAL ........................................................... 5
## RECORD ................................................ 324
Relationships ............................................ 10 
Report - Copy .......................................... 232 
Report Designer ........................................ 33 
Report Writer Scripting ............................ 209 
ReportPreviewer Methods ...................... 148 
Reports Wizard ......................................... 93 
Reports Wizard - Choose Columns .......... 94 
Reports Wizard - Create a New Dataset .. 94 
Reports Wizard - Edit Paths...................... 96 
Reports Wizard - File Schematic .............. 95 
Reports Wizard - Grouping Levels ............ 97 
Reports Wizard - Report Layout ............... 98 
Reports Wizard - Report Title and Finish 101 
Reports Wizard - Styles .......................... 102 
Reset Resets the view to the start .......... 171 
ResolveVariableFilename Specify value for  
a variable filename .............................. 172 
rich text format RTF ................................ 324 
## RIGHT ..................................................... 279
## ROUND ................................................... 272
Runtime Print Engine .............................. 213 


---

344 
ReportWriter 
 
 
 
 
Scalable SQL  .......................................... 309 
Scientific Notation  ................................... 240 
scientific notation picture  ......................... 254 
Scripting  .................................................. 209 
sequential access  ................................... 324 
server  ...................................................... 324 
SetNextPageNumber  .............................. 182 
SetNextPageNumber Set the next page 
number for report  ................................. 173 
SetNumberOfCopies  ............................... 182 
SetNumberOfCopies Set number of copies 
to print for report  .................................. 174 
SetOpenMode Set how the data files will 
be opened  ........................................... 175 
SetOrder Set Report Sort Order .............. 205 
SetPageRange  ....................................... 182 
SetPageRange Set range of pages for  
report  ................................................... 176 
SetParameter Set Report Parameter  ...... 206 
SetPreview  .............................................. 182 
SetPreview Set report s preview on or off151 
SetPrinter  ................................................ 182 
SetPrinter Set printer for report  ............... 152 
SetReportFilter  ........................................ 182 
SetReportFilter Set Report Filter  ............. 207 
SetReportOrder  ...................................... 182 
SetVariable  ............................................. 182 
SetVariable Set a value to a runtime  
variable  ................................................ 156 
Shapes  .................................................... 245 
## SHARE.EXE  ........................................... 324
Shipping Examples ..........................247, 249 
## SHORT  ....................................................... 5
## SIN  .......................................................... 276
Sorting Reports  ......................................... 20 
## SQL  ......................................................... 309
## SQRT  ...................................................... 272
## SREAL  ........................................................ 5
status bar  ................................................ 324 
stream mode  .......................................... 324 
## STRING ...................................................... 5
string pictures .......................................... 262 
## SUB ......................................................... 279
Subreport Control  ................................... 140 
Sum ........................................................... 36 
Suppressing a line when empty  ............. 246 
swap file  ................................................. 324 
syntax  ..................................................... 324 
system colors  ......................................... 324 
tag  .......................................................... 324 
## TAN ......................................................... 276
Technical Support  .................................. 339 
text file ..................................................... 324 
text justification ....................................... 324 
## TIME ........................................................... 5
Time Notation  ......................................... 240 
time pictures  ........................................... 257 
## TODAY  ................................................... 266
TopSpeed Files  ...................................... 311 
Total Fields................................................ 36 
Total Types ............................................... 36 
TXR Reports ........................................... 231 
## ULONG ........................................................ 5
UnloadReportLibrary  .............................. 182 
UnloadReportLibrary Unload a 
ReportWriter Report Library ................ 157 
## UPPER  ................................................... 279
UsePrinterDialog Open Printer Dialog .... 188 
## USHORT ..................................................... 5
Using the Pivot Grid Control ................... 106 
## VAL  ........................................................ 279
vector font  .............................................. 324 
view  ........................................................ 324 
virtual table  ............................................. 324 
widow  ..................................................... 324 
## YEAR ...................................................... 266
