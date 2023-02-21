n=int(input())
name= n%10
if n >= 11 and n <= 14:
        print(n, "korov")
elif name==0 or (name>=5 and name<=9):
        print(n, "korov")
elif name==1:
        print(n,"korova")
elif name>=2:
        print(n,"korovy")
