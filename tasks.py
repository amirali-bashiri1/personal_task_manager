def show_tasks(tasks):
    print("Your tasks:")

    for task in tasks:
        print("-", task)


def save_tasks(tasks):
    file = open("tasks.txt", "a")

    for task in tasks:
        file.write(task + "\n")

    file.close()