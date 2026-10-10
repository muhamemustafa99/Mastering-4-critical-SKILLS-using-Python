#51.

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
#52.

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
#53.

#Triple of Numbers  (O(n³))
first_range, sec_range, third_range = map(int, input("Enter 3 numbers: ").split())
counter = 0

for fnumber in range(1, first_range + 1):
    for snumber in range(fnumber, sec_range + 1):
        for thnumber in range(1, third_range + 1):

            if fnumber + snumber <= thnumber:
                counter += 1
print(counter)

#Only 2 Loops  (O(n²))

first_range, sec_range, third_range = map(int, input("Enter 3 numbers: ").split())
counter = 0

for fnumber in range(1, first_range + 1):
    for snumber in range(fnumber, sec_range + 1):

        #thnumber(min) ​= fnumber + snumber
        thnumber = fnumber + snumber
#After calculating the sum of the two numbers, I assign it to `thnumber`,
# then I'll check right away whether this number is within the available range or not
        if 1 <= thnumber <= third_range:
            print(thnumber)
#Idea: When we find a pair (fnumber, snumber) with a sum of thnumber, 
# this means that thnumber is the smallest possible sum for that pair. 
# And since the total sum (the pair + the third number) 
# must fall within the range third_range, 
# the third number can take any value from 1 up to (third_range - thnumber).
# So the number of such values is (third_range - thnumber + 1).
            counter += third_range - thnumber + 1
            
print(counter)
#=============================================================================================
#54.

# Printing ********

rows = int(input("How many rows: "))

while rows % 2 == 0:
    rows = int(input("How many rows: "))
    print("Enter Odd number")
    continue
else:
    for row in range(rows):
# Find the middle row.
        if row == rows // 2:
# The number of spaces before the star equals the row index.
            print(" " * row + "*")
        else:
# Calculate how far the current row is from the middle
            distance_from_middle = abs(row - (rows // 2)) 

#  Calculate the spaces before the first star
# Formula: middle - distance_from_middle
            spaces_before = (rows // 2) - distance_from_middle
# Calculate the spaces between the two stars
# The farther the row is from the middle, the more space there is between the stars.
            spaces_middle = 2 * distance_from_middle - 1

# Print the row in this order:
        # 1. Spaces before the first star.
        # 2. The first star.
        # 3. Spaces between the stars.
        # 4. The second star.
            print(" " * spaces_before + "*" + " " * spaces_middle + "*")
            
# إزاي تفكر في مسائل من النوع ده؟
# الخطوة 1: ارسم الشكل النهائي على ورقة
# اكتب الـ output اللي إنت عايزه بالظبط. ده هيساعدك تشوف النمط.

# الخطوة 2: حدد "الصف" و "العمود"
# في المسائل اللي فيها رسم:
# الصف = الصف الأفقي
# العمود = المكان في الصف

# الخطوة 3: ابحث عن العلاقة بين رقم الصف والمكان
# الصف الأول → النجمة فين؟
# الصف التاني → النجمة فين؟
# وهكذا...

# الخطوة 4: استخدم "البعد عن النص"
# كتير من الأشكال المتماثلة بتتعامل مع البعد عن النص. استخدم abs عشان تحسبها.

# الخطوة 5: قسّم الشكل لأجزاء
# مسافات قبل
# نجمة
# مسافات بين
# نجمة
# مسافات بعد

# الخطوة 6: اكتب معادلة لكل جزء
# spaces_before = ?
# spaces_middle = ?

# الخطوة 7: اختبر المعادلة يدوياً
# جربها على صف من الأول، صف من النص، صف من الآخر

#=============================================================================================
#55.

# Find special pairs 
first_range, sec_range= map(int, input("Enter 2 numbers: ").split())
counter = 0

for fnumber in range(50, first_range + 1):
    for snumber in range(70, sec_range + 1):

        if fnumber < snumber and (fnumber+snumber) % 7 == 0:
                                     
                counter += 1
print(counter)
#=============================================================================================
#56.

#Find all quadruples (O(n4))

first_range, sec_range, third_range, fourth_range = map(int, input("Enter 4 numbers: ").split())
counter = 0

for fnumber in range(1, first_range + 1):
    for snumber in range(1, sec_range + 1):
        for thnumber in range(1, third_range + 1):
            for founumber in range(1, fourth_range + 1):


                if fnumber + snumber == thnumber + founumber:
                    counter += 1
print(counter)

#Find all quadruples (O(n3))



















#=============================================================================================


