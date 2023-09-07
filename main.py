# # mano komentaras
# '''
#
# multi komentaras
# '''
# import random
# vardas = ("Diana")
# skaicius = 25
# print("mano sugalvotas skaicius" + str(skaicius))
#
# true_or_false = False boolinas
#
# print(type(true_or_false))
# listas
# fruits = ['apple','orange', 'kiwi', 'watermelon']
# print(fruits)
# print(type(fruits))

# lietuvos_pilietis = {
#     'id': 1;
# 'Vardas': 'Antanas'
# 'Amzius': 34,
# 'Miestas': 'Klaipeda'
#
# } kad nebutu sklaiustu ir kabuciu rasysime
#
# print(lietuvos_pilietis)
# print("Vardas:",lietuvos_pilietis["Vardas"])


# lietuvos_pilietis = {
#     'id': 1,
#     'Vardas': 'Antantas',
#     'Amzius': 34,
#     'Miestas': 'Klaipeda'
# }
# # print(lietuvos_pilietis)
# print("Pries:")
# print("Vardas: ", lietuvos_pilietis["Vardas"])
# print("Po: ")
# lietuvos_pilietis['Vardas'] = "Giedrius"
# print("Vardas: ", lietuvos_pilietis["Vardas"])
# # print(type(fruits))

# temperaturos = [20, 25, 22, 18, 12]
# suma = sum(temperaturos)
#
# kiekis = len(temperaturos)
# print(kiekis)
#
# # vidutine_temp = suma / kiekis
# print("Vidutine temperatura yra:", vidutine_temp)

# sudetis = 5 + 5
# atimtis = 6 - 2
# dalyba be liekanos = 15//3
# laipsnis = 2 ** 3
# dalyba su liekana = 10 % 3 rodo liekana 1
# daugyba = 5 * 9

# Print("Koks tavo vardas?:")

# # print(type(fruits))
# # 1.1. Sukurkite kintamąjį vardas ir priskirkite jam savo vardą. Tada parašykite programą, kuri išspausdina sveikinimo žinutę su jūsų vardu;
# vardas = ("Diana")
# print ("Labas" + vardas)

# 2. Sukurkite kintamuosius skaicius1 ir skaicius2, ir
# priskirkite jiems du skaičius. Parašykite programą, kuri juos sudeda ir išspausdina sumą.
# numeris1 = 10
# numeris2 = 20
# suma = numeris1+numeris2
# print(suma)


# 3. Parašykite programą, kuri prašo vartotojo įvesti skaičių ir nustato, ar tai yra lyginis ar nelyginis skaičius.

# n = int(input("skacius?"))
# if n +1:
#     print("lyginis, n, "reikmė yra" n+1)
# else:
#     print("lyginis, n, "reikmė yra" n-1)

import string

# question
# a = input( "prašau nurodykite skaičių:")
# a = 2
# while a % 2 ==0
#     print ("Lyginis")
#
#
# if a % 2 == 0:
#     a = a//2
#     a = int(input("lyginis"))


# 4. Sukurkite žodyną pavadinimu telefonu_knygute, kuriam raktai yra žmonių vardai,
# o reikšmės - jų telefono numeriai. Parašykite programą, kuri leidžia vartotojui
# ieškoti telefono numerio pagal žmogaus vardą.
#
# telefonu_knygute ={
#     'id': 1,
#     'Vardas': 'PETRAS',
#     'Telefono numeris': 868922251,
#     'id': 2,
#     'Vardas': 'SIGITA',
#     'Telefono numeris': 890254786,
#     'id': 3,
#     'Vardas': 'MARYTE',
#     'Telefono numeris': 867415298
#     }
# question =  input("Vardas:")
#
# if a == "PETRAS:"
#     print(868922251)
# if a == "SIGITA:"
#     print(890254786)
# if a == "MARYTE:"
#     print(867415298)
# print("Vardas: ", telefonu_knygute["Telefonu numeris"])


