from appliances import Appliance

class Refrigerator(Appliance):

    def __init__(self, color, heat_method):
        self.color = color
        self.heat_method = heat_method

    def make_ice(self):
        print("grind, grind, clunk. Time to call the repair person")
