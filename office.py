class Office:
    def_init_(self,global_state,inventory):
        self.global_state = global_state
        self.inventory = inventory
        self.set_state()
        self.name = "Office"
        if floor1_is_flooded:
            self.description = """You are in the Office.
            You see office supplies floating about. Johnson looks very
            intently at you, beckoning you over."""
        if not floor1_is_flooded:
            self.description = """You are in the Office.
        The staff are wearing soggy clothes,organizing a walk out.
        Johnson gives you a stern look as if you should be doing something
        else right now.""")
        print(self.description())
        self.run()

    def run(self):
        self.route(input(">>"))

    def route(self,command):
        if command in ["exit"]:
            self.move(command)
        else:
            print("What?")
        self.run()

    def move(self,direction):
        if direction == "exit":
            room = MainHall(self.global_state,self.inventory)
            room.run()

    def set_state(self):
        self.state{}
