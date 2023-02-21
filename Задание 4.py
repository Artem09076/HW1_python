a=int(input())
b=int(input())
c=int(input())
D=(b*b)-(4*a*c)
x1=(-b+D**0.5)/2*a
x2=(-b-D**0.5)/2*a
if D>0:
    print(x1,x2)
elif D==0:
    print(-b/(2*a))
elif D<0:
    print("")