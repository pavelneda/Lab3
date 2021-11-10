import json
import os
from datetime import datetime
class Pizza:
    def __init__(self,name,ingradients):
        self.name=name
        self.ingradients=ingradients
    def __str__(self):
        return f'Pizza: {self.__name}\nIngradients: {self.__ingradients}'
    def addingradients(self,ingradients):
        if not all(isinstance(ingradient,str) for ingradient in ingradients):
            raise TypeError("ingradient must be string")
        if not all(ingradient for ingradient in ingradients):
            raise ValueError("ingradient value not correct")
        if not os.path.isfile("ingradients_list.json"):
            raise FileNotFoundError("File not found")
        with open("ingradients_list.json", "r+") as file:
            ing_list = json.load(file)
            for ingradient in ingradients:
                if not ingradient in ing_list.keys() or ing_list[ingradient]<=0:
                    raise ValueError("Ingredients are not available")
                ing_list[ingradient]-=1
            file.seek(0)
            file.truncate()
            json.dump(ing_list, file, indent=4)
        self.__ingradients.extend(ingradients)
    def removeingradient(self,ingradients):
        if not all(isinstance(ingradient,str) for ingradient in ingradients):
            raise TypeError("ingradient must be string")
        if not all(ingradient for ingradient in ingradients):
            raise ValueError("ingradient value not correct")
        if not os.path.isfile("ingradients_list.json"):
            raise FileNotFoundError("File not found")
        with open("ingradients_list.json", "r+") as file:
            ing_list = json.load(file)
            for ingradient in ingradients:
                if not (ingradient in ing_list.keys() and ingradient in self.__ingradients):
                    raise ValueError("Ingredients are not available")
                ing_list[ingradient]+=1
                self.__ingradients.remove(ingradient)
            file.seek(0)
            file.truncate()
            json.dump(ing_list, file, indent=4)
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        if not isinstance(name,str):
            raise TypeError("name must be string")
        if not name:
            raise ValueError("name value not correct")
        self.__name=name
    @property
    def ingradients(self):
        return self.__ingradients
    @ingradients.setter
    def ingradients(self,ingradients):
        if not all(isinstance(ingradient,str) for ingradient in ingradients):
            raise TypeError("ingradient must be string")
        if not all(ingradient for ingradient in ingradients):
            raise ValueError("ingradient value not correct")
        if not os.path.isfile("ingradients_list.json"):
            raise FileNotFoundError("File not found")
        with open("ingradients_list.json", "r+") as file:
            ing_list = json.load(file)
            for ingradient in ingradients:
                if not ingradient in ing_list.keys() or ing_list[ingradient]<=0:
                    raise ValueError("Ingredients are not available")
                ing_list[ingradient]-=1
            file.seek(0)
            file.truncate()
            json.dump(ing_list, file, indent=4)
        self.__ingradients=ingradients
class Pizza_day(Pizza):
    def __init__(self):
        if datetime.today().strftime('%A')=="Monday":
            super().__init__("Margherita",["tomato","mozzarella","oregano"])
        elif datetime.today().strftime('%A')=="Tuesday":
            super().__init__("Four seasons",["tomato","mozzarella","mushrooms","ham","oregano","olives"])
        elif datetime.today().strftime('%A')=="Wednesday":
            super().__init__("Marinara",["tomato","garlic","basil"])
        elif datetime.today().strftime('%A')=="Thursday":
            super().__init__("Carbonara",["tomato","mozzarella","parmesan","eggs","bacon"])
        elif datetime.today().strftime('%A')=="Friday":
            super().__init__("Four cheeses",["tomato","mozzarella","parmesan"])
        elif datetime.today().strftime('%A')=="Saturday":
            super().__init__("Neapoletano",["tomato","mozzarella","oregano","anchovies"])
        else:
            super().__init__("Crudo",["tomato","mozzarella","ham"])
    
           
a=Pizza_day()
a.addingradients(["ham"])
a.removeingradient(["tomato"])
print(a)