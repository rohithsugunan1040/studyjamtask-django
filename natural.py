n=int(input("Enter the number: "))
summ=0
if n<1:
    print("no natural numbers exist")
else:
    for i in range(1,n+1):
        summ+=i
    print("The sum of first",n,"natural numbers is",summ)