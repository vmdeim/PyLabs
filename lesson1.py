
# Задание 1 : Заменить х на у
Xold = "faesgxwefxfwefgx"
Xnew = ""

for x in Xold:
    if x == "x":
        Xnew+= "y"
    else:
        Xnew += x
print ("Строка с заменой = ",Xnew)

# Задание 2 : Сосчитать произведение кратных 3 и 5
y = [1,5,6,1,14,15,3,5,7]
pp = 1
for x in y:
    if x//5 == x/5 and x//3 == x/3:
        pp=pp*x
print ("Произведение = ",pp)

# Задание 3 : Заменить х на у одной строкой
Xold = "faesgxwefxfwefgx"
Xnew = Xold.replace("x","y")
print ("Строка с заменой = ",Xnew)
