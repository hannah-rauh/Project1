import os
import filecmp
from dateutil.relativedelta import *
from datetime import date
import datetime

fileA='P1DataA.csv'
fileB='P1DataB.csv'

#Input: file name
#Ouput: return a list of dictionary objects where
#the keys are from the first row in the data. and the values are each of the other rows

def getData(fileName):
    studentInfo=[]

    infile = open(fileName,'r')
    lines=infile.readlines()[1:]
    infile.close()

    for line in lines:
        line = line.rstrip()

        studentInfoDict={}
        values=line.split(",")
        first=values[0]
        last=values[1]
        email=values[2]
        studentClass=values[3]
        dob=values[4]

        studentInfoDict["First"]=first
        studentInfoDict["Last"]=last
        studentInfoDict["Email"]=email
        studentInfoDict["Class"]=studentClass
        studentInfoDict["DOB"]=dob

        studentInfo.append(studentInfoDict)
    return studentInfo





#Sort based on key/column
#Input: list of dictionaries and col (key) to sort on
#Output: Return the first item in the sorted list as a string of just: firstName lastName

def mySort(data,col):
    sortedList=sorted(data,key=lambda data:data[col]) #sortedList[0]->{'First': 'Rosalyn', 'Last': 'Villarreal', 'Email': 'mauris.id@tortor.edu', 'Class': 'Freshman', 'DOB': '2/21/2015'}
    firstName=sortedList[0]['First'] #'Rosalyn'
    lastName=sortedList[0]['Last'] #'Villarreal'
    return firstName+" "+lastName


# Create a histogram
# Input: list of dictionaries
# Output: Return a list of tuples sorted by the number of students in that class in
# descending order
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]
def classSizes(data):
    classList=[]
    freshmanCount=0
    sophomoreCount=0
    juniorCount=0
    seniorCount=0
    for d in data: #d->{'First': 'Rosalyn', 'Last': 'Villarreal', 'Email': 'mauris.id@tortor.edu', 'Class': 'Freshman', 'DOB': '2/21/2015'}
        if d['Class']=='Freshman':
            freshmanCount+=1
        elif d['Class']=='Sophomore':
            sophomoreCount+=1
        elif d['Class']=='Junior':
            juniorCount+=1
        elif d['Class']=='Senior':
            seniorCount+=1
    classList.append(('Freshman',freshmanCount))
    classList.append(('Sophomore',sophomoreCount))
    classList.append(('Junior',juniorCount))
    classList.append(('Senior',seniorCount))
    return sorted(classList, key=lambda classList:classList[1],reverse=True)


# Find the most common birth month from this data
# Input: list of dictionaries
# Output: Return the month (1-12) that had the most births in the data
#'DOB': '2/21/2015'
def findMonth(data):
    bdayDict={} #{'3': 9, '7': 7, '2': 9, '12': 8, '4': 6, '10': 8, '5': 6, '8': 8, '6': 8, '9': 9, '11': 6, '1': 6}
    for d in data:
        month=d['DOB'].split('/')[0]
        if month in bdayDict:
            bdayDict[month]+=1
        else:
            bdayDict[month]=1
    mostBdays=list(bdayDict.keys())[0]
    for k in bdayDict.keys(): #k->3 then k->7
        if bdayDict[str(k)]>bdayDict[mostBdays]:
            mostBdays=k
    return int(mostBdays)


#Similar to mySort, but instead of returning single
#Student, the sorted data is saved to a csv file.
# as fist,last,email
#Input: list of dictionaries, col (key) to sort by and output file name
#Output: No return value, but the file is written
def mySortPrint(data,col,fileName):
    outFile = open(fileName, "w")
    sortedList=sorted(data,key=lambda data:data[col]) #sortedList[0]->{'First': 'Rosalyn', 'Last': 'Villarreal', 'Email': 'mauris.id@tortor.edu', 'Class': 'Freshman', 'DOB': '2/21/2015'}
    for d in sortedList:
        firstName=d['First'] #'Rosalyn'
        lastName=d['Last'] #'Villarreal'
        email=d['Email']
        outFile.write(firstName+','+lastName+','+email+'\n')

    outFile.close()





# def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB and the current date to find the current
# age in years.

def findAge(data):
    now = datetime.datetime.now()
    age=0
    total=0
    for d in data:
        dob=d['DOB'] #dob->'2/21/2015'
        month=int(dob.split('/')[0])
        day=int(dob.split('/')[1])
        year=int(dob.split('/')[2])
        if month<now.month: #test 11/03/1997, 10/15/1997, 3/23/1997
            age=now.year-year
        elif month==now.month:
            if day<=now.day:
                age=now.year-year
            else:
                age=(now.year-1)-year
        else:
            age=(now.year-1)-year
        total+=age
    return round(total/len(data))


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
    total = 0
    print("Read in Test data and store as a list of dictionaries")
    data = getData('P1DataA.csv')
    data2 = getData('P1DataB.csv')
    total += test(type(data),type([]),50)

    print()
    print("First student sorted by First name:")
    total += test(mySort(data,'First'),'Abbot Le',25)
    total += test(mySort(data2,'First'),'Adam Rocha',25)

    print("First student sorted by Last name:")
    total += test(mySort(data,'Last'),'Elijah Adams',25)
    total += test(mySort(data2,'Last'),'Elijah Adams',25)

    print("First student sorted by Email:")
    total += test(mySort(data,'Email'),'Hope Craft',25)
    total += test(mySort(data2,'Email'),'Orli Humphrey',25)

    print("\nEach grade ordered by size:")
    total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
    total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

    print("\nThe most common month of the year to be born is:")
    total += test(findMonth(data),3,15)
    total += test(findMonth(data2),3,15)

    print("\nSuccessful sort and print to file:")
    mySortPrint(data,'Last','results.csv')
    if os.path.exists('results.csv'):
        total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

    print("\nTest of extra credit: Calcuate average age")
    total += test(findAge(data), 40, 5)
    total += test(findAge(data2), 42, 5)

    print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
