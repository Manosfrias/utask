def list():    
  with open("task.txt",'r', encoding='utf-8') as tasksLibrary:
    for task in tasksLibrary:
      print('{}'.format(task)) 