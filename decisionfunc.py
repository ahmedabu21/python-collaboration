tasks =[]
taskstatus=[]

x=2

def addfunc():
    task=input('what is the task')
    taskstatus.append('ongoing')
    tasks.append(task)
    
    
def viewfunc():
    if len(tasks)==0:
        print("No Ongoing Tasks!!!")
    else:
        for i in range(0, len(tasks)):
            print("Task #", i+1,": ",tasks[i], taskstatus[i])
    
def completetask():
    
    for i in range(0, len(tasks)):
        print("Task #", i+1,":",tasks[i])
            
            
    completed=int( input("which tasks have you completed "))
    taskstatus[completed-1]='COMPLETE'
    
def deletetask():
    for i in range(0, len(tasks)):
        print("Task #", i+1,": ",tasks[i], taskstatus[i])
    deleted=int(input("which task would you like to delete"))
    tasks.pop(deleted-1)
    taskstatus.pop(deleted-1)
    
    

def decisionfun():
    decision=input("Would you like to, Add tasks (add) , view tasks( view) , mark task as complete(mark), or delete tasks(delete) ")

            

    if (decision!='add') and (decision!='view') and (decision!='mark') and (decision!='delete'):
        decision= input("Please try inputting again")
    else:
        decision=str(decision)
                
        return decision
            
    
def main():

    
    
    
    while x==2:
        decision=decisionfun()
        
        if decision =='add':
            addfunc()
            
            

            

        elif decision== 'view':
            viewfunc()
            
           

            
       
        elif decision == 'mark':
            completetask()
           
           

            
        
        elif decision=='delete':
            deletetask()
        
    

            
        
    
    
    
    
if __name__ == "__main__":
    
    main()
