import csv
import urllib

def convertCSVToDictionary(data):
    dictionary = {}
    for row in data:
        key, value = row
        dictionary[key] = value
    return dictionary

months = csv.reader(open('months.csv', 'r'))
days = csv.reader(open('dayofbirth.csv', 'r'))
lastdigitofbirthyear = csv.reader(open('lastdigitofbirthyear.csv', 'r'))
monthSelection = convertCSVToDictionary(months)
dayOfBirthSelection = convertCSVToDictionary(days)
lastdigits = convertCSVToDictionary(lastdigitofbirthyear)

month = raw_input("Please enter month of birth: ")
day = raw_input("Please enter day of birth: ")
lastdigit = raw_input("Please enter the last digit of birth year: ")


print(monthSelection[month] + dayOfBirthSelection[day] + lastdigits[lastdigit])

'''print(monthSelection)
print(dayOfBirthSelection)
print(lastdigits)'''


