envir = []
class environment:
    def __init__(self, location_id, x, y, temperature=0):
        self.location=[location_id, x, y, temperature]

    def position(self, location_id=1, x=0, y=0, temperature=0):
        self.location=[location_id, x, y, temperature]
        counter1=0
        counter2=0
        counter3=0
        while counter2<21:
            global envir
            envir.append(position(counter3, counter1, counter2).location)
            counter1+=1
            counter3+=1

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

environment.position
# while counter2<21:
#     environment.append(position(counter3, counter1, counter2).location)
#     counter1+=1
#     counter3+=1

#     if counter1>20:
#         counter1-=20
#         counter2+=1

print(envir)