users = [
    {'username':"user1",'password':'qwertyuiop'},
    {'username':"user2",'password':'poiuytrewq'},
    {'username':"user3",'password':'wertyuiopq'},
    {'username':"user4",'password':'owqpertyui'}
]

def login_required(func):
    """A decorator that checks if the user is 
    logged into thir account and has valid credenials
    
    :params: username, password
    :return: your credentials
    """
    def wrapper(credentials):
        username = credentials.get('username')
        password = credentials.get('password')
        for user in users:
            if user['username'] == username and user['password'] == password:
                print('login successful')
                return func(credentials)
            print('Invalid username or password')

            if username not in users:
                print('User not found')
    return wrapper


def age_check(func):
    """A decorator that checks if a user is
    eligible for voting or not ie. 
    it either lives in india or not

    :params: credentials
    :return: access to voting
    """
    def inner(credentials):
        if credentials['age'] > 18 and credentials['nationality'] == 'Indian':
            print("You are eligible for voting")
            return func(credentials)
        else:
            if credentials['age'] <= 18 or credentials['nationality'] != 'Indian':
                print("You are not eligible for voting")

    return inner

@login_required
@age_check
def voting_system(credentials):
    print('Welcome to the voting System')
    print('...')
    print('...')
    print('Vote for a Squadron Leader')
    print('1: You')
    print('2: player2')
    print('3: player3')
    print('4: player4')
    options = int(input("Select the options above:- \n"))
    if options not in range(1,5):
        print('please enter a valid value')
        options = int(input("Select the options above:- \n"))
    if options == 1:
        print('You have voted for yourself')
    if options == 2:
        print('You have voted for player 2')
    if options == 3:
        print('You have voted for player: 3')
    if options == 4:
        print('You have voted for player 4')
    print('thank you for voting')

    
username=input("Enter Your Username:-")
password=input("Enter Your password:-")
age=int(input("Enter Your age:-"))
nationality=input("Enter Your Nationality:-")

data={"username":username,"password":password,"age":age,"nationality":nationality}


voting_system(data)



        