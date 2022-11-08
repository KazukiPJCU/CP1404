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
            load_projects()
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


def load_projects():
    """Load projects."""
    projects = []
    filename = input("Type in project file to load: ")
    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            date_string = parts[1]
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            project = Project(parts[0], date, int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
    return projects


main()
