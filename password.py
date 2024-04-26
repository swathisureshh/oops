class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, entered_username, entered_password):
        if entered_username == self.username and entered_password == self.password:
            return True
        else:
            return False
user1 = User("myusername", "mypassword")
entered_username = input("Enter your username: ")
entered_password = input("Enter your password: ")

if user1.login(entered_username, entered_password):
    print("Login successful!")
else:
    print("Invalid username or password.")