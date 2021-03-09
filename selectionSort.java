public static void main(int [] array){
    /**
    * Takes an array of integers and sorts it.
    * @param array The array to sort.
    */
    for (int counter = 0; counter < array.length; counter++) {
        /* find smallest indice.
        * using a separate loop so that we leave out 
        * the already sorted values
        */
        int smallestPosition = counter;
        for (int counter2 = counter; counter2 < array.length; counter2++){
            if (array[counter2] < array[smallestPosition]){
                smallestPosition = counter2;
            }
        }
        // swap smallest indice to the end of the sorted values
        int cache = liste[counter];
        liste[counter] = liste[smallestPosition];
        liste[smallestPosition] = cache;
    }
}
