#Cumulative Calculator. 
# Instead of just adding two numbers and forgetting them, your program "remembers" the previous totals and keeps building on them.
#Think of it like a Bank Ledger or a Shopping Cart that keeps adding new items to your grand total.
c =0
def add(num1,num2):
    global c
    c = c + num1 + num2
   
for i in range(3):
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    add(n1,n2)  
    print(f"The total sum after 3 additions is: {c}")

def multiply(num1,num2):
    return num1 * num2
"""In our 'Bank Ledger' example,
 if the variable 'total_balance' is defined at the very top of your script and
   you want to update it inside a function, which keyword must you use?"""

#The global keyword acts like a 'key' that allows a function to reach out and modify a variable defined in the main program scope.

def sume(*n): #*n is used to take multiple arguments and the type of n is tuple so it will not change and can store duplicates
    total = 0
    for num in n:
        total += num
    return total
print(sume(2,2))

