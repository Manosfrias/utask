import json
def add(name):
     with open("task.txt",'a') as tasksLibrary:
        tasksLibrary.write(name + '\n')
        print("Se ha añadido {} a la lista de tareas".format(name))
    # print("Se ha añadido {} a la lista de tareas".format(name))