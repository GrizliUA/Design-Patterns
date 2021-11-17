from dataclasses import dataclass
from abc import ABC,abstractmethod

@dataclass
class Customization:
    extraMilk:float
    sugar:float
    mugSize:float

@dataclass
class Preparation:
    milk:float
    water:float
    sugar:float
    coke:float
    Coffee:float
    lemonjuice:float
    teabags:float


class Product(ABC):
    @abstractmethod
    def make(self,cust:Customization,stock:Preparation):
        pass


class Cappucino(Customization,Product):
    def make(self,cust:Customization,stock:Preparation):
        mug_dict_ml = {
        0 : 150,
        1 : 250,
        2 : 400,
        3 : 600}
        error = False
        try:
            cup_size = mug_dict_ml[cust.mugSize]
        except:return'Key error'
        
        if(stock.milk < cup_size*0.4 + cup_size*0.1*cust.extraMilk):
            print('\n\tNot enough milk')
            error = True
        if(stock.water < cup_size*0.4):
            print('\n\tNot enough water')
            error = True
        if(stock.sugar < cust.sugar*10):
            print('\n\tNot enough sugar')
            error = True
        if(error == True):
            return '\tCan`t make a cappucino'
        milk_dict = {
            0 : 'out',
            1 : ''}
        mug_dict = {
            0 : 'Small ',     # 150 ml
            1 : 'Standart ',  # 250 ml
            2 : 'Big ',       # 400 ml
            3 : 'Huge '}      # 600 ml
            
        if(cust.extraMilk == 1): stock.milk -= cup_size*0.5
        if (cust.sugar == 0):
            return f"\t{mug_dict[cust.mugSize]}cappucino with{milk_dict[cust.extraMilk]} extra milk without sugar"
        elif (cust.sugar == 1):
            stock.sugar = stock.sugar - 10
            return f"\t{mug_dict[cust.mugSize]}cappucino with{milk_dict[cust.extraMilk]} extra milk and with {cust.sugar} tablespoon of sugar"
        else: 
            stock.sugar -= cust.sugar * 10
            return f"\t{mug_dict[cust.mugSize]}cappucino with{milk_dict[cust.extraMilk]} extra milk and with {cust.sugar} tablespoons of sugar"
    
class BlackCoffee(Customization,Product):
    def make(self,cust:Customization,stock:Preparation):   #
        mug_dict_ml = {
        0 : 150,
        1 : 250,
        2 : 400,
        3 : 600}
        milk_dict = {
            0 : 'out',
            1 : ''}
        mug_dict = {
            0 : 'Small ',     # 150 ml
            1 : 'Standart ',  # 250 ml
            2 : 'Big ',       # 400 ml
            3 : 'Huge '}      # 600 ml
        error = False
        try:
            cup_size = mug_dict_ml[cust.mugSize]
        except:return'Key error'


        if(stock.Coffee < cup_size/15):
            print('\n\tNot enough liquid coffee')
            error = True
        else: stock.Coffee -= cup_size/15
        if(stock.water < cup_size*0.8):
            print('\n\tNot enough water')
            error = True
        if(stock.sugar < cust.sugar*10):
            print('\n\tNot enough sugar')
            error = True
        if(error == True):
            return '\tCan`t make a black coffee'
        if(cust.extraMilk == 1): stock.milk -= cup_size*0.1
        if (cust.sugar == 0):
            return f"\t{mug_dict[cust.mugSize]}black coffee with{milk_dict[cust.extraMilk]} extra milk without sugar"
        elif (cust.sugar == 1):
            stock.sugar = stock.sugar - 10
            return f"\t{mug_dict[cust.mugSize]}black coffee with{milk_dict[cust.extraMilk]} extra milk and with {cust.sugar} tablespoon of sugar"
        else: 
            stock.sugar -= cust.sugar * 10
            return f"\t{mug_dict[cust.mugSize]}black coffee with{milk_dict[cust.extraMilk]} extra milk and with {cust.sugar} tablespoons of sugar"

