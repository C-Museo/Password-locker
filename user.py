   class User:
      '''
      Class that generates a new user.
      '''
    User = []

    def __init__(self,user_name,password):

        self.user_name = username
        self.password= password
        
    def save_user(self):
		  '''
		  Function to save a newly created user instance.
		  '''
		User.users_list.append(self)
		

    class Credentials:
      '''
      Class to create  account credentials, generate passwords and save their information
      '''
    Credentials = []

    def check_user(cls, user_name, password)
