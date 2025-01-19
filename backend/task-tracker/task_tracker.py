import json
import sys
import logging
from datetime import datetime
logging.basicConfig(level=logging.INFO, format="%(message)s")

FILE_NAME = "tasks.json"

# タスクを読み込む
def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# タスクを保存する
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# タスクを追加する
def add_task(description):
    tasks = load_tasks()
    new_task = {
        "id": len(tasks) + 1,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat(),
    }
    tasks.append(new_task)
    save_tasks(tasks)
    logging.info(f"Task added successfully (ID: {new_task['id']})")

# タスクを更新する
def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            logging.info(f"Task ID {task_id} updated successfully.")
            return
    logging.info(f"Task ID {task_id} not found.")

# タスクを削除する
def delete_task(task_id):
    tasks = load_tasks()
    updated_tasks = [task for task in tasks if task["id"] != task_id]
    if len(tasks) == len(updated_tasks):
        logging.info(f"Task ID {task_id} not found.")
    else:
        save_tasks(updated_tasks)
        logging.info(f"Task ID {task_id} deleted successfully.")

# ステータスを進行中に変更する
def mark_in_progress(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "in-progress"
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            logging.info(f"Task ID {task_id} marked as in-progress.")
            return
    logging.info(f"Task ID {task_id} not found.")

# ステータスを完了に変更する
def mark_done(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            logging.info(f"Task ID {task_id} marked as done.")
            return
    logging.info(f"Task ID {task_id} not found.")

# タスクをリストアップする
def list_tasks(status=None):
    tasks = load_tasks()
    if status:
        tasks = [task for task in tasks if task["status"] == status]
    if not tasks:
        logging.info("No tasks found.")
    for task in tasks:
        logging.info(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, "
                     f"Created At: {task['createdAt']}, Updated At: {task['updatedAt']}")
# メイン関数
def main():
    if len(sys.argv) < 2:
        logging.info("Usage: task-cli [command] [arguments]")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            logging.info("Error: No task description provided.")
        else:
            add_task(" ".join(sys.argv[2:]))

    elif command == "update":
        if len(sys.argv) < 4:
            logging.info("Error: Task ID and new description required.")
        else:
            try:
                task_id = int(sys.argv[2])
                update_task(task_id, " ".join(sys.argv[3:]))
            except ValueError:
                logging.info("Error: Task ID must be an integer.")

    elif command == "delete":
        if len(sys.argv) < 3:
            logging.info("Error: Task ID required.")
        else:
            try:
                task_id = int(sys.argv[2])
                delete_task(task_id)
            except ValueError:
                logging.info("Error: Task ID must be an integer.")

    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            logging.info("Error: Task ID required.")
        else:
            try:
                task_id = int(sys.argv[2])
                mark_in_progress(task_id)
            except ValueError:
                logging.info("Error: Task ID must be an integer.")

    elif command == "mark-done":
        if len(sys.argv) < 3:
            logging.info("Error: Task ID required.")
        else:
            try:
                task_id = int(sys.argv[2])
                mark_done(task_id)
            except ValueError:
                logging.info("Error: Task ID must be an integer.")

    elif command == "list":
        status = sys.argv[2] if len(sys.argv) > 2 else None
        list_tasks(status)

    else:
        logging.info("Unknown command. Available commands are: add, update, delete, mark-in-progress, mark-done, list")

if __name__ == "__main__":
    main()
