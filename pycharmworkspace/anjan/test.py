import time
import random

from anjan.calculator import runoperation

print("Sleeping...")
time.sleep(1)
print("Awake...")
print(random.randint(0,10));

# Loop a random number of times (Between 10 & 50)
loopMax = random.randint(10, 50)

# Printing number of random requests
print("Request for " + str(loopMax) + "received... Beginning the calculations")

# Create a list which represent Calculator operations ' like +,-,*,/ '
operations = ['+']

# Append function to add the rest of the Calculator operations to the above list
operations.append('-')
operations.append('*')
operations.append('/')
operations.append('+')

# Printing the list of operations
print("Request to perform " + str(operations) + " calculator operations has been received.")

# Printing the number of operations in the list
print("Total number of operation which will be performed are :: " + str(len(operations)))

# Printing 3 lines. PRINT Function itself print by default 1 line and '\n' is used for additional number of lines.
print('\n\n')

# Start the loop
for index in range(loopMax):
    # Generate 2random number to perform operations on them
    num1 = random.randint(-99,99)
    num2 = random.randint(-99,99)
    print("1st random number generated is :: " + str(num1))
    print("2nd random number generated is :: " + str(num2))
    print('\n')

    for operation in operations:
        print("Operations = " + str(operations))
        runoperation(operation,num1,num2)
        print()