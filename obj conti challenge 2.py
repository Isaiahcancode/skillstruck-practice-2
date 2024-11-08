class Shopping:
    def __init__(self, item, quality):
        self.item = item
        self.quality = quality
        self.total = []

    def spending(self, cost):
        self.total.append(cost)


sportStore = Shopping("Kayak", "High Quality")


sportStore.spending(100)
sportStore.spending(200)
sportStore.spending(150)


print(sportStore.total)
