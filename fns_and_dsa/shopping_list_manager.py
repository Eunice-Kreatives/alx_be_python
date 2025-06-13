# shopping_list_manager.py

def display_menu():

    print("\n--- Shopping List Manager ---")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")
    print("-----------------------------")
        
    
    
def shopping_list_menu():
  
    shopping_list = []
    while True: 
        display_menu()

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            item_to_add = input("Enter the item to add: ").strip() 
            if item_to_add:
                shopping_list.append(item_to_add)
                print(f"'{item_to_add}' has been added to your list.")
            else:
                print("Item name cannot be empty. Please try again.")

        elif choice == '2':
            item_to_remove = input("Enter the item to remove: ").strip()
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                print(f"'{item_to_remove}' has been removed from your list.")
            else:
                print(f"'{item_to_remove}' was not found in your list.")

        elif choice == '3':
            print ("\n--- Your Shopping List ---")
            if not shopping_list:
                print("Your shopping list is empty.")
            else:
                for index, item in enumerate(shopping_list, 1): # enumerate for numbered list
                    print(f"{index}. {item}")
            print("--------------------------")

        elif choice == '4':
            print("Exiting Shopping List Manager. Goodbye!")
            break 

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    shopping_list_menu()





