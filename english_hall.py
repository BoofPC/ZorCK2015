class EnglishHall:
    def _init_(self,global_state,inventory):
        self.global_state = global_state
        self.inventory = inventory
        self.set_state()
        self.name = "English Hall"
        if floor1_is_flooded:
            self.description = "You are in the English Hall. The doors to McCarthy's and Kassler's rooms are unlocked. Some piranas hop down the stairs and swim down the hall. There is a locker."
        if not floor1_is_flooded:
            self.description = "You are in the English Hall. The doors to Mccarthy's and Kassler's rooms are unlocked. The floor is damp, and some piranas are dead on the floor. There is a locker."  
        print(self.description())
        self.run()

    def run(self):
        self.route(input(">>"))

    def route(self,command):
        if command in ["enter north","enter south","go east","go west"]:
            self.move(command)
        else:
            if command in ["open locker"]:
                if self.inventory["torn_planner"] == True:
                    self.inventory["sword"] == True;
                    print("You got a sword out of the locker!")
                if self.inventory["torn_planner"] == False:
                    print("The locker is locked.")               
            else:
                print("What?")
            self.run()

    def move(self,direction):
        if direction == "enter north":
            room = Kassler(self.global_state,self.inventory)
            room.run()
        if direction == "go west":
            room = Main_Hall(self.global_state,self.inventory)
            room.run()
        if direction == "go east":
            print("can't go that way!")
        if direction == "enter south":
            room = McCarthy(self.global_state,self.inventory)
            room.run()

    def set_state(self):
        self.state={}
        self.state["found_sword"] = False
        


        
        
    
