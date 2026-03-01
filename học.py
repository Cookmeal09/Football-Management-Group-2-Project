#lab1a
number1 = float(input("Enter a number: "))
number2 = float(input("Enter another number: "))
result = number1*number2
print(f"Your result is:  {result}")

number3 = float(input("Enter a number: "))
number4 = float(input("Enter another number: "))
result = number3+number4
print(f"Your result is:  {result}")


print("Printing current and previous number sum in a range(10)")
previous = 0

for current in range(10):
    total = current + previous
    print(f"Current number {current} Previous number {previous} Sum: {total}")
    previous = current
#nó lưu previous bằng với cái current hiện tại r chạy tiếp vòng lặp 9 lần
print("Name","Is","James",sep="**")
#------------------------------------------------------------------------
a = float(input("Enter first number (a): "))
b = float(input("Enter second number (b): "))
c = float(input("Enter third number (c): "))

# Accept a decimal number to convert to octal
num = int(input("Enter a decimal number to convert to octal: "))

# Convert decimal to octal using print() output formatting
print(f"The octal number of decimal number {num} is {num:o}")
#------------------------------------------------------------------
num= float(input("Enter a  number"))
print(f"your number is {round(num, 2)}")






#lab1b
# Q3: Program with quadratic calculation and triangle validation

import math

# Task 1: Input four real numbers a, b, c, x
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
x = float(input("Enter x: "))

# Task 2: Calculate S1 = ax² + bx + c
S1 = a * x * x + b * x + c
print(f"S1 = {S1}")

# Task 3: Calculate S2 based on discriminant (b² - 4ac)
delta = b * b - 4 * a * c
if delta >0:
    S2 = math.sqrt(delta)
    #math.sqrt là căn cái trong ngoặc
else:
    S2 = 0
print(f"S2 = {S2}")

# Task 4: Re-input a, b, c for triangle check
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

# Task 5: Check if a, b, c can form a triangle and calculate perimeter/area
if a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a):
    # Calculate perimeter
    perimeter = a + b + c
    print(f"Perimeter = {perimeter}")
    
    # Calculate area using Heron's formula
    p = perimeter / 2  # semi-perimeter
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(f"Area = {area}")
else:
    print("a, b, c are not side of a triangle")
#-----------------------------------------------------------------------------
# Q4: Program to accept 3 real numbers, find max/min, and arrange in ascending order

# Accept 3 real numbers
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

# Task 1: Display maximum and minimum values
maximum = max(a, b, c)
minimum = min(a, b, c)
print(f"Maximum value: {maximum}")
print(f"Minimum value: {minimum}")

# Task 2: Arrange them in ascending order (a ≤ b ≤ c)
# Sort the values and reassign
sorted_values = sorted([a, b, c])
a, b, c = sorted_values[0], sorted_values[1], sorted_values[2]

print(f"Numbers in ascending order: a = {a}, b = {b}, c = {c}")
#-----------------------------------------------------------------------------------------------------------------
#bài hours rate
hours =float(input("Enter Hours: "))
rate =float(input("Enter rate: "))
if hours > 40:
    total = 40 * rate + (hours-40) * rate * 1.5
else:
    total = hours * rate
    
print(f"Your total pays is: {total}")
#bài try except
try:
    hours = float(input("Enter hours: "))
    rate = float(input("Enter rate: "))
    total = hours * rate
    print(f"Your total is {total}")
except:
    print("Error, please enter numeric input")


def func1(*args):
    print("Printing value")
    for value in args:
        print(value)
func1(20, 40 ,60)
func1(80, 100)


#bài
#nhập điểm PE và FE xuất kết quả ra mà hình đậu hoặc rớt, pass nếu tbinh >=5 và khg có môn nào dưới <4
pe=float(input("Nhập điểm PE: "))
fe=float(input("Nhập điểm FE: "))
trbinh = (pe + fe)/2
print(f"điểm trbinh là {trbinh}")
if trbinh >=5 and pe >=4 and fe >=4:
    print("Pass")
