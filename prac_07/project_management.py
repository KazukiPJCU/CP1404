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
            projects = load_projects()
            print(MENU)
        elif menu_choice == "S":
            print("Save Projects")
            save_data(projects)
            print(MENU)
        elif menu_choice == "D":
            print("Display Projects")
            display_projects(projects)
            print(MENU)
        elif menu_choice == "F":
            print("Filter projects by date")
        elif menu_choice == "A":
            print("Add new project")
            add_new_project(projects)
            print(MENU)
        elif menu_choice == "U":
            print("Update project")
            update_project(projects)
            print(MENU)
        else:
            print("Incorrect menu choice")
        menu_choice = input("Menu Choice: ").upper()
    print("Quit program")


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


def save_data(projects, title):
    out_file = input("Save file name: ")
    with open(out_file, "w") as out_file:
        print("\t".join(title), file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date}"
                  f"\t{project.priority}\t{project.estimate}\t{project.completion}",
                  file=out_file, end="\n")


def display_projects(projects):
    completed_projects = [project for project in projects if project.is_complete()]
    incomplete_projects = [project for project in projects if not project.is_complete()]
    print("Incomplete Projects: ")
    for project in incomplete_projects:
        print(f"\t{project}")
    print("Completed Projects: ")
    for project in completed_projects:
        print(f"\t{project}")


# def filter_projects(projects):

def add_new_project(projects):
    print("Add a new project")
    name = input("Name: ").title()
    start_date = get_valid_date()
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: $ ")
    percent_complete = input("Percent complete: ")
    new_project = Project(name, start_date, priority, cost_estimate, percent_complete)
    projects.append(new_project)


def get_valid_date():
    is_valid_input = False
    while not is_valid_input:
        date_string = input("Date (dd/mm/yyyy): ")
        try:
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            is_valid_input = True
        except ValueError:
            print("Incorrect date format, type as indicated")
    return date


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i + 1} {project}")
    project_choice = int(input("Project choice: ")) - 1
    print(f"{projects[project_choice]}")
    new_percentage = input("New percentage: ")
    projects[project_choice].completion_percentage = new_percentage
    new_priority = input("New priority: ")
    projects[project_choice].priority = new_priority
    return projects


main()
