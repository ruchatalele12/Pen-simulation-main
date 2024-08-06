class Pen:
    def __init__(self, pen_type, ink_level=50):
        self.pen_type = pen_type
        self.ink_level = ink_level
        self.texts_written = []
        self.file_name = "written_story.txt"
        self.score = 0

    def write(self):
        while input("Do you want to write something? (yes/no): ").strip().lower() == "yes":
            self.ink_color = self.get_valid_ink_color()
            self.nib_type = self.get_valid_nib_type()
            self.cartridge_type = self.get_valid_cartridge_type()
            user_text = input("Write your thoughts: ").strip()
            if self.decrease_ink(user_text):
                self.texts_written.append(user_text)
                self.score += len(user_text.split())
                self.append_to_file(user_text)
            else:
                break

    def get_valid_ink_color(self):
        while True:
            ink_color = input("Ink color (blue/black/red): ").strip().lower()
            if ink_color in ['blue', 'black', 'red']:
                return ink_color
            else:
                print("Invalid ink color! Please choose from 'blue', 'black', or 'red'.")

    def get_valid_nib_type(self):
        while True:
            nib_type = input("Nib type (fine/medium/bold): ").strip().lower()
            if nib_type in ['fine', 'medium', 'bold']:
                return nib_type
            else:
                print("Invalid nib type! Please choose from 'fine', 'medium', or 'bold'.")

    def get_valid_cartridge_type(self):
        while True:
            cartridge_type = input("Cartridge type (standard/large): ").strip().lower()
            if cartridge_type in ['standard', 'large']:
                return cartridge_type
            else:
                print("Invalid cartridge type! Please choose 'standard' or 'large'.")

    def decrease_ink(self, text):
        words_written = len(text.split())
        ink_needed = words_written * self.get_ink_needed_multiplier()
        if self.ink_level >= ink_needed:
            self.ink_level -= ink_needed
            print(f"Ink level: {self.ink_level}")
            return True
        else:
            if input("Not enough ink! Refill? (yes/no): ").strip().lower() == "yes":
                self.ink_level += ink_needed
                print(f"Ink refilled to {self.ink_level}")
                return True
            else:
                print(f"Game over! Ink level: {self.ink_level}")
                return False

    def append_to_file(self, text):
        with open(self.file_name, 'a') as file:
            file.write(text + '\n')

    def read_file(self):
        try:
            with open(self.file_name, 'r') as file:
                print("=======** Contents of written_story.txt **=======")
                print(file.read())
        except FileNotFoundError:
            print("File not found.")

    def get_ink_needed_multiplier(self):
        nib_multipliers = {'fine': 1, 'medium': 2, 'bold': 3}
        cartridge_multipliers = {'standard': 2, 'large': 3}
        return nib_multipliers.get(self.nib_type) * cartridge_multipliers.get(self.cartridge_type)
