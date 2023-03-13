class Item:
     pay_rate=.8 #the pay rate after 20%
     all = []
     def __init__(self,name:str,price:float,quantity=0):
          #Run validaton to the received argument
          assert price >= 0,f"price {price} is not greater than zero"
          assert quantity >= 0, f" quantiy {quantity} should not be smaller than equal ot zero"

          self.name = name
          self.price= price
          self.quantity= quantity
          #action to execute
          Item.all.append(self)



     def calculate_total_price(self):
          return self.price*self.quantity
     def apply_discount(self):
          self.price = self.price * self.pay_rate
     def __repr__(self):
          return f"Item('{self.name}','{self.price}','{self.quantity}')"


item1 = Item("phone",100 ,1)
item2 = Item("Laptop", 1000,3)
item3 = Item("Cable",10,5)
item4 = Item("Mouse",50 ,5)
item5 = Item("Keyboard",75 ,5)



print(Item.all)
 