#include <stdio.h>
int main(){
    int liste[] = {1, 45, 0, -1, 69, 420, 0, 9999, 849712, -4};
    int length = sizeof(liste)/sizeof(liste[0]);
    
    for (int counter = 0; counter < length; counter++) {
        // find smallest indice
        int smallestPosition = counter;
        for (int counter2 = counter; counter2 < length; counter2++){
            if (liste[counter2] < liste[smallestPosition]){
                smallestPosition = counter2;
            }
        }
        // swap smallest indice to the beginning
        int cache = liste[counter];
        liste[counter] = liste[smallestPosition];
        liste[smallestPosition] = cache;
    }
    for (int counter = 0; counter < length; counter++){
      printf("%d ", liste[counter]);
    }
    printf("\n");
    return 0;
}
