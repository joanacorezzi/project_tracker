import argparse
from tabulate import tabulate  # external package for pretty tables

from models import User, Project, Task
from utils.storage import load_json, save_json


def load_items(filename, cls):
    #Load a list of objects
    data = load_json(filename)
    return [cls.from_dict(d) for d in data]


def save_items(filename, objects):
    #Save a list of model objects
    data = [obj.to_dict() for obj in objects]
    save_json(filename, data)

# command functions

def cmd_add_user(args):
    #create a new user
    users = load_items("users.json", User)
    user = User(name=args.name, email=args.email)
    users.append(user)
    save_items("users.json", users)
    print(f"User created: {user}")


def cmd_add_project(args):
    #create a project for a user
    users = load_items("users.json", User)
    projects = load_items("projects.json", Project)

    # find user by name
    owner = next((u for u in users if u.name == args.user), None)
    if owner is None:
        print(f"User '{args.user}' not found. Please add the user first.")
        return

    project = Project(
        title=args.title,
        description=args.description,
        due_date=args.due_date,
        owner_id=owner.id,
    )
    projects.append(project)
    save_items("projects.json", projects)
    print(f"Project created: {project} (owner: {owner.name})")


def cmd_add_task(args):
    #create a task for a project
    projects = load_items("projects.json", Project)
    tasks = load_items("tasks.json", Task)

    # find project by title
    project = next((p for p in projects if p.title == args.project), None)
    if project is None:
        print(f"Project '{args.project}' not found. Please add the project first.")
        return

    task = Task(
        title=args.title,
        assigned_to=args.assigned_to,
        project_id=project.id,
    )
    tasks.append(task)
    save_items("tasks.json", tasks)
    print(f"Task created: {task} (project: {project.title})")


def cmd_list_projects(args):
  #show all projects
    
    users = load_items("users.json", User)
    projects = load_items("projects.json", Project)

    # filter by user name 
    if args.user:
        owner = next((u for u in users if u.name == args.user), None)
        if owner is None:
            print(f"User '{args.user}' not found.")
            return
        projects = [p for p in projects if p.owner_id == owner.id]

    if not projects:
        print("No projects found.")
        return

    table = []
    for p in projects:
        owner_name = ""
        for u in users:
            if u.id == p.owner_id:
                owner_name = u.name
                break
        table.append([p.id, p.title, owner_name, p.due_date])

    # use tabulate to print a table
    print(tabulate(table, headers=["ID", "Title", "Owner", "Due Date"], tablefmt="github"))


def cmd_complete_task(args):
   #mark a task as complete by ID
    tasks = load_items("tasks.json", Task)

    task = next((t for t in tasks if t.id == args.id), None)
    if task is None:
        print(f"Task with ID {args.id} not found.")
        return

    task.mark_complete()
    save_items("tasks.json", tasks)
    print(f"Task marked as complete: {task}")


def build_parser():
    #Create the main argparse parser 
    parser = argparse.ArgumentParser(
        description="Simple Command-Line Project Management Tool"
    )
    subparsers = parser.add_subparsers(dest="command")

    # add-user
    p_add_user = subparsers.add_parser("add-user", help="Add a new user")
    p_add_user.add_argument("--name", required=True, help="User name")
    p_add_user.add_argument("--email", required=True, help="User email")
    p_add_user.set_defaults(func=cmd_add_user)

    # add-project
    p_add_project = subparsers.add_parser("add-project", help="Add a new project")
    p_add_project.add_argument("--user", required=True, help="Owner user name")
    p_add_project.add_argument("--title", required=True, help="Project title")
    p_add_project.add_argument("--description", default="", help="Project description")
    p_add_project.add_argument(
        "--due-date", default=None, help="Due date (e.g. 2025-12-31)"
    )
    p_add_project.set_defaults(func=cmd_add_project)

    # add-task
    p_add_task = subparsers.add_parser("add-task", help="Add a new task to a project")
    p_add_task.add_argument("--project", required=True, help="Project title")
    p_add_task.add_argument("--title", required=True, help="Task title")
    p_add_task.add_argument(
        "--assigned-to", help="User name this task is assigned to"
    )
    p_add_task.set_defaults(func=cmd_add_task)

    # list-projects
    p_list_projects = subparsers.add_parser(
        "list-projects", help="List projects (optionally by user)"
    )
    p_list_projects.add_argument(
        "--user", help="Filter by user name (optional, to search projects for a user)"
    )
    p_list_projects.set_defaults(func=cmd_list_projects)

    # complete-task
    p_complete_task = subparsers.add_parser(
        "complete-task", help="Mark a task as complete"
    )
    p_complete_task.add_argument("--id", type=int, required=True, help="Task ID")
    p_complete_task.set_defaults(func=cmd_complete_task)

    return parser


def run_cli():
    #Entry 
    parser = build_parser()
    args = parser.parse_args()

    if not hasattr(args, "func"):
        
        parser.print_help()
        return

    args.func(args)