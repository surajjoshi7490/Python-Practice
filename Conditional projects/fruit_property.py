''' Determine it a fruit : Green = unripe ,  yellow = Ripe  , Brown = Operripe '''
fruit=str(input("Which Fruit is it : "))
color = str(input("What is the color of the fruit  : \nGreen , Yellow , Brown :  "))

if fruit=="Banana":
    if color == "Green":
     print("Unripe")
    elif color=="Yellow":
     print("Ripe")
    elif color=="Brown":
     print("Overripe")
else :
  print("Fruit is not banana ")