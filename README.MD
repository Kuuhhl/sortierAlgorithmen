# Sortier-Algorhithmen
## Pseudocode
### Bubble-Sort
```
SET sorted to False

WHILE array not sorted:
    SET sorted to True

    FOR each item in the array
            IF item smaller than right neighbour THEN
                SWAP item with neighbour
                SET sorted to False
            ENDIF
    ENDFOR
ENDWHILE

RETURN array
```
### Selection-Sort
```
FOR index = 0 to arraylength
    FIND smallest item between current index and end of array
    MOVE the item to the index-th position of the array
ENDFOR

RETURN array
```
### Merge-Sort

```
SPLIT array into an array of arrays with up to 2 items each

FOR EACH array in arrays
    SORT array with Bubblesort

CREATE sortedArray

FOR EACH index = 0 to 1 
    CREATE cacheArray with index-th item of each array
    SORT cacheArray
    ADD cacheArray to sortedArray
ENDFOR

RETURN sortedArray
```
### UnknownNameSort (Improved)
```
REMOVE duplicate values from list
CREATE removedValues list with removed values

CREATE sortedList

WHILE still items in array
    FIND biggest number
    INSERT number to beginning of sortedList
    REMOVE number from list
ENDWHILE

FOR item in removedValues
    FIND index of item in sortedList
    INSERT item next to index
ENDFOR

RETURN sortedList
```
