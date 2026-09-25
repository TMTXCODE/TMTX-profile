# TMTXCODE Profile

name = input("What's your name? / اسمت چیه؟ ")

print()
print("1. فارسی")
print("2. English")

language = input("انتخاب / Choose: ").strip()

if language == "1":
    fa = True
else:
    fa = False


age = 19
main_language = "Python"
field_fa = "برنامه‌نویسی و شبکه"
field_en = "Programming and Networking"

skills_fa = [
    "Python",
    "C++",
    "HTML",
    "CSS",
    "JavaScript",
    "SQL",
    "Linux",
    "Git و GitHub",
    "Networking",
    "API",
    "JSON"
]

skills_en = [
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

interests_fa = [
    "برنامه‌نویسی",
    "شبکه",
    "لینوکس",
    "امنیت سایبری",
    "تکنولوژی",
    "گیم",
    "باشگاه",
    "بیزینس",
    "پول"
]

interests_en = [
    "Programming",
    "Networking",
    "Linux",
    "Cybersecurity",
    "Technology",
    "Gaming",
    "Fitness",
    "Business",
    "Money"
]


def show_header():
    print()
    print("TMTXCODE")
    print()


def show_about():
    print()

    if fa:
        print("درباره من")
        print("کلاً با برنامه‌نویسی، شبکه، لینوکس و امنیت سایبری حال می‌کنم.")
        print("هرچی بلد نباشم، یادش می‌گیرم و سعی می‌کنم باهاش یه چیزی بسازم.")
        print("هنوز اول راهم، ولی قرار نیست همون‌جا بمونم.")
    else:
        print("About")
        print("I'm into programming, networking, Linux and cybersecurity.")
        print("If I don't know something, I learn it and try to build something with it.")
        print("I'm still at the beginning, but I'm not planning to stay there.")

    print()


def show_skills():
    print()

    if fa:
        print("چیزایی که دارم یاد می‌گیرم:")

        for skill in skills_fa:
            print("-", skill)
    else:
        print("Things I'm learning:")

        for skill in skills_en:
            print("-", skill)

    print()


def show_interests():
    print()

    if fa:
        print("به چی علاقه دارم؟")

        for interest in interests_fa:
            print("-", interest)
    else:
        print("Interests:")

        for interest in interests_en:
            print("-", interest)

    print()


def show_goals():
    print()

    if fa:
        print("هدف‌ها")
        print("- ساختن نرم‌افزارهای کاربردی")
        print("- قوی‌تر شدن توی برنامه‌نویسی")
        print("- یادگیری شبکه و امنیت")
        print("- ساخت و انتشار پروژه‌های واقعی")
        print("- ادامه دادن حتی وقتی سخت می‌شه")
    else:
        print("Goals")
        print("- Build useful software")
        print("- Improve programming skills")
        print("- Learn networking and cybersecurity")
        print("- Build and publish real projects")
        print("- Keep going when things get difficult")

    print()


def show_info():
    print()

    if fa:
        print("اطلاعات")
        print("نام:", name)
        print("سن:", age)
        print("زبان اصلی:", main_language)
        print("رشته:", field_fa)
    else:
        print("Information")
        print("Name:", name)
        print("Age:", age)
        print("Main language:", main_language)
        print("Field:", field_en)

    print()


def show_menu():
    print()

    if fa:
        print("TMTXCODE")
        print()
        print("1. درباره من")
        print("2. مهارت‌ها")
        print("3. علاقه‌مندی‌ها")
        print("4. هدف‌ها")
        print("5. اطلاعات")
        print("6. تغییر زبان")
        print("7. خروج")
    else:
        print("TMTXCODE")
        print()
        print("1. About")
        print("2. Skills")
        print("3. Interests")
        print("4. Goals")
        print("5. Information")
        print("6. Change language")
        print("7. Exit")


show_header()

while True:

    show_menu()

    if fa:
        choice = input("\nانتخاب: ").strip()
    else:
        choice = input("\nChoose: ").strip()

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

        if fa:
            print("\n1. فارسی")
            print("2. English")
            new_language = input("زبان جدید: ").strip()
        else:
            print("\n1. فارسی")
            print("2. English")
            new_language = input("New language: ").strip()

        if new_language == "1":
            fa = True
        elif new_language == "2":
            fa = False

    elif choice == "7":

        if fa:
            print("\nفعلاً داش، بعداً برگرد.")
        else:
            print("\nSee you later.")

        break

    else:

        if fa:
            print("\nاین گزینه وجود نداره.")
        else:
            print("\nInvalid choice.")