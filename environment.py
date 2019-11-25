<<<<<<< HEAD
envir = []
class position:
    def __init__(self, location_id, x, y):
        self.location=[location_id, x, y]

counter1=0
counter2=0
counter3=0
locations=[]
while counter2<21:
    locations.append(position(counter3, counter1, counter2))
    counter1+=1
    counter3+=1
    envir=[]

    if counter1>20:
        counter1-=20
        counter2+=1


# class position:
#     def __init__(self, location_id, x, y, temperature=0):
#         self.location=[location_id, x, y, temperature]

month = 1
if month > 12:
    month-=12

temperature = 20-((month-6)^2)/4

counter1=0
counter2=0
counter3=0


# while counter2<21:
#     environment.append(position(counter3, counter1, counter2).location)
#     counter1+=1
#     counter3+=1

#     if counter1>20:
#         counter1-=20
#         counter2+=1

print(locations)
=======
class location():
    """docstring for location"""
    def __init__(self, arg):
        super(location, self).__init__()
        self.arg = arg
>>>>>>> 435439dd3a84f4e748fac985101502c54a12f915
