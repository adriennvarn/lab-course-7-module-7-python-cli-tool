# cli_tool.py

import argparse
from .models import Task, User

# Global dictionary to store users and their tasks
users = {}

# add a task for a user
def add_task(args):
    user = users.setdefault(args.user, User(args.user))
    user.add_task(Task(args.title))

# Implement function to mark a task as complete
def complete_task(args):
    user = users.get(args.user)
    if not user:
        print(f"User {args.user} not found.")
    
    task = next((task for task in user.tasks if task.title == args.title), None)
    if not task:
        print(f"Task {args.title} not found for user {user.name}.")
    
    task.complete()

# CLI entry point
def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers()

    # Subparser for adding tasks
    add_parser = subparsers.add_parser("add-task", help="Add a task for a user")
    add_parser.add_argument("user")
    add_parser.add_argument("title")
    add_parser.set_defaults(func=add_task)

    # Subparser for completing tasks
    complete_parser = subparsers.add_parser("complete-task", help="Complete a user's task")
    complete_parser.add_argument("user")
    complete_parser.add_argument("title")
    complete_parser.set_defaults(func=complete_task)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
