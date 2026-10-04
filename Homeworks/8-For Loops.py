#test case input and calculation logic

test_cases = int(input("How many test cases: "))

for case in range(test_cases):
    numbers_remaining = int(input("How many numbers: "))
    total_sum = 0
    for pos in range(numbers_remaining):
        current_number= int(input("Enter the numbers: "))  
        result = 1
        for i in range(pos + 1):     
            result *= current_number    
        print(result)                   
        total_sum += result             
    print("Sum is: ", total_sum,"\n")        
#=============================================================================================
first_range, sec_range, added = map(int, input("Enter 3 numbers: ").split())
counter = 0

for fnumber in range(1, first_range + 1):
    for snumber in range(1, sec_range + 1):
        if fnumber + snumber == added:
            counter += 1
print(counter)


#O(n) instead of O(n×m)


first_range, sec_range, added = map(int, input("Enter 3 numbers: ").split())
counter = 0

for fnumber in range(1, first_range + 1):
    snumber = added - fnumber
    if 1 <= snumber <= sec_range:
        counter += 1
print(counter)

# another way

# Read three integers from input: first_range, sec_range, added
first_range, sec_range, added = map(int, input("Enter 3 numbers: ").split())

# Compute the minimum possible value for fnumber (lower bound of the valid range)
minimum_fnumber = max(1, added - sec_range)

# Compute the maximum possible value for fnumber (upper bound of the valid range)
maximum_fnumber = min(first_range, added - 1)

# If the range is valid (minimum <= maximum), count the valid values
if minimum_fnumber <= maximum_fnumber:
    # Calculate the number of integers in the range [minimum_fnumber, maximum_fnumber]
    counter = maximum_fnumber - minimum_fnumber + 1
else:
    # No valid values exist
    counter = 0

# Output the final count
print(counter)

#=============================================================================================
