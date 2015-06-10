class Birkenfeld_Room:
    def __init__(self, global_state, inventory):
        self.global_state = global_state
        self.inventory = inventory
        self.set_state()
        self.name = "Mr. Birkenfeld's Room"
        self.description = """You're in a very messy classroom. You see glassware strewn everywhere, a room full of chemicals
                              in the back, and a very loud man sitting at his desk."""
        print(self.description())
        self.run()

    def run():
        self.route(input(">>"))

    def route(command):
        if command in ["enter hallway", "enter back room"]:
            move(command.split(" ")[1])
        else:
            if command in ["talk to man", "talk to teacher", "speak with man", "speak with teacher"]:
                talk_to_birk()
            elif command in ["do packet", "finish packet", "complete packet"]:
                finish_packet()
            elif command in ["look", "look around", "description"]:
                print(self.description)
            else:
                print("WAT!?!?!?!?")
            self.run()

    def move(direction):
        for key in self.state.keys():
            self.global_state[self.name + "_" + key] = self.state[key]
            
        if direction == "hallway":
            room = ScienceHallway(self.global_state, self.inventory)
            room.run()
        elif direction == "back room" or direction == "chemical room":
            print("YOU CAN'T GO IN THERE! BOOOOOOOOOOOOOOOM!")
        else:
            print("You can't go that way.")

    def set_state():
        self.state = {}
        self.state["talked_to_birk"] = False
        self.state["done_packet"] = False
        self.state["break_glass"] = False

    def talk_to_birk():
        if not self.state["talked_to_birk"]:
            print("""HELLO THERE, YOUNG SCHOLAR. HAVE YOU FINISHED YOUR HOMEWORK?""")
            self.state["talked_to_birk"] = True
        elif self.state["talked_to_birk"] and not self.state["done_packet"]:
            print("""DO YOUR HOMEWORK!!!""")
        else:
            print("""GOOD WORK, YOUNG SCHOLAR!!!""")
            self.inventory["letter of rec"] = True

    def finish_packet():
        if not self.state["done_packet"]:
            print("""You spend 17 hours finishing your packet.""")
        else:
            print("""You're already done!""")
