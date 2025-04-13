#chek if a number is even or odd
#write a python program that 1.Takes an integer input from the user.
#check wether the number is even or odd using an -if-else
#diplay the result accordingly.

input_number=(int(input("Enter a number : ")))

if(input_number % 2)==0:
    print("{0} is Even number ".format(input_number))

else:
    
    print("{0} is odd number".format(input_number))
