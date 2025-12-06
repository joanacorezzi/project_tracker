import unittest

from models import User, Project, Task


class TestModels(unittest.TestCase):
    #Basic tests 

    def test_create_user(self):
        #Test if a User is created with the right name and email
        user = User(name="Alex", email="alex@example.com")
        self.assertEqual(user.name, "Alex")
        self.assertEqual(user.email, "alex@example.com")

    def test_create_project(self):
        #Test if a Project stores its title and owner id
        project = Project(title="CLI Tool", description="Test", due_date="2025-12-31", owner_id=1)
        self.assertEqual(project.title, "CLI Tool")
        self.assertEqual(project.owner_id, 1)

    def test_task_mark_complete(self):
        #Test if a Task can be marked complete
        task = Task(title="Implement add-task", assigned_to="Alex", project_id=1)
        self.assertEqual(task.status, "pending")
        task.mark_complete()
        self.assertEqual(task.status, "complete")


if __name__ == "__main__":
    unittest.main()