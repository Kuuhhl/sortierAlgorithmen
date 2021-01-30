# Hier die Liste einfügen:
inputList = [9, 7, 4, 4, 2, 0, -4]


def findMaxNumber(inputList):
    """
    Returned die größte Zahl in der Liste.

    Parameter:
        inputList (list): Die Liste
    Returned:
        maxItem (int): Größte Zahl in der Liste
    """
    maxItem = inputList[0]
    for item in inputList:
        if maxItem < item:
            maxItem = item
    return maxItem


def main(unsortiert):
    """
    Sortiert eine Liste an Integern (klein > groß) und zeigt die Ergebnisse in der Konsole an.
    Parameter:
        inputList (list): Die Liste der Integer
    Returned:
        None
    """
    # Die sortierte Liste initialisieren:
    sortiert = []

    # Die unsortierte Liste ausgeben:
    startString = " | ".join(map(str, unsortiert))
    print(f"{len(startString) * '-'}\n{startString}\n{len(startString) * '-'}")

    # Die größte Zahl an die "sortiert"-Liste
    # anhängen, bis alles sortiert ist:
    while len(unsortiert) > 0:
        # Größte unsortierte Zahl finden:
        maxNumber = findMaxNumber(unsortiert)
        # Die Zahl an den Anfang der sortierten Liste anhängen:
        sortiert.insert(0, maxNumber)
        # Danach diese von der unsortierten Liste entfernen:
        unsortiert.remove(maxNumber)
        # Die sortierte Liste in der Konsole ausgeben:
        print(" | ".join(map(str, sortiert)))

    # Wenn fertig, die sortierte Liste ausgeben:
    resultString = " | ".join(map(str, sortiert))
    print(f"{len(resultString) * '-'}\n{resultString}\n{len(resultString) * '-'}")


main(inputList)
