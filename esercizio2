tupla_vendite = (
                (("RepartoA","info"),("Prodotto A", ("contanti",1000))),
                (("RepartoA","info"),("Prodotto B", ("carta di credito",1500))),
                (("RepartoA","tele"),("Prodotto C", ("carta di credito",1200))),
                (("RepartoA","tpsi"),("Prodotto D", ("contanti",200))),
                (("RepartoA","tele"),("Prodotto E", ("contanti",800))),
                (("RepartoA","info"),("Prodotto F", ("N/D",200))),
                (("RepartoB","tele"),("Prodotto A", ("contanti",1500))),
                (("RepartoB","tpsi"),("Prodotto B", ("carta di credito",900)))
                )
def media_globale(tupla_vendite):
    conta=0
    somma=0
    for reparto, prodotto in tupla_vendite:
        metodo, importo=prodotto[1]
        conta+=1
        somma+=importo
    media=somma/conta
    return media


def media(tupla_vendite, categoriaInserita, metodoInserito):
    conta=0
    somma=0
    for (reparto, categoria), (prodotto, (metodo, importo)) in tupla_vendite:
        if categoria==categoriaInserita and metodo==metodoInserito:
            conta+=1
            somma+=importo
    media=somma/conta
    return media


def venditaMax(tupla_vendite):
    vendita_max=0
    prodotto_max=[]
    for (reparto, categoria), (prodotto, (metodo, importo)) in tupla_vendite:
        if importo>vendita_max:
            vendita_max=importo
            prodotto_max=[prodotto]
        elif importo==vendita_max:
            prodotto_max.append(prodotto)
    return (vendita_max, (prodotto_max))


def venditaMin(tupla_vendite):
    vendita_min=500000
    prodotto_min=[]
    for (reparto, categoria), (prodotto, (metodo, importo)) in tupla_vendite:
        if reparto=="RepartoA":
            if importo<vendita_min:
                vendita_min=importo
                prodotto_min=[prodotto]
            elif importo==vendita_min:
                prodotto_min.append(prodotto)
    return(vendita_min, (prodotto_min))


while True:
    print("\nMenu di scelta:")
    print("1. calcola la media globale delle vendite")
    print("2. calcola la media delle vendite per categoria e metodo di pagamento")
    print("3. trova la vendita massima")
    print("4. trova la vendita minima nel RepartoA")
    print("5. esci")

    scelta = input("scegli un'opzione: ")

    if scelta == '1':
        print("media globale delle vendite:", media_globale(tupla_vendite))

    elif scelta == '2':
        categoriaInserita = input("Inserisci una categoria: ")
        metodoInserito = input("Inserisci metodo di pagamento: ")
        categoria_trovata = False
        metodo_trovato = False
        for (reparto, categoria), (prodotto, (metodo, importo)) in tupla_vendite:
            if categoriaInserita == categoria:
                categoria_trovata = True
            if metodoInserito == metodo:
                metodo_trovato = True
        if categoria_trovata and metodo_trovato:
            print("media delle vendite per categoria e metodo di pagamento:", media(tupla_vendite, categoriaInserita, metodoInserito))
        else:
            print("categoria o metodo di pagamento non trovato")

    elif scelta == '3':
        max_vendita, prodotti_max = venditaMax(tupla_vendite)
        print((max_vendita, (prodotti_max)))

    elif scelta == '4':
        min_vendita, prodotti_min = venditaMin(tupla_vendite)
        print("vendita minima nel RepartoA:", (min_vendita, (prodotti_min)))

    elif scelta == '5':
        print("uscita dal programma.")
        break

    else:
        print("scelta non valida. Riprova.")
