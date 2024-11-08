class Friday:

    def __init__(self, activity, friend):
        self.activity = activity
        self.friend = friend
    def pictures(self):
        print("We took so many pictures!")
thisWeekend = Friday("Movie", "charlotte")
thisWeekend.money = 20
thisWeekend.friend = "Shane"
print(thisWeekend)
print(thisWeekend.money)
print(thisWeekend.friend)