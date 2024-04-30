from datetime import datetime

tasks=[]

def ad_task():
    task=input("let's ADD your task in your list: \n")
    tasks.append(task)
def del_task():
    task=input("let's DELETE your completed or wrong task in your list: \n")
    if task in tasks:
        tasks.remove(task)
    else:
        print("OOPS! forget to add in list")
def lt_task(tasks):
    if tasks==[]:
        print("no tasks in there")
    else:
            return tasks
if __name__=="__main__":
    while True:
        print("\n list the plans-(myself-zz your to do list assistance )")
        i=input("WE HAVE 3 OPTION: you can create a file in 1.present and 2.future and 3.read the tasks list in past ")
        if i=="PRESENT" or i=="Present" or i=="present" or i=="Pres" or i=="pres" or i=="1" or i=="PRES":
            current_datetime = datetime.now().strftime("%Y-%m-%d") 
            str_current_datetime = str(current_datetime)
            file_name = str_current_datetime+".txt"
            i="0"
            while(i=="0"):
                a=input("enter 1 to add task and 2 to remove the task \n")
                if a=="1":
                    ad_task()
                elif a=="2":
                    del_task()
                i=input("enter 0 to add or remove: \n")       
        if i=="PAST" or i=="Past" or i=="past" or i=="Pst" or i=="pst" or i=="3" or i=="PST":
            past_datetime = input("enter the date in year-month-day")
            str_past_datetime = str(past_datetime)
            file_name = str_past_datetime+".txt"

        if i=="FUTURE" or i=="Furture" or i=="future" or i=="FUT" or i=="Fut" or i=="2" or i=="fut":
            future_datetime = input("enter the date in year-month-day")
            str_future_datetime = str(future_datetime)
            file_name = str_future_datetime+".txt"
            i="0"
            while(i=="0"):
                a=input("enter 1 to add task and 2 to remove the task \n")
                if a=="1":
                    ad_task()
                elif a=="2":
                    del_task()
                i=input("enter 0 to add or remove: \n")
        for task in tasks:
            print(task)
            file = open(file_name, 'a')
            file.write(str(task)+"\n")
            file.close()   