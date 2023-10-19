print(4,8,15,16,23,42,sep=' ',end='\n') #1,1 exercise
"""
Функция print() используется для вывода текста или значений в консоли.
sep=' ' - это параметр, который указывает, какой символ или строку использовать для разделения элементов, перечисленных внутри print(). Здесь установлен пробел, поэтому числа разделены пробелами.
end='\n' - это параметр, который указывает, что нужно добавить в конец вывода. 
\n - это символ новой строки, который переводит курсор на новую строку после вывода чисел.
"""




print(4,8,15,16,23,42,sep='\n')#1,2 exercise
"""
\n представляет собой символ новой строки, который переносит каждое число на новую строку.
"""



try:        #1,3 exercise
    m=int(input())

    print(m,m+1,m+2,sep=' ')
except ValueError : 
    print('please try again')
"""
try:: Это начало блока "try", в котором помещаются инструкции, которые могут вызвать исключение. В данном случае, код ожидает ввода числа, который может вызвать исключение ValueError, если пользователь введет нечисловое значение.
m = int(input()): Эта строка просит пользователя ввести значение с клавиатуры. input() возвращает введенную строку, и int() используется для попытки преобразовать эту строку в целое число и присвоить его переменной m.
print(m, m+1, m+2, sep=' '): Если пользователь успешно ввел целое число, код выводит значение m, m+1 и m+2, разделенные пробелами, используя функцию print().
except ValueError:: Это начало блока "except", который будет выполнен, если возникнет исключение ValueError.
print('please try again'): В случае возникновения ValueError, код выводит сообщение "please try again", предупреждая пользователя о необходимости ввести корректное числовое значение.

"""


try:        #1,4 exercise
    m1=int(input())
    m2=int(input())
    m3=int(input())
    print(m1+m2+m3)
except ValueError : 
    print('please try again')

"""
try:: Это начало блока "try", в котором помещаются инструкции, которые могут вызвать исключение. Здесь ожидается ввод трех чисел, которые могут вызвать исключение ValueError, если пользователь введет нечисловые значения.

m1 = int(input()), m2 = int(input()), m3 = int(input()): Эти строки просят пользователя ввести три значения с клавиатуры. input() возвращает введенные строки, и int() используется для попытки преобразовать эти строки в целые числа, которые присваиваются переменным m1, m2 и m3.

print(m1 + m2 + m3): Если пользователь успешно ввел три целых числа, код сложит их и выведет сумму с помощью функции print().

except ValueError:: Это начало блока "except", который будет выполнен, если возникнет исключение ValueError.

print('please try again'): В случае возникновения ValueError, код выведет сообщение "please try again", предупреждая пользователя о необходимости ввести корректные числовые значения.
"""

try:      #1,5 exercise
    num=int(input())   
    print("Volume = ",num*num*num)
    print('Volume = ',num*num*6)
except ValueError :
    print('please try again')
    """
    try:: Это начало блока "try", в котором помещаются инструкции, которые могут вызвать исключение. В данном случае, ожидается ввод числа, которое может вызвать исключение ValueError, если пользователь введет нечисловое значение.

num = int(input()): Эта строка просит пользователя ввести число с клавиатуры. input() возвращает введенную строку, и int() используется для попытки преобразовать эту строку в целое число, которое присваивается переменной num.

print("Volume = ", num * num * num): Если пользователь успешно ввел число, код вычисляет и выводит объем куба (кубической формы) с помощью формулы num * num * num. Строка "Volume =" предваряет значение объема куба.

print('Volume = ', num * num * 6): Также вычисляет и выводит объем гексаэдра (кубической формы) с помощью формулы num * num * 6. Строка "Volume =" снова предваряет значение объема.

except ValueError:: Это начало блока "except", который будет выполнен, если возникнет исключение ValueError.

print('please try again'): В случае возникновения ValueError, код выводит сообщение "please try again", предупреждая пользователя о необходимости ввести корректное числовое значение.
    """