else:
    print("Failed")


#nhập điểm PE và FE xuất kết quả ra mà hình đậu hoặc rớt, pass nếu tbinh >=5 và khg có môn nào dưới <4
#pe=float(input("Nhập điểm PE: "))
#fe=float(input("Nhập điểm FE: "))
#trbinh = (pe + fe)/2
#print(f"điểm trbinh là {trbinh}")
#if trbinh >=5 and pe >=4 and fe >=4:
#    print("Pass")
#else:
#    print("Failed")
#nhập vào 1 số nguyên cho biết trị tuyệt đối số nguyên đó
#number=float(input("Nhập vào 1 số bất kỳ: "))
#if number <0:
#    print(f"Trị tuyệt dối số đó là {-number}")
#else:
#    print(f"trị tuyệt dối số đó là chính nó")

#weather=input("Nhập thời tiết nang, mua, tuyet: ")
#temperature=float(input("Nhập nhiệt độ: "))
#if weather =="mua" or weather=="tuyet":
#    print("Mang ô hoặc áo mưa")
#elif weather =="nang" and temperature >30:
#    print("đi bơi")
#elif weather =="nang" and temperature <20:
#    print("đi dạo công viên")
#else:
#    print("thời tiết đẹp")


# Kiểm tra tính hợp lệ của mật khẩu
#password = input("Nhập mật khẩu từ người dùng: ")

#if password == "":  
#    print("Error")
#elif len(password) < 8:
#    print("Mật khẩu quá ngắn.")
#elif not any(char.isdigit() for char in password):
#    print("Mật khẩu cần có số.")
#else:
#    print("Mật khẩu hợp lệ.")

hours=float(input("Enter your hours: "))
rate =float(input("Enter your rates: "))
if hours > 40:
        total = 40 * rate + (hours - 40) * rate * 1.5
else:
        total = hours * rate
print(f"Your total pay is {total}")

try:
    hours=float(input("Enter hours: "))
    rate =float(input("Enter rate: "))
    total= hours * rate
    print(f"Your total pays is: {total}")
except:
    print("Error, please enter numeric input")

#----------------------------------------
    def calculation(a, b):
    # Tính tổng và hiệu
    sum_result = a + b
    diff_result = a - b
    # Trả về tuple (tổng, hiệu)
    return sum_result, diff_result

res = calculation(40, 10)
#res sẽ ra kqua + và - của 2 số a,b 
print(f"{res[0]}, {res[1]}")  # Output: 50, 30 res0 là kqua đầu 1 là kqua sau đó



def showEmployee(name, salary=9000):
        print(f"Name: {name} salary: {salary}")
showEmployee("Ben", 12000)
showEmployee("Jessa")

def outer_fun(a,b):
        def inner_fun():
                return a + b

        addition = inner_fun()
        return addition + 5



a = float(input("Enter a number: "))
b = float(input("Enter another number: "))


result = outer_fun(a, b)
print(f"Final result is: {result}")


# 1. Create a recursive function to calculate the sum of numbers from 0 to 10
# A recursive function is a function that calls itself, again and again.

    def addition(n):
        # Base case: if n is 0, return 0
        if n == 0:
            return 0
        # Recursive case: return n + sum of numbers from 0 to (n-1)
        else:
            return n + addition(n - 1)

    res = addition(10)
    print(res)


# 2. Assign a different name to function and call it through the new name

def display_student(name, age):
    print(name, age)

# Assign a different name to the function
show_student = display_student

# Call function using original name
display_student("Emma", 26)

# show= display nên show cũng phải có name và age thì ms đc print
show_student("Emma", 26)


x = [4 , 6 , 8, 24 ,12 , 2]
largest = max(x)
print(largest)  



# Get input number
num = int(input("original number "))

# Convert number to string to reverse it
num_str = str(num)
reversed_str = num_str[::-1]
reversed_num = int(reversed_str)

