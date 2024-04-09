from appliances.kitchen.utility.dishwasher import DishWasher
from appliances.laundry.washer import Washer
from appliances.laundry.dryer import Dryer
from appliances.kitchen.utility.refrigerator import Refrigerator
from appliances.kitchen.coffeemaker import CoffeeMaker



whirlpool_dishwasher = DishWasher("black", "electric")
whirlpool_dishwasher.wash_dishes()

samsung_washer = Washer("red", "gas", "normal")
samsung_washer.wash_clothes("normal")

samsung_dryer = Dryer("red", "gas", "low")
samsung_dryer.dry_clothes("low")

lg_fridge = Refrigerator("stainless", "electric")
lg_fridge.make_ice()

mr_coffee = CoffeeMaker("white", "electric")
mr_coffee.make_coffee()
