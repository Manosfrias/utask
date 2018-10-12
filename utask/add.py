import json
def add(name):
    task = {'tarea': {'nombre': name,'descripcion': name}}

    with open("tasks.json",'a') as tasksLibrary:    
        json.dump(task, tasksLibrary)
        # tasksLibrary.write(name + '\n')
    with open("tasks.json",'r') as tasksLibrary: 
        json.load(tasksLibrary)
    # print("Se ha añadido {} a la lista de tareas".format(name))