# Check if number is palindrome
if num == reversed_num:
    print("Given number palindrome")
else:
    print("Given number is not palindrome")


    


#def func1(*args):
#    print("Printing values")
#    for value in args:
#        print(value)

#func1(20, 40, 60)
#func1(80, 100)

#def calculation(a,b):
#        sum_result = a+b
#        diff_result = a-b
#        return sum_result, diff_result

#res =calculation(40,10)
print(f"{res[0]}, {res[1]}")
#* la` bo ngoac`

def showEmployee(name, salary = 9000):
    print(f"Name: {name} salary: {salary}")
    
showEmployee("Ben", 12000)
showEmployee("Jessa")    




#def outer_fun(a, b):
#    def inner_fun():
#        return a + b
#    addition = inner_fun()
#    return addition +5

#a = float(input("Enter a number: "))
#b = float(input("Enter another number: "))

#result=outer_fun(a, b)
#print(result)


#def display_student(name , age):
#    print(name , age)

#show_student=display_student


#display_student("Emma", 26)
#show_student("Emma", 26)

#number=int(input("Enter a number: "))
#number_str=str(number)
#reversed_str= number_str[::-1]
#eversed_number = int(reversed_str)

#if number == reversed_number:
#    print("Given number palindrome")
#else:
#   print("Given number not palindrome")



#x = [4, 6, 8, 24, 12, 2]
#largest = max(x)
#print(largest)




def result(Pe, Fe):
    trbinh = (Pe + Fe)/2

    if trbinh >=5 and Pe >=4 and Fe >=4:
        return"Pass"
    else:
        return "Failed"

Pe=float(input("Nhập điểm PE: "))
Fe=float(input("Nhập điểm FE: "))




#def computepay(hours, rate):
#    if hours >40:
#       total   = (40 * rate )+ ((hours-40) * 1.5 * rate)
#    else:
#         total = hours * rate
#    return total
 
#hours=float(input(f"Enter your hours: "))
#rate=float(input(f"Enter rate: "))
#total = computepay(hours, rate)
#print(f"Your total pay is {total}")

#nhập vào số nguyên n xuất ra màn hình các số chẵn từ 1 tới n

#n = int(input("Enter a number: "))
#i=2
#while i  <=n:
 #       if i%2==0:
 #           print(i)
#        i =i+1
    #nhập vô số n xuất ra n số chẵn đầu tiên
#n = int(input("Enter a number: "))
#i=2 #số bắt đầu
#count = 0
#while count < n:
#    print(i)
#    i +=2#số tiếp theo
#    count=count+1



for i in range (1, 6):
    for j in range(1, i+1):
        print(j, end = " ") # in cùng dòng
    print()#xuống dòng


n =int(input("Enter a number: "))
total = 0
k=1
while k <=n:
    total =total+k
    k=k+1
print("Sum is", total)

numbers = [12, 75, 150, 180, 145, 525, 50]


for num in numbers:
    if  num >500:
        break
    if num > 150:
        continue
    if num %5 == 0:
        print(num)

        
x=[1, 2 ,3 ,4 ,5 ,6, 7]
y=len(x)
print(f"Total digits are: {y}")

for i in range (1, 6):
    for j in range(1, i+1):
        print(j, end = " ") # in cùng dòng
    print()#xuống dòng
fruit=input("Enter a word: ")
nguyenam="a, e, i o, u"
b=""#lưu danh sách các ký tự ng.âm khg trùng
a=len(fruit)
print(a)
for letter in fruit:
    if letter in nguyenam and letter not in b:
            b +=letter
print(b)

fhand=open("mbox.txt","w")#w+ là ghi thêm w là xóa hết ghi lại
fhand.write("Newline\n")
fhand.seek(0)#ẩn hết cái ở trên
fhand.write("Newline 2\n")
fhand.write("Newline 3\n")

fhand=open("mbox.txt")
for i in fhand:
    print(i, end="")