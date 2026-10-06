Pret_initial=float(input('Pretul?:'))
Reducere=int(input('Reducere %:'))
Pret_final=Pret_initial*(Reducere/Pret_initial)
print(f'Spre achitare {Pret_final:.2f} lei')
Economie=Pret_initial-Pret_final
print(f'Ai economisit {Economie:.2f} lei')