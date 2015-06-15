class Food_Science_Hall:
    def _init_(self,global_state,inventory):
        self.global_state = global_state
        self.inventory = inventory
        self.set_state()
        self.name = "Food Science Hall"
        if floor1_is_flooded:
            self.description = """You are in the Food Science Hall.
            Various kitchen items float past you. The Food Science room seems to
            be open. A locker is ajar."""
        if not floor1_is_flooded:
            self.description = """You are in the Food Science Hall.
            Various kitchen items litter the floor. You hear a beeping from the
            Food Science room."""
        print(self.description())
        self.run()

    def run(self):
        self.route(input(">>"))

    def route(self,command):
        if command in ["enter Food Science room", "go south"]:
            self.move(command)
        else:
            if command in ["open locker"]:
                print("There is nothing in the locker.")
            else:
                print("What?")
            self.run()

    def move(self,direction):
        if direction == "enter Food Science room":
            room = Food_Science_Room(self.global_state,self.inventory)
            room.run()
        if direction == "go south":
            room = Main_Hall(self.global_state,self.inventory)
            room.run()

    def set_state(self):
        self.state={}
        
    
            
    
    
    
