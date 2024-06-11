# lib/main.py
from models.teams import Teams
from models.locations import Locations


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "00":
            exit_program()
        elif choice == "1":
            team_operations()
        elif choice == "2":
            location_operations()
        else:
            print("Invalid choice")

def team_operations():
    while True:
        print("\n***Team Management***")
        print("\nPlease select an option:")
        print("1. Create a new team")
        print("2. Show all teams")
        print("3. Show a single team")
        print("4. Edit a team")
        print("5. Delete a team")
        print("6. Return to main menu")
        print("00. Exit the program")

        choice = input("> ")
        if choice == "00":
            exit_program()
        elif choice == "1":
            name = input("Enter team name: ")
            Teams.create_team(name)
            print(f"{name} has been registered successfully!")
        elif choice == "2":
            print(Teams.show_all_teams())
        elif choice == "3":
            team_id = input("Enter team id: ")
            team = Teams.show_single_team(team_id)
            print(team)
        elif choice == "4":
            team_id = input("Enter team id: ")
            print(f"Selected Team: {Teams.show_single_team(team_id)}\n")
            name = input("Enter new team name: ")            
            Teams.edit_team(team_id, name)
            print(f"Team {team_id} has been updated successfully!")
        elif choice == "5":
            team_id = input("Enter team id: ")
            Teams.delete_team(team_id)
            print(f"Team {team_id} has been deleted successfully!")
        elif choice == "6":
            return menu()
        else:
            print("Invalid choice")

def location_operations():
    while True:
        print("\n***Location Management***")
        print("\nPlease select an option:")
        print("1. Create a new location")
        print("2. Show all locations")
        print("3. Return to main menu")
        print("00. Exit the program")

        choice = input("> ")
        if choice == "00":
            exit_program()
        elif choice == "1":
            name = input("Enter location name: ")
            Locations.create_location(name)
            print(f"{name} has been registered successfully!")
        elif choice == "2":
            print(Locations.show_all_locations())
        elif choice == "3":
            return menu()
        else:
            print("Invalid choice")

def menu():
    print("\n***Welcome to the League!***")
    print("\nPlease select an option:")
    print("1. Team Management")
    print("2. Location Management")
    print("00. Exit the program")

def exit_program():
    print("Goodbye!")
    exit()


if __name__ == "__main__":
    main()
