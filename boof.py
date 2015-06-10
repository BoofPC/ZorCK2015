class Boof:
    def __init__(self,global_state,inventory):
        self.global_state = global_state
        self.inventory = inventory
        self.set_state()
        self.name = "boof's room"
        self.description = """You enter Boof's room. It is a disorganized disaster with a chilling sense of order. That doesn't make sense. Maybe it's the stark, hospital white walls which encompass the room without any sign of decoration. You hear the faint sobs of past physics students coming from everywhere."""
        self.description_with_planner = """You enter Boof's room. It is a disorganized disaster with a chilling sense of order. That doesn't make sense. Maybe it's the stark, hospital white walls which encompass the room without any sign of decoration. You hear the faint sobs of past physics students coming from everywhere. There is a planner left on one of the desks."""
        self.route("look")
        self.run()
        
    def run():
        self.route(input(">>"))
           
    def route(command):
        if command in ["exit","leave"]:
            exit()
        else:
            if command in ["take planner","get planner","grab planner","pick up planner"]:
                take_planner()
            elif command in ["look","look around","description"]:
                if "planner" in self.inventory:
                    print(self.description)
                else:
                    print(self.description_with_planner)
                
            else:
                print("WAT!?")
            self.run()

    def exit():
        for key in self.state.keys():
            self.global_state[self.name+"_"+key] = self.state[key]
        room = ScienceHall(self.global_state,self.inventory)
        room.run()

    def set_state():
        self.state={}

    def take_planner():
        if "planner" in self.inventory:
            print("You already took the planner.")
        else:
            print("You grab the planner.")
            self.inventory.append("planner")

    
