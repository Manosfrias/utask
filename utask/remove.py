def remove(name):
    with open("task.txt",'w', encoding='utf-8') as tasksLibrary:
        task = tasksLibrary.readline()
        for task in tasksLibrary:
            if task != name:
                print(task)
                tasksLibrary.write(task)
            else:
                print('{} se ha eliminado de la lista'.format(task))
                
