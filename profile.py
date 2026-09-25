name = input("What's your name? ")

age = 19
main_language = "Python"
field = "Programming and Networking"

skills = [
    "Python",
    "C++",
    "HTML",
    "CSS",
    "JavaScript",
    "SQL",
    "Linux",
    "Git & GitHub",
    "Networking",
    "API",
    "JSON"
]

interests = [
    "Programming",
    "Networking",
    "Linux",
    "Cybersecurity",
    "Gaming",
    "Fitness",
    "Business",
    "Technology"
]


def show_header():
    print()
    print("TMTXCODE")
    print("Programming | Networking | Technology")
    print()


def show_about():
    print()
    print("About")
    print("I'm learning programming, networking, Linux and cybersecurity.")
    print("I learn by building projects and improving step by step.")
    print()


def show_skills():
    print()
    print("Skills")

    for skill in skills:
        print("-", skill)

    print()


def show_interests():
    print()
    print("Interests")

    for interest in interests:
        print("-", interest)

    print()


def show_goals():
    print()
    print("Goals")
    print("- Build useful software")
    print("- Improve programming skills")
    print("- Learn networking and cybersecurity")
    print("- Build and publish real projects")
    print("- Keep learning")

    print()


def show_info():
    print()
    print("Information")
    print("Name:", name)
    print("Age:", age)
    print("Main language:", main_language)
    print("Field:", field)
    print()


show_header()

while True:
    print("1. About")
    print("2. Skills")
    print("3. Interests")
    print("4. Goals")
    print("5. Information")
    print("6. Exit")
    print()

    choice = input("Choose: ").strip()

    if choice == "1":
        show_about()

    elif choice == "2":
        show_skills()

    elif choice == "3":
        show_interests()

    elif choice == "4":
        show_goals()

    elif choice == "5":
        show_info()

    elif choice == "6":
        print()
        print("Goodbye,", name)
        break

    else:
        print()
        print("Invalid choice.")