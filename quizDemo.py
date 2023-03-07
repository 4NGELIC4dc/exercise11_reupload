from quizMain import Choices

print("Welcome to the Genshin Impact quiz! Test your knowledge about the game with these few questions!")
playing = input("Do you want to proceed? yes/no: ")
if playing != "yes":
    quit()
print("Okay! Let's get started!")

def main():
    one = Choices()
    one.setQuestion("What is Diluc's last name?")
    one.addChoice("Minci", False)
    one.addChoice("Gunnhildr", False)
    one.addChoice("Ragnvindr", True)
    one.addChoice("Megistus", False)

    two = Choices()
    two.setQuestion("What is the name of Xiao's signature dish?")
    two.addChoice("Sweet Dream", True)
    two.addChoice("Prosperous Peace", False)
    two.addChoice("Woodland Dream", False)
    two.addChoice("No Tomorrow", False)

    three = Choices()
    three.setQuestion("What Egyptian deity is used as inspiration for Cyno's character design?")
    three.addChoice("Bastet", False)
    three.addChoice("Horus", False)
    three.addChoice("Osiris", False)
    three.addChoice("Anubis", True)

    four = Choices()
    four.setQuestion("What kind of Youkai is Yae Miko based on?")
    four.addChoice("Kitsune", True)
    four.addChoice("Tengu", False)
    four.addChoice("Oni", False)
    four.addChoice("Kappa", False)

    five = Choices()
    five.setQuestion("Who among the given names is NOT one of The Five Yakshas of Liyue?")
    five.addChoice("Menogias", False)
    five.addChoice("Inarias", False)
    five.addChoice("Boreas", True)
    five.addChoice("Bonanus", False)

    displayQuestion(one)
    displayQuestion(two)
    displayQuestion(three)
    displayQuestion(four)
    displayQuestion(five)

def displayQuestion(prompt):
    prompt.display()
    response=input("What's your answer? ")
    print(prompt.checkAnswer(response))

main()

print("You have reached the end of the Genshin Impact quiz. Thank you for playing!")
exit = input("Exit? yes/no: ")
if exit !="yes":
    quit()
print("Thank you for playing!")
