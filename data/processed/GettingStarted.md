i 
 


---

Table of Contents 
ii 
COPYRIGHT SoftVelocity Inc.  All rights reserved. 
This publication is protected by copyright and all rights are reserved by SoftVelocity Inc.  It may 
not, in whole or part, be copied, photocopied, reproduced, translated, or reduced to any electronic 
medium or machine-readable form without prior consent, in writing, from SoftVelocity Inc. 
This publication supports Clarion.  It is possible that it may contain technical or typographical 
errors.  SoftVelocity Incorporated provides this publication “as is,” without warranty of any kind, 
either expressed or implied. 
 
 
 
 
 
 
SoftVelocity Inc. 
www.softvelocity.com 
 
 
  
 
 
 
Trademark Acknowledgements: 
 
SoftVelocity is a trademark of SoftVelocity Incorporated. 
Clarion is a trademark of SoftVelocity Incorporated. 
All other products and company names are trademarks of their respective owners. 
 
 
 
 
 
 
 


---

Table of Contents 
iii 
Table of Contents 
Table of Contents 
iii 
Getting Started 
3 
Getting Started Lessons 
6 
Exercise One - Create the Dictionary 
8 
Exercise Two - Import Your Data 
10 
Exercise Three – Define your Tables relationships 
14 
Exercise Four - Add a Lookup File 
17 
Exercise Five - Create the Lookup Relationship 
25 
Exercise Six - Setup the Lookup Validity Check 
28 
Exercise Seven - Fine Tuning the Customer and Orders Tables 
29 
Exercise Eight - Generate your Program using the Wizards 
34 
Summary 40 
The Secret of Productivity 
42 
What's Next? 
49 
Index 
50 
Getting Started 
Introduction 
Clarion is an infinitely adaptable environment, written to offer fast solutions at every skill level: 
from the business owner to the enterprise development team. Whatever your level coming in, 
Clarion will help you take control of your company data—more cost-effectively, and up to ten 
times faster than any other product out there today. Here’s why… 
 
Advanced code generator 
Simply point to an existing database, or define a new one, and then use Clarion wizards to 
generate a full-featured business database application with advanced user interface functionality. 
The generated code includes complex features like multi-table joins, user authentication and 
access control, as well as functionality like filtering and sorting and reporting on any combination 
of database tables and records.  
When you need a "business" application to maintain a database, you can literally do the job in 
minutes using Clarion. The key is the database dictionary. If the Application Generator knows 
what files or tables you want in the application, and how they’re related, it can build an 
application. This is true regardless of where the files originated or in what format they are. So all 
you need to do is select one or more files, then indicate (when there are two or more files) the 
type of file relationships. The short Getting Started lessons herein demonstrate just how easy this 
whole process is.   
The Application Wizard can then create a full-featured application using the Clarion default 
application metaphor. We call this the browse-form metaphor, and it extends directly from the 
structure of your database. The application works like this: (1) The end user navigates the 
database—all or part of it, one data file or multiple related data files—by scrolling through a list 


---

Table of Contents 
4 
box, within which each item represents one record. The window in which this takes place is called 
a "browse." (2) The end user selects a specific record in the list to perform an action, such as 
editing the data. This generally occurs in a separate window, in which the database fields appear 
in separate edit boxes.  This is called an update "form." A form may also accept new data. (3) 
Optionally, the end user can look up a value from a related table during form entry. This opens 
another browse in a separate window. The end user can select an item, closing the new window 
and placing the value in the edit box on the form, in one step. This is called a "lookup." 
That’s the most general description. In addition, each browse window, navigable from the toolbar, 
opens on a separate thread with its own record buffer—which provides safer data handling. You 
can select among multiple key orders by CLICKING a tab. DOUBLE-CLICKING a record in the 
list opens an update form, with automatic concurrency checking (support for multi-user 
situations), and optional Referential Integrity constraint support (maintaining your database 
relationships). 
Anybody can do this. It just starts with picking a data file from a list.  
 
It’s a visual development environment 
With Clarion, dropping a control in a window gives you a lot more than other Rapid Application 
Development tools, which typically let you add a user interface control, but then expect you to 
write the code to implement its associated functionality. With Clarion, you add a template, which 
contains the control, and all its required data elements and executable code. That means you 
don’t have to write code—one CLICK places a complete business solution: a user interface 
control, and the code that enables it to do its job.  Moreover, each template has its own user 
interface. When you view the properties for the template, you’ll see an "Actions" tab. By checking 
a box, choosing a dropdown list item, or filling in an edit box, you can customize the behavior of 
the template so that it meets your needs exactly. You’ll set  "actions" for the templates at many 
places in the upcoming lessons.. The lessons that follow in this document introduce you to all of 
the Clarion RAD tools. 
When you use the template interface to specify these behaviors, the Application Generator writes 
the code (Clarion language source code) that implements the behavior for you—and the code it 
writes for you is built from Clarion’s Application Builder Class (ABC) Library, so the code is very 
compact and efficient. Using the templates, you can do an awful lot of customizing without 
actually writing a single line of source code by hand. 
One of the great advantages of the Clarion template system along with the ability to write code by 
hand is that you can ease into the language—as slowly as, as quickly as, as much as, or as little 
as you wish.   
Power users, who may not normally write programs, can easily do this. 
 
