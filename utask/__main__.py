from __init__ import parser

"""A partir de aquí hago cosas"""
args = parser.parse_args()
tasksLibrary = []
     
if args.add:
   with open("task.txt",'a') as tasksLibrary:
    tasksLibrary.write(args.name + '\n')
    print("Se ha añadido {} a la lista de tareas".format(args.name))
elif args.list:
    with open("task.txt",'r', encoding='utf-8') as tasksLibrary:
        for task in tasksLibrary:
            print('{}'.format(task)) 