#test multiplications

nb = input("nombre à multiplier : ")
x = input("table maximale souhaité : ")
i = 0
x = int(x)
nb = int(nb)
while i < x :
  print(i+1, "*", nb, "=", i + 1*nb)
  i = i+1
