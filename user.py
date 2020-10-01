   class User:
    """
    Class that generates a new user.
    """
    User = []

    def __init__(self,user_name,password):

        self.user_name = username
        self.password= password
        
    def save_user(self):
		'''
		Function to save a newly created user instance.
		'''
		User.users_list.append(self)
		