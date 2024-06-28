class cardHolder():
          def __init__(self , cardNum , pin , firstname , lastname , balance):
                  self.cardNum = cardNum
                  self.pin = pin
                  self.firstname =firstname
                  self.lastname = lastname
                  self.balance = balance

          ## getter method
          def get_cardNum(self):
                  return self.cardNum
          def get_pin(self):
                  return self.pin
          def get_firstname(self):
                  return self.firstname
          def get_lastname(self):
                  return self.lastname
          def get_balance(self):
                  return self.balance
          
          ##setter method
          def set_cardNum(self , newVal):
                  self.cardNum = newVal
          def set_pin(self , newVal):
                  self.cardNum = newVal
          def set_firstname(self , newVal):
                  self.cardNum = newVal
          def set_lastname(self , newVal):
                  self.cardNum = newVal
          def set_balance(self , newVal):
                  self.cardNum = newVal
          
          def print_out(self):
                  print("card #: " , self.cardNum)
                  print("Pin #: " , self.pin)
                  print("First name #: " , self.firstname)
                  print("Last name #: " , self.lastname)
                  print("Balance #: " , self.balance)
                
                  

                  