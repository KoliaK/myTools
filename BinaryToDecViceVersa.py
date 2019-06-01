'''
BINTODEC()
Step1: Enter binary number.
Step2: Next take the length of the binary number.
Step3: Using for loop we convert binary to a decimal number.
       Just like if the binary number is 1111, then the calculation would be
       1*2**3+1*2**2+1*2**1+1*2**0 = 15
Step4: Display the number.

DECTOBIN()
Step1: Enter the decimal number.
Step2: Using while loop
   *Divide the number it by 2. Find both remainder and quotient. Take another variable initialized with 1. 
   Now remainder will be multiplied with this variable and added with the final output number. That variable will be incremented by 1.
   *The first remainder is the last digit in the sequence.
Step3: Display the value.
'''

print("*****************************************************")
print(" DECIMAL TO BINARY AND BINARY TO DECIMAL CONVERSION")
print("*****************************************************")
print(" For Decimal to Binary...Press 1.")
print(" For Binary to Decimal... Press 2")
print("*****************************************************")
my_choice=int(input("Enter your choice: "))
if my_choice==1:
   i=1
   s=0
   my_dec=int(input("Enter decimal to be converted: "))
   while my_dec>0:
      rem=int(my_dec%2)
      s=s+(i*rem)
      my_dec=int(my_dec/2)
      i=i*10
   print ("The binary of the given number is ",s,'.')
else:
   my_bin=input ('Enter binary to be converted: ')
   n=len(my_bin)
   res=0
   for i in range(1,n+1):
      res=res+ int(my_bin[i-1])*2**(n-i)
   print ("The decimal of the given binary is ",res,'.')
print("******************************************************")

'''
Output

*****************************************************
 DECIMAL TO BINARY AND BINARY TO DECIMAL CONVERSION
*****************************************************
print(" For Decimal to Binary...Press 1.")
print(" For Binary to Decimal... Press 2")
*****************************************************
Enter your choice: 1
Enter decimal to be converted: 15
The binary of the given number is 1111.
******************************************************

*****************************************************
 DECIMAL TO BINARY AND BINARY TO DECIMAL CONVERSION
*****************************************************
 For Decimal to Binary...Press 1.
 For Binary to Decimal... Press 2
*****************************************************
Enter your choice:  2
Enter binary to be converted:  1111
The decimal of the given binary is 15.
******************************************************
'''
