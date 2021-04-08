print("Witamy w dziesiejszej lekcji \n Zacznijmy obliczanie twojego kredytu \n Podaj kwotę kredytu :")
'''
TotalCreditAmount = int(input())
print("Nastepnie miesieczna rate :")
Rata = int(input())
TimeToPay = (TotalCreditAmount / Rata) + 1
TimeToPay = int(TimeToPay)
#print(TimeToPay)
LastPart = (TotalCreditAmount - (Rata * (TimeToPay - 1 )))
TimeToPay = str(TimeToPay)
LastPart = str(LastPart)
print("Czas spłaty twojego kredytu nie uwzgledniajac inflacji to %s miesiecy \nKwota Ostaniej raty to\t %s" % (TimeToPay, LastPart)) #Stara szkoła formatowania Tekstu

print("Czas spłaty twojego kredytu nie uwzgledniajac inflacji to {} miesiecy \nKwota Ostaniej raty to\t {}" .format(TimeToPay, LastPart)) #Drugi sposób formatowania Tekstu

print(f'Czas spłaty twojego kredytu nie uwzgledniajac inflacji to {TimeToPay} miesiecy \nKwota Ostaniej raty to\t {LastPart}') #Najnowszy i zalecany sposób
'''
#Zadanie
#Pobieram kwote kredytu
credit_amount=float(input())
#ustalam oprocentowanie

loan_rate=float(input("Podaj RRSO kredytu"))
#kwota raty
print("podaj kwote raty")
rata=float(input())
total_credit_amount = credit_amount * loan_rate

print("Bardzo dobrze, biorac pod uwage inflacje, twoj kredyt bedzie sie rozkladal nastepujaco")
inf1 = 1.592824484
m1 = (1+((inf1 + 3) / 1200) * total_credit_amount - loan_rate)
k1 = total_credit_amount - m1
inf2 = - 0.453509101,
m2 =  (1+((inf2 + 3) / 1200) * m1 - loan_rate)
k2 = total_credit_amount - m2
inf3 = 2.324671717, 
(1+((inf3 + 3) / 1200) * m2 - loan_rate) , total_credit_amount - m3
inf4 , m4 , k4 = 1.261254407, (1+((inf2 + 3) / 1200) * m3 - loan_rate) , total_credit_amount - m4
inf5 , m5 , k5 = 1.782526286, (1+((inf2 + 3) / 1200) * m4 - loan_rate) , total_credit_amount - m5
inf6 , m6 , k6 = 2.329384541, (1+((inf2 + 3) / 1200) * m5 - loan_rate) , total_credit_amount - m6
inf7 , m7 , k7 = 1.502229842, (1+((inf2 + 3) / 1200) * m6 - loan_rate) , total_credit_amount - m7
inf8 , m8 , k8 = 1.782526286, (1+((inf2 + 3) / 1200) * m7 - loan_rate) , total_credit_amount - m8
inf9 , m9 , k9 = 2.328848994, (1+((inf2 + 3) / 1200) * m8 - loan_rate) , total_credit_amount - m9
inf10 , m10 , k10 = 0.616921348, (1+((inf2 + 3) / 1200) * m9 - loan_rate) , total_credit_amount - m10
inf11 , m11 , k11 = 2.352295886, (1+((inf2 + 3) / 1200) * m10 - loan_rate) , total_credit_amount - m11
inf12 , m12 , k12 = 0.337779545, (1+((inf2 + 3) / 1200) * m11 - loan_rate) , total_credit_amount - m12
inf13 , m13 , k13 = 1.577035247, (1+((inf2 + 3) / 1200) * m12 - loan_rate) , total_credit_amount - m13
inf14 , m14 , k14 = - 0.292781443, (1+((inf2 + 3) / 1200) * m13 - loan_rate) , total_credit_amount - m14
inf15 , m15 , k15 = 2.48619659, (1+((inf2 + 3) / 1200) * m14 - loan_rate) , total_credit_amount - m15
inf16 , m16 , k16 = 0.267110318, (1+((inf2 + 3) / 1200) * m15 - loan_rate) , total_credit_amount - m16
inf17 , m17 , k17 = 1.417952672, (1+((inf2 + 3) / 1200) * m16 - loan_rate) , total_credit_amount - m17
inf18 , m18 , k18 = 1.054243267, (1+((inf2 + 3) / 1200) * m17 - loan_rate) , total_credit_amount - m18
inf19 , m19 , k19 = 1.480520104, (1+((inf2 + 3) / 1200) * m18 - loan_rate) , total_credit_amount - m19
inf20 , m20 , k20 = 1.577035247, (1+((inf2 + 3) / 1200) * m19 - loan_rate) , total_credit_amount - m20
inf21 , m21 , k21 = - 0.07742069, (1+((inf2 + 3) / 1200) * m20 - loan_rate) , total_credit_amount - m21
inf22 , m22 , k22 = 1.165733399, (1+((inf2 + 3) / 1200) * m21 - loan_rate) , total_credit_amount - m22
inf23 , m23 , k23 = - 0.404186718, (1+((inf2 + 3) / 1200) * m22 - loan_rate) , total_credit_amount - m23
inf24 , m24 , k24 = 1.499708521, (1+((inf2 + 3) / 1200) * m23 - loan_rate) , total_credit_amount - m24
print (k24)
