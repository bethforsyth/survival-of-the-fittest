class locations:
    def __init__(self, x, y):
        self.location=[x,y]

grid = []
counter1=0
counter2=0
xrow=[]
while counter1 < 20:
    xrow.append(locations(counter1,counter2))
    counter2 += 1
    if counter2 > 20:
        counter2 = 0
        counter1 += 1
        grid.append(xrow)
        xrow=[]
print(grid)