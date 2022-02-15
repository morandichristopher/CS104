#Chris Morandi
#CS 104-01
#Average
average = 0
total = 0
howManyEntered = 0

howMany = int(input("How many test scores would you like to average: "))
testScore = int(input("Enter test score: "))

total = total + testScore

howManyEntered += 1

while howManyEntered < howMany:
    testScore = int(input("Enter test score: "))
    total = total + testScore
    howManyEntered += 1

average = total / howMany

print("The average for the test scores you entered is: " + str(average))
