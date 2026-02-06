#String slicing
# Split the entered string after white space or any symbol and Print the Initials of 
class Stringcat:
    def getname(self, name,year):
        leap_year = [year if year>2000 and year <2030 and year%4 ==0 else "Not in range or leap"]
        # print(name.split())
        # print(type(name))
        Signature =''
        for i in (name.split() or name.split('.') or name.split(',')):
            print(type(i.capitalize()))
            Signature += i[0]+'.'
        # print(Signature.capitalize()) # used to capitalized the first char only
        print('Signature of the User {} and the leap year is {}'.format(Signature.upper(),leap_year))
name = input("Enter your name: ")
year =int(input("Enter the Gradution year: "))
obj =Stringcat()
obj.getname(name,year)
