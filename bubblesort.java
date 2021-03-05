public static int[] zahlenVertauschen(int [] array, int index1, int index2){
	cachedIndex1 = array[index1];
	array[index1] = array[index2];
	array[index2] = cachedIndex1;
	return array;
}
public static int[] bubblesort(int [] inputArray){
    // veraendert auf True setzen, um in die while-Schleife zu gelangen
    boolean veraendert = true;
    // While Schleife überprüft so lange, bis nichts mehr verändert wird >> wir sind fertig
    while (veraendert == true){
        // Standardwert der Variable auf False
        veraendert = false
        // Jeden Eintrag in der Liste überprüfen
        for (int index = 0; index < len(inputArray) - 1; index++){
            // wird ausgeführt, wenn wir zwei Beträge vertauschen können
            if (inputArray[index] > inputArray[index + 1]){
                // veraendert auf True setzen, um die Schleife weiterzumachen
                veraendert = true;
                // In dieser Funktion vertauschen wir die Zahlen der Liste
                inputArray = zahlenVertauschen(zahlenVertauschen, index, index + 1);
	    }
    	}

    }
    return inputArray;
}
