import re
class User:
    """
    Class created to initialise and define User objects.
    """
    def __init__(self,id,name,username,password):
        self.id = id
        self.name =  name
        self.username = username
        self.password = password

    def __repr__(self):
        return f'id:{self.id}, name : {self.name}, username : {self.username}, password: {self.password}'


class System:
    '''
    the system on which the users will be stored and loggeed in and logged out users will be tracked.
    '''
    def __init__(self,name):
        self.system_name = name
        self.users = [] # <- Storing our users from class User here

    def signup(self,name,username,password):
        '''
        a signup method with simple password validation
        '''
        new_user = User(id = len(self.users) +1,
                        name=name,
                        username = username,
                        password = password
                        )
        for user in self.users:
            if username == user.username:
                return 'Username already exists pick another username'
            
            if len(new_user.password) < 8:
                return 'password must be atleast 8 characters' 
             
            if not re.search(r'[A-Z]',new_user.password):
                return 'have some uppercase alphabets in your password'
            
            if not re.search(r'[a-z]',new_user.password):
                return 'have some lowercase alphabets in your password'
            
            if not re.search(r'[0-9]',new_user.password):
                return 'Have some numbers in your password.'
            
        self.users.append(new_user)
        return new_user
    


    
    def read_users(self):
        '''
        reading the users in the system
        '''
        for user in self.users:
            print(user)

    def logging_in(self,username,password):
        '''
        A method to verify the users in question
        '''
        user = next((user for user in self.users if user.username == username), None)
        if not user:
            return 'User not found'
        if user.password == password:
            return 'Logged in successfully'
        else:
            return 'Incorrect password'   




    
    def logging_out(self,username):
        '''
        a simple logout function
        ps. Doesnt really do anything here at the moment
        '''
        for user in self.users:
            if user.username == username:
                return 'Logged out successfully'



app = System('Application')      
app.system_name = 'test name'
app.signup('Name1','username4','Password1')
app.signup('Name2','username5','Password3')
app.read_users()
app.logging_in('username4','Password1')
app.logging_in('username5','Password3')
app.logging_out('username4')

