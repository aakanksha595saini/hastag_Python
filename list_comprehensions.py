#comprehensions
"""list comprehensions as a sleek, one-line shortcut for creating new lists in Python. 
Instead of writing out a multi-line for loop, you can pack the logic into a single bracketed expression."""
#The Syntax: new_list = [expression for item in iterable if condition]
# 
print("Armstrong numbers between 1 and 1000:", 
      [num for num in range(1,1000) if sum(int(digit)**len(str(num)) for digit in str(num)) == num])

armstrong_numbers = [
    n for n in range(1, 10001)

    if (
        #(variable := value, comparison)[1] way to perform an assignment 
        # inside a list comprehension's if clause and then immediately use it for a check.
        (order := (1 if n < 10 else 2 if n < 100 else 3 if n < 1000 else 4 if n < 10000 else 5)),
        # 2. Extract digits and sum them (assuming up to 5 digits for this range)
        n == (
            ((n // 10000) % 10)**order +
            ((n // 1000) % 10)**order +
            ((n // 100) % 10)**order +
            ((n // 10) % 10)**order +
            (n % 10)**order
        )
    )[1]
     #The [1] at the end tells the if statement: 
     # "Ignore the first part of this tuple and only look at the second part to decide if you should keep the number."
]
print(armstrong_numbers)
# The expression inside the 'if'
# (
#     order := 3,                     # Index [0]
#     153 == (1^3 + 5^3 + 3^3)        # Index [1] (This evaluates to True)
# )[1]                                # We grab index [1], so the 'if' sees 'True