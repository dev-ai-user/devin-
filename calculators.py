
#hello  there is an calculator wehich is used to perform basic operation for calculation
   

a = input("enter the first number ")
b = input("enter the second number ")
a =int(a)
b = int(b)
print ("the sum of the two nnumbers is :",a+b,)
print ("the  subtraction of the two nnumbers is :",a-b,)
print ("the percentage  of the two nnumbers is :",a%b,)
print ("the multiplication of the two nnumbers is :",a*b,)
print ("the  divide of the two nnumbers is :",a/b,)
print ("the  modulus of the two nnumbers is :",a//b,)
print ("the  power of the two nnumbers is :",a**b,)

if a+b==120:
    print (f"{a}={b}you are the winner of the contest and theb prixe money is 1000000 ")
elif a-b==0:
    print(f"{a} = {b}  you are having the rarest items that is rolls royce phantom")
else:
    print("better luck next time in the lockdown period we are giving you 1000 rs as a consolation prize ")
