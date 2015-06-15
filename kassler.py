class Kassler:
    def_init_(self,global_state,inventory):
        self.global_state = global_state
        self.inventory = inventory
        self.set_state()
        self.name = "Kassler's Room"
        self.description = "You are in Kassler's Room. You are suddenly very sleepy. Let's look around!"
        print(self.description())
        self.run()

    def run(self):
        self.route(input(">>"))

    def route(self,command):
        if command in ["exit"]:
            self.move(command)
        if command in ["look around"]:
            self.look()
        if command in ["take planner"]:
            self.inventory["planner"] == True
            self.state[found_planner] == True
            print("There is a locker combination in the planner.")
        else:
            print("What?")
            
    def look(self):
        print(self.description())
        if self.state["found_planner"] == False:
            print("There is a planner on a desk.")

    def move(direction):
        if direction == "exit":
            room = EnglishHall(self.global_state,self.inventory)
            room.run()

    def set_state(self):
        self.state={}
        self.state["found_planner"] = False