#
# lietuvos_pilietis = {
#     'id': 1,
#     'Vardas': 'Antantas',
#     'Amzius': 34,
#     'Miestas': 'Klaipeda'
# }
# # print(lietuvos_pilietis)
# print("Pries:")
# print("Vardas: ", lietuvos_pilietis["Vardas"])
# print("Po: ")
# lietuvos_pilietis['Vardas'] = "Giedrius"
# print("Vardas: ", lietuvos_pilietis["Vardas"])


# 3. Parašykite programą, kuri prašo vartotojo įvesti skaičių
# ir nustato, ar tai yra lyginis ar nelyginis skaičius.

# skaicius = float(input("Prašau nurodykite skaičių: "))
# if skaicius % 2 == 0:
#     print(int(skaicius), "skaičius yra lyginis.")
# elif skaicius % 2 == 1:
#     print(int(skaicius), "skaičius yra nelyginis.")

# telefonu_knygute ={
#     'id': 1,
#     'Vardas': 'PETRAS',
#     'Telefono numeris1': 868922251,
#     'id': 2,
#     'Vardas': 'SIGITA',
#     'Telefono numeris2': 890254786,
#     'id': 3,
#     'Vardas': 'MARYTE',
#     'Telefono numeris3': 867415298
#     }
# Vardas = input("Vardas:")
# if Vardas == 'PETRAS':
#     print("Vardas: ", telefonu_knygute["Telefono numeris1"])
# elif Vardas == 'SIGITA':
#     print("Vardas: ", telefonu_knygute["Telefono numeris2"])
# elif Vardas == 'MARYTE':
#     print("Vardas: ", telefonu_knygute["Telefono numeris3"])
#
# #
# 5. Sukurkite žodyną pavadinimu produktai, kuriame saugosite prekių pavadinimus ir jų kainas.
# Parašykite programą, kuri suranda pigiausią produktą ir išspausdina jo pavadinimą ir kainą.

# Produktai ={
#     'Pavadinimas': 'pienas',
#     'kaina1': 2.99,
#     'Pavadinimas': 'kiaušiniai',
#     'kaina2': 3.19,
#     'Pavadinimas': 'šokoladas'
#     'kaina3': 1.25
# }
# Kaina = input("kaina:")
# telefonu_knygute ={
# #     'id': 1,
# #     'Vardas': 'PETRAS',
# #     'Telefono numeris': 868922251,
# #     'id': 2,
# #     'Vardas': 'SIGITA',
# #     'Telefono numeris': 890254786,
# #     'id': 3,
# #     'Vardas': 'MARYTE',
# #     'Telefono numeris': 867415298
# #     }
# # question =  input("Vardas:")
# #
# # if a == "PETRAS:"
# #     print(868922251)
# # if a == "SIGITA:"
# #     print(890254786)
# # if a == "MARYTE:"
# #     print(867415298)
# # print("Vardas: ", telefonu_knygute["Telefonu numeris"])
#
#
# IFAS
# skaicius = 42
# if skaicius < 42:
#     print("daugiau uz 42")
# elif skaicius == 42:
#     print("Lygu")
# else:
#     print("Nelygus")

#1sarasas = [1,2,3,4,5] suraso visus skaicius su zodziu elementu
# for elementas in sarasas:
#     print("Elementas: ", elementas)

#2suraso visus skaicius nuo 0 iki 5
# for i in range(5):
#     print(i)
#3suraso visus skaicius nuo 2 iki 7 (2 imtinai)
# for i in range(2,7):
#     print(i)
#4suraso visus skaicius nuo 1 iki 10 kas antra skaiciu
# for i in range (1,10,2):
#     print(i)
#5suraso 4skaicius atvirksciai nuo 5 iki 1
# for i in range (5,0,-1):
#     print(i)
# didziausias skaicius sarase

