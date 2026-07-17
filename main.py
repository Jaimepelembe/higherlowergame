from higherLower import newGame
from validationFunctions import inputValidation

gameOver=False

while not gameOver:
    #Start a new game
    newGame()

    userChoose=inputValidation("Quer jogar novamente? Pressione 'S' ou 'N' : " , ['S','N'])
    if userChoose =="n":
        gameOver=True