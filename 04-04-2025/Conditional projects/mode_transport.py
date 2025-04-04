# Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).
distance=float(input("How much distance you ahve to travel : "))

if distance < 3:
    print("You can walk")
elif 3<=distance<=15:
    print("Use auto or Bike")
else:
    print("Use a car")