#6skaiciai = [24,11,72,34,7, 84]
# didziausias_skaicius = skaiciai[0]
#
#7for skaicius in skaiciai:
# if skaicius > didziausias_skaicius:
# didziausias_skaicius = skaicius
# print("didziausias skaicius yra: ", didziausias_skaicius)

#8skaicius = input ("koks tavo vardas:")
# print(skaicius)

#int  - tik skaiciai
#float - su desimtaja dalimi

# (range 1 reikškia pradzia, skaicius +1 )
# skaicius = int(input("Iveskite skaiciu:"))
# suma = 0
# for i in range(1, skaicius +1):
#     suma += i
# print("skaiciu suma nuo 1 iki", skaicius, "yra",suma)

#iš sarašo išflitruoti lyginius skaicius

# sarasas = [2,5,11,25,9,16]
# lyginiai_skaiciai = []
#
# for skaicius in sarasas:
#     if skaicius %2 == 0:
#         lyginiai_skaiciai.append(skaicius)
# print ("Lyginiai_skaiciai ", lyginiai_skaiciai)

# piramidziu skaicius

# eiluciu_sk = int(input("iveskite sveika skaiciu"))
# for eilute in range(1, eiluciu_sk+1):
#     tarpas = eiluciu_sk - eilute  tarpas nuo krasto
#     zvaigzdes = 2 * eilute -1
#     print(" " * tarpas + "*" * luna)
#
# surasti pirminius skaicius is intervalo [10;50] pirminiai skaiciai rasti skaiciai intervalo viduje

# pradzia = 10
# pabaiga = 50
#
# print(f"pirminiai skaiciai tarp {pradzia} ir {pabaiga} yra: ")
# for skaicius in range(pradzia, pabaiga+1):
#     if skaicius > 1:
#         for daliklis in range(2,skaicius):
#             if (skaicius % daliklis)==0:
#                 break
#         else:
#             print(skaicius)

# zodziai_is_a = ["as", "tu", "jis", "asta", "marius"]
# raide = ("a")
# for zodis in zodziai_is_a:
#     if zodis[0].lower()== raide.lower():
#         print(zodis)

# # sudaryti ir isvesti daugybos lentele
# # tiek reiksmiu mes naudosime nuo 1 iki 10
# print("daugybos lentele nuo 1 iki 10")
# # for i in range(1,11):     tiek reiksmiu mes naudosime nuo 1 iki 10
# #     for j in range (1,11):    is ko daugynam
#         rezultatas = i*j
#         print(f"{i} x {j} = {rezultatas}")  f raide reiskia formatavimas
#     print ()

# parašyti ar skaicius yra teigiamas arba neigiams arba 0 ir isvesti pranesima

#  skaicius = int(input("Iveskite skaiciu_>")):
#      print("teigiamas")f skaicius > 0:
# elif skaicius < 0:
#     print ("neigiamas")
# else:
#     print ("lygus nuliui")

# isvesti fizz skaiciams, kurie dalijasi is 3, buzz skaiciams, kurie dalijasi is 5,
# fizzbuzz skaiciai, kurie dalijasi is 3 ir 5 intervale nuo 1 iki 100
# jeigu dalijasi is 3 ir is 5 tai
# for skaicius in range(1,101):
#     if skaicius %3 == 0 and skaicius %5 == 0:
#         print("fizzbuzz")
#     elif skaicius %3 == 0:
#         print("fizz")
#     elif skaicius %5 ==0:
#         print("buzz")
#     else:
#         print(skaicius)

# sukurkite skacius spejimo zaidima

# import random
#
# pasleptas_skaicius = random.randint(1,100)
# bandymai = 0
# maksimalus_bandymu_skaicius = 10
#  while bandymai < maksimalus_bandymu_skaicius:
#     spejimas = int(input("atspekite paslepta skaiciu nuo 1 iki 100:"))
#     bandymai +=1
#      if spejimas == pasleptas_skaicius:
#          print(f"Sveikiname! Atspejote skaiciu per{bandymai} bandymus")
#          break
#     elif spejimas < pasleptas_skaicius:
#          print ("Bandykite didesni skaiciu")
#     else:
#          print("Bandykite mazesni skaiciu")
# if bandymai >=maksimalus_bandymu_skaicius:
#     print(f"Jus pasiekete maksimalu bandymu skaiciu.pasleptas skaicius buvo {pasleptas_skaicius}

