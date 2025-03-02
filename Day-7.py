# 📢 Day 7 – Daily Python Challenge 🐍
# 🚀 Challenge:
# Aaj ka challenge ek mini project hoga! Tumhe ek "To-Do List CLI App" banani hai jo user se tasks store kare,
# show kare aur delete bhi kar sake! 📝✅❌

# Day-7.py

tasks = []

def show_tasks():
    if not tasks:
        print("Koi tasks nahi hain!")
    else:
        print("Aapke tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' add kiya gaya hai.")

def delete_task(task_number):
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task}' delete kiya gaya hai.")
    else:
        print("Invalid task number!")

def main():
    while True:
        print("\nTo-Do List CLI App")
        print("1. Task add karein")
        print("2. Tasks dekhein")
        print("3. Task delete karein")
        print("4. Exit karein")
        
        choice = input("Apna choice daalein (1/2/3/4): ")
        
        if choice == '1':
            task = input("Task daalein: ")
            add_task(task)
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            task_number = int(input("Delete karne ke liye task number daalein: "))
            delete_task(task_number)
        elif choice == '4':
            print("App se exit ho rahe hain. Shukriya!")
            break
        else:
            print("Invalid choice! Kripya sahi option daalein.")

if __name__ == "__main__":
    main()