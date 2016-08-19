master_list = {"Target": ["socks", "soap", "detergent", "sponges"], "Safeway": ["butter", "cake", "cookies", "bread"]}

test_list = ["apples", "wine", "cheese"]


def main_menu():
	print "Select one"
	print "0 - Main Menu"
	print "1 - Show all lists."
	print "2 - Show a specific list."
	print "3 - Add a new shopping list for a specific store."
	print "4 - Add an item to shopping list."
	print "5 - Remove an item from a shopping list."
	print "6 - Remove a list by name."
	print "7 - Exit"
	choice = int(raw_input())
	return choice


def display_lists():
	print master_list


def specific_list():
	specific = raw_input("Which store's list would you like to see?")
	if specific in master_list:
		print master_list[specific]
	else:
		print "You don't have a list for this store. Please create a new list for this store or check spelling."


def new_list():
	store = raw_input("what store is this list for?")
	if store in master_list:
		print "You already have a list for", store, "."
	else:
		master_list[store] = []


def add_item():
	# item = item.lower()
	store = raw_input("which store list would you like to add the item to?")
	if store in master_list:
		item = raw_input("What would you like to add?")
		master_list[store].append(item)
		print master_list
	else: 
		print "You don't have a list for this store yet."
# Slight issue: it's not printing the master lists after adding the item. It prints the values of that store's list...


def delete_list():
	store = raw_input("what store's list do you want to remove?")
	if store in master_list:
		del master_list[store]	
		print "Your list for", store, "has been deleted."
	else:
		print "You don't have a list for", store, "yet."

# def alphabetize():
# 	master_list[].sort()
# 	return master_list
# Not working! How to make sure every time the lists are printed, they are alphabetized?

def remove_item():
	item_to_remove = raw_input("What item would you like to remove from your shopping lists?")
	if item_to_remove in master_list:
		master_list.pop(item_to_remove)
		print "Here are your updated lists:", master_list
	else:
		print "You don't have", item_to_remove, "on any of your lists."
# Not working: even if I have the item in the dictionary, it runs the "else" scenario. Same logic works for delete_list, so not sure why... maybe because now I'm looking for a value and not a key

def write_to_file(param1, master_list):
	with open (param1, mode = "w") as my_file:
		my_file.write(str(master_list))

		
		# my_file.splbit()





def main():
	while(True):
		choice = main_menu()

		if choice == 1:
			# alphabetize()
			display_lists()

		elif choice == 2:
			specific_list()

		elif choice == 3:
			new_list()

		elif choice == 4:
			add_item()

		elif choice == 5:
			remove_item()

		elif choice == 6:
			delete_list()

		elif choice == 7:
			break

		else:
			return
	# user_input = raw_inpt()
	write_to_file("timea_shopping_list.txt", master_list)

if __name__ == '__main__':
	main()