class Food_Science_Room:
    def_init_(self,global_state,inventory):
        self.global_state = global_state
        self.inventory = inventory
        self.set_state()
        self.name = "food_science_room"
        self.description = """You enter the food science. culinary utensils now litter the floor. You hear a beeping from the ovens."""
        print(self.description())
        self.run()
    def run(self):
        self.route(input(">>"))
    def route(self,command):
        if command in ["go north","go south","go east","go west"]:
            move(command.split(" ")[1])
            else:
                if command in ["open oven","oven?","dat oven?", "the Oven?"]:
                    self.open_oven()
                elif command in [" Turn off the oven", "Apago el horno"]:
                    self.turn_off_oven()
                elif command in ["look","look around","examine"]:
                    print(self.description)
                else:
                    print("What you said?")
                self.run()
   def move(self,direction):
        for key in self.state.keys():
            self.global_state[self.name+"_"+key] = self.state[key]
        if direction == "north":
           room = Food_Science_Hall(self.global_state,self.inventory)
           room.run()
        if direction == "west":
            print("Homie quit running into walls")
        if direction == "east":
            print("Quit running into walls making a damn fool of youself")
        if direction == "south":
            print("You are abouta jump outta window! Get you suicidal butt in the classroom!")
   def set_state(self):
       self.state={}
       self.state["opened_oven"]= False
       self.state["oven_off"]=False
    def open_oven(self):
        if not self.state["opened_oven"]:
            print("his oven is full of burning baked goods. A plume of smoke rises to the ceiling. You should prolly turn it off")
        else:
            print("You know what kinda unholy creation is in that, jus' make sure it is off")
    def turn_off_oven(self):
        if not self.state["talked_to_dwarf"]:
            print("what how is it still beeping? well atleast it isn't hot and stuff")
            self.state["oven_off"]= True
        else:
            print("Dude it is off already. What is dead may never die!")
        
