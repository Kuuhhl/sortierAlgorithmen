def zahlenVertauschen(index1, index2, liste):
    """
    Returned die Indexe der unterschiedlichen Einträge in den Listen.

    Parameter:
        index1 (list): Das erste zu vertauschende Element
        index2 (list): Das zweite zu vertauschende Element
        liste (list): Die Liste, in der Einträge vertauscht werden sollen.
    Returned:
        liste(list): Neue Liste mit vertauschten Elementen.
    """
    liste = liste.copy()
    zahl1 = liste[index1]
    zahl2 = liste[index2]
    liste[index1] = zahl2
    liste[index2] = zahl1
    return liste


def getDiff(alteListe, neueListe):
    """
    Returned die Indexe der unterschiedlichen Einträge in den Listen.

    Parameter:
        alteListe (list): Die erste Liste
        neueListe (list): Die zweite Liste
    Returned:
        veraendertListe(list): Liste der Indexe der Unterschiede
    """
    veraendertListe = []
    for index in range(len(neueListe)):
        if neueListe[index] != alteListe[index]:
            veraendertListe.append(index)
    return veraendertListe


def printColorizedEntries(liste, indexList):
    """
    Gibt eine farbige Visualisierung der Liste in der Konsole aus.

    Parameter:
        liste (list): Die Liste
        indexList (list): Die Liste der Indexe, die farbig hinterlegt werden sollen.
    Returned:
        None
    """
    liste = liste.copy()
    for index in indexList:
        # Die merkwürdigen Zeichen sind ANSI-Escape-Codes. Sie sind für die farbige
        # Darstellung im Terminal verantwortlich.
        liste[index] = f"\u001b[4m\u001b[1m\u001b[31m{liste[index]}\033[0m"
    print(" | ".join(map(str, liste)))


def main(inputList):
    """
    Sortiert eine Liste an Integern (klein > groß) und zeigt die Ergebnisse in der Konsole an.
    Parameter:
        inputList (list): Die Liste der Integer
    Returned:
        None
    """
    # Start-Liste auf der Konsole ausgeben
    inputString = " | ".join(map(str, inputList))
    print(f"{len(inputString)* '-'}\n{inputString}\n{len(inputString) * '-'}")

    # veraendert auf True setzen, um in die while-Schleife zu gelangen
    veraendert = True
    # While Schleife überprüft so lange, bis nichts mehr verändert wird >> wir sind fertig
    while veraendert == True:
        # Standardwert der Variable auf False
        veraendert = False
        # Jeden Eintrag in der Liste überprüfen
        for index in range(len(inputList) - 1):
            # wird ausgeführt, wenn wir zwei Beträge vertauschen können
            if inputList[index] > inputList[index + 1]:
                # veraendert auf True setzen, um die Schleife weiterzumachen
                veraendert = True
                # Eine Kopie der Einträge machen, um einen Vergleichswert zu haben
                cacheList = inputList.copy()
                # In dieser Funktion vertauschen wir die Zahlen der Liste
                inputList = zahlenVertauschen(index, index + 1, inputList)
                # Die Funktion ist da, um in der Konsole eine farbige
                # Schritt-für-Schritt-Visualisierung zu ermöglichen:
                printColorizedEntries(inputList, getDiff(cacheList, inputList))
    # Das Endergebnis in der Konsole ausgeben
    resultString = " | ".join(map(str, inputList))
    print(f"{len(resultString) * '-'}\n{resultString}\n{len(resultString) * '-'}")


# Hier die Liste einfügen:
inputList = []

main(inputList)
