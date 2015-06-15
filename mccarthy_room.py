class MccarthyRoom:
    def _init_(self,global_state,inventory):
        self.global_state = global_state
        self.inventory = inventory
        self.set_state()
        self.name = "mccarthy_room"
        self.description = "You're in Room 204--McCarthy room."
        print(self.description())
        self.run()

    def run(self):
        self.route(input(">>"))

    def route(self,command):
        if command in ["exit","exit room"]:
            self.move(command.split(" ")[1])
        else:
            if command in ["talk to mccarthy","speak with mccarthy","speak to mccarthy"]:
                self.talk_to_mccarthy()
            elif command in ["look","look around","description"]:
                print(self.description)
                if not self.state["took_pickle"]:
                    print("You see a pickle hanging from the ceiling.")
            elif command in ["take pickle","get pickle", "take pickle"]:
                self.take_pickle()
            else:
                print("Sorry, what was that?")
            self.run()

    def move(self,direction):
        for key in self.state.keys():
            self.global_state[self.name+"_"+key] = self.state[key]
        room = EnglishHall(self.global_state,self.inventory)
        room.run()

    def set_state(self):
        self.state={}
        self.state["talked_to_mccarthy"] = False
        self.state["took_pickle"] = False

    def talk_to_mccarthy(self):
        if not self.state["talked_to_mccarthy"]:
            print("""
What's up dude? How's it going? Where's yo lover?
You're always seen with yo lover, but I guess today it's just you?
I'm gonna seranade for you anyways--*McCarthy starts seranading you*
You are my fire, the one desire, believe when I say...
""")
            self.state["talked_to_mccarthy"] = True
        else:
            print("""
You already talked to him.
McCarthy keeps seranading--you better just leave him alone.
""")
            
    def take_pickle(self):
        if not self.state["took_pickle"]:
            print("""
Pickle taken. How are you going use it? Maybe it will come in handy later.
                  """)
            self.inventory["pickle"] = True
            self.state["took_pickle"] = True
        else:
            print("You already took the pickle.")
        
