dis = {1: "dinesh", 2: "karthik"}
 
for i in (dis.values(), dis.keys()):
    # for extracting each values in iterable variable i in list form
    print("Dictionary Keys:", list(i))
print("Dictionary Values:", list(dis.values()))
 
dis = {1: "dinesh", 2: "karthik"}
#printing dictionary items
print("Dictionary Items:"+ str(dis.items()))
#extracting key,value pairs using for loop
for keys,values in dis.items():
    print(f"Key: {keys}, Value: {values}")
dis.keys() #for keys 
dis.values() #for value 
dis.items() #for (key, value) pairs
 