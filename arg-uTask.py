import argparse
parser = argparse.ArgumentParser(description="Create task manager by terminal")

parser.add_argument("name", help="The task name")

parser.add_argument("-a", "--add", action="store_true", help="Add a new task")
parser.add_argument("-l", "--list", action="store_true",  help="List all the tasks")

args = parser.parse_args()

if args.add:
   with open("task.txt",'a') as tasksLibrary:
    tasksLibrary.write(args.name + '\n')
    print("Se ha añadido {} a la lista de tareas".format(args.name))
elif args.list:
    with open("task.txt",'r', encoding='utf-8') as tasksLibrary:
        for task in tasksLibrary:
            print('{}'.format(task)) 


# with open('test.txt', 'w') as a:
#         a.write('theunixdisaster\t 05')
# class utask
#   def __init__ (self, name)
#     self._name = name
#   def add(self, name) 
#     self.name = name
#   def list
#     for utask in utaskList
#       print(utask)