try:        #2,1 exercise
    N = int(input("Enter the number of schoolchildren: "))  
    K = int(input("Enter the number of tangerines: "))

    whole_tangerines_per_student = K // N
    remainder_tangerines = K % N
    print("Each student will get", whole_tangerines_per_student, "whole tangerines.")
    print("There will be", remainder_tangerines, "whole tangerines remaining in the basket.")
except ValueError :
    print('please try again')
"""
try:: Это начало блока "try", в котором помещаются инструкции, которые могут вызвать исключение. Ожидается ввод пользователем двух чисел, которые могут вызвать исключение ValueError, если введены нечисловые значения.

N = int(input("Enter the number of schoolchildren: ")) и K = int(input("Enter the number of tangerines: ")): Эти строки запрашивают пользователя ввести количество школьников и количество мандаринов с клавиатуры. input() возвращает введенные строки, и int() используется для попытки преобразовать эти строки в целые числа, которые присваиваются переменным N и K.

whole_tangerines_per_student = K // N и remainder_tangerines = K % N: Здесь вычисляются целое число мандаринов, которое каждый школьник получит (деление с отбрасыванием остатка), и остаток мандаринов, которые останутся в корзине (остаток от деления).

print("Each student will get", whole_tangerines_per_student, "whole tangerines.") и print("There will be", remainder_tangerines, "whole tangerines remaining in the basket."): Эти строки выводят результаты расчетов, сообщая, сколько мандаринов каждый школьник получит и сколько мандаринов останется в корзине.

except ValueError:: Это начало блока "except", который будет выполнен, если возникнет исключение ValueError.

print('please try again'): В случае возникновения ValueError, код выводит сообщение "please try again", предупреждая пользователя о необходимости ввести корректные числовые значения.
"""



