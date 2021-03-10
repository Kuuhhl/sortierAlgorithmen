private void mergeSort(int[] array) {
        // Größe der geteilten Arrays 
        int chunk = 2; 
        // Teile Array:
        for(int i=0;i<array.length;i+=chunk){
            Arrays.copyOfRange(array, i, Math.min(original.length,i+chunk));
        }


        // sort all segments individually
        for (int index = 0; index < array.length;index++){
            array[index] = bubblesort(array[index]);
        }

        // create array of indices to sort
        int [] indice;
        int [] indices;
        for(int index=0;index<array[array.length].length;index++){
            for(index2 = 0; index2<array[index][index2].length;index2++){
                // Add n-th indice to array (and skip if it is not found)
                try{
                    indice += array[index][index2];
                }
                catch(Exception e){
                    continue;
                }
            }
            indices += indice;
            indice = null;
        }
        int [] sorted;
        BubbleSorter bs = new BubbleSorter();
        for(index = 0; index < indices[index].length; index++){
            sorted += bs.sortiere(indices[index]);
        }
        array = sorted;
    }
}
