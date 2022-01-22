# The prime number and divisible numbers.
flag = False
number = input("Enter the number: ")
if int(number)>1:
    for j in range(2, int(number)):
        if (int(number) % j) == 0:
            flag = True           
if flag:
    print(str(number)+" is a not a Prime Number.")
else:
    print(str(number)+" is a Prime Number.")

for i in range (2, int(number)//2+1):
    if int(number)%i !=0:
        continue
    print("%s is divisible by %d"%(number,i))
