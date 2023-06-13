def get_username():
    """
    Gets the players name
    """
    print('Hello')
    while True:
        username = input('Enter username:')
        if username == '':
            print('You must enter a username')
            continue    
        else:        
            print('Welcome', username, 'lets get started')
            break



get_username()