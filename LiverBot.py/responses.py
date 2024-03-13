import random

def handle_response(message):
    p_message = message.lower()

    myGames = ["Portal", "Portal2", "GTAV", "Valorant", "League of Legends",
                "Fallout: New Vegas", "Bioshock", "Mass Effect", "Assasin's Creed",
               "CSGO", "Dead By Daylight", "Terraria", "Dead Space 2", "Mario Kart Tour", 
               "Super Mario Galaxy 2", "Manhunt 2", "Pokemon Platinum", "Tales of Zestria",
               "Forza Horizon 5", "Call of Duty", "Animal Crossing", "Fortnite", "Minecraft",
               "Genshin Impact", "Roblox", "Apex Legends", "Team Fight Tactics"]
    
    lolItems = ["Relicario de los Solari", "Renovador de piedra lunar", "Ecos de Helia",
                "Redencion", "Bendicion de Mikael", "Pebetero Ardiente", "Mandato Imperial", 
                "Baculo de Agua Fluyente", "Corazon de Hielo", "Umbral del Invierno", 
                "Mascara Abisal", "Cituron Cohete Hextech", "Colmillo del Serpiente", 
                "Cadenas de Anatema", "Cetro de Crytsal de Rylai", "Espada de la Penumbra",
                "Vara de las Edades", "Guantelete de Hijo de Hielo", "Egida de Fuego Solar", "Cota de Espinas", "Daga de Statik", 
                "Maldad", "Espada Fantasma de Yoummuu", "Presagio de Randuin", "Enfoque del Horizaonte",
                "Esfera del Amanecer", "Oportunidades", "Desesperacion Eterna", "Bailarin Espectral", "Huracan del Runnan", "Al Filo de la Cordura", 
                "Fauces del Malmortius", "Filo de la Noche", "Fuerza de la Naturaleza",
                "Sierraespada Quimpunk", "Resplandor Vacio", "Criptorretono", "Rukerno Kaenico", "Baculo del Arcangel", "manamune", 
                "Apariencia Espiritual", "Saqueador de Esencias", "Placa del Hombre Muerto", "Descarga Tormentosa",
                "Acompanante de Luden", "Cicloespada Voltaica", "Recordatorio Mortal", "Recuerdos del Lord Dominik", "Guantelete de Sterak", 
                "Cuchilla Oscura", "Placa Hexpermiantal", "Corazon de Acero", "canon de fuego rapido", "Diente de Nashor",
                "Espadafuria de Guinsoo", "Baculo del Vacio", "Cimitarra Mercurial","Terminus", 
                "Impulso Cosmico", "El tormento de Liandry", "Matakrakens", "Arcoescudo Inmortal", "Arco Axiomatico", "Arrogancia",
                "Armadura de Warmog", "Maldicion del Liche", "Velo de la Banshee", "Lanza de Shojin", "Agrietador", "Cielo Desgarrado",
                "El Coleccionista", "Filo de la tormenta", "Espada del Rey Arruinado", "Lumbria", "Danza de la Muerte",
                "Jak'Sho, el Proteico", "Rencor de Serylda", "Reloj de Arena de Zhonya", "Filo del Infinito", "Hidra Voraz", "Hidra Titanica",
                "RompeAvances", "Cuchillas Raudas de Navori", "Hidra Profana", "Fuerza de la Trinidad", "La Sanguinaria", "Sombrero Mortifero de Rabadon"]
    
    myResponses = ["de quien eres?", "recomiendame un juego", "dame un build", "dame un item", "adivina mi color", "tira un dado", "te amo", 
                   "estoy triste", "cara o escudo", "dile a via que se calle", "eres gay?", "que es (tu opcion)", "estas despierto?"]
    
    if p_message == "!manual":
        return myResponses

    if p_message == "liverbot de quien eres?":
        return "Del LiverOil (JH)"
    
    if p_message == "liverbot recomiendame un juego":
        return random.choice(myGames)
    
    if p_message == "liverbot dame un build":        
        botas = ["Botas de rapidez", "Botas Ionicas de Lucidez", "Botas de Movilidad", "Grebas del Berserker", 
                 "Botas del Hechicero", "punteras de Acero Revestidas", "Botas de Mercurio"]
        
        build = random.sample(lolItems,5)
        build.append(random.choice(botas))
        return build

    if p_message == "liverbot dame un item":
        return random.choice(lolItems)

    if "liverbot adivina mi color" in p_message:
        myColors = ["negro", "negro carbon", "negro por dentro", "negro azabache"]
        return random.choice(myColors)
    
    if p_message == "liverbot tira un dado":
        return random.randint(1,6)
    
    if p_message == "liverbot te amo":
        return "No amo zorras, lo siento"
    
    if p_message == "liverbot estoy triste":
        tristResponses = ["Abraza un zapato con suela", "Ya no estes triste", "A ok", "por gei", "Come pasta, te recomiendo penne"]
        return random.choice(tristResponses)
    
    if p_message == "liverbot cara o escudo":
        myNum = random.randint(1,2)
        if myNum == 1:
            return "cara"
        else:
            return "escudo"
        
    if p_message == "liverbot dile a via que se calle":
        return "Via callese"
    
    if p_message == "liverbot eres gay?":
        return "Yugo es el gei"
    
    if "liverbot que es" in p_message:
        queEsRes= ["clasista", "gay", "gay y homofobico", "xenofobo", "racista", "racista y negro"]
        return random.choice(queEsRes)
    
    if p_message == "liverbot estas despierto?":
        return "desafortunadamente si :("
    