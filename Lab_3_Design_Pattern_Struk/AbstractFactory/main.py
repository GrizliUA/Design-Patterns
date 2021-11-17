from AbstractFactory import Preparation, Customization, C_Factory

if __name__ == '__main__':
    s = Preparation(
        milk=600.0,           # ml
        water=float("inf"),   # ml
        sugar=300.0,          # g
        coke=1000.0,          # ml
        Coffee=200.0,         # g
        lemonjuice=500,       # ml
        teabags=47)           # pcs

    c = Customization(
        extraMilk = 0,
        sugar = 0,
        mugSize = 0)

    '''
    Menu:
        - Cappucino
        - Black Coffee
        - Lemonade
        - Hot Milk
        - Coca Cola
        
    Customization:
        Extra Milk:
            0 - No extra milk
            1 - extra milk
        Sugar:
            N - 'Any amount of tablespoons'
        Mug size:
            0 - Small     150 ml
            1 - Standart  250 ml
            2 - Big       400 ml
            3 - Huge      600 ml
    '''

    def function_1():
        print("Choose customatization for your Cappucino")
    def function_2():
        print("Choose customatization for your Black Coffee")
    def function_3():
        print("Choose customatization for your Lemonade")
    def function_4():
        print("Choose customatization for your Hot Milk")
    def function_5():
        print("Choose customatization for your Coca Cola")








    
    '''Use this command to check items in stock ->'''
    #print(f"\n\nMilk: {s.milk} ml\nWater: {s.water} ml\nSugar: {s.sugar} g\nCoke: {s.coke} ml\nCoffee: {s.Coffee} g\nLemon juice: {s.lemonjuice} ml\nTea Bags: {s.teabags} pcs\n")
    
    #print("Your order:")
    #product_a = C_Factory().getCappucino(c,s).make(Customization(0,0,3),s)
    #print(product_a)

    #product_b = C_Factory().getBlackCoffee(c,s).make(Customization(0,0,3),s)
    #print(product_b)

    #product_c = C_Factory().getLemonade(c,s).make(Customization(0,0,3),s)
    #print(product_c)

    #product_d = C_Factory().getHotMilk(c,s).make(Customization(0,0,2),s)
    #print(product_d)

    #product_e = C_Factory().getCocaCola(c,s).make(Customization(0,0,3),s)
    #print(product_e)

    #print(f"\n\nMilk: {s.milk} ml\nWater: {s.water} ml\nSugar: {s.sugar} g\nCoke: {s.coke} ml\nCoffee: {s.Coffee} g\nLemon juice: {s.lemonjuice} ml\nTea Bags: {s.teabags} pcs\n")
    print("\033c")
    print("Hello in our cafe, what do you want to order?")
    a = int(input("Menu:\n\t1 - Cappucino\n\t2 - Black Coffee\n\t3 - Lemonade\n\t4 - Hot Milk\n\t5 - Coca Cola\n"))
    
    if a == 1:
        print("\033c")
        x = int(input("Choose customatization for your Cappucino\n\tExtra Milk:\n\t\t0 - No extra milk\n\t\t1 - extra milk\n"))
        if x <= 0: x = 0
        else: x = 1
        print("\033c")
        y = int(input("Choose customatization for your Cappucino\n\tSugar:\n\t\tN - 'Any amount of tablespoons\n"))
        print("\033c")
        z = int(input("Choose customatization for your Cappucino\n\tMug size:\n\t\t0 - Small     150 ml\n\t\t1 - Standart  250 ml\n\t\t2 - Big       400 ml\n\t\t3 - Huge      600 ml\n"))
        print("\033c")
        print("Your order:\t")
        print(C_Factory().getCappucino(c,s).make(Customization(x,y,z),s))
    elif a == 2:
        print("\033c")
        x = int(input("Choose customatization for your Black Coffee\n\tExtra Milk:\n\t\t0 - No extra milk\n\t\t1 - extra milk\n"))
        if x <= 0: x = 0
        else: x = 1
        print("\033c")
        y = int(input("Choose customatization for your Black Coffee\n\tSugar:\n\t\tN - 'Any amount of tablespoons\n"))
        print("\033c")
        z = int(input("Choose customatization for your Black Coffee\n\tMug size:\n\t\t0 - Small     150 ml\n\t\t1 - Standart  250 ml\n\t\t2 - Big       400 ml\n\t\t3 - Huge      600 ml\n"))
        print("\033c")
        print("Your order:\t")
        print(C_Factory().getBlackCoffee(c,s).make(Customization(x,y,z),s))
    elif a == 3:
        print("\033c")
        y = int(input("Choose customatization for your Lemonade\n\tSugar:\n\t\tN - 'Any amount of tablespoons\n"))
        print("\033c")
        z = int(input("Choose customatization for your Lemonade\n\tMug size:\n\t\t0 - Small     150 ml\n\t\t1 - Standart  250 ml\n\t\t2 - Big       400 ml\n\t\t3 - Huge      600 ml\n"))
        print("\033c")
        print("Your order:\t")
        print(C_Factory().getLemonade(c,s).make(Customization(0,y,z),s))
    elif a == 4:
        print("\033c")
        y = int(input("Choose customatization for your Hot Milk\n\tSugar:\n\t\tN - 'Any amount of tablespoons\n"))
        print("\033c")
        z = int(input("Choose customatization for your Hot Milk\n\tMug size:\n\t\t0 - Small     150 ml\n\t\t1 - Standart  250 ml\n\t\t2 - Big       400 ml\n\t\t3 - Huge      600 ml\n"))
        print("\033c")
        print("Your order:\t")
        print(C_Factory().getHotMilk(c,s).make(Customization(0,y,z),s))
    elif a == 5:
        print("\033c")
        z = int(input("Choose customatization for your Coca Cola\n\tMug size:\n\t\t0 - Small     150 ml\n\t\t1 - Standart  250 ml\n\t\t2 - Big       400 ml\n\t\t3 - Huge      600 ml\n"))
        print("\033c")
        print("Your order:\t")
        print(C_Factory().getCocaCola(c,s).make(Customization(0,0,z),s))
    else: "Error, please enter number 1 - 5"