# zodziu sarasas kur zodziai ilgesni negu 6 raides

# zodziai = ["kaimas", "miestas", "savivaldybe", "miestelis", "gyvenviete", "mama", "tetis"]
# zodynas = {}
# for zodis in zodziai:
#     zodynas[zodis] = len(zodis)
# for zodis, ilgis in zodynas.items():
#     if ilgis > 6:
#         print(f"{zodis}: {ilgis} simboliai")

# 1. Sukurkite žodyną ir trumpą tekstą. Atspasudinkite žodžius, kurie pasikartojo daugiau nei 3 kartus.

# tekstas ="karta gyveno maza mergaite su papuga. Papuga kartojo paskui mergaite zodzius.mergaite mylejo papuga"
# zodynas = {}
# zodziai = tekstas.split()
# for zodis in zodziai:
#     zodynas[zodis] = zodynas.get(zodis, 0) + 1
# for zodis, pasikartojimai in zodynas.items():
#     if pasikartojimai >=3:
#      print(f"pasikartojantis zodis yra:{zodis}, pasikartojimo {pasikartojimai} kartu")

# atsitiktinis zodziu generatorius

#
# ilgis = 7
# simboliai = string.ascii_letters + string.digits + string.punctuation
# random_string = ''.join(random.choise(simboliai) for _ in range(ilgis))
# print("random_string", random_string)

# random.choices

# # 2 .Sukurti sąrašą žodžių ir išvesti unikalius žodžius bei jų pasikartojimo dažnumą;
#
# zodzia = ["mergait", "autobusas", "medis", "stalas","suolas", "medis"]
#
# for zodis in zodziai:
#     if zodis.isalpha():
# 3. Sukurkite žodyną su studentų duomenimis ir atspausdinkite studentus, kurių vidurkis yra aukščiau 8.0;
#
# studentu_zurnalas:{
#     'Vardas': 'PETRAS',
#     'Vidutinis pazymis': 6.5,
#     'Vardas': 'SAULIUS',
#     'Vidutinis pazymis': 7.9,
#     'Vardas': 'REDA',
#     'Vidutinis pazymis': 8.5,
#     'Vardas': 'LINA',
#     'Vidutinis pazymis': 8.5,
#     'Vardas': 'SIMONAS',
#     'Vidutinis pazymis': 7.8,
# }
# for vidurkis in range (1,9)
# vidurkis = vidutinis pazymis

# 4. Sukurti žodyną su knygų informacija ir surikiuoti knygas pagal metus ir pavadinimus.

# Knygu_informacija:{
# 'Knyga': 'Pavasarelis',
# 'Metai': 1995,
# 'Knyga': 'Puokste',
# 'Metai': 2010,
# 'Knyga': 'Ant kalno',
# 'Metai': 2006,
# 'Knyga': 'Pukis'
# # 'Metai': 2003
# # }
# Metai = [1995, 2010, 2006, 2003]
# Knygos = ['Pavasaris', 'Puokste', 'Ant kalno']

# Parašykite programą, kuri suskaičiuoja visų sveikujų skaičių nuo 1 iki n ėjimo sumą, kur n yra vartotojo įvestas skaičius. Panaudokite "for" ciklą ir "if" sąlygos sakinį, kad tikrintumėte, ar įvestas skaičius yra sveikasis;

# n = int(input("Iveskite skaiciu:"))
# if n <= 0:
#     print("ivestas skaicius turi buti sveikasis")
# else:
#     suma = 0
#     for skaicius in range (1, n + 1):
#         suma += skaicius
#     print(f'skaiciu suma nuo 1 iki {n}, skaicius, yra,{suma}')

