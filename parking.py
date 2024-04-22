class Garage:
  
    def __init__(self, tickets, parkingSpaces, currentTicket):
      self.tickets = tickets
      self.parkingSpaces = parkingSpaces
      self.currentTicket = currentTicket 
    
      while parkingSpaces != 0:
        def takeTicket(self, currentTicket):
          currentTicket= dict(
          payment = 'Undefined'
          )
          parkingTickets =  [1,2,3,4]
          parkingSpaces = [1, 2, 3, 4]

          spaceNumber = input(int('What Space will you park in: 1-4?'))
          parkingTickets.pop(spaceNumber)
          parkingSpaces.pop(spaceNumber)

          def payForParking(self):
            
            payment = input(int("Please submit your payment! "))
            if payment > 0:
              currentTicket[payment] = ['True']
              print('Thanks for your payment, you have 15 min to leave')
              break
            
            
            else: 
              currentTicket[payment] = ['False']
              print("Please submit a valid payment method")

            def leaveGarage():
              if currentTicket[payment] == ['True']:
                print("Thank you, have a nice day")
                parkingTickets.append(spaceNumber)
                parkingSpaces.append(spaceNumber)
                break
              elif currentTicket[payment] == ['False']:
                print(input(int("Please submit your payment: ")))
              else:
                print("Thank You, have a nice day")
                break




        

    





    

