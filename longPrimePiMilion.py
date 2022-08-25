import datetime
import decimal
import math

print(datetime.datetime.now())

# using a file with 1,000,000 decimals of pi from https://www.angio.net/pi/digits/pi1000000.txt

#open text file in read mode
text_file = open("pi1000000.txt", "r")
#read whole file to a string
data = text_file.read() 
#close file
text_file.close()


# get string only with decimals 
stringLongDecimal = str(data)[2::]
#print(stringLongDecimal)


def isPalindrome(s):
    return s == s[::-1]
    

# function to check if num is prime
def isprime(num):
    if num> 1:  
        for n in range(2,num):  
            if (num % n) == 0:  
                return False
        return True
    else:
        return False
    
    
# check if start and end of each block is the same digit
print('Starting the search\n')

for i in range(0, len(stringLongDecimal) - 8):
    block = stringLongDecimal[i:i+9]
    
    if block[0] == block[8]:
        #print(block)
        
        #check if first number is equal a 1, 3, 5, 7, 9
        if block[0] in ('1', '3', '5', '7', '9'):
            #print ("is possible....", block)
            
            # check if is palindrome
            if isPalindrome(block):
                print("is Palindrome", block)
                
                # check if is prime
                if isprime(int(block)):
                    print(block, "is prime!!!!!!!!!")
                    break
                    
                    
print('Finished')
print(datetime.datetime.now())