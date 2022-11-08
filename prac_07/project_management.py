"""Project management"""
"""Estimated:   60"""
"""Actual:      """

from project import Project
import datetime

FILENAME = "projects.txt"
MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new " \
       "project\n- (U)pdate project\n- (Q)uit "


def main():
    print(MENU)
    menu_choice = input(">>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            print("Load Projects")
        elif menu_choice == "S":
            print("Save Projects")
        elif menu_choice == "D":
            print("Display Projects")
        elif menu_choice == "F":
            print("Filter projects by date")
        elif menu_choice == "A":
            print("Add new project")
        elif menu_choice == "U":
            print("Update project")
        else:
            print("Incorrect menu choice")
        menu_choice = input("Menu Choice: ").upper()
    print("Thanks for coming")


main()
