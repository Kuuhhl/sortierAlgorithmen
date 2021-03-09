#include <stdio.h>
#include <stdbool.h>
int main(){
    // array definieren
    int array[] = {1, 4, -18203, -2, 1, 323, 420, 666, 69};
    // laenge des arrays bestimmen
    int laenge = sizeof(array)/sizeof(array[0]);

    // veraendert auf True setzen, um in die while-Schleife zu gelangen
    bool veraendert = true;
    // While Schleife überprüft so lange, bis nichts mehr verändert wird >> wir sind fertig
    while (veraendert == true){
        // Standardwert der Variable auf False
        veraendert = false;
        // Jeden Eintrag in der Liste überprüfen
        for (int index = 0; index < laenge - 1; index++){
            // wird ausgeführt, wenn wir zwei Beträge vertauschen können
            if (array[index] > array[index + 1]){
                // veraendert auf True setzen, um die Schleife weiterzumachen
                veraendert = true;
		// Die Zahlen so vertauschen, dass die kleinere Zahl links hinkommt
		int cache = array[index + 1];
		array[index + 1] = array[index];
		array[index] = cache;
	    }
    	}

    }
    // Das fertige Array ausgeben
    for (int counter = 0; counter < laenge; counter++){
      printf("%d ", array[counter]);
    }
    printf("\n");
    return 0;
}
