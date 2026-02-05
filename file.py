#file handling
# How to open a file in Python
# Reading a file with Python (both at once or line-by-line)
# Writing to a file with Python
# Copy, move, rename, and delete files
# Check if a file or directory exists

# # r	open file for reading (default)
# w	open file for writing, truncating the file first
# x	create a new file and open it for writing
# a	Open for writing, append to the end of the file if it exists already
# t	Text mode (the default), can be used in combination with rwxa
# b	Binary mode (as opposed to text mode), can be used in combination with rwxa
# +	open a disk file for updating (reading and writing)

# file = open("functions.py")
# print(file.read())
# file.close()

with open('functions.py','w') as fun:
    
    for i in range(1, 5):
        fun.write(str(i))
    # for line in fun:
    #     print(line)
    text = fun.read()
print(text)
    