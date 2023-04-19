num=int(input("Enter a number:"))
x=num
sum=0            
while num!=0:
            rem=num%10
            sum=sum+rem*rem*rem
            num=num//10
if x == sum:
    print("Given number is armstrong number")
else:
    print("Not an armstrong number")            
            
