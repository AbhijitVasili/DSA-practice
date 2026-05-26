class cookie:
    def __init__(self,color):
        self.color = color
    
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color

cookie_one = cookie('green')
cookie_two = cookie('blue')

print('Cookie one is : ', cookie_one.get_color())
print('Cookie two is : ', cookie_two.get_color())

cookie_one.set_color('red') 

print('Cookie one is : ', cookie_one.get_color())   
print('Cookie two is : ', cookie_two.get_color())