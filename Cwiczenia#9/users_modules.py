"""Classes for Users, Privileges and Admin."""

class User:
    """Short class of simple user."""

    def __init__(self, first_name, last_name, nickname, user_age):
        """Initialize information about user"""
        self.full_name = f"{first_name} {last_name}"
        self.first_name = first_name
        self.last_name = last_name
        self.nickname = nickname
        self.user_age = user_age

    def describe_user(self):
        """prints a summary of the users information."""
        self.current_user = {
            "first name": self.first_name, 
            "second name": self.last_name, 
            "nickname": self.nickname,
            "user age": self.user_age
        }
        print(self.current_user)

    def greet_user(self):
        """prints a personalized greeting to the user."""
        print(f"{self.full_name} / {self.nickname} hello and welcome!\n")

class Privileges:
    """Class for describing privileges."""

    def __init__(self, *privileges):
        """Stores a list of privileges."""
        self.privileges = privileges

    def show_privileges(self):
        """Prints list of privilages."""
        print(f"List of current privilages:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    """Special "admin" subclass of user."""
    def __init__(self, first_name, last_name, nickname, user_age):   
        
        """Inheriting attributes from parent class."""
        super().__init__(first_name, last_name, nickname, user_age)
        
        self.privileges = Privileges('can ban users', 'can edit posts'\
 , 'is your master', 'can call you a pleb')