class Lemonade(Customization,Product):
    def make(self,cust:Customization,stock:Preparation):
        if (cust.extraMilk != 0):
            return "\tSorry, no extra milk in Lemonade"
        mug_dict_ml = {
        0 : 150,   #  
        1 : 250,   #  220    2
        2 : 400,   #  350    3  
        3 : 600}   #  550    4
        mug_dict = {
            0 : 'Small ',     # 150 ml
            1 : 'Standart ',  # 250 ml
            2 : 'Big ',       # 400 ml
            3 : 'Huge '}      # 600 ml
        error = False
        try:
            cup_size = mug_dict_ml[cust.mugSize]
        except:return'Key error'


        if(stock.lemonjuice < cup_size*0.2):
            print('\n\tNot enough lemon juice')
            error = True
        else: stock.lemonjuice -= cup_size*0.2
        if(stock.water < cup_size*0.8):
            print('\n\tNot enough water')
            error = True
        if(stock.sugar < cust.sugar*10):
            print('\n\tNot enough sugar')
            error = True
        if(error == True):
            return '\tCan`t make a Lemonade'
        if (cust.sugar == 0):
            return f"\t{mug_dict[cust.mugSize]}lemonade without sugar"
        elif (cust.sugar == 1):
            stock.sugar = stock.sugar - 10
            return f"\t{mug_dict[cust.mugSize]}lemonade with {cust.sugar} tablespoon of sugar"
        else: 
            stock.sugar -= cust.sugar * 10
            return f"\t{mug_dict[cust.mugSize]}lemonade with {cust.sugar} tablespoons of sugar"

class HotMilk(Customization,Product):
    def make(self,cust:Customization,stock:Preparation):
        if (cust.extraMilk != 0):
            return "\tSorry, no extra milk in Hot Milk"
        mug_dict_ml = {
        0 : 150,
        1 : 250,
        2 : 400,
        3 : 600}
        error = False
        try:
            cup_size = mug_dict_ml[cust.mugSize]
        except:return'Key error'
        if(stock.milk < cup_size):
            print('\n\tNot enough milk')
            error = True
        else: stock.milk -= cup_size
        if(stock.sugar < cust.sugar*10):
            print('\n\tNot enough sugar')
            error = True
        if(error == True):
            return '\tCan`t make a hot milk'
        mug_dict = {
            0 : 'Small ',     # 150 ml
            1 : 'Standart ',  # 250 ml
            2 : 'Big ',       # 400 ml
            3 : 'Huge '}      # 600 ml
            
        if (cust.sugar == 0):
            return f"\t{mug_dict[cust.mugSize]}hot milk without sugar"
        elif (cust.sugar == 1):
            stock.sugar = stock.sugar - 10
            return f"\t{mug_dict[cust.mugSize]}hot milk with {cust.sugar} tablespoon of sugar"
        else: 
            stock.sugar -= cust.sugar * 10
            return f"\t{mug_dict[cust.mugSize]}hot milk with {cust.sugar} tablespoons of sugar"

class CocaCola(Customization,Product):
    def make(self,cust:Customization,stock:Preparation):
        if (cust.extraMilk != 0 or cust.sugar != 0):
            return "\tSorry, no extra milk or sugar in Coca Cola"
        mug_dict_ml = {
        0 : 150,
        1 : 250,
        2 : 400,
        3 : 600}
        error = False
        try:
            cup_size = mug_dict_ml[cust.mugSize]
        except:return'Key error'
        if(stock.coke < cup_size):
            print('\n\tNot enough coca cola')
            error = True
        else: stock.coke -= cup_size
        if(error == True):
            return '\tCan`t make a coca cola'
        mug_dict = {
            0 : 'Small ',     # 150 ml
            1 : 'Standart ',  # 250 ml
            2 : 'Big ',       # 400 ml
            3 : 'Huge '}      # 600 ml
        return f"\t{mug_dict[cust.mugSize]}coca cola"




class A_Factory(ABC):
    @abstractmethod
    def getCappucino(self,cust:Customization,stock:Preparation) -> Product:
        pass
    @abstractmethod
    def getBlackCoffee(self,cust:Customization,stock:Preparation) -> Product:
        pass
    @abstractmethod
    def getLemonade(self,cust:Customization,stock:Preparation) -> Product:
        pass
    @abstractmethod
    def getHotMilk(self,cust:Customization,stock:Preparation) -> Product:
        pass
    @abstractmethod
    def getCocaCola(self,cust:Customization,stock:Preparation) -> Product:
        pass



class C_Factory(A_Factory):
    def getCappucino(self,cust:Customization,stock:Preparation) -> Product:
        return Cappucino(stock,cust,0)
    def getBlackCoffee(self,cust:Customization,stock:Preparation) -> Product:
        return BlackCoffee(stock,cust,0)
    def getLemonade(self,cust:Customization,stock:Preparation) -> Product:
        return Lemonade(stock,cust,0)
    def getHotMilk(self,cust:Customization,stock:Preparation) -> Product:
        return HotMilk(stock,cust,0)
    def getCocaCola(self,cust:Customization,stock:Preparation) -> Product:
        return CocaCola(stock,cust,0)


