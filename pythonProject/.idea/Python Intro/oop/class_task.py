from datetime import datetime


class Task:
    task_id_counter = 1  # Just initialized counter for generating task IDs

    def __init__(self, description, due_date):
        self.task_id = Task.task_id_counter
        Task.task_id_counter += 1  # Increment the counter for the next task
        self.description = description
        self.due_date = due_date
        self.status = "Pending"  # Default status

    def __str__(self):
        return f"Task ID: {self.task_id}\nDescription: {self.description}\nDue Date: {self.due_date}\nStatus: {self.status}"

    def change_status(self, new_status):
        valid_statuses = ["Pending", "In Progress", "Completed", "Cancelled"]  # Define valid statuses
        if new_status in valid_statuses:
            self.status = new_status
            return True
        return False


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def update_task(self, task_id, new_description, new_due_date):
        for task in self.tasks:
            if task.task_id == task_id:
                task.description = new_description
                task.due_date = new_due_date
                return True
        return False

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                return True
        return False

    def view_tasks_by_status(self, status):
        return [task for task in self.tasks if task.status == status]

    # just try to understand how this 'lambda' works! If you do not get it, skip it
    def view_tasks_by_due_date(self):
        return sorted(self.tasks, key=lambda task: task.due_date)


class TaskManager:
    def __init__(self):
        self.users = {}

    def register_user(self, username, password):
        if username in self.users:
            return False  # User already exists
        self.users[username] = User(username, password)
        return True

    def login_user(self, username, _password):
        if username in self.users and self.users[username].password == _password:
            return self.users[username]
        return None  # Invalid credentials


# Example usage:
if __name__ == "__main__":
    task_manager = TaskManager()

    # Register new users
    task_manager.register_user("user1", "password1")
    task_manager.register_user("user2", "password2")

    # Login with valid credentials
    user1 = task_manager.login_user("user1", "password1")
    if user1:
        # Create tasks
        task1 = Task("Complete the workflow of retouched.ai", datetime(2024, 4, 30))
        task2 = Task("Submit weekly report", datetime(2024, 5, 2))

        # Add tasks to user1
        user1.add_task(task1)
        user1.add_task(task2)

        # View tasks by due date
        print("Tasks by due date:")
        for task in user1.view_tasks_by_due_date():
            print(task)

        # Update a task
        user1.update_task(task1.task_id, "Complete the Binary Search Tree Studies!", datetime(2024, 4, 25))

        # Change task status
        task1.change_status("In Progress")

        # View tasks by status
        print("\nTasks by status (In Progress):")
        in_progress_tasks = user1.view_tasks_by_status("In Progress")
        for task in in_progress_tasks:
            print(task)

        # Delete a task
        user1.delete_task(task2.task_id)

        print("\nAfter deleting a task:")
        for task in user1.view_tasks_by_due_date():
            print(task)
    else:
        print("Invalid username or password")

