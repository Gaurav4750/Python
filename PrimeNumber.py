# Program to validate prime number and find divisible numbers.

flag = False
number = input("Enter the number: ")

# To validate the number entered is prime number or not
if int(number)>1:
    for j in range(2, int(number)):
        if (int(number) % j) == 0:
            flag = True           
if flag:
    print(str(number)+" is a not a Prime Number.")
else:
    print(str(number)+" is a Prime Number.")

# To find the divisible numbers for the entered numbber.
for i in range (2, int(number)//2+1):
    if int(number)%i !=0:
        continue
    print("%s is divisible by %d"%(number,i))
