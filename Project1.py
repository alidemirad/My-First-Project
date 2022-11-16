#Soru:[22,27,16,2,18,6] -> Insertion Sort

#Yukarı verilen dizinin sort türüne göre aşamalarını yazınız.

#Big-O gösterimini yazınız.

#Time Complexity: Dizi sıralandıktan sonra 18 sayısı aşağıdaki case'lerden hangisinin kapsamına girer? Yazınız

#1. Average case: Aradığımız sayının ortada olması
#2. Worst case: Aradığımız sayının sonda olması
#3. Best case: Aradığımız sayının dizinin en başında olması.

[22,27,16,2,18,6]
[22 | 27,16,2,18,6]
[22,27 | 16,2,18,6]
[16,22,27 | 2,18,6]
[2,16,22,27 | 18,6]
[2,16,18,22,27 | 6]
[2,6,16,18,22,27 |]

#Algoritmanın ilk adımında n karşılaştırma yapıyor. İlk sayıyı seçtiği zaman karşılaştıracağı sayı n - 1 oluyor ve bu
#1 ' e kadar devam ediyor. n ' den 1 ' e kadarki sayıların toplamı (n(n-1))/2 olduğundan Big-O = n**2 olur.


#Dizi sırasına göre 18 sayısı 4. indekste olduğundan Average Case'e girer.