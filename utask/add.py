import json
def add(name):
    task = {"tarea": []}
    data_holder = task["tarea"]
    counter = 0
    while counter < 2:
        data_holder.append({"nombre": name})
        data_holder.append({"descripcion": name})
        counter += 1
    with open("tasks.json",'a') as tasksLibrary:
        print(task)        
        json.dump(task, tasksLibrary)
        # tasksLibrary.write(name + '\n')
    print("Se ha añadido {} a la lista de tareas".format(name))