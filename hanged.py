import os
import random
from hangman_pics import HANGMANPICS, TITLE_HANGMAN, GAME_OVER_PIC

def read_data(): 
    data = []
    with open("./archivos/data.txt", 'r', encoding='utf-8') as f: 
        for item in f: 
            data.append(item[:-1])  
    return data  

def draw_name(cadena, name, letter): 
    temp = [i for i in cadena]
    for index in range(len(name)): 
        if name[index] == letter: 
            temp[index] = name[index]
    return array_to_string(temp)

def array_to_string(array): 
    return "".join([i for i in array])

def run(): 
    names = read_data()
    name = random.choice(names)
    game_over = False 
    cadena = ["_" for i in name]
    letter = ""

    index_pic = -1
    while(not game_over): 
        os.system("clear")
        print(TITLE_HANGMAN)
        print("Adivina la palabra!") 
        previous = array_to_string(cadena)
        cadena = draw_name(cadena, name, letter)
        print(cadena)         

        if cadena == name: 
            game_over = True 
            os.system("clear")
            print("Felicidades, GANASTE!")
            break 
        elif index_pic == len(HANGMANPICS) - 1:
            game_over = True 
            print(GAME_OVER_PIC)
            print(HANGMANPICS[index_pic])
            print("LA PALABRA ERA: " + name)
            break
        if previous == cadena: 
            index_pic += 1
        print(HANGMANPICS[index_pic])
        letter = input("Imgrese una letra: ")  
        
if __name__ == "__main__": 
    run() 
