<<<<<<< HEAD
'''print("Witamy w dziesiejszej lekcji \n Zacznijmy obliczanie twojego kredytu \n Podaj kwotę kredytu :")

=======
print("Witamy w dziesiejszej lekcji \n Zacznijmy obliczanie twojego kredytu \n ")
'''
>>>>>>> c0436698c46fc211434ed3e6bbca440c1480a69b
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
<<<<<<< HEAD

'''
#Zadanie
#Pobieram kwote kredytu
credit_amount=float(input())
#ustalam oprocentowanie
=======
#Homework task LOAN PERCENTAGES
#RECEIVE OF LOAN AMOUNT
>>>>>>> c0436698c46fc211434ed3e6bbca440c1480a69b

credit_amount = float(input("Podaj kwote otrzymana od banku w ramach kredytu : \n"))

#SET LOAN RATE
loan_rate = float(input("Podaj RRSO kredytu : \n"))

#AMOUNT EACH MONTH USER HAVE TO PAY

rata = float(input("Podaj kwote miesiecznej raty : \n"))
#Total amount that user will pay to bank
total_credit_amount = credit_amount * (1 + ( loan_rate / 100) * 2)

#Preparing to print out credit summary for next 24 month;s
# value inf - value that we received 
inf1 = 1.592824484
# value m - Amount left to pay
m1 = (1 + ((inf1 + 3) / 1200)) * total_credit_amount - rata
# Value k - Diffrence beetwen current and previous month.
k1 = total_credit_amount - m1
inf2 = - 0.453509101
m2 =  (1+((inf2 + 3) / 1200)) * m1 - rata
k2 = total_credit_amount - m2
<<<<<<< HEAD
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

'''

#Zajęcia z pętli
'''
age = 25
if age >= 18:
    print("osoba pelnoletnia")
'''
price = 0
person_age = input("Podaj wiek: ")
# age < 5: 0, age >= 5 and age <= 17: 20, age >= 18:30
if age <5:
    price = 0
print(price)

=======
inf3 = 2.324671717 
m3 = (1+((inf3 + 3) / 1200)) * m2 - rata
k3 = total_credit_amount - m3
inf4 = 1.261254407  
m4 = (1+((inf2 + 3) / 1200)) * m3 - rata
k4 = total_credit_amount - m4
inf5 = 1.782526286
m5 = (1+((inf2 + 3) / 1200)) * m4 - rata
k5 = total_credit_amount - m5
inf6 = 2.329384541
m6 = (1+((inf2 + 3) / 1200)) * m5 - rata
k6 = total_credit_amount - m6
inf7 = 1.502229842
m7 = (1+((inf2 + 3) / 1200)) * m6 - rata
k7 = total_credit_amount - m7
inf8  = 1.782526286
m8 = (1+((inf2 + 3) / 1200)) * m7 - rata
k8 = total_credit_amount - m8
inf9 = 2.328848994
m9 = (1+((inf2 + 3) / 1200)) * m8 - rata
k9 = total_credit_amount - m9
inf10  = 0.616921348
m10 = (1+((inf2 + 3) / 1200)) * m9 - rata
k10 = total_credit_amount - m10
inf11  = 2.352295886
m11 = (1+((inf2 + 3) / 1200)) * m10 - rata
k11 = total_credit_amount - m11
inf12 = 0.337779545
m12 = (1+((inf2 + 3) / 1200)) * m11 - rata
k12 = total_credit_amount - m12
inf13 = 1.577035247
m13 = (1+((inf2 + 3) / 1200)) * m12 - rata
k13 = total_credit_amount - m13
inf14 = - 0.292781443
m14 = (1+((inf2 + 3) / 1200)) * m13 - rata
k14 = total_credit_amount - m14
inf15 = 2.48619659
m15 = (1+((inf2 + 3) / 1200)) * m14 - rata
k15 = total_credit_amount - m15
inf16 = 0.267110318
m16 = (1+((inf2 + 3) / 1200)) * m15 - rata
k16 = total_credit_amount - m16
inf17 = 1.417952672
m17 = (1+((inf2 + 3) / 1200)) * m16 - rata
k17 = total_credit_amount - m17
inf18 = 1.054243267
m18 = (1+((inf2 + 3) / 1200)) * m17 - rata
k18 = total_credit_amount - m18
inf19 = 1.480520104
m19 = (1+((inf2 + 3) / 1200)) * m18 - rata
k19 = total_credit_amount - m19
inf20 = 1.577035247
m20 = (1+((inf2 + 3) / 1200)) * m19 - rata
k20 = total_credit_amount - m20
inf21 = - 0.07742069
m21 = (1+((inf2 + 3) / 1200)) * m20 - rata
k21 = total_credit_amount - m21
inf22 = 1.165733399
m22 = (1+((inf2 + 3) / 1200)) * m21 - rata
k22 = total_credit_amount - m22
inf23 = - 0.404186718
m23 = (1+((inf2 + 3) / 1200)) * m22 - rata
k23 = total_credit_amount - m23
inf24 = 1.499708521
m24 = (1+((inf2 + 3) / 1200)) * m23 - rata
k24 = total_credit_amount - m24

