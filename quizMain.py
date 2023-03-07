class Question:

    def __init__(self):
        self._text = ""
        self._answer = ""

    def setQuestion(self, textQuestion):
        self._text = textQuestion

    def setAnswer(self, correctAnswer):
        self._answer = correctAnswer

    def checkAnswer(self, answer):
        return answer == self._answer

    def display(self):
        print(self._text)

class Choices(Question):

    def __init__(self):
        super().__init__()
        self._choices = []

    def addChoice(self, choice, correctChoice):
        self._choices.append(choice)
        if correctChoice:

            choiceString = str(len(self._choices))
            self.setAnswer(choiceString)

    def display(self):

        super().display()

        for i in range(len(self._choices)):
            choiceDisplay = i + 1
            print("%d: %s" % (choiceDisplay, self._choices[i]))