It’s a business programming language 
At the language level, you can quickly code an application using Clarion’s fourth generation 
programming language. Clarion has a high level of abstraction, so that it’s very "readable," and a 
compact database grammar, so that you can easily manipulate data with standard language 
functions like ADD, GET, PUT and DELETE. You don’t have to know Clarion to create an 
application… but if you do know how it works, it helps you understand what your applications are 
doing, and that helps you make better applications. One lesson has you write a small amount of 
your own Clarion code into the template-generated source, and another lesson introduces the 
Clarion language at a fully hand-coded level. 
Clarion was designed from the ground up for business programmers. Yet for its relatively quick 
learning curve (as a high-level 4GL) you’ll get blazing performance.  The SoftVelocity compiler 


---

Index 
5 
technology turns all of your code—whether you wrote it or the Application Generator wrote it for 
you—into highly optimized machine code. 
  
No matter which level you intend to work at, you're going to work a lot smarter if you first work 
through all of the lessons all the way to the end. 
 
 


---

Table of Contents 
6 
Getting Started Lessons 
Clarion is a data-centric application development tool. Businesses rely on data. That means 
Clarion is optimized to create business programs. Clarion’s data-centric approach begins with 
the Data Dictionary. 
In Clarion, you can create a Data Dictionary using the Dictionary Editor and import your desired 
business data. You can then create a working application based on that data with the help of the 
Application Wizard—all with no coding required, and in less than 10 minutes.  
We will demonstrate this, and more, in this lesson! 
In this section: 
 
You’ll use the Import Tables Wizard in the Dictionary Editor to import a Customer and 
Orders table. 
 
You’ll define the relationship between two tables in the Dictionary Editor, complete with 
Referential Integrity rules. 
 
You’ll use Clarion’s Application Wizard to create a complete relational database 
application from the same data dictionary. 
 
Finally, you’ll use the Application Generator to add more functionality to the application 
using one of Clarion’s Procedure Wizards. 
 
This should all take about thirty minutes—without any "coding" on your part. By the end of this 
section, you’ll have a complete application for a database containing three related tables. 
Welcome! Let’s get started! 
 
  
Make sure that the Clarion IDE is loaded (started). Close any windows that may be opened at this 
time. You can leave this help file opened, and task switch back and forth with the IDE windows. 
 
 


---

Index 
7 


---

Table of Contents 
8 
Exercise One - Create the Dictionary 
 
Start Clarion by pressing the Windows button and typing ‘Clarion’ 
 
 
1. From the IDE Menu, choose View 
 Show Start Page and click on the  Dictionaries 
hyperlink.  
2. Press the New Dictionary button, and the Save As dialog window appears 
3. Navigate to the Lessons\GettingStarted folder, or any folder that you want to use for this 
exercise 
In the File name entry, type GSLesson.DCT. Press the Save button to load the Dictionary Editor. 


---

Index 
9 
 
The Dictionary Editor’s main window is then displayed. 
 
 
 


---

Table of Contents 
10 
Exercise Two - Import Your Data 
1. Now let’s import some data tables so that we can see their field and key definitions. In the 
GettingStarted folder, we have placed two sample data files. In this exercise, we will import 
a set of Customers, and their Orders. 
2. From the DCT Explorer’s toolbar menu, choose the Import Tables option as shown here: 
 
 
 
The Table Import Wizard window appears. 
3. In the Select Server prompt, select TopSpeed Files from the drop list (It’s at the bottom of 
the drop list). At the time of this release, there are 15 different import formats available for 
import in the drop list.  


---

Index 
11 
 
 
4. Press the Next button (located at the bottom of the dialog), and press the ellipsis button. 
The Select Files window appears. 
 
 
 
5. Press the ellipsis button to the right of the Files prompt. 


---

Table of Contents 
12 
6. If needed navigate to the \Lessons\GettingStarted folder, and holding your CTRL key 
down, highlight the CUSTOMER.TPS file and the ORDERS.TPS and press the Open 
button. 
7. Press the Next button to import the files. 
8. The DCT Explorer displays the imported tables under the Tables node. 
 
 
 
We now have two existing table definitions that we imported into our Dictionary. 
 
 


---

Index 
13 
 
 
 
Save your new Dictionary and proceed to Exercise Three. 
 


---

Table of Contents 
14 
Exercise Three – Define your Tables relationships 
We want to define the relationship of Customers and their Orders. In this case, one Customer can 
have many Orders, making this a "One to Many" relationship. We just need to define this 
relationship to provide the Application Generator with the information necessary to access the 
related records. 
 
Define the Relationship: 
1. Select Customers in the Tables node (1), then in the Quick View panel select the 
Relations node (2), then press the  Add button 
 (3) in the Toolbar above the list box, 
and then the Relationship dialog opens (4). 
 
 
 
