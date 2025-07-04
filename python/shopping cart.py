#create a shopping cart programmme that will continuosly ask the user for food product and the price of the product
#have an exut clause if the user wishes to stop adding more things to their cart
#at the end show the food items and the total cost of the user

foods =[]
prices=[]
total=0

while True:
    food = input("enter a food to buy or press q to quit")
    if food.lower() == 'q':
        break
    else:
        price=float(input(f"enter the price of the {food}:R"))
        foods.append(food)
        prices.append(prices)
        
        print("------YOUR CART-------")
        
        for food in foods:
            print(food,end="")
            
            for price in prices:
                total += price
                
                print("\n")
                print(f"Your total is: R{total}")