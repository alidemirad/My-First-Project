#[16,21,11,8,12,22] -> Merge Sort

#Yukarıdaki dizinin sort türüne göre aşamalarını yazınız.
#Big-O gösterimini yazınız.


[16,21,11,8,12,22]
  [16,21,11]      [8,12,22]
 [16] [21,11]    [8] [12,22]
[16] [21] [11]  [8] [12] [22]
 [16] [11,21]    [8,12] [22]
  [11,16,21]       [8,12,22]
     [8,11,12,16,21,22]

# Tüm elemanlar tek bir parantez içine alındıktan sonra her aşamada O(n) işlemini yapıyoruz ve bu işlemi 2**x = n defa
#yapıyoruz buradan da O(nlogn) gelir.