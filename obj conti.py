class Vacation:

    def __init__(self, place, distance, weather):
        self.place = place 
        self.distance = distance
        self.weather = weather

    def tuesday(self):
        print("We will be hiking on Tuesday")

summer = Vacation("Hawaii",2000,"Sunny")

summer.weather = "rainy"
summer.rating = 10
print(summer)
print(summer.rating)
print(summer.weather)
summer.tuesday()