usernames = ["Alice"," bob", "ALICE    ", "Bob", "charlie", "Charlie","JOHN"]
S1= {name.lower().strip() for name in usernames}
print(S1)
 
 