The Relationship Properties dialog is where you define the relationship.  
 
2. Make sure the Type dropdown list is set to 1:MANY.  
3. In the Primary Key dropdown list, press the down-arrow key to display the choices, 
highlight KeyCustNumber, and then press the TAB key. 
This is the key on the Customer table (the “One” side of the relationship) that we’ll use to 
link the two tables. 
4. In the Related Table dropdown list, press the down-arrowbutton to display the choices, 
highlight Orders, and then press the TAB key. 
5. In the Foreign Key drop list, press the down-arrow button to display the choices, highlight 
KeyCustNumber, then press tab. 


---

Index 
15 
This is the key on the Orders table (the “Many” side of the relationship) that we’ll use to link 
back to the Customers table.  
Next, the linking columns in the keys must be "mapped" so the Application Generator can 
know which field/columns in the two tables are related to each other. In this case both tables 
have a field/column named “Custnumber” so we have matching column names. 
 
6. Press the Map By Name button. 
The linking columns between the two tables appear in the two Column Mappings list 
boxes.  
 


---

Table of Contents 
16 
Setting up the Referential Integrity Constraints 
1. In the Referential Integrity Constraints section, choose Cascade from the On Update 
dropdown list. 
2. In the Referential Integrity Constraints group box, choose Restrict from the On Delete 
dropdown list. 
The generated source code will automatically maintain referential integrity between the 
tables.  
3. Press OK to close the Relationship Properties dialog. 
4. Another Relationship Properties dialog appears, allowing you to add a second relationship. 
Press the Cancel button to close this window. That brings us back to the Quick View panel 
and we can see the relationship we defined: 
 
 
 
 


---

Index 
17 
Exercise Four - Add a Lookup File 
In this lesson, we will now look at utilizing the Dictionary Editor to take advantage of the power in 
the Application Generator. The steps wewill be following in this lesson  will directly affect how our 
application will be generated in Lesson Eight. 
1. Highlight the Customer table and examine the Fields list. You should notice a State 
column. In the next sequence of steps, we will create a lookup table to allow a user to 
select from a list of valid state abbreviations. After that, we will "notify" the state column 
that a lookup is active. 
2. In the DCT Explorer, select the Tables node, and press the Add Table 
 button, located 
in the DCT Explorer toolbar. 
 


---

Table of Contents 
18 
 
 
3. In the Label entry field, type States 
4. You’ll see that the Dictionary Editor has filled the “Prefix” entry field with STA as the Prefix. 
Next, we need to choose a Database Driver.  
5. From the “Driver” entry field select TOPSPEED from the drop list 


---

Index 
19 
6. Click the OK button to complete adding the new Table. 
7. In the Quick View panel select the “Columns” node and then press the Add 
 button in 
the toolbar. 
 
 
 
8. Type State in the Column Name entry field, and press the TAB key. 
 
 


---

Table of Contents 
20 
 
This creates a column named State. We’ll setup this State column as the link to the State column 
in the Customer table. Using the same column names makes it clear this is the link the two tables 
use in the relationship.  
In the generated Clarion code, adding the table’s prefix to column labels (separated by a colon) 
creates unique names for columns with the same name in separate tables. Therefore, we’ll refer 
to this column as STA:State, whereas the column in the Customer table is called CUS:State. 
  
Clarion also fully supports the Field Qualification Syntax naming convention. The State column 
(STA:State) can also be referred to as States.State (file label.field label).  
 
9. In the Characters entry, type 2, or use the spin control, and press the TAB key. 
10. Accept all other defaults, and press the OK button to complete the new column. 
 
After adding the “State” column the dialog refreshes allowing you to enter another column. 
11. In the Column Name column, type StateName, and then press the TAB key. 
12. In the Characters column, type 30, then press the OK button to complete this column. 
13. The Column Properties dialog refreshes allowing you to enter another column, we are 
finished with this table’s columns, so press the Cancel button to exit this dialog. 
 
 
 
14. Next select the Keys node, and press the Add 
 button, (the button is located in the 
toolbar). 
 
15. In the Label column, Type StateKey. 
16. In the Attributes group, check the Require Unique Value check box. 
This specifies a key that does not allow duplicate entries, that means if a user tried to add a 
State to the States table, and that State was already in the table, an error would be thrown 


---

Index 
21 
and the duplicate State would not be added to the States table. The Key we’re defining is to 
create a Many to One relationship between the two tables (Many different Customers but 
each only lives in one State). 
 
17. Click on the Columns tab, and press the Add 
 button, located in the toolbar. In the 
Select a Column dialog, highlight State and press select as shown on the image: 
 


---

Table of Contents 
22 
 
 
18. Press Cancel in the Select a Column dialog to close this window, and press the OK button 
to save this key. Finally, press Cancel again in the Key Properties dialog to stop adding 
additional keys and return to the Dictionary view. 


---

Index 
23 
 
 
 
19. Press the Save button 
 in the IDE main toolbar at this time to save the changes we just 
made to our database definition. 
 


---

Table of Contents 
24 


---

