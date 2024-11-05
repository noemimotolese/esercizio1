datiPioggia = [
    ("Milano", [("gennaio", 10), ("febbraio", 15), ("marzo", "N/D"), ("aprile", 25), ("maggio", "N/D"), ("giugno", 0), ("luglio", 18)]),
    ("Monza", [("gennaio", 32), ("febbraio", "N/D"), ("marzo", 20), ("aprile", 0), ("maggio", 32), ("giugno", 12), ("luglio", 18)])
]

while True:
    nomeCitta=input("inserisci il nome della città: ")
    cittaTrovata=False
    for citta, dati in datiPioggia:
        if nomeCitta in citta:
            cittaTrovata=True
    if cittaTrovata==True:
        break
    if cittaTrovata==False:
        print("città non trovata")


def precipitazioni(nomeCitta):
    somma=0
    conta=0
    meseMax=[]
    meseMin=[]
    max=0
    min=100
    for citta, dati in datiPioggia:
      if citta==nomeCitta:
        for mese, pioggia in dati:
          if pioggia!="N/D":
            somma+=pioggia
            conta+=1
            if pioggia>max:
                  max=pioggia
                  meseMax=[mese]
            elif pioggia==max:
                  meseMax.append(mese)
            if pioggia<min:
                  min=pioggia
                  meseMin=[mese]
            elif pioggia==min:
                  meseMin.append(mese)
    media=somma/conta
    return(media,(max, meseMax),(min,meseMin))
  
print(precipitazioni(nomeCitta))