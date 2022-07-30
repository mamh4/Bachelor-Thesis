# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 13:29:10 2020

@author: moham
"""
import random






def vars_for_template():#We identify what we have in the html in the return function in "" and the return brackets are curly unlike normal brackets or dict() since the function returns a dictionary.
    value = random.randrange(0,100,1)
    if value < 21:
        supervision = True
    else:
        supervision = False
    return {"coin_toss": random.choice(["Head", "Tail"]), "supervision": supervision} 




x = 2
y = 3
z = 9

def trial(x,y,z):
    if x ==2 and y == 3:
        print("done")
    else:
        print("Not done")
    




class ResultsWaitPage():
    def hi():
        
        def detection():
            value = random.randrange(0,100,1)
            if value < 21:
                detected = True
            else:
                detected = False
            return(detected)
        

        detected = detection()
    
        return(detected)
    
    
    
    
    
class Results():
    def retriever():
        return (ResultsWaitPage.detected)