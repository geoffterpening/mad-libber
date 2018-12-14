boy_name = ""
adjective = ""
holiday = ""
noun = ""
plural_noun = ""
noun2 = ""
body_part = ""
subject = ""
school = ""
noun3 = ""
adjective2 = ""
noun4 = ""
try_again = ""

while try_again != "n":
    try_again = ""
    print("Welcome to the Mad Libs generator, you absolute mad lad/lass!\n")
    print("Give me the following words, and I'll tell you a story:\n")

    boy_name = input("Boy's name: ")
    adjective = input("Adjective: ")
    holiday = input("Holiday: ")
    noun = input("Noun: ")
    plural_noun = input("Plural Noun: ")
    noun2 = input("Noun: ")
    body_part = input("Body Part: ")
    subject = input("School Subject: ")
    school = input("Name of a School: ")
    noun3 = input("Noun: ")
    adjective2 = input("Adjective: ")
    noun4 = input("Noun: ")

    print('\n\nI hope you enjoy your story!\n-----------------------------')
    print("Girl: Oh, "+boy_name+", why did we have to come to this "+adjective+" old castle for?")
    print("Boy: All the hotels were closed because of "+holiday+".")
    print("Girl: Look at the sign, it says \"The Howard Dracula Holiday "+noun+".\"")
    print("Boy: Here comes the bellboy for our "+plural_noun+".")
    print("Girl: My, he is all bent over and has a big "+noun2+".")
    print("Boy: I think he is my old "+subject+" teacher from "+school+".")
    print("Girl: Watch out! He's throwing a/an "+noun3+" over your head!")
    print("Boy: No, no. He's just being "+adjective2+".")
    print("Girl: Now he\'s dragging you toward a bottomless "+noun4+"!")
    print("Boy: I was right, he is my old teacher. Help!")

    while try_again not in ["y","n"]:
        try_again = input("\n\nDo you want to try again? (y/n): ")
        if try_again == "y":
            ""
        elif try_again =="n":
            break
        else:
            print("\nPlease enter a correct response")


print("Press enter to close")
input()