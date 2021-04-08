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
#Homework task LOAN PERCENTAGES
#RECEIVE OF LOAN AMOUNT

credit_amount=float(input("Podaj kwote otrzymana od banku w ramach kredytu"))

#SET LOAN RATE

loan_rate=float(input("Podaj RRSO kredytu : "))

#AMOUNT EACH MONTH USER HAVE TO PAY

rata=float(input("Podaj kwote miesiecznej raty : "))
#Total amount that user will pay to bank
total_credit_amount = credit_amount * loan_rate

#Printing summary for next 24 months of credit 
print("Bardzo dobrze, biorac pod uwage inflacje, twoj kredyt bedzie sie rozkladal nastepujaco")
# value inf - value that we received 
inf1 = 1.592824484
# value m - Amount left to pay
m1 = (1+((inf1 + 3) / 1200) * total_credit_amount - loan_rate)
# Value k - Diffrence beetwen current and previous month.
k1 = total_credit_amount - m1
inf2 = - 0.453509101,
m2 =  (1+((inf2 + 3) / 1200) * m1 - loan_rate)
k2 = total_credit_amount - m2
inf3 = 2.324671717, 
m3 = (1+((inf3 + 3) / 1200) * m2 - loan_rate)
k3 = total_credit_amount - m3
inf4 = 1.261254407  
m4 = (1+((inf2 + 3) / 1200) * m3 - loan_rate)
k4 = total_credit_amount - m4
inf5 = 1.782526286
m5 = (1+((inf2 + 3) / 1200) * m4 - loan_rate)
k5 = total_credit_amount - m5
inf6 = 2.329384541
m6 = (1+((inf2 + 3) / 1200) * m5 - loan_rate)
k6 = total_credit_amount - m6
inf7 = 1.502229842
m7 = (1+((inf2 + 3) / 1200) * m6 - loan_rate)
k7 = total_credit_amount - m7
inf8  = 1.782526286
m8 = (1+((inf2 + 3) / 1200) * m7 - loan_rate)
k8 = total_credit_amount - m8
inf9 = 2.328848994
m9 = (1+((inf2 + 3) / 1200) * m8 - loan_rate)
k9 = total_credit_amount - m9
inf10  = 0.616921348
m10 = (1+((inf2 + 3) / 1200) * m9 - loan_rate)
k10 = total_credit_amount - m10
inf11  = 2.352295886
m11 = (1+((inf2 + 3) / 1200) * m10 - loan_rate)
k11 = total_credit_amount - m11
inf12 = 0.337779545
m12 = (1+((inf2 + 3) / 1200) * m11 - loan_rate)
k12 = total_credit_amount - m12
inf13 = 1.577035247
m13 = (1+((inf2 + 3) / 1200) * m12 - loan_rate)
k13 = total_credit_amount - m13
inf14 = - 0.292781443
m14 = (1+((inf2 + 3) / 1200) * m13 - loan_rate)
k14 = total_credit_amount - m14
inf15 = 2.48619659
m15 = (1+((inf2 + 3) / 1200) * m14 - loan_rate)
k15 = total_credit_amount - m15
inf16 = 0.267110318
m16 = (1+((inf2 + 3) / 1200) * m15 - loan_rate)
k16 = total_credit_amount - m16
inf17 = 1.417952672
m17 = (1+((inf2 + 3) / 1200) * m16 - loan_rate)
k17 = total_credit_amount - m17
inf18 = 1.054243267
m18 = (1+((inf2 + 3) / 1200) * m17 - loan_rate)
k18 = total_credit_amount - m18
inf19 = 1.480520104
m19 = (1+((inf2 + 3) / 1200) * m18 - loan_rate)
k19 = total_credit_amount - m19
inf20 = 1.577035247
m20 = (1+((inf2 + 3) / 1200) * m19 - loan_rate)
k20 = total_credit_amount - m20
inf21 = - 0.07742069
m21 = (1+((inf2 + 3) / 1200) * m20 - loan_rate)
k21 = total_credit_amount - m21
inf22 = 1.165733399
m22 = (1+((inf2 + 3) / 1200) * m21 - loan_rate)
k22 = total_credit_amount - m22
inf23 = - 0.404186718
m23 = (1+((inf2 + 3) / 1200) * m22 - loan_rate)
k23 = total_credit_amount - m23
inf24 = 1.499708521
m24 = (1+((inf2 + 3) / 1200) * m23 - loan_rate)
k24 = total_credit_amount - m24
print (k24)