Index 
25 
Exercise Five - Create the Lookup Relationship 
Set the Relationship for the Customer and States tables: 
 
1. Highlight Customer in the DCT Explorer panel, then select the “Relations” node and press 
the Add  
  button located in the toolbar. 
The Relationship Properties dialog appears. This is where we’ll define the relationship.  
 
2. Click on the “Type” drop list and set it to MANY:1.  
3. In the Foreign Key drop list, verify it is set to None. 
4. In the Related Table drop list, press the down-arrow button and select States, and then 
press the TAB key. 
5. In the Primary Key drop list, press the down-arrow to display the choices, highlight 
StateKey. 
The StateKey from the States table (the One side of the relationship) that will be used to link 
the two tables.  
Next, the linking columns in the keys must be "mapped" so the Application Generator can 
know exactly which columns in the two tables are related to each other. Since we used 
identical column names, this is easy. 


---

Table of Contents 
26 
6. Press the Map By Name button. 
The linking columns between the two tables appear in the two “Column Mappings” list 
boxes.  
  
If you did not have a matching column name, no problem! Simply double-click on the 
Columns Mapping entry, and select the linking field from the popup window provided. 
7. Since the table relationship defined is only in one direction, Referential Integrity 
Constraints are not needed. The dialog should have these settings now: 
 
 
8. Press OK to close the Relationship Properties dialog. When a new copy of the dialog 
opens press Cancel to exit the Relationship Properties dialog.  
 


---

Index 
27 
 
 
 
 


---

Table of Contents 
28 
Exercise Six - Setup the Lookup Validity Check 
Now that the table relationship is defined, we can set the Validity Checks for the column that we 
expect to use on update forms. 
When entering a new Customer, we can specify that the State column must match an existing 
record in the States table. 
Define the Validity Check for the Customer State column 
1. Highlight the Customer table in the DCT Explorer list. 
2. In the Quick View list, under the Columns node select the State column, then click on the 
“Validity Checks” tab 
3. Click on the “Must Be In Table” radio button 
4. In the Table Label dropdown list States should be displayed. 
This specifies that the State column in the Customers table can only contain a value from 
a matching row in the States table.  
5. Press the Save button in the main toolbar. 
 
 
 


---

Index 
29 
Exercise Seven - Fine Tuning the Customer and 
Orders Tables 
Back in Exercise Two (2), we imported an existing table into the dictionary.  Although this is the 
fastest and most accurate way of defining your tables in the data dictionary, the file format 
information may not be the display format you want for your application.  
For example, a table may store a zip code as a 4-byte integer on disk. A zip code of 33024, using 
the default picture for that data type, will be displayed as 33,024. If the zip code stores an 
extension, it may be worse. For example, 330241159 stored in the table would appear as 
330,241,159 by default.  
Also, some data columns should not be accessible to the end-user, like an order number or 
customer number.  By default, all columns imported into the dictionary are designated as 
updateable entry data types. 
This exercise demonstrates the art of fine tuning your dictionary elements defined. 
 
The more time spent fine tuning your dictionary, the more time you will save generating a 
near perfect application using the various wizard tools! 
 
Auto number your numeric Unique Keys 
1. Highlight the Customer table in the DCT Explorer list.  
2. In the Customer properties tree select the Keys node, then select the KeyCustNumber 
3. In the Attributes group, check the Auto Number check box. 
This will cause any new customer that we add to automatically be assigned with the next 
sequential customer number (by default). 
4. Press Save and Close to close the Customer window. 
5. Highlight the Orders table in the DCT Explorer list.  
6. In the Keys View, RIGHT-CLICK on KeyOrderNumber, and select Properties from the 
popup menu. 
7. In the Attributes group, check the Auto Number check box. 
This will effectively cause any new order that we add to automatically be assigned with the 
next sequential order number (by default). 
8. Press the Save button on the IDE main toolbar. 
 


---

Table of Contents 
30 
Set the Autonumber Unique Columns as Display Only 
After adding the auto numbering capability to our numeric unique keys, we can also change the 
display characteristics of the auto number column(s). The reason for this is that we do not want 
the user to be able to modify a number that is automatically assigned. In some applications, 
developers sometimes like to hide this information from the end-user by not populating it. In our 
application, we will choose to display this information, but not allow the user to modify it. 
1. Select the Customer table in the DCT Explorer list. 
2. Select the CustNumber column under the Columns node 
3. Click the Controls tab. Click the dropdown arrow and change the Control Type: from 
Entry to String, and press the IDE Save button. 
 
 
4. Select the Orders table in the DCT Explorer Tables list. 
5. Select the OrderNumber column in the Columns list 
6. Select the Controls tab. Change the control type from Entry to String, and press the Save 
button  
 
By setting the properties for a control in the DCT you save time later when creating your 
application. Every application you generate from the dictionary, and every Procedure in the 
Application will automatically format the control the way you have it set in the DCTt. If you 
don't format controls here, and if the control requires custom formatting, you will have to 
custom format it for each Procedure and Application later.  
 
Column Display Formatting 
All columns contained in our imported tables can display their data in a variety of formats, and 
we can preset the formats here in the DCT. 


