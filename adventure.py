import time

def print_slow(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def make_decision(prompt, options):
    print_slow(prompt)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    while True:
        choice = input("Enter your choice (1-{len(options)}): ")
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice)
        else:
            print(f"Invalid choice. Please enter a number between 1 and {len(options)}.")

def ending(result):
    print_slow("----- THE END -----")
    if result == "good":
        print_slow("Congratulations! You have reached a good ending.")
        print_slow("""
        _.-----....__________....
      :    /    :    .     .    :
      : __/_____:______       . |
    ---:      . :           `  |`-.
      |      `  |    `      |  |   `-----.
      :           :.     .   /`.|
        `-----.__________,'   :\
        :       :          `  | |
        :       |             |/
          `.__,'             / |
            : `-------------'  /
            | `.          _,'  /
            :   `      _,'   .'
              `.___,'  `.___.'   
        """)
    elif result == "bad":
        print_slow("Sorry, you have reached a bad ending. Better luck next time.")
        print_slow("""
          ,----.______ 
         //            \\ 
        ||  ~~~~~  ~~~  ||
        ||  ~~~  ~~~~~  ||
        ||     ______,  || 
        ||  ||  :  ||  ||
        ||  ||  :  ||  || 
        ||  ||__:_||__|| 
        ||  ||======||  ||
        ||  ||  ~~~~~  || 
        ||__||_________|| 
        |______________|
        """)

def main():
    while True:
        print_slow("Welcome to the Mysterious Forest Adventure!")
        print_slow("You find yourself standing at the edge of a mysterious forest.")
        print_slow("You can hear strange noises emanating from within.")
        print_slow("Are you brave enough to enter?")

        brave_choice = make_decision("Do you want to enter the forest?", ["Yes, I'm brave!", "No, it's too scary!"])

        visited_branches = set()

        while True:
            if brave_choice == 1 and "left_path" not in visited_branches:
                print_slow("You cautiously enter the forest.")
                print_slow("After walking for a while, you encounter a fork in the path.")
                direction_choice = make_decision("Which path do you want to take?", ["Left", "Right"])

                if direction_choice == 1:
                    print("You chose the left path and encounter a friendly creature.")
                    print("The creature leads you to a hidden treasure!")
                    ending("good")
                elif direction_choice == 2:
                    print("You chose the right path and encounter a spooky cave.")
                    cave_choice = make_decision("Do you want to enter the cave?", ["Yes, explore it.", "No, continue on the path."])

                    if cave_choice == 1:
                        print("Inside the cave, you find a sleeping dragon.")
                        dragon_choice = make_decision("What do you want to do?", ["Try to sneak past the dragon.", "Wake up the dragon."])

                        if dragon_choice == 1:
                            print_slow("You successfully sneak past the dragon and find a hidden exit.")
                            ending("good")
                        elif dragon_choice == 2:
                            print_slow("The dragon wakes up and chases you out of the cave.")
                            ending("bad")
                    elif cave_choice == 2:
                        print("You decide to continue on the path and avoid the spooky cave.")
                        print("After a while, you find a beautiful meadow with butterflies.")
                        ending("good")

                visited_branches.add("left_path")

            elif brave_choice == 2 and "no_forest" not in visited_branches:
                print_slow("You decide not to enter the forest. Maybe it's for the best.")
                ending("bad")
                visited_branches.add("no_forest")

            replay = input("Do you want to replay? (yes/no): ").lower()

            if replay != "yes":
                break

        print_slow("Thanks for playing!")
        replay = input("Do you want to start a new game? (yes/no): ").lower()
        if replay != "yes":
            break

if __name__ == "__main__":
    main()

