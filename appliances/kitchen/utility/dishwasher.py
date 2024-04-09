from appliances import Appliance

class DishWasher(Appliance):

    def __init__(self, color, heat_method):
        super().__init__(color, heat_method)

    def wash_dishes(self):
        print("grind, grind, clunk. Time to call the repair person")
