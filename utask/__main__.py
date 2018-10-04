from __init__ import parser
from add import add
from list import list

"""A partir de aquí hago cosas"""
args = parser.parse_args()
tasksLibrary = []
     
if args.add:
  add(args.name)
elif args.list:
  list()