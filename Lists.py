usernames = ["Alice"," bob", "ALICE    ", "Bob", "charlie", "Charlie","JOHN"]
S1= {name.lower().strip() for name in usernames} 
#strip is used to remove leading and trailing spaces
print(S1)
 
user_ids = [101, 102, 103, 101, 104, 102, 105]
S2= {uid for uid in user_ids if uid % 2 == 0}       

#List is an ordered collection that allows duplicate elements and mutable collection
# while a Set is an unordered collection that automatically removes duplicates.
my_list = [10, 2, 5, 4, 2]
my_list.sort(reverse=True)
print(my_list)