# 2. Sukurkite programą, kurioje vartotojas gali įvesti mokinio pažymį (nuo 1 iki 10). Programa turi grąžinti mokinio vertinimą (pvz., "Neužtektinai", "Silpnai", "Vidutiniškai", "Gerai", "Puikiai"). Naudokite "if" sąlygos sakinį;
#
# n = int(input("Iveskite pazymi:"))
# if n == 10:
#         print("Puikiai")
# elif n == 9:
#         print("Puikiai")
# elif n == 8:
#         print("Gerai")
# elif n ==7:
#         print("Gerai")
# elif n == 6:
#         print("Vidutiniskai")
# elif n == 5:
#         print("Vidutiniskai")
# elif n == 4:
#         print("Silpnai")
# else:
#     print("Neužtektinai")


#
# n = int(input("Iveskite pazymi:"))
# if pazymis <1 or pazymis >10:
#     vertinimas = "Netinkamas pazymis, iveskite pazymi nuo 1 iki 10
#
# print (f"Mokinio vertinimas: {vertinimas}

# 3. Sukurkite programą, kuri leidžia vartotojui įvesti metus. Programa turi patikrinti, ar įvesti metai yra keliamieji (dalijasi iš 4) ir atspausdinti atitinkamą pranešimą;
# n = int(input("Iveskite metus: "))
# for skaicius in n:
#     n[skaiciai] = len(skaicius)
# for skaicius, ilgis in skaicius.items():
# if ilgis !=4:
#     print("blogas datos formatas")
# elif skaicius % 4 == 0
#     print("Data pasirinkta puikiai")



# n = int(input("Iveskite metus: "))
# metai = {}
#  for skaicius in n:
#     metai[skaicius] = len(skaicius)
# for skaicius, ilgis in metai.items():
#     if ilgis < 4:
#     print(f"{metai}: {ilgis} Dtaos formatas blogas")



# 4. Turite žody# n = int(input("Iveskite metus is 4 simboliu: "))
# # if n % 4 ==0:
# #     print ("Data ivesta gerai")
# # else:
# #     print("Data ivesta bloga")
# ną, kuriame yra vardai ir amžius. Parašykite programą, kuri peržiūri žodyną ir išrenka tik tas poras, kuriose amžius yra didesnis arba lygus 18. Rezultatus patalpinkite naujame žodyne;


# Vardas_ir_amzius:{
#     'PETRAS': 16,
#     'SAULIUS': 26,
#     'REDA': 18,
#     'LINA': 24,
#     'SIMONAS': 32
# }
# naujas = {}
# for vardas, amzius in Vardas_ir_amzius.items():
#     if amzius >= 18:
#         naujas[Vardas] = amzius
# print(naujas)

# Leiskite vartotojui įvesti kelias prekes ir jų kainas. Sukurkite sąrašą, kuriame prekės yra žodynai, kuriuose yra prekės pavadinimas ir kaina.
# Taip pat paskaičiuokite bendrą visų prekių kainą;

# prekiu_krepselis = []
# while True:
#     preke = input("nurodykite preke arba irasykite zodi baigti")
#     if not preke:
#         break
#     kaina = float(input("Iveskite prekes kaina"))
#     prekes_info = {'pavadinias': preke, 'kaina': kaina}
#     prekiu_krepselis.append(prekes_info)
# Krepselio_suma = sum((prekes_info['kaina'] for prekes_info in prekiu_krepselis))
# print("prekiu sarasas: ")
# for prekes_info in prekiu_krepselis:
#         print (f"Pavadinimas: {prekes-info['pavadinimas']}, kaina: {prekes_info['kaina']}")
# print(f"Bendra kaina: {krepselio_suma}")


