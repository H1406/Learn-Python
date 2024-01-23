from random import random

keywords = ["cat","dog","mouse","elephant"]
ans = keywords[int(random()*(len(keywords)-1))]
blank = "_" * len(ans)
is_Full = False
try_Times = 5

def take_Guess(blank, try_Times, is_Full):
    #if(is_Full):return blank
    #if(try_Times==0):return 0
    guess= input()
    index = ans.find(guess)
    if(index!=-1):
        position= ans.index(guess)
        temp = blank[:position]+ guess + blank[position+1:]
        blank = temp
        print(blank)
    else:
        try_Times = try_Times - 1
        print("Try another one")
    if(blank == ans):
        is_Full = True
        print("Congrats! The whole ans is :" + ans)
    return blank
while((try_Times!=0)or(is_Full!= True)):
    take_Guess(blank, try_Times, is_Full)
    blank = take_Guess(blank, try_Times, is_Full)
    

   
    