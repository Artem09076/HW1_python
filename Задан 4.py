x=input()

edin=''
des=''
sot=''

if int(x) > 9:
    # преобразование десятков
    if int(x[0]) == 4:
        des = "XL"
    elif 9 > int(x[0]) >= 5:
        des = "L" + "X" * (int(x[0]) - 5)
    elif int(x[0]) == 9:
        des = "XM"
    elif int(x) == 100:
        des = "M"
    else:
        des = "X" * int(x[0])

# преобразование единиц
if x[-1] == "4":
    edin = "IV"
elif x[-1] == "5":
    edin = "V"
elif x[-1] == "6":
    edin = "VI"
elif x[-1] == "7":
    edin = "VII"
elif x[-1] == "8":
    edin = "VIII"
elif x[-1] == "9":
    edin = "IX"
elif x[-1] == "1":
    edin = "I"
elif x[-1] == "2":
    edin = "II" 
elif x[-1] == "3":
    edin = "III"

print(des + edin)

