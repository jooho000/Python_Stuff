from datetime import datetime
import random

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == "ayuda bot":
        return "empieza frases con '?' para privado lo demas se mandara a este canal\n Los frases tu los descubres :)"
    
    if p_message == "quiero patas":
        myNum = random.randint(0,9)
        myURLs = ["https://i.pinimg.com/originals/fa/8c/f3/fa8cf3df68e6c98b0a65eb9b2b57cf9c.jpg", 
                  "https://i.pinimg.com/736x/ff/0f/45/ff0f45d540040251092f427461b5359e.jpg", 
                  "https://i.pinimg.com/474x/74/50/15/745015fa7c4968a4dcb4cc588c2883d5.jpg", 
                  "https://img.freepik.com/free-photo/female-bare-feet-pedicure-concept_144627-42113.jpg",
                  "https://i.pinimg.com/736x/08/bb/9f/08bb9fa4c8d9d816262607720eb4ea73.jpg", 
                  "https://upload.wikimedia.org/wikipedia/commons/b/be/Girl%27s_feet.jpg", 
                  "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Female_soles.jpg/511px-Female_soles.jpg",
                  "https://i.pinimg.com/originals/13/72/5f/13725f8bebd68110fdf282cf931af975.jpg", 
                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJoRm5RMFlLKakWFYGRzMso3ZlerXCxgYW3A&usqp=CAU", 
                  "https://www.shutterstock.com/image-photo/beautiful-womans-bare-feet-against-260nw-2177340751.jpg"]
        
        return myURLs[myNum]
    
    if p_message == "que hora es?":
        now = datetime.now()
        timeString = now.strftime("%H:%M")
        return timeString

    if p_message == "vendes patas?":
        return "si"
    
    if p_message == "cuanto valen?":
        return "Es gratis!"
    
    if "quien es el que vende patas?" in p_message:
        return "La via"
    
    if "quien es el mejor en" in p_message:
        return "el Liver"
    
    if p_message == "despierta":
        return "DESPIERTA VIA"
    
    if p_message == "cual es el mejor duo?":
        return "El Duo de Via Oil y Liver Oil"
    
    if p_message == "para que es este server?":
        return "Para flamear :)"
    
    return ""
