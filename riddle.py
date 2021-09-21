print("ready to be riddled?")
anyNumber=int(input("choos a number from 1 to 10: "))
if anyNumber==1 :
    riddle= input("you measure my life in hours and I serve you by expiring. I’m quick when I’m thin and slow when I’m fat. The wind is my enemy. what am I? (write it as: a ....)  ")
    if riddle=="a candle" :
        print("well done!")
    else:
        print("oops! incorrect answer ")

    
elif anyNumber==2 :
    riddle= input("I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I? (write it as: a ....) ")
    if riddle=="a map" :
         print("well done!" )
    else:
        print("oops! incorrect answer ")


elif anyNumber==3 :
    riddle= input("what word in the English language does the following: the first two letters signify a male, the first three letters signify a female, the first four letters signify a great, while the entire world signifies a great woman. What is the word? ")
    if riddle=="heroine" :
         print("well done!" )
    else:
        print("oops! incorrect answer ")

        
elif anyNumber==4 :
    riddle= input("what English word has three consecutive double letters? ")
    if riddle=="bookkeeper" :
        print("well done!" )
    else:
        print("oops! incorrect answer ")

elif anyNumber==5 :
    riddle= input("a girl has as many brothers as sisters, but each brother has only half as many brothers as sisters. How many brothers and sisters are there in the family? (write it as: 'number' sisters and 'numer' brothers) ")
    if riddle=="4 sisters and 3 brothers" :
       print("well done!" )
    else:
        print("oops! incorrect answer ")


elif anyNumber==6 :
    riddle= input("what disappears as soon as you say its name? ")
    if riddle=="silence" :
        print("well done!" )
    else:
        print("oops! incorrect answer ")

elif anyNumber==7 :
    riddle= input("what gets wet while drying? (write it as: a ....) ")
    if riddle=="a towel" :
      print("well done!" )
    else:
        print("oops! incorrect answer ")

elif anyNumber==8 :
    riddle= input("this belongs to you, but everyone else uses it. (write it as: your ....) ")
    if riddle=="your name" :
       print("well done!" )
    else:
        print("oops! incorrect answer ")

elif anyNumber==9 :
    riddle= input("which word in the dictionary is always spelled incorrectly? (write the word only) ")
    if riddle=="incorrectly" :
     print("well done!" )
    else:
        print("oops! incorrect answer ")  

elif anyNumber==10 :
    riddle= input("what can you hold in your right hand, but never in your left hand? (write it as: your ....) ")
    if riddle=="your left hand" :
      print("well done!" )
    else:
        print("oops! incorrect answer ")

else:
    print("the number you enter must be from 1 to 10")

print("-------------------")
print("programmed by Anita Moghbel")
