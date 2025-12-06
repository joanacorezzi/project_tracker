class Person:
    # Class attribute to generate IDs
    _id_counter = 1

    def __init__(self, name, email, id=None):
       
        self._name = name
        self._email = email

        if id is not None:
            self.id = id
        else:
            self.id = Person._id_counter
            Person._id_counter += 1

    # properties

    @property
    def name(self):
        #Get the name
        return self._name

    @name.setter
    def name(self, value):
        #Set the name
        self._name = value

    @property
    def email(self):
        #Get the email
        return self._email

    @email.setter
    def email(self, value):
        # Set the email

        if "@" not in value:
            raise ValueError("Email must contain '@'")
        self._email = value

    # JSON helpers

    def to_dict(self):
        #Convert Person to a dictionary
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
        }

    @classmethod
    def from_dict(cls, data):
        #Create a Person from a dictionary
        return cls(
            name=data.get("name", ""),
            email=data.get("email", ""),
            id=data.get("id"),
        )

    def __str__(self):
        #string representation
        return f"Person(id={self.id}, name={self.name}, email={self.email})"


class User(Person):

    def __init__(self, name, email, id=None):

        super().__init__(name, email, id=id)
        
        self.projects = []

    def add_project(self, project):
        #Attach a project object to this user
        self.projects.append(project)

    def list_projects(self):
        #Return the list of projects
        return self.projects

    def to_dict(self):
       #Convert User to a dictionary
       
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
        }

    @classmethod
    def from_dict(cls, data):
        #Create a User from a dictionary
        return cls(
            name=data.get("name", ""),
            email=data.get("email", ""),
            id=data.get("id"),
        )

    def __str__(self):
        #Nice string representation
        return f"User(id={self.id}, name={self.name}, email={self.email})"