#check input number is prime or perfect
#prime is a number which is only divisible by 1 and itself
# perfect number is a number which is equal to the sum of its proper divisors excluding itself 6 = 1+2+3 =6
num = int(input("Enter a number: "))
def prime(num):
    if num>0:
        for i in range(2,num):
            if num%i==0:
                return "Not Prime"
        return "Prime"
print(f"The number {num} is {prime(num)}")
def perfect(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    if sum==num:
        return "Perfect Number"
    else:
        return "Not a Perfect Number"
    
print(f"The number {num} is {perfect(num)}")
#Factorial is number multiplied by all positive integers less than itself
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
fact = factorial(num)
print(f"The factorial of {num} is {fact}")
# fabonacci series is a series in which each number is the sum of the two preceding ones starting from 0 and 1
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    return fib_sequence[:n]
fib_series = fibonacci(num)
print(f"The first {num} numbers in the Fibonacci series are: {fib_series}")
#Fibonacci series another way
# n =[0,1]
# for i in range(num):
#     n.append(n[-1]+n[-2])
#     print(n[-1],end=" ")
# print("Another way to get Fibonacci series: ",n)

#Check if a number is Armstrong number
def is_armstrong(num):
    n =0
    # count = len(str(num))
    count = 0
    temp = num  
    while temp > 0:
        temp //= 10
        count += 1
    temp = num
    while(num>0):
        n +=( num%10 ) **count #3**3 + 7**3 + 1**3
        num =abs(num//10) #15
        print("Intermediate sum of digits:",n)
        print("Remaining number after removing last digit:",num)
    if(n==temp):
        print("Armstrong number sum of digits:",n)
        return "Armstrong number"
    else:
        return "Not an Armstrong number"
print(is_armstrong(num))
#Another way to check Armstrong number

armstrong_list =[]
even_armstronsg_list =[]
#store the armstrong numbers in a list and print the list at the end 
print("Armstrong numbers between 1 and 1000:")
for i in range(1,1000):
    # c = len(str(i))
    c = 0 #counter for digits
    temp  = i
    armstrong_num =0   
    while temp>0:
        temp =temp//10 # remove last digit
        c += 1
    temp = i
    while temp>0:
        armstrong_num += (temp%10) ** c
        temp = temp//10
    if armstrong_num == i and armstrong_num %2 !=0:
        armstrong_list.append(armstrong_num)
    #Armstrong number + even number
    if armstrong_num == i and armstrong_num % 2 ==0:
        even_armstronsg_list.append(armstrong_num)
print("Even Armstrong numbers between 1 and 1000:", even_armstronsg_list)
print(" Odd Armstrong numbers between 1 and 1000:", armstrong_list)
# print("Armstrong numbers between 1 and 1000:", [num for num in range(1,1000) if sum(int(digit)**len(str(num)) for digit in str(num)) == num])
print("Sum of all Armstrong numbers between 1 and 1000:", sum(armstrong_list))
print("Maximum Armstrong number between 1 and 1000:", max(armstrong_list))
print("Count of Armstrong numbers between 1 and 1000:", len(armstrong_list))

print(" Shorthend of finding Armstrong numbers between 1 and 1000:",
      [num for num in range(1,1000)
        if sum(int(digit)**len(str(num))
                for digit in str(num)) == num])


def armstrongnumber(start, end):
    armstrong_nums = []
    for num in range(start, end + 1):
        order = len(str(num))
        sum_of_powers = sum(int(digit) ** order for digit in str(num))
        if sum_of_powers == num:
            armstrong_nums.append(num)
    return armstrong_nums
start_range = int(input("Enter the start of range: "))
end_range = int(input("Enter the end of range: "))
armstrong_numbers = armstrongnumber(start_range, end_range)
print(f"Armstrong numbers between {start_range} and {end_range}: {armstrong_numbers}")



#Check if a number is palindrome
word_data = ["radar", "google", "level", "python", "madam", "kayak"]
# palindromes = []
# for word in word_data:
#     print(f"Checking word: {word}")
#     if word == word[::-1]:
#         palindromes.append(word)
#         print(f"{word} is a palindrome.")
#     else:
#         print(f"{word} is not a palindrome.")
# print(f"Palindromic words from the list: {palindromes}")
# #ith list comprehension
# palindromes = [word for word in word_data if word == word[::-1]]    
# print(f"Palindromic words from the list: {palindromes}")
# check if a string is palindrome with out using slicing
def is_palindrome(word): 
    word = word.lower()  # Convert to lowercase for case-insensitive comparison   
    left, right = 0, len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True
palindromic_words = []
for word in word_data:
    if is_palindrome(word):
        palindromic_words.append(word)
# palindromic_words = [word for word in word_data if is_palindrome(word)]

print(f"Palindromic words from the list: {palindromic_words}")
print(" Palindromic words from the list using list comprehension:",
      [word for word in word_data if is_palindrome(word)])
#Another way to check palindrome for number
number = int(input("Enter a number to check palindrome: "))
# print(number%10) #1
# print(number//10) #12
temp =number
reversed_num =0
while number>0:
    rem =number%10
    number =number//10
    reversed_num = reversed_num *10 + rem
if reversed_num == temp:
    print(f"{temp} is a palindrome")
else:
    print(f"{temp} is not a palindrome")

#Finding all palindromic numbers between 1 and 1000

palidrome_numbers = []
for num in range(1, 1001):
    temp = num
    reversed_num = 0
    while num > 0:
        rem =num%10
        num =num//10
        reversed_num = reversed_num *10 + rem
    if reversed_num == temp:
        palidrome_numbers.append(temp)
print("Palindromic numbers between 1 and 1000:", palidrome_numbers)
print("Sum of Palindromic numbers between 1 and 1000:", sum(palidrome_numbers))
print("Count of Palindromic numbers between 1 and 1000:", len(palidrome_numbers))
print("Maximum Palindromic number between 1 and 1000:", max(palidrome_numbers))
print(" Shorthend of finding Palindromic numbers between 1 and 1000:",
      [num for num in range(1,1001)
        if str(num) == str(num)[::-1]])



