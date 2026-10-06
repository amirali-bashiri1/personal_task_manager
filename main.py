from tasks import show_tasks, save_tasks

name = input("Enter your name: ")

print("Welcome", name)

tasks = []

for i in range(3):
    task = input("Enter a task: ")
    tasks.append(task)

save_tasks(tasks)

show_tasks(tasks)