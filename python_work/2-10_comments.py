# Christian Mudd
fName = "\t\n\tChristian\n\t " #enter first name with escape characters to add white space
lName = " \n\t\tMudd\t\n " # enter last name with escapte character to add white space
print(fName + lName) # print first and last name with with white spaces
print(fName.rstrip()) # print first name with all white spaces to the right removed
print(lName.rstrip()) # print last name with all white spaces to the right removed
print(fName.lstrip()) # print first name with all white spaces to the left removed
print(lName.lstrip()) # print last name with all white spaces to the left removed
print(fName.strip()) # print first name with all white spaces removed
print(lName.strip()) # print last name with all white spaces removed