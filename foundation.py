print("Welcome to Domestipets Charity Donation page")

canine_list = {"Dry kibble 1kg": 11.95,
               "Dry kibble 500g": 6.95,
               "Wet mixed grill can": 6.95,
               "Shine shampoo": 8.95,
               "Doggy chews": 4.00}

feline_list = {"Dreamy bites": 3.00,
               "Wet mixed grill can": 5.95,
               "Odour spray": 11.00,
               "Litter fresh": 5.00}

rodent_list = {"Snack seeds": 4.50,
               "Hay mix": 8.55,
               "Water bottle": 4.95,
               "Runner wheel": 10.00}

shopping_cart = []
total = 0

#While True:
type_input = int(input(("Please select pet type from options below:\n1: Canine\n2: Feline"\
                   "\n3: Rodent\n0: Exit\n")))
# Include some defensive coding for if none of the above are entered

if type_input == 1:
    print("-------------Canine menu---------------")
    for key, value in canine_list.items():
        print(f"{key}: £{value:.2f}")
    print("----------------------------------------")    

# Insert options to add to cart individual items from canine_menu
    
elif type_input == 2:
    print("-------------Feline menu---------------")
    for key, value in feline_list.items():
        print(f"{key}: £{value:.2f}")
    print("----------------------------------------")   

# Insert options to add to cart individual items from feline_menu    
    
elif type_input == 3:
    print("-------------Rodent menu---------------")
    for key, value in rodent_list.items():
        print(f"{key}: £{value:.2f}")
    print("----------------------------------------") 

# Insert options to add to cart individual items from feline_menu  

else:
    print("Thank you for viewing our page. We hope you come back soon!")    

# while True:
#     # Ask user to select an option form the menu
#     menu = input("Please select an option below:\n1: Add item\n2: View List"\
#                  "\n3: Delete item\n4: Sort List\n0: Exit\n")

#     if menu == "1":
#         # Ask user to enter an item and add the item to shopping list
#         new_item = input("Please enter the name of the item you would like to add:")
#         shopping_list.append(new_item)

#     elif menu == "2":
#         # View all items in shopping list
#         for i, item in enumerate(shopping_list, 1):
#             print(i, item)

#     elif menu == "3":
#         # Ask user to choose an index of an item to remove and remove item
#         for i, item in enumerate(shopping_list, 1):
#             print(i, item)
#         index = input("Please enter the index of the item you would like to remove:\n")
#         index = int(index)-1
#         item = shopping_list[index]
#         shopping_list.pop(index)
#         print(f'{item} removed!')

#     elif menu == "4":
#         # Sort shopping list
#         shopping_list.sort()
#         print("List sorted!")

#     elif menu == "0":
#         # Exit program
#         print("Goodbye!")
#         break
