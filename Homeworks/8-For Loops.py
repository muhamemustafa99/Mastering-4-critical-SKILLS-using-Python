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

for fnumber in range(1, first_range + 1):   # if we changed the start from 1 to 0, then the same number will be added twice
    for snumber in range(1, sec_range + 1):     # in our example, 70 will be added to the 0 twice 
        if fnumber + snumber == added:
            counter += 1
print(counter)         
#=============================================================================================
