class Project:

    _id_counter = 1  # class attribute for simple IDs

    def __init__(self, title, description="", due_date=None, owner_id=None, id=None):
       # Initialize a Project.

        if not title:
            raise ValueError("Project title cannot be empty.")

        self._title = title
        self.description = description
        self.due_date = due_date
        self.owner_id = owner_id  # link to User by id

        if id is not None:
            self.id = id
        else:
            self.id = Project._id_counter
            Project._id_counter += 1

      
        self.tasks = []

    # properties

    @property
    def title(self):
        #Get the project title
        return self._title

    @title.setter
    def title(self, value):
        #Set the project title
        if not value:
            raise ValueError("Project title cannot be empty.")
        self._title = value

    #helpers for tasks

    def add_task(self, task):
        #Attach a Task object 
        self.tasks.append(task)

    def list_tasks(self):
        #Return list of Task objects
        return self.tasks

    # JSON helpers 

    def to_dict(self):
     
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "owner_id": self.owner_id,
        }

    @classmethod
    def from_dict(cls, data):
        #Create a Project from a dictionary
        return cls(
            title=data.get("title", ""),
            description=data.get("description", ""),
            due_date=data.get("due_date"),
            owner_id=data.get("owner_id"),
            id=data.get("id"),
        )

    def __str__(self):
       
        return f"Project(id={self.id}, title={self.title}, due_date={self.due_date})"