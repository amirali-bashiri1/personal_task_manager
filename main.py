

from tasks import show_tasks, save_tasks
from dotenv import load_dotenv
import os

load_dotenv()

password = os.getenv("TASK_MANAGER_ADMIN_PASSWORD")

name = input("Enter your name: ")

print("Welcome", name)

admin = input("Do you want to enter Admin Mode? (yes/no): ")

if admin == "yes":
    user_password = input("Enter admin password: ")

    if user_password == password:
        print("Admin Mode enabled")
    else:
        print("Wrong password")

tasks = []

for i in range(3):
    task = input("Enter a task: ")
    tasks.append(task)
save_tasks(tasks)
show_tasks(tasks)
