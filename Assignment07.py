# ------------------------------------------------------------------------ #
# Title: Assignment 07
# Description: using exception handling and Python’s pickling module
# ChangeLog (Who,When,What):
# Rebecca Christopfel, 11-18-19, test pickle module
# Rebecca CHristopfel, 11-20-19, create try/except block for script
# ------------------------------------------------------------------------ #

# Pickling Example
# To store user demographic data

import pickle
# create some data to be pickled

strFirstName = str(input("Enter your first name: "))
strLastName = str(input("Enter your last name: "))
strAge = str(input("Enter your age: "))
strNumber = str(input("Enter your phone number: "))
demoData = [strFirstName, strLastName, strAge, strNumber]
print(demoData)

# store the data with the pickle.dump method
file = open("Demo.dat", "ab")
pickle.dump(demoData, file)
file.close()

# read the data back with the pickle.load method
file = open("Demo.dat", "rb")
fileData = pickle.load(file)
file.close()

print(fileData)

# Exception Handling
# To show calculation of age in years (and fraction of years) based on user's birthday
print("\n_____________________________________\n")
print("Now we'll do the exception handling...\n")
print("_____________________________________\n")

import datetime
today = datetime.date.today()
userBirthMonth = 0
userBirthDay = 0
userBirthYear = 0
while 1 > userBirthMonth or 12 < userBirthMonth:
    try:
        userBirthMonth = int(input("\nEnter your birth month (1-12): "))
    except ValueError:
        print("Oops! That is not a valid number. Try 1-12...")
while 1 > userBirthDay or 31 < userBirthDay:
    try:
        userBirthDay = int(input("\nEnter your birth day (1-31): "))
    except ValueError:
        print("Oops! That is not a valid number. Try 1-31...")
while True:
    try:
        userBirthYear = int(input("\nEnter your birth year: "))
        break
    except ValueError:
        print("Oops! That is not a valid number. Try format (yyyy) ...")
userBirthDate = datetime.date(userBirthYear, userBirthMonth, userBirthDay)
dateDiff = (today - userBirthDate)
userAge = round(float(dateDiff.days / 365.25), 2)
print("\n\tRounding to the nearest hundredth of a decimal, you are " + str(userAge) +" years old!")
