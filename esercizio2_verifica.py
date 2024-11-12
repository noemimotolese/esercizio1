tupla_produzione_agricola = (
    ("Toscana", [
        ("gennaio", ("grano", 1200)),
        ("gennaio", ("mais", 900)),
        ("febbraio", ("grano", 1100)),
        ("marzo", ("grano", 800)),
        ("marzo", ("mais", 900)),
        ("febbraio", ("grano", 1000)),
        ("marzo", ("grano", 950))
    ]),
    ("Lombardia", [
        ("gennaio", ("grano", 1300)),
        ("gennaio", ("mais", 850)),
        ("marzo", ("grano", 1250)),
        ("febbraio", ("mais", 920)),
        ("gennaio", ("grano", 1300)),
        ("febbraio", ("grano", 1250)),
        ("marzo", ("mais", 980)),
    ]),
    ("Umbria", [
        ("gennaio", ("grano", 1200)),
        ("gennaio", ("mais", 870)),
        ("marzo", ("mais", 1500)),
        ("febbraio", ("mais", 920)),
        ("gennaio", ("grano", 800)),
        ("febbraio", ("grano", 1100)),
        ("marzo", ("mais", 910)),
    ]),
)

while True:
    nomeRegione=input("inserire nome della regione: ")
    nomeColtura=input("inserire nome della coltura: ")
    regione_trovata=False
    coltura_trovata=False
    for regione, dati in tupla_produzione_agricola:
        for (mese, (coltura, produzione)) in dati:
            if nomeRegione==regione:
                    regione_trovata=True
            if nomeColtura==coltura:
                    coltura_trovata=True
    if regione_trovata==True and coltura_trovata==True:
        break
    else:
        print("regione o coltura non trovate")

def analizza_produzione_agricola(tupla_produzione_agricola, nomeRegione, nomeColtura):
    somma=0
    conta=0
    max_produzione=0
    mese_max=[]
    for regione, dati in tupla_produzione_agricola:
        for (mese, (coltura, produzione)) in dati:
            if nomeRegione==regione and nomeColtura==coltura:
                conta+=1
                somma+=produzione
                if produzione>max_produzione:
                    max_produzione=produzione
                    mese_max=[mese]
                elif produzione==max_produzione:
                    mese_max.append(mese)
    media=round(somma/conta,2)
    return (media,(max_produzione, mese_max))
print(f"risultato per {nomeRegione} e {nomeColtura}" ,analizza_produzione_agricola(tupla_produzione_agricola, nomeRegione, nomeColtura))