# This function finds Armstrong numbers between 1 and 154 and stores them in a dictionary.

def dic_arm():
    dictonary1 = {}
    even_armstron_numbers = []
    odd_armstron_numbers = []
    palindrom_nums = []
    
    for num in range(1,155):
        count =0
        temp =num
        armstrong_numbers = 0
        palin =0
        while temp>0:
            temp = temp//10
            count +=1   
        temp = num
        while temp>0:
            rem = temp%10
            palin = palin*10 + rem
            armstrong_numbers +=(temp%10)**count
            temp = temp//10
        if palin == num:
            palindrom_nums.append(palin)
        if armstrong_numbers == num and armstrong_numbers %2 ==0:
            even_armstron_numbers.append(armstrong_numbers)
        elif armstrong_numbers == num and armstrong_numbers %2 !=0:
            odd_armstron_numbers.append(armstrong_numbers)
    dictonary1["Even Armstrong Numbers"] = even_armstron_numbers
    dictonary1["Odd Armstrong Numbers"] = odd_armstron_numbers
    dictonary1["Palindrome Numbers"] =  palindrom_nums
    dictonary1[ "Totla found Palindrome numbers"] = len(palindrom_nums)
    dictonary1[" Total Even Armstrong Numbers"] =len(even_armstron_numbers)
    dictonary1[" Total Odd Armstrong Numbers"] =len(odd_armstron_numbers)
    dictonary1["Total numbers in Dict"] =len(even_armstron_numbers)+ len(odd_armstron_numbers)+len(palindrom_nums)
    return dictonary1   
print(dic_arm())
