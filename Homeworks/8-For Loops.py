test_cases = int(input("How many test cases: "))

for case in range(test_cases):
    numbers_remaining = int(input("How many numbers: "))
    total_sum = 0
    for number in range(numbers_remaining):
        current_number= int(input("Enter the numbers: "))  
        result = 1
        for i in range(number + 1):     
            result *= current_number    
        print(result)                   
        total_sum += result             
    print("Sum is: ", total_sum,"\n")
  #=============================================================================================
