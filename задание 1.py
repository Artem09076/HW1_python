k = int(input())
m = int(input())
n = int(input())
if k<32000 and m<32000 and n<32000 and n>k:
    print(((m*k)+((n-k)*m))*2)
elif k<32000 and m<32000 and n<32000 and n<k:
    print((n*m)*2)
elif k<32000 and m<32000 and n<32000 and n==k:
    print((n*m)*2)