try: #2,2 exercise
    number = int(input("Enter a four-digit number: ")) 

    if 1000 <= number <= 9999:
    # Extract individual digits
        thousands_digit = number // 1000
        hundreds_digit = (number // 100) % 10
        tens_digit = (number // 10) % 10
        ones_digit = number % 10

        print("Thousands digit:", thousands_digit)
        print("Hundreds digit:", hundreds_digit)
        print("Tens digit:", tens_digit)
        print("Ones digit:", ones_digit)
    else:
        print("Please enter a valid four-digit number.")
except ValueError :
    print('please try again')
"""
number = int(input("Enter a four-digit number: ")): Эта строка запрашивает пользователя ввести четырехзначное число с клавиатуры. input() возвращает введенную строку, и int() используется для попытки преобразовать эту строку в целое число, которое присваивается переменной number.

if 1000 <= number <= 9999:: Это условие проверяет, является ли введенное число четырехзначным, проверяя диапазон от 1000 до 9999.

Внутри условия, если число четырехзначное, код извлекает каждую из его цифр:

thousands_digit = number // 1000: Это извлекает цифру тысяч.
hundreds_digit = (number // 100) % 10: Это извлекает цифру сотен.
tens_digit = (number // 10) % 10: Это извлекает цифру десятков.
ones_digit = number % 10: Это извлекает цифру единиц.
После извлечения цифр, код выводит их значения с помощью функции print(), чтобы пользователь видел результат.

Если введенное число не является четырехзначным, код выводит сообщение "Please enter a valid four-digit number."

except ValueError:: Это начало блока "except", который будет выполнен, если возникнет исключение ValueError.

print('please try again'): В случае возникновения ValueError, код выводит сообщение "please try again", предупреждая пользователя о необходимости ввести корректное четырехзначное число.
"""



try:        #2,3 exercise
    total_peop=int(input('total nimber is '))   
    survive=total_peop/2
    print(int(round(survive)),' people survive')
except ValueError :
    print('please try again')
"""
total_peop = int(input('total number is ')): Эта строка запрашивает пользователя ввести общее количество людей с клавиатуры, предварительно выводя приглашение для ввода. input() возвращает введенную строку, и int() используется для попытки преобразовать эту строку в целое число, которое присваивается переменной total_peop.

survive = total_peop / 2: Эта строка вычисляет количество людей, которые выживут, как половину от общего числа.

print(int(round(survive)), ' people survive'): Здесь код выводит количество выживших людей. round() используется для округления числа до ближайшего целого, и int() используется для преобразования округленного числа в целое. Затем выводится сообщение "people survive".
"""



try:                   #2,4 exercise
    num = int(input("Enter a number: "))
    result = num << 1
    if result == 0:
        print("Warning: The result of << is zero.")
    else:
        print("The result of << is ", result)
except ValueError:
    print("Invalid input. Please enter a valid number.")
"""
num = int(input("Enter a number: ")): Эта строка запрашивает пользователя ввести число с клавиатуры, предварительно выводя приглашение для ввода. input() возвращает введенную строку, и int() используется для попытки преобразовать эту строку в целое число, которое присваивается переменной num.

result = num << 1: Здесь код выполняет операцию сдвига влево на 1 бит для числа num. Это эквивалентно умножению числа на 2 в двоичной системе.

if result == 0:: Это условие проверяет, равен ли результат операции сдвига влево нулю.

Внутри условия, если результат равен нулю, код выводит предупреждение: "Warning: The result of << is zero."

В противном случае, если результат не равен нулю, код выводит результат операции сдвига влево.

except ValueError:: Это начало блока "except", который будет выполнен, если возникнет исключение ValueError.

print("Invalid input. Please enter a valid number."): В случае возникновения ValueError, код выводит сообщение "Invalid input. Please enter a valid number."

"""


#2,5 exercise
def addition(num1, num2):
    return num1 + num2

# Function to perform subtraction
def subtraction(num1, num2):
    return num1 - num2

# Function to perform multiplication
def multiplication(num1, num2):
    return num1 * num2



b='please write anither second number'




# Function to perform division
def division(num1, num2):
    if num2 == 0:
        return "Error: Division by zero"
    return num1 / num2
result= None
try:
    # Prompt the user to enter two numbers
    num1 = float(input("Please enter the first number: "))
    num2 = float(input("Please enter the second number: "))

    # Prompt the user to choose an operation
    operation = input("Please choose the operation (+, -, *, /, in 'sqrt' Number 1 is subcortical number and Number 2 is root indicator ): ")

    # Perform the selected operation based on user input
    if operation == '+':
        result = addition(num1, num2)
    elif operation == '-':
        result = subtraction(num1, num2)
    elif operation == '*':
        result = multiplication(num1, num2)
    elif operation == '/':
        result = division(num1, num2)
  
    else:
        result = "Invalid operation choice"

    # Display the result or an error message
    print("Result: ", result)

except ValueError:
    print("Invalid input. Please enter valid numbers.")
    
"""
Определение функций addition, subtraction, multiplication и division, которые выполняют соответствующие операции над двумя числами и возвращают результат.

b - это строка, которая содержит сообщение, запрашивающее у пользователя ввести второе число.

try:: Это начало блока "try", в котором помещаются инструкции, которые могут вызвать исключение. В данном случае, код ожидает ввод пользователем двух чисел, операции и выполняет выбранную операцию.

num1 и num2 - это переменные, в которых хранятся введенные пользователем числа.

operation - это переменная, в которой хранится выбранная пользователем операция.

В блоке if operation == ... выполняются операции, соответствующие выбору пользователя, и результат присваивается переменной result.

Если пользователь выбирает недопустимую операцию, result устанавливается в "Invalid operation choice".

После выполнения выбранной операции, код выводит результат или сообщение об ошибке.

except ValueError:: Это начало блока "except", который будет выполнен, если возникнет исключение ValueError.

print("Invalid input. Please enter valid numbers."): В случае возникновения ValueError, код выводит сообщение "Invalid input. Please enter valid numbers."
"""