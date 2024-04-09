from appliances import Appliance

class CoffeeMaker(Appliance):

    def __init__(self, color, heat_method):
        self.color = color
        self.heat_method = heat_method

    def make_coffee(self):
        print("gurgle, gurgle. Ding. Your drug of choice is piping hot and ready!")