---

Index 
31 
1. Select the Orders table in the Dct Explorer, under the Columns node click on the 
OrderDate column 
2. Select the General tab and In the Screen Picture field, and now you can either type @D2, 
or you can press the ellipsis button to open the Edit Picture dialog and see a preview of 
the format. Prfess the IDE Save button. 
 
 
 
Clarion provides a number of different date and time picture formats that are used with date 
and time data types.  
 
3. Select the Customer table in the DCT Explorer list. 
4. Click on the ZipCode column in the Columns list 
5. In the Screen Picture entry, type @P#####P. Press the IDE Save button  
 
The zip codes stored in our Customer table are 5-digit zip codes. However, in the default 
picture format, it would display as a number, such as 33,334 for a zip code of 33334, and 
6,792 for a zip code of 06792. The @P picture we entered above is called a pattern 
picture.  
6. Press Dct Explorer Save and Close from the DCT Explorer toolbar. If you are prompted to 
save changes to GSLesson.DCT, press the Yes button to save and close the Dictionary 


---

Table of Contents 
32 
Editor. 
 


---

Index 
33 


---

Table of Contents 
34 
Exercise Eight - Generate your Program using the 
Wizards 
Now it’s time to use The Application Wizard. 
In this exercise, we will use the dictionary that we created in Exercises 1 – 7, and generate a full-
featured application, all in just a few minutes with no hand coding needed! 
The Application Wizard generates entire applications based on the DCT information that you 
preset and your selection to a series of Wizard dialogs that ask for one piece of information at a 
time. 
 
Create a New Application 
1. From the IDE main Menu, choose File 
 New 
 Solution, Project or Application, or 
from the Start page click on the New Solution link 
 
The New Solution, Project or Application dialog appears. 


---

Index 
35 
 
 
2. Select the Clarion for Windows item in the left Categories pane, and navigate to the 
Application Quick Start as shown above. 
3. Verify that the folder Location is in the target …\Lessons\GettingStarted directory.  
4. Type GSLesson in the Name field. 
5. Uncheck the Auto create project subdir checkbox. 
6. Press the Create button. 


---

Table of Contents 
36 
The Application Properties dialog appears. 
 
 
7. Press the ellipsis ( ... ) button to the right of the Dictionary File entry box. 
The Select Dictionary dialog appears. 
8. Highlight the …\Lessons\GettingStarted\GSLesson.DCT file and press the Open button. 
9. Verify that the Application Wizard check box is checked, and then press the OK button. 
The Application Wizard dialog appears. 
 
 
10. On the opening wizard window, press the Next button. 


---

Index 
37 
11. Accept the Default Theme and Layout1 Report Layout, and press the Next button. 
12. Make sure that the Generate Procedures for all files in my dictionary drop list choice is 
selected, and press the Next button four (4) times.  
13. You should now be in the Procedures & Reports dialog window. Make sure that the 
Generate Reports for each file checkbox is checked. 
 
14. Press the Finish button. The Application Wizard now creates the application.  
 
 
 
15. From the IDE Toolbar, Generate Source, and Build and Run your application by pressing 
the Start without Debugger button (shown below): 


---

Table of Contents 
38 
: 
Congratulations!  Your complete application is now running.  
Use the Application menu to explore your new application. Press the Browse menu and select 
“Browse the Customer file” then dbl-click any record in the list to enter the Customer form and 
verify that the CustNumber field is read-only like we set it in the DCT. Check the format of the 
ZIPCODE field where we used the @P#####P picture format. You can also run some reports on 
the default data that is supplied. 
Notice that In the Customer’s update form, if you enter an invalid state abbreviation it will cause a 
new Window to pop up when you tab or click away from the State field – this is the field we set in 
Exercise 6 for the DCT to have a ‘Validity’ check on any value entered. 
16. Exit the GSLesson program, which returns you to the Clarion IDE. In the Application 
toolbar, press the Save and Close button to close the application,  and then press the 
Close Solution button to close the application’s solution. 
 


---

Index 
39 


---

Table of Contents 
40 
Summary 
Let’s recap what was accomplished: 
 We used the Dictionary Editor to create a new data dictionary. 
 In our new dictionary, we imported a Customer and Orders table using the dictionary Editor’s 
Table Import feature.  
 We set up table relationships between the two tables that we imported. 
 We used the Data Dictionary to quickly define another table definition.  
 We defined the relationship between the tables and specified the Referential Integrity rules 
governing the relationship. 
 We used the Application Wizard to create a complete application, including the added 
validation to the Customer’s State column. 
In less than thirty minutes—without any "hand coding"—we created a complete application for a 
database containing three related tables. That‘s a real accomplishment! 
If you can do this much with Clarion’s "shortcuts," what can you expect to accomplish with all the 
other tools Clarion provides? 
You will find that the more time that you spend on your Dictionary design at the start, the less 
modifications you will need to make on the application side.  
In this Getting Started lesson, we have only scratched the surface into the power of the Clarion 
development environment. 
 
