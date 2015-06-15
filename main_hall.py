class Main_Hall:
    floor1_is_flooded = True
    if floor1_1_flooded = True:
        def __int__(self,global_state,inventory):
            self.global_state = global_state
            self.inventory = inventory
            self.set_state()
            self.description = """ You are the end end of senior hall near the library.
                               To the north there are stairs leading down to the main hall which looks flooded,
                               to the south there is a door that leads to the ASL room,
                               to the west is the history hall,
                               to the east is the senior hall. Choose wisely.. """
            print(self.description())
            self.run()
            

        def run(self):
            self.route(input(">>"))
    
        def route(self,command):
            if command in ["go north", "go south", "go east", "go west"]:
               self.move(command.split(" ")[1])
            else:
                if command in ["Walk down stairs", "Enter stairs", "pass through stairs,"]:
                    print("You cannot enter! The water is too deep to pass!")
                else:
                    print("What???")
                self.run()

        def move(direction):
            for key in self.state.keys():
                self.global_state[self.name+"_"+key] = self.state[key]
            if direction == "north":
                print("The stairs down to the art room seem to be flooded")
            if direction == "west":
                room = SeniorHall(self.global_state,self.inventory)
                room.run()
            if direction = "south":
                print("The doors to the ASL room seem to be locked.
                      "You look into the window but fail to see anything."
                      "It's too dark")
            for it is too dark")
            if direction = "east":
                room = HistoryHall(self.global_state,self.inventory)
                room.run()


    elif floor1_is_flooded = False
        def __int__(self,global_state,inventory):
            self.global_state = global_state
            self.inventory = inventory
            self.set_state()
            self.description = """ You are the end end of senior hall near the library.
                               To the north there are stairs leading down to the main hall which looks flooded,
                               to the south there is a door that leads to the ASL room,
                               to the west is the history hall,
                               to the east is the senior hall. Choose wisely... """
            print(self.description())
            self.run()

        def run(self):
            self.route(input(">>"))
    
        def route(self, command):
            if command in ["go north", "go south", "go east", "go west"]:
                self.move(command.split(" ")[1])
            else:
                if command in ["Walk down stairs", "Enter stairs", "pass through stairs,"]:
                   print("You are able to walk down the stairs and see that the main hall is no longer flooded")
                else:
                    print("What???")
                self.run()

        def move(direction):
            for key in self.state.kets():
                self.global_state[self.name+"_"+key] = self.state[key]
            if direction == "south":
                print("You see the the main entrance. It looks locked")
                if("Enter door", "Open door", "Pass through door")
                    print("You cannot go through this door")
            if direction == "west":
                room = EnglishHall(self.global_state,self.inventory)
                room.run()
            if direction = "north":
                room = ArtRoom(self.global_state,self.inventory)
                room.run()
            if direction = "east":
                print("Hmm...there is a giant hole in the middle of the floor...it's best that you dont pass through here..")
                      
                    
                      
        
           
        
            
