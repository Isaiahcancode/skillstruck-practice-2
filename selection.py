arr = []
function SelectionSort(list)

   for all elements (i) in list:
      minimum = i
      for remaining elements (j) in list:
         if list[j] < list[minimum]
            minimum = j
         end if
      end for
      if the index of minimum != i
         swap list[minimum] and list[i]
      end if
   end for
   return list
end SelectionSort