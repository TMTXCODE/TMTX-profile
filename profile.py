name = input("What's your name? ")

print()
print("Welcome,", name)
print()

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
    "Git",
    "Networking",
    "API",
    "JSON"
]

print("TMTXCODE")
print("Age:", age)
print("Main language:", main_language)
print("Field:", field)

print()
print("Things I'm learning:")

for skill in skills:
    print("-", skill)

print()

if name == "TMTXCODE":
    print("Welcome back, TMTXCODE.")
else:
    print("Nice to meet you,", name)
choice = input("What do you want to see? ")

if choice == "skills":
    print()
    print("Skills:")

    for skill in skills:
        print("-", skill)

elif choice == "about":
    print()
    print("About:")
    print("I'm learning programming, networking, Linux and cybersecurity.")

elif choice == "goals":
    print()
    print("Goals:")
    print("Learn more, build real projects and keep improving.")

else:
    print()
    print("Command not found.")