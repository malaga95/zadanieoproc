print ("Witamy w dziesiejszej lekcji \n Zacznijmy obliczanie twojego kredytu \n Podaj kwotę kredytu :")
TotalCreditAmount = int(input())
print ("Nastepnie miesieczna rate :")
Rata = int(input())
#float inf1=1,592824484
#float inf2=-0,453509101
#float inf3=2,324671717
#float inf4=1,261254407
#float inf5=1,782526286
#float inf6=2,329384541
#float inf7=1,502229842
#float inf8=1,782526286
#float inf9=2,328848994
#float inf10=0,616921348
#float inf11=2,352295886
#float inf12=0,337779545
#float inf13=1,577035247
#float inf14=-0,292781443
#float inf15=2,48619659
#float inf16=0,267110318
#float inf17=1,417952672
#float inf18=1,054243267
#float inf19=1,480520104
#float inf20=1,577035247
#float inf21=-0,07742069
#float inf22=1,165733399
#float inf23=-0,404186718
#float inf24=1,499708521
TimeToPay=(TotalCreditAmount%Rata)+1
print("Czas spłaty twojego kredytu nie uwzgledniajac inflacji to :" + TimeToPay + "miesiecy")