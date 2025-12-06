class Task:
   # Task class
   
    _id_counter = 1  # class attribute for IDs

    def __init__(self, title, assigned_to=None, status="pending", project_id=None, id=None):
        #Initialize a Task
        if not title:
            raise ValueError("Task title cannot be empty.")

        self._title = title
        self._status = status
        self.assigned_to = assigned_to
        self.project_id = project_id

        if id is not None:
            self.id = id
        else:
            self.id = Task._id_counter
            Task._id_counter += 1

    # properties

    @property
    def title(self):
        #Get the task title
        return self._title

    @title.setter
    def title(self, value):
        #Set the task title
        if not value:
            raise ValueError("Task title cannot be empty.")
        self._title = value

    @property
    def status(self):
        #Get the task status
        return self._status

    @status.setter
    def status(self, value):
       #Set the task status

        if value not in ["pending", "complete"]:
            raise ValueError("Status must be 'pending' or 'complete'.")
        self._status = value


    def mark_complete(self):
        #Mark task as complete
        self.status = "complete"

    # JSON helpers

    def to_dict(self):
        #Convert Task to a dictionary
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status,
            "assigned_to": self.assigned_to,
            "project_id": self.project_id,
        }

    @classmethod
    def from_dict(cls, data):
        #Create a Task 
        return cls(
            title=data.get("title", ""),
            assigned_to=data.get("assigned_to"),
            status=data.get("status", "pending"),
            project_id=data.get("project_id"),
            id=data.get("id"),
        )

    def __str__(self):
        
        return (
            f"Task(id={self.id}, title={self.title}, "
            f"status={self.status}, assigned_to={self.assigned_to}, "
            f"project_id={self.project_id})"
        )
