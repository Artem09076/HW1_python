n=int(input())
name= n%10
if n >= 11 and n <= 14:#В отрезки от 11 до 14 нужно писать "korov"
        print(n, "korov")
elif name==0 or (name>=5 and name<=9):#Остаток от деления на 10=0 или от 5 до 9
        print(n, "korov")
elif name==1:#Остаток от деления 1 то нужно выводить "korova"
        print(n,"korova")
elif name>=2:#Остаток от делиния 2 то нужно выводить "korovy"
        print(n,"korovy")
