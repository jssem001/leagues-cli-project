# lib/main.py

from helpers import (exit_program, helper_1)
from models.teams import Teams


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            team_operations()
        else:
            print("Invalid choice")

def team_operations():

    while True:
        print("Please select an option:")
        print("0. Exit the program")
        print("1. Create a new team")
        print("2. Show all teams")
        print("3. Show a single team")
        print("4. Edit a team")
        print("5. Delete a team")

        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            name = input("Enter team name: ")
            Teams.create_team(name)
            print(f"{name} has been registered successfully!")

        elif choice == "2":
            print(Teams.show_all_teams())
        elif choice == "3":
            Teams.show_single_team()
        elif choice == "4":
            Teams.edit_team()


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Team Management")


if __name__ == "__main__":
    main()
