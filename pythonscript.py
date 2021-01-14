global option
option = 0

contact_list = [{"first_name" : "Kyle", "last_name" : "Goertzen", "phone_number" : "2504302171"},
                {"first_name" : "Dylin", "last_name" : "Grbich-Zaytsoff", "phone_number" : "2365865188"},
				{"first_name" : "Kianna", "last_name" : "Norman", "phone_number" : "2365865240"}]

class operation:
    def __init__(self, name, message):
        self.name = name
        self.message = message
        
    def get_options(self):
        global option
        option = str(input("Enter a number between 0 and 3:>"))
        if str(option).isdigit():
            while not str(option).isdigit() and str(option).isalpha and str(option) and option >= 0 and option <= 4:
                option = str(input("Enter a number between 0 and 3:>"))
        if str(option).isalpha():
            while not str(option).isdigit() and str(option).isalpha and str(option):
                option = str(input("Enter a number between 0 and 3:>"))
        return option

    def print_options(self):
        print("What would you like to do?")
        print("Option 1 - Type the number 1 hit enter to see your contact list.")
        print("Option 2 - Type the number 2 hit enter to add to your contact list.")
        print("Option 3 - Type the number 3 hit enter to edit contact phone number by first and last name.")
        print("Option 4 - Type the number 4 hit enter to delete contact by first name.")
        print("Option 0 - Type the number 0 hit enter to quit.")
        global option
        self.get_options()
        if option == str(1):
            print(self.name + "'s" + " contact list")
            for i in range(len(contact_list)):
                if isinstance(contact_list[i], dict):
                    print(contact_list[i]["first_name"] + " " + contact_list[i]["last_name"] + " " + contact_list[i]["phone_number"])
					

        if option == str(2):
            first_name = str(input("Enter first name:>"))
            last_name = str(input("Enter last name:>"))
            for i in range(len(contact_list)):
                if first_name == contact_list[i]["first_name"] and last_name == contact_list[i]["last_name"]:
                    print("No duplicates")
                    return option
            phone_number = str(input("Enter phone number:>"))
            if phone_number == "":
                phone_number = "No number."
            contact = {"first_name" : first_name, "last_name" : last_name, "phone_number" : phone_number}
            contact_list.append(contact.copy())
		
        if option == str(3):
            the_first_name_to_edit = str(input("The first name of contact to edit:>"))
            the_last_name_to_edit = str(input("The last name to contact to edit:>"))
            phone_number = str(input("Enter your phone number:>"))
            for i in range(len(contact_list)):
                if contact_list[i]["first_name"] == str(the_first_name_to_edit) and contact_list[i]["last_name"] == str(the_last_name_to_edit):
                    contact_list[i]["phone_number"] = phone_number
                    
        if option == str(4):
            the_first_name_to_edit = str(input("The first name of contact to delete:>"))
            for i in range(len(contact_list)):
                if contact_list[i]["first_name"] == str(the_first_name_to_edit):
                    print(contact_list[i])
                    del contact_list[i]
            
        return option
            
global username

username = str(input("What is your name?>"))

while option != str(0):
    operation1 = operation(username, "Peace!")
    option = operation1.print_options()
	
print("Goodbye " + operation1.name + " " + str(operation1.message))