The Getting Started and Learning Clarion lesson applications 
The completed application and dictionary files are located in the  
…\Lessons\GettingStarted\Solution and …\Lessons\LearningClarion\Solution directory. These 
are the files created by following the steps in the Getting Started and Learning Clarion 
documents. 
 
There are two other lessons contained in this folder. The files used for the Online User’s Guide’s 
Debugger lesson can be found in the  
…\Lessons\Debugger folder. 
A lesson targeting the use of the Dictionary Synchronizer The files used for the Online User’s 
Guide’s Synchronizer lesson can be found in the  
…\Lessons\SQL folder. 
 
 


---

Index 
41 


---

Table of Contents 
42 
The Secret of Productivity 
The Secret of Productivity (you’ve all heard this before) is working smarter, not harder. That is 
exactly what Clarion is designed to allow you to do with its Template-driven programming 
paradigm—Clarion writes the repetitive code but customizes it for you, and then it is still flexible 
enough to let you add the "bells and whistles" (the fun part). 
The secret to real programmer productivity without loss of flexibility is this: always operate at the 
highest level of abstraction that can get the job done the way it needs to be done. The "problem" 
with operating at higher abstraction levels is the loss of flexibility to always do things exactly the 
way you want. With Clarion, this problem is solved.  
 
Template Driven Programming 
Clarion’s Application Generator is "template driven." This means that it is a tool that changes 
based on the requirements of the template you are using to generate your code. Clarion’s 
Procedure, Control, Extension, and Code Templates all write Clarion language source code for 
you, giving you a tremendous productivity boost. Clarion’s templates provide many of the benefits 
of object-oriented programming, especially reusability, and the default template set generates 
truly object-oriented Clarion code for you using the Application Builder Class (ABC) Library. This 
makes Templates the real key in Clarion to Rapid Application Development. 
 
What is a Template? 
In Clarion, a template is not just a "one-time" tool generating code that you must then maintain 
yourself (like the things that some other languages call "templates"), but is a continually 
interactive tool that asks specifically for the information it needs to generate your source code. 
Changing the information you provide to the template causes different source code to generate 
the next time you make your application. This interactivity makes Clarion’s Templates the key to 
Rapid Application Maintenance. 
Clarion templates allow you to insert your own Clarion source code into their generated source at 
any of the many Embed Points available to you within each template. This makes it unnecesssary 
for you to maintain all the generated code in order to customize the procedure’s behavior. It also 
guarantees that your customizations aren’t overwritten the next time you generate source—the 
template simply generates your code inside its code. This easy customization makes Clarion’s 
Templates the key to Rapid Application Enhancement. 
All the templates are stored in the registry file (TemplateRegistry.TRF). This file contains the pre-
written code and data structures which you customize and reuse. You can use the Template 
Registry to modify the design of each template’s default window or report to the way you want 
them to appear when you first create a procedure. 
You can modify the Clarion templates. You may also add third party templates, or write your own, 
and use them in addition to, and along with, the Clarion templates. This makes the Application 
Generator an infinitely extensible tool.  
 
How do you use Templates? 
When you create a new procedure, you identify the Procedure template that generates code that 
does the task you need to perform, then you customize it with the development tools. These 
Procedure templates include elements such as "browse windows" for viewing groups of rows, and 
"form windows" for editing one row at a time. If the procedure is for a window with a menu, the 
menu actions are automatically added to the application’s procedure tree, and marked "ToDo," as 
any other procedure call would be. 


---

Index 
43 
The Window Designer and Report Formatter are visual design tools that allow you to design 
windows and reports. You pick a control from a toolbox, click to place the control, then modify its 
properties. 
Once you have created a procedure you can also use the Control, Extension, and Code 
templates to add even more functionality to the procedure. Control templates contain controls and 
generate all the standard executable code needed to use and maintain them. All the pre-
populated controls that appear in the default window designs for the Procedure templates are 
actually Control templates that perform all the functions of the procedure. 
Extension templates add executable code that increases the functionality of the procedure. Each 
typically provides you with on-screen instructions on what information to "fill in" to incorporate its 
functionality into the application. 
Another way you may customize a procedure is to add your own embedded source code. The 
Application Generator displays a tree displaying all of the Embed Points that are available: 
before, during, and after the procedure’s main logic, and for every event the window or controls in 
the procedure can generate. You can also directly edit your embedded source within the context 
of all the generated source code. This allows you to pick the precise logical point at which to 
execute the code, then "hand code" it, or use a Code template to write code for you. The 
Application Generator generates all your application’s source code from the templates and all 
your customizations (including embedded source code).  
Clarion provides a rich assortment of standard templates with which you can rapidly develop 
applications. Just as the Quick Start lesson introduced you to the Wizards, the Application 
Generator lesson in the Learning Clarion document introduces you to using Clarion’s Templates 
to produce any Windows application you need. 
 
Clarion's Levels of Abstraction 
At this point in your introduction to Clarion, you’ve already worked with Clarion’s highest 
abstraction levels: the Wizards. You’ll work with most of the following features later in the 
Learning Clarion lessons. 
 
