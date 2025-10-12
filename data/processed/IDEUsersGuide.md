IDE User's Guide 
 
 
 
 
 
2 


---

COPYRIGHT SoftVelocity Inc.. All rights reserved. 
This publication is protected by copyright and all rights are reserved by SoftVelocity Inc.. It may not, in whole or part, be 
copied, photocopied, reproduced, translated, or reduced to any electronic medium or machine-readable form without prior 
consent, in writing, from SoftVelocity Inc.. 
This  publication supports Clarion. 
It  is  possible  that  it  may contain  technical  or typographical errors. 
SoftVelocity 
Inc. provides this publication ―as is,‖ without warranty of any kind, either expressed or implied. 
 
 
 
 
 
 
 
 
SoftVelocity Inc. 
www.softvelocity.com 
 
 
 
 
 
 
 
Trademark Acknowledgements: 
 
 
SoftVelocity is a trademark of SoftVelocity Inc.. 
Clarion™ is a trademark of SoftVelocity Inc.. 
Microsoft®, Windows®, and Visual Basic® are registered trademarks of Microsoft Corporation. 
All other products and company names are trademarks of their respective owners. 
 
 
 
 
 
 
 
 
 
Printed in the United States of America (0409) 


---

IDE User's Guide 
Table Of Contents 
 
 
Table Of Contents 
IDE User's Guide 
1 
Using this Guide ...................................................................................................................................... 1 
Environment Overview 
3 
Dictionary Editor ...................................................................................................................................... 4 
Application Generator .............................................................................................................................. 5 
Template Registry .................................................................................................................................... 6 
Database Driver Registry ........................................................................................................................ 7 
Dictionary Synchronizer Registry............................................................................................................. 8 
Editors and Designers ............................................................................................................................. 9 
Formula Editor .......................................................................................................................................11 
Structure Designer (Windows) ...............................................................................................................12 
Text Editor .............................................................................................................................................14 
The Dictionary 
15 
The Basics of Database Design ...................................................................................................................15 
Clarion's support of Database Design ..........................................................................................................17 
Dictionary Editor 
28 
Lesson 1 - Data Import .................................................................................................................................29 
Lesson 2 - Table Properties .........................................................................................................................31 
Lesson 3 - Column Properties ......................................................................................................................33 
Lesson 4 - Key and Index Properties ...........................................................................................................37 
Lesson 5 - Adding Relationships ..................................................................................................................40 
Lesson 6 - Trigger Properties. ......................................................................................................................42 
Lesson 7 - Dictionary Synchronization .........................................................................................................44 
Lesson 8 - Advanced Features of the Dictionary Editor ...............................................................................60 
Windows Design Issues 
62 
Design Principles .........................................................................................................................................62 
Event Driven Programming ..........................................................................................................................64 
Windows ....................................................................................................................................................... 66 
Window Elements.........................................................................................................................................68 
Menus ........................................................................................................................................................... 72 
Color ............................................................................................................................................................. 76 
The Application 
78 
Application Generator ..................................................................................................................................78 
Lesson 1 - Anatomy of an Application ..........................................................................................................80 
Lesson 2 - The power of the Application Wizards ........................................................................................88 
Application Wizard .................................................................................................................................89 
Procedure Wizards ................................................................................................................................92 
Form Wizard ..........................................................................................................................................94 
Report Wizard ........................................................................................................................................97 
Report Label Wizard ..............................................................................................................................99 
Process Wizard. ...................................................................................................................................101 
Window Wizard ....................................................................................................................................102 
Theme Maintenance ............................................................................................................................103 
Lesson 3 - The Application Generator Environment ..................................................................................104 
Lesson 4 - The Window Designer and Control Properties ......................................................................... 112 
Interactive Controls ..............................................................................................................................136 
Non-Interactive Controls ......................................................................................................................139 
Lesson 5 - Exploring the Menu/Frame Procedure .....................................................................................141 
Menu Editor .........................................................................................................................................141 
4 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
iii 


---

Toolbars .............................................................................................................................................. 152 
Lesson 6 - Exploring the Browse Procedure ............................................................................................. 154 
Creating List Boxes ............................................................................................................................. 154 
Lesson 7 - Exploring the Form (Update) Procedure .................................................................................. 158 
Lesson 8 - The Report Designer ............................................................................................................... 160 
Report Designer Interface ................................................................................................................... 160 
Report Properties ................................................................................................................................ 163 
Lesson 9 - Exploring the Report Procedure .............................................................................................. 168 
Common Reporting Tasks .................................................................................................................. 168 
Lesson 10 - Procedure Basics ................................................................................................................... 191 
Lesson 11 - Global Application Properties ................................................................................................ 199 
Lesson 12 - Advanced Features of the Application Generator .................................................................. 201 
Lesson 13 - Customizing the Application: Adding Templates ................................................................... 208 
Lesson 14 - The Source Procedure ........................................................................................................... 212 
Lesson 15 - Customizing the Application: Source Embeds ....................................................................... 213 
Lesson 16 - SQL, ODBC and ADO application support ............................................................................ 219 
Project System 
222 
Hand Coded Projects................................................................................................................................. 223 
Component Files ....................................................................................................................................... 227 
The Target File .......................................................................................................................................... 230 
Distributing Files ........................................................................................................................................ 232 
Writing Clarion Code 
236 
Source/Text Editor ..................................................................................................................................... 236 
Formula Editor 
252 
Development and Deployment Strategies 
256 
Overview—EXEs, .LIBs, and .DLLs .......................................................................................................... 256 
Multi-Programmer Development ................................................................................................................ 257 
Procedure Oriented Approach ............................................................................................................ 258 
Module Oriented Approach ................................................................................................................. 259 
Sub-Application Approach .................................................................................................................. 260 
One-Piece EXEs ........................................................................................................................................ 264 
EXE Plus DLLs .......................................................................................................................................... 267 
Hiding the Clarion Run-time Library .................................................................................................... 270 
The Debugger 
274 
Using the Clarion Debugger ...................................................................................................................... 274 
Debugger Lesson ...................................................................................................................................... 277 
Debugger Options ..................................................................................................................................... 287 
Debugger Windows ............................................................................................................................. 289 
Index 
294 


---

 


---

5 
 
IDE User's Guide 
Welcome to the Clarion IDE User‘s Guide! This document is a complete reference to the static (non-template) parts of the 
Clarion development environment. 
Once you‘ve become familiar with the Clarion development environment, through the various lessons included, you can 
refer back to the IDE User‘s Guide for complete in-depth information at any time. 
This document describes important aspects of each major component of the development environment from the Data 
Dictionary Editor to the Debugger; it also includes source code examples and a Debugger lesson. In addition, it includes 
several topics addressing various concepts and tools that are important to Windows programming and application 
development in general. 
Although to some extent the IDE User‘s Guide contents tracks the development environment‘s user interface, it also 
suggests a rough, but not mandatory, sequence of tasks with which to approach application development. When you want 
more information on how to accomplish a specific programming task we recommend using the index to find task-specific 
information. 
Please refer to the main online help and associated PDFs for complete information on the templates, and the ABC Library 
Reference for documentation regarding the Application Builder Class Library. Please refer to the Database Drivers help 
and PDF for complete information on the database drivers that come with this product. Please refer to the Language 
Reference help topics and PDF for complete information on Clarion language syntax and related examples. And don‘t 
forget to make liberal use of the rest of the extensive on-line help topics. 
 
 
Using this Guide 
There are example data files, dictionaries, and applications used throughout this document. Unless otherwise stated, 
these files can be found in the Clarion 7 install‘s \Lessons folder. 
At some point in the document, references and links will be made to the IDE‘s main Help file. You will be able to view all 
topics from there, and even navigate to additional topics if you wish. 
 
 
Conventions Used in this Help Document 
Paragraph text marked in BOLD indicate an IDE button or prompt text. 
 
 
Paragraph text marked in ITALICS indicate the title of an IDE dialog window, or information that you need to enter in a 
specific lesson step. 
 
 
This font indicates a source code example. 


---

10 
IDE User's Guide 
 
 
 


---



---

IDE User's Guide 
3 
 
 
 
Environment Overview 
 
 
 
 
 
The Clarion IDE (integrated development environment) is comprised of several components that assist in each step of the 
development process. 


---

User's Guide and Lessons 
4 
 
 
Dictionary Editor 
The Dictionary Editor is the starting point for beginning a new application. It is used to define your data files and business 
rules for those tables. 
 
 
 
## KEY FEATURES OF THE DICTIONARY EDITOR:
• 
Used to define the characteristics of the data that a program (or programs) will access. 
• 
File, field, key, and relationship information are defined and stored in Dictionary (.DCT) files. 
• 
A file should be defined in a dictionary for best integration with the Application Generator design process. 
 
 
Many options set up in the dictionary file determine how the Application Generator, templates, and wizards process your 
files in your applications. 


---

IDE User's Guide 
5 
 
 
Application Generator 
The Application Generator is the heart of the Clarion IDE, and is used to define the functionality of your application, and to 
then generate the code for it. 
 
 
 
 
## KEY POINTS OF THE APPLICATION GENERATOR:
• 
Used to create Windows applications. 
• 
Procedures are logically connected to other procedures and visually displayed in a tree format. 
• 
Stores procedure characteristics in Application (.APP) files. 
• 
Generates the source code for your application, which is subsequently compiled when the application needs to be 
tested or distributed. 


---

User's Guide and Lessons 
6 
 
 
Template Registry 
Registries provide the Clarion environment with the necessary file information that several of the major components need. 
This allows you to tailor the types of tools that you frequently use for application development. 
The Template Registry (Tools  Edit Template Registry) allows you to register 3rd party templates or modify/customize 
the existing Clarion default templates. Templates are the building blocks of the Application Generator. They provide much 
of the design options you will see in the applications that you create, and also generate solid source code which is used to 
build your target executables and libraries. 
 
 


---

IDE User's Guide 
7 
 
 
Database Driver Registry 
The Database Driver Registry (Tools  Register File Drivers) allows you to register the types of data tables that may be 
accessed by programs you create. You can set your system to only focus on the table types that are important to you. 
 
 


---

User's Guide and Lessons 
8 
 
 
Dictionary Synchronizer Registry 
The Dictionary Synchronizer Registry (Tools  Register Database Systems) is used to register special SQL, ODBC, and 
ADO drivers with the Synchronizer Utility. Again, you can set your system to only focus on the table types that are 
important to you. 
 
 


---

IDE User's Guide 
9 
 
 
Editors and Designers 
The Application Generator also contains two integrated code editors and two special window and report Designers 
designed to help you fine-tune your applications faster and easier. 
 
 
Source Editor 
As you progress in your usage of the Clarion IDE, you will soon discover that there is a very powerful language that is the 
foundation of all of your applications. Often, you will want to use this language to extend and enhance the type of 
applications that you create. 
Clarion provides several powerful methods for embedding source code. There are advantages to each of these methods 
as noted below: 
• 
The Embeditor (choose Source from the popup menu) lets you see the embedded source code within the context 
of the surrounding generated code and gives you the full power of the Text Editor, including text search and 
replace, copy and paste, the Populate Fields toolbox, and File Import. 
 
 
 
 
• 
The Embedded Source dialog (choose Embeds from the popup menu) lets you see only the embed points and 
their code, without the surrounding code. It gives you the full power of the Text Editor, plus a locator to find embed 
points, plus tools for moving and copying entire embed points with multiple blocks of embedded code, and for 
generating embedded code with Code templates. 


---

User's Guide and Lessons 
10
 
 
 
 
 
 
• 
The Embeds button for a control (choose Embeds from the Window Designer‘s popup menu) gives you the 
power of the Embedded Source dialog focused on the embed points for a single control. 
Source code embedded with the Embeditor is fully accessible with the Embedded Source dialog and vice versa, with the 
exception of Code templates, which are only modifiable with the Embedded Source dialog. 


---

IDE User's Guide 
11 
 
 
Formula Editor 
The Formula Editor helps you to quickly generate statements or structures that assign a value to a variable. You can use 
the Formula Editor to create unconditional or conditional assignments. 
An unconditional assignment assigns the evaluation of an expression to the variable you specify: variable = expression. 
For example, a variable called GrossPrice might receive the result of adding two variables called BasePrice and Tax. 
A conditional assignment places multiple possible assignments within a structure that executes only one of them. The 
Formula Editor builds IF structures and CASE structures for this purpose. The assignment statement executed depends 
on the evaluation of the IF or CASE condition. For example, a conditional variable called "Tax" could equal 0 when 
"Taxable" (the IF condition) evaluates as false, or "Tax" could equal Price times TaxRate if "Taxable" is true. 
The Formula Editor dialog provides access to data dictionary columns , as well as global and local memory variables, and 
helps you create syntactically correct expressions. This is its prime advantage: automatic syntax checking. 
To create an expression, you press buttons to add expression components to the Statement line. You can also enter your 
expression then check the syntax upon completion. 


---

User's Guide and Lessons 
12
 
 
Structure Designer (Windows) 
Typically, your applications you create will be using many windows to give your users visual interaction with you data. 
Choosing the window type is only just the beginning. The Window Designer provides a rich assortment of visual tools and 
menus to help you create and edit your window. 
The Window Designer lets you directly manipulate the window and the controls inside it. The sample window, for example, 
contains ‗handles‘—tiny boxes located at the corners and sides of the window. By selecting a handle and dragging the 
mouse, you may resize the sample window. The window the user sees when your application runs is the same size as the 
window you create by dragging. 
When the Window Designer generates the source code for the window, it places the data determining the size and 
position of the window (as you specified by dragging the mouse) in the AT attribute of the statement declaring the window. 
Similarly, the Window Designer supplies the other attributes by presenting you with options, check boxes and fields in 
which you specify your design preferences. 
 
Structure Designer (Reports) 
Using the Report Designer, you visually lay out your application‘s reports. The Report Designer automatically generates 
and places all the code structures necessary to produce the reports. Preview the reports without actually generating any 
code or data. 


---

IDE User's Guide 
13 
 
 
 
 
 
 
This chapter provides an overview of Clarion‘s page oriented print engine, and a comprehensive treatment of each feature 
of the Report Designer. 
Clarion has many powerful reporting features and we want to systematically cover all of them. However, you the 
developer, probably have a particular report you need to produce by yesterday! To read about those features that will help 
you produce your particular report right now, see the Report Designer chapter. 


---

User's Guide and Lessons 
14
 
 
Text Editor 
The text editor is used to create or modify Clarion source code and other ASCII files. From the New, Open or Start Page 
lists, selecting the Source file types accesses the text editor. 
## KEY FEATURES OF THE TEXT EDITOR:
• 
Primarily used to create or modify Clarion source code (.CLW) files. 
• 
Includes built-in visual Window and Report Designers. 
• 
When used within the Application Generator, the Window and Report Designers also allow access to a data 
dictionary. 
• 
Accessed by selecting the File > New > File or File > Open > File menu options, or simply double clicking on any 
source file in the Projects View (just to name a few). 
• 
Also accessed by the Application Generator to create embedded source code for an application and by the 
compiler in the event of compile errors. 
• 
Also accessed by a RIGHT-CLICK on a selected application‘s procedure and choosing Module from the pop-up 
menu. 
 
 
 
Project System 
Before an application can be tested, it must first be compiled and then linked to an executable file format (.EXE). The 
Project Menu and Properties contains a variety of options that determine the type and style of compile and link. 
Projects are required for the compilation of a program. Every application created in the Application Generator contains an 
associated project contained in a solution. Solutions can contain multiple projects and applications. 
Only one solution file may be active at any given time. The complete elements of every solution is displayed in the 
Solution Explorer. 
Project Options contained in the Properties dialog will be discussed in detail in a later topic. 
 
 


---

IDE User's Guide 
15 
 
 
 
The Dictionary 
The Basics of Database Design 
 
Overview: 
This lesson describes relational database concepts. The purpose of this lesson is to familiarize you with the meaning of 
certain terms commonly used when creating database applications. 
Objectives: 
At the completion of this lesson, you should: 
• 
Understand the concept of files, records, and fields. 
• 
Understand the concept of keys. 
• 
Understand the common types of file relationships. 
Introduction 
This Lesson is a review of relational database theory. For a more complete discussion of Relational Database theory and 
design, see Clarion's support of Database Design. 
 
 
Anatomy of a Data File 
A data file is an ordered set of information organized into a single storage entity containing multiple entries called records. 
In SQL databases, a file may also be referred to as a table. This terminology is used interchangeably throughout the 
Clarion Environment. 
Records 
Records are an entire set of information in a data file related to a single item or entry in the file. Data files contain many 
items or records. In SQL databases, a record may also be referred to as a row. 
Fields 
Fields are individual pieces of information contained within a single record of a data file. In SQL databases, a field may 
also be referred to as a column. 
Keys 
Keys are file structures that provide ordered access of records based on the contents a specified field or fields. Keys are 
dynamically updated whenever the value in a key field changes. 
 
 
 
File Relationships 
Relational Databases allow data to be organized into multiple files that are related to each other. In a relational database, 
files are linked together through a logical relationship formed by matching values. A common field maintains the 
relationships between the files. Key files are built for the common fields that allow the program to rapidly access the 
related records when requested. The following example illustrates files organized in a relational database. 
 
 
One to Many Relationships 
This is often called a Parent/Child relationship and is the most common relationship found in relational databases. For 
every record in a primary file, there can be one or more (i.e., many) matching records found in the related file. For 
example, in a Contact Manager program, one Contact may have many phone numbers. 


---

User's Guide and Lessons 
16
 
 
Many to Many Relationships 
A many to many relationship exists when many records in the primary file can point to many records in the secondary file. 
Conversely, many records in the secondary file point to many records in the primary file. 
 
 
One to One Relationships 
This type of relationship is when there can be one and only one matching record found in the related file. This type of 
relationship can be used to store a large number of fields that are not necessarily used in most records, thus saving 
storage space. 


---

IDE User's Guide 
17 
 
 
 
Clarion's support of Database Design 
There are a number of methods of database organization in use today. The Inverted List Model, the Hierarchical Model, 
and the Network Model are three that have been widely used in the past. Mostly, these models have been used on 
mainframe computers, and have not been implemented on PC systems on a widespread basis. The Clarion language has 
the tools to allow you to utilize any of these methods, if you so choose. 
By far, the most common method of database organization on PC systems today is the Relational Model, as defined by E. 
F. Codd. There is no database program that completely implements all of Codd‘s rules regarding relational database, 
because it is an extremely complex mathematical model. However, most database programs implement a sufficient sub- 
set of Codd‘s rules to allow practical use of the principles of the Relational Model. This essay is a very brief overview of 
the most fundamental aspects of relational database design as they impact business programming. 
 
 
Relational Database Design 
One basic principle of Relational Database involves the database design—a data item should be stored once—not 
duplicated in many places. There are two benefits to this: lowered disk space requirements, and easier data maintenance. 
To achieve this end, a relational database design splits the data into separate, related entities called tables. For example, 
assume a very simple order-entry system that needs to store the following data: 
Customer Name 
Customer Address 
ShipTo Address 
Order Date 
Product Ordered 
Quantity Ordered 
Unit Price 
This data could all be stored in each record of one table, but that would be very inefficient. The Customer Name, Address, 
ShipTo Address, and Order Date would be duplicated for every item ordered on every order. To eliminate the duplication, 
split the data into separate tables. 
 
 
Customer Table: 
Customer Name 
 
Customer Address 
 
Order Table: 
ShipTo Address 
Order Date 
Item  Table: 
Product Ordered 
Quantity Ordered 
Unit Price 
 
With this table configuration, the Customer Table contains all the customer information, the Order Table contains all the 
information that is pertinent to one order, and the Item Table contains all the information for each item in the order. This 
certainly eliminates duplicate data. However, how do you tell which record in what table relates to what other records in 
which other tables? This is the purpose of the relational terms "Primary Key" and "Foreign Key." 


---

User's Guide and Lessons 
18
 
 
 
A Primary Key is an index into a table based on a field (or fields) that cannot contain duplicate or null values. To translate 
this to Clarion language terms: a Primary Key would be a unique KEY (no DUP attribute) with key components that are all 
REQuired fields for data entry. In strict relational database design, one Primary Key is required for every table. 
A Foreign Key is an index into a table based on a field (or fields) which contain values that duplicate the values contained 
in the Primary Key fields of another, related, table. To re-state this, a Foreign Key contains a "reference" to the Primary 
Key of another table. 
Primary Keys and Foreign Keys form the basis of table relationships in Relational Database. The matching values 
contained in the Primary and Foreign Keys are the "pointers" to the related records. The Foreign Key records in "Table A" 
point back to the Primary Key record in "Table B", and the Primary Key in "Table B" points to the Foreign Key records in 
"Table A." 
Defining the Primary and Foreign Keys for the above example requires that you add some fields to the tables to fulfill the 
relational requirements. 
 
 
Customer Table: 
Customer Number – Primary Key 
 
Customer Name 
Customer Address 
 
 
Order Table: 
Order Number - Primary Key 
 
Customer Number - Foreign Key 
ShipTo Address 
Order Date 
 
 
 
Item Table: 
Order Number - 1st Primary Key Component and Foreign Key 
Product Ordered - 2nd Primary Key Component 
Quantity Ordered 
Unit Price 
 
In the Customer Table, there is no guarantee that there could not be duplicate Customer Names. Therefore, the 
Customer Number field is added to become the Primary Key. The Order Number has been added to the Order Table 
as the Primary Key because there is no other field that is absolutely unique in that table. The Customer Number was 
also added as a Foreign Key to relate the Order Table to the Customer Table. The Item Table now contains the Order 
Number as a Foreign Key to relate to the Order Table. It also becomes the first component of the multiple component 
(Order Number, Product Ordered) Primary Key. 
The Relational definitions of Primary Key and Foreign Key do not necessarily require the declaration of a Clarion KEY 
based on the Primary or Foreign Key. This means that, despite the fact that these Keys exist in theory, you will only 
declare a Clarion KEY if your application actually needs it for some specific table access. Generally speaking, most all 
Primary Keys will have a Clarion KEY, but fewer Foreign Keys need have Clarion KEYs declared. 


---

IDE User's Guide 
19 
 
 
 
 
Table Relationships 
There are three types of relationships that may be defined between any two tables in a relational database: One-to-One; 
One-to-Many (also called Parent-Child) and its reverse view, Many-to-One; and Many-to-Many. These relationships refer 
to the number of records in one table that are related to some number of records in the second table. 
In the previous example, the relationship between the Customer Table and the Order Table is One-to-Many. One 
Customer Table record may be related to multiple Order Table records. The Order Table and the Item Table also have a 
One-to-Many relationship, since one Order may have multiple Items. In business database applications, One-to-Many 
(Parent-Child) is the most common relationship between tables. 
A One-to-One relationship means that exactly one record in one table may be related to exactly one record in another 
table. This is useful in situations where a particular table may, or may not, need to have data in some fields. If all the fields 
are contained in one table, you can waste a lot of disk space with empty fields in those records that don‘t need the extra 
information. Therefore, you create a second table with a One-to-One relationship to the first table, to hold the possibly 
unnecessary fields. 
To expand the previous example, an Order may, or may not, need to have a separate ShipTo Address. So, you could add 
a ShipTo Table to the database design. 
 
 
Order Table: 
Order Number - Primary Key 
Customer Number - Foreign Key 
Order Date 
 
 
ShipTo Table: 
Order Number - Primary Key and Foreign Key 
 
ShipTo Address 
 
 
 
In this example, a record would be added to the ShipTo Table only if an Order has to be shipped to some address other 
than the address in the Customer Table. The ShipTo Table has a One-to-One relationship with the Order Table. 
Many-to-Many is the most difficult table relationship with which to deal. It means that multiple records in one table are 
related to multiple records in another table. Expand the previous example to fit a manufacturing concern, which buys Parts 
and makes Products. One Part may be used in many different Products, and one Product could use many Parts. 
 
 
Parts Table: 
Part Number – Primary Key 
Part Description 
 
 
Product Table: 
Product Number - Primary Key 
 
Product Description 


---

User's Guide and Lessons 
20
 
 
 
Without going into the theory, let me simply state that this situation is handled by defining a third table, commonly referred 
to as a "Join" table. This Join table creates two One-to-Many relationships, as in this example: 
 
 
Parts Table: 
Part Number – Primary Key 
Part Description 
 
 
Parts2Prod Table: 
 
Part Number - 1st Primary Key Component and Foreign Key 
Product Number - 2nd Primary Key Component and Foreign Key 
Quantity Used 
 
 
Product Table: 
Product Number - Primary Key 
 
Product Description 
 
 
 
The Parts2Prod Table has a multiple component Primary Key and two Foreign Keys. The relationship between Parts and 
Parts2Prod is One-to-Many, and the relationship between Product and Parts2Prod is also One-to-Many. This makes the 
Join table the "middle-man" between two tables with a Many-to-Many relationship. 
An advantage of using a Join table is that there is usually some more information that logically should be stored there. In 
this case, the Quantity Used (of a Part in a Product) logically only belongs in the Parts2Prod table. 
 
 
Translating the Theory to Clarion 
In practical relational database design, a Clarion KEY may not need to be declared for the Primary Key on some tables. If 
there is never a need to directly access individual records from that table, then a KEY definition based on the Primary Key 
is not necessary. Usually, this would be the Child table (of a Parent-Child relationship) whose records are only needed in 
conjunction with the Parent record. 
A Clarion KEY also may not need to be declared for a Foreign Key. The determination to declare a KEY is dependent 
upon how you are going to access the table containing the Foreign Key. If you need to access the Foreign Key records 
from the Primary Key, a Clarion KEY is necessary. However, if the only purpose of the Foreign Key is to ensure that the 
value in the Foreign Key field value is valid, no Clarion KEY is needed. 
Take the previous theoretical examples and create Clarion table definitions (Note: if this is the first time that you are 
looking at Clarion table definitions, you will notice that the FILE entity is used to define tables. This is there for legacy code 
modules, and the terms are often used throughout the documentation interchangeably): 
 
 
Customer FILE,DRIVER('Clarion'),PRE(Cus) 
CustKey 
KEY(Cus:CustNo) 
!Primary KEY 
Record 
## RECORD
CustNo 
## LONG
!Customer Number - Primary Key 
Name 
## STRING(30)
!Customer Name 
Address 
## STRING(30)
!Customer Address 


---

IDE User's Guide 
21 
 
 
 
END 
END 


---

User's Guide and Lessons 
22
 
 
 
Order 
FILE,DRIVER('Clarion'),PRE(Ord) 
OrderKey KEY(Ord:OrderNo) 
!Primary KEY 
CustKey 
 KEY(Ord:CustNo),DUP 
!Foreign KEY 
Record 
## RECORD
OrderNo 
## LONG
!Order Number - Primary Key 
CustNo 
## LONG
!Customer Number - Foreign Key 
Date 
## LONG
!Order Date 
END 
END 
 
ShipTo 
FILE,DRIVER('Clarion'),PRE(Shp) 
OrderKey KEY(Shp:OrderNo) 
!Primary KEY 
Record 
## RECORD
OrderNo 
## LONG
!Order Number - Primary Key and Foreign Key 
Address 
## STRING(30)
!ShipTo Address 
END 
END 
 
Item 
FILE,DRIVER('Clarion'),PRE(Itm) 
OrderKey KEY(Itm:OrderNo,Itm:ProdNo) !Primary KEY 
Record 
## RECORD
OrderNo 
## LONG
!Order - Primary Component and Foreign Key 
ProdNo 
## LONG
!Prod. - Primary Component and Foreign Key 
Quantity 
## SHORT
!Quantity Ordered 
Price 
## DECIMAL(7,2)
!Unit Price 
END 
END 
 
Product 
FILE,DRIVER('Clarion'),PRE(Pro) 
ProdKey 
 KEY(Pro:ProdNo) 
!Primary KEY 
Record 
## RECORD
ProdNo 
## LONG
!Product Number - Primary Key 
Description  STRING(30) 
!Product Description 
END 
END 
 
Parts2Prod FILE,DRIVER('Clarion'),PRE(P2P) 
ProdPartKey KEY(P2P:ProdNo,P2P:PartNo) !Primary KEY 
PartProdKey KEY(P2P:PartNo,P2P:ProdNo) !Alternate KEY 
Record 
## RECORD
PartNo 
## LONG
!Part - Primary Component and Foreign Key 
ProdNo 
## LONG
!Prod. - Primary Component and Foreign Key 
Quantity 
## SHORT
END 
END 
 
Parts 
FILE,DRIVER('Clarion'),PRE(Par) 
PartKey 
KEY(Par:PartNo) 
!Primary KEY 
Record 
## RECORD
PartNo 
## LONG
!Part Number - Primary Key 
Description STRING(30) 
!Part Description 
END 
END 
 
 
Notice that only one Foreign Key (in the Order table) was explicitly declared as a Clarion KEY. A number of Foreign Keys 
were included as part of Primary Key declarations, but this was simply good fortune. 
The Primary Key (Itm:OrderKey) defined on the Item table is there to ensure that an order does not contain duplicate 
Products Ordered. If this were not a consideration, Itm:OrderKey would only contain Itm:OrderNo, and would have the 
DUP attribute to allow duplicate KEY values. This would make it a Foreign Key instead of a Primary Key, and the table 
would not have a KEY defined for the Primary Key. 


---

IDE User's Guide 
23 
 
 
 
The Item table and the Product table have a Many-to-One relationship, which is One-to-Many looked at from the reverse 
perspective. This reverse view is most often used for data entry verification look-up. This means the Product Number 
entered into the Item table‘s data entry procedure can look-up and verify the Product Number against the records in the 
Product table. 
Referential Integrity 
There is one more fundamental issue in the Relational Model that should be addressed: "Referential Integrity." This is an 
issue that must be resolved in the executable source code for an application, because it involves the active, run-time 
inter-relationship of the data within the database. 
Referential Integrity means that no Foreign Key can contain a value that is not matched by some Primary Key value. 
Maintaining Referential Integrity in your database begets two questions which must be resolved: 
• What do you do when the user wants to delete the Primary Key record? 
• What do you do when the user wants to change the Primary Key value? 
The three most common answers to each of these questions are: Restrict the action, Cascade the action, or (less 
commonly) Nullify the Foreign Key values. Of course, there may also be application-specific answers, such as copying all 
information to history tables before performing the action, which should be implemented as required in individual 
programs. 
Restrict the action 
Restrict the action means that when the user attempts to delete the Primary Key record, or change the Primary Key value, 
the action is only allowed if there are no Foreign Keys that reference that Primary Key. If related Foreign Keys do exist, 
the action is not allowed. 
Using the tables defined previously, here is an example of how the executable code might look to Restrict deletes or a 
change of the Primary Key value. 
ChangeRec EQUATE(2) 
!EQUATE Change Action 
DeleteRec EQUATE(3) 
!EQUATE Delete Action value for readability 
SaveKey 
## LONG
!Primary Key save variable 
 
## CODE
SaveKey = Cus:CustNo 
!Save Primary Key value 
OPEN(window) 
## ACCEPT
## CASE ACCEPTED()
!Process entry individual control processing 
OF ?OKButton 
!Screen completion button 
IF Action = ChangeRec AND Cus:CustNo <> SaveKey !Check for changed Primary Key value 
DO ChildRecordCheck 
IF ChildRecordExists 
Cus:CustNo = SaveKey 
!change it back 
MESSAGE('Key Field changes not allowed!') !tell the user 
## SELECT(1)
!to start over 
## CYCLE
END 
ELSIF Action = DeleteRec 
!Check for Delete Action 
Ord:CustNo = Cus:CustNo 
!Initialize Key field 
GET(Order,Ord:CustKey) 
!and try to get a related record 
## IF NOT ERRORCODE()
!If the GET was successful 
MESSAGE('Delete not allowed!') ! tell user 
## SELECT(1)
!to start over 
## CYCLE
## ELSE
!If GET was unsuccessful 
DELETE(Customer) 
!go ahead and delete it 
## BREAK
!and get out 
END 
!other executable processing statements 
END 
EN 
D 
EN 


---

24
User's Guide and Lessons 
 
 
 
D 


---

25 
IDE User's Guide 
 
 
Cascade the action 
Cascade the action means that when the user attempts to delete the Primary Key record, or change the Primary Key 
value, the action cascades to include any Foreign Keys that reference that Primary Key. If related Foreign Keys do exist, 
the delete action also deletes those records, and the change action also changes the values in the Foreign Keys that 
reference that Primary Key. 
There is one consideration that should be noted when you Cascade the action. What if the table you Cascade to (the 
Child table) is also the Parent of another Child table? This is a situation which you must detect and handle, because the 
Cascade action should affect all the dependent table records. When you are writing source code to handle this situation, 
you need to be aware of the table relationships and write code that Cascades the action as far it needs to go to ensure 
that nothing is "left hanging." 
Again using the tables defined previously, here is an example of how the executable code might look to Cascade deletes 
or a change of the Primary Key value. 
 
 
ChangeRec EQUATE(2) 
!EQUATE Change Action 
DeleteRec EQUATE(3) 
!EQUATE Delete Action value for readability 
SaveKey LONG 
!Primary Key save variable 
## CODE
SaveKey = Cus:CustNo 
!Save Primary Key value 
OPEN(window) 
## ACCEPT
## CASE ACCEPTED()
!Process entry 
!individual control processing 
OF ?OKButton 
!Screen completion button 
IF Action = ChangeRec AND Cus:CustNo <> SaveKey 
!Check for changed Primary Key value 
DO ChangeCascade 
!and cascade the change 
ELSIF Action = DeleteRec 
!Check for Delete Action 
DO DeleteCascade 
!and cascade the delete 
END 
!other executable processing statements 
END 
END 
 
ChangeCascade ROUTINE 
Ord:CustNo = SaveKey 
!Initialize the key field 
SET(Ord:CustKey,Ord:CustKey) 
!and set to process all of one 
## LOOP
!customer’s orders 
NEXT(Order) 
!one at a time 
IF Ord:CustNo <> SaveKey OR ERRORCODE() THEN BREAK. 
!Check for end of cust. and get out 
Ord:CustNo = Cus:CustNo 
!Change to new value 
PUT(Order) 
!and put the record back 
## IF ERRORCODE() THEN STOP(ERROR()).
END 
 
DeleteCascade ROUTINE 
Ord:CustNo = SaveKey 
!Initialize the key field 
SET(Ord:CustKey,Ord:CustKey) 
!and set to process all of one 
## LOOP
!customer’s orders 
NEXT(Order) 
!one at a time 
IF Ord:CustNo <> SaveKey OR ERRORCODE() THEN BREAK. 
!Check for end of cust. and get out 
CLEAR(Itm:Record) 
!Clear the record buffer 
Itm:OrderNo = Ord:OrderNo 
!Initialize the key field 
SET(Itm:OrderKey,Itm:OrderKey) !and set to process all of one 


---

26
User's Guide and Lessons 
 
 
 
LOOP UNTIL EOF(Item) 
!order’s items 
NEXT(Item) 
!one at a time 
IF Itm:OrderNo <> Ord:OrderNo OR ERRORCODE() THEN BREAK. 
!Check for end of order 
!and get out of Item loop 
DELETE(Item) 
!and delete the Item record 
## IF ERRORCODE() THEN STOP(ERROR()).
END 
!End Item table loop 
Shp:OrderNo = Ord:OrderNo 
!Check for ShipTo record 
GET(ShipTo,Shp:OrderKey) 
## IF NOT ERRORCODE()
!If GET was successful 
DELETE(ShipTo) 
!delete the ShipTo record 
## IF ERRORCODE() THEN STOP(ERROR()).
END 
DELETE(Order) 
!and delete the Order record 
## IF ERRORCODE() THEN STOP(ERROR()).
END 
!End Order table loop 
 
 
Nullify the Foreign Key 
Nullify the Foreign Key means that when the user attempts to delete the Primary Key record, or change the Primary Key 
value, the Foreign Keys that reference that Primary Key are changed to null values (if the Foreign Key fields allow null 
values). 
Again using the tables defined previously, here is an example of how the executable code would look to Nullify the 
Foreign Keys on delete or a change of the Primary Key value. 
 
 
ChangeRec EQUATE(2) 
!EQUATE Change Action 
DeleteRec EQUATE(3) 
!EQUATE Delete Action value for readability 
SaveKey LONG 
!Primary Key save variable 
## CODE
SaveKey = Cus:CustNo 
!Save Primary Key value 
OPEN(window) 
## ACCEPT
## CASE ACCEPTED()
!Process entry 
!individual control processing 
OF ?OKButton 
!Screen completion button 
IF Action = ChangeRec AND Cus:CustNo <> SaveKey 
!Check for changed Primary Key value 
DO ChangeNullify 
!and nullify the Child records 
ELSIF Action = DeleteRec 
!Check for Delete Action 
DO DeleteNullify 
!and nullify the Child records 
END 
!other executable processing statements 
END 
END 
 
ChangeNullify ROUTINE 
Ord:CustNo = SaveKey 
!Initialize the key field 
SET(Ord:CustKey,Ord:CustKey) 
!and set to process all of one 
## LOOP
!customer’s orders 
NEXT(Order) 
!one at a time 
IF Ord:CustNo <> SaveKey OR ERRORCODE() THEN BREAK. 
!Check for end of cust. and get out 
Ord:CustNo = 0 
!Change to null value 
PUT(Order) 
!and put the record back 
## IF ERRORCODE() THEN STOP(ERROR()).
END 


---

27 
IDE User's Guide 
 
 
 
DeleteNullify ROUTINE 
Ord:CustNo = SaveKey 
!Initialize the key field 
SET(Ord:CustKey,Ord:CustKey) 
!and set to process all of one 
## LOOP
!customer’s orders 
NEXT(Order) 
!one at a time 
IF Ord:CustNo <> SaveKey OR ERRORCODE() THEN BREAK. 
!Check for end of cust. and get out 
Ord:CustNo = 0 
!Change to null value 
PUT(Order) 
!and put the record back 
## IF ERRORCODE() THEN STOP(ERROR()).
END 
 
 
The Nullify option does not require as many changes as the Cascade option. This is because the Cascade has to delete 
all the related records in as many tables as are related. Nullify only needs to null out the individual Foreign Keys that 
reference the Primary Key being changed or deleted. 
 
 
Summary 
• 
Each data item should be stored once. 
• 
Separate tables are used to eliminate data duplication. 
• 
Tables are related by Primary and Foreign Keys. 
• 
A Primary Key is a unique (and non-null) index into a table which provides for individual record access. 
• 
A Foreign Key contains a reference to the Primary Key of some other table. 
• 
One-to-Many table relationships are the most common. They are also referred to as Parent-Child and Many-to-One 
(same relationship, reverse view). 
• 
One-to-One table relationships are most commonly created to hold data that is not always needed in every record. 
• 
Many-to-Many relationships require a "Join" table which acts as a broker between the two tables. The Join table 
inserts two One-to-Many relationships between the Many-to-Many relationship. 
• 
Only those Primary and Foreign Keys that the application needs (as a practical consideration) for specific access to 
the tables need to have Clarion KEYs declared. 
• 
Referential Integrity means that all Foreign Keys contain valid references to Primary Keys. 
• 
Maintaining Referential Integrity requires executable code that tests for Update or Delete of the Primary Key values. 
• 
The three common solutions to maintaining Referential Integrity are: Restricting (update/delete not allowed), 
Cascading (also update/delete the Foreign Key), or Nullifying the Foreign Key (assign null values to the Foreign Key). 


---

28
User's Guide and Lessons 
 
 
 


---

29 
IDE User's Guide 
 
 
 
Dictionary Editor 
Overview and Introduction 
The lessons that follow describe the creation and maintenance of database dictionaries. Database dictionaries define the 
physical layout of the data files to be accessed by an application, the relationships existing between files, and the rules for 
maintaining these relationships. 
Programs that are created with the Application Generator in order to access data files require database dictionaries. 
 
 
Lesson 1 - Data Import 
In this lesson, see how easy it is to create a dictionary, and examine the different options that you have when importing 
data definitions. 
 
 
Lesson 2 - Table Properties 
Examine the options available for the tables that you import or create in your data dictionary. 
 
 
Lesson 3 - Column Properties 
Examine the many options available for each column defined in your dictionary. See how certain settings can help speed 
up and polish your applications. 
 
 
Lesson 4 - Key and Index Properties 
Explore the Key and Index options available in you data dictionary. Learn the importance of proper key definitions, and 
how it can save you time as you develop your applications. 
 
 
Lesson 5 - Adding Relationships 
Discover the importance of defining proper relationships between the tables defined in your dictionary. 
 
 
Lesson 6 - Trigger Properties 
Explore the use of Client-Side Triggers, and how you can easily enforce powerful business rules during normal database 
operations in your applications. 
 
 
Lesson 7 - SQL, ODBC, and ADO Imports 
Discover the deep support of Clarion‘s data dictionary with SQL, ODBC, and ADO type databases. Examine the 
Dictionary Synchronizer, a powerful accessory that is built into the environment. 
 
 
Lesson 8 - Advanced Features of the Dictionary Editor 
The Dictionary Editor is packed with features and options that can accelerate your planning and development. This lesson 
explores several key areas. 


---

User's Guide and Lessons 
31 
 
 
 
Lesson 1 - Data Import 
Lesson Tasks: 
• Create a new dictionary. This dictionary will be added to, and used in subsequent lessons. 
• Import table definitions using 3 different techniques. 
 
 
Creating a New Dictionary 
1. To create a dictionary, choose File  New  File from the IDE Menu. 
Then, the New File window appears which contains a Clarion Data Dictionary category to allow you to specify the Data 
Dictionary to create. 
2. To create a database dictionary, choose the Data Dictionary Quick Start. 
3. Press Create to complete the New window. 
 
 
As you complete the design of your dictionary, you will be prompted to save to the desired name. 
 
 
As an alternative, you can select the Dictionaries link on the IDE Start Page, and press the New Dictionary button. 
 
 
Adding Tables to Your Dictionary 
The first step in Dictionary Design is to define the data tables that you need to manage and process. 
 
 
Design Variations 
Some developers prefer to create their dictionary by defining a single table, adding the various fields to the table, and then 
the keys. After the keys are defined, they would proceed to the next table and repeat the entire process. 
A second method described here is probably an easier process. 
First define all of your tables, and then proceed to define all of the fields. After all of the fields are defined, proceed to 
define all of your keys. Finally, the table relationships can be defined, and other auxiliary features can then be added to 
selected elements before finishing the dictionary design process. 
So let‘s get started with the creation of our dictionaries‘ table definitions. We will show you three very popular techniques 
used in creating your tables. 
 
 
Technique 1: Import a Table 
This technique is popular and sometimes necessary when you would like your dictionary to accurately reflect an existing 
table structure. 
To begin the import process: 
1. Select the File  Import Table option from the toolbar menu of the DCT Explorer: 


---

IDE User's Guide 
30 
 
 
 
 
 
 
2. Specify a data table and additional options in the Import Table dialog. 
When you import an existing table, the field and key information should also be imported. The amount of information 
imported is dependant on the table type you have selected. 
Technique 2: Copy and Paste from an Existing Dictionary 
The second technique that we will demonstrate is a popular short cut with Clarion developers. 
Many times, you will find an existing dictionary that contains a table definition that is close to the type of table that you are 
creating. For example, a customer table with a first name, last name, address, city, state, zip, etc. is very similar to a 
contacts or prospects table. 
The begin the Copy and Paste process: 
1. With the Dictionary dialog active, select the File  Open option from the main menu. Choose the dictionary that you 
wish to copy from. 
2. Highlight the table that you wish to copy, and choose the Edit  Copy option from the main menu, or press the Copy 
button located on the toolbar (or right-click on the table aand select Copy from the popup menu). 
3. Navigate to your target dictionary, highlight the Tables node on the DCT Explorer, , and select the Paste option, located 
on the toolbar, main menu, or popup menu. 
Unlike the first option, this technique will import additional table information that was stored in the source dictionary. 
Examples of this are custom field pictures, help ids, default controls, etc. 
Clarion is packed with example dictionaries that contain a wide variety of table types. It‘s a safe bet to assume that, with a 
little research, you will discover a dictionary and its tables that comes close to the type of database you actually need. See 
the on-line Guide to Examples for specific information about the Clarion default examples that are installed. 
Technique 3: The Custom Method 
When there is no existing data table structure to emulate your planned database design (either on disk or in another 
dictionary), you may have to design a table definition from the ground up. 
To add a table to your dictionary using the "custom" method: 
1. With the DCT Explorer dialog active, press the Add Table button. 
 
The Add Table dialog is displayed. 
2. In the Label field, type the label (name) to be used when referring to this file from within the application. Labels may be 
up to 255 characters, however, limit your name to a reasonable length. Labels consists of alphabetic characters, numbers, 
the underscore character ( _ ), and the colon ( : ). Labels may not begin with a number or a colon and are not case 
sensitive. The underscore character is often used as a separator for readability (i.e. INVOICE_FILE) since a space is not 
valid in a label. Mixed case is often used for greater readability (i.e. InvoiceFile). 


---

User's Guide and Lessons 
31 
 
 
 
Lesson 2 - Table Properties 
 
Lesson Tasks: 
Explore and understand the Table Properties options. 
 
 
Table Types 
In the DCT Explorer, folders are available for you to add a Table, Global Data group, or Field Pool structure. You can 
define relationships for tables, but not for Global or Pool structures. The Add button dynamically changes based on what 
folder you have selected. 
 
 
Tables 
The structure represents a FILE. The Application Generator 
generates a FILE declaration as well as code to read and write 
the FILE. You can use the columns in the FILE as the parents 
of derived fields. See Derived From in the Column Properties 
dialog. 
 
Globals 
The structure represents a group of global data declarations. 
The Application Generator generates a global data declaration 
for each field in the structure. You can use the global fields as 
the parents of derived fields. See Derived From in the Column 
Properties dialog. This option enables the Generate Last 
checkbox, which causes these declarations to follow 
declarations made for global variables defined in the .APP. 
 
Pools 
The structure represents a Field Pool. The Application 
Generator generates no code for this structure. You can use 
the fields in the pool as the parents of derived fields. See 
Derived From in the Column Properties dialog. 
 
 
Table Properties 
 
 
The Table Properties window allows the characteristics of a data table as a whole to be specified. An explanation of key 
options shown in the Table Properties window follows: 
Label 
Type a data table name, as you wish to refer to it in your code. This serves as the label for the Clarion FILE structure. 
Specify a valid Clarion label--Clarion will automatically truncate the name if necessary. You may also specify a completely 
different name for the DOS file--see Full Pathname, below. 
Description 
Descriptions are a string of characters used to fully describe the contents of a data table. If the Table Label specified is 
somewhat cryptic, it is a good idea to enter a meaningful description. Information entered in the Description field is treated 
as a comment. The double-arrow button at the end of the description field may be used to enter a very long description of 
the table. 
Prefix 
A prefix is a combination of up to 3 characters that will preface the names (labels) of all of the fields defined within this 
data table. Prefixes are used to uniquely identify fields with the same name in different tables. The prefix will default to the 
first 3 characters of the Table name but can be overridden. 


---

IDE User's Guide 
30 
 
 


---

IDE User's Guide 
32 
 
 
Driver 
As mentioned previously, Clarion supports a number of different data table formats. The format to be used for table 
being created is specified in the Table Driver field. The formats currently supported include Clarion, Btrieve, binary 
(specified as DOS), flat ASCII (specified as ASCII), comma-delimited ASCII (specified as BASIC), and various xBase 
formats. Choose the table format that should be used from the list of available table drivers that is displayed in a 
combo box. A table driver must be chosen from the list. Since certain table characteristics are table driver dependent, 
after a driver is chosen, some options may be disabled. 
 
Driver Options 
The behavior of some of the database drivers may be customized. This customization is accomplished through the 
use of parameters when the driver is loaded. Online help documents the OPTIONS that may be specified for each of 
the table drivers. 
 
Owner Name 
Owner name is a combination of characters that can be used to restrict access to a data table. This is used to prevent 
someone from gaining access to table organization information. If this data table is not organized in a particularly 
sensitive manner or will not contain sensitive data, leave this field blank. All database drivers do not support this 
option. 
 
Full Path Name 
The drive, path, and actual DOS file name (if different from the File Label) for this data file should be specified here. If 
omitted, programs created with this dictionary will assume that the data table resides in the directory that is active 
when the program loads. 
 
Create 
This option is selected if the file may be created at run time. 
 
Reclaim 
This checkbox is selected if the space occupied by previously deleted records should automatically be reused when 
new records are added to the data file. This option is not supported for all file drivers. 
 
Encrypt 
This checkbox is selected if the data in the data file should be "scrambled" based on the Owner Name that was 
specified. If this option is selected, the data in the data file will be unreadable unless the Owner Name is known. 
 
Threaded 
If this file will be used in Multi-Threaded procedures, this checkbox will reserve additional memory for the record 
structure defined in every instance. 
 
OEM 
This option specifies that string data is converted from OEM ASCII to ANSI when read from disk and ANSI to OEM 
ASCII when writing to the file. 
 
Bindable 
This checkbox will specify that all variables in the Record structure are available for use in dynamic expressions at 
runtime. 
After entering the appropriate information for the file, press OK to complete the Add Table window. The file just defined 
now appears in the Dictionary window. 
When you have entered and reviewed all available options, press the OK button to save the file definition, and close the 
File Properties window. 


---

User's Guide and Lessons 
33 
 
 
 
Lesson 3 - Column Properties 
Lesson Tasks: 
Explore and understand the Column Properties options. 
Due to the amount of options available through Column Properties, the Validity Checks, Window, and Report options are 
discussed in the Advanced Features lesson. 
 
 
Overview 
Columns are added to the dictionary in the same manner as tables. There are two ways to add columns to any table. 
1. From the Quick View Fields window, press the Add button 
 on the Fields toolbar. You can also press the INSERT 
key in this window. 
When adding columns to a new table, the list boxes on this screen are initially empty. 
2. Double-clicking on any table in the DCT Explorer opens the Entity Browser. 
 
 
 
From this window, select the Columns folder, and press the Add button on the Entity Browser toolbar. 


---

IDE User's Guide 
34 
 
 
Column Properties Summary 
The Column Properties window allows the characteristics of each defined column to be specified. It contains a number of 
options that allow you to specify particular information about a column. An explanation of some key options shown in the 
Column Properties window follows: 
Column Name 
The label (name) to be used when referring to this control from within the application. Up to 80 characters may be 
entered in this screen for the control label. As with all Clarion labels, the control label may consist of alphabetic 
characters, numbers, the underscore character (_), and the colon ( : ). Labels may not contain spaces, may not begin 
with a number or a colon, and are not case sensitive. 
Derived From 
Press the ellipsis button (...) to select another (parent) field in the dictionary from which to copy all field attributes, 
except the field name. The parent field may be any other field in the data dictionary, including global data fields, field 
pool fields, or file fields. 
Press the refresh button to reapply the attributes from the parent field. Use the Freeze check box below to prevent a 
refresh from the parent. See also the Refresh Field, Refresh File, Refresh Dictionary, and Distribute Field menu 
commands 
Description 
Descriptions are a string of characters used to fully describe the type of information stored in this control. If the Control 
Label specified is somewhat cryptic, it is a good idea to enter a meaningful description. Information entered in the 
Description column is treated as a comment. Very long descriptions may be entered by using the double-arrow button 
at the end of this control. 
Data Type 
The data type for the control. The following data types are supported: String, Memo, Picture, Cstring, Pstring, Byte, 
Short, Ushort, Long, Ulong,Date, Time, Sreal, Real, BFloat4, Bfloat8, Decimal, Pdecimal and Group. For the 
characteristics of each data type, refer to the Declaring Variables chapter of the Language Reference. The data types 
available are database driver dependent. 
Base Type 
Enter the label of a previously declared GROUP or QUEUE structure from which it will inherit its structure. This setting 
is only active during GROUP, LIKE, or TYPE data types. 
Characters 
Used for the string and decimal data types to specify the maximum number of characters that may be entered into this 
control. 
Places 
Used with the decimal and floating point data types to specify the number of decimal place to be associated with a 
number. 
Binary 
This checkbox only appears in conjunction with Memo data types to indicate that it will be used to store binary 
information like graphical images. 
Dimensions 
Allows multiple copies of a control to be defined. A control with dimensions is called an array. The individual copies of 
the control are called elements. Elements of an array are referred to through the use of subscripts. For example, if the 
number 10 is entered in the dimensions column, 10 copies of the control are created. This copies are referred to as 
column[1] ... column[10]. Arrays are a shorthand way of creating multiple copies of a control. 
RowPicture 
Used with the PICTURE data type. It is a picture that indicates how stored data is formatted. For example, if a date is 
stored in a table as 10/22/92, it would be defined as a PICTURE type and the Record Picture would be @D1. This data 
could subsequently be displayed with a different picture by specifying an appropriate Display Picture. 
Screen Picture 
Screen Picture allows a formatting mask (picture type) for a column to be specified. 


---

User's Guide and Lessons 
35 
 
 
Prompt Text 
The default prompt is the value used for the string prompt for a control when it is placed (or populated) on a window. 
Column Heading 
The default column heading for this control is entered here. The default column heading may be used when the control 
is placed on reports in the Application Generator. 
 
 
Column Attributes Summary 
Attributes reference such entry characteristics as the case of characters entered into the control, the way the cursor 
functions in a control, and how characters will be echoed to the screen. 
Case 
The Case radio button options control the alphabetic case of the information entered into a control. 
 
Normal 
The case of the characters entered should not be modified by the program. 
 
Word Capitalized 
This mode specifies that the first letter of each word should be an uppercase character and all other characters 
entered should be lowercase characters. The program will convert the case of characters entered if necessary. 
 
Uppercase 
Only uppercase characters are allowed in this control. The program will change characters to uppercase if necessary. 
Typing Mode 
Radio buttons that allow the Typing Mode to be specified. 
 
Set Insert 
For string controls, causes entry to work in a manner similar to a word processor in insert mode. If information is being 
entered into a control already containing data, the original data is "pushed" to the right until the size limit of the control 
has been reached. 
 
For numeric controls, this mode causes the column to be filled from right to left, calculator style. This is the 
recommended mode for numeric controls containing information that varies greatly in length, such as controls 
containing currency data. 
 
Set Overwrite 
This mode causes a destructive overwrite if information is entered into a control already containing data. For numeric 
columns, this mode also specifies that numbers are to be entered from left to right. 
 
Do Not Reset 
Specifies that the typing mode should not be changed for this control. The typing mode used will be the typing mode 
"left over" from a previous setting of the typing mode. 
Flags 
These are checkboxes that allow entry attributes for a control to be specified. 
 
Immediate 
Immediate specifies immediate event notification for controls referencing this column. If you check the Immediate box. 
The Application Generator adds the IMM attribute. 
 
Password 
This attribute specifies that the information entered into this control should be "hidden". As characters are entered into 
this column, asterisks ( * ) are echoed back to the screen for each character typed. This attribute is chosen for columns 
requiring sensitive data (i.e. passwords) to be entered. 
 
Read Only 
This attribute specifies the column should be Display Only, not allowing data entry into this control. 


---

IDE User's Guide 
36 
 
 
Justification/Offset 
Allows for alignment justification along with indentation parameters to be specified for the column (control). 
Place Over 
Allows the column definition for the column being defined to redefine another column definition giving the ability to look 
at the same data in two different ways. Notice that a down arrow appears to the immediate right of this column. The 
down arrow indicates that a list is available to choose from. If the down arrow is chosen, a window will appear 
presenting a list of columns which may be overlaid with this column definition. 
 
 
External Name 
The name of the control within the data table may be different from the name used to refer to that control within the 
program (column label). If so, the name of the control as it exists in the data table should be entered here. 
Initial Value 
This column is used to "pre-load" a control with a particular value. For example, if a column named COUNTRY was 
being defined, a default value of USA might be specified. 
 
 
Part II of the Column Properties features is covered in Lesson 8 - Advanced Features 


---

User's Guide and Lessons 
37 
 
 
 
Lesson 4 - Key and Index Properties 
 
Overview 
Keys are a mechanism for organizing or sorting records in a data table based upon the contents of a column or a 
combination of columns. Keys are used to quickly locate related records in a relational database and to allow data to be 
presented in a particular sort sequence. 
To define keys for a data table: 
1. From the Quick View Keys window, press the Add button 
 on the Keys toolbar. You can also press the 
INSERT key in this window. 
When adding columns to a new table, the list boxes on this screen are initially empty. 
2. Double-clicking on any table in the DCT Explorer opens the Entity Browser. From this window, select the 
Columns folder, and press the Add button on the Entity Browser toolbar, or press the INSERT key. 
When adding keys to a new table, the list box on this screen is initially empty. 
Information on the characteristics of a key are specified in the Key Properties window. A brief description of important 
properties follows: 
Label 
Enter the name (label) to be used when referring to this key from within the application. As with all Clarion labels, the 
key name may consist of alphabetic characters, numbers, the underscore character (_), and the colon (:). Labels may 
not begin with a number or a colon, may not contain spaces, and are not case sensitive. 
Description 
Descriptions are a string of characters used to fully describe the type of information stored in this column. If the key 
name specified is somewhat cryptic, it is a good idea to enter a meaningful description. Information entered in the 
Description column is treated as a comment. 
External Name 
Enter the name of this key as stored in the data table. This option is table driver dependent, and is usually 
implemented in SQL based databases. 
 
 
Type 
The following radio buttons in the Key Properties window allow you to specify the type of key being defined: 
 
Row Key 
A key is a sort sequence on a column or group of columns that is maintained dynamically by the program. As the 
records in the data table are modified, the sort sequence is automatically adjusted. 
 
Static Index 
An index is a sort sequence that reflects the contents of the data table at a particular time. Indexes are not dynamically 
maintained, they are built only when specified. Indexes are useful for sort sequences that are used on an infrequent 
basis like month end or year end reporting. 
 
Runtime Index 
Dynamic indexes allow selected sort sequences to be chosen when the program executes. A dynamic index is defined 
without components. At runtime, the BUILD statement is issued to create the dynamic index. For more information on 
the BUILD statement, see the Language Reference manual. 
Order 
Order adds a sort order definition to a template symbol (%ORDER) in a similar manner as a KEY without affecting the 
file declaration. 


---

IDE User's Guide 
38 
 
 
 
 
Orders specified in a dictionary are not yet supported in the included templates. Some third party templates may use 
this option. 
 
 
Attributes 
Before saving your key definition, let‘s review some other important options. 
Checkboxes (and a single entry option) are found in the Attributes section to determine certain key attributes: 
Require Unique Value 
Selecting this option determines that the column used for the key cannot contain duplicate values. 
Primary Key 
Checking this option specifies that the key components of this key uniquely identify each record. There can only be 
one primary key per table. A primary key also refers to a key in the Parent table (on the Parent side of a Parent/Child 
relationship) containing the common column. 
Auto Number 
Selecting this option specifies that the program should automatically assign a numeric value to the column within the 
key when records are added to the data table. 
Case Sensitive 
If a key is case sensitive, upper and lower case characters are sorted separately. Upper case characters are placed 
into the sort sequence before any lower case characters. If this option is not selected, lower case characters are sorted 
as if they were upper case. 
Exclude Empty Keys 
This option, if selected, specifies that if no value is specified for the key column components, no entry for the record 
will be placed in the sort sequence of the key. 
The Key Columns tab option prompts for the columns that will be part of the key. The list box displays the available 
columns. If you are not creating a Runtime Index, you must select at least one column in order to be able to 
save the new key definition! 
3. Press the Add button to select the column components that will be part of this key. 
4. When you are finished setting key options and naming your column components, press the Save and Close button in 
either the Entity Browser or DCT Explorer to write your new key to the dictionary. 
 
 
Single and Composite Keys 
A key may have a single sort component, or may use multiple components when needed. 


---

User's Guide and Lessons 
39 
 
 
 
 
 
 
Composite keys (keys containing multiple columns) are created by pressing the Select button for each column that will be 
part of the key. When you have chosen more than one column for a key and you exit the Select a Column dialog, you will 
have the opportunity to move columns within a key relative to one another by using the mouse to drag and drop. 


---

IDE User's Guide 
40 
 
 
 
Lesson 5 - Adding Relationships 
Overview 
Table relationships describe how tables are related based upon common keys, columns within those keys, and how 
referential integrity should be maintained. Defining table relationships is generally the last step in the creation of a 
dictionary because columns and keys must be defined in order to create table relationships. 
Relationships for a table are defined by highlighting from the Relations list box and pressing the Add button when the 
appropriate table is active. You can also add relationships via the Entity Browser: 
 
 
 
 
 
 
Let‘s explore the Relationship Properties options in more detail: 
 
Adding Relationships 
Type 
The type of relationship being created is specified using this combo box: 1:Many, or Many:1. 
Primary Key 
The key in the table on the one side of a one-to-many relationship containing the common column(s). Notice the down 
arrow appearing next to this column. This symbol indicates that a drop list is available that will present you with a list of 
valid key name choices. 
Related Table 
This is the other table with which you are creating the relationship. If it is one the ONE side then it will be titled PARENT, 
and if it is on the MANY side it will be titled CHILD. A list box is also available for this column to give you a list of tables 
currently defined. 
Foreign Key 
The key in the table on the many side of a one-to-many relationship that contains the common column(s). 
Column Mapping 
Presents a list of the columns contained within the Access Keys that were specified for both tables. The columns in each 
key must be matched with the common columns in the corresponding table. 
Map by Name allows the common columns to be matched automatically if the column names are the same. 
Map by Order does just that regardless of column names. 


---

User's Guide and Lessons 
41 
 
 
The third method of mapping is to double click on [No Link] and then pick a suitable column from the other table. You will 
find it necessary to use this third method if a one-way relationship exists between the two tables, meaning that a suitable 
key exists in only one of the tables. 
Referential Integrity Constraints 
Allows "rules" to be defined for the maintenance of table relationships: 
On Update 
Update attributes allow you to specify what action should be taken (if any) when an attempt is made to modify a parent 
record with related child records. 
On Delete 
Delete attributes allow you to specify what action should be taken when an attempt is made to delete a parent record that 
has child records related to it. 
After creating tables, columns, keys, memos, and table relationships, the dictionary is near complete, and an application 
may be designed that uses the data dictionary. Let‘s look at a few more options that further demonstrate the power of the 
Dictionary Editor. 


---

IDE User's Guide 
42 
 
 
 
Lesson 6 - Trigger Properties 
Overview 
Triggers are a mechanism for providing Clarion language support during database operations on a selected table. This 
support is added in the data dictionary, so all applications that reference this table will automatically contain the built-in 
support. 
Regarding SQL tables, the trigger support that is added here is considered to be Client-Side, and should not be confused 
with the server-side database triggers supported by many SQL engines. 
The uses of dictionary triggers are limited only to the developer‘s imagination. For more information regarding the uses of 
dictionary triggers, review the Dictionary Triggers topic found in the core help. This section simply describes how a trigger 
is added and maintained in the data dictionary. 
 
 
To add a dictionary trigger to a selected table: 
 
 
1. In the DCT Explorer, double-click on the target table to open the Entity Browser. 
2. In the Entity Browser, click on the Triggers folder, then press the Add button, or press the INSERT key. 
Alternatively, you can also right-click on the Triggers folder, and select Add Triggers from the popup menu. 
3. In the Trigger Properties window, select from six different types of trigger entry points. Each name is self- 
explanatory: 
 
 
Before Insert 
After Insert 
 
Before Update 
After Update 
 
Before Delete 
After Delete 
 
 
After a trigger type is added, you cannot select it again for the same table. 
4. You can add trigger Data variables to use with the trigger source. Press the Columns tab to access the Trigger 
Data dialog, and press the Add button to add your data elements. 
These data elements are automatically included in the application‘s generated base class source file (Example: 
myappBC0.clw). They are only valid in the trigger type that they are created in, and are locally defined within the 
supporting trigger‘s derived method. 
5. Enter your trigger source code in the General tab using the text control provided. 
 
 
Example trigger source: 
 
 
! After update trigger 
## IF ~ERRORCODE()
!Log insert 
UPL:UpdRec = 'Pub ID: ('& PUB:PubID &') was updated in Publisher on '&| 
FORMAT(TODAY(),@D1) &' at '&format(Clock(),@t3) 
ACCESS:UpdLog.Insert() 


---

User's Guide and Lessons 
43 
 
 
 
! Change record in child file ( 1 <--> 1 relationship) 
PBI:PubID = PUB:PubID 
IF ~Access:Pub_Info.TryFetch(PBI:PubID_Key) 
 
!If record Change 
 
PBI:Pr_info = CLIP(PBI:Pr_Info)&'<13,10>Publisher '&clip(PUB:Pub_name) &| 
' in '& clip(PUB:City) & ' was updated on '&FORMAT(TODAY(),@d1)&'.' 
Access:Pub_Info.Update() 
END 
END 
! End of trigger (After update) 
 
 
Two functions are accomplished here. After a record has been updated, a log entry is automatically entered into another 
table defined in the dictionary. After the log update, a child table is also updated with appropriate information. 
 
 
Although trigger source should be designed to be maintenance free, the source code that is entered can be modified in 
the Application Generator through the following Global embeds: 
 
 


---

IDE User's Guide 
44 
 
 
 
Lesson 7 - Dictionary Synchronization 
This lesson introduces you to the Clarion Dictionary Synchronizer. It takes you through all the steps needed to 
synchronize two databases—both the data and the data definitions (.dct, .ddf, or SQL script). 
This synchronization process saves time in several development contexts: developing new applications to serve legacy 
databases, updating existing applications to conform to a modified database, and sharing application development among 
several developers with incremental modifications to the database definition. 
Lesson Objectives 
This lesson introduces you to the Clarion Dictionary Synchronizer. When you have finished the lesson you should be able 
to 
• 
Consolidate two Clarion data dictionaries 
• 
Run the Synchronizer Wizard 
• 
Convert existing data to a new format 
• 
Create and review a Dictionary Synchronizer log 
• 
Create a Clarion Data Dictionary from a Btrieve or SQL database 
 
 
To complete the lesson you will need a copy of the files from the Clarion …\Lessons\SyncLesson\Start folder. 
Please copy the files to the …\Lessons\SyncLesson folder. 
 
 
In Windows XP, the Lessons folder is found in: 
C:\Documents and Settings\All Users\Documents\SoftVelocity\Clarion7\Lessons 
 
 
In Vista and Windows 7: 
C:\Users\Public\Documents\SoftVelocity\Clarion7\Lessons 
 
 
Consolidate Two Clarion Data Dictionaries 
In a team development environment, the Dictionary Synchronizer automates the synchronization of the "master" dictionary 
or database with other project dictionaries and databases. 
This section of the lesson shows how to consolidate two similar but different Clarion data dictionaries into a single 
dictionary. In this example, the master.dct represents the "master" dictionary and the Project.dct represents another 
dictionary used by the development team. The two dictionaries must be consolidated into a single dictionary that all team 
members can use to continue to develop their application components. 
By using the Dictionary Synchronizer to update the Project.dct (as opposed to simply replacing it with a copy of the 
master.dct), you are able to see exactly which dictionary items changed and you can intelligently manage those changes; 
if both dictionaries have changed, you can incorporate the changes from both dictionaries by synchronizing each 
dictionary with the other; and finally, the Dictionary Synchronizer can generate a Clarion program to convert your existing 
data to the new format. 
 
 
Whenever you consolidate two Clarion dictionaries into a single dictionary, you risk damaging the relationship between 
the replaced dictionary and its corresponding applications, unless you first export those applications to text (.TXA) 
format. 


---

User's Guide and Lessons 
45 
 
 
Make a Master TXA File 
Make a Master.TXA file that you can use to create a master.app that will work with the consolidated dictionary. 
 
 
Starting Point: 
The C:\Clarion7\Lessons\SyncLesson\Master.app file should be opened in the Application Editor. 
 
 
1. Choose Application  Export Application To Text, then press the Save button to create Master.txa. 
2. Press the 
 button to save and close the \SyncLesson\Master.app. 
3. Select File  Close  Solution (CTRL+SHIFT+F4) to close the application solution. 
 
Run the Synchronizer Wizard 
The Synchronizer Wizard leads you step-by-step through the synchronization process. The wizard allows you to select 
the Synchronizer Server, the data dictionaries, the dictionary to synchronize (identify source and target), and set rules 
for matching items (files, fields, keys, etc.) between the dictionaries. 
1. Open Project.DCT. 
Every synchronization requires an open Clarion data dictionary (although the dictionary may be a newly created 
one that is completely empty). 
When synchronizing two Clarion data dictionaries, it doesn‘t matter which dictionary you open first. 
2. From the DCT Explorer, press the Synchronize button to start the Synchronizer Wizard (save the changes). 
 
 


---

IDE User's Guide 
46 
 
 
The Synchronizer Wizard is displayed. 
3. Verify that the Prompt Detail slider to the More position. 
 
 
Select the Synchronizer Mode 
1. CLICK on the Next > button to start a new synchronization. 
This page lets you rerun a prior synchronization. This page also lets you generate a data conversion program 
without modifying a data dictionary. 
 
 
Select the Synchronizer Server 
The Clarion Dictionary Server is the default (Synchronize With) server. A Synchronizer Server is a .dll that lets the 
Dictionary Synchronizer access a Clarion data dictionary or a database/file system such as ORACLE, MSSQL, Btrieve, 
etc. The Clarion Dictionary server handles all Clarion data dictionaries (regardless of the file driver). 
 
 
Select the Other Clarion Dictionary 
1. Press the ellipsis (...) button to Select the "other" database or dictionary with the Windows file dialog. 
If you choose an SQL, ADO, ODBC, or Btrieve Synchronizer Server, the Synchronizer Wizard prompts you for the 
logon information needed to connect to the SQL database or for the folder containing the Btrieve .DDF files. 


---

User's Guide and Lessons 
47 
 
 
 
 
 
 
2. Select the Master.dct, then press the Open button. 
 
 
Set the Synchronizer Log File 
The Synchronizer saves details about each synchronization so you can automatically repeat a synchronization process as 
often as you need to. You can use the Log Synchronization To field to name the log file that stores the synchronization 
information. Press the ellipsis button and select the current working directory 
(C:\Clarion7\Lessons\SyncLesson\SynLog.TXT). 
 
 
3. CLICK on the Next > button to continue. 
 
 
Set the Dictionary to Synchronize (source and target) 
4. CLICK on the From ..\Master.dct To Project.DCT radio button to make Project.DCT the target dictionary. 
The Dictionary Synchronizer only modifies the target dictionary. Specify which dictionary is the source and which is 
the target by clicking the appropriate radio button. 
The warning is simply a reminder that for any applications that use a dictionary that will be replaced (copied over), 
you should export those applications to text (.txa) format before you replace (copy over) the dictionary. A .txa is not 
necessary if you are simply synchronizing two dictionaries, both of which will survive the synchronization. 
5. CLICK on the Next > button to continue. 
 
 
Select the Source Files to Synchronize 
Select the files, views, and tables within the Clarion data dictionary to include in the synchronization process. The 
Synchronizer Wizard provides two file lists for the dictionary: on the left is a list of files not synchronized and on the right is 
a list of files to synchronize. Depending on the database server, the list may show filenames, table names, owner names, 
etc. 
6. CLICK on the > button to select the Customer file and related files. 
7. CLICK on the Next > button. 
8. CLICK on the >> button to move all the files from the left to the right. 
This synchronizes all files from Master.DCT to Project.DCT. 
9. CLICK on the Next > button to continue. 
 
 
Set the Synchronizer Options 
10. If it‘s not already cleared, clear the Generate Data Conversion Program box. 
The Dictionary Synchronizer options control how the Synchronizer begins the synchronization. You may change 
these settings later on in the process (in the Synchronize Dictionaries dialog). See the Dictionary Synchronizer 
Options for more information on these settings. 


---

IDE User's Guide 
48 
 
 
 
 
This page lets you request a data conversion program to convert existing data to the new format. Also, the 
Matchings button sets rules for matching dictionary items. The default rules match primarily on file and field names. 
11. CLICK on the Finish button to accept the defaults and continue. 
 
 
Synchronize Dictionaries Dialog 
When you "finish" the Synchronizer Wizard, it loads, analyzes, and compares the two dictionaries, then opens the 
Synchronize Dictionaries dialog where you complete the synchronization process. 
 
 
 
The Synchronize Dictionaries dialog compares the two data dictionaries, item by item and lets you resolve any differences 
between them. 
 
 
1. CLICK the Dictionary item (first item in the list) to select it. 
Actions you apply to the selected item cascade to all its children. 
The Synchronize Dictionaries dialog uses a "file centric" hierarchical list to compare the dictionaries. Beneath each 
item in the list, the dialog nests the item‘s properties and components (files, fields, keys, relationships, and aliases). 
The Synchronize Dictionaries dialog uses color to provide information about the synchronization process: 
Blue 
indicates no action is applied, and the item is either different than its matching item or it has no matching item. 


---

User's Guide and Lessons 
49 
 
 
Black 
indicates an action is applied and the resulting target item is valid, or no action is applied but none is needed 
because the items already match and the target item is valid. 
Red 
indicates an action is applied and the resulting target item is not valid—the target does not support the applied 
property. Red may also indicate an invalid condition in the source dictionary—you can clean up the source dictionary 
and resynchronize, or you can ignore the invalid item and complete the current synchronization. 
Gray 
The item is not supported by the target dictionary. 
Use the navigation buttons and the corresponding navigation menu items to quickly locate new, changed, or invalid 
dictionary components. 
The Synchronize Dictionaries dialog uses action indicators to show the action applied to each item. Action indicators 
are at the left side of the Destination (target) column. The question mark ( ? ) indicates no decision as yet. 
A gray action indicator indicates a cascaded (or inherited) action—the action was originally applied to a parent (full 
color indicator) and the child has inherited the action (gray indicator). 
2. Right-click on the Dictionary item (first item in the list), and choose Copy to MoreData from the popup menu to 
apply the action to the selected items. 
The action cascades to all children of the selected item—that is, to all items in the dictionary. 
When you select Copy to Project.DCT, the Action Indicator changes to a right arrow ( 
 ) for matched items, and 
to an exclamation point ( ! ) for unmatched items. 
The right arrow 
) indicates the synchronizer will copy the item‘s properties from the source to the target. 
The exclamation point ( ! ) indicates the synchronizer will ignore the suggested action for unmatched items. This is 
because the Copy to action only changes existing items in the target dictionary—it does not add new items. 
3. Press CTRL + Z to undo the Copy to action. 
The Action Indicator reverts to the question mark ( ? ) — indicating no decision. 
Undo may be applied multiple times. It undoes actions in LIFO (Last In First Out) order. 
4. RIGHT-CLICK the Dictionary item (first item in the list), then choose Merge Into from the popup menu. 
When you select Merge Into, the Action Indicator changes to a right arrow 
) for matched items, and to a plus 
sign ( + ) for unmatched items. A multi-item indicator on a parent item ( 
 ) indicates different actions for different 
children. For example, a file may contain both matching fields (right arrow) and new fields (plus sign). 
The right arrow 
) indicates the synchronizer will copy the item‘s properties from the source to the target. 
The plus sign ( + ) indicates the synchronizer will add the marked items to the target dictionary. This is because the 
Merge Into action not only changes existing items in the target dictionary, it also adds items. 
A gray action indicator indicates a cascaded (or inherited) action—the action was originally applied to a parent (full 
color indicator) and the child has inherited the action (gray indicator). 
5. Press the OK button to complete the synchronization and update the Project.DCT. 
The Dictionary Editor dialog shows the updated Project.DCT. 
The Project.DCT now matches the Master.dct. 


---

IDE User's Guide 
50 
 
 
 
6. Press the Save and Close button 
to close the Project.DCT. 
This dictionary now contains all the same information (properties, files, fields, and relationships) as the Master.dct; 
however, these two .dct files are not identical. The Project.DCT will work with the MoreData.app, and the Master.dct 
will work with the Master.app, but the converse is not true—the dictionaries are not interchangeable because their 
internal file, field, and key numbers may be different. 
 
 
Remake the Master Application 
Starting Point: 
The Clarion environment should be open. 
 
 
1. Choose File  New  Solution, Project or Application (CTRL + SHIFT + N). 
The New Project window is displayed: 
 
 
2. Select the Clarion for Window Category, and then select the Application from Txa Quick Start 
3. Enter Master in the Application QuickStart Name, change the location to C:\Clarion7\Lessons\SyncLesson, and 
uncheck the Auto create project subdir box as shown above. 
4. Press the Create button. 


---

User's Guide and Lessons 
51 
 
 
This opens the Select TXAFile dialog. 
5. Select Lesson.txa from the list, then press the Open button. 
6. Press the Replace All button when prompted for Procedure name clash. 
An Error Editor dialog warns you that the .TXA specifies a different dictionary than the application. Since we just 
synchronized the two DCT files, this warning can be safely ignored. 
7. Press the Close button to ignore the warning. 
You can now make and run the Lesson application using the synchronized Qwktutor.dct, and you can make and 
run the Qwktutor application with the same Qwktutor.dct! 
 
 
 
Summary 
When you replace a data dictionary, you must take the following steps to preserve the internal relationships between the 
application and the data dictionary: first, create a text application file (.TXA), then update the data dictionary, finally create 
a new application (.APP) from the text application file (.TXA). 
By using the Dictionary Synchronizer to update the Qwktutor.dct (as opposed to simply replacing it with a copy of the 
Tutorial.dct), you are able to see exactly which items changed and you can intelligently manage those changes; if both 
dictionaries have changed, you can incorporate the changes from both dictionaries by synchronizing each dictionary with 
the other; finally, the Dictionary Synchronizer can generate a Clarion program to convert your existing data to the new 
data format. 
 
 
 
 
Review the Dictionary Synchronizer Log 
The Dictionary Synchronizer creates a log to help with the debugging process and to allow batch synchronizations (see 
the Batch Synchronization help topic for more information). 
For every synchronization, the Dictionary Synchronizer creates a log file with the pathname you specify. This log serves 
two purposes: it can be used to rerun a synchronization in batch mode, and it should be submitted with any bug reports 
along with the synchronized data dictionaries to aid in the debugging process. 
The synchronization from the first part of this lesson created a log file ..\SyncTutr\SYNLOG.TXT. If you browse this file 
you will see the following: 
 
 
CMD(DCT(Clarion Dictionary-C:\Clarion7\Lessons\SyncLesson\Project.DCT)) 
CMD(DCT(Clarion Dictionary-C:\Clarion7\Lessons\SyncLesson\master.dct)) 
CMD(MATCH_Files(MatchByName)) 
CMD(MATCH_Fields(MatchByName)) 
CMD(MATCH_Keys(MatchByComponent)) 
CMD(MATCH_Alias(MatchByName)) 
CMD(SortFiles(FALSE)) 
CMD(SortFields(FALSE)) 
CMD(SortKeys(FALSE)) 
CMD(Hide(FALSE)) 
CMD(Convert(FALSE)) 


---

IDE User's Guide 
52 
 
 
 
CMD(AutoCorrect(FALSE)) 
CMD(GenDBAScript(FALSE) 
) CMD(CWSource(FALSE)) 
CMD(StopAfterMatch(FALSE)) 
CMD(StopBeforeLastCmd(TRUE)) 
## FILTER(CLARION)
Add,FullCluster,e247e4e1-7e83-4e51-941c-5a42029072ac 
## END_FILTER
## FILTER(OTHER)
AddAll,FullCluster 
## , END_FILTER
! SET_ERROR(Field,Customer:CustNumber,DERIVEDFROM,FldDerivedFreeze) 
! SET_ERROR(Field,Customer:CustNumber,FREEZE,FldDerivedFreeze) 
CMD(OP_Copy(FALSE,Dictionary,master,Object)) 
! RESET_ERROR(Field,Customer:CustNumber,DERIVEDFROM,FldDerivedFreeze) 
CMD(EVENT(Undo)) 
! SET_ERROR(Field,Customer:CustNumber,DERIVEDFROM,FldDerivedFreeze) 
! SET_ERROR(Field,Customer:CustNumber,FREEZE,FldDerivedFreeze) 
CMD(OP_Merge(FALSE,Dictionary,master,Object)) 
! RESET_ERROR(Field,Customer:CustNumber,DERIVEDFROM,FldDerivedFreeze) 
## CMD(EVENT(OK))
 
If a synchronization fails, the Clarion environment tries to create a log called C70log.txt in the current directory. Please 
submit this log, the synlog.txt file, and the synchronized data dictionaries and with your bug reports. 
Each Synchronizer Server (Oracle, MSSQL, Pervasive, etc.) calls the corresponding database driver to collect information 
from the database. Therefore, you can also enable database driver logging to trace the Synchronizer Server calls. For 
more information see the Debugging your SQL Application topic. 
 
 
Convert Existing Data to New Format 
 
 
The Dictionary Synchronizer optionally generates a Clarion program to convert existing data to the new format. 
 
 
Starting Point: 
Open the \SyncLesson\Master.dct with the Clarion environment. 
 
 
Add a Field to the Master Dictionary 
1. In the DCT Explorer, select the Customer file. 
2. In the Fields Quick View, select the FirstName field, then press the Add 
button. 


---

User's Guide and Lessons 
53 
 
 
3. In the Column Name field, type MiddleName, then press TAB to the next field, and then press the OK button. 
4. Press the Cancel button to stop inserting fields. 
5. Press the 
 button in the IDE toolbar to save the Master.dct. 
 
Synchronize the Project Dictionary 
 
 
 
1. Press the Synchronize button in the DCT Explorer to start the Synchronizer Wizard. 
The Synchronizer Wizard is opened. 
2. Press the Next > button to start a new synchronization. 
3. Press the ellipsis (...) button to select the Project.dct, then press the Open button. 
4. CLICK on the Next > button to continue. 
5. CLICK on the Next > button to make Project.dct the target dictionary. 
 
 
 
Set Options to Generate Conversion Program 
1. CLICK on the >> button to select all Master.dct files. 
2. CLICK on the Next > button to continue. 
3. CLICK on the >> button to select all Project.dct files. 
4. CLICK on the Next > button to continue. 
5. Make sure that the Generate Data Conversion Program check box is checked. 
6. CLICK on the Finish button to open the Synchronize Dictionaries dialog. 
 
 
Finish the Synchronization and Generate the Program 


---

IDE User's Guide 
54 
 
 
1. In the Synchronize Dictionaries dialog, right-click the Dictionary item (first item in the list), then choose Add to 
Project from the popup menu. 
This adds all new items (MiddleName field) to the Project.dct. 
2. Press the OK button to complete the synchronization, update the Project.dct, and generate the data conversion 
program. You may be prompted to save the CONVERT.PRJ project file, and make sure that it is saved in the 
..\SyncLesson folder. 
The Synchronizer generates the conversion program components into the working directory (c:\SyncTutr). The 
conversion program consists of the following components: 
 
Clacvt_1.clw 
file declarations, procedure definitions, field assignments 
Convert.clw 
program map, class declarations, initialization 
Convert.prj 
project file to compile and link the program 
 
3. Press the Close button to close the Master.dct. 
 
 
Make and Run the Conversion Program 
1. Open the Convert.PRJ file in the ..\SyncLesson folder (choose File  Open  Solution, Project or Application. 
2. Press the 
 button to make and run the conversion program. 
The conversion program lets you select the specific data files to convert to the new format. The conversion program 
optionally backs up the files you select to the backup folder you specify. 
The conversion program handles new files as well as changed files. This gives you the framework to create and 
prime new files or to split one file into two new related files. You can edit the Clacvt_1.clw source code to prime 
records and make custom field assignments as needed. 
3. Press the Proceed button to convert the Customer file, or press the Cancel button to abort the conversion. 
 
 
 
 
 
Create an SQL Database from a Clarion Dictionary 
The Dictionary Synchronizer can create an entire Data Dictionary, including relationships, from an existing database in a 
single pass. Conversely, it can create a database from an existing Clarion Data Dictionary. This part of the lesson shows 
you how to create a database from a Clarion Data Dictionary. 
In the SQL case, the Synchronizer generates a SQL script you can run to create the database; in the Btrieve case, the 
Synchronizer actually creates DDF files that define the database. 
 
 
Apply this part of the lesson to your preferred SQL database (MSSQL, Oracle, Pervasive, SQLAnywhere, or AS/400) 
 
 
Create an SQL Database Definition 
 
 
Starting Point: 


---

User's Guide and Lessons 
55 
 
 
The \SyncLesson\Master.dct is open and you have a valid SQL based target in mind. 
 
 
1. In the DCT Explorer toolbar, press the Synchronize button to start the Synchronizer Wizard. 
2. CLICK on the Next > button to start a new synchronization. 
3. Choose your SQL platform from the Synchronize With drop list. 
 
 
Set the SQL Database Definition Destination Folder 
1. Press the Select other dictionary ellipsis button (...) to select the relative location or definition of the SQL data 
definition file. 
This opens the Select Dictionary dialog (a Windows file dialog). 
With SQL databases, specify the connection information in the Connection, User ID, and Password fields, then 
press the OK button. 
The Clarion SQL drivers attach to the proper interface needed for the selected format. 
This connection screen will vary from driver to driver. 
 
ADO: Connection, User ID, and Password 
Pervasive (Btrieve): Specify a DDF file to generate. 
Microsoft SQL: Server, Database, Login ID, Password, and Trusted connection options 
Oracle: HostName, User Name, Password 
ODBC: Datasource, User ID, Password 
Pervasive (SQL) – Choose from Database or DDF source, Owners, Username, Password 
SQL Anywhere – Database, User ID, Password 
 
 
Make sure to consult your SQL documentation for the proper connection settings. 
The default database filter excludes system tables from the synchronization process. Generally your applications do 
not need access to system tables. 
 
 
2. CLICK on the Next > button to continue. 
 
 
Set the Synchronizer Source and Target 
1. CLICK on the From ..\Lesson.dct To \SYNCTUTR\your database radio button to make \SyncTutr the target 
folder for the conversion script. 
If your database can only be opened READ-ONLY, you will not be able to proceed. Consult your system 
administrator, or check your security rights before continuing. 
2. CLICK on the Next > button to continue. 
 
 
Set the Files to Synchronize 
3. CLICK on the >> button to include all the Lesson.dct files for synchronization. 
4. Highlight the FieldPool column, and press the < button to move this back to the Do Not Synchronize list. 
5. CLICK on the Next > button to continue. 


---

IDE User's Guide 
56 
 
 
6. CLICK on the Next > button to bypass the SQL target tables and continue. 
Set the Synchronizer Options 
7. CLICK on the Finish button to accept the default synchronizer options and open the Synchronize Dictionaries 
dialog. 
 
 
Add the Dictionary Information to the SQL Database 
8. In the Synchronize Dictionaries dialog, RIGHT-CLICK the Dictionary item (first item in the list), then choose Add 
To (SQL target database) from the popup menu. 
The Action Indicator changes to a plus sign ( + ) for all items. The plus sign indicates the synchronizer will "add" the 
marked items to the target database. 
9. Press the OK button to complete the synchronization and create the SQL database definition. 
In the Btrieve case, the Synchronizer writes .ddf files to the path you specified. 
In the SQL case, the Synchronizer writes an SQL script (an .sql file instead of a .dct or .ddf file). The Synchronizer 
prompts you for the pathname of the script file. Type Lesson.sql in the Filename field of the Windows save file 
dialog. 
 
 
The script (..\SyncLesson\Lesson.sql) looks something like the following: 
 
 
## SET QUOTED_IDENTIFIER ON
CREATE TABLE Customer( 
CustNumber INT, 
Company CHAR(20), 
FirstName CHAR(20), 
MiddleName CHAR(20), 
LastName CHAR(20), 
Address CHAR(20), 
City CHAR(20), 
State CHAR(2), 
CHECK(State IN ('AL', 'MS', 'FL', 'GA', 'LA', 'SC')), 
ZipCode INT, 
CONSTRAINT KeyCustNumber PRIMARY KEY (CustNumber)) 
CREATE INDEX KeyCompany ON Customer(Company) 
CREATE INDEX KeyZipCode ON Customer(ZipCode) 
 
 
CREATE TABLE Orders( 
CustNumber INT, 
OrderNumber SMALLINT, 
InvoiceAmount DECIMAL(7,2), 
OrderDate INT DEFAULT (getdate()), 
OrderNote CHAR(80), 
CONSTRAINT KeyOrderNumber PRIMARY KEY (OrderNumber)) 


---

User's Guide and Lessons 
57 
 
 
 
CREATE INDEX KeyCustNumber ON Orders(CustNumber) 
 
 
CREATE TABLE Detail( 
OrderNumber SMALLINT, 
ProdNumber SMALLINT, 
Quantity SMALLINT, 
ProdAmount DECIMAL(5,2), 
TaxRate DECIMAL(3,2)) 
CREATE INDEX KeyProdNumber ON Detail(ProdNumber) 
CREATE INDEX KeyOrderNumber ON Detail(OrderNumber) 
 
CREATE TABLE Products( 
ProdNumber SMALLINT, 
ProdDesc CHAR(25), 
ProdAmount DECIMAL(5,2), 
TaxRate DECIMAL(3,2), 
CONSTRAINT KeyProdNumber PRIMARY KEY (ProdNumber)) 
CREATE INDEX KeyProdDesc ON Products(ProdDesc) 
 
CREATE TABLE Phones( 
PhoneID SMALLINT, 
CustNum INT, 
Area INT, 
Phone INT, 
Description CHAR(20), 
CONSTRAINT KeyPhoneID PRIMARY KEY (PhoneID)) 
CREATE INDEX KeyCustNumber ON Phones(CustNum) 
 
 
ALTER TABLE Phones ADD 
CONSTRAINT KeyCustNumber1 FOREIGN KEY (CustNum) 
REFERENCES Customer(CustNumber) 
 
ALTER TABLE Orders ADD 
CONSTRAINT KeyCustNumber2 FOREIGN KEY (CustNumber) 
REFERENCES Customer(CustNumber) 
 
ALTER TABLE Detail ADD 
CONSTRAINT KeyOrderNumber1 FOREIGN KEY (OrderNumber) 
REFERENCES Orders(OrderNumber) 


---

IDE User's Guide 
58 
 
 
 
ALTER TABLE Detail ADD 
CONSTRAINT KeyProdNumber1 FOREIGN KEY (ProdNumber) 
REFERENCES Products(ProdNumber) 
 
 
 
 
Create a Clarion Data Dictionary from an SQL Database 
The Dictionary Synchronizer can create an entire Data Dictionary from an existing database in a single pass. Conversely, 
it can create a database from a Clarion Data Dictionary. This part of the lesson shows you how to create a Clarion Data 
Dictionary from an existing SQL based database. 
 
 
To synchronize an SQL database, you must have read privileges for the database system tables—except for security 
or access tables (user ids, passwords, privileges, etc.) 
 
 
Create an Empty Dictionary: 
 
 
Starting Point: 
The Clarion Environment is open, your SQL database driver is registered, and the database is started (if 
applicable). 
 
 
1. From the IDE Start Page, select the Dictionaries category link, and press the New Dictionary button. 
This opens the Windows Save As file dialog. 
2. In the File name field, type SQLDemo, then press the Save button. 
This opens the Dictionary dialog to the empty data dictionary. 
 
3. In the DCT Explorer toolbar, press the Synchronize button 
to start the Synchronizer Wizard. 
4. CLICK on the Next > button to start a new synchronization. 
5. Choose your SQL database type from the Synchronize With drop list. 
 
 
Select the SQL Database 
1. Press the ellipsis button to select the SQL database. 
2. Specify the appropriate connection information, then press the OK button. 
If you are using the Oracle Demo database supplied with Personal Oracle. The host is local (2:), the Username is 
DEMO, and the Password is DEMO. 
The host for later versions of Personal Oracle (7.3 and 8) is blank (not 2:). 
The default database filter excludes system tables from the synchronization process. Generally your applications do 
not need access to system tables. 
3. CLICK on the Next > button to continue. 


---

User's Guide and Lessons 
59 
 
 
Set the Synchronizer Source and Target 
1. CLICK on the From ..(your SQL target) To ..\SQLDemo.dct radio button to make SQLDemo.dct the target 
dictionary. 
2. CLICK on the Next > button to continue. 
 
 
Select the Tables to Synchronize 
1. CLICK on the Next > button to select files and continue. 
2. CLICK on a desired table name, then click on the > button to select the table and all related tables (if applicable). 
3. CLICK on the Next > button to accept the synchronizer options and continue. 
4. CLICK on the Finish button to continue. 
The synchronizer collects information from the SQL database. 
3. In the Synchronize Dictionaries dialog, RIGHT-CLICK the Dictionary item (first item in the list), then choose 
Merge Into from the popup menu. 
The Action Indicator changes to a plus sign ( + ) for all items. The plus sign indicates the synchronizer will add the 
marked items to the target data dictionary. 
4. Press the OK button to complete the synchronization and complete the SQLDemo.dct dictionary. 
The Dictionary dialog shows the completed SQLDemo.dct dictionary, including file relationships. 
5. Press the Save and Close button to close and save the SQLDemo.dct file. 
6. Run the Application Wizard against the SQLDemo.dct file to create a complete application to access the target 
SQL database. 


---

IDE User's Guide 
60 
 
 
 
Lesson 8 - Advanced Features of the Dictionary Editor 
 
Overview 
If you could only create tables, columns, keys and relationships, the Clarion Dictionary Editor would still be a useful and 
powerful tool. However, Clarion takes Application Development technology to the next level by providing additional 
options in the dictionary that help to set values and control types. This can determine how the application is generated 
(and even behaves). A majority of these design "gems" are located back in the Column properties window. Let‘s examine 
a few of these options. 
 
 
Validity Checks - The Heart of Data Validation 
In the Column Properties window, the Validity Checks Tab option is chosen to establish rules for the entry of valid data 
into a control. The Application Generator uses information defined here when creating and maintaining controls. 
Here is a typical data validity scenario. When the user completes the column and shifts focus to another control, the 
application will sound a warning beep and set focus back to the control if the data is not valid. 
The validity checks window contains a number of radio buttons that allow you to specify a particular data validation 
method. Here is a brief description of each: 
No Checks 
Selecting this option indicates that no data validation should be performed for this control. 
Cannot Be Zero Or Blank 
Specifies that some type of information must be entered for this control (The data is required). 
Must Be In Numeric Range 
A numeric value must be entered in the control and the value entered must be between the Lowest and Highest value 
specified, inclusively. 
Must Be True Or False 
Used to create a checkbox control. If a checkbox is selected (check mark is displayed) the value in the control 
associated with the checkbox is 1 (true). If the checkbox is not selected, the value in the control would be 0 (false). 
Must Be In Table 
Specifies that the value entered into the control must exist in another table. In other words, the value entered is 
"checked" against a master list of valid values. Validating state abbreviations is a common use of this option. Table 
relationships must exist before this option may be selected. 
Must Be In List 
If this option is selected, a list of valid values for this control is entered in the Choices column. This option is intended 
for use with controls that have a limited number (5 or less are recommended) of possible values. For example, if a 
control called TITLE is being defined, possible choices might be: Mr. Mrs. Ms. Dr.; valid choices are separated with a 
vertical bar. The Application Generator will create Radio Buttons or a Drop Box for the choices entered. 
 
 
Fine Tuning Your Dictionary 
There are a couple of other areas to explore before completing this lesson. 
In the Help tab of the Column Properties window, there are three options for each column that directly affect the levels of 
help you wish to make available in your applications: 
• 
For external help tables that you create for your programs, a HelpID can be assigned here to reference a selected 
column. 
• 
For custom messages to be displayed on a Windows Status Bar, type an appropriate message in the Message 
entry dialog. 
• 
To create custom "bubble help" for each column in your program, type an appropriate help message in the Tool 
Tip entry dialog. 


---

User's Guide and Lessons 
61 
 
 
 
Finally, the Window and Report tabs in the Column Properties window controls the default population of the Application 
Generator. In other words, the appearance and characteristics of a column or control can be "pre-set" when populated on 
a window or report structure by accessing or modifying certain options. 
An example of using this option would be to designate an auto-populate, unique column as a STRING column (instead of 
the default ENTRY column) to prevent a user from modifying its contents. 


---

IDE User's Guide 
62 
 
 
 
Windows Design Issues 
 
This chapter provides an introduction to: 
• 
The design principles which Microsoft suggests for designing the user interface of Windows-based applications. 
• 
Event driven programming and how it should influence your application‘s design process. 
• 
The types of windows, controls, cursors, and other objects common to Windows applications. 
• 
The standard menus and menu commands recommended for Windows applications. 
• 
The use of color and how it relates to the user. 
 
 
Design Principles 
If you make your program look and act like other Windows programs, your users will learn it more quickly, and feel more 
confident using it to accomplish the tasks you designed it to do. The Graphical User Interface (GUI) environment demands 
that you address your users on their terms. The program design must reflect that the user is in control, both visually and in 
the underlying structure of program flow. 
Apple, in its Human Interface Guidelines, IBM, in its Common User Access: Advanced Interface Design Guide, and 
Microsoft, in The Windows Interface: an Application Design Guide have all published detailed design principles for 
software designers working in popular GUI environments. Creating a standard for program design offers these 
advantages: 
u Given consistency between applications, users learn new applications more quickly and easily, minimizing the need for 
training. 
u Consistency between applications increases the level of confidence in the user, resulting in increased productivity. 
User Control 
There are two especially important Windows design principles for the Clarion programmer to keep in mind when designing 
the user interface. The first is user control—providing a real-world based metaphor for the program‘s organization, and 
maintaining a consistent look and feel for all parts of the program, builds the user‘s confidence. The second is to 
remember that Windows programming is event driven—the user decides the next action. The programmer‘s responsibility 
is to provide a visual list of options the user can act upon. 
Metaphors 
Your users may not have years of experience using a wide variety of programs. Providing a metaphor from the real world 
will help provide a ‗setting‘ or group of expectations to apply to your program. A word processing program, for example, 
uses a ‗paper‘ metaphor—the document is like a piece of paper to write on, erase characters from, etc. Many database 
programs use Rolodex card metaphors. By establishing a relation to the real world, you increase the comfort level of your 
users, and actively engage them in the work of the program. 
 
 
Visual Consistency 
Visual consistency is very important. As much as possible, an application should use a single way to implement actions. A 
user learning a new procedure in your program builds upon prior experience with other procedures in the same program. 
Creating a standard look for your dialog boxes, and making screens for similar tasks look like one another, also reduces 
the time it takes you to design the different screens your program requires. 


---

User's Guide and Lessons 
63 
 
 
Directness 
Directness makes a user feel they are in charge. Moving a document from one folder to another, or moving one icon to 
another, such as the Recycle Bin icon, can seem to a user to be a real action. Clarion provides drag-and-drop server 
support, which lets you create, for example, an icon with a picture of a person on it, representing an employee record. A 
user might drag the icon to another representing money, to open a dialog box displaying the employees‘s payroll records. 
 
 
Simplicity 
Simplicity is usually the best design. Cluttering the screen with too many windows, buttons, icons, lists and other objects 
can confuse the user. Dialog boxes especially, usually must fit in a small space, so their messages must be simple. The 
same is true for colors. Limit the use of colors to areas where they are needed to provide emphasis, such as red text for 
an important message. 
 
 
Feedback 
Let the user know what‘s going on—provide feedback. When the user chooses a command or begins an operation, visual 
feedback should confirm it is being carried out. The confirmation may be graphical, such as a cursor change, or simply a 
progress bar or message on the status bar. If there will be a delay while the program finishes another operation, inform 
the user, and advise, if possible, how long it will take. 
 
 
Plain Language 
Your application should use plain language. When designing an application for a corporate environment, technical terms 
are often essential. Watch out for the times when plain English is better. Of special importance to the programmer, who 
may be new to Windows programming—beware of "Window-isms." It‘s very easy to create two buttons marked "OK" and 
"Cancel." Yet "Yes" and "No" are far better button labels when the question is: "Do you wish to delete this Customer?" 


---

IDE User's Guide 
64 
 
 
 
Event Driven Programming 
Related to user control issues, and the most important concept for new Windows programmers, is that you must design 
Windows programs to be event-driven. This means controlled by messages. In a multi-tasking environment, a program 
simply cannot direct the sequence of program action—the user directs it. 
The underlying structure of Windows is such that the operating system informs the program with messages just what it is 
the user wants the program to do. This is the opposite of DOS programming. 
Windows messages tell a program when a menu is selected, when a window is selected, when the user wants to shut 
down the operating system—the MSDN documentation devotes over 200 pages just to listing and explaining the different 
messages. Most programming languages require elaborate message handling procedures to branch program flow upon 
receiving different types of Windows messages. 
Clarion automatically handles the housekeeping associated with message handling. The ACCEPT loop frees the Clarion 
programmer from worrying about system messages. Yet you still must consider the event-driven model when designing 
your program. 
A Windows program must constantly look for input—in the form of data entry in an edit box, for example. In a window with 
several controls, the user can TAB or CLICK with the mouse to make any of them active. You must plan your input dialogs 
accordingly. 
Additionally, your users will expect a complete set of user interface elements, including menus, multiple windows and 
graphical controls, all available simultaneously. 
You may create an application which allows the user to open two windows, with markedly different functions. Clarion will 
automatically handle events generated within each window. Yet what about the menu commands, or the tool bar? You 
should plan these so that the commands will act on any active window. Clarion helps you do this automatically when 
creating an application using Multiple Document Interface. There may be times, however, when you may need to 
manually disable and re-enable menu commands. 
Finally, the event-driven model should influence the windows you design for your application. Plan on using your main 
application window as the backbone for your program. Generate another window only upon some user action in the main 
window. 
Background Processing 
Background processing is another important concept for Windows programmers. In a multi-tasking environment, your 
program should always leave the user in control, especially when it is doing a lengthy process such as reading or writing a 
large file. 
At the language level, Clarion supports background processing through the invocation and detection of TIMER events. 
That is, specifying a TIMER for a WINDOW tells the operating system to generate a timer event for the Window at 
regular intervals. The TIMER Events may be detected and acted upon within the WINDOW‘s ACCEPT statement. Your 
program performs a small portion of a larger process for each timer event. The net effect is that your program can work 
concurrently with other programs that employ a similar technique. 
 
See the Language Reference for more information on TIMER, ACCEPT, EVENT(). 
At the template level, all the Clarion templates automatically support background processing with the TIMER technique 
described above. The ABC Templates dynamically adjust records per cycle to optimize sharing of machine resources. 
You can control the sharing of machine resources by adjusting the amount of time between timer events and the amount 
of processing that occurs for each timer event. For example, a small TIMER interval with a high volume of processing per 
interval hogs resources, whereas a large TIMER interval with a small volume of processing per interval lets the machine 
sit idle. 


---

User's Guide and Lessons 
65 
 
 
 
A reasonable TIMER interval ranges from 1/100 to 30/100 of a second depending on the process performed and the 
hardware doing the processing. 
 
MyWindow WINDOW(‘With a Timer’),TIMER(1) !1/100 of a second 
... 
## CODE
... 
MyWindow{PROP:Timer} = 30 !30/100 of a second 
A reasonable number of iterations or LOOP cycles per interval may range from 1 to 1000, depending on the length of the 
timer interval, the process performed, and the hardware doing the processing. See the RecordsPerCycle variable 
generated by the Process template. 


---

IDE User's Guide 
66 
 
 
 
Windows 
This section describes common window types. Choosing the right window for the right job helps your users get the most 
out of your program. 
Multiple Document Interface (MDI) 
Clarion enables Multiple Document Interface (MDI) programs. This manages multiple documents or multiple views of the 
same document, each in a separate window which appears inside the main application window. If the user resizes the 
application window to make it smaller than the document window, the document window will appear clipped. 
There are three types of windows in a typical MDI program: application, document and dialog boxes. 
 
 
Application Window 
The application window should usually "contain" all the other windows your program may generate. If you open a browse 
window, it should appear inside the application window. If a user resizes an application window to a smaller size, you may 
allow your other windows to appear partially outside it. Additionally, you may allow users to move moveable dialog boxes 
outside the application window. 
Application windows should always contain a title bar that contains the name of your application. Microsoft recommends 
that application windows also contain resizable frames, a Control-menu box, and Minimize and Restore buttons. In 
Clarion, you add these attributes to the window with the Application Properties dialog. 
 
 
To create an application window with Clarion, you select Frame - Multiple Document Main Menu from the Select 
Procedure Type – Templates dialog, Default MDI Frame in the Select Procedure Type – Defaults or select Application 
Main MDI Frame in the New Structure dialog, or declare an APPLICATION structure in your source code. 
 
 
Document Windows and Dialog Boxes 
Document windows and dialog boxes are very similar in that they are both defined as Clarion WINDOW structures. They 
differ in the conventional context in which they are commonly used and the conventions regarding appearance and 
attributes. In many cases, the difference is not distinguishable and does not matter. The generic term for both document 
windows and dialog boxes is "window" and that is the term used throughout this text. 
 
 
Document Windows 
Microsoft recommends each document window contain a title bar with the name of the document, a system menu, and a 
Maximize button. Optionally, you can include a minimize button. Document windows usually display data. For example, in 
the Windows environment, the "Main" program group window that appears when you DOUBLE-CLICK on the "Main" icon 
in the Program Manager‘s desktop is a document window. 
 
 
Dialog Boxes 
The Windows design guidelines for dialog boxes are very flexible. They may be movable, or maintain a fixed position. 
They may have a single size, or a ‗More >>‘ button to make it unfold and offer additional options. They may be modal or 
modeless. They may present a brief message with only an ‗OK‘ option, or provide complex choices, controls, and entry 
options. 


---

User's Guide and Lessons 
67 
 
 
 
Here are a few pointers, which will help you design windows (Document Windows and Dialog Boxes) that are easier to 
use. 
 
 
• 
Using either the caption bar or static text in the window, briefly explain the function of the window, or indicate 
which command caused it to appear. 
 
 
• 
Set as many controls to the default setting as possible, so that you require the least amount of entry on the part of 
the user. 
 
 
• 
Place the most important information at the upper left, the least important at the lower right. Your users read from 
left to right, top to bottom—this is the natural way in which they expect to enter information. 
 
 
• 
Set the focus to the first entry box. This lets the user type a word or words at the keyboard without repositioning 
the cursor. 
 
 
• 
Place default buttons—the most likely user choice—on the right. This gives the user to opportunity to ‗read‘ the 
choices on the left before presenting the ‗decision.‘ 
 
 
• 
When presenting a brief message, take advantage of the default icons available with the MESSAGE function. The 
Stop, Information, and Question icons are familiar to users from other applications. 


---

IDE User's Guide 
68 
 
 
 
Window Elements 
This section describes common window elements. Choosing the right element for the job at hand helps your users get the 
most out of your program. 
 
 
Buttons 
A button initiates an action. When the user presses a button, the button appears to be depressed. When a button action is 
unavailable, the button label should be dimmed. 
Clarion lets you use text, graphical labels (picture buttons), or both. If you are using picture buttons you should include 
tool tips to allow the user to see, in words, what action the button will initiate. Stick to standard bitmaps (such as the icons 
many bestselling applications use for File Open, File Save, etc). Too many picture buttons in a window can be confusing 
to the user. Some reviewers have accused programs of "iconitis"—having so many graphical buttons on the screen at 
once that it‘s impossible for users to remember which button executes which action. 
 
 
Buttons can perform several types of actions. 
 
 
• 
A button may initiate an action. 
 
 
• 
A button may close the active dialog box, then open another, related dialog. 
 
 
• 
A button may open another dialog on top of the current one, without closing the current one. 
 
 
• 
A button may "unfold" or resize the dialog window to include more options. 
 
 
• 
A button can turn the "page" on a wizard dialog. 
 
 
Always designate one button as the default. When the user presses ENTER, it will initiate the default button action. 
Microsoft also suggests that you not assign a mnemonic—for example, "&OK," which appears as OK—to a default button. 
 
 
Check Boxes 
Check boxes control true/false, yes/no, on/off or logical variables. The user toggles the state by CLICKING on the box, or 
pressing the SPACEBAR. If a check box option is unavailable, the label should be dimmed. 
 
 
Radio Buttons 
Radio buttons, also referred to as option buttons, present the user with a single choice in a mutually exclusive set of 
choices. The user may select only one at a time. If space is at a premium, and the number of choices is greater than four, 
consider a drop-down list box, which takes up less space. 
 
 
List Boxes 
List boxes display choices for the user. If a choice is unavailable, in general you should drop it from the list. If the choice is 
important enough that the user should know it is unavailable, Microsoft recommends it appear in the list box as a dimmed 
selection. 


---

User's Guide and Lessons 
69 
 
 
 
Always allow your list boxes enough room. Try to allow vertical space for three to eight choices; horizontal space for the 
average length of selection text plus several extra spaces. 
Remember that a list box can present a user with a great deal of information—keep it simple! 
 
 
Combo Boxes 
A combo box is a combination of text box and list box. They are appropriate where the data lends itself to possible 
responses, but allows the user to type in a response not in the list. 
The design guidelines for list boxes apply to combo boxes. 
 
 
Drop-Down List Boxes 
Drop-down single-selection lists perform the same function as list boxes, but take up less space. When closed, the drop- 
down is only tall enough to show one selection. Opened, the list will show more items, like a standard list box. 
Novice users often have much more difficulty selecting an item from a drop-down than from a normal list box. Whenever 
space permits, use radio buttons (for four choices or less) or normal list boxes. 
 
 
Text Boxes 
Text boxes allow the user to type in information. They may be single line or multi-line. Multi-line edit boxes should usually 
provide a vertical scroll bar. 
The standard Windows accelerator keys for copy, paste, etc., are active by default. This is useful, because it enables the 
user to copy, for example, a paragraph from another application, then paste it directly into a multi-line text box in your 
application. For this reason, we recommend you do not reassign the default windows editing shortcut keys—such as 
CTRL+C for copying or CTRL+V for pasting—to alternate commands in your Clarion application. 
 
 
Fixed-length, auto-exit text boxes may speed up data entry. As soon as the user fills the text box (by typing the maximum 
allowable characters), the focus moves to the next control. Microsoft recommends applications use this type of text box 
sparingly, as the shift of focus may be disconcerting if it catches a user by surprise. We recommend using this type of text 
box when there are many fields to enter in a dialog. For dialogs with only a few fields, the programmer should try to 
anticipate what the end user will expect, and choose accordingly. 
 
 
Clarion lets you select the font for text boxes. We suggest using the default system font. Microsoft specifically chose this 
font for menus and other system items because it is especially easy to read on a monitor. 
 
 
Spin Boxes 
Spin boxes are specialized text boxes with a pair of arrows (spin buttons) attached to the right of the text box. Spin boxes 
accept a limited set of values, which the user may type in, or by using the arrows, increase or decrease the value by a 
specified unit. Spin boxes can provide an alternative to drop-down lists when the set of values is limited in quantity and fits 
into a natural progression; for example, ‗Spring, Summer, Fall, Winter.‘ 
Besides increase or decrease controls for simple numbers or choices, you may use spin boxes to manipulate values that 
consist of several components. You may display time in hours, minutes and seconds, for example. Be sure to visually 
separate each component with a relevant separator character, such as a colon. 


---

IDE User's Guide 
70 
 
 
Static Text 
Static text should present read-only information, such as directions for entering data in the other controls in the dialog box. 
You should also use static text to label controls not automatically labeled by the Window Designer, such as a text box. 
Clarion lets you select the font for static text. We suggest using the default system font. Microsoft specifically chose this 
font for menus and other system items because it is especially easy to read on a monitor. You should certainly feel free to 
make the text bigger, as in creating a ‗title‘ for a dialog box ‗form.‘ 
 
 
We also advise you to resist the temptation to use odd or too many different colors for static text. You never can tell what 
the default window background will be. 
 
 
Group Boxes 
Group boxes provide a visual grouping for related controls. They consist of a rectangular frame with a label at the upper 
left. 
A group box can guide the user directly to the controls that are most important to the task at hand. If your application 
requires a dialog with more than ten controls or fields, we highly recommend taking a moment to consider whether some 
of the controls fit into logical groups. 
 
 
Sheets and Tabs 
The Property Sheets with tabs provide another method of grouping related controls, by allowing you to place controls with 
similar or related functions on separate "pages." 
Tabbed dialogs can "flatten" your application, by reducing the number of visible controls and displaying only those that are 
most important to the task at hand. If your application requires a dialog with more than ten controls, you should consider a 
" multi-page" approach. 
Keep in mind that Required Entry fields should be on the first visible tab. 
 
 
Wizards 
The WIZARD attribute on a Property Sheet control lets you control the user‘s movement through the tab "pages." This lets 
you present a series of dialogs in a linear fashion. Optionally, you can control the next "page" based on the answers the 
user provides in previous pages. 
Wizards have become increasingly popular because they let users answer only one question at a time, decreasing the 
chances of confusion or error. 
 
 
Control Labels 
The Window Designer automatically supplies labels for many, but not all controls. You may supply labels for the other 
controls using static text. Not only will this identify the control for the user, but it also will allow keyboard users to quickly 
direct the focus to the control. 
When the user keys in the mnemonic (such as the "S" in ‗Daily Sales‘), Windows automatically directs the focus to the 
next control after the static text label. Thus, you may place ‗Daily &Sales‘ to the left of a drop-down box. When the user 
presses ALT+S, the combo box will receive the focus. The keyboard user will merely have to press the DOWN ARROW 
key to view the choices in the list. 


---

User's Guide and Lessons 
71 
 
 
 
Microsoft suggests the following guidelines for control label text: 
 
 
• 
Capitalize the first letter of each word, except for articles (e.g., a, an, the), coordinate conjunctions (e.g., and, or, 
for), prepositions (e.g., by, with) or the word "to" in infinitives. 
 
 
• 
Try to use the first letter of the first word for the mnemonic. Since the mnemonics need to be unique, however, 
this isn‘t always possible. Alternately, use another letter if it allows a stronger mnemonic link: such as the "x" in 
"Exit". If the first word in the control label is less important than another, use the other (e.g., "by Ascending 
Order"). 
 
 
• 
Choose consonants over vowels: they are more distinctive and more easily remembered. 
 
 
Microsoft also suggests the following positioning for control labels for the following controls: 
 
 
• 
Command buttons: inside the button. 
 
 
• 
Check boxes, radio buttons: to the right of the control. 
 
 
• 
Text boxes, spin boxes, lists, combo boxes: above or to the left of the control. Place a colon after the last word of 
the label. Left align the label with the section of the dialog box in which it appears. 
 
 
Cursors 
In a graphical environment such as Windows, the mouse cursor, or screen pointer, is the means by which the user shows 
the application what to do next. For example, the I-bar, or insertion point, may tell a word processing application where the 
next characters typed by the user should appear. This is a key part of the ‗event driven programming‘ referred to earlier in 
this chapter. 
Though Microsoft has not set specific guidelines for the use of each system cursor, the following uses have evolved into 
standards across GUI platforms: 
 
 
Arrow: selects controls and menu commands. I- 
beam: selects and inserts text. 
Crosshairs: draws and manipulates graphics. 
Plus sign: selects fields in an array. 
Hourglass: shows that a lengthy operation is in progress. 


---

IDE User's Guide 
72 
 
 
 
Menus 
Menus display the range of commands available for the user to execute. Windows users are accustomed to standard 
menus and commands, which appear in many different applications. If you use these same menus, new users may learn 
your application more easily, and the sense of familiarity will increase all users‘ confidence and productivity levels. 
When designing additional, custom menus and commands, bear in mind that the model for GUI design is the ‗ Noun- 
Verb.‘ principle. Apple fancifully refers to this as ‗Hey you—do this!‘ 
In the ‗Noun-Verb‘ model, the user points to something—for example, an on-screen object such as text. This is the noun. 
The model assumes that the next command action the user chooses will tell the application what to do to the noun. The 
action is the verb. If you word your menus and commands in a way that the menu - command is a short ‗do this‘ 
sentence—such as: 
"Insert Customer" 
"View  ? Transaction" 
"List Activity" 
"Select Current Group" 
…your menus will gain added clarity. 
This guideline should not severely limit you. There are times when it is most appropriate to use a single menu item to 
initiate complicated instructions, such as bringing up a dialog box with many different preferences and options for the user 
to set. When doing so, add an ellipsis (...) following the last word of the menu command. 
The following discusses the standard menu implementations recommended by Microsoft: 
 
 
File Menu 
Many database applications do not naturally lend themselves toward allowing the user to open and close external 
document files. In the simplest case, a database or databases open automatically with the application, and user editing is 
limited to editing individual rows. Clarion programmers may wish to limit commands on the file menu to those that affect 
the global operation of the application—Printer Setup and Exit, in the most extreme case. At the very minimum, your 
Clarion applications should have a File  Exit command: this is how users expect a Windows application to allow them to 
quit the program. 
 
 
New or New... 
Creates a new file with a default name such as ‗Untitled.‘ This is sometimes 
a problematical menu item when creating database applications. Unless 
your application allows the user to create a new database, or creates 
separate editable external files (such as text files) Clarion programmers 
may wish to drop this command. 
 
Open 
Displays the File Open dialog, from the Windows common dialog library. 
Allows the user to open external files. 
 
Save 
Saves the active document. For a new file, calls the Save As dialog. 
 
Save As 
Displays the Save As dialog, from the Windows common dialog library. 
 
Print or Print... 
Prints the active document, or leads to a dialog allowing the user to set print 
options. 
 
 
The Print command can be an interesting one in a database application. Many times, a database application allows the 
user only to print pre-formatted reports. 


---

User's Guide and Lessons 
73 
 
 
 
 
Other ‗docu-centric‘ Windows applications may simply go ahead and print the current document in its entirety—but a 
database application can hardly be expected to print a 30,000 record database as the default print preference. 
One solution some popular applications use is to drop the print command entirely and provide a separate Report menu. 
This is a good solution for an application with a limited number of reports. Alternatively, an application with a limited 
number of reports might also use a cascading menu, attached to the File Print command. 
 
For an application with a large number of pre-formatted reports, one solution might be to present a list box in a dialog 
window when the user selects the File Print command. 
 
 
Print Setup 
Displays the Printer Setup dialog, from the Windows common dialog library. 
This dialog allows the user to change the active printer and/or specify settings 
for the selected printer. 
 
Exit 
Closes all application windows and terminates the application. If don‘t have a 
File menu in your application, place your Exit command on the leftmost 
application menu, as the last command on the menu. 
 
 
Edit Menu 
The Edit menu usually provides commands for reversing the user‘s last action, plus the clipboard editing commands: cut, 
copy and paste. 
 
 
Undo 
The Undo command should reverse the user‘s last action. It must always be 
the first command on the Edit menu, if your application supports undo. 
 
Clearly, database programs present special problems for Undo. In general, Windows applications disable the Undo 
command after a file operation, such as when a File Save command saves an edited document to disk. A database 
application may easily present a situation in which it writes data to disk every few seconds when, for example, a user 
enters a group of new records. 
 
 
Cut 
Transfers a selected object to the clipboard and deletes it from the field. 
 
Copy 
Places a copy of a selected object in the clipboard. 
 
Paste 
Places a copy of an object previously placed in the clipboard into the current 
field. 
 
Clarion automatically enables clipboard support for Cut, Copy and Paste when in an edit box. The default accelerator keys 
for these actions are CTRL+X, CTRL+C and CTRL+V respectively. 
 
 
View Menu 
Microsoft defines the View menu as optional, and states that it includes commands for changing how the program 
presents the data to the user, without changing any of the data. As such, it presents a natural means for a database 
application to allow different browse options on a single database. 


---

IDE User's Guide 
74 
 
 
 
The View menu may also present options for displaying various interface elements such as toolbars, status bars, and 
other special controls that are part of the application window. There are no specific command text suggestions for the 
View menu. 
 
 
Window Menu 
This is an optional menu. If you choose to support the Multiple Document Interface (MDI) in your application, the Window 
menu allows the user to manipulate entire child windows. 
The commands for this menu are flexible. Common commands include: 
 
 
Tile 
Arranges child windows end-to-end, so that all are visible. 
 
Cascade 
Arranges child windows in an overlapping fashion, so that the title bar of 
each is visible. 
 
 
The Window menu may also contain a numbered list of up to nine open child windows. A number should precede each 
child window name. When the user chooses a window from the list, the window should receive the focus. 
 
 
Help Menu 
The Help menu provides the user with access to the Windows Help system. It should always be the last menu on the 
right. The Help menu usually contains the following commands: 
 
 
Contents 
Loads the Windows Help system, then opens the external Help file to the 
main contents page. 
 
Search for Help On This loads the external Help file, then automatically opens the Search 
dialog. This allows the user to type in a word; if the word appears as a 
topic title, the Help system jumps to the title. 
 
How to Use Help This opens the Windows Help system, and displays the instructions for 
using it. The file WINHELP.HLP, which Windows automatically installs, 
contains the instructions. 
 
 
Accelerator Keys 
A number of commands have gained standard accelerator (or alert, or hot) keys. When creating your application, should 
you use any of the following commands, we recommend you use the following keys: 
 
Command 
Accelerator 
 
File 
New 
## CTRL+N
File 
Open 
## CTRL+O
File 
Save 
CTRL+S, or SHIFT+F12 


---

User's Guide and Lessons 
75 
 
 
 
File  
Edit  
Exit 
Undo 
## ALT+F4
## CTRL+Z
 
 
Edit 
Cut 
## CTRL+X
Edit 
Copy 
## CTRL+C
Edit 
Paste 
## CTRL+V
Edit 
Select All 
## CTRL+A


---

IDE User's Guide 
76 
 
 
 
Color 
Color can greatly affect how your user works with your application. Microsoft does not publish standard guidelines on 
color usage—yet. When designing your application, the following guidelines may help you: 
Windows allows users to select default colors for window text and background. It‘s best to accept these default colors for 
the parts of the program that require the most data entry: the user has expressed a preference, so you should respect it! 
Without forgetting the first point, you may choose to accentuate windows and screen elements by using color. Color can 
set off specific areas in a window—it can be more effective than a group box. 
Use color to discriminate between different parts of your program. For example, you may associate one window 
background color for dialog boxes related to accounts receivable data entry, and another for payables. 
Use color to visually relate similar parts of the program. For example, you may associate one window background color 
with phone number data. 
Use standard cultural associations for special alerts. In western culture, the most ‗meaningful‘ colors are probably the 
ones on the traffic lights: red, yellow and green. You may use red to signal a halt in a procedure. You may use yellow to 
signal a warning. Green, of course, means go, all clear. 
When adding color to text elements, remember that most colors look best against a neutral grey background. If you don‘t 
use grey, be sure there is a high contrast between the text and the background color. In dim lighting, color tends to wash 
out. 
Bear in mind that 8% of males in Europe and America have some degree of color blindness. The most common type 
reduces the ability to distinguish red and green from gray. In a less common type, the user cannot distinguish between 
yellow, blue and gray. 
Remember that on monochrome LCD screens, light blue is very hard to distinguish from gray and white. 


---

User's Guide and Lessons 
77 
 
 
 


---

IDE User's Guide 
78 
 
 
 
The Application 
 
Application Generator 
Overview and Introduction 
The lessons that follow describe the heart of the Clarion IDE, the Application Generator. You will learn how to create and 
maintain an application. An application combines elements from the Clarion template language, a data dictionary, and 
optional custom source code to produce rich and robust source code modules. These modules are then compiled and 
linked to executables or libraries using the Project system. 
When you use the Application Generator, you define procedures for the major tasks you want your application to do. Then 
you describe how the procedures accomplish the tasks, and how their windows, dialogs and reports appear to the end 
user. 
 
 
Lesson 1 - Anatomy of an Application 
What makes up an application file? A quick tour of the Application Generator, then see how to create one. 
 
 
Lesson 2 - The power of the Application Wizard 
Explore the Application Wizard and its powerful options to create a ready-to-run application. 
 
 
Lesson 3 - The Application Generator Environment 
Examine in this lesson the Application Options and other configuration issues. 
 
 
Lesson 4 - The Window Designer 
Examine in detail the options and features of the Window Designer. 
 
 
Lesson 5 - Exploring the Menu/Frame Procedure 
Learn how to create menus in your application, and understand the many options available to you. 
 
 
Lesson 6 - Exploring the Browse Procedure 
Learn what is a Browse procedure, how is it used, and what variations are available to you. 
 
 
Lesson 7 - Exploring the Form (Update) Procedure 
Learn what is a Form procedure, how is it used, and what variations are available to you. 
 
 
Lesson 8 - The Report Designer 
Similar in function to the Window Designer, this tool helps you to create rich and deeply detailed reports for your 
application. Explore its options and features in this lesson. 
 
 
Lesson 9 - Exploring the Report Procedure 
Learn what is a Report procedure, how is it used, and what variations are available to you. 


---

User's Guide and Lessons 
79 
 
 
 
 
Lesson 10 - Other Procedures - (Viewer, Process, etc.) 
Explore the Viewer, Splash, and Process template procedures and their options and features. 
 
 
Lesson 11 - Global Application Properties 
Explore the application‘s global area, including standard options and features. 
 
 
Lesson 12 - Advanced Features of the Application Generator (Formula Editor, Utilities, etc.) 
The Application generator is packed with tools and utilities that make your design cycle more efficient. This lesson 
explores several of these items. 
 
 
Lesson 13 - Customizing the Application: Adding Templates 
This lesson explores the rich library of Extension, Control, and Code templates available to you. Use these templates to 
extend the power and features of your application. 
 
 
Lesson 14 - The Source Procedure 
This lesson explore a very powerful door to open in your Clarion expertise. When a template just doesn‘t fit into a feature 
or requirement of your application, what can you do? 
 
 
Lesson 15 - Customizing the Application: Source Embeds 
Sometimes a template will take your design requirements only so far. This lesson explores using Source Embeds to finish 
the job. 
 
 
Lesson 16 - SQL, ODBC and ADO application support 
Clarion is made to order when you need an application that needs access to a server-based database. In this lesson, we 
explore how to implement this design process using the Application Generator 


---

IDE User's Guide 
80 
 
 
 
Lesson 1 - Anatomy of an Application 
 
Introduction 
Once you have completed the preliminary design of the data dictionary, the next step is to decide what needs to be done 
with the data. 
Information will need to be entered so that records can be added to data tables. Existing information will need to be 
revised or deleted and reports will need to be printed. In order to accomplish these tasks, the computer needs to be given 
instructions. These instructions must be very explicit. The computer must be told every step to take and in what order to 
take each step. 
With a traditional programming language, it is the job of the programmer to write the instructions that make up a program. 
With Clarion, the necessary statements of the programming language are generated for you. You will denote the major 
tasks to be done, describe the way you want those tasks to work, and how your screens and reports will appear. Clarion 
will write the program, creating the language statements needed to do the job in the most efficient manner. 
The major tasks to be performed by the program (display a screen, print a report, etc.) are called procedures. 
Procedures consist of a number of instructions. When these instructions are being performed, we say that the procedure 
is executing. A procedure returns when all instructions have been executed. 
Procedures must be named. A procedure begins to execute when an instruction calls the procedure by its name. 
Certain types of procedures are common to almost all programs. Most programs consist primarily of menus, scrolling lists, 
data entry screens, and reports. Clarion supports these and many other procedure types. 
Programs are created in the Application Generator by choosing a procedure type which most closely matches your 
requirements and then customizing the default menu, screen, or report, and/or by defining data, or by creating formulas 
and embedded source. Procedures "call" other procedures and are "connected" to them in a "building block" approach 
that eventually results in a complete program. The Application Generator stores program and procedure characteristics in 
Application (.APP) files. 


---

User's Guide and Lessons 
81 
 
 
 
 
In addition, there are code, control, extension and wizard templates, which allow you to virtually customize and quickly 
generate any of the built-in procedure templates, bundled with Clarion. For example, a form may now have a List Box, by 
choosing a "Browse Box" control template. Validation of a field or control can be added anywhere by adding the 
appropriate code or extension. 
Creating the Application (.APP) File 
The first step in creating a new application (after creating a Data Dictionary) is to create an application (.APP) file. The 
application file holds the procedure specifications, data declarations, and other properties you define for your 
application—it contains everything necessary to generate source code, and then make an executable program. 
All applications are contained within a Clarion Solution file (*.SLN). A Solution file contains all of the information needed 
to build the application into a distributable executable file or library for use with other executables. Solutions can also hold 
multiple applications, but that topic is covered in a later lesson in this section. 
You may want to create a new folder for each application you develop because whenever you open an application (.APP) 
file, Clarion uses the directory in which the file resides as the working directory. 
 
 
1. Optionally, in Windows Explorer, choose File  New  Folder, type a folder name then press OK. 
This creates a working folder for your application. You can also let the Clarion Project System create the folder for you. 
2. Start Clarion and choose File  New  Solution, Project or Application. 


---

IDE User's Guide 
82 
 
 
This opens the New Solution, Project or Application dialog. 
 
 
 
 
This dialog allows you to type in the basic information the Project System needs to create a new Clarion for Windows 
project file (.CWPRJ) and solution file (*.SLN for you). 
 
 
Categories 
Select a valid category. To create a Win32 application, select the Clarion 
for Windows category. 
 
Quick Starts 
Specify the type of project that you wish to create. In Clarion for Windows, 
the Quick Starts available are hand coded DLL, EXE, or Library projects, 
or Applications (from scratch or from an existing TXA file). A TXA file is an 
application in a special text format. Select the Application Quick Start 
here. 
 
Name 
Type in a project name which displays at the top of the Tree List in the 
Project View. This is normally the name of your target output by defualt, 
but your target can later be modified. 
 
Location 
Type in (or select with the Browse for Folder dialog after pressing the 
ellipsis button) the location where the project will be created. 


---

User's Guide and Lessons 
83 
 
 
 
Create directory for 
Sources 
Check this box to specify a subdirectory with the project name that will be 
created at the Location you specified. 
 
Auto create project 
subdir 
Check this box to autocreate a project folder that uses the project Name 
and Location specidfied. For example, if the name of the project is Orders 
and the Location is C:\Example, a sub-folder named Orders will be 
created in the Example folder. 
 
 
3. After selecting the appropriate options above (make sure you have selected the Application Quick Start), 
press the Create button. 
This opens the Application Properties dialog where you define the basic files and properties for the application. 
 
 
 
4. In the Application File entry, optionally press the ellipsis (...) button to redefine the pathname for your .APP file. 
5. Type a name for the .DCT file in the Dictionary File entry, or press the ellipsis (...) button to select the dictionary 
file from the Select Dictionary dialog. 
See the previous lesson for information on creating your application‘s data dictionary. 
 
 
The Application Generator does not require a data dictionary to generate an application if you clear the Require a 
dictionary box in the Application Options dialog. See Lesson 3 - The Application Generator Environment for more 
information. 
6. In the First Procedure entry, name the application‘s "supervisor" procedure if you do not wish to use the default 
name of "Main". 
7. Choose the Destination Type from the drop-down list. 


---

IDE User's Guide 
84 
 
 
 
This defines the target file for your application. Choose from Executable (.EXE), Library (.LIB), or Dynamic Link 
Library (.DLL). 
Choosing Dynamic Link Library (.DLL) enables the Export Procedure prompt in the Procedure Properties dialog 
(see Setting Procedure Properties) and the Export all file declarations prompt in the Global Properties dialog. 
 
 
Using LIBs or DLLs to modularize and organize larger applications can provide substantial savings in development and 
maintenance costs: compiling and linking only a portion of a large application saves development time, and calling a set of 
common functions from a single source means maintaining only one set of code. 
You may want to develop a portion of an application as an .EXE, then remake it as a .DLL when complete. See Advanced 
Topics - Development and Deployment Strategies for more information. 
 
 
Setting the Project‘s Target Type is equivalent to setting the Application‘s Destination Type and vice versa. See Project 
System for more information. 
 
 
8. Type a name for the application‘s .HLP file in the Help File field, or use the ellipsis (...) button to select one from 
the Select Help File dialog. 
If you specify a help file in the current directory, the application looks for the help file in the current directory, 
then the system directory, then the system path. The full path is not stored. 
However, if you specify a help file in another directory, a full path is established and the application looks for the 
help file by the full pathname. 
You are responsible for creating a Windows Standard .HLP file that contains the context strings and keywords 
that you enter as HLP attributes for the application‘s various controls and dialogs. There are many third party 
products that help you do this. 
9. Choose the Application Template type. 
Accept the default (ABC), or press the ellipsis (...) button to select from another template set. The Application 
template controls source code generation. 
10. Choose the ToDo Template type. 
Accept the default (ABC), or press the ellipsis (...) button to select from a third party template set. The ToDo 
template controls source code generation. 
11. Clear the Application Wizard box by clicking on it. 
Checking this box causes the Application Generator to create an entire working application based on the data 
dictionary you selected. In the next topic lesson, we will build an application using the Application Wizard. For 
now, we‘ll examine the Application Tree when completing the next step. 
12. Press the OK button. 
 
 
Clarion creates the .APP file, then displays the Application Tree dialog for your new application. When you make a new 
application, you only have one procedure defined for you. This procedure is a ToDo type, which means you may 
choose what type of procedure to create. You do this by pressing the Properties button. 


---

User's Guide and Lessons 
85 
 
 
 
 
 
 
The Application Tree dialog provides six different views of your application. The Procedure view displays all application 
procedures in hierarchical order, nesting each procedure under its calling procedure. 
 
 
 
Adding Procedures to your Application 
 
 
A procedure is a series of Clarion language statements (source code) which perform a task. A Procedure template is an 
interactive tool that (with the help of Clarion‘s development environment) requests information from you, the developer, 
then generates a custom procedure for just the task you specify. 
A Procedure as stored in a Clarion application (.app) file, is really a specification that the development environment uses 
to generate the procedure source code. The specification includes the Procedure template, your answers to its prompts, 
the WINDOW definition, the REPORT definition, local data declarations, embedded source code, etc. 
Your application‘s supervisor procedure is called "Main" by default. You can name this procedure anything you want, but 
this chapter refers to it as "Main." All other procedures branch from "Main"—one procedure can call another. 
 
 
Application Tree 
The hierarchical tree controls (or outline controls) in the Application Tree dialog illustrate how the procedures branch from 
"Main" and from each other. This provides a schematic diagram of your program‘s logical structure. 
 
 
An 
 icon means the procedure contains embedded source code. 
 
The Application Generator adds a procedure to the Application Tree whenever you press the insert key, or add a menu 
item, a toolbar command, or a code template that calls a procedure. Each new procedure is marked "To Do." When you 
"fill in" its functionality, the Application Generator replaces the "To Do" with your description. 


---

IDE User's Guide 
86 
 
 
Defining the Procedure Type 
Once you add a "ToDo" procedure to the Application Tree, the next step is to define its type from the choices available in 
the Select Procedure Type dialog. The choices available correspond directly to the Procedure templates in your template 
registry. See Procedure Templates in the Template Guide for more information on the Procedure templates in this 
package. 
• 
To open the Select Procedure Type dialog, select any "ToDo" procedure in the Application Tree dialog, then 
press the Properties button, or double-click on the "ToDo" procedure. 
Wizards 
Template Wizards are the most powerful design tool within the Application Generator. Here, you can select a base 
procedure (Browse, Form, Report, etc.) or a whole application, and then fine tune the wizard prompts and options to 
produce a near perfect application or procedure that fits your specifications. 
The next lesson will focus on the Wizards in more detail 
 
 
Defaults 
The Defaults tab allows you to select from a wide variety of pre-defined structures and functionality. Based on the type of 
default you select, the template procedure associated with it is automatically attached upon your selection. 
 
 
Templates 
This dialog lets you choose a procedure template, adding functionality to any new or "To Do" procedure in the Application 
Tree 
CLICK on a procedure template from the list, then press the Select button. Once you select a procedure type, you can 
customize it using its Procedure Properties dialog. 
If you add third party, or your own customized templates to the Template Registry, they also appear in the list. 
 
 
If you must change the procedure type later, go to the Application Tree, highlight the procedure, then press the 
Properties button. 


---

User's Guide and Lessons 
87 
 
 
 
 
Press the ellipsis button as shown above. The Select Procedure Type dialog appears so you can select another 
procedure type. If the new procedure type doesn‘t support some of the structures—such as menus—that you defined in 
the previous procedure type you may "orphan" the previously defined structures. Therefore, be cautious when changing 
procedure type. 
 
 
This concludes this lesson. 


---

IDE User's Guide 
88 
 
 
 
Lesson 2 - The power of the Application Wizards 
Introduction 
This section explores a powerful set of application utility templates in the Clarion IDE called wizards. 
In the Environment Overview lesson, we saw that templates are the building blocks of the Application Generator. They 
provide much of the design options you will see in the applications that you create, and also generate solid source code 
that is used to build your target executables and libraries. 
A wizard is essentially a collection of templates whose features are activated under your control (i.e., based on a series of 
questions that you answer, a series of templates generate a specially formatted text file that is imported into an active 
application. When you create your target output, the templates step in again to generate the source code that is 
compiled). 
This release of Clarion also introduces template styles, which contain default colors, icons, text, and other options that you 
can reuse in other applications for a consistent look and feel in all of your projects. 
 
 
 
 
The green boxes indicate actions that the IDE performs automatically. The blue boxes indicate areas where the developer 
has control, and where input is required. 
Referring to the diagram above, you should notice that a wizard could be accessed in one of three ways: 
• 
Creating a new application, and checking the Application Wizard check box in the Application Properties 
window. 
• 
In the Application Generator, press CTRL + U or Application  Template Utility… from the IDE menu. 
• 
In the Application Generator, press the INSERT key or press the New Procedure button from the IDE menu. 


---

User's Guide and Lessons 
89 
 
 
Upon start up of all wizards, you will be prompted for an associated style file. The style file controls the default prompts 
that you are presented with in each wizard. In addition, you can modify these prompts and save your changes to an 
existing style file, or write the entire contents of your wizard session to a new style file. 
On exit, each wizard processes the style file according to your options, and generates an application text file (.TXA) that is 
imported into the active application file. 
In the following sections, we will explore the features of each wizard. If you are new to Clarion, please refer first to the 
Getting Started Help for a quick lesson designed to help you create an application using the Application Wizard. 
 
 
Application Wizard 
The Clarion Application Wizard generates an entire application program. The program includes a main menu and 
subordinate procedures for viewing, searching, updating, and printing data from one or more tables. The Application 
Wizard generates a full program based on an existing data dictionary with one or more related or unrelated tables. 
After the introduction screen, you are presented with the following options: 
Theme Selection: 
Theme 
Select from the drop list of themes. Themes are groups of settings that control colors, fonts, icons, backgrounds, positions 
and much more - for Frame, Browse, Form and Report procedures. You will have the opportunity to create a new theme 
as you progress through the wizard. Select a starting or default theme here. 
Report Layout 
Select a default report layout from the drop list provided. This layout will be the basis for all of the reports that will be 
generated by the wizard. 
 
 
If you are using the Quick Start Wizard, this is the only dialog that you will be presented with. Press the Finish button to 
begin the creation of your application. 
 
 
Other prompts that follow on subsequent windows: 
 
 
Generate Procedures for: 
all files in my dictionary 
Select this item to instruct the wizard to generate browse/form and optional report procedures for all tables defined in the 
dictionary. 
primary files 
Select this item to instruct the wizard to generate browse/form and optional reports for all tables defined in the dictionary 
that are not defined as relational child tables to any other table. This option is useful for applications with large dictionaries 
whose relationships have not yet been defined, and limits the generation of additional procedures used to establish these 
related tables (child browse procedures and selects). 
selected files 
Select this item to instruct the wizard to generate browse/form and optional report procedures for all tables selected in the 
next dialog window, which is a list of all tables defined in the selected dictionary. 
For SQL based file systems, the Application Wizard also generates code to capture user login information upon initial 
program load, and then reuse the login information for each file accessed. 


---

IDE User's Guide 
90 
 
 
Which control model should the Application use? 
There are three models the wizard can use to create applications: Button, Toolbar, or Both. 
 
 
Button 
The wizard builds the application with traditional Insert, Change, Delete, OK, and Cancel command buttons that appear 
on each dialog. 
 
 
Toolbar 
The wizard builds the application with global toolbar command buttons that appear on the application frame. The toolbar 
buttons control each dialog. 
 
 
Both 
The wizard builds the application with both the traditional dialog command buttons and the global toolbar command 
buttons. 
 
 
Customization 
Wizards have different "look and feel" settings and actions called themes, which can be modified and saved for use in 
other applications. Themes are set and controlled by a variety of customization options. 
Press the Next button to accept the selected theme‘s settings, or press one of the customization buttons to modify them 
at this time. 
 
 
Create an Internet Enabled Application 
If you are using the ABC template chain, check this box to apply the Web Application Extension (WebBuilder) templates to 
your application. If you are using the Clarion template chain, check this box to apply the Internet Application Extension 
(Internet Connect) templates to your application. In both instances, this allows your application to be deployed as both a 
Windows and Internet application. 
You must have the appropriate template set registered in order to use this feature. 
 
 
Overwrite existing procedures 
Check this box to overwrite existing procedures with the same names. Clear the box to preserve existing procedures. 
 
 
Generate Reports for each file 
Check this box to automatically generate report procedures. Clear the box to omit report procedures. 
 
 
Select Sort Order 
Select from the drop list the sort and report generation method from the following choices: 
 
 
Single Key 
Select this option to force the wizard to generate a separate report for each key defined in your file (or files). 


---

User's Guide and Lessons 
91 
 
 
Runtime Key Selection 
Select this option to force the wizard to generate a single report that pops up a sort order dialog prior to printing at 
runtime. 
 
 
Record Order 
Select this option to force the wizard to generate a single report sorted by record order for your selected file (or files). 
 
 
On the last dialog, the Finish button is enabled. If you are satisfied with your answers, press the Finish button. You also 
have the option here to Save Changes, where any changes to customization options are saved to the theme that you 
selected at the start of the wizard. If you wish, you can opt to Save on a new theme, and enter the new name of the 
Theme and Theme file. 
You can press the Back button to change a prior selection or press the Cancel button to abandon the application. 
The Application Wizard creates the .APP file based on the dictionary and the answers you provided, and then displays the 
Application Tree dialog for your new application. 
 
 
Fine Tuning the Wizard 
You can control how the wizard builds your application by specifying options for Tables, Columns, Keys, and 
Relationships in the Data Dictionary. 
 
 
 


---

IDE User's Guide 
92 
 
 
Procedure Wizards 
Generate data oriented procedures (data browsing, data entry, and reports) based on specific table descriptions in a 
data dictionary. The generated code accommodates the defined table relationships, by including multiple procedures 
as needed to support both primary and related table updates and validation. 
The following Procedure Wizards are available in this release: 
 
 
Browse Wizard 
This wizard creates a multi-keyed Browse procedure from an existing dictionary table definition. The BrowseBox is sorted 
by each key you specify. The sort order is controlled by Tab Controls. It also creates associated Form (Update) 
procedures, if you specify that updates be allowed. 
After the introduction screen, you are presented with the following options: 
 
 
Theme Selection 
 
Theme 
Select from the drop list of themes. Themes are groups of settings that control 
colors, fonts, icons, backgrounds, positions and much more - for Frame, 
Browse, Form and Report procedures. You will have the opportunity to create 
a new theme as you progress through the wizard. Select a starting or default 
theme here. 
 
Save Settings 
After you have selected a theme, you have the option to save these settings for 
any future applications that you create. 
 
 
What name should be used as the label of the procedure? 
Type the browse procedure name. 
 
 
Which file do you want to browse? 
Press the ellipsis (...) button to select a file from the dictionary. 
 
 
Browse using all record keys 
Check this box to make the list sortable on all keys. Clear the box to specify a single sort key. 
 
 
Allow the user to update records 
Check this box to generate a subordinate procedure to update the table. Optionally, provide the name of the update 
procedure. Clear the box to make the list read only. 
 
 
Call update using popup menu 
Check this box to provide right-click popup menus on the Browse list in addition to any command or toolbar buttons. 
 
 
Parent Record Selection 


---

User's Guide and Lessons 
93 
 
 
 
This prompt appears only if you specify a single sort key that is the linking key in a Many:One relationship. The Browse 
Wizard infers from this that you may want to browse only the child records for a specific parent record. Select one of the 
following to confirm or deny this inference. 
Do not select by parent record 
Do not limit the browse - in other words, browse all records. 
 
 
Select parent record via button 
Browse only the child records for a specific parent record. Provide a button to select the parent record. 
 
 
Assume that the parent record is active 
Browse only the child records for a specific parent record. Assume the parent record is already active. 
 
 
Provide buttons for child files 
Check this box to provide buttons on the Browse window to access related child tables. Alternatively, related tables may 
be accessed from the generated update procedure. 
 
 
Provide a "Select" button 
Check this box to provide a "Select" button that displays when the Browse procedure is called to select a record, but is 
hidden when the Browse is called to update records. 
Which control model should the Application use? 
 
Button 
The wizard builds the browse with traditional Insert, Change, and Delete 
command buttons that appear on each dialog. 
 
Toolbar 
The wizard builds the browse to use global toolbar command buttons that 
appear on the application frame. See Control Templates - 
FrameBrowseControl. 
 
Both 
The wizard builds the browse to use both traditional dialog command 
buttons and global toolbar command buttons. 
 
Customization 
Wizards have different "look and feel" settings and actions called themes, which can be modified and saved for use in 
other applications. Themes are set and controlled by a variety of customization options. 
Press the Next button to accept the selected theme‘s settings, or press one of the customization buttons to modify them 
at this time. 
 
 
Overwrite existing procedures 
Check this box to overwrite existing procedures with the same names. Clear the box to preserve existing procedures. 
 
 
On the last dialog, the Finish button is enabled. If you are satisfied with your answers, press the Finish button. You also 
have the option here to Save Changes, where any changes to customization options are saved to the theme that you 
selected at the start of the wizard. If you wish, you can opt to Save to a new theme. 


---

IDE User's Guide 
94 
 
 
 
The Browse Procedure Wizard creates the procedure(s) based on the dictionary file and the answers you provided, and 
then displays the Procedure Properties dialog for your new procedure. 
 
Form Wizard 
This wizard creates an update Form Procedure from an existing dictionary table definition. 
 
 
After the introduction screen, you are presented with the following options: 
Theme Selection: 
 
Theme 
Select from the drop list of themes. Themes are groups of settings that control 
colors, fonts, icons, backgrounds, positions and much more - for Frame, 
Browse, Form and Report procedures. You will have the opportunity to create 
a new theme as you progress through the wizard. Select a starting or default 
theme here. 
 
Save Settings 
After you have selected a theme, you have the option to save these settings for 
any future applications that you create. 
 
 
What name should be used as the label of the form procedure? 
Type the procedure name. 
 
 
Which file do you want the form to update? 
Press the ellipsis (...) button to select a file from the dictionary. 
 
 
Allow Records To Be Added 
Check this box to allow new records. 
 
 
Allow Records To Be Modified 
Check this box to allow records to be changed. 
 
 
Allow Records To Be Deleted 
Check this box to allow records to be deleted. 
 
 
Insert Message 
Type the title bar text to display when adding a record. 
 
 
Change Message 
Type the text to display when changing a record. 
 
 
Delete Message 


---

User's Guide and Lessons 
95 
 
 
 
Type the text to display when deleting a record. 


---

IDE User's Guide 
96 
 
 
Where do you want this message to be displayed? 
Choose the title bar or the status bar. 
 
 
A field can be displayed that identifies the active record. 
Press the ellipsis button to select a column from the dictionary to display on the window title bar. 
 
 
Validate field values whenever field value changes? 
Check this box for immediate validation when the end user "accepts" the column. 
 
 
Validate field values when the OK button is pressed? 
Check this box for column validation on the OK button. 
 
 
Browsing child files 
Select one of the following choices. 
Place children on tabs 
Access children with push buttons 
Do not provide child access 
 
Which control model should the Application use? 
 
Button 
The wizard builds the dialogs with traditional Insert, Change, and 
Delete command buttons. 
 
Toolbar 
The wizard builds the form to use global toolbar command buttons that 
appear on the application frame. 
 
Both 
The wizard builds the form to use both traditional dialog command 
buttons and global toolbar command buttons. 
 
Customization 
Wizards have different "look and feel" settings and actions called themes, which can be modified and saved for use in 
other applications. Themes are set and controlled by a variety of customization options. 
Press the Next button to accept the selected theme‘s settings, or press one of the customization buttons to modify them 
at this time. 
Overwrite existing procedures 
Check this box to overwrite existing procedures with the same names. Clear the box to preserve existing procedures. 
 
 
On the last dialog, the Finish button is enabled. If you are satisfied with your answers, press the Finish button. You also 
have the option here to Save Changes, where any changes to customization options are saved to the theme that you 
selected at the start of the wizard. If you wish, you can opt to Save to a new theme. 
The Form Procedure Wizard creates the procedure(s) based on the dictionary table and the answers you provided, and 
then displays the Procedure Properties dialog for your new procedure. 
 


---

User's Guide and Lessons 
97 
 
 
Report Wizard 
This wizard creates a Report Procedure from an existing dictionary table definition. 
 
 
After the introduction screen, you are presented with the following options: 
Theme Selection: 
 
Theme 
Select from the drop list of themes. Themes are groups of settings that 
control colors, fonts, icons, backgrounds, positions and much more - for 
Frame, Browse, Form and Report procedures. You will have the opportunity 
to create a new theme as you progress through the wizard. Select a starting 
or default theme here. 
 
Report Layout 
Select a default report layout from the drop list provided. This layout will be 
the basis for all of the reports that will be generated by the wizard. 
 
Save Changes? 
After you have selected a theme, you have the option to automatically save 
changes to this theme for any future applications that you create. 
Check this box to store changes when completing the wizard. 
 
 
What name should be used as the label of the report procedure? 
Type the procedure name. 
 
 
Which file do you want to report? 
Press the ellipsis (...) button to select a file from the dictionary. 
 
 
Key Sequence - Select Sort Order 
Select from the drop list the sort and report generation method from the following choices: 
 
 
Single Key 
Select this option to force the wizard to generate a separate report for the key that you select in the Enter a key prompt 
that follows. 
 
 
Runtime Key Selection 
Select this option to force the wizard to generate a single report that pops up a sort order dialog prior to printing at 
runtime. 
 
 
Record Order 
Select this option to force the wizard to generate a single report sorted by record order for your selected file (or files). 
 
 
How many columns do you want the report to use? 
Type the number of columns for your report. The Report Wizard distributes the report columns evenly across the columns. 


---

IDE User's Guide 
98 
 
 
Select the fields that you want to use 
Build your report in this list box by adding and deleting fields from the selected file. You can also modify the properties of 
the fields regarding column labels, picture tokens, and justification. Use the arrow buttons to specify the order that each 
field will appear on the report. 
 
 
Customization 
Wizards have different "look and feel" settings and actions called themes, which can be modified and saved for use in 
other applications. Themes are set and controlled by a variety of customization options. 
Press the Next button to accept the selected theme‘s settings, or press the Report Customization button to modify it at 
this time. 
 
 
Overwrite existing procedures 
Check this box to overwrite existing procedures with the same names. Clear the box to preserve existing procedures. 
On the last dialog, the Finish button is enabled. If you are satisfied with your answers, press the Finish button. You also 
have the option here to Save Changes, where any changes to customization options are saved to the theme that you 
selected at the start of the wizard. If you wish, you can opt to Save to a new theme. 
The Report Procedure Wizard creates the procedure based on the dictionary table and the answers you provided, and 
then displays the Procedure Properties dialog for your new procedure. 
 
 
 
 


---

User's Guide and Lessons 
99 
 
 
Report Label Wizard 
This wizard creates a report procedure from an existing dictionary file definition that includes a defined report label layout. 
 
 
After the introduction screen, you are presented with the following options: 
 
 
Theme Selection: 
 
Theme 
Select from the drop list of themes. Themes are groups of settings that 
control colors, fonts, icons, backgrounds, positions and much more - for 
Frame, Browse, Form and Report procedures. You will have the opportunity 
to create a new theme as you progress through the wizard. Select a starting 
or default theme here. 
 
Label Group 
Select a label group from the drop list. A label group contains the most 
popular classes of labels (Avery, Card Products, InkJet, etc.). If your type of 
label is not listed here, select Others. 
 
Label Type 
Select a label type from the drop list. A label type normally corresponds to its 
product code. 
 
Save Settings 
After you have selected a theme, you have the option to save these settings 
for any future applications that you create. 
 
 
What name should be used as the label of the report procedure? 
Type the procedure name. 
 
 
Which file do you want to report? 
Press the ellipsis (...) button to select a file from the dictionary. 
 
 
A report can use a single record key, or can run in record order. Enter a key below, or leave the field blank to run 
in record order. 
Press the ellipsis (...) button to select a sort key. Leave the field blank to specify no sort key. 
 
 
Select the fields that you want the report to use? 
Build your report in this list box by adding and deleting fields from the selected file. You can also modify the properties of 
the fields regarding column labels, picture tokens, and justification. Use the arrow buttons to specify the order that each 
field will appear on the report. 
 
 
Customization 
Wizards have different "look and feel" settings and actions called themes, which can be modified and saved for use in 
other applications. Themes are set and controlled by a variety of customization options. 
Press the Next button to accept the selected theme‘s settings, or press the customization button to modify it at this time. 


---

IDE User's Guide 
100 
 
 
Overwrite existing procedures 
Check this box to overwrite existing procedures with the same names. Clear the box to preserve existing procedures. 
 
 
On the last dialog, the Finish button is enabled. If you are satisfied with your answers, press the Finish button. You also 
have the option here to Save Changes, where any changes to customization options are saved to the theme that you 
selected at the start of the wizard. If you wish, you can opt to Save to a new theme. 
 
 
 


---

User's Guide and Lessons 
101
 
 
Process Wizard 
This wizard creates a Process Procedure from an existing dictionary table definition. 
 
 
After the introduction screen, you are presented with the following options: 
 
 
Theme Selection: 
 
Theme 
Select from the drop list of themes. Themes are groups of settings that control 
colors, fonts, icons, backgrounds, positions and much more - for Frame, 
Browse, Form and Report procedures. You will have the opportunity to create a 
new theme as you progress through the wizard. Select a starting or default 
theme here. 
 
Save Settings After you have selected a theme, you have the option to save these settings for 
any future applications that you create. 
 
 
What name should be used as the label of the Process procedure? 
Type the procedure name. 
 
 
Which file do you want to process? 
Press the ellipsis (...) button to select a file from the dictionary. 
 
 
A process can use a single record key, or can run in record order. Enter a key below, or leave the field blank to 
run in record order. 
Press the ellipsis (...) button to select a sort key. Leave the field blank to specify no sort key. 
 
 
Customization 
Wizards have different "look and feel" settings and actions called themes, which can be modified and saved for use in 
other applications. Themes are set and controlled by a variety of customization options. 
Press the Next button to accept the selected theme‘s settings, or press one of the customization buttons to modify them at 
this time. 
 
 
Overwrite existing procedures 
Check this box to overwrite existing procedures with the same names. Clear the box to preserve existing procedures. 
On the last dialog, the Finish button is enabled. If you are satisfied with your answers, press the Finish button. You also 
have the option here to Save Changes, where any changes to customization options are saved to the theme that you 
selected at the start of the wizard. If you wish, you can opt to Save to a new theme. 


---

IDE User's Guide 
102 
 
 
Window Wizard 
This wizard creates a window using template themes and other basic settings. 
After the introduction screen, you are presented with the following options: 
 
Theme Selection 
 
Theme 
Select from the drop list of themes. Themes are groups of settings that control 
colors, fonts, icons, backgrounds, positions and much more - for Frame, 
Browse, Form and Report procedures. You will have the opportunity to create 
a new theme as you progress through the wizard. Select a starting or default 
theme here. 
 
Save Settings 
After you have selected a theme, you have the option to save these settings 
for any future applications that you create. 
 
 
What name should be used as the label of the procedure? 
Type the window procedure name. 
Customization 
Wizards have different "look and feel" settings and actions called themes, which can be modified and saved for use in 
other applications. Themes are set and controlled by a variety of customization options. 
Press the Next button to accept the selected theme‘s settings, or press the Window Customization button to modify it at 
this time. 
 
 
Overwrite existing procedures 
Check this box to overwrite existing procedures with the same names. Clear the box to preserve existing procedures. 
On the last dialog, the Finish button is enabled. If you are satisfied with your answers, press the Finish button. You also 
have the option here to Save Changes, where any changes to customization options are saved to the theme that you 
selected at the start of the wizard. If you wish, you can opt to Save to a new theme. 
 
 
 


---

User's Guide and Lessons 
103
 
 
Theme Maintenance 
The Theme Maintenance Wizard is a powerful template utility that allows you to Add, Modify, or Delete selected template 
wizard themes. 
Themes are defined as text files that control a wizard‘s generated output and, in addition, the wizard‘s default prompt 
settings that are presented to the developer. A theme file has a default file extension of TFT, and is stored in the TFT sub 
folder of the Clarion TEMPLATE folder. This path, and the list of existing themes, is found in the C6TFT.INI file located in 
the Clarion BIN folder. 
 
 
Theme Selection 
 
 
Theme 
From the drop down list, select an existing theme that you wish to add, 
modify, or delete. If you are adding a new theme, you will need to select an 
existing theme. After you make modification to the selected theme, you can 
use the Save As option. 
 
Report Layout 
From the drop down list, select an existing report layout that you wish to add, 
modify, or delete. Changes to the Report Wizard will be applied to this layout. 
 
 
Operations 
The buttons shown on this wizard sheet direct you to one of four operations. You can Design Theme, based on the 
theme selected on the previous window. After your modifications, return to this window to Save Theme Default.TFT (the 
selected theme), or Save As to a new theme name. 
After saving the theme through one of the above methods, press the Cancel button to exit the wizard. Your theme is 
already saved. You can also press the Finish button to exit the wizard, but you will have to complete the required entries 
in the Save As dialog. 
You can also remove the selected theme permanently by pressing the Delete Theme Default.TFT button. 


---

IDE User's Guide 
104 
 
 
 
Lesson 3 - The Application Generator Environment 
This chapter is important for understanding the general development flow of a typical application, and how your 
environment settings can affect your design environment. 
 
 
Overview: Developing Your Application 
Once the .APP file exists, you develop your application through a series of dialogs. When you create your application‘s 
menus and toolbars, they call procedures that you name. The Application Generator adds these "ToDo" procedures to the 
application tree. You define the functionality of the "ToDo" procedures by picking from a set of Procedure templates. 
Remember, templates are code generation scripts that prompt you for information on how to customize the generated 
code. Use the Window and Report Designers to supply information to the templates about how your application looks to 
the end user. 
Following is an overview illustrating the tasks that you normally complete when building an application with the Application 
Generator. The lessons in this help document that follow provide a more detailed description. 
• 
Define the "Main" procedure. 
Add menu commands and their "ToDo" procedures. 
• 
Define the "ToDo" procedures. 
Choose the appropriate template to generate each procedure. 
Use the Procedure Properties dialog to identify the procedure‘s source file. 
Use the Window Designer to design your windows. 
Use the Report Designer to design your reports. 
Use the Procedure Properties dialog to add local variables as needed. 
• 
Make the application (generate source code, compile, and link). 
• 
Incrementally test the application (run it). 
 
 
Define the Main Procedure 
In the Application Tree dialog, highlight the Main "ToDo" procedure, then press the Properties button 
 to access the 
Select Procedure Type dialog. This lists the Procedure templates and template defaults available in the Template 
Registry. 


---

User's Guide and Lessons 
105
 
 
 
 
 
 
From the Defaults tab of the Select Procedure Type dialog, select the Default MDI Frame default procedure type for 
Main, and then press the Select button. 
The Frame procedure template is usually the best starting point for a typical application which employs different MDI 
child windows to present data in different views and forms. The Frame procedure template contains an MDI application 
frame, which already includes fully functional standard windows menus like File, Edit and Help. This menu will be 
discussed in more detail in a later lesson (See Exploring the Menu Frame Procedure ). 
Also in the Select Procedure Type dialog, you can choose the Wizard tab to use one of the various wizards to build your 
procedure. To build a new procedure that is between a wizard built procedure and the templates, choose the Defaults 
tab. This lists procedures that are nearly complete. 
Choose the Template tab when you wish to add your own controls, control and extension templates. This is ideal for 
designs that require the most customization. It places minimal controls on the procedure. 


---

IDE User's Guide 
106 
 
 
After you make your selection, the procedure‘s Properties tab dialog appears. 
 
Each Procedure template contains defaults or starting points for such elements as the window, a basic menu structure, 
reports and more. These defaults are designed with real world uses in mind, such as update forms (a window that 
displays a single record) for updating a database record. When developing an application, you can customize these 
procedures to fit your needs. 
 
 
Add Menu Commands and Their "ToDo" Procedures 
In the Properties tab dialog, access the Window Designer by pressing the Window tab, and then pressing the Designer 
button. You can also access the Window Designer directly from the application tree, and that method is more commonly 
used by developers. 
When the Window Designer dialog appears, go directly to the Menu Editor: the best way is to simply right-click on the 
Menu, and select Edit Menu from the popup menu. The Menu Editor dialog appears. You can also select the Edit Menu 
link located in the Properties Pad. 


---

User's Guide and Lessons 
107
 
 
 
 
See Exploring the Menu Frame Procedure for details on editing the menu. 
Typically, you add a menu item by pressing the Add New Item (Insert) 
 button. Then, right-click on the item that you 
just added, select the Actions item from the popup menu to specify the procedure or program to execute when the end 
user chooses that menu item. Once you type in the procedure name, the Application Generator adds the procedure to the 
Application Tree as a "To Do." 


---

IDE User's Guide 
108 
 
 
When creating a Multiple Document Interface (MDI) application, check the Initiate Thread box when prompted. 
Press the OK button to close the Actions dialog, and then press the Save and Close button 
 to close the Menu 
Editor, saving your changes. Press 
 to exit the Window Designer and save your changes. Press the Save and Close 
button again in the Window Designer Editor to return to the Application Tree. 
 
 
Define the "ToDo" Procedures 
Select the first "ToDo" procedure in the Application Tree and press the Properties 
button. The "ToDo" items are the 
procedure or procedures you named with the Menu Editor. 
 
 
Choose the Appropriate Template to Generate each Procedure 
Select a Procedure type from the choice of three tabs, then select the procedure from the Procedure Type dialog, then 
press Select. At this point, you might choose, for example, a Browse template, which displays records in a list box. 
If you use the Wizards, one of the many procedure wizards prompts you for the information needed to complete your 
procedure (or procedures). 
 
 
Choose the Tables that the Procedure Uses 
The Data / Tables Pad (FSP) is a special pad that displays the contents of an active dictionary and other application data 
elements (Global, Module, and Local). This pad is available when either the Dictionary Editor or Application Generator is 
opened. Open or bring focus to the Data / Tables Pad by pressing the F12 Key. 
Based on the template procedure that you selected, you should see a <To Do> entry. Highlight the <To Do> entry, and 
press the Add button on the Pad toolbar. 
 
 
 
 
Add local variables 
In the Data / Tables Pad, highlight the Local Data folder, and press the Add button on the Pad toolbar.. Basically, you 
declare each variable same way you define a column in a table. 
 
 
Use the Window Designer to design your windows 
In the Application Tree, highlight the target procedure and press the Window button. The Window Designer displays a 
sample window. See the Window Designer lesson for more detailed information. Depending on the Procedure template 
you chose, the window may already contain some predefined controls. 
Everything that appears in the window is a control, including buttons, list boxes, check boxes, spin boxes, data entry 
fields, etc. Select a control, then open or select the Properties Pad to specify the appearance and behavior of the control. 


---

User's Guide and Lessons 
109
 
 
 
 
Use the Control Templates Pad to place "prefabricated" controls—fully functional controls with associated source code. 
See the Adding Templates lesson for more information. For example, a BrowseBox control template generates a list 
control with associated source code that loads and scrolls the list. 


---

IDE User's Guide 
110 
 
 
 
Use dictionary columns (Window Designer  Populate  Column) to place "some assembly required" controls, that is, 
entry controls that are automatically loaded with a data dictionary column or memory variable values. 
Use simple controls (View  Control Toolbox) to place "do-it-yourself" controls, that is, controls with no associated 
source code. See the lesson on the Window Designer for more information. 
 


---

User's Guide and Lessons 
111
 
 
Make the Application 
Press the 
 button on the toolbar to generate source code, compile, and link the application. The Application Generator 
automatically maintains the compile and link information for the application. 
 
 
Test the Application 
Press the 
 button on the toolbar or choose the Make and Run All menu item from the Debug IDE Menu. 
After testing your first procedure, you can add more procedures, embed custom source code, and otherwise add 
functionality to your application. 
 
 
Configuring the Application Generator 
 
 
The Application Options dialog lets you specify default settings for each new application you create as well as for the 
active application. To access the dialog, choose Tools  Application Options. The dialog is divided into seven sections 
or tabs: Application, Registry, Generation, Synchronization, Embed Editor, OOP Embed Tree Options and Embed 
Tree Options. 
 
 


---

IDE User's Guide 
112 
 
 
 
Lesson 4 - The Window Designer and Control Properties 
This topic: 
• 
Explains how to use the Window Designer to create a new WINDOW structure or edit an existing one. 
• 
Explains how to use the Properties Pad to set window properties. 
• 
Explains how to configure the Window Designer to work the way you prefer. 
• 
Explains how to set control properties with the Data Dictionary. 
• 
Explains the types of controls available 
• 
Explains how to set Common Control Attributes using the Properties Pad. 
 
 
The first half of this lesson will focus on the Window structure. The second half will focus on the basic controls that can be 
populated on a window. Click here to skip to that part of the lesson. 
 
 
Window Creation Overview 
Use the Window Designer to visually design window elements—windows and controls—on screen. The Window Designer 
generates the Clarion language source code that describes the window, then the Application Generator places the 
generated source code at the appropriate point in your application. 
Most likely, your application will use a number of windows to display instructions, accept input, and provide data or other 
information to the user. In general, this is what you will do to put such a window on the screen: 
 
 
1. Select or create the procedure that manages the window. 
 
 
See the Application Generator topic for more information. 
 
 
2. From the Application Tree dialog, RIGHT-CLICK the procedure name and select Window from the popup menu. 
If no default window is defined, select a window type from the New Structure dialog. See Choosing a Window Type. 
If a default window is already defined, the Window Designer opens. 
 
You can also access the Window Designer from the Text Editor! To create a new window from the Text Editor, place the 
cursor on a blank line, then in the IDE Menu choose Edit Structure Designer or press CTRL+D. To edit an existing 
window, place the cursor anywhere within the source code structure that defines the window, then choose Edit  
Structure Designer or press CTRL+D. 
 
 
3. Using the Properties Pad, customize the window by setting its size and properties. 
See the Window Properties help topic located in the core help. 
 
4. Optionally, place a menu in the window with the Menu Editor. 
See Lesson 5 - Exploring the Menu/Frame Procedure for more information on this process. 


---

User's Guide and Lessons 
113
 
 
 
5. Place controls in the window—these might include entry boxes for editing fields from the database, command 
buttons for initiating or canceling actions, text, strings, or prompts containing instructions for the user, and other 
controls to enhance the appearance and ease of use of the window. 
 
 
6. Using the Property Pad, set the target control properties. 
You can do this by selecting the control, and pressing the F12 Key. See the Controls and Their Properties topic. 
 
 
7. Exit the Window Designer and Save your work as you return to the Application Tree. 
 
 
Choosing a Window Type 
 
 
Clarion‘s Procedure templates usually provide an appropriate default window for you. So if you create your procedure with 
a code generation Wizard or with a Frame, Browse, Form, Viewer, or Splash Procedure template, then you need not 
choose a window type, although you can change the default if you want to. 
However, if you use the Window - Generic Window Handler Procedure template, or if you start the Window Designer from 
within the Text Editor (CTRL+D) the Application Generator opens the New Structure dialog so you can choose from a list of 
default window definitions. Following are some guidelines to help you choose the right window for the job at hand. 
 
 
STARTing Modeless Windows (new thread) 
When you START a procedure on its own thread, the procedure and its window operate independently of other threads in 
the same program; that is, the end user can switch focus between each execution thread at will. This is true regardless of 
whether the windows on each thread are MDI or non-MDI. These are "modeless" windows. 
 
 
MDI and Non-MDI Windows (same thread) 
If you start a procedure on an existing thread (call a procedure without START), program behavior depends on whether or 
not the procedure‘s window has the MDI attribute. 
A non-MDI window on the same thread as its parent blocks access to its parent window, blocks access to all other threads 
in the program, and prevents subsequent opening of non-MDI windows on the same thread. This is an "application modal" 
window. When the application modal window closes, the other execution threads are available again. 
An MDI window on the same thread as its parent blocks access only to its parent window. When the MDI child window 
closes, its parent window regains focus. 


---

IDE User's Guide 
114 
 
 
Default Window Structures 
Some of the types of windows you can create with Clarion appear in the New Structure dialog. The items in the New 
Structure dialog represent Clarion language data structures. 
You may see window structures, report structures, or both, depending on how you access the dialog. A window structure 
is a group of Clarion language statements that define all the attributes of a window. You may want to think of a window 
structure as the definition of the window. See the WINDOW help topic in the Language Reference. 
This section discusses only the default window structures supplied with this release; however, you may modify these 
default windows, and you may even add your own default window structures by editing the \LIBSRC\DEFAULTS.CLW file. 
If you edit the DEFAULTS.CLW file, be sure to precede each new structure with the following line: 
!!> title 
where "title" is the structure name that appears in the New Structure dialog. 
Following is a description of the default window structures provided with this package. 
 
 
Simple Window 
To create a general-purpose document window or dialog box, choose Simple Window from the New Structure dialog. The 
Window Designer generates a non-MDI WINDOW structure with no controls. That is, a bare or empty window. 
This window accepts any controls (listboxes, entry boxes, buttons, etc.) you want to add. Because the window is non-MDI, 
it can move "outside" its application window. 
 
 
Window with OK & Cancel 
This window is exactly like the Simple Window described above, except it contains OK and Cancel buttons. There are no 
actions associated with the buttons; you must add any needed functionality. If you want buttons with functionality already 
attached, see the Control Templates —CancelButton, CloseButton, etc. 
There are seven other variations to this window, adding an optional Help button, default icons for each button, and STD 
attributes that perform standard Windows functions. 


---

User's Guide and Lessons 
115
 
 
MDI Child Window 
To create a document window that appears only inside an application frame, choose MDI Child Window. The Window 
Designer generates a WINDOW structure with the MDI attribute. 
The child window typically appears as a normal window, with frame, system menu, maximize and minimize buttons, and 
icon. The user should be able to manipulate it like any other window—except that the child window cannot move outside 
the main application window. 
All MDI windows must reside in separate procedures and execution threads from the APPLICATION window (see 
Application Main MDI Frame below). This means you must initiate a thread (use START) when you start this window‘s 
procedure from the Application frame. 
There are two variations to the MDI Child Window. The first adds OK and Cancel buttons. There are no actions 
associated with the buttons; you must add any needed functionality. The second variation also adds default icons to those 
buttons. 
Any menus and toolbars you create for an MDI window will automatically merge with the APPLICATION‘s menu and 
toolbar when the MDI child is the active window! 
 
 
Application Main MDI Frame 
To create the APPLICATION frame, or main window, for an MDI application, choose Application Main MDI Frame. This 
provides the "outside" frame in which the MDI child windows appear. 
Typically, the APPLICATION window should have a resizable frame, plus a system menu, maximize and minimize 
buttons, and a menu. The File menu should provide commands to open the MDI child windows, and the Window menu 
should provide commands for managing the separate child windows. The Frame template provides all these features 
automatically! 
The APPLICATION window may only have controls on its toolbar. MDI child windows contain all other controls in an MDI 
application. In other words, the APPLICATION window should hold only its child windows, and optionally, its toolbar. 
The APPLICATION window and its MDI children must not reside in the same procedure. You must START the MDI child‘s 
procedure so that the MDI child window is in a separate thread from the APPLICATION. Multiple MDI windows may run in 
the same thread, but not on the same thread as the APPLICATION window. 
 
 
Progress Window 
A progress window is designed to provide the user with a visual indication of progress during a process or report. 
This window starts exactly like the Simple Window described above, and then centers the window position, gives it a 
GRAY attribute, and adds a TIMER attribute. Next, it adds a progress control, two strings for messaging, and a Cancel 
button. There are no actions associated with the default controls; you must add any needed functionality. 
There are four other variations to this window, adding three types of default icons and, in the fourth variation, a vertical 
progress control. 
 
 
 


---

IDE User's Guide 
116 
 
 
Window Designer Configuration 
Before beginning your first session with the Window Designer, it is important to understand your configuration options. 
The Window Designer Options dialog sets the default position and size values applied when auto-populating controls, or 
when aligning controls with the alignment tools. To access the dialog, choose Tools  Options   Window Designer 
Options from the environment menu. The dialog is divided into two areas: General and Grid Options. 
 
 
 
Using the Window Designer 
Choosing the window type is just the beginning. The Window Designer provides a rich assortment of visual tools and 
menus to help you create and edit your window. 
The Window Designer lets you directly manipulate the window and the controls inside it. The sample window, for example, 
contains ‗handles‘—tiny boxes located at the corners and sides of the window. By selecting a handle and dragging the 
mouse, you may resize the sample window. The window the user sees when your application runs is the same size as the 
window you create by dragging. 
When the Window Designer generates the source code for the window, it places the data determining the size and 
position of the window (as you specified by dragging the mouse) in the AT attribute of the statement declaring the window. 
Similarly, the Window Designer supplies the other attributes by presenting you with options, check boxes and fields in 
which you specify your design preferences. 


---

User's Guide and Lessons 
117
 
 
Window Designer Tools 
During the design process, there are several Window Designer tools at your disposal. 
Sample Window 
The Window Formatter is a visual design tool. You always see a sample of the window you're working on, as you work on 
it. For example, place a list box in the sample window and drag its handles to the size you want. Toggle the Visual Styles 
and Control Transparency settings to fine-tune your visual display. 
Properties Pad 
The Window Designer's Properties Pad allows you to quickly specify the appearance and content of the text on each 
control within the window and on the window title bar. Control the font, size, style, and content of all your text, using 
standard word processor buttons and drop down lists. 
Display and get focus to the Properties Pad by choosing View Properties. Resize the Properties Pad by placing the 
cursor on the border of the box. When the cursor changes to a double headed arrow, CLICK and DRAG. 
 
Alignment Toolbar 
The Window Designer's Alignment toolbar allows you to quickly, professionally, and precisely align the controls in your 
window. 
Select the controls to align (CTRL+CLICK allows you to select multiple controls, or you can "lasso" multiple controls with 
CLICK+DRAG), then click on the appropriate alignment tool. All the alignment actions are also available from the Window 
Designer > Format menu. 


---

IDE User's Guide 
118 
 
 
 
 
 
For most alignment functions, the last set of controls selected (black handles) are aligned with the first control selected 
(white handles). That is, the first control selected is the anchor control. It doesn't move, the others do. 
Position the cursor over any tool and wait for half a second. A tool tip appears telling you the type of alignment this tool 
will accomplish. 
 
 
Command Toolbar 
The Window Designer shares a Command toolbar with the Alignment toolbar. The toolbar lets you quickly execute a 
variety of Report Designer functions at the touch of a button. 
All the commands in the Command toolbar section are also available from the IDE menu. 
Position the cursor over any tool and wait for half a second. A tool tip shows you the type of control this tool creates. 
 
Save and Close 
Exit the Report Designer and save changes. 
Cancel 
Exit the Report Designer and abandon changes. 
Bring to Front 
For overlapping controls, select this item to move the active control to the top. 
Send to Back 
For overlapping controls, select this item to move the active control to the back. 
Tab Order 
Not applicable in the Report Designer. 
Print Preview 
Calls the Print Preview dialog in the Report Designer, allowing to you render a sample report for viewing. 
Switch SupressTransparency 
Allows the proper display of special static parent controls when populated "on top of" multiple tab controls. This property is 
set to TRUE by default, and ensures a proper display regardless of Visual Styles used. No effect on runtime window. 
Use Visual Styles 
This button controls the display of Visual Styles for all valid controls in design mode (controls appear as if the XP manifest 
was active). 
 
 
Data / Tables Pad 
The Window Designer has access to the Data / Tables Pad. This pad allows you to quickly "populate" a window with 
entry controls and prompts for fields in your data dictionary tables. 
Display or hide the Data / Tables Pad by choosing View Data / Tables Pad. Resize the pad by placing the cursor on 
the border of the box. When the cursor changes to a double headed arrow, CLICK and DRAG. 


---

User's Guide and Lessons 
119
 
 
 
 
1. Select a table from the top pane. 
2. Select the column you want on your window in the bottom pane. 
3. DRAG the column in the sample window to place the control and its associated prompt. 
The type of control (entry box, check box, radio button, etc.) is determined by the settings for this particular column in the 
Data Dictionary. 


---

IDE User's Guide 
120 
 
 
Controls Toolbox 
The Window Designer contains a floating Controls toolbox, similar to those found in many draw or paintbrush programs. 
Simply choose a control from the toolbox (CLICK on it), then DRAG to the sample window at the target location to place 
the control in the window. 
Display or hide the Controls toolbox by choosing View Toolbox. Resize the Controls toolbox by placing the cursor on 
the border of the box. Select a control by clicking on it, and DRAG to the desired location on the target window. 


---

User's Guide and Lessons 
121
 
 
Window Designer Menus 
The Window Designer provides many features available from standard and popup menus. 
 
 
The Window Designer menu is visible during any Designer session, and provides populating controls options and 
alignment (Format) commands for spacing and sizing the controls within the window. 
 
 
 
 
There is also a dynamic popup menu for all controls and the window itself. For example. Right click on any button 
template control, and you will see the following: 
 
 
 
 
The popup menu is an invaluable tool. As you can see above, it incorporates key items from the IDE Menu, Window 
Designer Menu, and Smart Links from the Properties Pad. 


---

IDE User's Guide 
122 
 
 
Window Properties Dialog 
 
 
Use the Properties Pad to set all the properties or attributes of a WINDOW or APPLICATION. Properties include the 
window caption, whether the window is resizable, whether the window is scrollable, icons associated with the window, 
messages, help files, and cursor types associated with the window, and many others. In short, all the properties 
associated with windows as opposed to properties associated with procedures, controls, columns, etc. 
To open the Properties Pad dialog from the Window Designer: 
RIGHT-CLICK on the sample window then choose Properties from the popup menu. 
Select the sample window then press the F4 KEY. 
Select the sample window then choose View  Properties from the menu. 
 
 
 
Placing Controls on a Window 
 
 
This section explains how to place a control in a window. The Controls and Their Properties topic explains how to 
customize the controls you place. 
 
 
To place a control: 
1. 
CLICK on an entry in the Controls toolbox, or choose a control from the Data / Tables Pad or the Window Designer 
Populate menu. You can also select a control template from the Control Templates Pad. 
2. After you have selected a control or control template, pass the cursor over the sample window. 
The cursor changes to a crosshair (+). Position the crosshair where you want the control to appear. 
3. 
CLICK the mouse. 
The Window Designer places the upper left hand corner of the control at the position of the cursor crosshair when you 
click the mouse. By default, the control takes on the size of the other controls of that type already in the window. If there 
are no like controls in the window, the control is the default size. 
Control templates generate source code to declare controls and manage their associated data. For example, the 
BrowseBox control template not only generates source code to display a listbox control, it also generates code to load 
data from a table into a QUEUE, then display the data in the listbox with complete scrolling and mouse-click selection 
capability. 
 
 
Generally, it is to your advantage to use a Control template rather than a simple control. 
 
 
When using the Window Designer Populate option to place a Dictionary Column, it automatically opens the Select Column 
dialog so you can select or define a data dictionary column or memory variable to associate with the control. Once placed, 
you can access the control‘s Properties Pad dialog from the View menu or from the right-click popup menu. 
 
 
4. If necessary, CLICK and DRAG on a control handle to resize the control. CLICK and DRAG on the interior of the control to 
move the control. 


---

User's Guide and Lessons 
123
 
 
 
 
 
You can also resize multiple controls at the same time if they are selected. 
 
 
 
 
 
Controls and Their Properties 
 
This section shows you how to set control properties. It assumes you understand how to use the Window Designer to 
choose, place, and size controls. 
It provides an overview of the types of controls as they relate to data entry, discusses the properties applicable to the 
controls, then covers each control type individually. It also shows you how to associate the contents of a variable with an 
entry or display control. 
 
 
Setting Control Properties with the Data Dictionary 
Control properties may be set for a single control using the Window Designer. Better still, with the Data Dictionary, you 
may set control properties for every control associated with a specific database column (press the Controls tab of the 
Column Properties dialog). When control properties are set in this manner (with the Data Dictionary), the Application 
Generator applies these properties every time you place the column on a window or report and every time you 
synchronize your application and data dictionary. 
 
 
Types of Controls 
For this discussion, we will divide controls into three categories: Interactive Controls, Non-Interactive Controls, and 
Custom Controls. 
 
 
Interactive Controls 
Interactive controls are clicked on or typed into by the user. 
• 
Action controls—BUTTON—lead to an instantaneous result. For example, closing a dialog box and completing its 
pending operations. Clarion also supports associating a continuous action with a button—pressing the button and 
holding it down is the same as clicking the button repeatedly. 
• 
User Choice controls—CHECK, OPTION, RADIO, COMBO, SPIN and LIST—let the user enter data by choosing 
from a finite group of alternatives. No keyboard input is required. They create streamlined user entry since it is 
usually faster to pick an item from a list than to type the name of an item you may not remember. Use choice 
controls to force the user to choose only one of a set of mutually exclusive selections—create "latched" buttons 
that stay depressed until pressed again, or groups of radio buttons where only one button can be selected at a 
time. 
• 
Entry controls—ENTRY and TEXT—allow data entry from the keyboard. Clarion provides extensive options for 
automatically validating user data entry, plus supports Windows standard Cut, Copy, and Paste operations for 
these text controls. 
• 
{ Hybrid controls—SHEETs, TABs and REGIONs—interact with the user by guiding them to other controls, and by 
generating events that your program can detect and act upon. 


---

IDE User's Guide 
124 
 
 
Non-Interactive Controls 
Non-interactive controls provide visual cues that help the user understand and operate the interactive controls. 
• 
Static controls—PANEL, PROMPT, GROUP, BOX, ELLIPSE, LINE and IMAGE—don‘t perform an action, but 
instead guide the user to other controls or otherwise provide visual candy. They can take the form of a group box, 
a line, or a graphic image, all of which visually organize or emphasize other controls. GROUP controls also help 
you develop and maintain your application by letting you apply common attributes such as positioning, enabling, 
or hiding to several controls at once. 
 
 
Custom Controls 
Custom controls are defined outside the Clarion Development Environment and may be either interactive or non- 
interactive. Custom controls are discussed in a later topic. 
 
 
Common Control Attributes 
The attributes you add to a control determine how the control looks and acts. Different controls support different functions, 
and so require different attributes. However, all Clarion controls allow you to set two common attributes: USE and AT. 
Additionally, most controls allow you to set TEXT, COLOR, KEY, ALRT, FONT, SKIP, HIDE, DISABLE, SCROLL, 
CURSOR, HLP, MSG, and TIP attributes. This section explains how to set these common control attributes. Each 
attribute is discussed fully in the Language Reference. 
 
 
RIGHT-CLICK on a control and select Properties from the popup menu, or press the F4 KEY to access its properties in the 
Properties Pad. 
 
 
Setting the USE Attribute 
The Use property takes either a Field Equate Label or a variable label. If you placed a control template, you can accept 
the default label or you may specify your own label. 
 
 


---

User's Guide and Lessons 
125
 
 
Field Equate Labels 
Use a Field Equate Label when you don‘t need to assign a value from the control to a variable. A field equate label is a 
valid Clarion label prefixed by a question mark(?). This label references the control within your source code (see the 
Language Reference for more information). For example: 
HIDE(?MyButton) 
!hides the control with USE attribute ?MyButton 
 
 
Variable Labels 
Use a variable label when you do need to assign a value from the control to a variable or vice versa. 
 
 
Some controls, such as PROMPTs and LINEs, cannot accept variable values and therefore only accept Field Equate 
Labels as their USE attribute. 
The variable must be declared in your program, module, or procedure. Press the ellipsis (...) button in the control‘s 
properties dialog to declare the variable or to select the variable from those already declared. 
The variable label automatically serves as the field equate label for the control too! For example: 
 
 
MESSAGE('My Variable = '& MyVar) !displays the variable MyVar 
HIDE(?MyVar) 
!hides the ?MyVar entry control 
 
Duplicate Field Equate Labels 
Two or more entry controls may update the same variable. However, they cannot have the same field equate label. In this 
circumstance, the Window Designer automatically creates unique field equate labels by appending a sequence number to 
the field equate labels that would otherwise be duplicated. The unique field equate label is specified by the third 
parameter of the USE attribute (see USE in the Language Reference). For example, if you place three controls on a single 
window that all update the same variable, the Window Designer generates code something like this: 
 
 
window WINDOW('Caption'),AT(,,183,119),GRAY 
SPIN(@s20),AT(66,27),USE(MyVar) 
COMBO(@s20),AT(66,50),USE(MyVar,,?MyVar:2) 
ENTRY(@s20),AT(67,7),USE(MyVar,,?MyVar:3) 
END 
 
To set the USE attribute 
1. 
RIGHT-CLICK the control, then choose Properties from the popup menu. 
This displays the Properties Pad for the selected control, which lets you specify the USE property for your control. 
 
 
2. If the control is an entry control or has an associated variable (CHECK, COMBO, CUSTOM, ENTRY, LIST, 
OPTION, PROGRESS, SHEET, SPIN, STRING, or TEXT), press the Use column ellipsis (...) button to select or 
define a data dictionary column or memory variable from the Select Column dialog. 
If the control does not have an associated variable (BOX, BUTTON, ELLIPSE, GROUP, IMAGE, LINE, PANEL, 
PROMPT, RADIO, REGION, or TAB), type a valid Clarion label prefixed with a question mark ( ? ). Notice there is no Use 
column ellipsis (...) button for these controls. 


---

IDE User's Guide 
126 
 
 
 
Remember, you can always use the default label supplied by the Window Designer. 
 
 
3. Press the OK button. 
 
 
Field equate labels and Clarion‘s property syntax let you modify the control at run-time. For example, you can use the 
DISABLE statement to "dim out" controls in situations when they should be unavailable to the user: 
DISABLE(?MyList) 
 
 
Following is an alternative method for setting the USE attribute. This method works best for controls with no associated 
variable. 
1. From the Window Designer Options dialog, check Show Properties Toolbar. Press OK to save the Options. 
On the next Designer open, this displays the Property toolbox, which lets you specify the USE attribute for your controls. 
2. Click the control you want to change. 
3. In the Property toolbox Use entry, type a Field Equate Label or the label of a variable to use with the control. 
 
 
Setting the AT Attribute 
The AT attribute defines the control‘s position and size. The Window Designer lets you visually set the AT attribute of 
each control simply by dragging it wherever you want. You may also specify position and size by manually typing 
coordinates in the control‘s properties dialog and by using the Alignment tools. To set the AT attribute, which defines the 
control‘s position and size: 
1. RIGHT-CLICK on the control, then choose Properties in the popup menu. This displays the Properties Pad, and the 
Position category as shown here: 
 
 


---

User's Guide and Lessons 
127
 
 
 
 
2. Specify coordinates for the top left corner of the control. 
Type in an ‗X‘ (horizontal) and ‗Y‘ (vertical) coordinate. This places the top left corner of the control relative to the top left 
corner of the window. The unit of measurement for the coordinates is the dialog unit. See the Glossary for the definition of 
dialog units. These provide a relative measure based on the size of the character set currently in use. 
3. Specify Width and Height options. 
Choose Default and Clarion automatically selects a size based on the display picture on an entry control. Or choose Fixed 
and type in width and height values for the control in dialog units. 
 
 
For IMAGE controls, Default displays the picture at the size it was created. 
You may also specify that the control fills the window by choosing the Full options. This adds the FULL attribute to the 
control. See the Language Reference for more information on this attribute. 
 
 
Default and Full are mutually exclusive choices. For example, you cannot set Width to Full and Height to Default. 
 
 
You can provide your users a full window text editor for MEMO columns. Create a window and place a TEXT control in it. 
Optionally change the cursor to an I-Beam, then set the Width and Height of the TEXT control to Full. 
 
 
Setting the Text Property 
Many controls, such as BUTTONs, TABs, CHECKs, GROUPs, etc., display constant text on their face. This is the most 
straightforward and common method for telling the user how and when to use the control. 
To set the text property: 
1. RIGHT-CLICK on the control then choose Properties from the popup menu. 
This displays the Properties of the respective control, which lets you specify the text attribute for your control. 
 
 
 
2. In the Text property, enter the text to display. 


---

IDE User's Guide 
128 
 
 
 
An ampersand (&) within the text means the next character is the mnemonic key for the control. When displayed, the 
character is underlined, and when the user presses ALT plus the mnemonic key, the control‘s action initiates. For example 
type &Print to display Print and to let ALT +P initiate the control‘s action. 
 
 
Field equate labels allow you to use executable statements and Clarion‘s property syntax to modify the text of the control 
at run-time. For example, you can change text on the fly with: 
?MyButton{PROP:Text}='new text' 
 
 
Following is an alternative method for setting the USE attribute. This method works best for controls with no associated 
variable. 
1. From the Window Designer Options dialog, check Show Properties Toolbar. Press OK to save the Options. 
On the next Designer open, this displays the Property toolbox, which lets you specify the Text attribute for your controls. 
2. Click the control you want to change. 
3. In the Property toolbox TEXT entry, enter a text value to use with the control. 
 
 
There is still another way to set the text attribute. This is done through the use of a control‘s Smart Tag. 
 
 
 
 
As you click on the smart tag (shown above), a menu of smart choices appears. Selecting the Edit Text item allows you 
to update the Text property as needed. 


---

User's Guide and Lessons 
129
 
 
Setting the Display Picture 
Many controls, such as ENTRYs, COMBOs, STRINGs, etc., display variable values as well as constant text. These 
controls provide a Picture property instead of the Text property. 
To set the display picture for variable values, type a picture token in the Picture entry or press the ellipsis button to use the 
Edit Picture String dialog (see the Picture Editor chapter). See the Language Reference for more information on pictures. 
See also Dictionary Editor—Defining Column Properties. 
 
 
Setting the COLOR Attribute 
The sparing use of color can improve the look and functionality of your program. See Windows Design Issues for more 
information on the use of colors in the Windows environment. 
Enter a valid color value in any of the following properties to add the COLOR attribute to your control declaration. See 
..\LIBSRC\EQUATES.CLW for a list of valid color equates. 
TextColor 
To apply a specific color to the control text, type a valid color equate in this entry, or press the drop list to select a color 
from the Color dialog. 
Background 
To apply a specific color to the entire control, except for selected text, type a valid color equate in this entry, or press 
the drop list to select a color from the Color dialog. 
SelForeGround 
To apply a specific color to the control‘s selected text, type a valid color equate in this entry, or press the drop list to 
select a color from the Color dialog. 
SelBackGround 
To apply a specific color to the background of control‘s selected text, type a valid color equate in this entry, or press 
the the drop list to select a color from the Color dialog. 
GridColor (LIST and COMBO only) 
To apply a specific color to the LIST‘s grid lines, type a valid color equate in this entry, or press the the drop list to 
select a color from the Color dialog. 
BorderColor (BOX, ELLIPSE, and REGION only) 
To apply a specific color to the control‘s border, type a valid color equate in this entry, or press the the drop list to 
select a color from the Color dialog. 
FillColor (BOX, ELLIPSE, REGION, and PANEL only) 
To apply a specific color to the control‘s interior, type a valid color equate in this entry, or press the the drop list to 
select a color from the Color dialog. 
 
 
The Color Dialog 
You invoke the Color dialog from several places within the Clarion environment, but primarily when setting color for a 
window or for a window control. The Color dialog is a Microsoft product, but is documented here for your convenience. 
Custom Colors 
Choose from 48 custom color samples that you define. click on the color you want. 


---

IDE User's Guide 
130 
 
 
Define Custom Colors 
To define a custom color, right-click on one of the 16 Custom Color sample boxes. The Color dialog expands so you can 
define the custom color. 
 
 
 
Color Continuum Pad 
Displays a continuum of color choices. click on this pad to set the gross definition for your custom color. Fine tune your 
color definition with the controls described below. 
Luminance Continuum Slider 
Displays a continuum of luminance choices. click and drag inside the elongated rectangle to adjust the luminance of the 
color from darkest (black) to lightest (white). 
Color|Solid 
Displays a sample of the currently defined (mixed) color and its nearest solid color equivalent. To convert the currently 
defined color to its nearest solid color equivalent, type Alt+O. The conversion automatically adjusts the values of the six 
components listed below to make the appropriate solid color equivalent. 
 
Hue 
An integer from 0 to 240 representing the hue. 
 
Sat 
 An integer from 0 to 240 representing the saturation. 
Lum 
An integer from 0 to 240 representing the luminance. 
Red 
  An integer from 0 to 255 representing red. 
Green 
An integer from 0 to 255 representing green. 


---

User's Guide and Lessons 
131
 
 
 
Blue 
An integer from 0 to 255 representing blue. 
 
Add to Custom Colors 
When you are satisfied with the custom color definition press the Add Colors button. 
 
 
Web Colors 
Choose from a list of standard colors deemed safe and compatible with all modern general use browsers. 
System Colors 
Choose from a drop-down list of the system colors that Clarion uses to create its default Windows standard application 
interface. These colors match the default colors used by Clarion‘s template generated procedures. 
 
 
 
 
 
Setting the KEY Attribute 
The KEY attribute applies to any control which may receive focus (Combo Box, Entry Box, Group Box, List Box, Option 
Box, Property Sheet, Spin Box, Tab, Text Column, Button, Check Box, Custom Control, and Radio Button). It specifies a 
hot key which gives immediate focus to the control. For an action control, such as a command button, the hot key initiates 
the action as well. See the Language Reference for more information. 
 
 
To set the KEY attribute: 
1. RIGHT-CLICK on the control, and choose Key in the popup menu. 
This opens the Input Key dialog, which lets you specify the KEY attribute for your control. 
2. Press the desired key or key combination. 
The key or key combination you press appears in the Key entry, and is used as the parameter to the KEY attribute for this 
control. Alternatively, press a character or function (f1, f2, etc.) key and check a combination of the Ctrl, Shift, or Alt boxes 
to specify a hot key combination. 
 
 
Mouse clicks may be used as hot keys; however, mouse clicks cannot be specified by clicking the mouse. For mouse 
clicks, check the corresponding box(es). For example, to give focus to a control when the user ALT+DOUBLE-CLICKS, check 
the Alt box, the Left Button box, and the Double Click box. 
 
 
The ESC, ENTER, and TAB keys cannot be specified by simply pressing them, because these keys are standard Windows 
navigation keys. For these keys, press the ellipsis (...) button and type "esc," "enter," or "tab." 
 
 
3. Press the OK button. 
 
 
Avoid using ALT plus letter combinations as hot keys. These combinations should be reserved for menu accelerator keys. 
 
 
 


---

IDE User's Guide 
132 
 
 
Setting the ALRT Attribute 
The ALRT attribute applies to any control which may receive focus. It specifies an alert key which is enabled when the 
control has focus. When the user presses an alerted key, it generates an EVENT:AlertKey. This lets you execute an 
action while the user is still in the entry control. For example, you may set an ALRT to display additional information to the 
user upon a function key press. 
To set the ALRT attribute: 
1. RIGHT-CLICK on the control, then choose Alert in the popup menu. 
This opens the Alert Keys dialog, which manages the ALRT attributes for your control. You may set as many alert keys as 
you like for a control. 
2. Press the Add button. 
This opens the Insert Key dialog, which lets you specify the ALRT attribute for your control. This is the same dialog used 
to specify the KEY attribute. See Key above for information on how to use this dialog. 
3. Press the OK button. 
 
 
Setting the FONT Attribute 
You may specify the appearance of the text displayed on a control. Select typeface, size, color, style, and script from 
standard drop-down lists. Choose strikeout and underline effects too. See FONT in the Language Reference for more 
information. 
To set the FONT attribute: 
1. 
RIGHT-CLICK on the control and choose Properties in the popup menu. 
This displays the Properties Pad dialog. The Font properties are grouped as follows: 
 
 
2. Press the ellipsis to the right of the TextFont property. The Font Dialog is displayed. 


---

User's Guide and Lessons 
133
 
 
 
3. Select typeface, size, color, style, and script from standard drop-down lists. 
The dialog displays a sample of the text design you have chosen. 
4. Optionally check the Strikeout or Underline boxes if needed. 
5. Press the OK button. 
 
 
Be sure the font you pick is present on the user‘s system. If not, Windows will try to substitute an equivalent font; however, 
since you have no control over the substitution, you cannot be sure of the result. If you must use a font that may not be on 
your user‘s system, you must ship the font with your install set. 
 
 
Following is an alternative method for setting the FONT attribute: 
1. From the Window Designer Options dialog, check Show Properties Toolbar. Press OK to save the Options. 
On the next Designer open, this displays the Property toolbox, which lets you specify the USE attribute for your controls. 
2. CLICK on the control you want to change. 
3. In the Property toolbar, select the font typeface and size from standard drop-down lists. 
4. In the Property toolbar, theselect font style with standard bold, italic, and underline buttons. 
 
 
Setting Control Modes 
The Properties Pad of the various control properties dialogs lets you set several attributes that control the "mode" of your 
window controls. To set the control‘s mode: 
1. 
RIGHT-CLICK on the control, and choose Properties in the popup menu. 
This displays the Properties Pad dialog for the selected control. 
2. You should see a Mode category, which displays a list of toggle properties. 
 
 
 
3. Toggle any combination of the Mode properties. The choices and their effects are: 
 
 
Skip 
Instructs the Window Designer to omit the control from the Tab Order (the order in which controls get input focus as 
the user presses the TAB key). When the user tabs from control to control in the dialog box, Windows will not give the 
control focus. This is useful for seldom-used controls, because the user can still access the control by clicking on it. 
The Window Designer places the SKIP attribute on the control (see the Language Reference). 


---

IDE User's Guide 
134 
 
 
Disable 
Disables (or dims) the control when your program initially displays it, so it is unavailable to the user. The Window 
Designer places the DISABLE attribute on the control. You can use the ENABLE statement to allow the user to access 
the control (see the Language Reference). 
Hide 
Makes the control invisible at the time Windows would initially display it. Windows actually creates the control — it just 
doesn‘t display it on screen. The Window Designer places the HIDE attribute on the control. You can use the UNHIDE 
statement to display the control (see the Language Reference). 
Scroll 
Specifies whether the control should remain in the window when the user scrolls the window. By default (unchecked), 
the control remains in the window. Check the Scroll box to create a control that can be "scrolled off" the window. The 
Window Designer places the SCROLL attribute on the control (see the Language Reference). 
Transparent 
Specifies whether the control is drawn on the window, or only its text or icon. By default (unchecked), the control is 
drawn. Check the Transparent box to create a control that is invisible, except for its text or icon. The Window Designer 
places the TRN attribute on the control (see the Language Reference). 
Locked 
This property is actually located in the Design Mode category, and "Freezes" the control, and all its children, so that 
subsequent data dictionary changes are not applied (see Synchronize). You can override the #Freeze attribute for all 
controls, or for individual controls. 
 
 
Setting Help Attributes 
The Help category of the various control properties dialogs lets you set several attributes that supply information to the 
user about the control. 
1. RIGHT-CLICK on the control, and choose Properties in the popup menu. 
This displays and selects the Properties Pad dialog for the selected control. 
2. Locate the Help category, where the common properties for the Help attribute are located. 
 
 
 
The default view of the Properties Pad is the Category View (shown above) 
3. In addition to the Alrt and Key properties that were discussed above, optionally fill in any of the four entries. 


---

User's Guide and Lessons 
135
 
 
 
The entries and their effects are: 
Cursor 
Lets you specify an alternate shape for the cursor when the user passes it over the control. The Cursor drop-down list 
provides standard cursor choices such as I-Beam and Crosshair. To select an external cursor file (whose extension 
must be .CUR), choose Select File... from the drop-down list, then pick the file using the standard file dialog. The 
Window Designer places the CURSOR attribute on the control (see the Language Reference). 
 
 
The I-Beam, which signals text entry, is an excellent choice for the active cursor for an entry or text control. 
 
 
Help ID 
Sets the HLP attribute for a control (see the Language Reference). When the control has focus and the user presses 
F1, the Windows Help file opens to the topic referenced by the HLP attribute. In the Help ID entry, type either a help 
keyword or a help context string present in a .HLP file. 
A Help keyword is a word or phrase indexed so the user may search for it in the Help Search dialog. If more than one 
topic matches a keyword, the search dialog appears. 
A Help context string is the arbitrary string that uniquely identifies each topic page for the Windows Help Compiler. A 
help context string must be prefixed with a tilde (~). 
 
 
When authoring a Windows Help file, you indicate a keyword with the ‗K‘ footnote. A Help context string is the arbitrary 
string that uniquely identifies each topic page for the Windows Help Compiler. When creating the Help file, the ‗#‘ 
footnote marks a context string. These tasks are all done for you by many help authoring tools. 
 
 
Message 
Sets the MSG attribute for the control (see the Language Reference). The MSG attribute specifies text to display in the 
first zone of the status bar when the control has focus. In the Message entry, type the text to display in the status bar. 
 
 
Tip 
Sets the TIP attribute for the control (see the Language Reference). TIP displays text in a small box near the cursor 
when the cursor is idle on the control for a specified period. The default period is half a second. This technique is also 
known as "Balloon Help." In the Tip entry, type the text to display in the tip box. 
The Tip entry supports multi-line tool tips, but they do not automatically word wrap. To create a tip that spans more 
than one line, include carriage returns in the text (press the ENTER key between lines). 
 
 
 


---

IDE User's Guide 
136 
 
 
Interactive Controls 
 
Button Properties 
A BUTTON is a control that performs an action when the user presses it. In addition to the common control attributes 
described above, the Window Designer lets you set the following button properties: 
 
 
• 
The Button text. 
• 
The Button icon or picture. 
• 
The action to take When Pressed. 
• 
The STD ID specifying a standard windows action for the button to take. 
• 
Whether the button‘s action is the default action. 
• 
The Drop ID specifying drag and drop operations for which the button is a valid target. 
 
 
By convention, a button is a rectangular area containing text, picture, or both. When the user presses (clicks on) the 
button, it executes the command described by the text or picture. 
 
 
To specify button properties, RIGHT-CLICK the button control and choose Properties from the popup menu. The Properties 
Pad dialog is selected. This dialog helps you to specify the attributes for the BUTTON statement. 
See the Button Control Properties help topic in the core help for a detailed examination of the Button Properties dialog. 
 
 
Radio Button Properties 
A Radio Button, also called an option button, provides the user a set of mutually exclusive choices. For example, in a 
group of three buttons, only one can be selected at a time. 
By default, Radio Buttons display as small circles; the selected button is filled. You can make Radio Buttons look like push 
buttons simply by adding icons to each button; the selected button remains depressed. 
Relationship Between RADIOs and OPTIONs 
An option box—an OPTION structure—must always surround the radio button choices. The Window Designer 
automatically prompts you to create an option box if you try to place a radio button outside an option box. The option box 
appears at run time as a rectangle with a caption in the top border, and radio buttons inside. When you set radio button 
properties, you should also set the properties for the option box. 
When the user selects a radio button, the OPTION‘s USE variable receives a value indicating which button was selected: 
either the text of the selected button, the button number, or another value that you specify. Your program can then take 
appropriate action based on the value of the OPTION‘s USE variable. 
To place a radio button and an associated option box, CLICK the RADIO entry in the Controls Toolbox, then CLICK in the 
sample window. The Window Designer automatically adds an option box and a radio button. 
See the Option Control Properties help topic in the core help for a detailed examination of the Option Control Properties 
dialog. 
See the Radio Button Control Properties help topic in the core help for a detailed examination of the Radio Button 
Properties dialog. 


---

User's Guide and Lessons 
137
 
 
Check Box Properties 
A check box manages a variable that the user may turn on or off. Select the CHECK entry in the Controls Toolbox, then 
DRAG AND CLICK to the sample window. Once placed, RIGHT-CLICK the check box and select Properties from the popup 
menu; the Properties Pad dialog for the control is selected. 
See the Check Box Control Properties help topic in the core help for a detailed examination of the Check Box Control 
Properties dialog. 
 
 
List Boxes 
List Box controls are covered in detail in Lesson 6 - Exploring the Browse Procedure . 
 
 
Combo Boxes 
The COMBO control combines an entry box with a list box. It is useful for selecting data which usually is a member of the 
list, but sometimes is not. 
Combo Box properties are set exactly like List Box properties except for four additional properties associated with the 
entry box portion of the COMBO control. 
See the Combo Box Control Properties help topic in the core help for a detailed examination of the Combo Box Control 
Properties dialog. 
 
 
Spin Boxes 
A SPIN control is a specialized entry box that only accepts values in a predefined range. The SPIN also provides 
‗increase‘ and ‗decrease‘ buttons, which many people like because they can use the mouse to change the value. You can 
also type a value directly into the control. 
See the Spin Box Control Properties help topic in the core help for a detailed examination of the Spin Box Control 
Properties dialog. 
 
 
Entry Box 
An ENTRY control allows the user to enter data from the keyboard. Clarion provides extensive options for automatically 
validating user entry. 
• 
You may specify a picture for the column, automatically formatting the data the user enters. 
• 
You may specify an initial value for the column. 
• 
You may validate the data the user enters either at the time it‘s typed, or when the focus changes to another 
control. 
To set the properties for an entry box RIGHT-CLICK the entry box then select Properties from the popup menu. 
See the Entry Control Properties help topic in the core help for a detailed examination of the Entry Control Properties 
dialog. 
 
 
Text Box 
The TEXT control provides a multi-line data entry control. This control is especially suitable for holding a long STRING or 
a MEMO. The TEXT control provides automatic word wrapping. 
To set the properties for a text box RIGHT-CLICK the text box then select Properties from the popup menu. 
See the Text Box Control Properties help topic in the core help for a detailed examination of the Text Box Control 
Properties dialog. 


---

IDE User's Guide 
138 
 
 
Sheet Controls 
The SHEET control declares a group of TAB controls that offer the user multiple pages of controls for a single window. 
The multiple TAB controls in the SHEET structure define the pages displayed to the user. The SHEET structure‘s USE 
variable receives the text of the TAB control selected by the user. 
See the Sheet Control Properties help topic in the core help for a detailed examination of the Sheet Control Properties 
dialog. 
 
 
Tab Controls 
The TAB structure declares a group of controls. This group is one of multiple pages of controls that may be contained 
within a SHEET structure. The multiple TAB structures within the SHEET structure define the pages displayed to the user. 
The SHEET structure‘s USE attribute receives the text of the TAB control selected by the user. 
The Windows standard to change from tab to tab is CTRL+TAB. Clarion TAB controls follow this standard, both in the 
development environment and in a compiled application. 
If you nest TABS, only the top level is controlled by CTRL+TAB. 
See the Tab Control Properties help topic in the core help for a detailed examination of the Tab Control Properties dialog. 
 
 
Region Controls 
A REGION control is simply a rectangular area of the screen. Its main purpose is to provide a reference to test whether a 
given event—such as a mouse event—occurred within that region. 
You may give a region control color, a bevel, or provide for a cursor change when the user passes the mouse over the 
region. 
See the Region Control Properties help topic in the core help for a detailed examination of the Region Control Properties 
dialog. 
 
 
 


---

User's Guide and Lessons 
139
 
 
Non-Interactive Controls 
Non interactive controls do not accept data, but instead guide the user to other controls with text or graphics. For 
example: 
• 
A string in a dialog box can provide directions for filling out a data control. 
• 
One of the simplest graphic elements—a group box—can visually associate a group of controls, signalling the 
user that the entries all relate to the same thing. 
• 
An image or graphic can do more than embellish a dialog. It can convey meaning to a process that might 
otherwise take many, many words. 
 
 
String 
The String control lets you place a string constant on screen. It optionally lets you display a variable value. 
Strings do not support multi-line text; for multi-line text (word wrap) use a Prompt control or a Text control. 
See the String Control Properties help topic in the core help for a detailed examination of the String Control Properties 
dialog. 
 
 
Prompt 
The PROMPT control lets you place a string on screen that automatically provides an accelerator key to the next active 
control following the prompt. It is identical to the STRING control, except it has no variable capability and no angle 
capability; however, unlike a STRING, a PROMPT supports word wrapping (multi-line text). 
See the Prompt Control Properties help topic in the core help for a detailed examination of the Prompt Control Properties 
dialog. 
 
 
Group Box 
A GROUP control draws a box around other controls. It visually associates the controls for the user, and lets you address 
all the controls as one entity—making it easy, for example, to disable all at once. 
See the Group Control Properties help topic in the core help for a detailed examination of the Group Control Properties 
dialog. 
 
 
Progress Bar 
The PROGRESS control declares a control that displays a progress bar. This usually displays the current percentage of 
completion of a batch process by incrementally "filling" the bar as the process progresses. 
See the Progress Control Properties help topic in the core help for a detailed examination of the Progress Control 
Properties dialog. 
 
 
Image 
The IMAGE control lets you place bitmapped and vector images in a window. The bitmap file formats supported are .BMP, 
.CUR, .PCX, .GIF, .ICO and .JPG. The vector file format supported is .WMF. Clarion supports up to 16.7 million color 
resolution. 
GIF images are substantially faster than .JPG images although they do not compress quite as well. 32-bit JPG images are 
significantly faster than 16-bit JPG images. Clarion does not support printing of ICO images (because Windows doesn‘t 
support it). BMP images are fast, but take lots of space because they are not compressed. 


---

IDE User's Guide 
140 
 
 
 
 
Use the PALETTE attribute on your window to ensure ample color support for your images. The PALETTE attribute 
specifies how many colors you want this window to use when it is the foreground window. This is applicable in hardware 
modes where a palette is in use and spare colors are available. 
See the Image Control Properties help topic in the core help for a detailed examination of the Image Control Properties 
dialog. 
 
 
Line 
The LINE control lets you place a straight line in your windows. You may set the line‘s color, thickness and position. The 
Line control cannot receive focus, nor can it generate events. 
See the Line Control Properties help topic in the core help for a detailed examination of the Line Control Properties dialog. 
 
 
Box 
The Box control lets you place a square or rectangle in your windows. You may fill the box with a color, and specify a 
border color. You may also specify it should have rounded corners. The Box control cannot receive focus, nor can it 
generate events. 
See the Box Control Properties help topic in the core help for a detailed examination of the Box Control Properties dialog. 
 
 
Ellipse 
The ELLIPSE control lets you place a circle or ellipse in your windows. You may fill the ellipse with a color, and specify a 
border color. The ellipse control cannot receive focus, nor can it generate events. 
See the Ellipse Control Properties help topic in the core help for a detailed examination of the Ellipse Control Properties 
dialog. 
 
 
Panel 
The PANEL control lets you place a raised or depressed rectangular panel in your windows. You may color the panel. The 
panel control cannot receive focus, nor can it generate events. 
See the Panel Properties help topic in the core help for a detailed examination of the Panel Properties dialog. 


---

User's Guide and Lessons 
141
 
 
 
Lesson 5 - Exploring the Menu/Frame Procedure 
This topic: 
• 
Explains how to use the Menu Editor to create a new MENUBAR structure or edit an existing one. 
• 
Explains how to use the Window Designer to create a new TOOLBAR structure or edit an existing one. 
 
 
Menu Editor 
A menu is a list of the various actions your application may perform. In Clarion, this list of actions (menu) is declared using 
the MENUBAR structure, MENU structures, and ITEMs. In this chapter, the word menu generically refers to the list of 
actions your application may perform. The words MENUBAR, MENU, and ITEM refer to Clarion Language statements that 
define your application‘s menu. 
The Menu Editor is a visual design tool—a subset of the Window Designer—that generates Clarion Language statements 
to define your application‘s menu. 
This section: 
• 
Discusses dynamic menu management for Multiple Document Interface (MDI) applications. 
• 
Shows you how to call the Menu Editor and create a menu. 
• 
Describes how to automatically implement Standard Windows Behavior (SWB) for commands such as Edit 
 Copy by linking a Clarion Standard ID (STD attribute) to an ITEM or MENU. 
 
Merging MDI Menus 
Multiple Document Interface (MDI) applications make special demands upon a program. Often, the program may support 
a variety of document windows, each of which has a slightly different set of commands from which the user may select. 
Normally in an MDI application, the developer writes code to monitor which window is active and to change the menus 
and toolbars to reflect the options currently available to the user. Clarion does this automatically by merging menus and 
toolbars according to preferences you specify with the Menu Editor. However, accurate specification requires some 
understanding and planning by the application developer. 
 
 
Global Selections 
On an APPLICATION frame, the MENUBAR defines the Global menu selections for the program. These Global menu 
selections are generally available on all MDI "child" windows. However, if the NOMERGE attribute is present on the 
application‘s MENUBAR, then there is no Global menu, and the application‘s menu is a Local menu displayed only when 
no MDI child windows are open. 
 
 
Local Selections 
On an MDI child window, the MENUBAR defines Local menu selections that are automatically merged with the Global 
menu selections defined on the application‘s MENUBAR. Both the Global and the Local menu selections are available 
while the MDI "child" window has input focus. Once the window loses focus, its Local menu selections are removed from 
the Global menu selections. If the NOMERGE attribute is specified on an MDI child window‘s MENUBAR, the Local menu 
overwrites and replaces the Global menu. 
 
 
Non-MDI Windows 
On a non-MDI window, the Local menu selections are never merged with the Global menu selections. A MENUBAR on a 
non-MDI window always appears in the window, and not on any application frame which may have been previously 
opened. 


---

IDE User's Guide 
142 
 
 
 
 
Merging Order 
Normally, when an MDI window‘s menu (Local selections) merges into an application‘s menu (Global selections), the 
Global menu selections appear "first", followed by the Local menu selections. First means either toward the left or toward 
the top, depending on whether the merged selection is displayed on the action bar (horizontal list) or in a menu (vertical 
list). 
The merge process also considers whether any Local MENUs match any Global MENUs. MENUs that have the same 
name and the same MENUBAR level, match. When there are no matches, the menus merge in the normal order. 
However, when MENUs match, a single menu (vertical list) results with the Global selections appearing above the Local 
selections. This new menu has all the attributes of the Global MENU, such as, MSG, FIRST, etc. Within this merged 
menu, any matching subMENUs are also merged into a single menu. Note that ITEMS are not merged, even when they 
match. 
The normal merging order may be modified by using the Menu Editor‘s Position drop-down list (see Menu Positions and 
Merging Behavior below) to add FIRST or LAST attributes to individual MENUs and ITEMs. The merge position priority is: 
1. Global selections with FIRST attribute 
2. Local selections with FIRST attribute 
3. Global selections without FIRST or LAST attributes 
4. Local selections without FIRST or LAST attributes 
5. Global selections with LAST attribute 
6. Local selections with LAST attribute 
 
 
Planning and Implementing Menus 
To create menus for MDI applications: 
1. Create a master menu for the APPLICATION frame window. 
Most likely, this will include a File menu and a Help menu, since they contain functions that are available even when no 
document windows are open. 
Clarion‘s Application Frame procedure template comes with a predefined menu with many of the most common functions 
already provided for you. 
Use the Window Designer‘s Menu Editor to create your menus. Be sure to choose the FIRST attribute for the File MENU, 
and the LAST attribute for the Help MENU from the Position property drop-down list. This ensures that File and Help will 
maintain their relative positions when Clarion merges this global menu with local menus. 
 
 
2. Plan the additional menus for the child windows. 
Can they all share the same menu titles? Do they share many of the same commands? Ideally, most of the MENUs 
and ITEMs can be active in all the child windows. If there are only a few commands specific to certain windows, plan on 
disabling those MENUs and ITEMs in the windows that don‘t support them, and enabling them in those that do. 
 
 
3. Create the menu for the first child window. 
Again, you will use the Window Designer‘s Menu Editor to create the menu. Add any window-specific MENUs to the first 
child window. That is, the window-specific MENUs the application frame lacks-—such as Edit, Insert, etc. 
Optionally, add a File MENU to the first child window. This is necessary only if the child window needs an ITEM on the 
File MENU that is not already included on the application‘s File MENU. For example, adding a Close command might be 
appropriate. If so, add the File MENU to the first child window. Add the Close ITEM to the File MENU. 


---

User's Guide and Lessons 
143
 
 
 
Add the Window MENU to the first child window. Window MENUs are standard for most windows programs. A typical 
Window MENU includes the following ITEMs: Arrange Icons, Tile, Cascade, plus a document (windows) list that displays 
all open child windows and allows the user to switch between them. In many cases this entire MENU, including the 
document list, can be implemented with standard ID‘s (StdID‘s). See Creating Your Application's Menu below. 
4. Exit the Menu Editor and save the menu. 
5. Test the interaction of these first two menus. 
Do they merge the way you planned? Are the correct selections available for the window with focus? Make any 
adjustments with the Menu Editor. 
6. Repeat steps 3. through 5. for other child windows. 
 
 
Calling the Menu Editor 
To create a menu for your application, use the Menu Editor. You access the Menu Editor through the Window Designer. 
You can also create a toolbar for your application using the Window Designer. See Toolbars for more information. 
This section provides detailed examples of using the Menu Editor to create menus. From the Window Designer, DRAG 
the MENUBAR control in the Controls Toolbox to the active window to create a new menu, or right-click on the MENU and 
choose Edit Menu from the popup menu to edit an existing menu. You can also select the Window and click on the Edit 
Menu smart link in the Properties Pad. 
The Menu Editor dialog visually represents a Clarion MENUBAR data structure. The menu tree (on the left hand side of 
the dialog) appears as simplified Clarion language syntax, containing these Clarion keywords: 
• 
A MENUBAR keyword at the top. 
• 
A MENU statement followed by the corresponding Use property, and a menu name (Text). 


---

IDE User's Guide 
144 
 
 
 
• 
An ITEM statement followed by the corresponding Use property, followed by an item name (Text). 
• 
A SEPARATOR followed by the corresponding Use property. 
 
 
 
 
Menu Editor command buttons allow you to add and delete MENUs and ITEMs. You may also move MENUs and ITEMs 
within the MENUBAR structure with navigation buttons. 
The right hand side of the dialog lets you specify the properties of your MENUs and ITEMs. 
For a more detailed look at the Menu Editor and its options, click here. 
 
When using the Application Generator, each ITEM you place on a MENU or MENUBAR automatically adds an embed 
point to the control event handling tree in the Embedded Source dialog. This lets you easily attach functionality to your 
ITEMs. 
The following section provides a step-by-step procedure for creating a menu. Following that are sections detailing the 
Menu Editor commands and options, and a discussion of considerations to keep in mind when creating MDI application 
menus. 
 
 
 
 
 
Creating Your Application’s Menus 
Here are the steps for creating a menu starting from an empty window within the Window Designer. 
1. Open the Controls Toolbox (View  Toolbox) and DRAG the MENUBAR control to the active window. 
2. RIGHT-CLICK on the MENUBAR control just populated, and select Edit Menu from the popup menu. 
The Menu Editor dialog appears. Only the MENUBAR statement is present. 
3. Press the Add new menu 
button. 
This adds the first MENU statement, its name, and its corresponding USE attribute. 
The ampersand within the MENU name signifies that the character following the ampersand is the accelerator key. That 
is, the character is underlined (for example: Menu1), and, when the user presses ALT+accelerator key, the menu displays. 
4. In the Menu Text property on the right side of the Menu Editor, type the text to display for this MENU. 
For example, type &File, so the end user sees File. 
5. In the Use property, type a Field Equate Label. 
A Field Equate Label has a leading question mark (?), and you should make it descriptive. For example ?File shows 
this menu is to manipulate a file. You can refer to the MENU in your source code by its Field Equate Label. 
6. Press the Add new item 
button. 
This inserts an ITEM just after the MENU statement. Note that ITEMs are used to execute commands or procedures, 
whereas MENUs are used to display a selection of other MENUs or ITEMs. 


---

User's Guide and Lessons 
145
 
 
7. In the Text property field, type the text to display for this menu ITEM. 
For example, type &Open, so the end user sees Open. The ampersand within the ITEM name signifies the character 
following the ampersand is the accelerator key. That is, the character is underlined, and, when the user presses the 
accelerator key, the action associated with the ITEM executes. 
A MENU accelerator key requires the alt key to take effect, whereas an ITEM accelerator key does not require the alt key, 
but does require that the ITEM is currently displayed. See Adding a Hot Key below for another method of invoking your 
MENUs and ITEMs. 
8. In the Use property, type a Field Equate Label. 
A Field Equate Label has a leading question mark (?), and you should make it descriptive. For example, ?FileOpen shows 
at a glance the intended purpose of this ITEM: to open a file. 
You refer to an ITEM within source code by its Field Equate Label. 
9. In the Message property, type the MSG attribute contents. 
This message text displays in the status bar (if enabled) when the user highlights this MENU or ITEM. 
10. In the HelpID property, type either a help keyword or a context string present in a .HLP file. 
If you fill in the HelpID for a MENU or an ITEM, when the user highlights the MENU or ITEM and presses F1, the help file 
opens to the referenced topic. If more than one topic matches a keyword, the search dialog appears. 
The HelpID property (HLP attribute) takes a string constant specifying the key for accessing a specific topic in a Windows 
Help file. This may be either a Help keyword or a context string. 
A Help keyword is a word or phrase indexed so that the user may search for it in the Help Search dialog. 
When authoring a Windows Help file, you indicate a keyword with the ‗K‘ footnote. A Help context string is the arbitrary 
string which uniquely identifies each topic page for the Windows Help Compiler. When creating the Help file, the ‗#‘ 
footnote marks a context string. Many help authoring tools do all these tasks for you. 
When referencing a context string in the Help ID field, you must identify it with a leading tilde (~). 
11. RIGHT-CLICK on the ITEM just added, and select Actions from the popup menu. 


---

IDE User's Guide 
146 
 
 
 
 
 
 
12. Choose Call a Procedure from the When Pressed drop-down list. 
The procedure you specify executes when the user selects this ITEM. You may specify parameters to pass and standard 
file actions (insert, change, delete, or select) if applicable (Clarion‘s Procedure templates understand and carry out the 
requested file actions). Or you may initiate a new thread. The procedure appears as a "ToDo" item in your Application 
Tree (unless you named a procedure that already exists). 
When you START a procedure on its own thread, the procedure and its window operate independently of other threads 
in the same program; that is, the end user can switch focus between each execution thread at will. These are 
"modeless" windows. 
If you don‘t initiate a new thread, the program behavior depends on whether the procedure‘s window has the MDI 
attribute. A non-MDI child window on the same thread as its parent, blocks access to all other threads in the program. 
This is an "application modal" window. When the application modal window closes, the other execution threads are 
available again. An MDI child window on the same thread as its parent, blocks access only to its parent window. When the 
MDI child window closes, its parent window regains focus. 
This is one way to add functionality to your ITEM. You may also add functionality by choosing Run a Program from the 
drop-down list, by embedding source code, or by typing an STD ID in the STD ID field. STD IDs give your application 
Standard Windows Behavior (SWB) for common actions such as File/Open and Edit/Cut, Copy, and Paste. See 
Implementing Standard Windows Behavior. 
After following these steps, you have a single MENU called File, with a single ITEM called Open. To add other ITEMS to 
the MENU, repeat steps 6 through 12. To add a second MENU, press the 
 button. Use the arrow buttons to move it if 
needed. 
13. To finish the menu and return to the Window Designer, Save and Close button 
 to exit the Menu Editor. 
 
Adding Special Characters to your Menu 
You can embed tabs and other special characters within your menu text. To embed special characters (such as the tab 
character) in your menu text: 
1. Press the Save and Close button again to exit the Window Designer.. In the Window Designer Editor dialog, 
press the Edit as Text button. 


---

User's Guide and Lessons 
147
 
 
 
 
 
 
This opens the Text Editor to the WINDOW declaration for this procedure. When you embed special ASCII characters in 
your WINDOW declaration, you must edit the source code directly, because the Window Designer doesn‘t recognize the 
ASCII delimiter characters (<,>). 
2. In your ITEM text, type <n> where you want the character to appear. 
Where n is the ASCII code for the character. The brackets (<,>) tell the Clarion compiler to insert the ASCII characters 
specified within. For example: 
ITEM('Cut<9>Ctrl+X'),USE(?CutText),KEY(CtrlX),STD(STD:Cut) 
3. Press the Accept button to save your changes. 
You can embed special characters within POPUP menu text and MESSAGE text by using the ASCII delimiters (<,>). 
 
 
Implementing Standard Windows Behavior 
There are some menus and commands that you see in almost every windows program. For example, Cut, Copy, and 
Paste. Clarion provides an easy method for implementing these standard actions in your application menus—with the Std 
ID field on the Menu Editor dialog. 
To specify a standard action for your menu ITEM, enter one of the equates listed below in the Std ID field. Clarion 
automatically implements the command using standard windows behavior; you do not need any other support for it in your 
code. The standard equate labels and their associated actions are also contained in the \LIBSRC\EQUATES.CLW file. 
 
 
STD:PrintSetup 
Opens Printer Options Dialog 
 
STD:Close 
Closes active window 
 
STD:Undo 
Reverses the last editing action 
 
STD:Cut 
Deletes selection, copies to clipboard 
 
STD:Copy 
Copies selection to clipboard 
 
STD:Paste 
Pastes clipboard contents at the insertion point 
 
STD:Clear 
Deletes selection 
 
STD:TileWindow 
Arranges child windows edge to edge 


---

IDE User's Guide 
148 
 
 
 
STD:TileHorizontal 
Arranges child windows edge to edge 
STD:TileVertical 
Arranges child windows edge to edge 
STD:CascadeWindow 
Arranges child windows so title bars are visible 
STD:ArrangeIcons 
Arranges iconized child windows 
STD:WindowList 
Select child windows from a MENU 
STD:Help 
Opens .HLP file to the contents page 
 
STD:HelpIndex 
Opens .HLP file to the index 
STD:HelpOnHelp 
Opens Microsoft‘s Help system.HLP file 
STD:HelpSearch 
Opens Microsoft‘s Help Search .HLP file. 
 
Menu Positions and Merging Behavior 
The Position drop-down list lets you specify MENU and ITEM order priority when Clarion merges menus. Choose from: 
Normal 
Set normal merging order. In normal merging, Global selections precede Local selections. 
First 
Force the selected MENU or ITEM to the first position when merging menus. This adds the FIRST attribute to the 
MENU or ITEM statement. 
Last 
Force the selected MENU or ITEM to the last position when merging menus. This adds the LAST attribute to the 
MENU or ITEM statement. 
 
 
The following two property Flags let you specify whether or not your menu can be merged, and right justification of 
selections displayed on the action bar: 
Do Not Merge 
To never merge this MENUBAR with other MENUBARs, check this box. This is available only for the MENUBAR. 
See NOMERGE in the Language Reference for more information. 
Right 
To right justify the selected MENU, check this box. This is available only for MENUs on the action bar. Nested 
MENUs (subMENUs) cannot be right justified. Checking this box displays the selected MENU, and all MENUs 
after the selected MENU, at the far right of the action bar. 
 
 
Adding Hot Keys 
A hot key is very similar to an accelerator key. A hot key or hot key combination allows the end user to immediately 
display a MENU, or execute the action associated with an ITEM, without mouse clicking, and without displaying the menu 
that contains the ITEM. Customarily, hot keys take the form of CTRL + character, or CTRL + SHIFT + character. To add a hot 
key: 


---

User's Guide and Lessons 
149
 
 
1. Press the Key property ellipsis (...) button to select the hot key combination. 
This opens the Input Key dialog. Use this dialog to add the KEY attribute to your MENU or ITEM. The KEY attribute 
specifies a "hot" key or key combination. 
2. From the Input Key dialog, specify the hot key or key combination by pressing the desired key or keys. 
The keys you press appear in the Key field, and are supplied as the parameter to the KEY attribute for this menu item. 
Mouse clicks may be used as hot keys; however, mouse clicks cannot be specified by clicking the mouse. For mouse 
clicks, check the corresponding check box(es). For example, to execute the Open command when the user double-clicks, 
check the Left Button box and the Double Click box. 
The ESC, ENTER, and TAB keys may be used as hot keys, but they cannot be specified by pressing them. For these keys, 
press the ellipsis (...) button and type "esc," "enter," or "tab." 
3. Press the OK button to return to the Menu Editor . 
4. To display the hot key combination (or any other text) as right-justified menu text, type the text in the Menu Text field. 
For example, if you set the hot key as CTRL+h, type CTRL+h in the Hot Key Menu Text field. Then, each time the end user 
uses the menu, the right-justified text reminds her that the menu choice can be invoked with the ctrl+h keystrokes. 
 
 
Other Menu Behavior—Disabling and Toggling 
The following two "Flag" properties let you disable a selection, and set up an ITEM as toggle switch. 
 
 
Disable 
To disable a MENU or ITEM (dim the text and make it unavailable to the user), set this property to TRUE. This adds the 
DISABLE attribute to the MENU or ITEM statement. 
The Disable box is handy when you incorporate modality into a program—that is, when one type of child window does not 
support the same commands another type does. For the type that doesn‘t support the command, disable the ITEM rather 
than omitting it. This will avoid confusing the user with menu ITEMs that disappear and reappear depending on which 
window is active. 
 
 
Check 
To create an on/off toggle for a selected ITEM, set this property to TRUE. The ITEM should have a numeric variable in the 
Use property. The variable should be declared using one of the data dialogs, or in embedded source. See Creating Your 
Application's Menu above. The Menu Editor adds the CHECK attribute to this ITEM. 
With the CHECK attribute, when the user selects the item for the first time, the item is "on," the USE variable‘s value is 
one (1), and a check mark appears beside the item. When the user selects the item a second time, the item is "off," the 
USE variable‘s value is zero (0) and no check mark is displayed. You should add source code to control the application‘s 
behavior depending on the state of the USE variable. 


---

IDE User's Guide 
150 
 
 
Changing the Appearance of Menus 
The General and Color property categories lets you change and set how your menu and menu items look. These 
property settings give your menus a more professional look and allow you to conform to existing design standards. 
 
 
Icon 
To add an icon to a menu item, either select an icon from the drop list or press the ellipsis button to lookup the file name. 
This entry is not available when the MENUBAR is selected. You can use any image file Clarion supports, but keep in mind 
that large images may not give you the desired effect. For best results, choose an image that is 32x32 bits. 
When making Web based applications, use GIF images. 
Color 
Enter a valid color value in any of the following entries to add the COLOR attribute to your MENU declaration. 
See ..\LIBSRC\EQUATES.CLW for a list of valid color equates. 
TextColor 
To apply a specific color to the menu text, type a valid color equate in this entry, or press the ellipsis (...) button to 
select a color from the Color dialog. 
BackColor 
To apply a specific color to the background, type a valid color equate in this entry, or press the ellipsis (...) button 
to select a color from the Color dialog. 
SelectedTextColor 
To apply a specific color to the menu‘s selected text, type a valid color equate in this entry, or press the ellipsis 
(...) button to select a color from the Color dialog. 
SelectedBackgroundColor 
To apply a specific color to the background of the menu‘s selected text, type a valid color equate in this entry, or 
press the ellipsis (...) button to select a color from the Color dialog. 


---

User's Guide and Lessons 
151
 
 
LeftOffset 
Enter a numeric value to make the menu or menu item offset from the far left. By default, there is a small space (for icons) 
and this setting can be used to remove this space or increase it. 
The value is in dialog units (Special fractional measurement units, based on the system font. Windows automatically 
calculates the horizontal measurement unit in fourths of the average system character width, and the vertical in eighths of 
character height. The net effect supports a proportional placement of dialog box elements regardless of the resolution 
Windows is running in). 
 
 
Width (AT) 
To specify the width of your menu or menu item, choose the desired width value. Choose from: 
Default 
Setting to TRUE instructs Windows to set the width of the menu or menu item to a default value which will depend 
on the user‘s system. 
Value 
To set a specific width, mark the Default property FALSE and specify a value. This sets the width of the window in 
dialog units. 
Height (AT) 
To specify the height of your window, choose the desired height value. The choices are the same as for Width. 
 
 
TextFont 
To set a font property for this menu or menu item, press the ellipsis button and select one. If you choose a font on a menu 
item, then the menu item will appear in the font style you select. 
If a menu, then all menu items under it inherit the font. If a MENUBAR, then all menus and menu items inherit the font 
selected. 
Choose a font that could be installed on any machine. Otherwise, you will have to ship the font in your installation 
procedure. 
 
 
Managing Your Menus 
Press this button to add a separator bar after the highlighted MENU or ITEM. 
 
 
Separator bars can provide the user with a visual cue that a group of ITEMs on the menu perform related functions. 
 
 
Press this button to delete the highlighted MENU or ITEM. If you delete a MENU, all nested ITEMs and MENUs, and its 
associated END statement are also deleted. 


---

IDE User's Guide 
152 
 
 
 
 
To move the highlighted MENU or ITEM up or down in the menu list, press the appropriate button. When moving a 
MENU, all ITEMs and MENUs within it and its associated END statement move also. 
 
 
 
 
Toolbars 
With a simple action in the Window Designer, you can add a toolbar to any window. You can place any controls on a 
toolbar, but the ones you will probably use the most are command buttons, check boxes, radio buttons, and drop-down 
listboxes. As with menus, Clarion automatically merges global and local toolbars in certain situations. 
 
 
Merging Toolbars 
Global and Local Toolbars 
The TOOLBAR structure declares the tools displayed for an APPLICATION or WINDOW. On an APPLICATION, the 
TOOLBAR defines the Global tools for the program. Global tools are active and available on all MDI child windows unless 
the MDI child window‘s TOOLBAR structure has the NOMERGE attribute. 
If you specify the NOMERGE attribute on the APPLICATION‘s TOOLBAR, there are no global tools; the tools are local 
and are displayed only when no MDI child windows are open. 
To merge toolbars, the APPLICATION‘s toolbar AT width must be less than the APPLICATION‘s frame width. In the 
Procedure Properties dialog, press the Window‘s ellipsis (...) button, then set the TOOLBAR‘s width (third AT attribute) 
equal to the X position plus the width of the rightmost toolbar control. 
MDI Windows 
On an MDI window, the TOOLBAR defines tools that are automatically merged with the Global toolbar. Both the Global 
and the local MDI window‘s tools are active while the MDI child window has input focus. Once the window loses focus, its 
specific tools are removed from the Global toolbar. If the NOMERGE attribute is specified on an MDI window‘s TOOLBAR, 
the tools overwrite and replace the Global toolbar. 
Non-MDI Windows 
On a non-MDI WINDOW, the TOOLBAR is never merged with the Global menu. A TOOLBAR on a non-MDI window 
always appears with the window itself, and not on the parent window. 
Merging Order 
When an MDI window‘s TOOLBAR is merged into an application‘s TOOLBAR, the global tools appear first, followed by 
the local tools. The toolbars are merged so that the fields in the window‘s toolbar begin just right of the position specified 
by the value of the width parameter of the application TOOLBAR‘s AT attribute. The height of the displayed toolbar is the 
maximum height of the "tallest" tool, whether global or local. If any part of a control falls below the bottom, the height is 
increased accordingly. 


---

User's Guide and Lessons 
153
 
 
Toolbar Merging Checklist 
Application Properties 
1. Set the NOMERGE property of the APPLICATION‘s toolbar to TRUE. 
2. TOOLBAR‘s width property must be less than APPLICATION‘s width. 
In the Properties Pad dialog for the TOOLBAR control, set the TOOLBAR‘s Width property (third AT attribute) equal to the 
X position plus the width of the rightmost toolbar control. 
 
 
Child Window Properties 
1. Set the NOMERGE property of the WINDOW‘s toolbar control to FALSE. 
2. Set the MDI property to TRUE. 
 
 
Adding Toolbars 
The following describes how to add a toolbar to a window, then how to add a control to the toolbar. The starting point is 
the Window Designer, open to an empty window: 
1. In the Controls Toolbox, select the TOOLBAR control entry, and DRAG and DROP to the active window. 
The Window Designer places a toolbar at the top of the window (gray rectangle). 
2. To place a control on the toolbar, click on a control in the Controls toolbox, then click inside the toolbar in the 
target window. 
This places the control in the toolbar. See Controls and Their Properties for more information on various controls. 
 
 
Use .ICO files that are 32 x 32 pixels for toolbar buttons. These larger .ICO files contain both the enabled and the disabled 
icon in the same file, rather than requiring a separate file. When creating a custom .ICO file for a toolbar button, place the 
image in the center of the icon file. Clarion automatically crops the icon image to fit the button size. 


---

IDE User's Guide 
154 
 
 
 
Lesson 6 - Exploring the Browse Procedure 
This topic: 
• 
Explains how to use the List box Formatter to format your LIST and COMBO controls. 
• 
Explains how to format list box controls, including how to create multi-column list boxes, and hierarchical lists. 
 
 
Creating List Boxes 
The heart of ALL Browse procedures centers on scrolling (or browsing) through selected table information using a LIST 
control. 
The LIST control is most useful for presenting a great number of choices to the user. It can display a large amount of data 
in a small area, which has led to its use as an all-purpose data control. Using Clarion you can create list boxes which look 
like spreadsheets, perform drag and drop tasks, and more. 
Further, you may use Control templates (BrowseBox, FileDrop, etc.) to generate code that declares the LIST and 
manages it too (loads it, scrolls it, locates items, selects items for processing, etc.). 
As you read this section, please be aware that all the information that applies to LIST controls also applies to COMBO 
controls. 
When you create a list box (whether a control template or a simple control), you define its data source, its format, and its 
functionality. The development environment divides these property definitions among three dialogs: 
The List Box control‘s Properties Pad specifies the queue that supplies the list data, the general scrolling capability, and 
whether the list is a drop-down list or a regular list. In other words, the List Properties dialog specifies all the properties of 
the list box that are not column-specific. 
The List Box control‘s Properties options are discussed in more detail in the List Control Properties core help topic. 
 
 
List Box Formatter 
The List Box Formatter dialog lets you add, delete, reorder, and resize the specific columns that are displayed in the list 
box. In other words, the List Box Formatter dialog specifies all the column-specific properties of the list box. 
The List Box Formatter is a visual design tool—a subset of the Window Designer—that generates Clarion Language 
statements to format your application‘s LISTs. The List box Formatter provides a wide degree of flexibility to create and 
modify your list boxes, drop-down list boxes, and combo boxes. You may invoke the List Box Formatter from the Window 
Designer or from the Report Designer. 
Once you specify a QUEUE to provide the data for the list (done automatically when specifying a BrowseBox template), 
the List box Formatter lets you customize your list in the following ways: 
• 
You can set the number, content, and formatting of columns, with or without resizable borders. 
• 
You can specify that a row from the QUEUE occupy more than one list box row. 
• 
You can add horizontal scrollbars for each column or group of columns in the listbox. 
• 
You can specify the focus on rows or individual "cells," spreadsheet fashion. 
• 
You can specify headers for the list box columns. 
• 
You can add a locator control that allows users to quickly find the item they need. 
• 
You can enable selection of multiple rows in the list. 
• 
You can enable colorization of items in the list. 
• 
You can enable iconization of items in the list. 


---

User's Guide and Lessons 
155
 
 
 
• 
You can enable nesting (indenting) of items in the list. 
• 
You can create column tool tips. 
 
 
List Overview 
LIST controls come in a variety of forms, the most common of which are list boxes, drop-down list boxes, and combo 
boxes. 
A list box, by convention, is a read-only display of data in a tabular format (rows and columns). It is scrollable and may 
display many rows and columns. It efficiently displays large amounts of data. 
A drop-down list box, by convention, is a read-only display of mutually exclusive selections or choices. It is often scrollable 
and is called a drop-down list because it initially appears as a single row, but "drops down" to display multiple rows, like a 
menu. It forces valid user selections, provides a visual cue reminding the user that a selection is required, offers a default 
selection, and doesn‘t take up much screen space. 
A combo box is a drop-down list box with the ability to accept user input. 
When creating a list box control, you define its data source, its functionality, and its format. Clarion‘s development 
environment divides these property definitions among several dialogs: 
• 
The List Box Properties Pad specifies a drop-down list versus a regular list, specifies the queue that supplies the 
list data, and specifies the general scrolling capability, that is, all the properties of the list box that are not column- 
specific. 
• 
The List box Formatter dialog lets you add, delete, reorder, and resize the specific columns displayed in the list 
box. And it defines the appearance and behavior of individual list box columns as well as groups of columns. For 
example, define individual column headers, widths, and scrolling, or spread a header across several columns. 
This dialog is discussed here. 
After you‘ve started defining your list box with the Formatter and Properties Pad, these are the general steps for 
completing your list box. 
 
 
Understanding the List Box Formatter 
 
 
Add columns, one by one, and format them 
From the Window Designer, RIGHT-CLICK on the LIST or COMBO control, then choose List Box Format... from the popup 
menu to open the List box Formatter dialog. 
The Sample List Box 
The List Box Formatter displays a representation of the list box—the sample list box. Each field appears as a column in 
the list box. If any field contains a header, a header row appears over the list. You format the columns one by one, which 
updates the sample list box. 
The List Box Formatter does not display a vertical scroll bar, even if you checked the Vertical box in the List Properties 
dialog. However, the vertical scroll bar does appear at run time, if the queue contains more items than will fit in the list 
box. 


---

IDE User's Guide 
156 
 
 
 
 
 
 
1. Press the Add Field button 
to add a new field (column). 
When working from within the Application Generator, choose a column from the Select Column dialog. The List Box 
Formatter adds the selected column. 
2. In the List Box Properties Pad, set the column-specific heading width and text, data format, scrolling, and other 
attributes. 
3. Use the Color and Style and Flags property categories to set the column-specific icons, colors, fonts, and nesting. 
 
 
For each setting you make, the List box Formatter creates the appropriate FORMAT attribute for the LIST statement that 
defines your list box. 
 
 
At run-time, the PROP:Format property always contains the current format of the listbox, including any user changes. To 
save the user‘s column sizes, use GETINI and PUTINI to save and restore the PROP:Format values: 
PUTINI('Settings','UserList',?List{PROP:Format},'MYAPP.INI') 


---

User's Guide and Lessons 
157
 
 
 
 
• 
To remove a column from the listbox, press the 
 button. 
• 
To cancel the formatting changes, press the Cancel button. 
• 
To accept the formatting changes and close the List box Formatter, press the OK button. 
• 
To move the selected column to the left, click the 
 button, or press CTRL+UP arrow. 
If the selected column is leftmost in a group, the 
 button moves the field out of the group, but the order of the 
columns is unaffected. Conversely, the 
 button moves the selected column into a group at its immediate left, 
and the order of the columns is unaffected. 
• 
To move the selected column to the right, click the 
 button, or press CTRL+DOWN arrow. 
If the selected column is rightmost in a group, the 
 button moves the column out of the group, but the order of 
the columns is unaffected. Conversely, the 
 button moves the selected column into a group at its immediate 
right, and the order of the columns is unaffected. 
• 
You can also just use the keyboard. Hold the CTRL key and press the up or down arrow key. To unselect all 
items just release the Ctrl key and press the up or down arrow key. or release the CTRL key and mouse click on 
any column. 
The List Box Formatter property options are discussed in more detail in the List Box Formatter Dialog core help topic. 


---

IDE User's Guide 
158 
 
 
 
Lesson 7 - Exploring the Form (Update) Procedure 
Overview 
The Form procedure is derived from the basic Window procedure. It generates code to display and update a single record 
from a table. It also generates code to display and access related records in other related tables. 
The Form procedure begins by using a FORM (Add/Edit/Delete) procedure default, which provides a predefined window, 
a SaveButton Control template and a ValidateRecord Extension template. 
The SaveButton Control template handles the table I/O and the ValidateRecord template validates incoming data 
according to data dictionary settings. The Data / Tables Pad automatically attaches your table choices to the SaveButton 
Control template. For accessing related records, the Form wizard template optionally provides a BrowseBox Control 
template. 
 
 
Browse-Form Paradigm 
The Form template is an integral part of Clarion‘s Browse-Form paradigm which uses Browses (windows with sortable, 
scrollable, searchable, selectable lists of data), Forms (windows with a single updatable database record), and Reports to 
organize and present database information to end users. 
A Form can deviate from this paradigm with the use of the FormVCRButtons Control template. This template provides 
nearly all of the functions provided by the Browse, but without the list control. 
 
 
Form Template Prompts 
In addition to the standard Application Generator command buttons and prompts, the Form template Procedure Properties 
Actions dialog contains the prompts inherited from the Window Template (Parameters, Return Value, and Window 
Behavior—see Window Procedure Templates – Window Template Prompts), plus the prompts provided by the 
ValidateRecord Extension and the SaveButton Control. 


---

User's Guide and Lessons 
159
 
 
 
 
 
Record Validation 
The RecordValidation Extension template adds additional prompts so you can control how and when record validation 
happens. 
 
 
Save Button Properties 
The SaveButton Control template provides additional prompts so you can control how and when the record is updated, 
including the type of updates allowed, whether multiple inserts are allowed, messages shown to the end user, and more. 


---

IDE User's Guide 
160 
 
 
 
Lesson 8 - The Report Designer 
Overview 
Using the Report Designer, you visually lay out your application‘s reports. The Report Designer automatically generates 
and places all the code structures necessary to produce the reports. Preview the reports without actually generating any 
code or data. 
This topic starts with an overview of Clarion‘s page oriented print engine, and a comprehensive treatment of each 
feature of the Report Designer. It concludes with a detailed look at creating a report. 
Clarion has many powerful reporting features and we want to systematically cover all of them. However, you the 
developer, probably have a particular report you need to produce by yesterday! To read about those features that will help 
you produce your particular report right now, fast forward to the Creating Reports topic in this lesson. 
Clarion's Report Engine 
Before you explore the Report Designer, it‘s important to understand how reports are printed by Clarion within the 
Windows environment. Please refer to How the Print Engine Processes Report Sections at Runtime in the core help file to 
read an informative topic regarding this process, before continuing to the next section. 
 
 
 
 
Report Designer Interface 
 
Opening the Report Designer 
You can access the Report Designer from the Application Generator or from the Text Editor. 
 
 
To open the Report Designer from the Application Generator 
1. From the Application Tree, RIGHT-CLICK the report then choose Report from the popup menu (or press the Report 
button). 
This opens the Report Designer. You‘re now ready to construct the report, section by section. 
 
 
When you open the Report Designer with the Application Generator, you have full access to the data dictionary "short 
cuts"—the Column Toolbox, the Populate menu, the Data / Tables Pad, Control Templates Pad etc. 
 
 
To open the Report Designer from the Text Editor 
1. Open a source code document. 
2. Locate a blank line in the data section and place the cursor there. 
This is where the Report Designer places the Clarion language REPORT structure. 
3. Choose Edit  Structure Designer from the IDE menu. 
You may also press the CTRL+D keyboard accelerator. This opens the New Structure dialog. 
4. From the New Structure dialog, choose a valid Report structure. The following defaults are available: 
Paper size A4 - Portrait 
Paper size A4 - Landscape 


---

User's Guide and Lessons 
161
 
 
Paper size Legal - Portrait 
Paper size Legal - Landscape 
Paper size Letter - Landscape 
Paper size Letter - Portrait 
This opens the Report Designer. You‘re now ready to define the report. 
 
 
To edit an existing report from the Text Editor, open the source code file and place the cursor on any line within the 
REPORT structure, then choose Edit  Structure Designer from the menu, or press CTRL+D. 
 
Band View 
When you first open the Report Designer, your report appears in Band View. That is, each REPORT section (HEADER, 
BREAK, DETAIL, FOOTER, and FORM) appears in a separate "band" inside the window. This is true even though the 
report sections may actually overlap when printed. 
 
 
 
 
Rulers 
To quickly determine each section‘s position, look at the rulers. The horizontal (X axis) ruler shows the position relative to 
the left edge of the page. The vertical (Y axis) rulers show the positioning relative to the top of each band. The 
measurement units are set in the Report Properties dialog (see Report Structures and Properties in the Language 
Reference Manual). 


---

IDE User's Guide 
162 
 
 
Caption Bars 
Each report section has it‘s own caption bar. Each caption bar displays the band type and an expand/contract button at 
the far right. Break section caption bars also display the name of the variable the section breaks on. 
Show/Hide Button 
 
To expand or contract the report band, click on the expand/contract button at the far right of its caption bar. 
 
 
Report Designer Toolboxes 
During the design process, there are several Report Designer tools at your disposal. 
 
 
Click on the appropriate link for a more detailed examination of each tool: 
 
 
In the core help FAQs, examine the following topics: 
 
 
Using the Report Designer - Sample Reports 
Using the Report Designer - Controls Toolbox 
Using the Report Designer - Populate Columns 
Using the Report Designer - Property Toolbox 
Report Designer Alignment Options 
Using the Report Designer - Command Toolbar 
 
 
Report Designer Menus 
The Report Designer provides many features available from standard and popup menus. 
Please refer to the Report Designer Menu Commands topic in the core help for a detailed explanation of the menu 
commands and options. 


---

User's Guide and Lessons 
163
 
 
Report Structures and Properties 
The REPORT structure contains all the information necessary to format and print each report page. Following is an 
example of a REPORT structure with empty headers, footer, and form, a break on "CustNumber," and several variable 
strings in the detail. The Report Designer generated the following structure. 
 
 
Report 
 
 
REPORT,AT(1000,2000,6000,7000),PRE(RPT),FONT(‘Arial’,1 
## 0,,),THOUS HEADER,AT(1000,1000,6000,1000)
END 
CustBreak BREAK(CUS:CustNumber) 
## HEADER,AT(,,,1000)
END 
Detail 
## DETAIL
STRING(@n4),AT(125,52),USE(CUS:CustNumber) 
STRING(@S20),AT(125,208),USE(CUS:Company) 
STRING(@S20),AT(125,365),USE(CUS:Address) 
STRING(@S20),AT(125,531),USE(CUS:City) 
STRING(@S2),AT(125,688),USE(CUS:State) 
STRING(@n5),AT(125,844),USE(CUS:ZipCode) 
END 
END 
## FOOTER,AT(1000,9000,6000,1000)
END 
## FORM,AT(1000,1000,6000,9000)
END 
END 
 
 
Report Properties 
There are two Report Properties dialogs. One of these dialogs is associated with the Report Procedure template. This 
dialog is accessed with the Actions button in the Procedure Properties dialog and is discussed in the Report Template 
topic. 
The other Report Properties dialog is the Report Properties Pad associated with every report, whether or not the Report 
Procedure template is used. This dialog is accessed from the Report Designer by choosing Report Designer  
Properties, and discussed here. This dialog allows you to set up basic report options, including page orientation, 
measurement units, detail print area, fonts and paper size. We recommend setting these options before laying out other 
parts of your report. 
 
 
Color 
Enter a valid color equate in the TextColor or BackGround fields, or press the ellipsis (...) button to select a color from 
the Color dialog. The Report Designer adds the COLOR attribute to your report declaration. 
See ..\LIBSRC\EQUATES.CLW for a list of valid color equates. 


---

IDE User's Guide 
164 
 
 
Design 
 
Locked 
"Freezes" all the controls on the report so that subsequent data dictionary 
changes are not applied. You can override the #Freeze attribute for all 
controls or for individual controls. See Application Options in the core 
help.. 
 
 
Extra 
 
Preview 
Specifies the name of a QUEUE which stores the filename(s) (*.WMF) for 
the metafile(s) generated for page preview. See the PREVIEW attribute in 
the Language Reference. If you are using the Report Template, it is 
handled automatically if you check the Print Preview box and you should 
leave this entry blank. 
 
 
General 
 
Jobname 
Names the print job, as listed in the Windows Print Manager application. 
 
Label 
Type a valid Clarion label to name the REPORT data structure. 
 
Landscape 
Specifies landscape paper orientation. New reports default to portrait 
mode. Landscape means the report text is aligned parallel with the 
longest paper edges. 
 
Layout 
Indicates the orientation of the report controls. Left to Right maintains the 
original layout specified in the Report Designer. Default field navigation 
moves from left to right. Right to Left essentially "flips" the report 
controls‘ display as a mirror image of the layout specified in the Report 
Designer. 
 
Paper-Type 
Choose from over 40 standard sizes, or choose Other to specify a custom 
size. 
 
Width 
Specifies a custom paper width in units specified on the General tab. 
Height 
Specifies a custom paper height in units specified on the General tab. 
Prefix 
Specifies the label prefix for the REPORT structure. 
TextFont 
To set the default font for all controls appearing in the report, press the 
Font button, then choose the font and style in the Font dialog. You may 
override the default by setting a different font in the Properties dialog for 
any specific control. The options you choose in the dialog become the 
parameters for the FONT attribute. As you choose options, the dialog box 
displays a sample of the formatting. 
 
Units 
Specifies the default measurement for all controls placed in the report. 
Choose Dialog Units, THOUSandths of Inches, MilliMeters or POINTS. 


---

User's Guide and Lessons 
165
 
 
 


---

IDE User's Guide 
166 
 
 
Position 
Lets you set the location and size of the report detail print area, by filling in the AT attribute. The measurement units for 
these boxes are specified on the General tab. 
To set a precise starting point for your print detail area relative to the top left corner of the paper, specify Top Left Corner 
coordinates with this dialog. In effect, this establishes the left margin for your report. The top margin is usually determined 
by the Page Header position. These settings may also be accomplished visually by dragging report sections and borders 
in the Report Designer's Page Layout View. 
To set the size of the print detail area, choose from the following options for the Width and Height. When changing a 
report from portrait to landscape, or vice versa, you should also change the width and height on this tab. 
 
Default 
Sets a value based on the Paper Type property. 
 
Value 
To set a specific size, mark the Value choices. 
 
 
 
 
Band Properties – Form 
To specify constant text or graphics which print on every page, place it in the FORM. The print engine composes the 
FORM at the beginning of the print job; it does not update it with each new page. Therefore, the FORM is not suitable for 
holding variable data, or even a page number. You can, however, print columns from a control table, if you wish to print 
the same column contents on every page. 
The form usually overlaps the other sections and may be used as a layer, to hold graphic frames or "preprinted" material 
into which the data from the other sections fit. You might use lines and boxes, for example, to divide the DETAIL into 
compartments, grouping data for the user. You may even create a "greenbar" effect by alternating gray or light green color 
blocks. Another use for the FORM is to simulate a watermark. 
For best results when using a drawing tool to create a watermark, on, for example, a 300 DPI printer, set the fill for the 
watermark element to 10% gray, or light gray. At higher printing resolutions, try 20% gray. 
To add a form to your report, choose Bands   Page Form. 
For a detailed examination of the Form Band properties, see Report Form Properties in the core help. 
 
 
Band Properties – Page Header 
To specify text and data to compose at the start of each page, place it in the page HEADER. Remember, the page header 
may be physically positioned anywhere on the page, not just at the top. 
Typically, the HEADER includes a report title and the page number. It is also a useful place to display your company logo. 
To add a page header to your report, choose Bands   Page Header. 
For a detailed examination of the Page Header properties, see Page Header Properties in the core help. 


---

User's Guide and Lessons 
167
 
 
Group Breaks 
Group breaks provide a means of grouping report data into sections and optionally displaying subheadings, subtotals, or 
other information associated with the group. Each group consists of a set of row all sharing the same value in the BREAK 
field. 
When the value of the break variable changes, the old group ends and a new group begins. Ending a group means that 
the last DETAIL in the group is processed and the group FOOTER is composed. Beginning a group means that the group 
HEADER is composed and the first DETAIL in the new group is processed. In order to produce meaningful groups, the 
row must be sorted on the same columns the BREAKs are declared on. See Specifying Sort Order and Specifying Nested 
Group Breaks. 
Within a report, you may visually separate these groups with spaces, subtotals, headers, or other summary information, 
either above the group, below the group, or both. Displaying summary information for a group is accomplished by placing 
text or graphic controls in a group HEADER or FOOTER. 
A BREAK structure may contain most of the same elements as a REPORT structure: group HEADERs, DETAILs, group 
FOOTERs, and BREAKs. Thus breaks may be nested, giving several levels of record grouping. The Report Designer 
displays group breaks in an indented outline structure which lets you easily visualize nested group breaks. 
For a detailed examination of the Group Break general properties, see Break Properties in the core help. 
For a detailed examination of the Group Break Header properties, see Break Group Header Properties in the core help. 
For a detailed examination of the Group Break Footer properties, see Break Group Footer Properties in the core help. 
 
Band Properties – Detail 
To specify the data for the body of the report, place it in a DETAIL. This is typically where lowest level information is 
printed. High level, duplicate, or summary information is better suited to HEADER or FOOTER structures. To add a 
DETAIL, choose Bands   Detail. 
Note that a report may have multiple DETAILs that can be printed conditionally. This is useful for printing one-time only 
pages such as title pages or grand total pages (see Creating Totals and Calculated Fields ). You can also use embedded 
source statements to control which DETAIL to print at run-time. Each DETAIL structure requires its own PRINT statement. 
The DETAIL prints within the print detail area defined by the REPORT‘s AT attribute. Additionally, any the group 
HEADERs, group FOOTERs, or group BREAKs also print inside the detail print area. 
For best automatic handling when it comes to placing structures on the page, nest your DETAIL inside all other structures. 
For example, if you have two BREAK structures, one nested in the other, delete all DETAIL structures except the one 
nested inside the innermost BREAK. 
For a detailed examination of the Group Break properties, see Detail Band Properties in the core help. 
 
 
Band Properties – Page Footer 
To specify text and data to generate at the end of each page, place it in the page FOOTER. Remember, the page footer 
may be physically positioned anywhere on the page, not just at the bottom. Typically, the page FOOTER includes totals, 
page numbers, print dates, etc. To add a page footer to your report, choose Bands   Page Footer. 
 
For a detailed examination of the Page Footer properties, see Page Footer Properties in the core help. 


---

IDE User's Guide 
168 
 
 
 
Lesson 9 - Exploring the Report Procedure 
Clarion has many powerful reporting features and we want to systematically cover all of them. However, you the 
developer, probably have a particular report you need to produce by yesterday! You may only want to read about those 
features that will help you produce your particular report right now. Therefore, this chapter provides a "how to" reference 
for common report effects and functions such as sorting, totaling, page breaking, etc. 
This chapter provides a list of report functions and effects that developers are frequently or occasionally asked to provide. 
It provides a general description of how to create specific report effects, plus a reference to those parts of the Report 
Designer that are needed to produce the particular effect. 
This chapter also suggests a proper sequence for building reports. For example, we discuss the features that define 
tables and keys and establish page size, orientation, and margins before the features that lay out other parts of the report. 
The list of effects is not comprehensive, but instead attempts to launch you quickly into doing a variety of report functions. 
Once you understand how to create these basic effects, you will be well on your way to creating truly dazzling special 
effects for your reports. 
For systematic coverage of all Report Designer tools and features, see the Report Designer chapter topic. 
 
 
Common Reporting Tasks 
Creating the Report Procedure 
If you have not defined a report procedure, you may do so by opening the Application Tree dialog and pressing the INSERT 
key, or by pressing the New Procedure button. When the Select Procedure Type dialog opens, select Report from the 
Templates tab. 
 
 
 
This creates a report procedure. and opens its Procedure Properties dialog. You should next specify the report‘s tables 
and keys as described immediately below. 
Alternatively, you may use the Report Wizard to help you define your report procedure. 


---

User's Guide and Lessons 
169
 
 
Specifying Tables 
The first logical step in preparing a report is to specify the tables and keys your report procedure uses. You should do this 
from the Data / Tables Pad, before starting the Report Designer. 
 
 
 
The tables you specify determine which data dictionary columns can appear on your report. You may specify more than 
one table to report on, that is, a primary table plus secondary related tables and even other unrelated tables. See Adding 
Relationships. 
 
 
To specify the tables for your report 
1. Open the Data / Tables Pad. Use this dialog to tell the Application Generator which tables and keys your report 
procedure uses. 
2. Highlight the <ToDo> item for your report procedure, and press the Add button in the Data / Tables Pad toolbar. 
This opens the Select a Table dialog. 
3. Select the table you wish to report from. 
This sets the table and closes the Select a Table dialog. The <ToDo> item is replaced by the primary table you chose. 
 
 
Printing From More Than One Table (Adding Secondary Tables) 
1. From the Data / Tables Pad, select the primary table for your report procedure, and press the Add button in the 
Data / Tables Pad toolbar. 
This opens the Select a Table dialog, listing tables related to the primary table. On the other tab, is all the tables in your 
dictionary. 
2. 
DOUBLE-CLICK or select the additional table you wish to report. 
This sets the table and closes the Select a Table dialog. Repeat these steps for any other tables, related or otherwise. 
When adding tables, you may also select a secondary table, and then choose from tables related only to the secondary 
table. 
All the columns from the primary table and the secondary tables may be displayed on your report, and they are available 
for sorting and filtering as well. 


---

IDE User's Guide 
170 
 
 
Specifying Keys (Sort Order) 
The keys (or indices) you specify for your report procedure will determine the sequence in which the report items appear. 
The keys should also determine break variables and nesting order of any group breaks. 
Adding secondary tables (see above) to your procedure also gives you another logical column to break on—that is, the 
common columns linking the two tables. 
 
 
The ABC Report Template lets you specify other sort columns in addition to the key you set in the Data / Tables Pad. See 
Procedure Templates—Report Template in the core help. 
To specify the keys for your report: 
1. From the Data / Tables Pad, select the primary table for your report procedure, and press the Change button in 
the Data / Tables Pad toolbar. This opens the Select Key from dialog. 
2. 
DOUBLE-CLICK or select the key you want for this report. This sets the key and closes the Select Key from dialog. 
 
 
Specifying Which Rows to Print (Range Limits & Filters) 
You don‘t always want to print all the rows in a table. Often, you want to specify a subset of rows to print. You can specify 
a subset of rows to print by using Range Limits, Filters, or both. 
You should use Range Limits whenever possible to specify your row selection, because Range Limits use table keys and 
are therefore very fast. When Range Limits cannot provide a narrow enough selection criterion, you can add Filters to 
restrict your report to precisely the rows you need. 
To specify Range Limits and Filters, open the Procedure Properties dialog for your report, then press the Report 
Properties button. 
 
 
Specifying Paper Size and Orientation 
Paper size and text-to-paper orientation should be carefully thought out and established early in the report development 
process. Changing these settings after the report columns, headings, etc. have been laid out usually results in redoing 
much of the layout work. 


---

User's Guide and Lessons 
171
 
 
 
To set the paper size and orientation, open the Properties Pad in the Report Designer. Choose Report Designer 
 Properties, then select and edit the Paper Type property. 
Measurement Unit 
To change the page measurement unit, edit the Units property in the Properties Pad. Select dialog units, thousandths of 
inches, millimeters, or points from the Units drop-down list. 
Dialog units are defined as one-quarter the average character width by one-eighth the average quality height. The size of 
a dialog unit depends on the size of the default font for the report. This measurement is based on the font specified in the 
FONT attribute of the report or on the printer‘s default font. 
 
 
Specifying Report Margins 
Margins for the various report sections (FORMs, page HEADERs, page FOOTERs, and the detail print area) are all set 
independently of each other, therefore, there is no one margin setting that applies to the entire report. You may specify 
these margins visually with the Report Designer‘s Page Layout View. Please note that the boundaries of each of these 
structures may overlap. 
To use the Page Layout View effectively, you should maximize the window so you can see as much of the report at one 
time as possible. Then use the TAB key to select the report section to reposition (the Report Designer displays the selected 
section in the status bar at the bottom of the window). Finally, set the position of the selected section by clicking and 
dragging its interior, or position one or two edges of the selected section by clicking and dragging one of its handles. 
You may also specify the margins of the FORM, page HEADER, page FOOTER, and detail print area on the Position tab 
of the respective Form Properties, Page/Group Header Properties, Page/Group Footer Properties, and Report Properties 
dialogs. 


---

IDE User's Guide 
172 
 
 
The Detail Print Area 
The detail print area is defined by the REPORT structure‘s AT attribute. The four rules you should understand and 
remember about the detail print area are: 
• 
Every DETAIL, group HEADER, and group FOOTER is printed within the boundaries of the detail print area. 
• 
The boundaries of the detail print area may be set with the Report Designer‘s Page Layout View or with the 
Position (AT) properties of the Report‘s Properties Pad dialog. 
• 
Each item within the detail print area is printed relative to the previous item printed. 
• 
The relative position of items printed within the detail print area may be set with the Position tab of the item‘s 
Properties dialog, or by dragging the item‘s handles in Band View. 
 
 
Positioning and Alignment 
 
 
The AT Attribute 
Select the Position properties in the Report‘s Properties Pad to set the AT attribute for various report structures. The AT 
attribute on print structures performs two different functions, depending upon the structure on which it is placed. 
When placed on a FORM, page HEADER, or page FOOTER, the AT attribute defines the position and size of the 
structure. The position specified by the x and y parameters is relative to the top left corner of the page. 
When placed on a DETAIL, a BREAK, a group HEADER, or group FOOTER, the structure is printed relative to the 
previous item printed, according to the following rules (unless the ABSOLUTE attribute is present): 
• 
The width and height parameters of the AT attribute specify the minimum size of the structure. 
• 
The structure is actually printed at the next available position within the detail print area. 
• 
The position specified by the x and y parameters of the structure‘s AT attribute is an offset from the next available 
print position within the detail print area. 
• 
The first item is printed at the top left corner of the detail print area (at the offset specified by its AT attribute). 
• 
Next and subsequent items are printed relative to the ending position of the previous item: 
 
If there is room to print the next item beside the previous item, it is printed there. If not, it is printed below the previous 
item. 
 
 
Precise Positioning and Alignment 
There are four major tools to help you precisely align your report data: Grid Snap, alignment tools, the Position properties 
of the respective properties dialogs, and constrained dragging. Grid Snap is discussed in Report Designer— Menus. The 
alignment tools are discussed above in Report Designer— Toolboxes. 


---

User's Guide and Lessons 
173
 
 
 
 
For precise positioning, edit the Position properties of the respective properties pad. When you position a structure on 
screen, the smallest unit you can move it is usually 1/96 inch. However, the Position properties lets you specify position 
by thousandths of inches. 
 
 
Constrained Dragging 
Press and hold the SHIFT key while dragging a control to limit the control‘s movement to a single axis. That is, SHIFT + DRAG 
moves a control either horizontally or vertically, but not both. 
 
 
Skipping Blank Lines 
Use the SKIP attribute on a STRING control to suppress printing an empty string. That is, an empty STRING with SKIP 
attribute on a line by itself takes up no vertical space on the page. 
For labels or other reports that may have an empty STRING on the same line as non-empty STRINGS, you can populate 
a series of local STRING variables, such as AddressColumn1 and AddressColumn2, on your report rather than the 
optional database columns. Then embed source code such as: 
 
 
IF MBR:Address2 
!If 2nd address line not empty 
AddressColumn1 = MBR:Address2 !assign it to the report column 
AddressColumn2 = CLIP(MBR:City)&', '&MBR:State&' '&MBR:Zip 
## ELSE
!If 2nd address line is empty 
AddressColumn1 = CLIP(MBR:City)&', '&MBR:State&' '&MBR:Zip 
AddressColumn2 = '' 
!skip it 
END 
 
 
Alternatively, you can populate a TEXT control on your report whose USE variable is a STRING that is long enough to 
contain the entire series of optional and required database columns. Then embed source code such as: 
 
 
TextColumn = CLIP(FirstName)&' '&MBR:LastName&'<13,10>' !name + return 
TextColumn = CLIP(TextColumn)&MBR:Address1&'<13,10>' 
!address + return 
IF MBR:Address2 
!if address2 exists 
TextColumn = CLIP(TextColumn)&MBR:Address2 &'<13,10>' !address2 + return 
END 
TextColumn = CLIP(TextColumn)&CLIP(MBR:City)&', '&MBR:State&' '&MBR:Zip 
 
 
 
Handling Different Size Memos 
Use the RESIZE attribute on a TEXT control to allow the control (and the report band) to expand to accommodate all of 
the text. That is, with the RESIZE attribute, you need not make the report band or the TEXT control as large as the largest 
data item to be printed. Make the controls as small as the smallest item and the report engine expands the controls for 
larger items. 


---

IDE User's Guide 
174 
 
 
Specifying a "Pre-printed" Form 
In the Report Designer‘s Report Form Band, place text or graphic controls in the form band. This specifies constant text or 
graphics which prints on every page. This underlying "form" prints independently of and "underneath" all other items on 
the report. 
See Form in the Report Designer chapter. 
 
 
Specifying Page Headers and Footers 
In the Report Designer‘s Band View, place text or graphic controls in the page header band or the page footer band. Use 
the Bands menu to add bands as required. 
Page headers are composed prior to details and breaks. Page footers are composed after details and breaks. Both 
HEADERs and FOOTERs may be located anywhere on the page. 
The data printed in the page headers and footers may be constant or variable. Page headers and footers are typically 
used to present report titles, fixed column headings, page numbers, print dates, company logos, etc. 
See Report Designer—Page Header and Page Footer. 
 
 
Specifying Column Headers and Report Titles 
Static strings are good for printing column headings, report titles, and any other text that doesn‘t change. You will usually 
want to place your titles and headings in the page header or the page form. If you need to print titles or headings that 
change, see Specifying Columns to Print. 
 
 
See also Controls and Their Properties—String Properties. 
 
 
To place a static string control in your report 
1. Select the STRING control from the Controls Toolbox, and DRAG AND DROP in the band that displays the title 
(usually the page header). 
The Report Designer places a STRING control in the report structure. The center of the crosshair positions the upper left 
corner of the string. 
2. 
RIGHT-CLICK the control then choose Properties from the popup menu. 
3. In the Properties Pad, enter the text to display in the Text property. 
No quotation marks are needed. 
4. Modify the Font property to specify the typeface, size, color, and style of the text. 
 
 
Alternatively you may specify the text and it‘s font with the Property toolbox. Choose Option 
Show Propertybox. 
5. Specify the text justification with the Justification property drop-down list. 
 
 
For special effects 
6. Set TextColor and Angle properties. 


---

User's Guide and Lessons 
175
 
 
Specifying Columns to Print (variable text) 
Variable string controls are the basic unit for printing variable data in the report. Variable strings are also used for 
displaying totals and other calculated columns. 
By using the USE variable, the report procedure accesses the memory variable or data dictionary column you want to 
print. The Report Designer formats the data according to the picture token you specify. 
To place a variable string control in your report 
1. Use the Data / Tables Pad, or highlight a column in the Populate Column toolbox (choose Report Designer 
 Populate  Column). 
Using either method lets you place a data dictionary column only, without ever leaving the Report Designer. Using the 
Populate Column option lets you select from data dictionary columns and memory variables using the Select Columns 
dialog. 
2. 
CLICK in the band that will contain the variable string (usually the detail, group header or group footer). 
The Report Designer places a STRING control in the REPORT data structure with a variable as the string‘s Use property, 
and sets the following string properties: the VariableString property is TRUE, a Text property picture token and a 
Justification value is provided based on the data dictionary information for the selected column or variable. 
Alternatively, you can place a string control, then set the string properties manually to accomplish the same result: set the 
VariableString property to TRUE, type the variable name in the Use property, type a picture token in the Text property, 
and select a Justification value from the drop-down list. 
3. Edit the Font property to specify the typeface, size, color, and style of the text. 
Alternatively you may specify the text and it‘s font with the Properties Toolbar. From the IDE Menu, choose Tools 
 Options  REPORT Structure Designer  Show Properties Toolbar. 
 
For special effects: 
4. In the Properties Pad, optionally set the TextColor and Angle properties. 
5. Optionally, select a total type from the TotalType property drop-down list to create sums, averages, tallies 
(counts), page numbers, etc. 
 
 
Specifying Group Breaks 
In order to have meaningful groups or subtotals in your report, the report rows must be sorted properly. 
To create a group break 
1. In the Report Designer IDE Menu, choose Bands  Surrounding Break. 
2. Move the cursor over the detail band, then, when the cursor changes to a crosshair, CLICK in the DETAIL band. 
This opens the Break Properties dialog. 
3. In the Variable entry, enter a break variable. 
At runtime, when the variable‘s value changes, a new group begins. 
4. In the Label entry, enter a valid Clarion label to use as a label for the BREAK structure. 
This label may be referenced by the RESET and TALLY attributes. 
5. In the Use entry, enter a field equate label to reference the BREAK in your source code. 
6. Press the OK button. 
This inserts the group BREAK. When the break variable changes, the report composes the group FOOTER and the next 
group HEADER defined for the break. 


---

IDE User's Guide 
176 
 
 
Specifying Group Headers and Footers 
The print engine composes the group HEADER before the group DETAIL. The group HEADER is a good place to identify 
the group, for example, with a static string saying "Customer:" followed by a variable string displaying the customer name 
column. 
The print engine composes the group FOOTER after the group DETAIL. The group FOOTER is a good place to 
summarize the group, for example, with a static string saying "Total:" followed by a variable string displaying a sum. See 
Creating Totals. See also Report Designer—Group Breaks—Group Headers and Group Footers. 
1. First, define a group break as described above. 
2. Choose Bands  Group Header from the Report Designer IDE menu to define a group HEADER for the 
## BREAK.
3. Move the cursor over the break band; when the cursor changes to a crosshair, CLICK in the BREAK caption bar. 
This opens the Page/Group Header Properties dialog. Specify a field equate label and any special page breaking 
behavior. 
4. Press the OK button. 
This inserts the group HEADER band. You may place controls here just as in any other report band. Group footers are 
added similarly, using Bands  Group Footer from the menu. 
 
Specifying Nested Group Breaks 
A nested break is created the same way as the first break. The second break may be nested "within" the first break by 
placing the second break on the detail inside the first break. Alternatively, the second break may be added "outside" the 
first break by placing the second break on the first break. 
When establishing nested breaks, you should coordinate the nesting order of the breaks with the sort order of the tables 
being processed. For example, if you have chosen a key composed of the Department, Title, and LastName columns, 
then you could similarly break on LastName, within Title, within Department. 
You can review your key‘s component columns in the Data Dictionary‘s Column/Key Definitions dialog. 
Adding secondary tables to your procedure also gives you another logical column to break on: that is, the common 
columns linking the two tables. 
 
 
Specifying Page Breaking Behavior 
Edit the properties of the group HEADERs, the DETAILs, and/or the group FOOTERs. There are several options 
available. The options are Page Before, Page After, With Next, and With Prior. 
 
 
Creating Totals and Calculated Columns 
See Specifying Columns to Print above. 
A total column is simply a variable STRING control with the SUM attribute added. The AVE, CNT, MAX and MIN attributes 
similarly create averages, counts (tallies), maximum, and minimum columns. These attributes may be added by choosing 
from the Total type drop-down list in the String Properties dialog. 
In addition, you can precisely control the totaling behavior by specifying the RESET attribute from the Reset on drop- 
down list and by specifying the TALLY attribute from the Tallies list on the Extra tab. Finally, you can get ultimate control 
by specifying a variable to receive intermediate values for the SUM, AVE, CNT, MAX, and MIN operations with the Using 
entry. You can perform custom calculations in embedded source using the intermediate variable to get any result you 
need. 


---

User's Guide and Lessons 
177
 
 
 
 
You cannot automatically calculate intermediate group level totals with Clarion‘s Report Procedure templates and 
STRINGs. For example, you cannot add together two group level totals to create a third total. This type of calculation 
requires manual tracking of group breaks. 
In general, you place a total column in a page or group FOOTER so it can total the rows from the beginning of the report, 
from the beginning of the page, or from the beginning of the BREAK group. However, you can also place a total column in 
a DETAIL structure to provide a running total. A tally (CNT) column in the DETAIL can number the rows as they appear on 
the report. 
To specify a total column 
1. Place a variable string control as described in Specifying Columns to Print. 
For example, if you want total sales from an order entry system, select the data dictionary column containing the sales 
value. 
2. 
CLICK on the string control to select the string‘s Properties Pad dialog. 
3. Choose a total type from the TotalType property drop-down list. Choose from Sum, Average, Minimum, 
Maximum, Count, and Page No. 
4. Optionally, use the Reset property drop-down list to reset the total to zero before each page or before each break. 
For example, if your report is page-based so you need a total for each page, select Page from the Reset property drop- 
down list. If you want totals per customer and you have defined a break on customer, select the customer break from the 
Reset property drop-down list. If you want a grand total, select <None> from the Reset property drop-down list. See 
Grand Totals below. 
5. Optionally, set the Tally property to specify when the calculation occurs. 
By default, the specified calculation (SUM, CNT, MAX, MIN, AVG) occurs each time a report DETAIL is printed. This is 
true even if the calculated column is not in the DETAIL band and even if the calculated column is not in the lowest level 
child row of a multi-level table relationship. 
In other words, use the Tally property list to limit the occurrence of the calculation to the printing of higher-level breaks. 
For example, in a report that prints a three level table relationship (Customer>Order>Item), where the column to total 
resides in the middle level (Order) and the report prints all three levels, select the OrderBreak in the Tally property list to 
increment the total each time the Order BREAK prints rather than each time the Item DETAIL prints. 
Don‘t choose the same break for both Reset and Tally. If you do, the result is always zero. 
6. Optionally, set the Using property entry to specify a variable to receive intermediate values for the SUM, AVE, 
CNT, MAX, or MIN operation. 
In effect, this gives you access to the Report Engine‘s totaling capabilities. You can use the specified variable within your 
own custom calculations in embedded source code. Please note the Report Engine only writes to the intermediate 
variable, it does not read or reuse the variable for subsequent calculations. Therefore, you cannot alter a total generated 
by the Report Engine; however, you can HIDE the column calculated by the report Engine and replace it with your own 
custom calculated column. 


---

IDE User's Guide 
178 
 
 
Sub-totals and Page Totals 
Sub-totals are created simply by placing a total column within a page or group footer, and resetting the total to zero at the 
beginning of each page or group. Use the Reset property drop-down list in the string‘s Properties Pad dialog to reset the 
total to zero before each new page or group. 
 
 
Grand Totals 
In effect, grand totals are simply sub-totals based on a break variable that never changes. 
To create a grand total for your report, add a group break on a variable that doesn‘t change throughout the report. Any 
other group breaks should be nested within this grand total group break. 
Next add a footer to the grand total group break. Finally, add the sub-total to the group footer as described above. Do not 
reset the total to zero, that is, select <None> from the Reset property drop-down list in the String Properties dialog. 
Alternatively, you can create a separate DETAIL to calculate the grand total: 
1. Add a new Detail band outside of any BREAK structures in the report. 
2. Place your grand total columns on the new Detail band. Be sure to set Reset property to <None> and specify the 
detail or break structures on which to tally the total in the Tally property. 
3. Suppress the Detail band from automatically printing: 
o 
On the bands Properties Pad dialog, name a field equate label as the detail structure's USE 
property attribute. 
o 
On the Procedure Properties for the Report, press the Report Properties button, then select 
the Detail Filters tab. Highlight the grand total Detail band then press the Properties button. 
Then, in the Filter entry, enter False to suppress automatic printing. 
4. Embed the following code to explicitly print your grand total detail band: 
Clarion Templates 
Before Print Preview 
ABC Templates 
 ReportManager Method Executable Code Section 
AskPreview()—Priority 1300 
PRINT(RPT:MyGrandTotalDetailBand) 
 
 
Row Totals 
Displaying a row total (or any other calculation) requires two steps: assigning a value to a variable, then displaying the 
variable value in a string control (see Specifying Columns to Print above). 
You can assign the value to the variable with embedded source code (see the Embedded Source Code topic) or with the 
Formula Editor (see the Formula Editor topic). 
Whether you use the Formula Editor or embedded source, the key point to know is that the assignment should be done 
just prior to the PRINT statement. This table shows which embed point to use for each alternative: 
 
Formula 
Before Print Detail 
 
Clarion Templates 
Before Printing Detail Section 
 
ABC Templates 
Process Manager Method Executable Code Section 
 
TakeRecord(),BYTE 
 
 
 


---

User's Guide and Lessons 
179
 
 
Page Numbers 
Controlling/Resetting Page Numbers 
Edit the properties of the group HEADERs, the DETAILs, and/or the group FOOTERs. There are several options 
available. The options are Page Before, Page After, With Next, With Prior, and New Page No. 
Displaying Page Numbers 
Use the ReportPageNumber template (see Control Templates in the core help Template Guide) or create your own page 
number control as follows: 
1. Select the STRING tool from the Controls Toolbox, then DRAG AND DROP in the page header or footer band. 
2. 
CLICK on the string control you just placed. 
This selects the target string’s Properties Pad dialog. In the Pad: 
3. Set the VariableString property to TRUE. 
4. In the Picture property entry, enter @pPage <<#p. 
This picture token suppresses leading zeroes and displays the page number following the word "Page." 
5. In the Use property entry, enter a field equate label to reference the string in source code. 
For example, enter ?PageCount. This need not reference a variable. The Report Engine generates its own variable to 
hold the page number. 
6. From the TotalType property drop-down list, choose Page No. 
 
 
Displaying Print Dates 
To place a "Date Printed" in a report 
Use the ReportDateStamp template or create your own date stamp control as follows: 
1. Select the STRING tool from the Controls Toolbox, then DRAG AND DROP in the page header or footer band. 
For a print date you generally use the page header or page footer. 
2. 
CLICK on the string control you just placed. 
This selects the target string’s Properties Pad dialog. In the Pad: 
3. In the Text property entry, enter a date picture (@d1, for example). 
4. In the Use property entry, enter a local variable called PrintDate. 
5. Press the Save and Close button to exit the Report Designer. 
6. In the Data / Tables Pad, create a LONG local variable called PrintDate to match the variable you entered. 
7. Press the Save and Close button to exit the Report Designer Editor, and return to the Application Tree. 
 
 
To assign a value of TODAY() to PrintDate: 
1. Select your target Report Procedure, and then press the Embeds button in the Application Tree. 
2. In the Embedded Source dialog, DOUBLE-CLICK the following embed point: 
Clarion Templates 
Procedure Setup 
ABC Templates 
WindowManager Method Executable Code Section 
 
Init() 
 
3. In the Select embed type dialog, DOUBLE-CLICK SOURCE. 


---

IDE User's Guide 
180 
 
 
 
4. In the Text Editor enter this code: 
PrintDate = TODAY() 
5. Press the Save and Close button and save your embedded source. 
 
 
 
 
Implementing Print Preview 
Generate a report procedure with the Report template or the Report Wizard (see Lesson 2: The power of the 
Application Wizard). In the report procedure‘s Procedure Properties dialog, press the Report Properties button, 
then check the Print Preview box in the Report Properties dialog. 
If you prefer to hand code your print preview process, see PREVIEW in the Language Reference for more 
information and examples. 
 
 
Printing Labels (Dynamically) 
This section shows only one technique for printing report labels. There is also a Label Wizard that we strongly 
recommend for you to use. 
Printing labels simply means printing a multi-column report so that the report rows and columns match up with the 
commercial label forms you use. 
In the real world, different users will have different label papers at different times, so ideally, the user should be 
able to specify the dimensions of the label paper at run-time, and the label report should fit the specified label 
paper. 
To print dynamically sized labels: 
o 
Add a Labels table to your data dictionary. 
o 
Create Browse and Update procedures for the Labels table. 
o 
Create a Label Report procedure. 
o 
Add the Label table to the Label Report Table Schematic. 
o 
Embed code to do the run-time resizing. 


---

User's Guide and Lessons 
181
 
 
Add a "Labels" Table to Your Data Dictionary 
The table may use whichever file system you prefer, and should contain the following columns. No keys are 
required, but using LabelType as a unique key provides alphabetic sorting and prevents duplicate entries. See: 
Adding Tables to the Dictionary and Adding or Modifying Columns. 
 
 
 
Name 
Type 
Length 
Initial Value 
LabelType 
String 
15 
PageWidth 
Decimal 
5,2 
PageHeight 
Decimal 
5,2 
LabelWidth 
Decimal 
5,2 
LabelHeight 
Decimal 
5,2 
TopMargin 
Decimal 
5,2 
LeftMargin 
Decimal 
5,2 
FontSize 
Byte 
11 
 
 
Create a Browse and an Update Form for the Label Table 
The fastest way to build these procedures is to use the Procedure Wizard. 
3. From the Application Tree, press the INSERT key, or press the New Procedure button. 
4. In the New Procedure dialog, enter a name (BrowseLabels) then press OK. 
5. In the Select Procedure Type dialog, select the Browse Wizard in the Wizards tab. 
6. Answer the Wizard‘s questions: 
Choose the Labels table. Do allow the user to update rows. Do provide a "Select" button. The Wizard builds both 
procedures, then opens the Procedure Properties dialog for the Browse procedure. 
5. Press the Save and Close button to exit the Procedure Properties dialog. 
 
 
Create a Label Report Procedure 
Your report should observe these conventions. The report columns should have Height and Width of Default and 
there should be only one column per line. Thus if you need to display FirstName and LastName on the same line, 
you should concatenate these columns into a single column. 
6. 
Create a report for your address table (meaning the table that contains the addresses you wish to use). 
Use the Report Wizard if you want, but don‘t worry about formatting yet. Just make sure the report contains all the 
name and address columns you need for your labels. 
Call the label report as you would any other report. 
2. From the Application Tree, select your report procedure and press the Report button to enter the Report 
Designer. 
3. Delete all report sections, except the Detail section. 


---

IDE User's Guide 
182 
 
 
 
CLICK on the section‘s caption bar then press DELETE. 
4. For report lines with more than one column, concatenate the columns and remove trailing spaces. 
This step improves the appearance of your labels by removing unnecessary spaces. This step is also required to 
support the embedded code recommended below. 
Follow the steps described in the How to CLIP and Concatenate Name Columns of the How Do I...? topic in the 
online help. 
5. Set the properties for each report column. 
 
 
Use the Property Toolbar to identify the columns. 
Arrange your name and address columns in a vertical format, that is, one column below another, starting at the 
top left corner of the Detail band. Use the Alignment tools for precise alignment. See Specifying Columns to Print 
above. 
Remember to set the Height and Width properties of each column to Default. 
Your report should look similar to the illustration. 
 
 
 
 
6. Specify a field equate label (USE attribute) for the Detail section. 
CLICK on the detail then type ?detail in the Property Toolbar Use entry. 
7. Press the Save and Close button to exit the Report Designer and save your changes. 
 
 
Add the Label Table to the Report Table Schematic 
This step ensures that the report procedure opens the Label table and therefore has access to the Label table‘s 
row buffer. The embedded code below uses the position and size values in this row buffer to assign run-time 
positions and sizes to the label report. 
8. 
From the Application Tree, select your label report procedure, and then select the Data / Tables Pad. 
9. 
From the Data / Tables Pad, select Other Tables, and press the Add button. 
10. 
From the Select a Table dialog, DOUBLE-CLICK or select Labels. 


---

User's Guide and Lessons 
183
 
 
Embed Run-time Resizing Code 
Now we will embed code at three points in the report procedure: 
o 
Beginning of Procedure—call the BrowseLabels procedure to allow the user to specify the label paper to 
use. 
o 
After Opening Report—call the ResizeTheReport routine to assign the label sizes specified by the user. 
o 
Procedure Routines—the ResizeTheReport routine. 
 
3. 
From the Application Tree, RIGHT-CLICK your label report procedure then choose Embeds from the popup menu. 
4. 
From the Embedded Source dialog, DOUBLE-CLICK on the following embed point: 
 
 
Clarion Templates 
Beginning of Procedure, After Opening Files 
 
ABC Templates 
WindowManager Method Executable Code Section 
 
Init()—Priority 7800 
 
 
o From the Select Embed Type dialog, DOUBLE-CLICK SOURCE and enter the following statements: 
 
!Allow Run-time Specification of Label Paper 
GlobalRequest = SelectRecord 
!enable select button 
BrowseLabels 
!call BrowseLabels procedure 
 
 
3. Exit the Text Editor and save your changes. 
4. From the Embedded Source dialog, DOUBLE-CLICK on the following embed point: 
 
 
Clarion Templates 
After Opening Report 
 
ABC Templates 
WindowManager Method Executable Code Section 
 
Open()—Priority 7800 
 
 
6. From the Select Embed Type dialog, DOUBLE-CLICK SOURCE and enter the following statements. 
DO ResizeTheReport 
7. Exit the Text Editor and save your changes. 
8. From the Embedded Source dialog, DOUBLE-CLICK the Procedure Routines embed point (ABC and Clarion 
Templates). 
9. From the Select Embed Type dialog, DOUBLE-CLICK SOURCE and enter the following statements. 


---

IDE User's Guide 
184 
 
 
 
If you specified a label for your REPORT structure, change the report labels below to match your label. 
 
 
ResizeTheReport ROUTINE 
!!============================================================= 
!! Modify the report to fit specified label paper. 
!! Assumes Report Measurement Unit is 1/1000 of an inch. 
!!============================================================= 
 
 
SETTARGET(report) !Make report the target for property assignments 
 
 
!!=========================================================== 
!! Define the REPORT's AT attribute (ie detail print area). 
!! The detail print area should be the size of the entire page. 
report{PROP:Width} = LAB:PageWidth * 1000 
report{PROP:Height} = LAB:PageHeight * 1000 
!! Adjust the margins to center the address text within each label. 
report{PROP:Xpos} 
= LAB:LeftMargin * 1000 
report{PROP:Ypos} 
= LAB:TopMargin * 1000 
 
 
!!=========================================================== 
!! Define the DETAIL's AT attribute. 
!! The DETAIL should be the size of each individual label. 
?detail{PROP:Width} = LAB:LabelWidth * 1000 
?detail{PROP:Height} = LAB:LabelHeight * 1000 
 
 
!!=========================================================== 
!! Adjust font size and vertical position of the report columns. 
LOOP Fld#=FIRSTFIELD() TO LASTFIELD() 
!Process all report columns 
Fld#{PROP:Fontsize} = LAB:FontSize 
!Set font size 
IF Fld# > FIRSTFIELD() 
!Skip the first column, 
Fld#{PROP:Ypos}=BottomOfPreviousColumn# ! reposition the rest 
END 
BottomOfPreviousColumn#=Fld#{PROP:Ypos}+(16*LAB:FontSize) 
END 
## SETTARGET()
!Reset default target to the active window. 
## EXIT
!Exit the ROUTINE. 
 
That‘s it! Make and run your application. When you run your label report, you will have the opportunity to input the 
dimensions of your various label papers. The dimensions are stored in the Label table where they are available 
for your selection or modification each time you print labels. 


---

User's Guide and Lessons 
185
 
 
Printing One Row per Page 
To print a separate page for each row, check the PAGEAFTER box in the Detail Properties dialog. See Report 
Structures and Properties—Detail. 
 
 
Printing Mail-Merge Documents 
For a mail merge document, you usually place the name and address columns in the HEADER, and then reserve 
the DETAIL for a multi-line text control. See Page Header above. See Printing Multi-Line Text below. 
 
 
Printing Graphics 
Graphic controls embellish the report and guide the reader‘s eye to the data. The following controls allow you to 
add pictures, lines, and shapes to your report. See the Controls and Their Properties section for more information 
on the following controls. 
Image 
Most likely you will wish to place an image, such as a logo, in a HEADER. You may choose any of the graphic 
table formats supported for window controls; however, printing large images, especially .JPG files may present 
problems for some printers. 
The most important consideration when placing an image is its size—Clarion automatically resizes the image to fit 
the control size. This may introduce distortion. WMF files distort the least, however, the simplest way to prevent 
distortion is to preserve the height to width ratio of your images. 
To size a 640 x 480 pixel graphic, for example, determine its height-to-width ratio, which is 4:3. Plan an image box 
in the same ratio—for example, 2000 x 1500 thousandths, which represents a 2-inch by 1.5-inch box on the page. 
 
 
Whenever possible, use vector graphics such as the Windows Metafile Format (*.WMF). When you need to shrink 
or stretch them, their appearance is less subject to distortion than a bitmap. 
 
 
To place an IMAGE control in your report: 
1. Select the IMAGE control from the Controls toolbox, and DRAG and DROP to the band where you want to place 
the control. 
The Report Designer places an IMAGE control in the report structure. The center of the crosshair positions the 
upper left corner of the control. 
2. 
CLICK the control you just placed. 
This selects the Image‘s Properties Pad dialog. 
3. In the File property entry, enter the fully qualified image file name, or press the ellipsis (...) button to select the file 
from the Windows file dialog. 
Clarion automatically links the image file into the executable when the file is explicitly named in the control, so you 
don‘t have to ship the image file separately. 
4. In the Use property entry, enter a field equate label to refer to the image control in source code. 
5. Enter the correct image size in the fixed Width and Height property entries. 
6. Set the ImageMode drop list property to designate how the image will be displayed within the container control. 
You may also resize the image by clicking and dragging its handles. 


---

IDE User's Guide 
186 
 
 
Line 
Lines are the simplest means of visually separating sections or columns within your report. To place a line: 
1. Select the LINE tool from the Controls toolbox, and DRAG and DROP to the band where you want to place 
the control. 
The center of the crosshair positions the left end point. The Report Designer places a LINE control in the report 
structure. Relocate and resize the line by dragging its handles. 
2. 
CLICK the control you just placed. 
This selects the line‘s Properties Pad dialog. 
3. In the Use property entry, enter a field equate label to refer to the line control in source code. 
4. To specify a horizontal line, be sure to set the Fixed property to TRUE in the Height group, and enter a 
zero (0) in the box next to it. The height is the measure of the vertical distance between the origin and the 
end point; for a horizontal line, this is equal to zero. In the Width property, enter the length of the line in 
the Fixed property. 
5. To specify a vertical line, set the Fixed property to TRUE in the Width group, and enter a zero (0) in the 
box next to it. The width is the measure of the horizontal distance between the origin and the end point; 
for a vertical line, this is equal to zero. In the Height group, type the length of the line in the Fixed 
property. 
To specify a horizontal or vertical line the full width or height of the section, setthe Full property to TRUE. 
 
 
To create a horizontal divider line useful for splitting a HEADER from the DETAIL section, for example, check Full 
Width, and set the Fixed Height to zero. 
6. To specify a line color, set the LineColor property, and then choose a color from the Color dialog. 
 
 
Box 
You can highlight a report column by placing a gray box underneath it. You can frame an entire area of a report 
by placing a box with no fill around it. 
When overlapping one control over another, choose Report Designer  Format  Order  Bring to Front to 
ensure the underlying control is printed before the overlying control; otherwise the overlying control may be 
obscured. 
 
 
To place a box: 
1. Select the BOX tool from the Controls Toolbox, and DRAG and DROP to the band where you want to place 
the control. 
The center of the crosshair positions the upper left corner of the box. When you click, the Report Designer places 
a BOX control in the report structure. Resize and relocate the box by dragging its handles or its interior. 
2. Select the box you just placed. This opens the Box Properties Pad dialog. 
3. In the Use property entry, enter a field equate label to refer to the control in source code. 
4. Set the COLOR property attributes. 
If you want a solid box filled with color, enter a valid color equate in the check FillColor property or press the 
ellipsis (...) button to choose a color from the Fill Color dialog. 


---

User's Guide and Lessons 
187
 
 
If you want a colored border, enter a valid color equate in the check BorderColor property or press the ellipsis 
(...) button to choose a color from the Border Color dialog. 
5. If you want rounded corners for the box, set the Round box property to TRUE. 
6. Enter the measurements you wish in the target Width and Height properties (AT). 
To create a border or ‗frame‘ around the whole report, place a box in the Form band. Be sure the FORM is the full 
size of the page. Create a box with a border but no fill, and set the width and height to Full. 
 
 
Ellipse 
When placing an ELLIPSE in a report, follow the same procedures as for placing a box. 
 
 
Printing Multi-line Text with Word-wrap 
A multi-line text control can print a long string (such as a MEMO), automatically word-wrapping and printing as 
many lines as the MEMO‘s contents requires. 
1. Select the TEXT tool from the Controls Toolbox, and DRAG and DROP to the band where you want to place 
the control. 
The center of the crosshair positions the upper left corner of the control. 
The Report Designer places a TEXT control in the report structure. Resize the text box by using the mouse to 
drag its handles. 
2. 
CLICK the text control and choose Properties from the popup menu to open the Properties Pad for the 
Text coontrol. 
3. Enter the name of the variable in the Use property. 
4. Set the Resize property to TRUE. 
5. You can optionally display Rich Text Format content by setting the RTF property to TRUE 
(UseRichTextFormat). 
At run-time, the text expands downward, expanding the detail if necessary, to contain the entire text of the memo! 
If necessary, the text flows onto the following page. The RESIZE attribute only adjusts the height of the TEXT and 
the DETAIL. 
 
 
Reports That Look Like Windows 
The Report Designer gives you the ability to print on the page virtually anything you can put on the screen. This 
includes specialized controls such as list boxes, check boxes, group boxes, radio buttons, etc. 
In most cases, setting control properties for a report is identical to setting control properties for a window. See the 
Controls and Their Properties topic for more information on each of the following controls. 


---

IDE User's Guide 
188 
 
 
Option Box 
You may print an OPTION structure within your report. This appears on the page exactly as it does on screen—as 
an option box. You place an option structure on the page only to hold radio buttons. You may hide the box 
structure so that only the buttons print on the page. 
1. Select the OPTION tool from the Controls toolbox, and DRAG and DROP to the band where you want to 
place the control. 
The center of the crosshair positions the upper left corner of the box. The Report Designer places an OPTION 
structure within the report structure. Resize and relocate the option box by dragging its handles or its interior. 
2. Select the option box you just placed. This selects the Options Properties Pad. 
3. In the Text property entry, enter a caption for the option box. 
If you choose not to hide the option box when printing, the caption appears at the upper left border of the box, just 
as it does on screen. 
4. In the Use property entry, enter a field equate label to refer to the control in source code. 
5. Set the Boxed property to FALSE to hide the box, but not the radio buttons. 
You must add each radio button separately, placing them in the OPTION box. 
 
Radio Button 
Placing RADIO buttons in a printed report provides a visual aid to the user by showing the selected value as well 
as all the possible values for the column. 
Before you place the radio buttons in the report, you must first place an OPTION structure, by using the Controls 
 Option Box command. The RADIO button must be placed inside the option box representing the OPTION 
structure. If you attempt to place a radio button without an OPTION structure, the Development Environment 
displays an error message. 
1. Place an OPTION box as described above. 
2. Select the RADIO tool from the Controls Toolbox, and DRAG and DROP to the band where you want to place 
the control. 
The center of the crosshair positions the upper left corner of the radio button. The Report Designer places an 
RADIO control within the OPTION structure. 
3. Select the radio button you just placed. This selects the Radio Button Properties Pad. 
4. In the Text property entry, enter a caption for the radio button. 
The caption appears beside the radio button, just as it does on screen. 
5. In the Use property entry, enter a field equate label to refer to the control in source code. 
The radio button automatically turns ‗on‘ or ‗off‘ according to the value of the variable specified in the OPTION 
box‘s USE attribute. 
 
 
Check Box 
The check box (CHECK control) provides an attractive way to display a yes/no choice for a column—the 
alternative might be an entire column that repeats "one," "yes," or even ".T." for each row. 
The printed check box looks similar to an on screen check box. To place the check box: 
1. Select the CHECK tool from the Controls Toolbox, and DRAG and DROP to the band where you want to place 
the control. 
The center of the crosshair positions the upper left corner of the check box. 
2. Select the CHECK control. This selects the Check Box Properties Pad dialog. 


---

User's Guide and Lessons 
189
 
 
3. In the Text property entry, enter a caption for the check box. 
The caption appears beside the check box, just as it does on screen. You may make this text appear to the left or 
right of the checkbox by using the justification settings. 
 
 
Group Box 
The primary reason for placing a group box in a report is to make a group of controls on paper resemble their 
appearance on screen. 
To place the GROUP control: 
1. Select the GROUP tool from the Controls toolbox, and DRAG and DROP to the band where you want to place 
the control. 
The center of the crosshair positions the upper left corner of the group box. The Report Designer places a 
GROUP structure within the report structure. 
2. Select the control, or RIGHT-CLICK the control and choose Properties from the popup menu. This opens 
the Group Properties Pad dialog. 
3. In the Text property entry, enter a caption for the group box. 
This appears at the upper left border of the group box when the report prints, provided you set the Boxed 
property to TRUE. 
4. In the Use property entry, enter a field equate label to refer to the control in source code. 
Clear the Boxed box to hide the box, but not the internal controls. 
5. Add additional controls to the group as needed. 
 
 
List Box 
When the data you require for the report exists in a QUEUE, you may place a list box in the report. The list box 
that appears on the page is similar to the LIST control that appears on screen, though it will obviously not have 
the same functionality—the printed page does not support scroll bars, for example. 
Because a queue is required for a list box, and because Clarion‘s report template does not normally use a queue, 
several embedded source statements must be added to a template generated report procedure in order to use a 
list box. Alternatively, you may hand code the report procedure or use a report template that uses a queue. 
At print time, the first time the code cycles through the report, it prints the LIST‘s header and the first item in the 
queue. Each additional cycle prints the next item of the queue without repeating the header. The LIST‘s header is 
automatically repeated for applicable page breaks and group breaks. 
To place a list box in your template generated report: 
1. Select the LIST tool from the Controls Toolbox, and DRAG and DROP to the band where you want to place 
the control. The center of the crosshair positions the upper left corner. 
Each listbox item prints as a "selected" item with the specified selected item colors. The default Windows colors 
for a selected item are "reverse video" (white-on-black). To produce normal black-on-white printing, use the List 
Box Formatter to set the Selected Text for each column to COLOR:Black and the Selected Background to 
COLOR:White. 
2. Make the list box one (1) row high (about .220 inches). 
3. Drag the bottom handle until only the list box headings are visible. This eliminates empty space between 
rows. 
4. Make the detail band the same height as the list box. 


---

IDE User's Guide 
190 
 
 
Drag the list box to the top of the band or set its Y property coordinate to zero (0), then drag the bottom handle of 
the band to the bottom of the list box. This eliminates empty space between rows. 
5. Select the list box to open the List Properties Pad. 
6. In the Use property entry, enter a field equate label to refer to the control in source code. 
7. In the From property entry, enter the label of the queue the list box displays. 
 
 
Embeds Required for the List Box Processing: 
Generally speaking, the embedded source statements need to do two things: declare the QUEUE and load the 
queue buffer with data. 
1. Declare a QUEUE in the following embed point: 
 
 
Clarion Templates: 
Data Section, Before Report Declaration 
ABC Templates: 
Data Section, Before Report Declaration 
 
CustomerView VIEW(Customer) !Template generated view 
PROJECT(CUST:Name) 
PROJECT(CUST:Phone) 
PROJECT(CUST:Zip) 
END 
 
 
CusQ 
## QUEUE,PRE
!embedded QUEUE declaration 
Name 
 LIKE(CUST:Name) 
State 
LIKE(CUST:Phone) 
ZIP 
LIKE(CUST:Zip) 
END 
 
 
2. Load the queue in the following embed point: 
 
 
Clarion Templates 
Before Printing Detail Section 
 
ABC Templates 
ProcessManager Method Executable Code Section 
Next(BYTE ProcessRecords=True),BYTE 
Priority 7500 
 
 
CusQ.Name = CUST:Name 
!copy VIEW buffer to QUEUE buffer 
CusQ.Phone = CUST:Phone 
CusQ.Zip = CUST:Zip 


---

User's Guide and Lessons 
191
 
 
 
Lesson 10 - Procedure Basics 
This lesson explores the fundamental properties common to all procedures. 
 
 
Setting Procedure Properties 
After you choose the procedure type, you can define the procedure‘s properties—these properties include: 
 
 
• 
a description of the procedure 
• 
the procedure prototype 
• 
the module containing the generated source code 
• 
whether to export the procedure 
• 
whether to declare the procedure globally 
• 
parameters passed to the procedureT 
• 
return values from the procedureT 
• 
INI file settings used by the procedureT 
• 
tables accessed by the procedure 
• 
the WINDOW displayed by the procedure, including its size, shape, appearance and functionality 
• 
the REPORT generated by the procedure 
• 
data items (columns and variables) used by the procedure 
• 
procedures called by the procedure 
• 
custom source code embedded within the procedure 
• 
formulas used by the procedure 
• 
template generated extensions to the procedure 
 
 
These prompts are provided by the Procedure templates, therefore their presence or absence depends on the particular 
template that generates the procedure. 
You need not define every property for every procedure. In many cases, the default property definition is appropriate. 
When a default property is already established, a special icon appears beside its command button in the Application Tree. 
For example, the Browse procedure template contains a predefined window; therefore, an icon appears next to the 
Window button for procedures with this template. 


---

IDE User's Guide 
192 
 
 
 
 
For the properties you do define, you may use a Wizard and you may use the Procedure Properties dialog and its 
subordinate dialogs and Designers to set them. This section is primarily concerned with the Procedure Properties 
dialogs (see Lesson 2 for more information on Procedure Wizards). 
 
 
Application Generator Properties (Prompts) 
The properties discussed in this section are common to all Procedure Properties dialogs because they are managed by 
the Application Generator. You define these properties by completing the entry boxes and using the command buttons on 
the Application Tree. 
 
 
Template Properties (Prompts) 
In addition to the Application Generator properties, the Procedure Properties dialog displays and manages the template 
prompts for the templates in the procedure. 
 
 
To set the procedure properties 
From the Application Tree, select a procedure then press the Properties button to access the Procedure Properties 
dialog. Alternatively, DOUBLE-CLICK on the procedure, or RIGHT-CLICK the procedure, then choose Properties from the 
popup menu. 
This opens the Procedure Properties dialog, which displays the following prompts. 


---

User's Guide and Lessons 
193
 
 
 
 
 
 
Procedure Name 
The Procedure Name is displayed here. Press the ellipsis button to change the name if desired. You will be prompted for 
a New Procedure Name, and the ability to Accept or Discard your changes. 
 
 
Template 
The base template type used by this procedure is displayed here. You can change the template type by pressing the 
ellipsis button to the right. The Select Procedure Type dialog is displayed for a new selection if needed. 
 
 
Changing procedure template types can result in "orphaned" embed code. Be careful when using this function. 
 
 
Description 
A short text description for the procedure, which appears next to the procedure name in the Application Tree dialog. 
Press the ellipsis (...) button or the ALT + F2 key to edit a longer (up to 1000 characters) description. 
 
Category 
A category is used to help you group procedures together when the Category Tree Mode is active. 
 
 


---

IDE User's Guide 
194 
 
 
Module Name 
Specify which module (.CLW) file contains the source code for the procedure by selecting from the drop-down list. By 
default, the Application Generator names modules by taking the first five characters of the .APP file name, then adding a 
three digit number for each module. You may specify your own module names by choosing Application  Insert Module 
from the IDE menu. 
 
 
Prototype 
Optionally specify a custom procedure prototype which the Application Generator places in the MAP section. If you 
specify nothing, the Application Generator provides the correct prototype for the selected procedure template. See the 
Procedure Prototyping in the Language Reference and Prototyping and Parameter Passing below for more information. 
For example: 
 
 
(SHORT ID,STRING Name) 
 
 
Declare Globally 
Check this box to generate the procedure‘s prototype into the PROGRAM‘s MAP, rather than the MODULE‘s MAP. This 
makes the procedure callable from any other procedure, but it also forces a recompile of all program modules whenever 
you change the prototype. 
 
 
Export procedure 
Visible when the Application‘s Destination Type is set to DLL. Check this box to add the procedure to the application‘s 
automatically generated export (.EXP) file, so the procedure can be called by other executables. See Module Definition 
Files in the core help and Development and Deployment Strategies for more information. This prompt is only available 
when you specify Dynamic Link Library (.DLL) or Static Link Library (.LIB) as the Destination Type in the Application 
Properties dialog. 
 
 
Procedure Tables 
By default, table data (data maintained by your application) are available to any procedure within the entire application; 
however, you must tell the Application Generator which tables are used by the procedure so it can provide source code 
for reading (and writing) the tables. 
 
 
From the IDE Menu, select View  Data / Tables Pad. 
or 
Press the F12 Key 
 
 
This opens the Data / Tables Pad dialog. 
To add a table to the table schematic, select a control template <To Do> item, a control template file, or OTHER 
TABLES, and then press the Add button. Next, choose a table from the Select a Table dialog. 
When you select a <To Do> item for the control template, you add a "primary" table from among all the tables in your data 
dictionary. When you select an existing control template table, you add a "secondary" or "child" table from a list of related 
tables only. Clarion‘s templates automatically generate all the code needed to open, read, and close both the primary and 
any secondary tables. The templates also generate any code needed to update the primary table. 
Select OTHER TABLES when you want to access a table that is already open and positioned to the appropriate record, or 
when you want to hand code the table access. The templates automatically generate code to open (if not already open) 
and close OTHER TABLES , but any other processing is up to you. 


---

User's Guide and Lessons 
195
 
 
To delete an item from the table schematic, highlight it and press the Delete button. 
 
 
Sorting 
To specify the sort sequence of a table, select it in the Tables list, then press the Change button. Choose a key from the 
Change Access Key dialog. 
 
 
Views and Joins 
To specify an "inner join" or a custom join instead of the default "left outer join" for the generated JOIN structure, select 
the secondary (child) table, then press the Change button to open the Table Relationship dialog. 
 
 
Dictionary 
Choose this to generate a VIEW that reflects the table relationship as defined in the Data Dictionary. For example: 
 
 
 
 
 
 
 
 
 
 
 
Custom 
 
VIEW(Customer) 
PROJECT(CUS:LastName) 
PROJECT(CUS:FirstName) 
## PROJECT(CUS:ID)
JOIN(PH:CustomerIDKey,CUS:ID) !default JOIN 
END 
END 
Choose this to enter a custom JOIN expression for the generated VIEW. See JOIN in the Language Reference 
topic for more information. For example: 
 
 
 
 
 
 
 
 
 
 
 
Inner 
 
VIEW(Customer) 
PROJECT(CUS:LastName 
) 
PROJECT(CUS:FirstName 
## ) PROJECT(CUS:ID)
JOIN(Phone,‘PH:CustomerID,CUS:ID’) !custom JOIN 
END 
END 
Check this box so that only those primary table rows with related secondary table rows are retrieved. Inner joins 
are normally more efficient than outer joins. See INNER in the Language Reference for more information. For 
example: 
 
 
VIEW(Customer) 
PROJECT(CUS:LastName) 
PROJECT(CUS:FirstName) 
## PROJECT(CUS:ID)
JOIN(Phone,‘PH:CustomerID,CUS:ID’),INNER !custom inner JOIN 
END 
END 


---

IDE User's Guide 
196 
 
 
Procedure Windows 
To access any procedure‘s window: 
CLICK on the procedure, and press the Window button in the Application Tree dialog. 
or 
RIGHT-CLICK the procedure in the Application Tree, then choose Window from the popup menu. 
or 
In the Procedure Properties window, select the Window tab control to access the Window Editor and Designer. 
The Window Designer lets you visually design the size, shape, menus, controls and functionality for the window in this 
procedure. See the Window Designer lesson for details on how to define your window. 
In the Window Editor, the Edit as Text button allows you to edit the WINDOW or APPLICATION structure at the source 
code level. Clarion allows you to easily switch back and forth between editing the window graphically, and editing the 
source code that describes it. 
You may notice some non-language keywords such as #FREEZE, #ORIG, or #SEQ in this source code. Do not remove or 
change these keywords. The Application Generator uses them to manage source code generation, but does not include 
them in the generated source. The #LINK keyword ties an input control to its associated PROMPT control and can be 
safely deleted. 
 
 
Procedure Reports 
To access any procedure‘s report: 
CLICK on the procedure, and press the Report button in the Application Tree dialog. 
or 
RIGHT-CLICK the procedure in the Application Tree, then choose Report from the popup menu. 
or 
In the Procedure Properties window, select the Report tab control to access the Report Editor and Designer. 
The Report Designer lets you visually design the size, shape, content, layout, and functionality for the report in this 
procedure. See the Report Designer lesson for more information. 
The Edit as Text button in the Report Editor lets you edit the source code declaring the REPORT structure. You may 
notice some non-language keywords such as #LINK or #ORIG in this source code. Do not remove or change these 
keywords. The Application Generator uses them to manage source code generation, but does not include them in the 
generated source. 
 
 
Procedure Data 
Procedures may access several classes of data. These include table or column data, GLOBAL data, MODULE data, and 
LOCAL data. 
 
 
LOCAL data are defined in the data section of a procedure, and may only be accessed by the procedure that defines 
them. MODULE data are defined in the data section of a module. A module is simply a source file that may contain 
several procedures. Module data may be accessed by any procedures contained in the source file where the module data 
are defined. GLOBAL data may be accessed by any procedure in the entire application. See the Language Reference 
section on Data Declarations and Memory Allocation for more information. 


---

User's Guide and Lessons 
197
 
 
Accessing LOCAL Data 
In the Application Tree, select your target procedure. 
From the IDE Menu, select View  Data / Tables Pad. 
or 
Press the F12 Key 
This opens the Data / Tables Pad dialog. 
Local Data is displayed in this dialog. If any local variables already exist, they appear in the list. 
To define a new data item, press the Add button. 
This opens the Column Properties dialog. Type in the variable name, choose the variable type, and set any additional 
attributes, including screen attributes. See The Dictionary Editor—Adding or Modifying Columns for more information on 
this dialog. 
 
 
MODULE Data 
Defining Module data is exactly like defining Local data with one exception—you must select a module rather than a 
procedure in the Application Tree. To define MODULE data (memory variables available to several procedures in a single 
source file): 
 
 
1. From the Application Tree dialog, select the Module Tree Mode view. 
2. Highlight a module (folder), not a procedure. 
3. In the Data / Tables Pad, highlight Module Data and press the Add button. 
4. This opens the Column Properties dialog. This is the same dialog used to set column properties in the data 
dictionary. 
 
 
Unlike LOCAL data, MODULE data is not automatically cleared when a procedure closes. You, the developer, must 
take care to initialize the MODULE data as required by your various procedures. 


---

IDE User's Guide 
198 
 
 
Calls to Other Procedures 
Press the Calls tab in the Procedures Properties dialog to identify procedures called within embedded source code. 
Procedures may call other procedures. Procedure calls specified with template prompts are automatically added to the 
Application Tree; however, the Application Generator cannot "see" procedures called from embedded source code. 
Identifying these embedded procedure calls is important to project management and to source code generation. When 
you use the Calls tab to identify procedures called within embedded source code, the Application Generator can properly 
display the procedures within the Application Tree hierarchy, and the Application Generator can generate the appropriate 
local MAP structure for the source module. 
To identify procedures called from embedded source, press the Calls tab to open the Called Procedures dialog. This 
dialog lists all procedures in the application. Mark the called procedure by clicking on its name. 


---

User's Guide and Lessons 
199
 
 
 
Lesson 11 - Global Application Properties 
You can specify a number of settings that apply to your entire application, including table handling defaults, use of .INI 
files, global variables, template extensions, list box formats, keyboard redirection, control focus, visual styles, and 
embedded source code. These "global" settings are done primarily through the Application Properties tab and Actions 
dialog. 
 
 
 
Global Template Settings 
The prompts on the Global Properties tabs are provided by the Application Template. 
See Global Properties in the core help for a detailed description of each of these prompts. 
 
The tabs in the Application Editor (Embeds, and Extensions) are provided by the Application Generator, and are 
described in this section. 
 
 
Global Data and Variables 
Global data must be declared before the CODE statement in your PROGRAM module. There are several ways to 
accomplish this with the Clarion environment. You can declare global data in the data dictionary (see Dictionary Editor— 
File Properties); you can declare global data with the Data / Tables Pad; and you can declare global data with the 
Embeds tab in the Application Editor (embed data declarations in a data section embed point—see the Embedded 
Source Code topic). 
 
 
Data Dictionary global data 
Declares global data that can be shared by several applications. Because it is declared with the Column 
Properties dialog, you can specify controls and properties to apply to the data each time you populate them on 
your application‘s windows and reports. 


---

IDE User's Guide 
200 
 
 
Data / Tables Pad Global Data 
Declares global data for a single application. Because it is declared with the Column Properties dialog, you can 
specify controls and properties to apply to the data each time you populate them on your application‘s windows 
and reports. 
Application Editor Embeds tab 
Declares global data for a single application with free form source code. 
To access the Global Properties dialog, go to the Application Tree dialog and select the Properties tab. 
To add global variables, select the Global Data section and press the Add button in the Data / Tables Pad. 
 
 
To add a new variable to the list – Data / Tables Pad 
1. Select the Global Data section, and press the Add button. 
2. Fill in the Column Properties dialog. 
The Column Properties dialog is the same dialog used to add a column to the Data Dictionary. You can set all the 
characteristics of the variable, including the data type, length, label, etc. in this dialog. See Dictionary Editor— 
Adding or Modifying Columns. 
3. Press the OK button to close the Column Properties dialog. 
The Column Properties dialog appears. Press Cancel to stop adding new columns. 
 
 
To change the data type or label of a global variable 
1. Select the Data / Tables Pad, and highlight the variable in the Global Data section. 
2. Press the Change button. 
3. Make any changes necessary in the Edit Column Properties dialog then press OK. 
 
 
To reposition a global variable 
 
 
1. In the Data / Tables Pad, to move a variable up in the list, highlight it, and then drag it up or down as needed. 
 
 
Global Embed Points 
The global embed points are provided by the Application Template. See Global ABC Embed Points in the Template Guide 
for more information on these embed points. 
To access these embed points, press the Embeds tab in the Application Editor dialog. As with any embed point, you can 
write your own custom code, call a procedure, or use a code template. The Application Generator, when generating code, 
places your code or calls your procedure at the next source code line following the point you pick from the Embedded 
Source dialog. See the Embedded Source Code topic for more information on adding embedded source code to your 
application. 
 
 
Global Extensions 
The Global Extensions tab in the Application Editor lets you add Extension templates to your application. Extension 
templates generate a variety of task oriented source code statements at one or more preset locations as needed to 
accomplish the extension task. 
Templates that you may use in your application are listed. Refer to the Template Guide in the core help for a description 
of these templates. 


---

User's Guide and Lessons 
201
 
 
 
Lesson 12 - Advanced Features of the Application Generator 
This lesson summarizes more of the built-in template support and surrounding tools that are standard features of the 
Application Generator. 
Global Template Support 
In Lesson 11, the basic functions of the Application Generator‘s Global Properties were introduced. This section continues 
by exploring more of the Global standard features and options available for your applications. 
Each of the following options is discussed in more detail in the Global Properties help topic. This section is designed to 
give you a quick summary of the many features available. 
ABC Template Chain 
General 
Program Author 
Program Icon 
Use column description as MSG() when MSG() is blank 
Generate template globals and ABC‘s as EXTERNAL 
External Globals and ABC‘s Source Module 
Dynamic Link Library (DLL) 
Statically Linked Library (LIB) 
Generate EMBED Comments Non- 
Volatile Storage Settings 
Location (INI File or System Registry) 
INI File Options Registry Options 
INI File to use 
App Registry Key 
Other File Name 
Registry Root 
Disable Save/Restore Window Locations 
Preserve (Global Variables) 
Enable Run-Time Translation 
Enable Fuzzy Matching 
Fuzzy Matching Options 
Ignore Case 
Word Only 
 
App Settings 
Enable Window Frame Dragging 
Include Default XP Manifest 
Provide visual indicators on control with focus 
Set visual indicators 
Field Navigation 
Use ENTER key instead of TAB 
Exclude Controls 
Default Action (Enable/Disable/Runtime) 
Default Action (Runtime Only) 
Extended Browse Options 
Enable Auto size BrowseBox Columns 
Enable List Format Manager 
List Format Manager Configuration 
Enable Rebase 
Image Base Memory Address 
File Control 
Generate all file declarations 
Enclose RI code in transaction frame 
Seconds for RECOVER 
File Attributes 
Threaded (Use File Setting/All Threaded/None Threaded) 
Create (Use File Setting / Create All / Create None) 


---

IDE User's Guide 
202 
 
 
External (None External / All External) 
Declaring Module 
All files are declared in another .APP 
File Access 
File Open Mode ( Share / Open / Other ) 
Other Open Mode 
User Access ( Read/Write / Read Only / Write Only ) 
Other Access ( Deny None / Deny All / Deny Read / Deny Write / Any Access) 
Defer opening files until accessed 
Individual File Overrides 
Properties (Options similar to File Control tab) 
Global Objects 
Don‘t generate globals 
Error Manager 
INI File Manager Run- 
time Translator 
Fuzzy Matcher 
Classes 
Refresh Application Builder Class Information 
Application Builder Class Builder 
General 
Window Manager 
Image Manager 
Error Manager 
Popup Manager 
DOS File Lookup 
Resizer 
INI Manager 
Run-Time Translator 
Calendar Class 
Browser 
Browser 
File Loaded Drop Manager 
File Loaded Combo Manager 
FormVCR Manager 
EIP 
 
 
QBE 
Browse EIP Manager 
Template Interface 
Edit-in-Place Class 
 
QueryForm 
QueryForm Visual 
Query List 
Query List Visual 
Step Managers 
Abstract Step Base Class 
Long 
Real 
String 
Custom 
Locator Managers 
Step 
Entry 
Incremental 
Filtered 
Others 
Fuzzy Matcher 


---

User's Guide and Lessons 
203
 
 
 
Grid Manager 
Sidebar Manager (deprecated) 
Ascii Viewer 
Ascii Viewer 
Ascii Searcher 
Ascii Printer 
Ascii File Manager 
File Management 
File Manager 
View Manager 
Relation Manager 
Process and Reports 
Process 
Print Previewer 
Report Manager 
Report Target Selector 
Break Manager 
Toolbar Managers 
Toolbar Manager 
Toolbar List Box Manager 
Toolbar Relation Tree 
Toolbar Update Manager 
Toolbar FormVCR Manager 
ABC Library Files 
Override defaults 
Location of ABC Library 
External library base name 
Clarion Version 
Clarion Version 
Template Family 
Template Version 
ABC Version 


---

IDE User's Guide 
204 
 
 
Clarion Template Chain 
General 
Program Author 
Program Icon 
Use column description as MSG() when MSG() is blank 
Generate template global data as EXTERNAL 
Generate EMBED Comments 
INI File Settings 
Use .INI file to save and restore program settings 
.INI file to use 
Other File Name 
App Settings 
Enable Window Frame Dragging 
Include Default XP Manifest 
Provide visual indicators on control with focus 
Set visual indicators 
Field Navigation 
Use ENTER key instead of TAB 
Exclude Controls 
Default Action (Enable/Disable/Runtime) 
Default Action (Runtime Only) 
Report Preview Mode (ABC Class / Procedure) 
Default Report Procedure 
Extended Browse Options 
Enable Auto size BrowseBox Columns 
Enable List Format Manager 
List Format Manager Configuration 
Browse Active Invisible 
Enable Rebase 
Image Base Memory Address 
File Control 
Generate all file declarations 
When done with a File (Close the File / Keep the File Open) 
Enclose RI code in transaction frame 
Seconds for RECOVER 
File Attributes 
Threaded (Use File Setting/All Threaded/None Threaded) 
Create (Use File Setting / Create All / Create None) 
External (None External / All External) 
Declaring Module 
All files are declared in another .APP 
File Access 
File Open Mode ( Share / Open / Other ) 
Other Open Mode 
User Access ( Read/Write / Read Only / Write Only ) 
Other Access ( Deny None / Deny All / Deny Read / Deny Write / Any Access) 
Defer opening files until accessed 
Individual File Overrides 
Properties (Options similar to File Control tab) 
Classes  
Enable the use of ABC classes 
Refresh Application Builder Class Information 
Application Builder Class Builder 
ABC Library Files 
Override defaults 
Location of ABC Library 
External library base name 


---

User's Guide and Lessons 
205
 
 
 
Default Classes 
Edit in Place 
Browse EIP Manager 
Entry Class 
Text Class 
Check Class 
Spin Class 
DropList Class 
DropCombo Class 
Color Class 
File Class 
Font Class 
MultiSelect Class 
Calendar Class 
Lookup Class 
Other Class 
Reports  
Print Previewer 
Report Target Selector 
 
 
Clarion Version 
Clarion Version 
Calendar Class 
Calendar Class 
Template Family 
Template Version 
 
 
 


---

IDE User's Guide 
206 
 
 
Application Utilities 
The Application Generator has several useful utilities available to you. These utilities are template based, and available 
from within the Application Generator. 
Access the following utility templates by pressing the Template Utility button on the Application Generator‘s toolbar (or 
press CTRL + U). 
 
 
View ABC Classes 
The View ABC Classes Utility is better known as the Application Builder Class Viewer. Its purpose is to display all of the 
ABC Compliant Classes in a relational tree format. 
The rules for registering a class and to include it in the Viewer are found in the ABC Compliant Classes help topic. 
 
 
The following views are available: 
 
 
Class List 
An alphabetical list of Classes, and their Properties, Methods, and 
Implements. 
 
Class Hierarchy 
An alphabetical list of Classes, and other classes that inherit them. 
 
Interfaces 
An alphabetical list of Interfaces, and their methods and prototypes. 
 
Class Method List 
An alphabetical list of all methods, prototypes, and what class they 
belong to. 
 
Class Property List 
An alphabetical list of all properties, their declared data type, and class 
location. 
 
Class Files 
The full list of all ABC Compliant Class Files and their Classes, 
Interfaces and Public Procedures contained therein. 
 
 
WriteHLP 
The ListHLPIDs utility template searches through an active application and extracts all help IDs specified by any existing 
HLP attribute on a WINDOW or control. The output is generated to a designated text file. 
 
 
This tool is invaluable to any developer writing professional help for their applications. 
 
 
Dictionary Print 
This utility is used to document and print the contents of the active application‘s data dictionary.There are many options 
available, including: 
 
 
• 
Generate and keep the output text file, or delete it after printing. 
• 
Name your text file, and decide whether to print it right away. 
• 
Select all files, or any combination to document and print. 


---

User's Guide and Lessons 
207
 
 
 
• 
Control the level of detail for files, fields, keys, and relationships. 
 
 
More information can be found at the Dictionary Print Wizard core help topic. 
 
 
 
Application Import/Export 
The Clarion IDE provides several methods of importing and exporting selected parts of your application with other Clarion 
applications. In addition, the export feature is an excellent way of archiving or backing up your important work. It can also 
be used with your selected Version Control System. Each item can be found on the IDE Application menu. 
There are 4 types of import/export functions available. 
Import From Application 
This function allows you to import one or more procedures from another application file. Select the file from the Open File 
dialog. Then choose procedures to import from the Select Items to Import dialog. 
You can select an item by DOUBLE-CLICKING on it. A check mark appears to indicate the item is selected. Select 
additional items by DOUBLE-CLICKING. De-select an item by DOUBLE-CLICKING a previously selected item. Note: Both 
applications must use the same dictionary. 
Selective Export 
This function allows you to select individual procedures to export to an application text file. This feature is particularly 
useful when you need to transfer a procedure to another developer for sharing, and without having to send the entire 
application. 
Import Text 
Imports the procedures defined in a .TXA (text) file. These are the TXA files you can create by using the Selective Export 
or Export Text functions. 
Export Text 
Creates a .TXA (text) file from the current application. 


---

IDE User's Guide 
208 
 
 
 
Lesson 13 - Customizing the Application: Adding Templates 
In our previous lessons, we focused on the fundamentals of application design, and the templates and tools that support 
it. This lesson provides an overview of the additional templates available to you, with links and references to appropriate 
documentation. 
 
 
Procedure Templates 
In previous lessons, we learned that a procedure is a series of Clarion language statements (source code) that perform a 
task. A Procedure template is an interactive tool that (with the help of Clarion‘s IDE) requests information from you, the 
developer, and then generates a custom procedure for just the task you specify. A Procedure as stored in a Clarion 
application (.app) file is really a specification that the development environment uses to generate the procedure source 
code. The specification includes the Procedure template and your answers to its prompts, the WINDOW definition, the 
REPORT definition, other local data declarations, embedded source code, etc. 
Clarion provides a rich assortment of task oriented Procedure templates with which you can rapidly develop database 
applications. In Getting Started, the lesson introduces a few procedure templates; the Application Generator lessons in 
Learning Clarion introduces more. This chapter describes all the procedure templates and their prompts. 
Using Procedure Templates 
You use procedure templates by selecting the template based on the general task you want it to perform, such as 
browsing or searching data (Browse template), changing data (Form template) or reporting data (Report template). You 
select the template when you create the procedure (see Select Procedure Type in the core help for more information). 
Then you refine the template-generated code to fit your specific task by using the Procedure Properties dialog to answer 
template prompts and to access other development environment tools such as the Window Designer and the Report 
Designer. 
In the Select Procedure Type dialog, use the Defaults and Wizards tab selections for the majority of your new procedure 
designs. The Templates tab contains selections that provide a minimum starting point for all procedure templates, and is 
primarily useful for the basic Window, Source, and External procedure templates. 
 
 
Procedures as Containers 
Procedures can contain data structures such as WINDOW structures, REPORT structures, and the controls within those 
structures. And Procedure templates can contain other templates—Control and Extension templates that present 
additional opportunities to customize the procedure. 
 
 
Procedures Contain Controls 
Procedure templates provide standard prompts for any BUTTON, ENTRY, or CHECK controls you add to the procedure‘s 
WINDOW. You access these prompts through the Properties dialog for these controls. For each ENTRY control, for 
example, the procedure template provides prompts to let you use the ENTRY as a lookup field. For a CHECK box, the 
procedure template provides prompts to let you update variables and hide or unhide controls based on the state of the 
CHECK box. 
Procedure templates provide standard embed points for controls you add to the procedure‘s WINDOW. Generally, there is 
an embed point for each event the control generates. Embedding code into these embed points generates code that 
evecutes when the control generates the event. See ABC Template Embed Points for more information. 


---

User's Guide and Lessons 
209
 
 
Procedures Contain Other Templates 
Finally, Procedure templates can contain other templates—Control templates and Extensions templates which provide 
their own development environment prompts and embed points, and their own runtime functionality. 
Thus, a Procedure and its template act as a container which automatically provides support for many layers of 
functionality and customization. And the Application as stored in the development environment, acts as a container for the 
Procedures and their templates. 
Many of the ABC Procedure templates already contain Control templates. Control templates generate code to define and 
manage a specific control, including loading data in and out of the control. In fact, the unique set of Control templates 
within a Procedure template are what determine the template‘s primary purpose or task. For example, the Browse 
Procedure template is a generic Window Procedure template which contains the BrowseBox and BrowseUpdateButtons 
Control templates. 
 
 
Inter-Procedure Communication 
Clarion‘s template generated procedures use a simple system of global variables and EQUATEs to communicate with 
each other. 
The procedures use two global variables named GlobalRequest and GlobalResponse. The calling procedure uses 
GlobalRequest to tell the called procedure what database action to do. The called procedure uses the GlobalResponse 
variable to tell the calling procedure the result of the requested database action. 
Whenever a template-generated procedure calls another template-generated procedure, the calling procedure sets the 
value of GlobalRequest to one of the EQUATEs declared in ABFILE.EQU as follows: 
 
 
 
InsertRecord 
## EQUATE (1)
!Add a record to table 
ChangeRecord 
## EQUATE (2)
!Change the current record 
DeleteRecord 
## EQUATE (3)
!Delete the current record 
SelectRecord 
## EQUATE (4)
!Select the current record 
ProcessRecord 
## EQUATE (5)
!Process the current record 
ViewRecord 
## EQUATE (6)
!View the current record 
SaveRecord 
## EQUATE (7)
!Save the current record 
 
 
The called procedure checks the GlobalRequest variable and tries to carry out the requested action. The called procedure 
indicates success or failure by setting the value of GlobalResponse to one of the EQUATEs declared in ABFILE.INC: 
 
 
 
RequestCompleted 
## EQUATE (1)
!Update Completed 
RequestCancelled 
## EQUATE (2)
!Update Aborted 


---

IDE User's Guide 
210 
 
 
Summary of Standard Procedure Templates 
 
 
Extension Templates 
Extension templates add functionality to procedures, but are not bound to a control or a single embed point. Each 
Extension template has one well-defined task. For example, the DateTimeDisplay template lets you display the date, time, 
or both on a WINDOW. 
From a Procedure Properties dialog, add an Extension template by pressing the Extensions tab. 
 
 
Only Extension templates may be added and deleted using the Extensions tab. Control templates may be modified here, 
but may not be added or deleted. Use the Window Designer to add or delete Control templates. 
 
 
Control Templates 
A control is almost anything you see on a window or a report. For example, a check box, a push button, an entry field, and 
a list box are all controls. 
Control templates generate source code to declare controls and manage their associated data. For example, the 
BrowseBox Control template not only generates source code to declare a list box, it also generates code to load data into 
a QUEUE, then display the QUEUE in the list box with complete scrolling, searching, sorting, updating, and mouse-click 
selection capability. 
Control templates can also control file I/O; for example, the SaveButton Control template can warn that changes were 
made if the end user tries to close the window without saving the changes to disk. 
 
 
Generally, it is to your advantage to use a Control template rather than a simple control. 
 
 
Adding Control Templates 
When starting with a new procedure, to add a Control template: 
1. In the Window Designer or Report Designer, add a Control template by selecting the desired template in the 
Control Templates Pad, and DRAGing to the target window location. 
The Designer places one or more controls (the type of controls depend on the Control template) in the window or 
report. 
2. RIGHT-CLICK on the control, then choose Actions from the popup menu to access the Control template 
prompts. 
These prompts define and customize its functionality. 
3. Select the Properties Pad dialog to set the control‘s appearance, location, and other functionality. 
Once a Control template is added to a procedure, you can access the Control template prompts via the Extensions 
tab. 


---

User's Guide and Lessons 
211
 
 
Code Templates 
Code templates generate source code into an embed point that you specify, and sometimes into other embed points as 
well. Their purpose is to make procedure customization quick and easy. Each Code template has one well-defined task. 
For example, the Initiate Thread Code template simply starts a new execution thread, and no more. Typically, the Code 
template provides a dialog box with prompts and instructions. Add Code templates to your procedure with the Embedded 
Source dialog. 
 
 
Utility Templates 
In Lesson 2, we discussed the power of the Application Wizards, and how they can be used to quickly generate feature- 
rich procedures and whole applications. 
Wizards are actually categorized as a form of Utility template. By definition, a Utility template is a template that acts 
externally to an application on information read from the active dictionary or application itself. 
All utility templates generate an ASCII text-based file. The main difference between the Wizards and other Utility 
templates is that Wizards generate information that is read into an application file, where non-Wizard Utility templates 
read information out of an active dictionary or application for use with external utilities, documentation, or third-party 
products. 
 
 
Module Templates 
In Clarion terms, a module is defined as a source or library file used for a given project. In the Application Generator, there 
may be times when you need to include an external source module or library into your application design. The Module 
templates allow you to do this effortlessly within the Application Generator. 
To add a module to an existing application, choose Application  Insert Module from the Application Generator‘s Main 
Menu. 


---

IDE User's Guide 
212 
 
 
 
Lesson 14 - The Source Procedure 
Overview 
As you have seen in the previous lessons, templates can perform some amazing source code generation, greatly easing 
the programming that you have to do. 
Sometimes you have a process that is complex, unique, or both, and a template simply doesn‘t fit the requirements and 
specifications. Does this mean that you have to hand-code your entire project, and give up on the Application Generator? 
Absolutely not! The Source Procedure template is your solution. 
 
 
Source Template 
The Source Procedure template provides an elegant and simple way to add hand code to your application. It provides two 
points at which to embed your code: the data section, and the code section. 
The template simply declares the procedure, handles any optional parameters, places the embedded data declarations in 
the data section, begins the CODE section, then places any embedded executable code in the CODE section: 
 
 
(local data) 
## CODE
(your embedded code) 
 
 
Source Template Prompts 
In addition to the standard Application Generator command buttons and prompts (see Application Generator in the User‘s 
Guide), the Source template Procedure Properties dialog contains the following additional prompts: 
 
 
Parameters 
Specify the parameter list for your procedure. See PROCEDURE and Procedure Prototypes in the Language Reference 
and Prototyping and Parameter Passing in the User‘s Guide for more information. 
The parameter list is an optional list of datatypes and labels that appear on the generated PROCEDURE statement. The 
entire list is enclosed in parentheses. There must be a parameter in the parameter list for each parameter defined in the 
procedure 
prototype. We recommend providing the data type and the parameter label in both the parameter list and in the procedure 
prototype. For example: 
(SHORT Id,STRING Name) 
You should handle the parameters in the procedure‘s embedded source code. 


---

User's Guide and Lessons 
213
 
 
 
Lesson 15 - Customizing the Application: Source Embeds 
 
Adding Embedded Source to a Procedure 
• 
RIGHT-CLICK the procedure in the Application Tree, then choose Embeds from the popup menu (or press the 
Embeds button in the Application Tree) to open the Embedded Source dialog to embed source code using 
alphabetically or logically ordered named embed points. 
or 
• RIGHT-CLICK the procedure in the Application Tree, then choose Source from the popup menu to open the 
Embeditor to embed source code within the context of surrounding generated code. 
or 
• 
In the Procedure Properties, select the Embeds tab to open the Embeditor to embed source code within the 
context of surrounding generated code. 
or 
• RIGHT-CLICK on a control in the Window Designer, then choose Embeds from the popup menu to access the 
embed points for a single control. 
Clarion‘s templates let you add your own customized code to many predefined points inside the standard code that the 
templates generate. It‘s a very efficient way to achieve maximum code reusability and flexibility. The point at which your 
code is inserted is called an Embed Point. Embed points are available at all the standard events for the window, the 
window controls, and for many other logical positions within the generated code. The embed points are determined by the 
templates. You can even add your own embed points if needed. See #EMBED in the online Template Language help. 
Embedding source code in a procedure lets you fully customize the procedure. The Application Generator saves the 
embedded source in the .app file and integrates it into the template generated source code each time you generate 
source code. 
You can write your own embedded source code or use Code templates to generate the code for you. Once you embed 
source code in a procedure, the procedure is flagged with the 
 icon in the Application Tree. 
In order to effectively embed code, you should understand the surrounding template generated code. 
 
 
Several ways to Embed Source Code 
Clarion provides several powerful methods for embedding source code. There are advantages to each of these methods 
as noted below: 
• 
The Embeditor (choose Source from the popup menu) lets you see the embedded source code within the context 
of the surrounding generated code and gives you the full power of the Text Editor, including text search and 
replace, copy and paste, code completion,and the Data / Tables Pad. 
• 
The Embedded Source dialog (choose Embeds from the popup menu) lets you see only the embed points and 
their code, without the surrounding code. It gives you the full power of the Text Editor, plus a locator to find embed 
points, plus tools for moving and copying entire embed points with multiple blocks of embedded code, and for 
generating embedded code with Code templates. 
• 
The Embeds button for a control (choose Embeds from the Window Designer‘s popup menu) gives you the 
power of the Embedded Source dialog focused on the embed points for a single control. 
Source code embedded with the Embeditor is fully accessible with the Embedded Source dialog and vice versa, with the 
exception of Code templates, which are only modifiable with the Embedded Source dialog. 


---

IDE User's Guide 
214 
 
 
1. The Embeditor 
1. From the Application Tree, RIGHT-CLICK the procedure, then choose Source from the popup menu. 
The Embeditor generates a temporary source file with shading and optional comments to identify all the embed points for 
the selected procedure. You may insert source code into the embed points simply by typing the new source statements 
into the unshaded or white area. 
You may configure the Embeditor‘s temporary source file with the Application and Editor tabs of the Application Options 
dialog. Choose Setup    Application Options. See Configuring the Environment—Action for Legacy embeds and Editor. 
The Embeditor is the Text Editor opened in a special mode which allows you to not only edit all the embed points in your 
procedure, but to edit them within the context of template-generated code. The Embeditor displays all possible embed 
points for the procedure within the context of all the possible code that may be generated for the procedure. Notice the 
distinction here—Embeditor does not show you the code that will be generated, but all the code which could be 
generated, if you placed code into every available embed point. 
2. Press 
 to scroll to the next embed point. 
scrolls to the previous embed point; 
 scrolls to the next filled embed point; 
 scrolls to the previous filled embed 
point. 
3. Place the insertion point in the unshaded area, then type your source code. 
The full power of the Text Editor is at your disposal. See the Text Editor lesson for more information. 
The Embeditor automatically indents your source code at least as far as the embed point comments. You may indent 
farther (to the right), but you may not indent less (to the left). 
4. Press the Save and Close Button 
 to save your changes and Exit the Embeditor. 
The Embeditor automatically puts your source into the appropriate embed point and sets the priority for the embedded 
code. 
 
 
2. Embedded Source Dialog 
1. From the Application Tree, RIGHT-CLICK the procedure, then choose Embeds from the popup menu. 
This opens the Embedded Source dialog, providing access to all the embed points in the procedure. You can also get 
here from the Embeds button on the Procedure Properties window, but the popup menu is quicker. 
You may sort the embed points in alphabetical order or in logical order with the Application tab of the Application Options 
dialog. Choose Tools  Application Options from the menu. 
2. Filter the embed points by choosing from the View menu or by pressing buttons on the toolbar. Choose from: 
Text Buttons (not on toolbar): 
Insert 
Opens the Select Embed Type dialog, which allows you to add handwritten source code, call a procedure, and/or choose 
a code template. 
Properties 
Allows you to edit the embedded code. If it is hand written code, then the Text Editor appears. If it's a code template, the 
prompts dialog for the code template appears. 
Delete 
Allows you to delete embedded code you previously added. 


---

User's Guide and Lessons 
215
 
 
Move Up/Down 
Moves the embedded code item up or down another (modifying the Priority). Each executes in the order they appear at an 
embed point. 
Priority 
Sets the Priority for the embedded source. The Priority of each block within an embed point controls the execution 
sequence of the code relative to any other code in the same embed point. Lower priority numbers execute before higher 
priority numbers. 
Filled 
Press this button to call the Embeditor, allowing you to only show embed points that actually have had source code 
entered into them. 
Source 
Press this button to call the Embeditor, allowing you to see your embedded source in context. 
Expand All 
Fully expand the embeds list. 
Contract All 
Fully contract the embeds list. 
Expand Filled 
Expand only the filled embeds. 
 
Toolbar Buttons 
 
Show Filled Only 
Show only filled embeds. 
Show Priority Labels 
Show template generated embed point labels so you can precisely interleave your code with template generated code. 
 
Show Legacy Embeds 
Show Clarion 2.x embed points. 
You may set the default for legacy embed points with the Application tab of the Application Options dialog. Choose Setup 
  Application Options. See Configuring the Environment—Action for Legacy embeds. 
Show Window Embeds 
Available only when editing embeds for a control, this button allows you to expand the view to show embeds for the 
window. 
3. Locate an embed point by typing its name in the locator field near the top of the dialog, or by choosing from 
Navigate menu or by pressing buttons on the toolbar. Choose from: 
 
Previous Filled 
Scroll to the next filled embed point. 
Next Filled 
Scroll to the next filled embed point. 
To embed code associated with a specific control, open the Window Designer, RIGHT-CLICK the control and choose 
Embeds from the popup menu. Only those embed points associated with the selected control are listed. 
4. Select an embed point then press the Insert button. 


---

IDE User's Guide 
216 
 
 
This opens the Select Embed Type dialog. There are three ways to create the embedded source code: hand-coding with 
the text editor, calling another procedure, or embedding a Code template. 
You may combine one or more of these three methods at a single embed point—that is, a single embed point accepts 
multiple "blocks" of embedded code. You can control the execution sequence of each block of code relative to any other 
code in the embed point by setting its priority. Lower priority numbers execute before higher priority numbers. 
The Embedded Source dialog displays the embedded source in the order it generates and executes. 
 
 
3. Custom (hand-code) embedded source with the Text Editor 
1. Press the Insert button in the Embeds dialog. The Select Embed Type window is displayed. 
2. Select Source in the Select Embed Type dialog. 
3. Press the Select button to start the Text Editor with a blank source code window. 
This opens the Text Editor (see Text Editor for more information). The display includes access to the Data / Tables Pad 
from which you can select variable names and field names. Simply CLICK on an item in the toolbox and DRAG it to the 
window to insert its fully qualified name at the insertion point. 
4. Write your custom code in the source code window. 
 
 
Don‘t forget to use the on-line help for explanations and examples of Clarion Language syntax and techniques. Copy and 
paste directly from the help examples! 
5. Press the Save and Close button 
to close the Editor and save changes. 
6. Optionally set the Priority for the embedded source. 
The Priority of each block within an embed point controls the execution sequence of the code relative to any other code 
in the same embed point. Lower priority numbers execute before higher priority numbers. 
 
 
4. Call a Procedure 
1. Press the Insert button in the Embeds dialog. The Select Embed Type window is displayed. 
2. Select Call a Procedure in the Select Embed Type dialog. 
A dialog named for the embed point opens to accept the name of the procedure to call. 
3. In the Embed: Procedure Call dialog, type a name for the procedure or choose an existing procedure from the list. 
 
 


---

User's Guide and Lessons 
217
 
 
 
Typing a new name tells the Application Generator to add the procedure to the Application Tree as a "To Do" item. If 
another procedure with the same name already exists, the Application Generator generates code to call it. 
You define the functionality of the other procedure separately. See Defining Procedure Properties. 
4. Press the OK button to close the dialog. 
 
 
5. Use a Code template to generate the embedded code 
1. In the Select Embed Type dialog, select a Code template then press the Select button. 
Code templates are the items indented beneath the Class folders. See the Code Templates section in the online help 
for descriptions of the Code templates included with this package. 
This displays a Prompts for... dialog box. 
2. Read the instructions and explanations in the dialog. 
Each code template includes explanatory text on its proper use and how to fill in the necessary options. 
3. Fill in or choose from the options in the Prompts for... dialog. 
4. Press the OK button to close the dialog. 
 
 
 
 
Managing Embedded Source 
The Embedded Source dialog contains several tools that let you control the sequence in which embedded source is listed 
and executed. The Priority spin control and the 
 and 
 buttons change the order of one or more embedded source 
items; execution occurs in the order they are listed. 
There are also Delete and Properties buttons, plus standard Cut, Copy, and Paste buttons for maintenance. To Cut and 
Paste (or Copy and Paste) embedded source from one embed point to another: 
1. In the Embedded Source dialog, highlight a line in the tree diagram. 
Highlighting an embed point line (folder icon) selects all the embedded source at this embed point for subsequent cut and 
paste operations. Highlighting a single embed source item selects only that item. 
2. Press the 
 to cut, or press the 
 button to copy. 
3. Again, highlight a line in the tree diagram. 
4. Press the 
 button to paste. 
 
Copying Embedded Source Between Procedures 
Occasionally you will create two or more procedures that are very similar and that require lots of embedded source code. 
Rather than retype the embedded source in the similar procedures, you can copy the embedded source as follows: 
1. Develop and test the embedded code in your first procedure. 
2. Choose Application  Selective Export. 
3. Specify a .TXA file to receive the exported procedures, then press OK. 
4. Select all the similar procedures for export, then press OK. 
Selected procedures are identified with a check mark. 
5. With your favorite text editor, open the .TXA file and copy the embed definitions from the finished procedure to the 
other similar procedures, then save the .TXA file. 


---

IDE User's Guide 
218 
 
 
The embed definitions commence with the [EMBED] line. See the Advanced Programming Resources PDF for more 
information on TXA file format. 
6. In Clarion choose Application  Import Text. 
7. Specify the .TXA file, then press OK. 
The import replaces the procedures in the .APP with the procedures from the .TXA, with the embedded source code 
intact. 


---

User's Guide and Lessons 
219
 
 
 
Lesson 16 - SQL, ODBC and ADO application support 
The Clarion IDE provides powerful support for applications connecting to SQL, ODBC, and ADO based data sources, 
through an easy to use Dictionary Synchronizer, and Language and Template support. This lesson examines these areas, 
and gives you a summary of all of the tools available. 
Guidelines for selecting a driver 
To a new developer, selecting the right database driver to use in your applications can be a perplexing decision. Here are 
some general guidelines to follow: 
 
 
Getting Started 
Choosing a file system is an important decision, and we encourage you to gather as much information from as many good 
sources as you can to support your decision. Although the choice of file systems is important, with Clarion, it is not 
irrevocable. If the file system you choose does not live up to your expectations, you can change to one that does. For 
example, some developers use the TopSpeed file system for project development, then switch to an SQL file system 
during project implementation in order to postpone the expense of the SQL software and server hardware until late in the 
development cycle. 
 
 
ISAM Native Drivers 
AN ISAM (Indexed Sequential Access Method) file is best used with programs accessed by a single, or limited amount of 
users. It is normally stored on a local drive, or a network server if accessed by multiple users. In this configuration, the 
access time to read and write data is adequate. The cost of implementing this type of database is also minimal. However, 
as the number of users increases, and the size of the data stored grows, your access times to read and write your data 
may decrease, and an SQL based database should be considered. 
Native ISAM file types supported by Clarion: 
ASCII, BASIC, Btrieve, Clarion 2.1, Clipper, dbaseIII, dbaseIV, DOS (Binary), FoxPro 2.6, and TopSpeed. For more 
information, see the main help section on ISAM Database Drivers. 
 
 
SQL Native Drivers 
SQL is actually a declarative language that has become the standard query language for many database systems. 
Advantages are numerous, including more concurrent users, ability to access data from remote servers (sometimes on 
different platforms), numerous security and backup/restore features, and expanded query abilities. The disadvantages are 
cost and a learning curve with its configuration and language familiarization. However, with the rise applications deployed 
on the Internet, SQL databases‘ long term cost savings in development time and maintenance are significant. 
Native SQL file types supported by Clarion: 
Microsoft SQL, Oracle, Pervasive.SQL, and SQL Anywhere. For more information, see the main help section on Database 
Drivers. 
 
 
Application support of ISAM and SQL databases 
With both ISAM and SQL dictionary definitions, Clarion‘s Application Generator provides two basic template sets (Clarion 
and ABC) to use in your application design. 
Behind the scenes, the SQL drivers convert standard Clarion I/O statements and function calls into optimized SQL 
statements, which they send to the back end SQL servers for processing. 
Although both sets support the SQL drivers defined in the data dictionary, the ABC template chain offers extended options 
for SQL databases. 


---

IDE User's Guide 
220 
 
 
Global Support 
In the Global Properties Classes tab control, the Browser Class (the library that supports the retrieval of data rows to a 
selected list box) has additional configuration options that optimize database performance based on the file system you 
are using. 
See the Browser Class configuration topic for more information. 
SQL Advanced Support 
The ability to return a row of records from an SQL database is provided by the BrowseBox control template, and is 
included by default in all default Browse procedures. 
 
When an SQL driver is detected as the primary table used in the Browse Box, the template registry provides an 
additional SQL Advanced tab control. This control allows you to extend the optimized SQL statements generated by 
the template. For more detailed information, see the SQL Advanced Tab topic in the core help. 
 
 
Language Support 
Finally, don‘t forget the Application Generator‘s built-in template embeds that allow you to extend the functionality and 
performance of the basic template defaults. Each SQL driver (or accelerator) contains a number of Driver String and 
Properties that allow you to extend the SQL application beyond its default behavior. Refer to the core help and Database 
Drivers manual for a more detailed look at the rich support that is offered. 
 
 
The ODBC Driver 
A good rule of thumb is to always use a native driver if you have the opportunity to do so (namely, it is on the list of drivers 
provided by Clarion). But what do you do when your database it not on the list of drivers? 
First, check to see that the database vendor supplies an ODBC driver. Once you have installed the vendor‘s ODBC driver 
support, use the Clarion ODBC driver to attach to the data source. (See Lesson 7 in the Dictionary section to review how 
this is done). 
See the ODBC:Overview and other topics in the core help for a more detailed examination. 
Finally, ADO Support 
ADO (ActiveX Data Objects) is a relatively new interface for establishing a connection to virtually any database. Think of 
ADO as a higher layer of abstraction over the ODBC connectivity layer. They are objects used to connect to various data 
sources. Its primary benefits are ease of use, high speed, low memory overhead, and a small disk footprint. ADO supports 
key features for building client/server and Web-based applications. 
Again, like ODBC, your database vendor should provide you with the proper ADO libraries. When they are installed they 
will look like other ODBC data sources that are registered. 
The next step is to import the ADO data source into the Clarion dictionary. Although it is registered and accessed like all 
other drivers, keep in mind that the Clarion ADO "driver" is merely holding the connection string information that can be 
used by the ADO Connection Object in the Application Generator. The ADO "file structure" imported in the dictionary is 
present to satisfy some template requirements in the application generator and to assist you in your application design 
sessions. 
To access ADO data sources in your applications, a complete set of ADO support templates are shipped with Clarion. 
Here is a complete list of these templates: 


---

User's Guide and Lessons 
221
 
 
ADO Extension Templates 
 
ADOSupport 
A required global extension for all ADO based applications 
QcenterSupport 
Support to modify BrowseQBEList default expressions. 
ADORecordsetObject 
Support to access methods in RecordSet object 
ADOCommandObject 
Support to access methods in Command object 
AddADOFile 
Add an ADO file not associated directly with procedure 
ADOloginExtension 
Add support to create a Login procedure. 
ADO Procedure Templates 
ADOErrorsProc 
ADOLoginProc 
Browse 
Form 
Process 
Report 
ADO Control Templates 
ADOBrwLocator 
ADOErrList 
ADOLoginControl 
BrowseBox 
BrowseBoxSelectButton 
BrowseProcessButton 
BrowseQBEList 
BrowseUpdateButtons 
PauseProcessControl 
ProcessControl 
SaveButton 
 
 
ADO Code Templates 
ADOCommandExecute 
ADORecordsetGetBOF 
ADORecordsetGetCacheSize 
ADORecordsetGetCursorLocation 
ADORecordsetGetEOF 
ADORecordsetGetMaxRecords 
ADORecordsetGetPageCount 
ADORecordsetGetPageSize 
ADORecordsetOpen 
ADORecordsetPutCacheSize 
ADORecordsetPutCursorLocation 
ADORecordsetPutMaxRecords 
ADORecordsetPutPageSize 
ADORecordsetToXML 
BrowseRefresh 
BrowsetoXML 


---

IDE User's Guide 
222 
 
 
 
Project System 
All of the components that are used to create the final executable (target file) for your application is managed by a Clarion 
Solution file (*.SLN) . The project file (contained in every solution, and using a .CWPROJ extension) stores the compiler 
options ranging from whether to include debug code or not, to setting a preferred optimization method. The compiler and 
the linker depend on this project information to tell them how, and what, to compile and link. The project information is 
functionally equivalent to a MAKE file for other language compilers. 
The Clarion Project System visually manages the project information. It maintains tree diagrams of the source files, 
external libraries, resources, and other project components. 
 
 
 
 
This chapter discusses the Project System and related topics. It shows you how to: 
• 
Add source code files to the Project Tree. 
• 
Add external libraries to the Project Tree, and how to access their functions and procedures in your source code. 
• 
Specify the target file and set other compiler options. The target file is the ultimate executable created for your 
application or project 


---

User's Guide and Lessons 
223
 
 
 
Hand Coded Projects 
This section provides an overview of the steps necessary to create a solution file (*.SLN), and associated project file 
(*.CWPROJ). The project file tracks all the components that are used to create the executable file. It also sets the 
compiler options ranging from whether to include debug code or not, to defining switches. 
If you use the Application Generator to create your source code, the project files are created automatically, and the only 
thing you will probably use the Project System for is to set debugging options. The Application Generator takes care of 
maintaining most everything else for you. Therefore, this chapter is primarily concerned with using the Project System for 
hand-coded programs. 
The Project Tree dialog organizes all the project components and provides access to other dialogs that manage your 
project file. 
 
 
To create a solution and project file 
1. Choose File New Solution, Project, or Application. or press the New Project button 
 on the IDE 
toolbar 
This opens the New Project dialog. The Categories list contains all available code platforms currently registered in the 
IDE. The Quick Starts list contains all available targets for the selected category. 
In this topic we will focus on the Clarion for Windows category. For handcoded executables, the Win32 EXE Quick Start 
is selected, as shown below: 
 
 


---

IDE User's Guide 
224 
 
 
 
 
2. In the Name entry, enter a descriptive name for your project. By default, this will be the name of your project‘s 
target output, by this can be modified later in the Project Properties if needed. 
3. In the Location entry, enter (or select with the Browse for Folder dialog after pressing the ellipsis button) the 
location where the project will be created. 
4. Optionally check the Create directory for Sources and Auto create project subdir boxes to create additional 
project folders if needed 
5. Press the Create button. 
This opens the Solution Explorer dialog, and the Text Editor with your program‘s source file loaded. 
 
 
 
Add Project Components 
1. RIGHT-CLICK on any Project Tree component category (such as Database driver libraries), then choose the Add 
<component> menu item. 
This opens a dialog where you can select a component of the specified type. For Database driver libraries, the Add File 
Driver item calls the Select File Drivers… dialog so you can choose from a list of valid Clarion database drivers. In nearly 
all other instances, the Add <component> item opens the Windows File dialog to help you locate the component file. 
2. Select the component file to add it to your project. 
3. Repeat the above steps for all component files. 
 
 
Set Global Make Options 
1. In the Solution Explorer, select (CLICK on) the Project (first) line then press the Properties button in the Solution 
Explorer toolbar. 
This opens the Project Properties dialog. This dialog sets various compile and link options for your entire project, including 
optimization method, type of executable created, whether to include debug code, etc. 
Select the tabs in the Project Properties dialog to get an idea of the available options, or press the Help button to see a 
description of each option. See the core help Project Properties – Clarion 7 topic for more information on these compile 
and link options. 
 
 
Set Local Make Options 
Like the Add <component> menu item, the Properties button behaves differently depending on which Project Tree folder 
is highlighted. When a source file is highlighted, the Properties button calls the Properties Pad dialog. This dialog sets 
compile options for the specific source file highlighted. Specific compile options take precedence over global compile 
options. 


---

User's Guide and Lessons 
225
 
 
 
 
For now, select the property entries in the Properties Pad dialog to get an idea of the available options. 
 
 
Compile and Link Options 
This section provides an overview of the steps necessary to maintain a project file. Maintaining the project file includes 
adding and removing source files, object files, libraries, etc. from the compile and link process. In addition, you may set 
both global and local compile and link options in the project file. 
 
 
Here is a detailed look at the Project System‘s Compile and Link Options. 
 
 
Configuration 
Specify which Project configuration options you wish to set. Select Build or 
Release from the drop list provided. To change the Build target, use the 
Build/Set Configuration menu option. 
 
Platform 
Current default is AnyCPU. 
 
Target Name 
The output filename of the project. The Project System will use the description 
next to the Project name in the Project View tree list. It will also be the default 
project target filename (<output name.output.type>). Macros are allowed, but 
only %V%, %X% and %L%. 
 
Output Path 
The default target is based on the Project folder name and Build Configuration 
(e.g., <projectfolder>\debug or <projectfolder>\release). Use this option to 
specify an alternative target path where the target EXE, LIB, or DLL will be 
copied to. The only time you might want to use this is if you want to 
temporarily output a program you are creating to a different directory to 
preserve an old executable. 
 
Output Type 
Specify the type of executable file: choose .EXE, .LIB, or .DLL from the 
Target Type drop down list. 


---

IDE User's Guide 
226 
 
 
 
 
 
Link Mode 
Specifies how the runtime library is called by the target file: choose DLL LIB, 
or CustomDLL from the Link Mode drop down list.: 
 
 
 
DLL 
Uses the Clarion runtime library DLL (and database driver(s) 
.DLLs). It is called C70RUN.DLL. 
 
LIB 
Links the runtime library and any database drivers into your 
executable using Smart Method Linking (only the necessary 
portions are linked in). This creates a "one-piece" executable. 
 
CustomDLL 
Specifies that another External DLL contains the runtime libraries 
and database drivers. The calls to this DLL must be exported. 
 
 
 
Application 
icon 
By inserting .ICO files after the Application icon item, you can link the icons into 
your executable so they do not have to be shipped separately. 
 
Project 
Information 
Displays the Project folder, Project file and Output name. These items are 
read-only. 


---

User's Guide and Lessons 
227
 
 
 
Component Files 
This section explores the Project System‘s individual component files. 
 
 
Projects to Include 
The Project System can compile and link other projects referenced in the current project file. The other project can 
even specify yet another, in a cascading sequence of compile references. 
Cascading projects lets you split the development process into separate projects, then link them all together when 
you‘re ready. 
• 
To add a project to the Project Tree, RIGHT-CLICK on the Projects to include in the Project Tree list, and select 
the Add Project to Include menu item. Select the project file you wish to add with the standard Open File dialog. 
 
 
Source Code Files 
Source code files are those files that contain your Clarion Language statements (and other support statements). 
Adding a source code file to the Solution Explorer dialog is simply a matter of right-clicking on the project node and 
selecting one of the Add Item options.. 
External Source Files 
To add "hand-coded" source code files, RIGHT-CLICK on the Project name then select Add Exixting Item from the 
popup menu and select the file you wish to add with the Windows file dialog. 
Generated Source Files 
For application (*.APP) files, Generated source files cannot be added or deleted with the Project System. They can 
only be added or deleted with the Application Generator. Any attempt to add these source modules will add them to the 
External source files. 
 
 
Database Driver Libraries 
Your application calls various database driver routines to access your database tables. These routines are in libraries 
supplied with Clarion and installed by default in the \LIB subdirectory by the Clarion setup program. During the link 
process, references to these external routines can only be resolved if the library containing the routines is added to 
your project file. 
The Application Generator automatically adds the appropriate driver libraries based on the Data Dictionary table driver 
selections. For hand coded projects, you should manually add the appropriate driver libraries. 
• 
To link a database driver library, RIGHT-CLICK on File Drivers in the Solution Explorer list and select the Add 
File Driver item and select the driver to add from the Select File Drivers to Include dialog. 
 
 
Library, Object, and Resource Files 
 
 
Libraries and Objects 
An object (.OBJ) file contains objects—routines, functions, or procedures that can be linked into your program during 
the link process. A library (.LIB) file is simply a file that contains multiple objects. When properly linked, your program 
can call on these objects to perform certain tasks. 
You can create .LIB files for use with your Clarion applications. This topic is discussed in more detail in The Target File 
topic below. 
Objects used in this manner need not be written with Clarion. Your Clarion programs can call objects compiled from C, 
C++, Pascal, etc. 


---

IDE User's Guide 
228 
 
 
To link a library, object or resource file, RIGHT-CLICK on the Solution Explorer‘s Library, object, and resource files 
folder, and then select the Add Library, Object or Resource File(s) menu item and select the file you wish to add with 
the Windows file dialog. 
The .LIB, .OBJ, .RSC, etc. file appears in the Project Tree, and any objects from the file that are properly referenced in 
your source code are linked into your target (executable) file. 
 
 
Resource Files 
A resource file is any other file (.RSC, .ICO, .BMP) that should be linked into your program. One of the most likely 
things you‘ll do with the Project System is to specify resources to link into your executable. By linking them into the 
executable, you avoid having to ship them as separate, external files. 
If you directly reference a graphic file within a data structure, the compiler automatically links the graphic, so there is no 
need to add the graphic file to your Project Tree. For example, if you place an IMAGE control in a window, and specify 
a file by name in the Image Properties Pad dialog, the linker automatically includes that file in your executable. But if 
you assign a different graphic to a control using a run-time property assignment statement, the linker will only include 
the new file in your executable if you add the file to your Project Tree. 
The Clarion runtime libraries assume the .EXE or .DLL where a window was most recently opened is where any 
referenced icons are located. 
 
 
To add graphic files to the executable 
1. RIGHT-CLICK on the Solution Explorer‘s Library, object, and resource files folder, and then select the Add 
Library, Object or Resource File(s) menu item 
Select Image Files as the Files of Type filter, and then select the bitmap, icon, or metafile graphic from the standard 
Open File dialog. 
2. Press the OK button to return to the Solution Explorer. 
3. DOUBLE-CLICK on the source code file that references the graphic. The Text Editor opens the source code file. 
4. Place a tilde (~) in front of the graphic file name in the source code assignment statement (not in the data 
section). 
For example: change 
?Image{PROP:Text} = 'I.ICO' 
to 
?Image{PROP:Text} = '~I.ICO' 
The tilde indicates the program should find the item as a linked in resource, not as an external file. 
Optionally, choose Search  Find to locate the file name. 
5. Choose File  Close  File, then click on Yes when asked if you want to save. 
Now, when you recompile and link, the executable will no longer require the external graphic file. 


---

User's Guide and Lessons 
229
 
 
More Project Options 
Nestled in the Project Properties dialog are many other powerful options to your project. Here are some highlights. 
 
 
Build Events 
Build Events lets you customize the compile and link process by executing the program(s) of your choice at the 
beginning or the end of the build process. These can be .BAT files or more sophisticated .EXE files that perform any 
additional tasks you specify as part of the compile and link process. 
• 
To add a build event to the project, select the Build Events tab in the in the Project Properties dialog. Then 
select the pre or post event and enter the program file(s) you wish to add. Use the ellipsis to select an item 
from the Windows file dialog. 


---

IDE User's Guide 
230 
 
 
 
The Target File 
Using the Project System, you can create .EXE, .LIB, and .DLL files. This section describes these three target file types 
and how to create them. More information can be found in the Distributing Files section below, and see also 
Development and Deployment Strategies. 
• 
By default, the project system creates a standard executable (.EXE) file, which you distribute with C70RUNX.DLL. 
When you name the project file in the New Project File dialog, it automatically sets the Output Type extension to 
EXE and the Link Mode to Standalone in the Application Project Properties. 
• 
To create a library (.LIB file), simply change the Output Type extension located on the Project Properties 
Application tab. 
• 
To create a dynamic link library (.DLL), simply change the Output Type extension located on the Project 
Properties Application tab. 
 
 
Setting the Project‘s Output Type is equivalent to setting the Application‘s Destination Type and vice versa. See the 
Application Properties dialog. 
 
 
.LIB Files 
Library files (.LIB) contain procedures and functions that are linked into your executable at compile time. To create library 
files that may be accessed by Clarion, or by any of the other TopSpeed compilers, just set a .LIB file as the target file. 
To use procedures and functions from a precompiled .LIB file, you must prototype the procedures and functions called by 
your program. Prototyping is accomplished by adding a MODULE structure to your application‘s MAP. To call an external 
.LIB procedure from "hand coded" source: 
1. Add a MODULE structure to your application‘s MAP. 
The MODULE should reference the external library file. In the Application Generator, you can place this in the Inside the 
Global Map embed point. 
2. Add the procedure prototypes: 
Example: 
 
MAP 
## MODULE(‘EXTERNAL.LIB’)
ExtProc(*CSTRING),RAW 
ExtFunc(USHORT, *BYTE[]),USHORT 
END 
END 
 
Each prototype specifies the name of the procedure, the data types of any parameters (in parentheses), and the return 
data type (if any). 
In the example above, the ExtProc procedure expects the address (without the length, hence the RAW attribute) of a 
CSTRING to be passed to it as a parameter. 
The ExtFunc procedure expects the value of a USHORT variable, the address of an array of BYTEs, and will return a 
## USHORT.
3. To specify a different calling convention, add it to the prototype. 


---

User's Guide and Lessons 
231
 
 
 
 
You may use .LIB or .OBJ files created by other compilers. 
Modifying the above examples, the first line below identifies a procedure expecting the C calling convention. The second 
line identifies a procedure expecting the PASCAL calling convention, which is the Windows standard calling convention: 
 
 
ExtProc(*CSTRING),C,RAW 
ExtFunc(USHORT, *BYTE[]),USHORT,PASCAL 
 
4. To optionally specify a third party linker‘s identifier, add it to the prototype. 
Some compilers, most notably ‗C‘ language compilers, add a leading underscore to the name of procedures and functions 
at compile time. The examples below add the NAME attribute: 
 
 
ExtProc(*CSTRING),C,RAW, NAME(‘_ExtProc’) 
ExtFunc(USHORT, *BYTE[]),USHORT,PASCAL,NAME(‘_ExtFunc’) 
 
For more information refer to the Language Reference Help regarding the following topics: MODULE, MAP, 
PROCEDURE, and prototypes for more information. 
 
 
.DLL Files 
Dynamic Link Libraries (.DLL) contain procedures that are linked to your application at run-time. To create dynamic link 
libraries, just specify .DLL as the target file extension. 
To call a .DLL procedure, follow the steps outlined for calling a .LIB procedure, above. 
Setting the Project Properties‘s Output Type is equivalent to setting the Application‘s Destination Type and vice versa. 


---

IDE User's Guide 
232 
 
 
 
Distributing Files 
This topic describes the different program distribution options available to you. 
 
 
Choosing a Configuration 
This section is included to help you decide what kind of target file to specify for your project. Also see Development and 
Deployment Strategies. 
Clarion produces executable files which you may distribute on a royalty-free basis. The applications you distribute require 
Windows 2000, NT, XP or Vista versions. 
Clarion executables come in two flavors: .EXE files, and .DLL files. An .EXE file is simply an executable program. A .DLL 
(Dynamic Link Library) file is executable code that is linked into an .EXE file at run-time. This is in contrast to .OBJ and 
.LIB files which are linked into an .EXE at compile time. The most obvious benefit of the .DLL is that it provides a method 
of modifying .EXE operation without remaking (compiling and linking) the .EXE. 
Clarion executables may be distributed in three configurations: 
1. *.EXE ( A one-piece .EXE) 
A one-piece .EXE will usually be larger than an .EXE distributed with .DLLs. However, the one-piece .EXE will probably 
be smaller than the combined sizes of an .EXE and its associated .DLLs. 
The one-piece .EXE is made as small as possible by Clarion‘s smart linking process that only links in procedures actually 
called by the application program (whereas the .DLL contains a fixed set of procedures, whether or not they are actually 
called by your program). 
A one-piece .EXE cannot have conflicts or problems that arise from linking with the wrong .DLLs at run time. 
Make (compile and link) time for a one-piece .EXE is greater than for an .EXE combined with .DLLs. 
 
To make a one-piece .EXE follow the steps described in Development and Deployment Strategies. 
 
 
2. *.EXE + Runtime library (C70RUNX.DLL) 
Splitting the executables between .EXEs and .DLLs allows for more efficient use of disk space. Many Clarion applications 
(.EXEs) can share a single C70RUNX.DLL. Or, a single application suite with several .EXEs can share a single 
C70RUNX.DLL. However, as a developer, you must ensure that your application accesses the correct version of the 
runtime library. 
An example of .DLL usage is the typical accounting system where the .EXE controls the system main menu, and calls 
system subparts such as Accounts Receivable and Accounts Payable from separate .DLLs. This method of distribution 
allows for program parts to be sold and maintained separately. 
 
 
Splitting executables between .EXEs and .DLLs allows for more efficient use of disk space, but less efficient use of RAM. 
This is because the Windows operating system loads an additional C60RUNX.DLL into memory for each active Clarion 
executable, and because the C60RUNX.DLL contains some procedures your .EXE never calls. 
 
 
To make an .EXE + C70RUNX.DLL: in the Project Properties dialog within the Project System, set Output Type to .EXE 
and set Link Mode to Standalone. 
 
 
3. *.EXE + C70RUNX.DLL + *.DLL1 + ... + *.DLLn 


---

User's Guide and Lessons 
233
 
 
 
This configuration offers the same advantages and disadvantages as the .EXE + C70RUNX.DLL configuration. It is listed 
here to illustrate that you are not limited to a single .DLL, nor are you limited to Clarion .DLLs. Your Clarion applications 
may make use of .DLLs compiled from other languages as well as the C70RUNX.DLL and the SoftVelocity database 
driver .DLLs. 
4. *.EXE + *.DLL1 + ... + *.DLLn 
This configuration offers most of the same advantages and disadvantages as the .EXE + C70RUNX.DLL configuration. It 
is listed here to illustrate that the C70RUNX.DLL may be linked into another .DLL. This technique "hides" the 
C70RUNX.DLL and ensures that your application will never get the wrong version of C70RUNX.DLL, because, 
technically, it isn‘t looking for C70RUNX.DLL. 


---

IDE User's Guide 
234 
 
 
 
 
To "hide" C70RUNX.DLL in another DLL, follow the steps described in the Development and Deployment Strategies topic. 
 
 
Installing and Accessing Your Application’s DLLs 
If you distribute C70RUNX.DLL, it must reside in the same directory as the application program, in the Windows\System 
subdirectory, or in a directory referenced in the system PATH. We recommend that you install C70RUNX.DLL to the 
application directory. 
Remember, multiple Clarion applications may use the same C70RUNX.DLL file, thus saving space on the users‘ hard 
drive. On the other hand, sharing a single C70RUNX.DLL raises the possibility of conflicts among applications developed 
under different versions of Clarion. To avoid possible conflicts, install a separate C70RUNX.DLL to each application 
directory, or distribute the application as a single .EXE file, or link the C70RUNX.DLL into another .DLL that is unique to 
your application. 
 
 
The Ship List 
For generated applications, Clarion templates automatically create a ship file (.SHP) that contains the names of the files 
that are needed to run your application. The file is called application.SHP and is in the same subdirectory as your .APP 
file. 
This ship file only includes those files that are visible to the templates. Any DLLs loaded in EMBEDs or INCLUDE files 
may not be visible to the templates, and may not be in the list. 
In the case of external library modules, the .LIB file is also included in the list. Some of the .LIBs (WINDOWS.LIB for 
example) do not have associated DLLs; however, most do have associated .DLLs that you will need to distribute with your 
application. 
In the case of an external library module generated by Clarion, you must ensure that all files on the shipping list for that 
LIB/DLL are also included. 
 
 
You can modify your application‘s ship list by embedding text at the Inside the Shipping List Global Embed point. 


---

User's Guide and Lessons 
235
 
 
 


---

IDE User's Guide 
236 
 
 
 
Writing Clarion Code 
 
Source/Text Editor 
This lesson introduces the Source/Text Editor. 
If you allow the Application Generator to write most of your source code, you will probably only use the Text Editor to write 
your embedded source code (see Application —Embedded Source Code). If you write your source code "from scratch," 
you will probably use the Text Editor extensively to create and manage your code. The Text Editor features the following 
to help you accomplish either purpose: 
 
 
• 
Multiple Document Windows, in which you may edit as many documents as your system allows. 
• 
Color coded syntax highlighting, which makes reading individual code lines easier. The color coding is fully 
customizable. 
• 
Always available Search and Replace. 
• 
Auto-indent, to make reading and writing code easier. 
• 
Next Error and Previous Error locator. 
• 
Current cursor position (row and column), displays on the status bar. 
• 
Configuration options to customize the Text Editor to fit your needs. 
• 
F1 hyperlink sensitive help for all Clarion Language statements. 
• 
Code folding and code completion options. 
• 
Ability to create user-defined macros. 
 
 
Opening the Text Editor 
Anytime you view a source code document with Clarion, you use the Text Editor. Here are several ways to open a 
source code document: 
 
 
• 
In the IDE Menu, choose File  New  File to open the New File dialog. Select the appropriate Category and type 
of file in the Quick Starts. This opens a blank source code document. After editing, when you close the file, you 
can navigate to your target directory and fill in the name of your new file in this standard dialog. Then press the 
Save button. 
• 
Choose File  Open  File, select the Clarion Files of type source, then DOUBLE-CLICK a source code file in the 
standard Open File dialog. 
• 
Use the Start Page to view your most recently edited files. Select the Source Files section, and click on a source 
code file entry. 
• 
In the Solution Explorer, DOUBLE-CLICK on any source (.CLW) file to open it. 
• 
After a compile that generates errors, DOUBLE-CLICK on any entry in the Errors Pad. 
• 
In the Application Tree dialog, RIGHT-CLICK a procedure, then choose Source to open the Embeditor (Text Editor 
in a special embedded source mode). 
• 
In the Application Tree dialog, RIGHT-CLICK a procedure, then choose Module to edit a generated source module. 


---

User's Guide and Lessons 
237
 
 
Managing Text Editor Windows 
Each source code file appears in a separate document window. This section provides a summary of actions you can take 
to change the layout of these windows: 
The Editor’s document window features color-coded syntax highlighting. 
 
 
Close a window 
Choose File  Close  File from the main menu, or press the "X" in the client area, or RIGHT-CLICK on the tab, and select 
Close, or press CTRL+F4. 
 
 
Activate a window 
Click anywhere within the window, or select the document name from the Window menu. Alternatively, press CTRL+F6, or 
CTRL+SHIFT+F6 until the window you wish is active. 
 
 
Move a window 
Drag the document window‘s tab with the mouse, and dock it where desired. 


---

IDE User's Guide 
238 
 
 
Resize a window 
Drag its border with the mouse. 
 
 
Maximize a window 
Press the maximize button on the IDE title bar; or choose Maximize from the window‘s system menu. 
 
 
Iconize a window 
Press the minimize button on the IDE‘s title bar; or choose Minimize from the window‘s system menu. 
 
 
Restore iconized 
To restore an iconized document window, DOUBLE-CLICK the IDE tray icon; or choose Restore from the icon‘s system 
menu. 
 
 
Cycle to next window 
To switch to the next window, press CTRL+F6 or CTRL+SHIFT+F6. 
 
 
Feature Tour 
 
 
Full visual control 
Control your display colors, line numbers, rulers, and enable or disable the features that you need. 


---

User's Guide and Lessons 
239
 
 
Configurable with different file extensions 
The Text Editor has built-in configurations for over 9 different extension groups, including Clarion! 
 
Support for code folding 
 
 
 
Code Completion 
The new Text Editor can assist you with completing language constructs and classes 
 
 
 
 
Code Templates 
Code Templates or Snippets can be added and used anywhere in the Editor! 
 
 
 


---

IDE User's Guide 
240 
 
 
 
 
Customizable Smart Indentation 
The Text Editor offers two text indentation modes. Smart indentation is fully customizable. 
 
 
 
Quick Class Browser 
The optional Quick Class Browser allows a quick jump to any CLASS method or PROCEDURE: 
 
 
 
 
Go to…options 
You can jump to any method or procedure‘s definition or declaration, rename it, and identify the references. 
 
 


---

User's Guide and Lessons 
241
 
 
Powerful Search and Replace options. 
The Text Editor has a versatile and flexible Search/Replace interface, where you can search an individual file, or an entire 
project or drive/directory: 
 
 
 
Built in special XML Editor and Code Completion 
Finally, there is a special XML editor and menu system: 
 
 


---

IDE User's Guide 
242 
 
 
Customizations 
We suggest that before you start with any serious editing session that you first browse and explore the Text Editor 
Options. With very little effort, you‘ll find a comfort setting that will ensure success and optimize your productivity. 
To access the Text Editor Options, select Tools > Options > Text Editor from the main IDE menu: 
 
 
 
 
Nearly everything you need to customize the editor is contained in this section. 
In the General section, you can set the custom font type and size used by the editor, and enable or disable the code 
folding and Quick Class Browser. 
The Markers and Rulers section controls rulers, line number display and style, and visual display and limits of tabs, 
spaces and the editor cursor (caret). 
The Behavior section controls your indentation options, caret behavior, and mouse wheel direction. 
Clarion Specific Options give you added control to the Smart Indentation mode, and includes other auto-formatting 
features. 
The Code Completion section allows you to enable or disable its use, and adds other options as to storage and code 
completion behavior. 
The XML Options and Schema sections control the XML editor add on behavior in general. 
Finally the Highlighting section displays all built-in file extensions and their highlighting schemes. This area is very 
detailed and specific for many elements within the text editor. 
 
 
Using the Quick Class Browser 
When viewing any Clarion source file in the Text Editor, it is often necessary to locate program dependencies. In other 
words, one source file might contain a procedure that is calling another procedure. 


---

User's Guide and Lessons 
243
 
 
The Text Editor enables a Quick Class Browser, and enabled or disabled in the Tools > Options > Text Editor > 
General dialog. 
This utility is anchored on top of the Text Editor as shown here: 
 
 
 
The left drop list displays all global declarations, and is useful whenever the program‘s global section is active: 
 
 
 
 
When the global source is active, a list of global classes, files and record structures are listed. Clicking on any element will 
jump directly to that structure. 
Once a structure has been targeted in the global section, the drop list on the right displays the sub elements of the target 
structure. For example, if a FILE is selected, the drop list on the right will display all elements in that structure that are not 
part of another structure. In most cases, this would be KEYs, MEMOs, and BLOBs. 
If a RECORD structure is selected, a list of Fields are displayed: 


---

IDE User's Guide 
244 
 
 
 
 
 
 
Finally, each of the program‘s module will display a complete list of prototypes: 
This tool is very handy locating all prototypes and references, and when used with the "Find References" option, can be 
an invaluable debugging technique. 


---

User's Guide and Lessons 
245
 
 
Code Completion 
Code Completion is a feature provided by the Clarion text editor that involves predicting a word or phrase that the user 
wants to type in without the user actually typing it in completely. 
 
 
 
Code Completion can be used to find a desired method. In the code sample shown above, typing "SELF." displays a 
popup of valid methods that can be used here. 
The same also applies for language statements. For example: 
The word INSTRING, followed by an open parentheses, displays a popup of 3 valid choices that match the INSTRING 
function. 
 
 
Code Snippet Wizards 
In addition to the Quick Class Browser and Code Completion as powerful language tools, there is also support in the Text 
Editor for Code Templates (or Code Snippets). We use the term "Snippets" here as not to confuse them with the Code 
Templates used in the Application Generator. 
Here is how they work. After assigning the target file extension group, a template name and optional description is added 
or assigned to the extension group. For each name, a section of custom code is added. Pressing a hot key at any place in 
the editor activates this list of code templates. 
Code Snippets are configured in the Tools > Options > Coding section as shown below: 
Code Templates are assigned by file extension. Built into the IDE are preset Code Templates for HTML, CS (C Sharp), 
and VB (Visual Basic). 
To add the Clarion extensions to the Code Template section. 
1. Press the Add New Group button. 


---

IDE User's Guide 
246 
 
 
 
2. In the Extensions prompt, add the clarion source extensions (.clw;.inc) 
3. Press the Add button. In the Edit Template dialog, add the Template code word, and an optional Description. 
4. Finally, in the text area below, enter the actual code sequence. 
Here are a few sample entries: 
 
This list can be as extensive as you like. You will probably want to add the construct that you use more often, and also 
include the more complex code sequences. 
To apply (use) the code templates in your target source, press CTRL + J at any time. You will see a display similar to the 
Code Completion popup: 


---

User's Guide and Lessons 
247
 
 
Go to Definition/Declaration 
Another powerful feature included in the Text Editor is its ability to recall any method‘s definition and corresponding 
declaration. 
To see this, you can right click on any PROCEDURE definition or declaration in any CLASS. For example: 
 
 
 
In the popup menu shown above, if you click on "GoTo Definition": 
This feature is very handy in large projects and multiple source files, as the GoTo will span files. 
Search Features 
The Clarion Text Editor has a very powerful Search and Replace dialog. To activate it at any time from within the editor, 
press CTRL + F. 
This dialog serves both Find and Replace options. Clicking on the Replace toolbar button adds an additional Replace 
with: prompt. 
You can search single or multiple documents using this dialog, and optionally replace the target search string. 
For example, in the following code project, I am looking for all instances of Init 
In the Find what prompt, enter Init. You can also select a previous search string from the drop list. 


---

IDE User's Guide 
248 
 
 
The Look in option sets the range of the current search. You can search in the active open document only, the selected 
elements of an active document, all open documents, the entire active project or entire solution (where multiple projects 
are possible). Press the ellipsis button to select an external folder to search. If you are searching in a target folder, check 
the Include sub-folders box to allow the search to cascade into any sub-folders. 
If your Look in option is a folder, the Look at these file types: prompt is enabled. Enter the file type extensions to search 
into. Use a semicolon to separate multiple extensions. 
You can also limit your search using the Match Whole word only or Match Case before clicking on the Find Next button. 
The last decision is the type of search to execute. Standard search looks for the exact string in the Find dialog. Regular 
Expressions searches based on the result of a valid expression entered. Basically, a regular expression is a pattern 
describing a certain amount of text. Their name comes from the mathematical theory on which they are based. Your 
regular expressions require the C# syntax. Wildcards allows the use of wildcard characters in the search string. 
After the search above, here are our search results: 
398 occurrences may not be effective. Let‘s narrow it down a little more: 
 
Or maybe we just need to add a little more to the search term: 


---

User's Guide and Lessons 
249
 
 
 
 
 
 
Code Folding 
Another popular editor feature in this release is the use of Code Folding. 
Code Folding is popular with many developers because it allows them to collapse sections of source code while working 
in other parts of it. This allows you to manage larger amounts of code within one window. 
You enable or disable code folding by accessing the option in Tools > Options > Text Editor > General: 
The + and – icons control the code folding. When code is folded, you can move your mouse over the ellipsis button to see 
a partial popup of the folded contents. 


---

IDE User's Guide 
250 
 
 
Indentation 
Indentation within the Text Editor is controlled in the Tools > Options > Text Editor > Behavior dialog. 
The new Text Editor has three indentation modes. 
None provides no indentation at all. As you press the Enter Key, the editor caret (the blinking cursor) is always returned to 
column 1. 
Automatic 
With Indentation set to Automatic ,the Text Editor keeps a running indent. When you press the Enter key, spaces and tabs 
are inserted to line up the insert point under the start of the previous line. 
Smart 
After a keyword statement, the next line is indented by the tab size set above. After certain keywords (break, return etc.) 
the next line is "non-indented". 
 
 
Other rules for Smart indentation include: 
• 
Indent statements from the CODE keyword position. The default is "on". 
 
 
 
 
• 
Treats any expression that ends with a colon ":" as a label in the CODE section (The default is off, where colons 
are treated as an actual procedure call). You need to have the caret position at the beginning of the target 
statement, and then press Enter. 
 
 
 
 
• 
Indent a line after the Enter key is pressed at the end of the line. The default is on. 


---

User's Guide and Lessons 
251
 
 
 
 
 
 
 
• 
Indent pasted text if several lines were pasted. The default is "off". 
 
 
 
 
• 
Preferred indentation to a specified column number. If a recognized keyword should not be indented relative to 
the parent, it will be indented to the preferred column. The default setting is column 21. 
 
 
• 
Automatic comment indentation. The default is off. 
 
 
 
See the Clarion Specific options dialog to control each of the options described above. 


---

IDE User's Guide 
252 
 
 
 
Formula Editor 
If you are new to Clarion or the Clarion Language, there is a powerful utility available to you that is built-in to the 
Application Generator called the Formula Editor. As a matter of fact, its ease of use causes many experienced users to 
continue to use it regularly. 
The Formula Editor helps you to quickly generate language statements or structures that assign a value to a variable. You 
can use the Formula Editor to create unconditional or conditional assignments. 
• 
An unconditional assignment assigns the evaluation of an expression to the variable you specify: variable = 
expression. For example, a variable called GrossPrice might receive the result of adding two variables called 
BasePrice and Tax. 
• 
A conditional assignment places multiple possible assignments within a structure that executes only one of them. 
The Formula Editor builds IF structures and CASE structures for this purpose. The assignment statement 
executed depends on the evaluation of the IF or CASE condition. For example, a conditional variable called "Tax" 
could equal 0 when "Taxable" (the IF condition) evaluates as false, or "Tax" could equal Price times TaxRate if 
"Taxable" is true. 
The Formula Editor dialog provides access to data dictionary columns, as well as global and local memory variables, and 
helps you create syntactically correct expressions. This is its prime advantage: automatic syntax checking. 
To create an expression, you press buttons to add expression components to the Statement line. You can also enter 
your expression then check the syntax upon completion. 
Let‘s quickly review the components of a Clarion expression in the next section. 
 
 
Expressions 
An expression is made up of two types of components: operands and operators. Operators perform an operation (such as 
addition, subtraction, etc.) on one or more operands of the expression. Operands are the components on which 
operations are performed. Operands either contain or return a value. Constants, data dictionary columns, memory 
variables, and functions are examples of operands. An operand can be made up of more than one component, such as a 
function and its parameters. 
The Formula Editor lets you choose operators and operands, and then insert them into the Statement line. 
The sections below lists all the components used in Clarion expressions. 
Math Operators 
 
+ 
Plus sign: Adds two operands together. 
 
- 
Minus sign: Subtracts one operand from another. 
 
* 
Asterisk: Multiplies one operand by another. 
 
/ 
Slash: Divides one operand by another. 
 
% 
Percent sign: Returns the remainder from a division operation (modulus division). 
 
^ 
Caret: Raises one operand to the power of the other. 
 
( ) 
Parentheses: Groups components together within an expression. 


---

User's Guide and Lessons 
253
 
 
Logical (Boolean) Operators 
 
= 
Equal: Evaluates whether one expression is equal to the other. 
 
< 
Less Than: Evaluates whether one expression is less than the other. 
 
> 
Greater Than: Evaluates whether one expression is greater than the other. 
 
<> 
Not Equal: Evaluates whether one expression is not equal to the other. 
 
>= 
Greater or Equal: Evaluates whether one expression is greater than or equal to the 
other. 
 
<= 
Less or Equal: Evaluates whether one expression is less than or equal to the other. 
 
AND 
Connects two logical expressions together. For an expression containing an AND to 
be true, both expressions of the AND must be true. 
 
OR 
Connects two logical expressions together. An expression containing an OR is true if 
either expression of the OR is true. 
 
XOR 
Connects two logical expressions together. An XOR expression is true if either 
expression is true, but not both. 
 
NOT 
Reverses the evaluation of an expression. 
 
~ 
Reverses the evaluation of an expression. 
 
 
String Operators 
 
& 
Ampersand: Appends one text string to another. 
 
 
Operands 
 
Data 
Includes data dictionary columns, global, and local memory variables. 
 
Functions 
All of the built-in functions of the Clarion language. These functions all 
perform some operation on parameters (other operands) and return a 
value. 
 
User 
Any FUNCTION in your application. These functions perform some 
operation on parameters (other operands) and return a value. 
 
Constant Text 
You can type constant text surrounded in single quotes ( ‗A‘ ) on the 
Statement line. 
 
Constant Number 
You can type constant numbers on the Statement line. Constant numbers 
can be represented in any valid format, such as Decimal (1 or 1.2345), 
Scientific Notation ( 22e4), Binary (0101b), or Hexadecimal (1AFFh). 


---

IDE User's Guide 
254 
 
 
 
 
Example Expressions 
 
Lastname & ‗, ‗ & FirstName 
!concatenated string constants & variables 
ABS(Amount) * 100 
!function, numeric variable & constant 
TaxCode = True AND Amount > .25 
!Boolean with variables & constants 
 
Using the Formula Editor 
The Formula Editor consists of three dialog boxes: 
 
Formula 
Manages all formulas you have created for the procedure. 
Formula Editor 
Creates simple assignment statements. 
Conditionals 
Creates conditional structures (IF..THEN or CASE..OF). 
 
 
Formula Dialog 
See the Formula Dialog core help topic for a detailed look at the prompts and options on this window. 


---

User's Guide and Lessons 
255
 
 
Formula Editor Dialog 
See the Formula Editor Dialog core help topic for a detailed look at the prompts and options on this window. 


---

IDE User's Guide 
256 
 
 
 
Development and Deployment Strategies 
 
Overview—EXEs, .LIBs, and .DLLs 
The way you organize your application files can have a significant impact on the efficiency of your work processes 
throughout the life cycle of the application. For example, developing all of your procedures within a single .APP file keeps 
everything under one roof. This can be a benefit for smaller applications—keeping all files in a single directory makes 
finding and backing up the files quite easy if there are reasonably few files. This benefit can become a problem for larger 
applications—backing up or compiling hundreds of files at once can be time consuming and tricky. So you can see how 
organization affects the development phase of your application. 
The ultimate size and number of your application‘s executable files affects your ability to quickly and easily distribute 
upgrades and bug fixes to your end users. This is one way that organization affects the maintenance phase of your 
application. 
This appendix discusses of some of the factors you should consider when deciding how to structure your application files, 
both for the development and maintenance phases of the application. This includes instructions on how to implement the 
organization that best suits your needs. 
Generally speaking, the benefits of breaking large programming projects into smaller logically related pieces are: 
 
 
Development Phase 
• 
Smaller, more manageable problems. 
• 
The ability to test and debug smaller pieces of code. The smaller the code, the easier it is to isolate problems. 
• 
Faster compile and link times. 
• 
The ability to make your code generic and reusable. 
• 
The ability to delegate programming tasks to multiple programmers. 
 
 
Maintenance Phase 
• 
The ability to sell and distribute discrete application components. 
• 
The ability to deploy bug fixes and upgrades with small files. 
• 
For reused code, the ability to affect many procedures by changing a single source file. 
These benefits are most easily realized by creating multiple .APP files that are used to make separate .DLLs or .EXEs 
that are developed and tested independently. As the project nears completion the executable files are linked together 
and tested as a whole. 
Some problems associated with breaking large programming projects into smaller pieces include: 
Development Phase 
• 
Managing more files: backing up, naming conventions, and synchronization of files becomes a bigger job. 
• 
Correctly linking together related pieces of executable code. 
 
 
Maintenance Phase 
• 
Managing more files: version control is more difficult. The end user must have a complete set of compatible files. 
• 
For reused code, unintentionally affecting many procedures by changing a single source file. 
• 
Accidentally omitting a required file during deployment. 


---

User's Guide and Lessons 
257
 
 
 
Multi-Programmer Development 
Clarion‘s modular approach to source code management, its procedure-oriented language, and its ability to produce .DLL 
and .LIB files allows your team to split the work on big programming projects. 
Our recommended methods for group development assume the team is linked by a LAN, which supports the ability to 
grant read-only or read-write privileges to individual developers. It doesn‘t matter whether the LAN is peer-to-peer or a 
more traditional network operating system. We also assume the project will have a Team Leader or Project Manager to 
coordinate the overall efforts of the team. Finally we assume, as per our license agreement, each Clarion programmer has 
a licensed copy of Clarion. 
The first step to prepare for a team-development project is to create a data dictionary available to all developers, but 
which only the team leader may edit. An Application Generator option (Open Dictionary Files and Template Registry as 
Read-Only check box under Tools  Application Options) provides support for opening the Data Dictionary and 
TemplateRegistry.TRF in read only mode, so that many developers working with separate .APP files can work with the 
same dictionary. Prior to beginning the project, all team members should synchronize their TemplateRegistry.TRF and 
their template source files. The Team Leader should be responsible for the dictionary and the template set. 
Once the data dictionary is created, there are three basic approaches your team can take to use Clarion as a group 
development tool: 
• 
Procedure-oriented: 
The team divides the application into procedures, as listed in the Application Tree. These should be organized 
around the various windows, dialog boxes, menu items, and command buttons that form the user interface. 
The Team Leader prepares a "shell .APP," (or master) upon which all the others build. Each team member 
receives a copy of the .APP file, then works on a procedure (or procedures). The Team Leader imports the 
completed procedures into the master .APP file for compiling. This approach is suitable for small to medium size 
projects. 
• 
Module-oriented: 
The team divides the application into its target-file-level components (.DLL‘s, .LIB‘s, and executables). Each team 
member creates a single target file. Separate project files (.PRJ) compile the individual components. A master 
project file may include all the other project files, building all target files at once. This approach is suitable for 
medium to large size projects. 
• 
Sub-Application: 
The team divides the application into its target-file-level components (.DLL‘s). Each team member creates a single 
application or Dynamic Link library (.DLL). A master application calls each .DLL. This approach is suitable for 
medium to large size projects. This method provides the most flexibility and minimizes version control concerns. 
 
 
Enabling and Organizing Team Projects 
This section describes how to set up the Clarion Development Environment at each workstation, and where to store the 
files necessary for all three group development approaches: 
1. Create the data dictionary in a shared directory. 
All team members working on the project must have read rights to the directory. Those permitted to edit the 
dictionary should also have write privileges, though it may be best that only the Team Leader be allowed to edit it. 
2. Create a shared directory for resource files. 
Provide read rights for all team members to icon, cursor, bitmap, and other resource files. 
3. Within Clarion, at each workstation, choose Tools  Application Options. 
This opens the Application Options dialog. 
4. Check the Open Dictionary Files and Template Registry as Read-Only checkbox. 


---

IDE User's Guide 
258 
 
 
 
This specifies that when working in the Application Generator, the copy of Clarion residing at each workstation 
opens the dictionary file on the network in read-only mode. The purpose is to ensure that no one accidentally 
deletes a field, file, or key needed by other team members. For this reason, we recommend that only the Team 
Leader have write privileges to the directory containing the dictionary. To modify the dictionary, all team members 
must close all applications that use the dictionary. The Team Leader must clear the Open Dictionary Files and 
Template Registry as Read-Only box in order to modify the dictionary and, upon completion, check the box again. 
5. Press the OK button to close the dialog. 
6. Create a directory on each workstation‘s local drive to hold each team member‘s individual .APP and source files. 
The real work is planning how to split the development project, which is what the remainder of this chapter 
discusses. 
 
 
If your application‘s .DLLs use your application files, the FILE definitions and all Global variables must be declared in a 
.DLL (not the .EXE) and exported. See the Sub-Application Approach for more information. 
 
 
Procedure Oriented Approach 
The Application Generator lets you import and export procedures from other .APP files. With careful management, a 
Team Leader can organize development so that each team member can compile and test a copy of the application that 
includes the parts he or she works on. Each views the entire menu and the application‘s most important dialog boxes, yet 
executes only the procedures for which that team member is responsible. 
 
 
This approach is only necessary If your team members are not using Enterprise Edition, or do not have Version 
Control/team Developer. 
To accomplish this, each team member requires a copy of a "master" .APP file, containing the MAIN procedure (which 
would most likely be an Application Frame procedure), plus other procedures inserted below it as "ToDo" procedures. 
Each team member then "plugs in" the procedures he or she is responsible for. 
To assemble the complete application, using the Application  Import from Application command, the Team Leader 
imports each finished procedure into the master .APP file. 
The following outlines a possible implementation of the procedure-oriented approach: 
1. Create the data dictionary and set up the workstations as described above. 
2. Create a "master" .APP file in a directory to which only the Team Leader has write privileges. 
3. Within the .APP file, edit the MAIN procedure‘s most important user interface elements and declare its global 
variables. 
The user interface elements may include any dialog boxes or windows of particular importance to the application. 
As you specify procedure calls to menu items and/or toolbar controls, the Application Generator automatically 
adds "ToDo" procedures the application tree. 
4. Save and copy the .APP file to each team member‘s local drive. 
If the team prefers, you can rename each copy; for example, MASTER01.APP, MASTER02.APP, etc. or 
JIM.APP, JANE.APP, etc. 
5. Team members work on the procedures for which they are responsible, using their own copy of the .APP file. 
With the .APP file containing the complete user interface, each team member can compile an interim build locally, 
to test their own procedures while under development. 


---

User's Guide and Lessons 
259
 
 
 
6. Each team member synchronizes their local directory with an equivalent directory on the network at the end of 
each work session, or copies renamed .APP files to a "master" directory. 
7. To update the master .APP file with the latest work from a developer, the Team Leader replaces a "To Do" 
procedure in the Application Tree with a completed procedure in a team member‘s .APP by importing it. The 
Team Leader chooses Application Import from Application, indicating the same procedure in the .APP file in 
the developer‘s network directory. 
Any sub-procedures added by the team members will be brought along as new "To Do" procedures. When the 
Team Member completes these, they can be imported in the same manner. As the Team Leader‘s master .APP 
file "grows", it can be copied back to team members‘ individual directories (but only if all the work done by the 
individual team member was imported). This way, each team member has access to all the work completed by 
other members of the team. Keep in mind that each of the other member‘s modules will need to be compiled on 
the member‘s local drive. 
If the Team Leader is also a team member—i.e., also responsible for coding procedures—it‘s best to maintain a 
completely separate directory and copy of the master .APP file for that work. 
8. After importing the updated procedure, the Team Leader checks to see if it added any new "To Do" procedures to 
the tree, and imports those, if ready. 
Communication at this step is vital. In fact, based on E-Mail messages within the team, the Team Leader could 
optionally import "works in progress." 
9. The Team Leader compiles the project, so that it now includes each team member‘s work added through 
importing procedures. 
10. The Team leader repeats the last three steps on a periodic basis until all work by all team members is complete, 
and the entire application can be tested. 
 
 
Module Oriented Approach 
With this approach, each team member creates a separate target file. This requires splitting the application into a "Main" 
executable and "secondary" executables or dynamic link libraries. The individual team members maintain separate project 
files (.PRJ) for each component. The Team Leader creates a master project file to build all target files at once. 
The key to successfully implementing this strategy is extensively pre-planning the "division of labor" between the various 
target files created by the application. The Notes section below provides a few helpful suggestions. 
The following outlines a possible implementation of this strategy: 
1. Create the data dictionary and set up the workstations as described above. 
2. Each team member creates their own .APP and .PRJ files, specifying the dictionary file on the network as the 
data dictionary, and a directory on the local drive as the default directory for the .APP file. Each team member 
specifies a different target file. 
One particular .APP or .PRJ file creates the executable which launches or calls library functions or procedures in 
the others. To the end user, this is the .EXE program to start when working with the complete application. 
3. Each team member synchronizes their local directory with an equivalent on the network at the end of each day. 
4. The Team Leader creates a master .PRJ file which includes all the other .PRJ files, in a network subdirectory. 
The Team Leader inserts the name of each .PRJ file (previously copied to the network) in the Projects to Include 
item in the Project Tree. 
5. The Team Leader compiles the master project, which in turn compiles all the target files one by one. 
6. The Team leader repeats the last step on a periodic basis until all work by all developers is complete, and the 
entire application can be tested. 


---

IDE User's Guide 
260 
 
 
Notes on Splitting the Project 
There are probably as many ways to split a project, as there are projects; this section provides a few general suggestions. 
• 
If a task associated with a menu command requires extensive coding, store it in its own external .DLL, so that 
only a single developer can work on it. 
A typical example might be an accounting program, which could store all procedures and functions associated with 
accounts receivable in one .DLL file, accounts payable in another, and so forth. 
• 
Organize .DLL‘s by function; for example, place utility procedures and functions such as backups and file exports 
in a UTILITIES.DLL. 
• 
Store user defined functions in .LIB files; distribute the compiled .LIB files to each team member as they become 
available so that each may test any functions required in their own work. 
 
 
Notes on File Management 
Each multi-developer project has its distinct properties, so you‘ll undoubtedly adapt the following suggestions to fit your 
needs: 
• 
Create a subdirectory for each team member on the network drive, either at the same level or below the one 
holding the data dictionary file. Give each developer write privileges only to their own directory, and use a network 
utility to synchronize the directories at the end of the day. 
This not only serves as a backup, but provides the Team Leader access to the latest work done by all members of the 
team. 
• 
If the application under development creates an .INI file, a copy of it should reside in a network directory to which 
all team members have write privileges, so that if anyone should need to add a variable to the file, other members 
of the team can see it. 
 
 
Sub-Application Approach 
This section describes the steps to create a program using one main application and several sub-applications compiled 
and linked as external .DLLs. Dividing a large project into multiple .DLLs provides many benefits: 
• 
Each sub-application can be modified and tested independently. 
• 
Developers can work on their portion of the project without interfering with others on the development team. 
• 
Each sub-application can be compiled as a .DLL and tested in the main program without recompiling the entire 
project. This reduces compile and link time. 
• 
Dynamic Pool Limits are avoided in large projects. 
• 
Future updates can be deployed by shipping a new .DLL, reducing shipping costs. 
 
 
The Clarion runtime libraries assume the .EXE or .DLL where a window was most recently opened is where any 
referenced icons are located. 
With this approach, each Team Member creates a separate .DLL that is called by a "master" application. This requires 
splitting the application into a "Main" executable and "secondary" .DLLs. The individual team members maintain separate 
application files for each component. The Team Leader creates a master application that calls the sub-applications and a 
"data" application that contains (and exports) all the File definitions and Global variables. Optionally, members can call 
procedures from another member‘s .DLL. 
This method also requires extensive pre-planning of the "division of labor" between the various target files created by the 
application. The previous section provides a few helpful suggestions. 


---

User's Guide and Lessons 
261
 
 
 
The following outlines a possible implementation of this strategy: 
1. Create the data dictionary and set up the workstations as described above. 
2. Create a "data" application to store and export all data declarations. All Global variables or structures and all file 
definitions are defined (and exported) in this application. Use the following settings: 
In the Application Properties dialog: 
 
Dictionary File: 
master dictionary 
 
First Procedure: 
none 
 
Destination Type: 
## .DLL
 
 
In the Global Properties dialog General tab: 
Generate template globals and ABCs as External: 
OFF 
 
 
In the Global Properties dialog File Control tab: 
 
Generate All File declarations: 
ON 
 
External: 
## NONE EXTERNAL
 
Export All File declarations: 
ON 
 
 
 
You do not need (and should not have) OWNER, NAME or PASSWORD on those FILES which have the EXTERNAL 
attribute. These attributes should only be on FILEs not declared EXTERNAL. 
3. Team member create their own sub-application .APP files, specifying the dictionary file on the network as the data 
dictionary, and a directory on the local drive as the default directory for the .APP file. Each team member specifies 
a different target file using the following settings: 
In the Application‘s Module Tree: 
Choose Application  Insert Module, then in the Select Module Type dialog, select ExternalDLL, then 
in the Module Properties dialog, select the corresponding .LIB for the .DLL containing the data definitions. 
 
 
In the Application Properties dialog: 
 
Dictionary File: 
master dictionary 
 
Destination Type: 
.EXE for development 
 
.DLL for release 
 
Changing the Destination Type enables procedures to be exported. Make sure that every procedure that is called by the 


---

IDE User's Guide 
262 
 
 
 
master application or another .DLL has the Export Procedure check box in the Procedure Properties checked (the check 
box is only available after changing the destination type). 
In the Global Properties dialog General tab: 
Generate template globals and ABCs as External: 
ON 
 
 
In the Global Properties dialog File Control tab: 
 
Generate All File declarations: 
OFF 
 
External: 
## ALL EXTERNAL
 
All Files declared in another .App: 
ON 
 
Declaring Module: 
(Leave this blank) 
 
 
In the Global Properties dialog External Module Options tab: 
Standard ABC LIB/DLL? 
ON 
One particular .APP creates the executable which launches or calls library functions or procedures in the others. 
To the end user, this is the .EXE program to start when working with the complete application. 
4. Team members synchronize their local directory with an equivalent on the network at the end of each day. 
5. Team Members release their compiled and linked .DLLs to the Team Leader. 
Each sub-application has a "dummy" frame (not exported) that calls the sub-application‘s procedures so the Team 
Member can test the sub-application by compiling it as an .EXE. Once it passes testing, the member compiles it 
to a .DLL by changing the Application Properties‘ Destination Type to .DLL and releases the file to the Team 
Leader. 
 
 
If you edit the Redirection file to include "." at the start of the *.DLL and *.LIB search paths, Clarion generates the *.DLL 
and *.LIB files into the local sub-application subdirectory instead of \C70\BIN and \C70\OBJ. This is a little safety 
precaution that prevents the *.DLL and *.LIB from getting into other Team Members‘ hands before it‘s ready. In addition, 
adding the Master directory to the end of these search paths enables the sub-application or main application to find the 
completed .LIB‘s and .DLL‘s belonging to other sub-applications in the master subdirectory. 
6. The Team Leader copies the released .DLLs into the master directory and creates a master .APP file which calls 
the entry point procedures in the .DLLs. 
The Master .APP is typically just a bare bones application with just a splash screen and a main frame with a menu 
and toolbar. The .DLLs are called at run-time so you don‘t need to compile a large Master .EXE. The Master .APP 
should have the same settings as the sub-applications except that it is always compiled as an .EXE. 
The master .APP should have these settings: 
In the Application Properties dialog: 
Dictionary File: 
master dictionary. 
 
Destination Type: 
Executable (.EXE) 


---

User's Guide and Lessons 
263
 
 
In the Global Properties dialog General tab: 
Generate template globals and ABCs as External: 
ON 
In the Global Properties dialog File Control tab: 
Generate All File declarations: 
OFF 
 
External: 
## ALL EXTERNAL
 
All Files declared in another .App: 
ON 
 
Declaring Module: 
(Leave this blank) 
 
 
In the Application‘s Module Tree: 
Choose Application  Insert Module, then in the Select Module Type dialog, select ExternalDLL, then in the 
Module Properties dialog, select the corresponding .LIB for the .DLL containing the data definitions. 
Choose Application  Insert Module, then in the Select Module Type dialog, select ExternalDLL, then in the 
Module Properties dialog, select the corresponding .LIB for the sub-application .DLL. Repeat this step for each 
sub-application. 
 
 
For each procedure the main application calls, edit the ToDo procedure as follows: 
 
Template: 
External template. 
Module name: 
Select the .LIB from the drop-down list. 
If necessary delete any empty generated modules. 
7. The Team Leader compiles the master .APP and tests the calls to the .DLLs. 
8. The Team leader repeats the last step on a periodic basis until all work by all developers is complete, and the 
entire application can be tested. 


---

IDE User's Guide 
264 
 
 
 
One-Piece EXEs 
A one-piece .EXE is an .EXE file that contains everything it needs to run except files that cannot be linked in (.VBXs, data 
files, etc.). That is, the .EXE needs no associated .DLLs, .ICOs, etc., because they are already linked into the .EXE. 
 
 
When to Use One-Piece EXEs 
 
 
Development Pros and Cons 
Potentially none, because the final state of the .EXE does not necessarily affect the organization of the project at 
development time. 
For example, an application may be developed using several .APP files to generate separate executables (.EXE or .LIB). 
Eventually the separate executables are linked together to make a one-piece .EXE. 
The make time for the one-piece .EXE is greater than the make time for its individual components, so at the point in the 
development cycle where you link in and test all components, make times increase. 
Maintenance Pros 
You deploy a single file. There‘s no chance of forgetting a required executable file or of deploying an incompatible set of 
.EXEs and .DLLs. There‘s no chance of a conflict with a different version of a .DLL with the same name. 
Maintenance Cons 
Your changes require re-linking the entire project, plus deploying a larger file. Larger files are generally more difficult to 
deploy. Your end user cannot share .DLLs between multiple programs; that is, if two or more one-piece .EXEs execute 
the same code, that code is duplicated within each .EXE—an inefficient use of disk space. 
Conclusion 
Use a one-piece .EXE for small and medium applications that are infrequently deployed. That is, the application is 
reasonably stable or the application is distributed to only a few end users. 
Use .LIBs when you want to separate your development process into multiple applications, but you want to deploy your 
application as a one-piece .EXE. You can initially make each application an .EXE so it can be independently developed 
and tested. When you are ready to integrate all the applications together, make the called applications into .LIBs, then link 
them into the parent application. 
 
 
How to Implement One-Piece EXEs 
Create a one-piece .EXE from one or several .APP files. The simplest approach is to create an .EXE from a single .APP 
file. Alternatively, you may use several .APP files to create one or more .LIBs which are linked into the one-piece .EXE. 
You may want to create .EXEs rather than .LIBs during the development cycle in order to reduce link times and to permit 
isolated testing and debugging of discrete executables. Near project completion, convert to .LIBs by changing the 
Project‘s Target Type or the Application‘s Destination Type to LIB. 
To create a one-piece .EXE from one or more .APP files: 
Set the Parent Application’s Destination Type to EXE 
The highest level (parent) application‘s Destination Type should be set to .EXE in the Application Properties dialog. The 
parent application is the one whose procedures are not called by any other application‘s procedures. 
1. Open the parent application. 
2. Select the Properties tab from the Application Tree. 
3. In the Application Properties dialog, choose executable (.EXE) from the Destination Type drop-down list. 


---

User's Guide and Lessons 
265
 
 
 
 
Setting the Project‘s Target Type is equivalent to setting the Application‘s Destination Type and vice versa. 
Set the Parent Application’s Link Mode to LIB 
Set the parent application‘s Link Mode to Lib in the Project Editor‘s Application dialog. This links the Clarion runtime 
functions, including all referenced file drivers into the application‘s .EXE. 
1. Open the parent application. 
2. Choose Project  Project Options from the menu. 
3. In the Application tab, choose Lib from the Link Mode drop-down list. 
 
 
Run-Time Library in this context automatically includes all file drivers used by your application! 
If there are no LIBs, then you are ready to make your one-piece EXE. Skip to the last step in this section Make and Run 
Your One-Piece EXE. 
 
 
Make the LIBs 
You may make LIBs for other purposes than creating one-piece .EXEs. The following information, except Set the LIB 
Application’s Run-Time Library to Local, applies for any LIBs you make. 
Make and test your LIB application just as you would any other application. Note the name of your LIB and it‘s procedures 
because you will reference these names in your parent application. 
When you are finished testing, remake your LIB application with the following settings to create a LIB file to link into the 
parent EXE. 
1. Select the Properties tab from the Application Tree. 
2. Choose Library(.LIB) from the Destination Type drop-down list then press OK. 
 
 
Declare the LIB’s Procedures Globally 
By default, the ABC Templates declare procedures locally using local MAPs. Local MAPs minimize compile times but are 
inappropriate when making a LIB and will produce a "Link Error: procedure@F is unresolved..." when making the calling 
application. Within the LIB‘s application, you should declare globally, each procedure called by the parent application. So 
either 
1. In the Procedure Properties dialog, check the Declare Globally box for each called procedure; 
or 
1. Choose Tools  Application Options from the menu, select the Generation tab, then clear the Create Local 
Maps box to declare all procedures globally. 
 
 
Set the LIB Application’s Link Mode to Lib 
Set the LIB application‘s Link Mode to Lib in the Project Editor‘s Global Options dialog. This tells the linker that the 
Clarion run-time functions, including all referenced file drivers, are in the parent application‘s EXE. 
1. Choose Project  Project Options from the IDE menu. 
2. In the Application tab, choose Lib from the Link Mode drop-down list. 
3. Choose Build  Build Solution from the menu to make the .LIB. 


---

IDE User's Guide 
266 
 
 
Add the LIB Modules to Your Parent Application 
The following steps tell your parent application that some external procedures are called from a particular .LIB. 
1. Open the parent application. 
2. Choose Application  Insert Module from the menu. 
3. In the Select Module Type dialog, choose ExternalLIB. 
4. In the Module Properties dialog Name field, type the name of the .LIB then press OK. 
5. In the Module Properties dialog Map Include File field, type the name of the include file that contains the called 
procedures‘ prototypes. 
You must create this file. You can do so by copying the procedure prototypes from the generated appname.clw file and 
saving them into a separate .inc file. 
 
 
Add the External Procedures to Your Parent Application 
1. Open the parent application. 
2. Press the New Procedure button from the Application Tree. 
3. In the New Procedure dialog, type the name of the external procedure and press OK. 
4. In the Select Procedure Type dialog, select External. 
This opens the Procedure Properties dialog. The Files, Procedures, Formulas, and Extensions buttons on this dialog 
are not meaningful for external procedures and you should ignore them. 
5. In the Module Name drop-down list, select the .LIB that contains the external procedure then press OK. 
This tells the parent application where to find the external procedure. 
 
Make and Run Your One-Piece EXE 
1. Open the parent application. 
2. Choose Debug  Make and Run All from the menu. 
The Application Generator and the Project System generate source code, then compile and link the one-piece EXE based 
on: 
• 
Application Properties‘ Executable(.EXE) Destination Type 
• 
Project Editor—Global Options .EXE Target Type 
• 
Project Editor—Global Options Local Run-Time Library 
• 
The .LIB Modules and external procedures you inserted into your application tree. 


---

User's Guide and Lessons 
267
 
 
 
EXE Plus DLLs 
.EXE Plus .DLLs is an .EXE that requires some associated files that could have been linked into the .EXE at compile 
time. That is, the .EXE does need associated .DLLs, .ICOs, etc., because they are not already linked into the .EXE. 
The use of this configuration primarily affects the maintenance cycle of the application; however, the creation of one or 
more .DLLs implies the presence of multiple .APP files, which also affects the development cycle. 
The .DLLs often include the Clarion run-time .DLL and one or more file driver .DLLs. Please be aware that these .DLLs 
may be hidden by creating a one-piece .EXE, or by linking them into another .DLL that you create! See Hiding the Clarion 
Run-time Library. 
The Clarion runtime libraries assume the .EXE or .DLL where a window was most recently opened is where any 
referenced icons are located. 
 
 
When to Implement 
Use an .EXE plus .DLLs for two or more applications that share a common .DLL. This saves disk space. A good 
example of this is two Clarion applications that use the same TopSpeed file driver: C70TPSX.DLL. The applications 
and shared .DLLs should be fairly stable so you don‘t have two different .DLLs with the same name on the same 
machine. Different .DLLs with the same name can lead to confusion and worse if the .DLL files are not managed 
properly. 
Use an .EXE plus .DLLs for very large applications or for applications that are deployed frequently. This lets you deploy 
only the portions of the application that actually change. 
 
 
How to Implement 
To create an .EXE plus .DLLs: 
Set the Parent Application’s Destination Type to EXE 
Set the parent application‘s Destination Type to .EXE in the Application Properties dialog. 
Typically, an .EXE calls .DLLs, however, a.DLL may call other .DLLs. 
1. Open the parent application. 
2. Select the Properties tab from the Application Tree. 
3. In the Application Properties dialog, choose Executable(.EXE) from the Destination Type drop-down list. 
 
 
Setting the Project‘s Output Type is equivalent to setting the Application‘s Destination Type and vice versa. 
 
 
Set the Parent Application’s Link Mode to Dll 
The parent application‘s Link Mode should be set to DLL in the Project Properties dialog. This allows the .EXE to link in 
Clarion external functions at run-time from C70RUNX.DLL. 
1. Open the parent application. 
2. Choose Project  Project Options from the menu. 
3. In the Application tab, choose Dll from the Link Mode drop-down list. 


---

IDE User's Guide 
268 
 
 
 
If you are not making your own .DLLs, that is, if there is only one .APP file, then you are ready to make your .EXE plus 
.DLLs. Skip to the last step in this section, Make and Run Your .EXE Plus .DLLs. 
 
 
Generate Global Data and ABCs EXTERNAL 
 
 
If your application‘s .DLLs use your application files, the FILE definitions and all Global variables must be declared in a 
.DLL (not the .EXE) and exported. 
 
 
Generate the parent application‘s global data and ABC Library declarations with the EXTERNAL attribute. This allows the 
ABC Library objects, the GlobalRequest and GlobalResponse variables, plus global variables you define to be shared 
between local and external functions. 
Open the parent application. 
1. Choose the Properties tab from the Application Tree, and press the Actions button. 
2. In the Global Properties dialog, check the Generate template globals and ABCs as EXTERNAL box. 
3. Exit the Global Properties and open the Data / Tables Pad (F12). 
4. In the Global Data dialog, press the Change button. 
5. In the Field Properties dialog, select the Attributes tab. 
6. In the Storage Class group, check the EXTERNAL-and DLL check boxes. 
7. Repeat 5 through 7 for each global data item. 
 
 
Make the DLLs 
Make and test your .DLL application just as you would any other application. Note the name of your .DLL and it‘s 
procedures because you will reference these names in your parent application. 
Typically one of the .DLLs (the "Data DLL") contains file declarations and ABC Library objects only, with no other 
procedures. We recommend this configuration because it is easy to set up and to maintain. If needed (your system uses 
more than one data dictionary), you can make a separate DLL for each data dictionary, and a separate DLL for the ABC 
Library objects. 
When you are finished testing, remake each DLL application with the following settings to create a DLL file to link into the 
parent EXE at runtime. 
1. Choose the Properties tab from the Application Tree. 
2. Choose Dynamic Link library(.DLL) from the Destination Type drop-down list. 
Choosing a Destination Type of .DLL automatically exports (makes public) each procedure in the application. 
To optimize performance, export only the procedures called by another executable. 
3. In the Procedure Properties dialog, clear the Export Procedure box for each procedure not called externally. 
Procedures that are only called within the .DLL application need not be exported. 
 
Set the DLL Application’s Link Mode to DLL 
Set the .DLL application‘s Link Mode to DLL in the Project Properties Application dialog. This lets the .DLL link in Clarion 
functions at run-time from C70RUNX.DLL. 


---

User's Guide and Lessons 
269
 
 
 
1. Choose Project  Project Options from the menu. 
2. In the Application tab, choose Dll from the Link Mode drop-down list. 
3. Choose Build  Build Solution from the menu. 
 
Add the DLL modules to the Parent Application 
The following steps tell your parent application that some external procedures are called from a particular .DLL. 
1. Open the parent application. 
2. Choose Application  Insert Module from the menu. 
3. In the Select Module Type dialog, choose ExternalDLL. 
When you make a .DLL with Clarion, you also generate a corresponding stub .LIB. The linker links the stub .LIB at 
compile time so your application can call the .DLL at run-time. 
4. In the Module Properties dialog, press the Module Name ellipsis button to select the stub LIB (or type the LIB 
name) that corresponds to the .DLL, then press OK. 
 
 
Add the External Procedures to the Parent Application 
1. Open the parent application. 
2. Press the New Procedure button. 
3. In the New Procedure dialog, type the name of the external procedure then press OK. 
4. In the Select Procedure Type dialog, select External. 
This opens the Procedure Properties dialog. 
The Files, Procedures, Formulas, and Extensions buttons on this dialog are not meaningful for external procedures 
and you should ignore them. 
5. In the Module Name drop-down list, press the Module Name ellipsis button to select the stub LIB (or type the LIB 
name) that corresponds to the .DLL, then press OK. 
 
 
Make and Run Your EXE Plus DLLs 
1. Open the parent application. 
2. Choose Debug  Make and Run All from the menu. 
The Application Generator and the Project System generate source code, then compile and link the .EXE plus .DLLs 
based on: 
• 
Application Properties‘ Executable(.EXE) Destination Type 
• 
Project Editor—Global Options .EXE Target Type 
• 
Project Editor—Global Options Standalone Run-Time Library 
• 
The .DLL Modules and external procedures you inserted into your application tree. 


---

IDE User's Guide 
270 
 
 
Hiding the Clarion Run-time Library 
Making a one-piece .EXE hides the Clarion run-time Library within the .EXE. You can also hide the run-time Library by 
linking it into another .DLL as follows: 
 
 
Set the Parent Application’s Destination Type to .EXE 
The parent application‘s Destination Type should be set to Executable(.EXE) in the Application Properties dialog. The 
parent application is the one whose procedures are not called by any other application‘s procedures. 
1. Open the parent application. 
2. Select the Properties tab from the Application Tree. 
3. In the Application Properties dialog, choose Executable(.EXE) from the Destination Type drop-down list. 
 
 
Setting the Project‘s Output Type is equivalent to setting the Application‘s Destination Type and vice versa. 
 
 
Set the Parent Application’s Link Mode Library to CustomDLL 
The parent application‘s Link Mode should be set to CustomDLL in the Project‘s Application dialog. This tells the .EXE to 
link in Clarion external functions at run-time from a .DLL other than C70RUNX.DLL. 
1. Open the parent application. 
2. Choose Project  Project Options from the menu. 
3. In the Application tab, choose CustomDll from the Link Mode drop-down list. 
 
 
Link Mode in this context automatically includes all file drivers used by your application! 
 
 
If your application‘s .DLLs use your application files, the FILE definitions and all Global variables must be declared in a 
.DLL (not the .EXE) and exported. 
 
 
Generate Global Data and ABCs EXTERNAL 
Generate the parent application‘s global data as EXTERNAL. This allows the GlobalRequest and GlobalResponse 
variables, plus global variables you define to be shared between local and external functions. 
1. Choose the Properties tab from the Application Tree, and press the Actions button. 
2. In the Global Properties dialog, check the Generate template globals and ABCs as EXTERNAL box. 
3. Exit the Global Properties and open the Data / Tables Pad (F12). 
4. In the Global Data dialog, press the Change button. 
5. In the Field Properties dialog, select the Attributes tab. 
6. In the Storage Class group, check the EXTERNAL-and DLL check boxes. 
Repeat 5 through 7 for each global data item. 


---

User's Guide and Lessons 
271
 
 
Make the DLL Containing Clarion’s Run-time Functions 
1. Choose File  New  Solution, Project or Application from the menu. 
2. In the New Project dialog, select the Clarion for Windows category and the Application Quick Start. 
3. In the Name field, type the name of the application. 
4. Press the Create button. 
5. The Application Properties dialog appears. 
6. If applicable, select a data dictionary. 
7. Choose Dynamic Link Library(.DLL) from the Destination Type drop-down list and press OK. 
 
 
Set the DLL Application’s Link Mode to LIB 
1. Choose Project  Project Options from the menu. 
2. In the Application tab, choose LIB from the Link Mode drop-down list. 
3. Choose Build  Build Solution from the menu. 
This links the Clarion functions into your .DLL at compile time so that they can eventually be linked into your .EXE at run- 
time. It also generates a Module Definition file (.EXP) for your .DLL. You edit the .EXP file in the following step to export 
the run-time functions from your .DLL. 
 
 
Export the Clarion Run-time Functions 
1. Open the parent application. 
2. Choose Build  Build Solution from the menu. 
Because the run-time functions have not been exported, the linker generates an "unresolved" error for each function. 
Expect several hundred to one thousand plus error messages, depending on your application. 
In the following steps we use the Clarion Text Editor to convert the error messages into EXPORT statements. You may 
use any text editor for this purpose. 
3. DOUBLE-CLICK in the Errors Pad to open the Text Editor. 
4. Delete all messages except the "...function is unresolved..." messages. 
5. Choose Search  Replace from the menu. 
6. In the Find what field, type is unresolved in file <filename.ext>. 
Replace <filename.ext> with the filename and extension in the first message. 
7. In the Replace with field, type an ampersand and a question mark with no spaces, like this: @?. 
8. Press the Replace All button. 
This converts the error messages for file <filename.ext> into EXPORT statements. Repeat steps 5 through 8 until all the 
...function is unresolved... messages are converted. 
9. Delete any duplicate statements. 
Select all the statements and copy them to the clipboard, then paste them into a word processor or spreadsheet that has 
sort capabilities. Sort the statements so that duplicate statements appear together, then delete the duplicates. Select all 
the remaining statements, copy them to the clipboard and save your work. 
10. Insert the EXPORT statements into the export file (.EXP) for the .DLL application in the following steps. 
11. If you have not already done so, choose Save and Close from the menu to exit the Text Editor. 
12. Choose File  Open from the menu. 


---

IDE User's Guide 
272 
 
 
13. In the File Name field, type *.exp, then press ENTER. 
14. Select the .EXP file associated with your .DLL (not your parent application), then press OK. 
This opens the .EXP file with the Text Editor. 
15. Scroll to the end of the file then click the mouse to set the insertion point. 
16. Choose Edit  Paste from the menu. 
 
 
You can modify the .EXP file by embedding text in .EXP related Global Embed points. 
 
 
Make the DLL Application with the Exported Functions 
1. Open the .DLL application. 
2. Choose Build  Build Solution from the menu. 
This links the Clarion run-time functions into your .DLL and exports them so they can be called at run-time by your .EXE. 
 
 
Make the Parent Application 
1. Open the parent application. 
2. Choose Project  Make and Run All from the menu. 
Now that the Clarion run-time functions are exported, the linker resolves calls to those functions and issues no 
more unresolved messages. 
 
 
Making LIBs and DLLs for Other Environments 
Unlike most non-Clarion development tools (Delphi, PowerBuilder, Visual C++, Visual Basic, etc.), Clarion generates 
executables that use register based parameters. Since Clarion uses register based parameters and these other tools do 
not, when making DLLs for other tools, you must prototype your exported Clarion procedures with the C or PASCAL 
attribute, depending on the calling environment. See C and PASCAL calling conventions in the core help for more 
information. 
Non-Clarion environments generally cannot link Clarion created LIBs because of memory model incompatibility. However, 
they can link the stub LIBs associated with Clarion DLLs. 


---

User's Guide and Lessons 
273
 
 
 


---

IDE User's Guide 
274 
 
 
 
The Debugger 
 
Using the Clarion Debugger 
Overview 
Clarion ships a 32-bit debugger for your 32-bit applications. It is a powerful tool for finding and diagnosing errors in your 
applications. You can examine source code and data as your program executes, and exercise complete control over 
your program‘s execution. 
This chapter tells you how to: 
• 
Prepare your projects for debugging. 
• 
Start the debugger. 
• 
Customize the debugger‘s operation to your work environment. 
• 
Monitor your program‘s execution and check its state at specific points by setting breakpoints and watch 
expressions. 
 
 
The Debugging Process 
The debugger is very flexible, quite complex, and there are many windows, options, and features available. This overview 
of the debugging process suggests a general sequence of steps that introduces you to the most important features of the 
debugger with the least amount of confusion. Keep this sequence in mind as you explore the debugger. 
1. Shut down other applications, then start the debugger. 
2. This offers two benefits. First, more system resources are available to your application and the debugger. 
Second, you won‘t lose data from other active applications if a system crash occurs during the debugging 
process. 
3. Load only the source files you need to debug. 
4. Each source file you select becomes a child window in the debugger. The fewer source files you select, the 
less clutter you have on your debugger screen, and the less overhead the debugger must manage. 
5. Set Debug Options. 
6. Take a few minutes to read Setting Debugger Options. Several Options such as Custom Font, Stop on 
dynamic dll load, etc. can make the debugger easier to read and work with. 
7. Set a breakpoint. 
8. Run your application (the debuggee) with Go or Step commands. 
9. Select and arrange the debugger windows. 
10. Many of the debugger windows will be empty until your application stops at a breakpoint. Once your 
application stops, and the windows are populated, they will be more meaningful and easier to understand and 
work with. Iconize or close the windows you don‘t need to see. 
11. Set breakpoints, set watch expressions, and change variable values. 
12. Run your application with Go or Step commands. 
13. Repeat steps 7 and 8 as needed. 
14. Exit your application (debuggee). 


---

User's Guide and Lessons 
275
 
 
Preparing Your Projects for Debugging 
The Project System lets you set the debug options for your application in the Global Options dialog. To make your 
executable (.EXE or .DLL) suitable for debugging: 
 
 
Generate Global Debug Information 
1. Create your project file, and make it the current project (the Project System chapter explains how). 
2. Choose Project  Project Options to view the Project Properties dialog. 
3. Set the Configuration drop down to Debug 
4. Select the Compiling tab, then choose Full from the Debug Mode drop list. 
The compiler generates the debug information into the .EXE or .DLL. 
5. Optionally check the Add Line Number information to map file box. 
Line numbers are automatically available to the Clarion debugger, however, if you are using another debugger, checking 
this box will make line numbers available to it. 
6. Close the Project Properties, and press the Save button on the IDE toolbar to save your project changes. 
7. Choose Build  Set Configuration  Debug from the IDE Menu. 
8. Press the Build Solution button on the toolbar to compile and link the application. 
The application now includes the information the debugger needs. 
 
Generate Local Debug Information 
You can also turn on debugging information for a single module in the project. This reduces the overhead for the 
debugger. To do so, follow the steps above for Global Options, except choose None from the Debug Mode drop list. Then 
follow the steps below: 
1. Choose View  Solution Explorer to view the Solution Explorer dialog. 
2. Select only the source module you need to debug, and then press the Properties button. 
3. In the Properties Pad, choose Full from the Debug information drop list. 
4. Press the Build Soution button on the toolbar to compile and link the application. 
This includes debug information for that module only. 
Locating Page Faults (GPF) 
The debuggers can identify a specific line of code where your program is crashing. Make the debugger the system 
debugger (see Setting Debugger Options), then run your program. When it crashes, select debug to invoke the debugger 
to take you to the offending line. 


---

IDE User's Guide 
276 
 
 
Starting the Debugger from a Popup Menu 
When you start the debugger from Windows, you should take steps to set the proper working folder—usually the directory 
that contains the debuggee. For example, create a Windows shortcut that sets the "Start in" folder. 
Or you can use a program like "RegEdit" to make Windows registry entries to start the debugger by right-clicking on the 
.exe to debug. Here are some example registry entries that start the debugger with the appropriate working directory: 
 
 
[HKEY_CLASSES_ROOT\exefile\shell\32bit Debugger] 
[HKEY_CLASSES_ROOT\exefile\shell\32bit Debugger\command] 
@="C70dbx.exe c:\\C70\\bin\\Clarion7.red c:\\C70\\bin\C70ee.ini %1" 
 
 
[HKEY_CLASSES_ROOT\exefile\shell\Restart Debugger] 
[HKEY_CLASSES_ROOT\exefile\shell\Restart Debugger\command] 
@="C70db.exe /r" 


---

User's Guide and Lessons 
277
 
 
 
Debugger Lesson 
 
Clarion ships with a standalone 32-bit debugger; C70db.exe. In Windows there exists the concept of a system "debugger". 
When you install the Clarion debugger as the system debugger, it uses the API function DebugActiveProcess() to connect 
to the process that caused the debugger to execute. 
 
 
Lesson 
 
 
This lesson uses the ABC Template chain. You must register these templates (ABCHAIN.TPL) before starting the lesson. 
 
 
Prepare Your Program for Debugging 
In this Lesson you will debug the Orders application, installed by default as …\Lessons\Debugger\Orders.APP. We have 
deliberately created a bug in this application. To begin, start Clarion and open the Orders application. 
 
 
In Windows XP, the Lessons folder is found in: 
C:\Documents and Settings\All Users\Documents\SoftVelocity\Clarion7\Lessons 
 
 
In Vista and Windows 7: 
C:\Users\Public\Documents\SoftVelocity\Clarion7\Lessons 
 
 
To debug your program with the debugger, you must tell the compiler to generate debug information. Use the Project 
Editor to establish this setting. (32-bit with debug information). 
1. Open the Orders application with Clarion. 
2. From the IDE menu, choose Project  Project Options to open the Project Properties. 
3. Verify that the Configuration drop down list is set to Debug. 
4. On the Compiling tab, select Full from the Debug Mode drop-down list. 
5. Close the Project Properties dialog and Save your project changes if needed. 
 
 
Identify the Bug 
We have deliberately created a bug in the Orders application. To see it: 
1. Set the Build Version to Debug (Choose Build  Set Configuration  Debug) 
2. Press the 
 button to make and run the Orders program. 
3. From the Orders program menu, choose Browse  Browse Customer Information File. 


---

IDE User's Guide 
278 
 
 
 
 
This opens the customer list. 
4. With the customer list open, and using your mouse, highlight a customer in the middle of the list and click the 
down arrow button at the bottom of the scroll bar 
 to scroll down one row. 
The list scrolls up! Using the arrow keys, the down arrow does nothing. Page Up, Page Down, Ctrl + Page Up, Ctrl + Page 
Down all work as expected. 
You‘ve identified the bug: it is in the BrowseCustomer procedure and it only occurs when scrolling down. 
5. Close (exit) the Orders program. 
The Clarion environment gains focus. 
 
Start the Debugger 
To start the debugger: 
1.   From the Clarion environment, press the 
 button to start the debugger. 
You may want to shut down other applications to conserve resources because you will be running the Clarion 
environment, the debugger, plus the Orders program in addition to any others. 
 
 
You can run the debugger independent of the development environment to save even more resources: run C70db.EXE. 
When you invoke the debugger, the Clarion IDE will re-make the project if needed, and then run the degugger. The 
debugger opens the Globals window, the Procedures window, the Stack Trace (local variables) window, and a starting 
source file. 


---

User's Guide and Lessons 
279
 
 
 
 
 
 
The debugger also opens the Trace window and the Disassembly window in the iconized state. 
 
 
Arrange the Debugger Windows 
All of the debugger windows are movable and resizable. So you should arrange the windows so that they are easy for you 
to work with. 
1. Maximize the debugger. 
You will usually want to see several debugger windows at once, so you need as much screen space as possible. 
2. In the Procedures window, click BROWSECUSTOMER to open the source window for the BrowseCustomer 
procedure. 
 
 


---

IDE User's Guide 
280 
 
 
 
 
The debugger opens a source code window for ORDER002.CLW, the source module containing the BrowseCustomer 
procedure. 
 
 
CLICK on the procedure or module headers to sort the respective columns in ascending order. 
The Procedures window shows all the procedures and routines for the program you are debugging. CLICK on any 
procedure to see the source code for that procedure. 
3. Reposition and resize the windows so they are easy for you to work with. 
We recommend a layout that shows lots of source code, shows as many local variables as possible (in the Stack Trace 
window), and a watch window. You will need to adjust these windows according to your tastes. 
 
 
 
 
Setting BreakPoints 
A breakpoint tells the debugger that an application should break (pause execution) at a certain point. 
Breakpoints allow you to suspend execution where and when you need to. Rather than stepping through your code line- 
by-line or instruction-by-instruction, you can allow your program to run until it hits a breakpoint, then start to debug. This 
speeds up the debugging process enormously. 
 
 
You want to suspend (or break) the program at the point the bug occurs, and then look for the cause of the problem, 
usually in the form of incorrect variable values or incorrect execution sequence. Recall the bug is associated with scrolling 
downward. To set the breakpoint: 


---

User's Guide and Lessons 
281
 
 
1. CLICK on the ORDER002.CLW window to give it focus. 
2. Press the F key to open the Search for dialog. 
 
 
A right-click on the source code window displays a popup menu of all the source window functions and their keyboard 
shortcuts. 
3. In the Search for dialog, enter scrollone, and then press the OK button. 
You will land on the ScrollOne method declared for the BRW1 class. Press the A key to find scrollone again. This time, 
you land on the label for the code of this method. 
 
 
 
 
This method is a likely location for the breakpoint you need. 
 
 
Searching is not case sensitive. 
 
 
4. CLICK on the first executable statement after the code statement: 


---

IDE User's Guide 
282 
 
 
 
IF LOC:Flag 
 
 
Although you can set a breakpoint on routine and method labels, you may get unexpected results. We recommend setting 
breakpoints only on executable statements. 
 
 
5. Press the B button in the lower right section of the source window or press the B key to set a breakpoint on this 
statement. 
You may also right-click and select Set Breakpoint from the popup menu. Or you may double-click the line. If you repeat 
any of these actions on the same line, it will clear the breakpoint. 
The debugger displays breakpoints in red; however, because this is also the currently selected line (green), the breakpoint 
appears yellow until you move off the current line. 
Debug the Program 
The debugger is now set to suspend program execution at the first statement in the BRW1.ScrollOne method. To debug 
the program: 
1. Press the G button or press the G key to start the Orders program. 
The Orders program begins execution. Its main window opens on top of the debugger. 
2. Choose Browse  Browse Customer Information file. 
This opens the customer browse list. 
3. With the customer list open, select a customer halfway down the list and click on the down arrow button 
 to 
scroll down one row. 
The debugger detects the breakpoint, suspends the Orders program, and displays the breakpoint statement (with a yellow 
background). 
4. Click on the Source window to give it focus, and click on the T button (or press the T key) to execute the next 
statement. 
The debugger executes a single statement, then displays the next source statement to execute with a green background. 
5. Repeat step 4 until after the PARENT.ScrollOne(Event) executes. This calls an ABC method, 
BrowseClass.ScrollOne in ABBROWSE.CLW: 
 
 
BrowseClass.ScrollOne PROCEDURE(SIGNED Ev) 
## CODE
SELF.CurrentEvent = Ev 
IF Ev = Event:ScrollUp AND SELF.CurrentChoice > 1 
SELF.CurrentChoice -= 1 
ELSIF Ev = Event:ScrollDown AND | 
SELF.CurrentChoice < SELF.ListQueue.Records() 
SELF.CurrentChoice += 1 
ELSIF ~SELF.FileLoaded 
SELF.ItemsToFill = 1 
SELF.Fetch(CHOOSE(Ev = EVENT:ScrollUp,1,2)) 
END 


---

User's Guide and Lessons 
283
 
 
 
When you step through this method, only the first condition executes causing the current choice to move up one line. 
 
 
Examine Variable Values 
You can surmise that the above IF condition must be true in order for the customer list to scroll up one row, and the ELSIF 
condition must be true in order for the customer list to scroll down one row. You can examine (and modify) the values of 
the variables within the ELSIF condition to test this theory—EVENT:ScrollUp must be the event passed to this method. 
Also, SELF.CurrentChoice is greater than one, meaning the highlight row is not the first in the list box. 
To examine and edit the variable values: 
1. Press the G button or press the G key to continue executing the Orders program. 
The Orders program gains focus and continues execution where it left off. 
2. Again, click on the down arrow button to scroll down one row. 
Again, the debugger detects the breakpoint, suspends the Orders program, and displays the breakpoint statement. 
3. CLICK in the Stack Trace window, or choose Window  Stack Trace, or restore the minimized Stack Trace 
window. 
 
 
 
 
4. In the Stack Trace window, RIGHT-CLICK on the EVENT variable. 
This shows a popup menu. Select Watch Variable. A new window appears labeled Watch. Add the LOC:Flag variable in 
the same manner. 
The watch window shows the label of the variable on the left and its value on the right. The value of EVENT is 4. The 
value of LOC:Flag is currently 3. 
You can surmise that EVENT is getting the wrong value from LOC:Flag. In the next section, we‘ll test this theory by 
changing the value of LOC:Flag to a different number, for example, 4. 
 
 
Edit Variable Values 
1. In the Stack Trace window, RIGHT-CLICK on LOC:Flag, then choose Edit variable to open the Edit dialog. 
2. In the Edit dialog, enter 4, then press OK. 
The debugger changes the value of LOC:Flag to 4. Now you can continue execution of the Orders program to see if it 
scrolls properly. 
3. With focus in the Source window, press the T button or press the T key to execute the next statement. 


---

IDE User's Guide 
284 
 
 
 
The debugger displays the next source statement to execute with a green background. 
4. Repeat step 3 until the first statement in the BrowseClass.ScrollOne method executes. 
Notice that the ELSIF conditional statements now executes. This is because the ELSIF condition is now true: Ev is equal 
to EVENT:ScrollDown, and the highlighted row is less than SELF.ListQueue.Records. 
5. Press the G button or press the G key to continue executing the Orders program. 
The Orders program continues execution where it left off. 
This time, the customer list scrolls correctly! This confirms the theory that EVENT contains an incorrect value at this point 
in the program. 
 
 
 
Examine Global Variable Values 
Often you will want to examine global variables, record buffer values, and the values of Clarion‘s built-in "Library State 
functions (ACCEPTED(), EVENT(), ERRORCODE(), etc.). 
To examine and edit these global variable values: 
1. Again, press the down arrow key to scroll down one row. 
Again, the debugger detects the breakpoint and suspends the Orders program. 
2. CLICK in the Globals window, or choose Window  Globals. 
3. In the Globals window, click on the ( + ) beside ORDERS (near the bottom of the Globals list) to expand the list of 
global variables for the ORDERS module. 
4. In the Globals window, click on the ( + ) beside CUSTOMER$CUST:RECORD to expand the list of customer 
record buffer fields. 
5. In the Globals window, click on the ( + ) beside CUST:CONTACT to see the value of each byte in the 
CUST:CONTACT field. 


---

User's Guide and Lessons 
285
 
 
 
 
 
 
The Globals window shows global variables, record buffers, and Library States. The labels are on the left and the values 
are on the right. 
 
 
You may also edit global variables the same way you edited local variables. 


---

IDE User's Guide 
286 
 
 
Watch Selected Variables 
The Watch window lets you pick specific variables (local, global, or both) and "Library States" to monitor during the 
debugging process. That is, rather than searching through the Stack Trace window and the Globals window with each 
debugging cycle, you can add the variables to the Watch window and examine all the pertinent values in one place. 
To place variables in the Watch window: 
1. In the Stack Trace window or the Globals Window, RIGHT-CLICK on an item (variable or Library State), then 
choose Watch variable. 
This opens the Watch window and places the selected item in the window. 
 
2. Repeat step 1 for all the pertinent variables and Library States. 
 
 
Close the Debugger 
1.   In the debugger, choose File  Exit. 
The debugger automatically shuts down the debuggee (the Orders program) too. 


---

User's Guide and Lessons 
287
 
 
 
Debugger Options 
 
Starting the Debugger 
The debugger runs as a separate application, but you can start it either from the development environment, or directly 
from Windows. Starting from Windows, with the development environment unloaded, means more system resources are 
available for your application and the debugger. The debugger can also debug multiple programs at the same time. 
 
 
Starting the debugger from the development environment 
1. Choose Project Debug Project or press the 
 button on the toolbar. 
The environment checks the project information for options and settings and starts the debugger. 
or... 
2. Compile and link your application by pressing the 
 button, then, with the compile results dialog still open, 
press the Debug button. 
 
 
 
Starting the debugger from the environment sets the working directory to the debuggee program‘s directory. This ensures 
the debugger will use any applicable configuration (.INI) files and redirection (.RED) files. 
 
 
Start the debugger from Windows 
When you start the debugger from Windows, you should take steps to set the proper working directory—usually the 
directory that contains the debuggee. For example, create a Windows shortcut that sets the "Start in" directory. 
 
 
1. With your preferred method (Start menu, Explorer, Program Manager, etc.) start C70db.EXE. 
2. Choose File  File to Debug, then choose an .EXE file in the Windows file dialog. 
 
 
When debugging, run only the debugger and the debuggee programs. By doing so, you won‘t lose data in other 
applications if a problem occurs during the debugging process. 


---

IDE User's Guide 
288 
 
 
Loading the Source Files 
The source associated with the debuggee program is automatically loaded and is available for your examination. 
However, you may specify any additional source files you want the debugger to manage. 
To specify additional source files 
1. Choose Window  Source. 
This opens the Select Source dialog. 
2. Highlight a source file then press the OK button. 
Repeat for each source file you want to debug. 
 
Setting Debugger Options 
The debugger Setup menu provides two choices: Options and Install as System Debugger. Use Options to customize 
the debugger. 
 
 
Options 
Choose the Setup  Options command to access the following options: 
Redirection File 
The debugger uses the redirection file to find project components. A redirection file is optional and follows the 
same conventions as the Project redirection file. 
Clarion Run-time 
Specifies the Clarion dynamic link library (DLL) linked into the .EXE being debugged. 
 
 


---

User's Guide and Lessons 
289
 
 
Stop At Program Entrypoint 
Tells the debugger to stop the debuggee program at its entrypoint upon initial program load. Initial program load 
(and start) occurs when you choose File   File to Debug and select the .EXE file from the Windows file dialog. 
Checking this option lets you survey the status of your program at the earliest possible point of execution without 
explicitly setting a breakpoint. 
Stop At First Source Line 
Tells the debugger to stop the debuggee program at its first line of executable code upon initial program load. 
Initial program load (and start) occurs when you choose File   File to Debug and select the .EXE file from the 
Windows file dialog. 
Give Debugger Focus When Debuggee Suspended 
When the debuggee is suspended at a breakpoint, focus immediately returns to the debugger. 
Open Procedure Window on Startup 
Tells the debugger to open the Procedures In window on debugger startup. See Debugger Windows. 
Stop on dynamic DLL load 
Tells the debugger to suspend debuggee execution when a dynamic DLL load (demand load) is detected. This 
gives you the opportunity to examine the newly loaded code and set breakpoints before anything else happens. 
Allow stepping into Kernel 
Lets the debugger examine the Windows Kernel32.dll. This setting could cause system lock ups, so use with 
care. 
Show unmangled procedure names 
Check this box to display procedure names as they appear in source code. Clear the box to show the mangled 
names that allow procedure overloading. 
Custom Font 
Check this box to set a custom font to use during the debugging session. A Font Dialog window is provided. Press 
the ellipsis button at any time to modify the existing font. The default value is your System Font. 
 
 
Install as System Debugger 
Installs the debugger as the system debugger. In this configuration, the debugger is available whenever a program 
crashes. This is shown with the Debug button on the GPF dialog. 
 
 
Debugger Windows 
The debugger contains a collection of child windows that track information about the debuggee program. These windows 
are: 
• 
The Procedures window 
• 
The Globals window 
• 
The Stack Trace window 
• 
The Watch window 
• 
The source window 
• 
The disassembly window 
• 
The memory window 


---

IDE User's Guide 
290 
 
 
 
After you start the debugger, take a moment to arrange the various windows in a format that is comfortable for you. 
Position the most important windows where you can quickly scan for the information you need. Iconize or close unneeded 
windows. Use the Window menu to open windows of special interest. 
By default, the debugger initially opens three windows: the Procedures window, the Globals window, the Stack Trace 
window, and the source window. 
 
 
The Procedures window 
The Procedures window lists the procedures in the debuggee and their associated source modules. CLICK on a 
procedure name to display its associated source or assembler code. 
Use the Procedures window to navigate through your source code. 
 
 
The Globals window 
The Globals window displays the current value of each global variable, as well as various Library States (Clarion runtime 
library functions such as ACCEPTED, EVENT(), FIELD(), etc.). 
The Globals window contains expandable tree controls, so you can hide variables you don‘t want to see. Variables with a 
( + ) button are expandable by clicking on them. Variables with a ( - ) button are contractible by clicking on them. 
 
 
RIGHT-CLICK on a variable to change its value. 
 
 
The Stack Trace window 
The Stack Trace window shows the current register and local variable values. The variable name is on the left and its 
value in decimal format then in hexadecimal format is on the right. This information is for the current thread only. 
The Stack Trace window contains expandable tree controls, so you can hide variables you don‘t want to see. Variables 
with a ( + ) button are expandable by clicking on them. Variables with a ( - ) button are contractible by clicking on them. 
The Stack Trace window has a step locator: type a letter to search for variables beginning with that letter. 
The Stack Trace window has the following special functionality: 
RIGHT-CLICK on a variable to change its value. RIGHT- 
CLICK on a variable to monitor its value. 
RIGHT-CLICK on a call to locate its corresponding source line or assembler line. This is the option you use to 
quickly find a line of source that caused a GPF. 
RIGHT-CLICK on a register to examine the memory pointed to by the register. 
 
 
The Watch window 
The Watch window lets you pick specific variables (local, global, or both) and "Library States" to monitor during the 
debugging process. That is, rather than searching through the Stack Trace window and the Globals window with each 
debugging cycle, you can add the variables to the Watch window and examine all the pertinent values in one place. 
To place variables in the Watch window: in the Stack Trace window or the Globals window, RIGHT-CLICK on an item 
(variable or Library State), then choose Watch variable. This opens the Watch window and places the selected item in 
the window. 


---

User's Guide and Lessons 
291
 
 
The Source window 
Displays a source module. There may be multiple source windows open showing different source modules. The title 
bar shows the module name. The cursor is green. This cursor simply marks a line for your use. It may or may not mark 
the program‘s current position. Breakpoint lines are red. If the current line is also a breakpoint line, it is yellow. 
 
 
Use the source window‘s task bar buttons to control the execution of the debuggee and to set and remove breakpoints. 
The taskbar buttons correspond to the options on the popup menu which can be accessed by right-clicking anywhere in 
the window. See Running the Program below for a description of each command. 
 
 
RIGHT-CLICK anywhere in the window to access the popup menu. 
 
 
The Disassembly window 
Displays assembler code. There may be multiple disassembly windows open. The title bar shows the .EXE name. The 
cursor is green. This cursor simply marks a line for your use. It may or may not mark the program‘s current position. 
Breakpoint lines are red. If a line is both the cursor and a breakpoint line, it is yellow. 
Blue text has a corresponding source statement associated with it. Moving the cursor to a line with blue text moves the 
cursor in the source window to the corresponding source line. 
Use the disassembly window‘s task bar buttons to control the execution of the debuggee, and to set and remove 
breakpoints. The taskbar buttons correspond to the options on the popup menu which can be accessed by right-clicking 
anywhere in the window. See Running the Program below for a description of each command. 
The disassembly window has two vertical scroll bars. The left bar scrolls 64K of code at a time, the right bar scrolls 1 
display line at a time. 
RIGHT-CLICK anywhere in the window to access the popup menu. 
 
 
The Memory window 
Displays memory allocated to the debuggee. The title bar shows the .EXE name. The memory window has two vertical 
scroll bars. The left bar scrolls 64K of memory at a time, the right bar scrolls 1 display line at a time. 
 
 
Setting Breakpoints 
Normally, when debugging an application, you identify a small part of the program that produces incorrect output, or 
crashes. The debugging process for this situation will probably require running just that part of the program, and stopping 
it at one or more points to check its status. 
Breakpoints allow you to automatically halt execution at the line of code at which (or near which) you think the problem 
occurs. Your program runs up to the breakpoint, then halts and turns control back to the debugger. You can then check 
the contents of variables to identify the cause of the problem, and step through from that point on. 
When you set a breakpoint, the line where the breakpoint occurs appears in red in the source and disassembly windows. 
Breakpoints appear yellow when you first create them because both the red breakpoint color and the green cursor color 
are present. 
 
 
To set a breakpoint 
1. Navigate to the source or assembler code where you want the debugger to break. 
CLICK on a procedure name in the Procedures window to jump to that procedure. Or RIGHT-CLICK in the source window 
to access the Find command to find a text string. 
2. Highlight the line of code to break on. 


---

IDE User's Guide 
292 
 
 
3. Press the breakpoint (B) button. 
 
 
The breakpoint button acts as a toggle. Pressing it a second time removes the breakpoint. 
 
 
Running the Program 
The taskbar buttons on the source windows and the disassembly windows control execution of your program. Similar 
taskbars appear on each source and disassembly window. It makes no difference which taskbar you use. Program 
execution always continues from the point at which it stopped. 
Alternatively, you can use the popup menus available in each window. The taskbar commands are duplicated on the 
respective popup menus of the source and disassembly windows. RIGHT-CLICK anywhere in the window to access the 
popup menu. 
 
 
Go (G) 
Advances the program from its current position to the next breakpoint. If no breakpoints are encountered, the program 
keeps running. 
 
 
Step Assembler (S) 
Advances the program from its current position, one line of assembler code at a time. 
 
 
Step Over Assembler (O) 
Advances the program from its current position to the next assembler breakpoint, without executing any statements in 
between. 
 
 
Step Source (T) 
Advances the program from its current position, one line of source code at a time. 
 
 
Step Over Source (E) 
Advances the program from its current position to the next source breakpoint, without executing any statements in 
between. 
 
 
Go Cursor (C) 
Advances the program from its current position to the cursor. This has the effect of making the cursor a temporary, one- 
time-only breakpoint. 
 
 
Locate Line/Offset ( L ) 
Advances the cursor (not the program) to the line number (or offset for assembler) you specify. 
 
 
Find (F) 
Advances the cursor (not the program) to the source string you specify (source window only). 


---

User's Guide and Lessons 
293
 
 
Find Again (A) 
Advances the cursor (not the program) to the source string specified for the previous Find command (source window 
only). 
 
 
Editing Variables at Run Time 
 
 
Examining Variable Values 
The best way to examine variable values at run-time is to look for them in either the Globals window or the Stack Trace 
window. Global variables are shown in the Globals window and local variables are shown in the Stack Trace window in 
both decimal and hexadecimal format. 
Both windows contain tree controls, so that you can expand only the variables you want to examine. Controls 
containing a ( + ) are expandable by clicking on them. Controls containing a ( - ) are contractible by clicking on them. 
The Stack Trace window also shows machine register values and locates the memory area the register points to. RIGHT- 
CLICK the register, or highlight it and press enter, to examine the correct memory location in the memory window. 
 
 
Changing Variable Values 
RIGHT-CLICK on a variable, or highlight it and press enter, in either the Globals window or the Stack Trace window to 
change its value. 


---

IDE User's Guide 
294 
 
 
 
Index 
ADD 
Templates .................................................................... 205 
## ADD ............................................................................. 205
ADO application .......................................................... 216 
Advanced Topics ............................................................. 3 
## APPLICATION
Customizing................................................................. 205 
## APPLICATION............................................................. 205
Application Design......................................................... 79 
Application Generator ...............................................3, 77 
Clarion Code 
Writing ............................................................................. 3 
Clarion Code ................................................................... 3 
Color .............................................................................. 75 
Customizing 
Application ................................................................... 205 
Customizing................................................................. 205 
Database Design.....................................................15, 17 
Debugger Lesson ........................................................ 274 
Debugger Options ....................................................... 284 
Deployment Strategies ................................................ 253 
Development ............................................................... 253 
Dictionary ........................................................................ 3 
Dictionary Editor .............................................................. 3 
Environment Overview .................................................... 3 
EXE Plus DLLs ............................................................ 253 
Explore 
Form ............................................................................ 156 
Report Procedure ........................................................ 165 
Explore ........................................................................ 156 
Explore ........................................................................ 165 
fields .............................................................................. 15 
Form 
Exploring ..................................................................... 156 
Form ............................................................................ 156 
Formula Editor ............................................................. 249 
 
 
Keys .............................................................................. 15 
Lesson ................................................................ 156, 165 
Lessons - Users Guide 
1 - Data Import .............................................................. 28 
Lesson 12 - Advanced Features of Application 
Generator .................................................................... 198 
Lesson 2 - Table Properties .......................................... 30 
Lesson 3 - Column Properties ...................................... 32 
Lesson 4 - Key and Index Properties ............................ 36 
Lesson 5 - Adding Relationships .................................. 39 
Lesson 6 - Trigger Properties........................................ 41 
Lesson 7 - Dictionary Synchronization .......................... 43 
Lesson 8 - Advanced Features ..................................... 59 
Many Relationships ....................................................... 15 
Menus ........................................................................... 71 
Multi-Programmer Development ................................. 253 
## ODBC .......................................................................... 216
One Relationships ......................................................... 15 
One-Piece EXEs ......................................................... 253 
Project System ................................................................ 3 
## RECORDS .................................................................... 15
Relational Database ...................................................... 15 
relationships .................................................................. 15 
Report Designer Lesson ............................................. 158 
Report procedure 
Exploring ..................................................................... 165 
Report procedure ........................................................ 165 
Source Editor .............................................................. 233 
Source Procedure Lesson .......................................... 209 
## SQL ............................................................................. 216
Templates 
Adding ......................................................................... 205 
Templates ................................................................... 205 
Text Editor ................................................................... 233 
Tutorial Contents ............................................................. 3 
Users Guide Conventions ............................................... 1 
Using the Clarion Debugger ........................................ 271 


---

295 
 
 
Index 
 
Window Elements .......................................................... 67 
Writing 
Clarion Code ................................................................... 3 
Writing ............................................................................. 3 
