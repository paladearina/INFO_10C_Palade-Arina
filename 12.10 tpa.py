 n=int(input('Introdu numarul de zile: '))
 ore=n*24
 minute=n*1440
 print(f'Numarul de ore este: {ore}')
 print(f'Numarul de minute este: {minute}')
 
 m1=float(input('Introdu prima masa (kg): '))
 m2=float(input('Introdu a doua masa (kg): '))
 total=m1+m2
 grame=total*1000
 print(f'Masa totala este: {total} kg')
 print(f'Masa totala este: {grame} g')
 
 distanta=float(input('Introdu distanta (km): '))
 consum=float(input('Introdu consumul (l/100km): '))
 combustibil=distanta*consum/100
 print(f'Combustibilul necesar este: {combustibil} l')
 
 n=int(input('Introdu numarul de minute: '))
 ore=n//60
minute=n%60
print(f'Numarul de ore si minute este: {ore} ore si {minute} minute')
