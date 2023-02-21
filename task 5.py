a=int(input())
b=int(input())
if b%a==0:#Если при делении получается целое число 
    print(-b//a)
elif b==0:#Если  b=0 то при любом x ответом будет 0
    print("Inf")
else:
    print("No")
