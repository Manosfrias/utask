import argparse
parser = argparse.ArgumentParser(description="Create task manager by terminal")

parser.add_argument("name", help="The task name")

parser.add_argument("-a", "--add", action="store_true", help="Add a new task")
# parser.add_argument("-l", "--list", action="store_true", help="Add a new task")

args = parser.parse_args()

if args.add:
    tasksLibrary = open("task",'w')
    tasksLibrary.write(args.name)
    tasksLibrary.close()
	print("Se ha añadido {} a la lista de tareas".format(args.name))


# class utask
#   def __init__ (self, name)
#     self._name = name

#   def add(self, name) 
#     self.name = name

#   def list
#     for utask in utaskList
#       print(utask)