class SeniorHall:
    def __init__(self,global_state,inventory):
        self.global_state = global_state
        self.inventory = inventory
        self.set_state()
        self.name = "Senior Hall"
        self.description = """You're in Senior Hall, the central upstairs hallway of the school."""
        print(self.description())
        self.run()
        
    def run(self):
        self.route(input(">>"))
           
    def route(self,command):
        if command in ["go north","go south","go east","go west"]:
            self.move(command.split(" ")[1])
        

    def move(self,direction):
        for key in self.state.keys():
            self.global_state[self.name+"_"+key] = self.state[key]
        if direction == "south":
            print("You can't go that way!")
        if direction == "north":
            room = ScienceHall(self.global_state,self.inventory)
            room.run()
        if direction == "east":
             room = MainHall(self.global_state,self.inventory)
            room.run()
        if direction == "west":
            room = HistoryHall(self.global_state,self.inventory)
            room.run()

