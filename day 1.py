f = open("data","r")
fr = f.readlines()

def Fuel_Counter_Upper():
    fuel = 0
    for i in fr:
        x = int(i)

        while x > 0:
            x = ((x//3)-2)
            if x > 0:
                fuel += x
    print(fuel)
Fuel_Counter_Upper()
