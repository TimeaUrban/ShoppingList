shopping_list = [ ]

def main():
	print shopping_list
	choice = raw_input("What would you like to do? 1) Add item 2) Remove item 3) Quit ")

	if choice == "1":
		add_item()
		return main()

	elif choice == "2":
		remove_item()
		return main()

	elif choice == "3":	
		print "Thank you for using my great shopping list creator! Your final shopping list is:", shopping_list

	else: 
		print "Please select 1, 2 or 3!"
		main()


def add_item():
	added_item = raw_input("What item would you like to add? ").lower()

	if check_item(added_item) == True:
		print "This item is already on your list!"

	if check_item(added_item) == False:
		shopping_list.append(added_item)
		shopping_list.sort()
		# Change sorting into a separate function
		print added_item + " added to your list!"


# def remove_item():	


def check_item(added_item):
	return added_item in shopping_list
	

if __name__ == '__main__':
	main()