from art import logoHigherLower, logoVersus, logoYouLose
from gameData import data
from fileOperations import readFile, writeFile
from validationFunctions import inputValidation, validateInteger


def chooseDictionary():
    """Returns a dictionary choosed randomly and remove the element from the list data."""
    from random import randint
    
    try:
        lenghtData=len(data)
        index=randint(0,lenghtData)
        dictionary=data.pop(index)
    except IndexError:
        print(f"IndexError: list index out of range. The valid range is 0 to {lenghtData}")
    else:
        return dictionary
    



def newGame():
    score=0
    gameOver=False
    fileName="highScore.txt"
    highScore=validateInteger(readFile(fileName))
    timeUsed=0
    #print(type(highScore))
    optionA = chooseDictionary()

    while not gameOver and len(data)>0:
        optionB = chooseDictionary()
        print(logoHigherLower)
        if score > 0:
             print(f"Você está certo! Pontuação actual: {score}")
        print(f"Compare A: {optionA['name']}  , {optionA['description']}, de {optionA['country']}, que tem {optionA['followers']:,} seguidores")
        print(logoVersus)
        print(f"Contra B: {optionB['name']}  , {optionB['description']}, de {optionB['country']}")

        userChoose=inputValidation("Quem tem mais seguidores? Digite 'A' ou 'B' : " , ['A','B'])
        print("\n"*20)
        #See who has more followers A or B
        isOptionABigger=False
        if optionA['followers'] > optionB['followers']:
                isOptionABigger=True

        if userChoose== "a" and isOptionABigger:
            score+=1
            timeUsed+=1
            if timeUsed> 2:
                 timeUsed=0
                 optionA=optionB
        elif userChoose =="b" and not isOptionABigger:
            score +=1
            optionA=optionB
        else:
            print(logoYouLose)
            print(f"Desculpe, está errado. Pontuação final: {score}\nO seu recorde é: {highScore}")
            gameOver=True

        if score> highScore:
                highScore=score
                writeFile(fileName,f"{highScore}") 



