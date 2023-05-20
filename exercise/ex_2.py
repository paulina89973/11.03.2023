# trojkat

a = 10
b = 20
c = 15
h = 12

obwod = a + b + c
pole = int((h * a) / 2)

print("Obwod trojkata wynosi " + str(obwod) + ", zas pole wynisi " + str(pole) + ".")

#prostokat
a=2
b=5

obwod= 2a + 2b
pole= a * b

print("Obwod prosotkata wynosi" + str(obwod) + " , zas pole wynosi" + str(pole) + ".")

# romb
a = 12
obwod_rombu = a*4
f=11
g=15
pole_rombu = (f*g)/2
print("Obwod rombu wynosi: " + str(obwod_rombu) + ", a pole wynosi " + str(pole_rombu))

#kolo
r = 14
obwod_kola = 2*math.pi*r
pole_kola = math.pi*math.pow(r,2)
print("Obwod kola wynosi: " + str(obwod_kola) + ", a pole wynosi " +str(pole_kola))


#trapez
a = 11
b = 5
c = 7
d= 9
h = 3

pole_trapezu = ((a+b)*h)/2
obwod_trapezu = a+b+c+d
print("Obwod trapezu wynosi: " + str(obwod_trapezu) + ", a pole wynosi " +str(pole_trapezu))
