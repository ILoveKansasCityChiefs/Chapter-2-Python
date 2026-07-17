age_ticket = int(input("How old are you?: "))


while True:
    
  
    if age_ticket < 3:
        print("Ticket is free")
        age_ticket = int(input("How old are you?: "))
    elif age_ticket <= 12:
        print("Ticket cost $10")
        age_ticket = int(input("How old are you?: "))
    elif age_ticket > 12:
        print("Ticket cost $15")
        age_ticket = int(input("How old are you?: "))
        
