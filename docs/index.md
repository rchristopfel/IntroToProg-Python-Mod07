# Module07 Website---

Rebecca Christopfel\
IT FDN 100 A Au 19: Foundations Of Programming: Python\
Module 07\
Assignment 07\
Due: November 20th by 11:59pm\


## Step 1
Watched Intro To Python Mod07 Video and played along with Labs practicing the elements of python as described by Randal./
## Step 2
Read book sections from Chapter 7/
## Step 3
Reviewed web pages and performed the exercises./
## Step 4
Watched the videos…./
## Step 5
Write a script or scripts that show pickling and exception handling…/
## Step 6 – Document

To complete this assignment, we were asked to show examples of pickling as well as examples of exception handling./

The python pickle module is designed to transform some type of data into an “obscure” form of itself. This is done to save space (file size is reduced) as well as to transport in a more streamlined way. Once the data is pickled, it is relatively easy to un-pickle (re-load) the data in a developer environment and then use it as intended./

Code showing this below:/


![pickling code]()/
![pickling code dat file]()

Following the pickling experiment, I moved on to the exception handling./

I wanted to create a script that used user inputs to calculate some value. I chose birthdate and had to utilize the datetime python type. Python universally stores dates in the following format:/

2019-11-20/

So I created a tuple of the user inputs and used datetime.date to convert it to the appropriate type./

userBirthDate = datetime.date(userBirthYear, userBirthMonth, userBirthDay)/

From here I did a some simple arithmetic to get the users age with decimal floats./

In order to prevent the user from entering a sting or a number outside of the valid range for days and months, I used a while loop to encapsulate my range and then the try/except block to ensure an integer value was the input. Code and result shown below./


![try/except code ]()/
![try/except code result]()

