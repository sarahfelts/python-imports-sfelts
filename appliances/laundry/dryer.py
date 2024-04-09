from appliances.appliance import Appliance

class Dryer(Appliance):

    def __init__(self, color, heat_method, setting):
        super().__init__(color, heat_method)
        self.setting = setting

    def dry_clothes(self, setting):
        if setting != "low":
          print("Please allow 40 minutes for you clothes to come out crispy.")
        else:
          print("Please allow 40 minutes for your clothes to come out soggy.")
