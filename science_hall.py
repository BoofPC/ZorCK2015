class ScienceHall:

    if self.global_state["floor2_is_flooded"]:
        def __init__(self,global_state,inventory):
            self.global_state = global_state
            self.inventory = inventory
            self.set_state()
            self.name = "science_hall"
            self.description = """You are in the Science Hall.
It is flooded--microscopes are littered on the floor,
and lab papers are floating on the surface of the water.
To the north, the door that leads to Birkenfeld's room is open."""
            print(self.description())
            self.run()

        def run(self):
            self.route(input(">>"))

        def route(self,command):
            if command in ["go north","go east","go west","go south"]:
                self.move(command.split(" ")[1])
            else:
                if command in ["take microscope","pick up microscope"]:
                    self.take_microscope()
                elif command in ["take lab papers","take papers"]:
                    self.take_papers()
                elif command in ["enter room","go to birkenfeld's room","birkenfeld"]:
                    room = Birkenfeld(self.global_state,self.inventory)
                    room.run()
                elif command in ["look","look around","description"]:
                    print(self.description)
                else:
                    print("Sorry, what was that?")
                self.run()

        def move(self,direction):
            for key in self.state.keys():
                self.global_state[self.name+"_"+key] = self.state[key]
            if direction == "north":
                room = Birkenfeld(self.global_state,self.inventory)
                room.run()
            if direction == "west":
                print("All classrooms to the west seem to be locked.")
            if direction == "east":
                print("All classrooms to the east seem to be locked.")
            if direction == "south":
                room = SeniorHall(self.global_state,self.inventory)
                room.run()

        def set_state(self):
            self.state = {}
            self.state["took_microscope"] = False
            self.state["took_papers"] = False

        def take_microscope(self):
            if not self.state["took_microscope"]:
                print("Microscope taken. It's soaked and seems to be damaged.")
                self.state["took_microscope"] = True
                self.inventory["microscope"] = True
            else:
                print("You've already taken the microscope.")

        def take_papers(self):
            if not self.state["took_papers"]:
                print("Papers taken. They are soaked and on the verge of disintegrating.")
                self.state["took_papers"] = True
                self.inventory["papers"] = True
            else:
                print("You've already taken the papers.")

        
    else:
        def __init__(self,global_state,inventory):
            self.global_state = global_state
            self.inventory = inventory
            self.set_state()
            self.name = "science_hall"
            self.description = """You are in the Science Hall.
It is no longer flooded, but the carpet is wet.
To the north, the door that leads to Birkenfeld's room is open."""
            print(self.description())
            self.run()

        def run(self):
            self.route(input(">>"))

        def route(self,command):
            if command in ["go north","go east","go west","go south"]:
                self.move(command.split(" ")[1])
            else:
                elif command in ["enter room","go to birkenfeld's room","birkenfeld"]:
                    room = Birkenfeld(self.global_state,self.inventory)
                    room.run()
                elif command in ["look","look around","description"]:
                    print(self.description)
                else:
                    print("Sorry, what was that?")
                self.run()

        def move(self,direction):
            for key in self.state.keys():
                self.global_state[self.name+"_"+key] = self.state[key]
            if direction == "north":
                room = Birkenfeld(self.global_state,self.inventory)
                room.run()
            if direction == "west":
                print("All classrooms to the west seem to be locked.")
            if direction == "east":
                print("All classrooms to the east seem to be locked.")
            if direction == "south":
                room = SeniorHall(self.global_state,self.inventory)
                room.run()

        def set_state(self):
            self.state = {}
