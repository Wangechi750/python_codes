#creating class and object
class temperature:
    def __init__(self,temp):
        self.temp=temp
    def convertFahrenheit(self):
       #formula
       x=self.temp*9/5+32
       return x
       
    def convertCelsius(self):
       #formula
       y=self.temp-32*5/9
       return y
       
temp=temperature(50)
print(temp.convertFahrenheit())
print(temp.convertCelsius())