Dictionary Editor  
Your Data Dictionary is a single repository for all the table definitions and their default data entry 
control settings. For existing data, defining your tables can be as simple as importing the table’s 
definition into the Data Dictionary directly from the table itself! 
 


---

Table of Contents 
44 
Application Wizard 
Generates a complete "standard" application for you in just minutes, based on the table 
definitions and settings in your Data Dictionary. 
 
Procedure Wizards 
Generate "standard" procedures for you (like a Browse list, or data entry Form) based on the 
settings in your Data Dictionary. 
 
Procedure Templates 
Generate "standard" procedures for you (such as the application Frame menu, or a Report), 
based on the window or report design you create in Clarion’s Window Formatter and Report 
Formatter, and the options you select for the Template’s prompts for information about your 
procedure. 
 
Control Templates 
Add "standard" controls to your window or report design (such as a related tables Tree control) 
and generate all the code needed to "drive" the behavior of the control.  
 
Extension Templates 
Generate additional code into a procedure to provide functionality unrelated to any specific 
window control (such as a Date/Time display in the application Frame’s status bar).  
 
Code Templates 
Generate code into a procedure that usually performs a single task related to a specific window 
control (such as Data Entry validation). 
 
Embedded Source Code 
You can write Clarion language source code of your own in any of the very numerous Embed 
Points in each procedure to customize and/or modify the behavior of the Template-generated 
code. 
 
Source Template 
A Template which allows you to completely write your own Clarion language procedures while still 
maintaining the application in the Application Generator. 
 
Windows API and C Standard Library 
In any Clarion language code that you write (whole procedures or into Embed Points), you can 
directly call Windows API functions or C standard library functions, if you really need to. A utility 
program will generate the Clarion language Windows API function prototypes, and C Standard 
Library prototypes are documented in the Programmer’s Guide. 
 


---

Index 
45 
C/C++ or Modula-2 Code 
Write any SoftVelocity C/C++ or Modula-2 functions that you need to and link them into your 
Clarion application. These compilers are included and are invoked by simply adding a .C, .CPP, 
or .MOD source code module to your Clarion project (also sold separately). 
As you can see, the levels of abstraction available to you in Clarion span every level from the 
Application Wizard right down to writing C code (or even Assembly, if you want to work that hard). 
 
The Clarion Key to Maximum Productivity 
The key to making Clarion work for you is to always work at the highest abstraction level possible: 
 Let the Application Wizard write a "starting point" application for you.  
 Use the Procedure Wizards to add new procedures, as needed.  
 Modify what you need to in each Procedure Template using Clarion’s two-way interactive 
tools (like the Window and Report formatters).  
 Add Control, Extension, and Code Templates as you find you need their functionality. 
 Customize it all with some Embedded Source Code.  
 When you find you need to do something that no template does for you, use the Source 
Template and write it in the Clarion language (or get a third-party Template that does what 
you need).  
 Dive all the way down to the Windows API and C/C++ levels only when you absolutely must. 
This is the Clarion philosophy of working smarter, not harder, by letting the toolset do the 
"drudge" work. Do this, and you’ll find that your productivity soars compared to any other tool 
you’ve ever used. 
 
Clarion's Development Environment 
The development environment contains several main tools, all of which are accessible from the 
others. When using the Application Generator, buttons and menus in the various dialogs lead to 
the other tools.  
The following Application Development Flow chart shows how all the tools common to both 
Professional and Enterprise Editions of Clarion interact with each other and the template registry, 
with the Application Generator at the center of the whole process: 
 
This section provides a description of each tool, in the order that a typical programmer using the 
Application Generator might encounter them. Each tool contains dialog boxes which the 
programmer fills out to describe the Application’s functionality to the Application Generator. On 
your command, the Application Generator generates the specified source code, and the Project 
System compiles and links it to make an executable program. 
 


---

Table of Contents 
46 
Common Tools 
The following are brief descriptions of the tools common to both Professional and Enterprise 
editions of Clarion. 
 
The Dictionary Editor 
The Data Dictionary (a .DCT file), maintained by the Dictionary Editor, holds a description of the 
database, including its tables, keys, indexes, database drivers, file relations, columns, column 
validation rules, referential integrity constraints, and more. This is the first file you create when 
you design your application. 
You can create the table definitions from scratch, or you can import definitions from existing 
tables. The other tools of the development environment use the information in the Data Dictionary 
to let you, for example, easily place columns in a dialog box you design for the end user. The 
Application Generator creates code for all the statements that access the tables based on how 
you construct the Data Dictionary. In fact, the Application Wizard can generate a fully functional 
application based solely on your Data Dictionary! 
 
The Application Generator 
The Application Generator generates your application’s source code, one procedure at a time, 
based on the templates you pick from the template registry. It lets you add global and local 
memory variables, and customize the procedures with visual design tools and embedded source 
code. 
The Application Generator provides access to the other tools of the development environment so 
you can customize the look and functionality of the windows, menus, reports and other user 
interface elements of your application. The templates provide their own controls (which appear 
within the Application Generator) allowing you to provide the information with which the template 
customizes the requested functionality. 
 
