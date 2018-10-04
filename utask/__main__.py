from __init__ import parser
from add import add

"""A partir de aquí hago cosas"""
args = parser.parse_args()
tasksLibrary = []
     
if args.add:
  add(args.name)
elif args.list:
    with open("task.txt",'r', encoding='utf-8') as tasksLibrary:
        for task in tasksLibrary:
            print('{}'.format(task)) 