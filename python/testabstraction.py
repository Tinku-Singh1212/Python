from abc import ABC ,abstractmethod
class TV(ABC):
    @abstractmethod
    def changecolor():
        pass
    @abstractmethod
    def changevolume():
        pass
    @abstractmethod
    def changechannel():
        pass
class samsung(TV):
        def changechannel(self):
            print("channel is change of sumsang")
        def changecolor(self):
            print("color is changed of samsung")
        def changevolume(self):
            print("volume is changed of samsung")
        pass    
class mi(TV):
    def changechannel(self):
        print("chanel is changed of mi tv")
    def changecolor(self):
        print("color is changed of mi tv")
    def changevolume(self):
        print("volue is changed of mi tv")    
    pass 
obj=samsung()   
obj.changechannel()
obj.changecolor()
obj.changevolume()
obj=mi()
obj.changechannel()
obj.changecolor()
obj.changevolume()