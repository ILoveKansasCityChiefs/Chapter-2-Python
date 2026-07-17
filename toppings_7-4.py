topping = input("Enter a topping that you want on your pizza: ")


while True:
  
    if topping == 'quit':
        break
    else:
        print(f"Adding {topping} onto your pizza")
        topping = input("\nEnter another topping that you want on your pizza: ")
