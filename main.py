from pen import Pen

def pen_func():
    pen_type = input("Enter the type of pen you want: ").strip()
    print(pen_type)
    my_pen = Pen(pen_type)
    print(f"Welcome! You have a {my_pen.pen_type} with {my_pen.ink_level} units of ink.")
    my_pen.write()
    print(f"Game Over! Ink level: {my_pen.ink_level}")
    print(f"Texts written: {my_pen.texts_written}")
    print(f"Well done you got: {my_pen.score} points")
    if input("Read the file 'written_story.txt'? (yes/no): ").strip().lower() == "yes":
        my_pen.read_file()

if __name__ == "__main__":
    pen_func()