#Printing summary for next 24 months of credit 
print(total_credit_amount)
print("Bardzo dobrze, biorac pod uwage inflacje, twoj kredyt bedzie sie rozkladal nastepujaco")
print(f'W 1 miesiacu splacania kredytu pozostalo do splaty {m1} \n To mniej o {k1} niz w poprzednim miesiacu\n')
print(f'W 2 miesiacu splacania kredytu pozostalo do splaty {m2} \n To mniej o {k2} niz w poprzednim miesiacu\n') 
print(f'W 3 miesiacu splacania kredytu pozostalo do splaty {m3} \n To mniej o {k3} niz w poprzednim miesiacu\n')
print(f'W 4 miesiacu splacania kredytu pozostalo do splaty {m4} \n To mniej o {k4} niz w poprzednim miesiacu\n')
print(f'W 5 miesiacu splacania kredytu pozostalo do splaty {m5} \n To mniej o {k5} niz w poprzednim miesiacu\n')
print(f'W 6 miesiacu splacania kredytu pozostalo do splaty {m6} \n To mniej o {k6} niz w poprzednim miesiacu\n')
print(f'W 7 miesiacu splacania kredytu pozostalo do splaty {m7} \n To mniej o {k7} niz w poprzednim miesiacu\n')
print(f'W 8 miesiacu splacania kredytu pozostalo do splaty {m8} \n To mniej o {k8} niz w poprzednim miesiacu\n')
print(f'W 9 miesiacu splacania kredytu pozostalo do splaty {m9} \n To mniej o {k9} niz w poprzednim miesiacu\n')
print(f'W 10 miesiacu splacania kredytu pozostalo do splaty {m10} \n To mniej o {k10} niz w poprzednim miesiacu\n')
print(f'W 11 miesiacu splacania kredytu pozostalo do splaty {m11} \n To mniej o {k11} niz w poprzednim miesiacu\n')
print(f'W 12 miesiacu splacania kredytu pozostalo do splaty {m12} \n To mniej o {k12} niz w poprzednim miesiacu\n')
print(f'W 13 miesiacu splacania kredytu pozostalo do splaty {m13} \n To mniej o {k13} niz w poprzednim miesiacu\n')
print(f'W 14 miesiacu splacania kredytu pozostalo do splaty {m14} \n To mniej o {k14} niz w poprzednim miesiacu\n')
print(f'W 15 miesiacu splacania kredytu pozostalo do splaty {m15} \n To mniej o {k15} niz w poprzednim miesiacu\n')
print(f'W 16 miesiacu splacania kredytu pozostalo do splaty {m16} \n To mniej o {k16} niz w poprzednim miesiacu\n')
print(f'W 17 miesiacu splacania kredytu pozostalo do splaty {m17} \n To mniej o {k17} niz w poprzednim miesiacu\n')
print(f'W 18 miesiacu splacania kredytu pozostalo do splaty {m18} \n To mniej o {k18} niz w poprzednim miesiacu\n')
print(f'W 19 miesiacu splacania kredytu pozostalo do splaty {m19} \n To mniej o {k19} niz w poprzednim miesiacu\n')
print(f'W 20 miesiacu splacania kredytu pozostalo do splaty {m20} \n To mniej o {k20} niz w poprzednim miesiacu\n')
print(f'W 21 miesiacu splacania kredytu pozostalo do splaty {m21} \n To mniej o {k21} niz w poprzednim miesiacu\n')
print(f'W 22 miesiacu splacania kredytu pozostalo do splaty {m22} \n To mniej o {k22} niz w poprzednim miesiacu\n')
print(f'W 23 miesiacu splacania kredytu pozostalo do splaty {m23} \n To mniej o {k23} niz w poprzednim miesiacu\n')
print(f'W 24 miesiacu splacania kredytu pozostalo do splaty {m24} \n To mniej o {k24} niz w poprzednim miesiacu\n')
>>>>>>> c0436698c46fc211434ed3e6bbca440c1480a69b
