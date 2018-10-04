def remove(name):
    with open("task.txt",'w', encoding='utf-8') as tasksLibrary:
        if name in tasksLibrary:
            try:
                tasksLibrary.pop(tasksLibrary.index(name))
                print("Se ha eliminado {} de la lista de tareas".format(name))
            except ValueError:
                pass
        else:
            print("{} no existe en la lista de tareas".format(name))
                
