################# Day 1

# print('practice', "makes perfect.")
# print("Childern must be taught\n how to think\n NOT\n what to think")
# print("\"\"")
# print('2*3*4*5/10=')
# print(2*3*4*5/10)

# print('*')
# print('* *')
# print('* * *')
# print('* * * *')
# print('* * * * *')

# print('        *')
# print('      * * *')
# print('    * * * * *')
# print('  * * * * * * *')
# print('* * * * * * * * *')
# print('  * * * * * * *')
# print('    * * * * *')
# print('      * * *')
# print('        *')

# print('HI')
# print()
# print("I am Mohamed")
# print(3*6)
# print("wonderful \" Day")
# print("wonderful Day")




################# Day 2

# Name=input("Enter your name:\n")
# Age=input("Enter your age:\n")
# Track=input("Enter your track:\n")

# print("Your name is: " + Name)
# print("Your age is: " + Age)
# print("Your track is: " + Track)

# print("Your name is: " + input("Enter your name:\n"))
# print("Your age is: " + input("Enter your age:\n"))
# print("Your track is: " + input("Enter your track:\n"))
##############################

# Num1 = float(input("Enter your first Number: "))
# Num2 = float(input("Enter your second Number: "))

# print(f"{Num1} + {Num2} = {Num1 + Num2}")
# print(f"{Num1} - {Num2} = {Num1 - Num2}")
# print(f"{Num1} * {Num2} = {Num1 * Num2}")
# print(f"{Num1} / {Num2} = {Num1 / Num2}")
###############################

# Name1 = input("Enter the first student's name: ")
# ID1 = input("Enter the first student's ID: ")
# Grade1 = float(input("Enter the first student's grade: "))

# Name2 = input("Enter the second student's name: ")
# ID2 = input("Enter the second student's ID: ")
# Grade2 = float(input("Enter the second student's grade: "))

# Avg_grade = (Grade1 + Grade2) / 2

# print(f"\nThe first student's name is: {Name1}, ID: {ID1}, Grade: {Grade1:.2f}")
# print(f"The second student's name is: {Name2}, ID: {ID2}, Grade: {Grade2:.2f}")
# print(f"\nAverage grade of both students: {Avg_grade:.2f}")
###############################

# odd1, even1, odd2, even2, odd3, even3, odd4, even4 = map(int, input("Enter 8 numbers: \n").split())

# total_odd = odd1 + odd2 + odd3 + odd4
# total_even = even1 + even2 + even3 + even4

# print("Sum of odd numbers:", total_odd)
# print("Sum of even numbers:", total_even)
###############################

# msg1 = input("Enter your first msg: ")
# msg2 = input("Enter your second msg: ")
# msg3 = input("Enter your third msg: ")

# all_msg = (f"{msg1}'{msg2}\"{msg3} ")

# print(all_msg * 10)
###############################

# num1 = 1
# num2 = 2

# num3= num1+num2  #3
# num1=num2        #2
# num2=num3        #3

# num3= num1+num2  #5
# num1=num2        #3
# num2=num3        #5

# num3= num1+num2  #8
# num1=num2        #5
# num2=num3        #8

# num3= num1+num2  #13
# num1=num2        #8
# num2=num3        #13

# num3= num1+num2  #21
# num1=num2        #13
# num2=num3        #21

# num3= num1+num2  #34
# num1=num2        #21
# num2=num3        #34

# print(num3)
###############################

# num1,num2=map(int, input("Enter 2 numbers: ").split())

# temp_val = num1
# num1 = num2
# num2 = temp_val

# print(f"The numbers after being swapped {num1},{num2}")
###############################

# num1,num2=map(int, input("Enter 2 numbers: ").split())

# num1,num2=num2,num1

# print(f"The numbers after being swapped {num1},{num2}")
###############################

# num1,num2,num3=map(int, input("Enter 3 numbers: ").split())

# num1,num2,num3=num2,num3,num1

# print(f"The numbers after being swapped {num1},{num2},{num3}")
###############################

# numbers = list(map(int, input("Enter numbers separated by space: ").split()))
# print("You entered: ",numbers)

# for num in numbers:
#     if num == -1:
#      print((2 * num) + 1)
#     elif num == 1:
#      print(num * num)
###########################     

# number = int(input("Enter your number: "))

# sum_numbers= (number* (number + 1)) // 2

# print(sum_numbers)
###########################     

#05 Operators
nb = int(input("Enter the number of Boys: "))
ng = int(input("Enter the number of Girls: "))
nt = int(input("Enter the number of Teachers: "))

print(bool(nb > 25))
print(bool(ng <= 30))
print(bool(nb > 20 and nt > 2 or ng > 30 and nt > 4))
print(bool(nb < 60 or ng < 70))
print(bool(not nb >= 60 and not ng >= 70)) #Not
print(bool(nb == ng+10))
print(bool(nb-ng > 10 or nt > 5))
print(bool(nb == ng+10 or ng == nb+15))
#---------------------------------------------------------
