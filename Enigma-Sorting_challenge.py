from ast import Break
import numbers


def sort(unsortedNumbers):

    unsortedNumbers.sort(key = lambda num: abs(num))
            
    return unsortedNumbers

# Do not edit any code below this line --------------------------------------
def validate(numbers):
    testNumbers = [0,1,1,1,2,2,2,3,3,4,4,4,4,5,5,5,5,5,6,6,7,7,7,8]

    if len(testNumbers) != len(numbers):
        return False

    for i in range(len(numbers)):
        if numbers[i] != testNumbers[i]:
            return False

    return True

# Start of main execution -------------------------------------------------------




myUnsortedNumbers = [1,2,3,4,5,6,5,4,5,4,5,6,7,7,8,1,2,5,3,1,0,7,4,2]

print("Run sort...")
completeNumbers = sort(myUnsortedNumbers)
print("...Sort complete")
print(completeNumbers)


print("Validating...")
validateResult = validate(completeNumbers)

if(validateResult == True):
    print("...Success!")
else:
    print("...sorry try again!")
 