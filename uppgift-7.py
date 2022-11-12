#test
n=0
lon = 0
sum_lon = 0
antal = int(input(" Antal dagar = "))
while n <= antal-1 :
   lon = 2**n
   sum_lon+= lon
   #print (n, lon, sum_lon)
   if (sum_lon >= 100000000):
        print(" en miljon", n, " dagar" ) 
   n+=1 
print (" summa pengar = ", sum_lon) 