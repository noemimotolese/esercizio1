tupla_competizioni = (
    ("ChefA", "Piatto1", 8.5, 6),
    ("ChefB", "Piatto2", 7.2, 4),
    ("ChefC", "Piatto3", 9.0, 6),
    ("ChefA", "Piatto4", 7.8, 5),
    ("ChefB", "Piatto5", 8.1, 4),
)

def media_punteggio_competizioni(tupla_competizioni):
    somma=0
    conta=0
    for chef, piatto, punteggio, giudici in tupla_competizioni:
        conta+=1
        somma+=punteggio
    media=round(somma/conta,2)
    return media



def media_punteggio_chef(tupla_competizioni, chefInserito):
    somma=0
    conta=0
    for chef, piatto, punteggio, giudici in tupla_competizioni:
        if chefInserito==chef:
            conta+=1
            somma+=punteggio
    media=round(somma/conta,2)
    return media


def competizione_con_piu_giudici(tupla_competizioni):
    max=0
    chefMax=[]
    piattoMax=[]
    punteggioMax=[]
    for chef, piatto, punteggio, giudici in tupla_competizioni:
        if giudici>max:
            max=giudici
            chefMax=[chef]
            piattoMax=[piatto]
            punteggioMax=[punteggio]
        elif giudici==max:
            chefMax.append(chef)
            piattoMax.append(piatto)
            punteggioMax.append(punteggio)
    return(chefMax, piattoMax, punteggioMax, max)


def competizione_con_meno_giudici(tupla_competizioni):
    min=100
    chefMin=[]
    piattoMin=[]
    punteggioMin=[]
    for chef, piatto, punteggio, giudici in tupla_competizioni:
        if giudici<min:
            min=giudici
            chefMin=[chef]
            piattoMin=[piatto]
            punteggioMin=[punteggio]
        elif giudici==min:
            chefMin.append(chef)
            piattoMin.append(piatto)
            punteggioMin.append(punteggio)
    return(chefMin, piattoMin, punteggioMin, min)


while True:
    print("\n1 - media dei punteggi di tutte le competizioni"
          ,"\n2 - media dei punteggi di un determinato chef"
          ,"\n3 - competizioni con il maggior numero di giudici"
          ,"\n4 - competizioni con il minor numero di giudici"
          ,"\n5 - esci dal programma")
    scelta=int(input("fai la tua scelta: "))
    if scelta==1:
        print("media dei punteggi di tutte le competizioni: ",media_punteggio_competizioni(tupla_competizioni))

    elif scelta==2:
        chefInserito=input("inserire nome dello chef: ")
        chef_trovato=False
        for chef, piatto, punteggio, giudici in tupla_competizioni:
            if chefInserito==chef:
                chef_trovato=True
        if chef_trovato==True:
            print(f"media dei punteggi dello chef {chefInserito}: ",media_punteggio_chef(tupla_competizioni, chefInserito))
        else:
            print("chef non trovato")
        
    elif scelta==3:
        print("competizioni con il maggior numero di giudici: ")
        chefMax, piattoMax, punteggioMax, max=competizione_con_piu_giudici(tupla_competizioni)
        for i in range (len(chefMax)):
            print(f"({chefMax[i]}, {piattoMax[i]}, {punteggioMax[i]}, {max})")
        
    elif scelta==4:
        print("competizioni con il minor numero di giudici: ")
        chefMin, piattoMin, punteggioMin, min=competizione_con_meno_giudici(tupla_competizioni)
        for i in range (len(chefMax)):
            print(f"({chefMin[i]}, {piattoMin[i]}, {punteggioMin[i]}, {min})")

    elif scelta==5:
        print("esci dal programma")
        break

    else:
        print("scelta non valida, riprova")


