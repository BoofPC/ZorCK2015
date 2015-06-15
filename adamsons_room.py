class AdamsonRoom:
    def __init__(self,global_state,inventory):
        self.global_state = global_state
        self.inventory = inventory
        self.set_state()
        self.name = "Adamson's Room"
        self.description = """You find yourself in a large room among many ancient machines.
A small banner at the top of the doorway reads "The geeks shall inherit the earth."
Threre is a very messy desk and an array of shelves toward the front of the room.
A machine labeled "MakerBot" is found at the back of the room, along with several plastic robots.
The door exits to the north."""
        # http://cougarchronicle.org/wp-content/uploads/2014/12/adamson-900x519.jpg
        print(self.description())
        self.run()
        
    def run():
        self.route(input(">>"))
           
    def route(command):
        if command in ["go north","go south","go east","go west"]:
            move(command.split(" ")[1])
        else:
            if command in ["examine shelves","open shelves","see shelves", "look at shelves"]:
                examine_shelves()
            elif command in ["read book", "take book", "look at book", "examine book"]:
                read_book()
            elif command in ["examine bot","examine makerbot","examine maker bot","use bot","use makerbot","use maker bot"]:
                use_bot()
            elif command in ["look","look around","description", "see"]:
                print(self.description)
            else:
                print("WAT!?")
            self.run()

    def move(direction):
        for key in self.state.keys():
            self.global_state[self.name+"_"+key] = self.state[key]
        if direction == "north":
            exit() # i hope this works
        if direction == "west":
            print("A wall prevents you from moving there!")
        if direction == "east":
            print("A wall prevents you from moving there!")
        if direction == "south":
            print("Windows block your path.")

    def set_state():
        self.state={}
        self.state["examined_shelves"] = False
        self.state["read_book"] = False

    def examine_shelves():
        print("""
        The shelves reveal a number of plastic figurines, along with many machine parts and books. One of the books catches your eye.
        """)
        self.state["examined_shelves"] = True

    def read_book():
        if not self.state["examined_shelves"]:
            print("I don't see any books.")
        else:
            print("""The book's titled is revealed to be "Your Guide To The MakerBot".
Reading the book provides you with invaluable knowledge on how to operate this 3D printer.""")
            self.state["read_book"] = True

    def use_bot():
        if self.state["read_book"] and not self.state["used_machine"]:
            # guess who the bald man is
            print("""
            You activate the MakerBot, a tiny figure in the shape of a bald man is printed.
            As you examine the figure, you realize that it's made out of pure sapphire.
            """)
            self.state["used_machine"] = True
            self.inventory["sapphire_figure"] = True
        else:
            print("""
            It is a fascinating machine, but you have no idea how to operate it.
            """)
    