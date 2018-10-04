import argparse
parser = argparse.ArgumentParser(description="Create task manager by terminal")

parser.add_argument("name", help="The task name")
# parser.add_argument("list", action="store_true",  help="List all the tasks")

parser.add_argument("-a", "--add", action="store_true", help="Add a new task")
parser.add_argument("-r", "--remove", action="store_true", help="Remove a new task")