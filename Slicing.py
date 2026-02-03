n =[1,2,3,4,5,6,7,8,9,10]
#ways to slice a list

print(n[::])  # prints the entire list
print(n[::2]) # prints every second element
print(n[1::2]) # prints every second element starting from index 1
print(n[::-1]) # prints the list in reverse order
print(n[-1]) # prints the last element
print(n[-2]) # prints the second last element

print(n[5:1:-1]) # prints elements from index 5 to 2 in reverse order
print(n[3:7]) # prints elements from index 3 to 6
print(n[:5]) # prints the first five elements
print(n[5:]) # prints elements from index 5 to the end
print(n[-1::-1]) # prints the list in reverse order using negative indexing
print(n[-3:]) # prints the last three elements
print(n[:-3]) # prints all elements except the last three
print(n[-5:-1]) # prints elements from index -5 to -2
print(n[2:-2]) # prints elements from index 2 to -3
print("a"**3) # prints 'aaa'
print("abc"[::-1]) # prints 'cba'
