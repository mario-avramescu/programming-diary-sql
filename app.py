from data.database import create_table, add_entry, get_entries

menu = """\nPlease select one of the following options:
1) Add new entry for today
2) View entries
3) Exit

Your selection: """

welcome = "Welcome to the programming diary \n"

def prompt_new_entry():
    entry_content = input("What have you learned today? \n")
    entry_date = input("What is the date?: \n")
        
    add_entry(entry_content, entry_date)

def view_entries():
    entries = get_entries()

    for entry in entries:
        print(f"{entry['content']}: {entry['date']}")    

print(welcome)
create_table()

while (user_input := input(menu)) != "3":
    if user_input == "1":
        prompt_new_entry()
    elif user_input == "2":
        view_entries()
    else:
        print("Invalid option. Please try again.\n")