# 6. Turite sąrašą žmonių vardų. Sukurkite programą, kuri leidžia vartotojui įvesti vardą ir patikrina,
# ar jis yra sąraše. Jei vardas yra sąraše, programa turi išvesti pranešimą
# "Vardas yra sąraše," kitu atveju - "Vardo nėra sąraše."


# 4. Turite žody# n = int(input("Iveskite metus is 4 simboliu: "))
# # if n % 4 ==0:
# #     print ("Data ivesta gerai")
# # else:
# #     print("Data ivesta bloga")

# vardas = ["Petras", "Maryte", "Sigita", "Ona", "Dainius"]
# x = input ("Iveskite varda:")
# if x in vardas:
#     print("Vardas yra sarase")
# else:
#     print("Vardas nera sarase")

# 4. Turite žody#

# n = int(input("Iveskite metus is 4 simboliu: "))
# if n % 4 ==0:
#     print ("Data ivesta gerai")
# else:
# #     print("Data ivesta bloga")
#
# for a in range (0, 10, 1):  #cia koks zingsis
#     print(a)
#
# def age (year_born, cur_year):
#     return cur_year - year_born
# print(age(2000, 2024))
#metai 24 gaunasi

# def hello():
#     print("hello")
# hello()

# vardas = ["Petras", "Maryte", "Sigita", "Ona", "Dainius"]
# x = input ("Iveskite varda:")
# if x in vardas:
#     print("Vardas yra sarase")
# else:
#     print("Vardas nera sarase")

# a = [1, 4, 8, 13, 2, 1, 1]
# print(a.count(1))
# kiek 1 elemente = elemente yra 3 vienetukai

# # a = [1, 4, 8, 13, 2, 1, 1]
# # a.sort()
# # print(a)
# Gauname 1,1,1,2,4,8,13
#
# a = [1, 4, 8, 13, 2, 1, 1]
# a.sort(reverse=True)
# print(a)
# Gauname 13,8,4,2,1,1,1,

# n = int(input("Iveskite metus is 4 simboliu: "))
# if n % 4 ==0:
#     print("Data ivesta gerai")
# else:
#     print("Data ivesta bloga")

# namu darbai



# 1. Sukurkite sąrašą temperatūros su temperatūromis.
# Patikrinkite kiekvieną temperatūrą sąraše ir išveskite "šilta" (jei temperatūra virš 20)
# arba "šalta" (jei temperatūra 20 ar mažiau).

temp = [15, 20, -9, 32, -24, 16]
x = int(input("Pasirinkite norima temperatura is saraso: "))
for x in range(1):
    if x >20:
        print ("silta")
    elif x <20:
        print ("šalta")



# 2. Turite žodyną su studentų vardais ir jų pažymiais.
# Parašykite "for" ciklą, kuris išveda kiekvieno studento vardą ir jo pažymį.

# zodynas = {"Petras": 8, "Maryte": 7, "Saule": 6, "Marius": 10}
# for zodis in zodynas.items:
#     print(zodis)

# 3. Sukurkite tuščią sąrašą sarasas ir leiskite vartotojui įvesti skaičius.
# Naudojant "while" ciklą, pridėkite kiekvieną įvestą skaičių prie sąrašo. Ciklą nutraukite, kai vartotojas įveda 0.

# sarasas =[]
# n = int(input("Iveskite skaiciu:"))
# while n >0:
#     sarasas.append(n)
#     if n ==0:
#         break
#     print(sarasas)
#     n +=1
# 4. Turite žodyną, kuriame saugomi gėrimų pavadinimai ir jų kainos. Vartotojas įveda gėrimo pavadinimą, o jūs patikrinkite, ar tokio pavadinimo gėrimas yra žodyne. Jei taip, išveskite jo kainą; jei ne, išveskite pranešimą "Gėrimas nerastas".

#
# zodynas = {"Fanta": 2.5, "sprite": 1.5, "Cola": 4}
# naujas = {}
#     n = int(input("Gerimas:"))
#     for n in zodynas.items:
#     naujas [gerimas] = kaina
#     print(naujas)



