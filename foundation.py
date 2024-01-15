print("Welcome to Domestipets Charity Donation page")

donatable_items = {"dry kibble cat": 11.95,
               "dry kibble dog": 6.95,
               "wet mixed grill can": 6.95,
               "shine shampoo": 8.95,
               "doggy chews": 4.00,
               "dreamy bites": 3.00,
               "wet mixed grill can": 5.95,
               "odour spray": 11.00,
               "litter fresh": 5.00,
               "catnip": 4.95,
               "snack seeds": 4.50,
               "hay mix": 8.55,
               "water bottle": 4.95,
               "runner wheel": 10.00}

shopping_cart = []
total = 0

print("----------Donatable items list----------")
for key, value in donatable_items.items():
    print(f"{key}: £{value:.2f}")
print("------------------------------------") 

while True:
    cart_items = input("Please select item to add to cart (e to exit): ").lower()
    if cart_items == "e":
        break
    elif donatable_items.get(cart_items) is not None:
        shopping_cart.append(cart_items)

print("----------Your Cart----------")
for cart_items in shopping_cart:
    total += donatable_items.get(cart_items)
print(shopping_cart)

print()
print(f"Your total is: £{total:.2f}")

added_items = []
removed_items = []

while True:
    optional_input = input("Would you like to add or remove items from your cart (e to exit): ").lower()
    if optional_input == "e":
        break
        
    elif optional_input == "add":
        add_input = input("Please select item to add to cart (q to quit): ").lower()
        if add_input == "q":
            break

        else:
            shopping_cart.append(added_items)


    elif optional_input == "remove":
         remove_input = input("Please select items to remove (q to quit): ")
         if remove_input == "q":
            break
         
         else:
          for i, item in enumerate(shopping_cart, 1):
            print(i, item)
            remove_input = (item)-1
            remove_input = shopping_cart[item]
            shopping_cart.pop(item)
            print(f'{item} removed!')  

            print("----------Your Cart----------")
            for cart_items in shopping_cart:
                total += donatable_items.get(cart_items)
            print(shopping_cart)

            print()
            print(f"Your total is: £{total:.2f}")

print("Thank you for your PETronage. Please come back soon!")  



# print("----------Your Cart----------")
# for cart_items in shopping_cart:
#     total += donatable_items.get(cart_items)
# print(shopping_cart)

# print()
# print(f"Your total is: £{total:.2f}")           


    

  
        





#type_input = int(input(("Please select pet type from options below:\n1: Canine\n2: Feline"\
                  # "\n3: Rodent\n0: Exit\n")))
# Include some defensive coding for if none of the above are entered


#else:
    #print("Thank you for viewing our page. We hope you come back soon!")    

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
