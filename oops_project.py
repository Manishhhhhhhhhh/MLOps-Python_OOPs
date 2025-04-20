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
                            3. Press 3 to post.
                            4. Press 4 to message a friend.
                            5. Press any other key to exit.""")
        if userInput == "1":
            self.signUp()
        elif userInput == "2":
            self.signIn()
        elif userInput == "3":
            pass
        elif userInput == "4":
            pass
        else:
            exit()

    def signUp(self):
        email = input("Enter your email here.")
        password = input("Enter your password.")
        self.userName = email
        self.password = password
        print("You have signed up successfully.")
        print("\n")
        self.menu()

    def signIn(self):
        if self.userName == "" and self.password == "":
            print("Please signup first by pressing 1 in the main menu.")
        else:
            userNamee = input("Enter your user name.")
            inputPassword = input("Enter your password.")

            if self.userName == userNamee and self.password == inputPassword:
                print("You have signed in successfully.")
                self.loggedIn = True
            else:
                print("Please input correct credentials.")
        
        print("\n")
        self.menu()


obj = chatBook()
    