tasks =[]
taskstatus=[]
decision=input("Would you like to, Add tasks (add) , view tasks( view) , mark task as complete(mark), or delete tasks(delete) ")
x=2
while x==2:
    if decision=='add':
        task=input('what is the task')
        taskstatus.append('ongoing')
        tasks.append(task)
        decision=input("Would you like to, Add tasks (add) , view tasks( view) , mark task as complete(mark), or delete tasks(delete) ")
    
    
    elif decision== 'view':
        for i in range(1+ len(tasks)):
            
            
            
            
            print("Task #", i+1,": ",tasks[i], taskstatus[i])
            decision=input("Would you like to, Add tasks (add) , view tasks( view) , mark task as complete(mark), or delete tasks(delete) ")
            
    elif decision == 'mark':
        for i in range(len(tasks)):
            print("Task #", i+1,":",tasks[i])
        completed= input("which tasks have you completed ")
        taskstatus[i]='COMPLETE'
        
       
        
        
            
    
        
    
    
    
    
    
    