The Window Designer 
Visually design your application’s windows and controls—everything the end user sees—in the 
Window Formatter. It automatically generates the source code for the elements you visually 
design on screen. 
 
The Report Formatter 
The Report Formatter works with the Application Generator in much the same way as the 
Window Formatter. You place controls in a sample report page. At run time, the print engine 
processes the rows, handling page breaks, group breaks, headers, and footers as specified. 
 


---

Index 
47 
The Text Editor 
The Text Editor is a functional programmer’s editor which you can use to write any source code 
your application needs. Most likely, when using the Application Generator, you’ll use the Text 
Editor to create embedded source code to customize the way a procedure operates.  
The Text Editor features color coded syntax highlighting, making it easier to identify the different 
parts of the Clarion language statements for editing purposes. It also has full text search and 
replace capabilities, along with all the standard editing tools. 
 
The Formula Editor 
The Formula Editor helps you quickly generate and manage simple or complex assignment 
statements based on any kind of mathematical or string expression. The Formula Editor provides 
syntax checking, plus instant access to all the variables, functions, and operators, so that the 
formulas generated are always syntactically correct. 
 
The Project System 
The project file contains compile and link options, such as whether to include debug code, 
optimization choices, external files, the source code files, libraries and other external files 
included in the compile and link process. 
 
The Debugger 
Debugging a program usually requires running the program and repeatedly stopping it at various 
points during execution to examine the value of different variables to determine the cause of logic 
errors in the program. The Clarion Debugger have a number of windows which display source 
code, variable contents, active procedures, and much more. 
There are three lessons on using the Debugger contained in the User’s Guide. We recommend 
that you go through them after finishing Getting Started and Learning Clarion lessons. 
 
The On-Line Help 
Clarion provides extensive on-line context sensitive help from almost every screen. Click on the 
Help button, or press f1.  
The Common Questions section of the on-line help provides instructions and examples for 
performing common application tasks. You can cut and paste example code directly from the help 
system into your program. Choose Help  Contents, then press the FAQ button. 
 


---

Table of Contents 
48 
Enterprise Edition Tools 
The following are brief descriptions of the tools which are in the Enterprise Edition of Clarion and 
are not available in Professional Edition, except as add-ons (in certain cases). These tools are all 
fully documented in the core help—including lessons for each. 
 
Dictionary Synchronizer 
The Dictionary Synchronizer allows you to synchronize one data dictionary to another (available 
only in Enterprise Edition).  You can synchronize two Clarion data dictionaries (.DCT files), or 
synchronize a Clarion data dictionary with an SQL back end’s data dictionary (either direction). 
This allows you to get all the table definitions and relationships at once from the SQL backend 
database and eliminate a lot of front-end work and keep the Clarion data dictionary in synch with 
the SQL RDBMS at all times, no matter what changes the SQL Database Administrator makes.  
 
Dictionary Diagrammer 
The Data Dictionary (a .DCT file), can also be maintained by the Dictionary Diagrammer (also 
available as an add-on to Professional Edition). This is a visual data modeling tool, allowing you 
to view your database design from an entity-relationship diagram perspective.  
 
Business Math Library 
The Business Math Library is a set of standard business and statistical functions which you may 
use (also available as an add-on to Professional Edition). There are also a full set of templates 
which make implementing these functions in your programs very easy. 
 
 
 


---

Index 
49 
What's Next? 
There are several directions that we would like to recommend: 
1. The GSLesson application that we started here is greatly expanded with many of Clarion’s 
powerful templates and other features in the Learning Clarion section of this online help 
file. These lessons are designed to introduce you to all the common development tools 
Clarion offers in both Professional and Enterprise Editions. 
2. Dive in and get started with your own projects. The Online User's Guide, accompanied 
with the Clarion Core Help, provide comprehensive information to help you through your 
particular projects. 
3. SoftVelocity offers educational seminars at various locations. Call Customer Service at 
(954) 785-4555 to enroll. 
4. Join (or form) a local Clarion User’s Group and participate in joint study projects with other 
Clarion developers. 
5. Participate in SoftVelocity’s online newsgroups. SoftVelocity’s news server offers 
newsgroups for all SoftVelocity products. On this news server you can exchange ideas 
with other Clarion programmers.  


---

Table of Contents 
50 
Index 
Clarion Programming Concepts ................ 42 
Getting Started............................................ iii 
Ex. 1 - Create the Dictionary ....................... 8 
Ex. 2 - Import Your Data ............................ 10 
Ex. 3 - Relate Your Tables ........................ 14 
Ex. 4 - Add a Lookup File .......................... 17 
Ex. 5 - Create the Lookup Relationship ..... 25 
Ex. 6 - Set the Lookup Validity Check ...... 28 
Ex. 7  - Fine Tuning the Customer and 
Orders Tables ........................................... 29 
Ex. 8 - Create your Program using the 
Wizard ....................................................... 34 
Summary ................................................... 40 
Getting Started Lessons ............................. 6 
 
