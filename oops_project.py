class chatBook:

    __userID = 1

    def __init__(self):
        self.__name = 'Default User'  ## this is now hidden and cannot be accessed(but can be accessed if it is accessed like self._obj__attrName. This is called Encapsulation.)
        self.id = chatBook.__userID
        chatBook.__userID += 1
        self.userName = ''
        self.password = ''
        self.loggedIn = False
        #self.menu()

    @staticmethod
    def getter_id():
        return chatBook.__userID
    
    @staticmethod
    def setter_id(val):
        chatBook.__userID = val

    def getter_name(self):
        return self.__name
    
    def setter_name(self,value):
        self.__name = value
        


    def menu(self):
        userInput = input("""Welcome to ChatBook!! How would you like to proceed?
                            1. Press 1 to Sign Up.
                            2. Press 2 to Sign In.
                            3. Press 3 to post.
                            4. Press 4 to message a friend.
                            5. Press any other key to exit.-->  """)
        if userInput == "1":
            self.signUp()
        elif userInput == "2":
            self.signIn()
        elif userInput == "3":
            self.myPost()
        elif userInput == "4":
            self.sendMessage()
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

    def myPost(self):
        if self.loggedIn == True:
            txt = input("Enter your message here.")
            print(f"Following content has been posted --> {txt}")
        else:
            print("You need to sign in first to post")
        print("\n")
        self.menu()

    def sendMessage(self):
        if self.loggedIn == True:
            txt = input("Enter your message here.")
            frnd = input("Whom to send the message?")
            print(f"Your message has been sent to {frnd}")
        else:
            print("You need to sign in first to post something...")
        print("\n")
        self.menu()



#obj = chatBook()
    