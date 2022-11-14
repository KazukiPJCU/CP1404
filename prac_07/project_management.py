"""Project management
Estimated:   60
Actual:     120 """

from operator import attrgetter
from project import Project
import datetime

FILENAME = "projects.txt"
MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new " \
       "project\n- (U)pdate project\n- (Q)uit "


def main():
    categories = load_categories(FILENAME)
    print(MENU)
    menu_choice = input(">>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            print("Load Projects")
            projects = load_projects()
            print(MENU)
        elif menu_choice == "S":
            print("Save Projects")
            save_data(projects, categories)
            print(MENU)
        elif menu_choice == "D":
            print("Display Projects")
            display_projects(projects)
            print(MENU)
        elif menu_choice == "F":
            print("Filter projects by date")
            filter_projects(projects)
            print(MENU)
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
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
        return projects


def save_data(projects, categories):
    """Save projects to file typed in"""
    out_file = input("Save file name: ")
    with open(out_file, "w") as out_file:
        print("\t".join(categories), file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date}"
                  f"\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}",
                  file=out_file, end="\n")


def load_categories(filename):
    """Gets the categories for projects txt file"""
    with open(filename, "r") as in_file:
        category = in_file.readline().strip().split("\t")
    return category


def display_projects(projects):
    """Displays projects"""
    completed_projects = [project for project in projects if project.is_complete()]
    incomplete_projects = [project for project in projects if not project.is_complete()]
    print("Incomplete Projects: ")
    for project in incomplete_projects:
        print(f"{project}")
    print("Completed Projects: ")
    for project in completed_projects:
        print(f"{project}")


def filter_projects(projects):
    """Filter projects"""
    user_date = get_valid_date()
    for project in projects:
        project.start_date = convert_date_filter(project.start_date)
    sorted_projects = [project for project in projects if project.start_date >= user_date]
    for project in sorted(sorted_projects, key=attrgetter("start_date")):
        print(project)
    for project in projects:
        project.start_date = convert_date_string_format(project)


def convert_date_filter(date):
    """Converts date to usable form for filtering"""
    return datetime.datetime.strptime(date, "%d/%m/%Y").date()


def convert_date_string_format(project):
    """Converts date back to string formatting"""
    return f"{project.start_date.day}/{project.start_date.month}/{project.start_date.year}"


def add_new_project(projects):
    """Adds a new project"""
    print("Add a new project")
    name = input("Name: ").title()
    start_date = get_valid_date()
    priority = get_valid_priority()
    cost_estimate = get_valid_cost_estimate()
    percent_complete = get_valid_percent()
    new_project = Project(name, start_date, priority, cost_estimate, percent_complete)
    projects.append(new_project)


def get_valid_priority():
    while True:
        try:
            priority = int(input("Enter priority: "))
            while priority < 0 or priority > 10:
                print("Priority must be between 1 - 10")
                priority = int(input("Enter priority: "))
        except ValueError:
            print('Error: Please enter number only')
            continue
        return priority


def get_valid_cost_estimate():
    while True:
        try:
            cost = int(input("Cost estimate: $ "))
        except ValueError:
            print('Error: Please enter number only')
            continue
        return cost


def get_valid_percent():
    while True:
        try:
            percent = int(input("Enter Percentage Complete: "))
            while percent < 0 or percent > 100:
                print("Percent completed must be between 0% - 100%")
                percent = int(input("Enter Percentage Complete: "))
        except ValueError:
            print('Error: Please enter number only')
            continue
        return percent


def get_valid_date():
    """Checks date is correct"""
    is_valid = False
    while not is_valid:
        date_string = input("Date (dd/mm/yyyy): ")
        try:
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            is_valid = True
        except ValueError:
            print("Incorrect date format, type as indicated")
    return date


def update_project(projects):
    """Lets user update project"""
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
