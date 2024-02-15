import colorama             #import colorama to be used to change colour of some text outputs
from colorama import init, Fore

colorama.init(autoreset=True)

from datetime import datetime       #import datetime class

def print_menu():           #function to print menu
    print("""
    _______________________________________________________
    │  Drinks                  │  Food                    │  
    │ - Tea           : £1.00  │ - Croissant     : £1.50  │
    │ - Americano     : £1.70  │ - Muffin        : £2.10  │
    │ - Latte         : £1.90  │ - Toast         : £1.00  │  
    │ - Cappuccino    : £1.90  │ - Panini        : £2.90  │
    │ - Mocha         : £2.00  │ - Buttered Roll : £0.70  │
    │ - Hot Chocolate : £2.20  │ - Stroopwafel   : £0.50  │
    │ - Bottled Water : £1.00  │ - Potato Cake   : £1.00  │
                   """)

menu = {                    #dictionary containing food menu items and associated prices
    "Tea": 1.00,
    "Americano": 1.70,
    "Latte": 1.90,
    "Cappuccino": 1.90,
    "Mocha": 2.00,
    "Hot chocolate": 2.20,
    "Bottled Water" : 1.00,
    "Croissant": 1.50,
    "Muffin": 2.10,
    "Toast": 1.00,
    "Panini": 2.90,
    "Buttered Roll": 0.70,
    "Stroopwafel": 0.50,
    "Potato Cake": 1.00
}
                             
extras = {                  #Dictionary containing extra menu items and associated prices
    "Skimmed milk": 0.15,
    "2% milk": 0.20,
    "Full fat milk": 0.30,
    "Almond milk": 0.35,
    "Oat milk": 0.35,
    "Soya milk": 0.35,
    "Lactose-free milk": 0.40,
    "Custard": 1.00,
    "Ham 1 slice": 0.50,
    "Shredded chicken": 1.50,
    "Butter": 0.30,
    "Cheese": 1.00,
    "Salami 1 slice": 0.50,
    "Salad": 0.70
}

final_order = []            #creates an empty list which will be used to store orders

def start():
    while True:     #program will loop until user inputs either y or n
        customer_name = input("Hello and welcome to Brian's Bistro, please can I take your name: ")
        if not customer_name:  #check if the user entered a name
            print(Fore.RED + "Please enter your name.")
            continue
        current_datetime = datetime.now().strftime("%d-%m-%Y-- %H:%M:%S")
        print("Unfortunately our card machine is broken today and we are only accepting cash. Here is the menu: ")
        print_menu()     
        welcome_message = input("Would you like to place an order? y/n: ") # A small amount of ascii for our menu
        if welcome_message == "y": #start with an 'if' statement to determine if the customer would like to create an order or not
            print("Good choice")
        elif welcome_message == "n":
            start()
        else:
            print("Invalid input, enter 'y' or 'n' ") #if user is to type anything other than 'y' or 'n' they will recieve the invalid input error
            continue 
        break
        
    total_cost = 0  #start the total cost from 0 for every new order.
    while True: #program will continue to loop until command is given which will break the loop
        order_input = input("What would you like to order?: ").capitalize() #convert input to always have first letter as capital for case sensitivity
        if order_input.capitalize() not in menu:    #checks to see if selected item is in the menu, error message printed it not
            print(Fore.RED + "Sorry, that item is not available.")
            continue
        order_count = int(input("How many would you like: "))
        total_cost += menu[order_input] * order_count #update the total cost of the order 
        print(Fore.GREEN + f"{order_count} {order_input}(s) have been added to your order. Current total: £{total_cost:.2f}")
        final_order.append((order_input, order_count))

        while True: # Loop until valid input is provided
            extra_order = input("Would you like to add any extras? (y/n): ")    
            if extra_order.lower() == "y":
                print("Available extras:")
                for extra in extras:
                    print(f"- {extra}: £{extras[extra]:.2f}")  #if extras are selected then print them and their prices
                while True:
                    chosen_extra = input("Enter the name of the extra you'd like to add, or 'finished' to finish adding extras: ").capitalize()
                    if chosen_extra == "Finished":
                        break
                    elif chosen_extra in extras:
                        total_cost += extras[chosen_extra]
                        print(Fore.GREEN + f"{chosen_extra} has been added to your order. Current total: £{total_cost:.2f}")
                    else:
                        print(Fore.RED + "Sorry, that extra is not available.")
                break
            elif extra_order.lower() == "n":
                break
            else:
                print(Fore.RED + "Invalid input. Please enter 'y' or 'n'.")

        next_order = input("""Would you like to add another item to you order? (y/n) 
                           (Type 'restart' to cancel all items and start again)
                           (Type 'menu' to see the menu again): """)
        if next_order.lower() == "n":   #option to add more items to the order
            break
        elif next_order.lower() == "menu":
            print_menu()
        elif next_order.lower() == "restart": #option of cancelling current order and returning to start 
            total_cost = 0
            final_order.clear()
            start()

    print(Fore.BLUE + f"Here is your order {customer_name} The total is £{total_cost:.2f}. Thank you for visiting Brian's Bistro, have a good day")
    print(Fore.BLUE + f"Date and Time: {current_datetime}")
    print("Please leave us a review on our tripadvisor page https://www.tripadvisor.co.uk/Restaurant_Review-g186233-d27188539-Reviews-Brian_s_Bistro-Chester_Cheshire_England.html")    

    with open("receipts.txt", "a", encoding="utf-8") as f: #creates textfile to store orders and translate unicode character into matching binary string
        f.write("Name: " + customer_name + "\n") #"\n" used to create new line
        f.write("Items:\n")
        for item, count in final_order:
            f.write(f"- {count} {item}\n")  #print number of each items ordered to receipt
        f.write(f"Amount: £{total_cost:.2f}\n")
        f.write("Date and Time: " + current_datetime + "\n")
        f.write("------------------------------------" + "\n\n")

start() 