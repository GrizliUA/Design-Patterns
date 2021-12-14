from abc import ABCMeta,abstractmethod
import os

class Appliance(metaclass=ABCMeta):
    def enabled(self):
        self.enabled = False

    @abstractmethod
    def start(self):
        self.enabled = True

    @abstractmethod
    def stop(self):
        self.enabled = False

class AC(Appliance):
    def __init__(self):
        super().__init__()

    def start(self):
        print("AC is on")
        self.enabled = True

    def stop(self):
        print("AC is off")
        self.enabled = False

class Refrigerator(Appliance):
    def __init__(self):
        self.enabled = False
        self.empty = False

    def full_fridge(self):
        if self.empty == True:
            print("You filled fridge")
            self.empty = False
        else:
            print("Fridge already filled")

    def empty_fridge(self):
        if self.empty == True:
            print("Refrigerator already empty, buy something!")
        else:
            self.empty = True
            print("Your fridge now is empty")

    def start(self):
        if self.empty == False:
            print("Refrigerator is on")
            self.enabled = True
        else:
            print("Fridge is empty, dont waste electricity!")

    def stop(self):
        if self.empty == True:
            print("Refrigerator is off")
            self.enabled = False
        else:
            print("Food in fridge, i will not turn off!")


class Fan(Appliance):
    def __init__(self):
        self.enabled = False
        self.speed = 0

    def start(self):
        if self.speed == 0:
            print("Fan now is on")
            self.speed += 1
            self.enabled = True
        elif self.speed == 1:
            print("Speed increased")
            self.speed += 1
        elif self.speed == 2:
            print("Max speed")
            self.speed += 1  
        else:
            print("Fan is already working at max speed")

    def stop(self):
        if self.speed <= 0:
            print("Fan already off")
        elif self.speed == 2 or self.speed == 3:
            print("Speed decreased")
            self.speed -= 1
        elif self.speed == 1:
            print("Fan disabled")
            self.speed -= 1
            self.enabled = False

class TV(Appliance):
    def __init__(self):
        self.enabled = False
        self.channel = 1

    def switch_channel(self,num):
        if num >= 1 and num <= 35:
            self.channel = num
        else:
            print(f'No channel with number {num}')

    def switch_channel_toward(self):
        if self.channel == 35:
            self.channel = 1
        else:
            self.channel += 1

    def switch_channel_back(self):
        if self.channel == 1:
            self.channel == 35
        else:
            self.channel -= 1

    def start(self):
        print("TV is on")
        self.enabled = True

    def stop(self):
        print("TV is off")
        self.enabled = False

class Gate(Appliance):
    def __init__(self):
        self.enabled = False

    def start(self):
        print("Gate is opened")
        self.enabled = True

    def stop(self):
        print("Gate is closed")
        self.enabled = False

class Switch(metaclass=ABCMeta):
    def __init__(self, appliance: Appliance):
        self.appliance = appliance

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class AutomaticRemoteController(Switch):
    def __init__(self,appliance : Appliance):
        super().__init__(appliance)

    def turn_on(self):
        if self.appliance.enabled:
            print("Appliance already enabled")
        else:
            self.appliance.start()

    def turn_off(self):
        if self.appliance.enabled:
            self.appliance.stop()
        else:
            print("Appliance already disabled")

class ManualRemoteController(Switch):
    def __init__(self,appliance : Appliance):
        super().__init__(appliance)

    def turn_on(self):
        if self.appliance.enabled:
            print("Appliance already enabled")
        else:
            self.appliance.start()

    def turn_off(self):
        if self.appliance.enabled:
            self.appliance.stop()
        else:
            print("Appliance already disabled")


os.system('CLS')
ac = AC()
ARC_AC = AutomaticRemoteController(ac)
ARC_AC.turn_off()
ARC_AC.turn_on()
ARC_AC.turn_off()
print('\n\n')

fridge = Refrigerator()
MRC_F = ManualRemoteController(fridge)
MRC_F.turn_on()
MRC_F.turn_off()
fridge.empty_fridge()
MRC_F.turn_off()
print('\n\n')

fan = Fan()
ARC_F = AutomaticRemoteController(fan)
ARC_F.turn_on()
fan.start()
fan.start()
fan.stop()
fan.stop()
ARC_F.turn_off()
print('\n\n')

tv = TV()
MRC_TV = ManualRemoteController(tv)
MRC_TV.turn_on()
MRC_TV.turn_on()
MRC_TV.turn_off()
MRC_TV.turn_off()
print('\n\n')

gate = Gate()
MRC_G = ManualRemoteController(gate)
MRC_G.turn_on()
MRC_G.turn_on()
MRC_G.turn_off()
MRC_G.turn_off()