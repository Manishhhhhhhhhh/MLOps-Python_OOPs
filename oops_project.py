class chatBook:

    def __init__(self):
        self.userName = ''
        self.password = ''
        self.loggedIn = False
        self.menu()


    def menu(self):
        userInput = input("""Welcome to ChatBook!! How would you like to proceed?
                            1. Press 1 to Sign Up.
                            2. Press 2 to Sign In.
                            3. Press 3 t post.
                            4. Press 4 to message a friend.
                            5. Press any other key to exit.""")
        if userInput == "1":
            pass
        elif userInput == "2":
            pass
        elif userInput == "3":
            pass
        elif userInput == "4":
            pass
        else:
            exit()

obj = chatBook()
    