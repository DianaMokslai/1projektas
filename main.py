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
#
# temp = [15, 20, -9, 32, -24, 16]
# x = int(input("Pasirinkite norima temperatura is saraso: "))
# for x in range(1):
#     if x >20:
#         print ("silta")
#     elif x <20:
#         print ("šalta")



# 2. Turite žodyną su studentų vardais ir jų pažymiais.
# Parašykite "for" ciklą, kuris išveda kiekvieno studento vardą ir jo pažymį.


# zodynas = {"Petras": 8, "Maryte": 7, "Saule": 6, "Marius": 10}
# for zodis in zodynas.items():
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

# jeigu nera indekso viduje grazina paskutini nuo galo, jeigu prie pop bus indeksas tad nuo priekio skaiciuojame nuo
# vardai = ['Jonas', 'Petras', 'Marius', 'Laura']
# pirmas_vardas = vardai.pop()
# print(pirmas_vardas)

# idedam elementa pagal nurodyta reiksme
# vardai.insert(1, 'Giedrius')
# print(vardai)
# ideda varda i gala
# vardai.append('Giedrius')
# print(vardai)
#
# vardai.sort(reverse=true)
# print(vardai)

# a = ("b", "g", "a", "d", "f", "c", "h", "e")
# x = sorted(a)
# print(x)

# vardai.remove('Laura')
# print(vardai)

# vaisiai = ('obuolys', 'kriause', 'Bananas', 'braske')
# vaisiai1 = ['obuolys', 'kriause', 'Bananas', 'braske']
# vaisiai = {'obuolys',
#     'kriause',
#     'Bananas',
#     'braske'
# }
#
# vaisiai2 = vaisiai[0]
#     print(vaisiai2)

# skaiciai = (3.14, 2.71)
# x, y = skaiciai
# print(x)
# print(y)

# vaisiai1 = ['obuolys', 'kriause', 'Bananas', 'braske']
# for indeksas, vaisius in enumerate(vaisiai1, start =1):
#     print(f"{indeksas}, {vaisius}")

# with open("failo_pav.txt", 'r', encoding='utf-8') as file:
#     for eilute in file:
#         print(eilute.strip())

# vaisiai = []

# with open("vaisiai.txt", 'r', encoding='utf-8') as file:
#     file.write('obuolys, \nkriause, \nBananas, \nbraske')
#     vaisiai = file.readlines()
#     print(vaisiai)

# 4. Turite žodyną, kuriame saugomi gėrimų pavadinimai ir jų kainos.
# Vartotojas įveda gėrimo pavadinimą, o jūs patikrinkite, ar tokio pavadinimo gėrimas yra žodyne.
# Jei taip, išveskite jo kainą; jei ne, išveskite pranešimą "Gėrimas nerastas".


# drinkas = input('Iveskite gerimo pavadinimus')
# zodynas = {"Fanta": 2.5, "sprite": 1.5, "Cola": 4}
# if drinkas in zodynas:
#     kaina =  zodynas [drinkas]
#     print(kaina)
# else:
#     print('tokio gerimo nerurime')





# 2.
# zodynas = {"Petras": 8, "Maryte": 7, "Saule": 6, "Marius": 10}
# for zodis in zodynas.items():
#     print(zodis)


# 1. Sukurkite sąrašą temperatūros su temperatūromis.
# Patikrinkite kiekvieną temperatūrą sąraše ir išveskite "šilta" (jei temperatūra virš 20)
# arba "šalta" (jei temperatūra 20 ar mažiau).
#


# 5. Patikrinkite, ar skaičiai sąraše yra lyginiai arba nelyginiai.
# Sukurkite du tuščius sąrašus: vienas lyginiams ir kitą nelyginiams skaičiams, išrūšiuokite lyginius ir nelyginius skaičius iš skaičiai sąrašo.


# 1. Parašykite funkciją, kuri priimtų sąrašą studento pažymių ir grąžintų vidurkį;

# Petras = [8,5,6,7]
# Maryte = [7,5,10,9,8]
# Saule = [6,10,10,10]
# Marius =[10,10,2,9]


# def mano_sarasas(sarasas):
#    sandauga = 1
#    for skaicius in sarasas:
#         sandauga *= skaicius
#    return sandauga
# sk_sarasas = [2, 4, 6, 8, 10]
# print('Saraso skaiciu sandauga lygi:',mano_sarasas (sk_sarasas))

# # objektinis programavimas
# #sukuriamas klase pvz projektas
# class Zmogus:
#     #sukuriamas konstruktorius apibrezimas ko nori
#     def __init__(self,vardas, amzius):
#         self.vardas = vardas
#         self.amzius = amzius
#         #kuriami metodai
#
#     def sveikinimas(self):
#         return f"Sveiki, as esu {self.vardas} ir man yra {self.amzius} metu"
#
# #sukuriamas objektas
#
# zmogus1 = Zmogus("Jonas", 30)
# zmogus2 = Zmogus("Antanas", 45)
#
# print(zmogus1.sveikinimas())
# print(zmogus2.sveikinimas())

# class Automobilis:
#     def __init__(self, marke, modelis):
#         self.marke = marke
#         self.modelis = modelis
#         self.greitis = 0
#
#     def akseleratorius(self):
#         self.greitis += 10
#
#     def stabdis (self):
#         self.greitis -= 5
#
#     def info(self):
#         return f"{self.marke} {self.modelis}, greitis: {self.greitis} km/h"
#
# auto1= Automobilis("Mazda", "323")
# auto1.akseleratorius()
# auto1.akseleratorius()
# auto1.akseleratorius()
# auto1.stabdis()
#
# print(auto1.info())
#
# class Knyga:
#
#     def __init__(self, pavadinimas, autorius, leidimo_metai):
#         self.pavadinimas = pavadinimas
#         self.autorius = autorius
#         self.leidimo_metai = leidimo_metai
#
#     def info(self):
#             return f"Knygos pavadinimas {self.pavadinimas}, Autorius: {self.autorius}, leidimo_metai: {self.leidimo_metai}"
#
# knyga = Knyga("Visi norejo testo", "Studentas",2023)
# print(knyga.info())
#
# class Preke:
#
#     def __init__(self, pavadinimas, kaina):
#         self.pavadinimas = pavadinimas
#         self.kaina = kaina
#     def info(self):
#         return f"{self.pavadinimas}: {self.kaina} Eur"
#
# class Krepselis:
#
#     def __init__(self):
#
#         self.prekes = []
#
#     def ideti_preke(self, preke):
#         self.prekes.append(preke)
#
#     def krepselio_info(self):
#         if not self.prekes:
#             print('tokios prekes nera')
#         else:
#             print("krepselio turinys:")
#             for preke in self.prekes:
#                 print(preke.info())
#
#     def bendra_suma(self):
#         suma = sum(preke.kaina for preke in self.prekes)
#         return suma
#
# krepsys = Krepselis()
# preke1 = Preke('obuolys', 5.0)
# preke2 = Preke('bananas', 2.0)
# preke3 = Preke('vanduo', 1.3)
# preke4 = Preke ('kava', 10.5)
#
# krepsys.ideti_preke(preke1)
# krepsys.ideti_preke(preke2)
# krepsys.ideti_preke(preke3)
# krepsys.ideti_preke(preke4)
# krepsys.ideti_preke(preke4)
#
# krepsys.krepselio_info()
#
# print(f"bendra suma : {krepsys.bendra_suma()} Eur")
#
# Sukurkite klasę "Saskaita", kuri turėtų šias savybes ir metodus:
#
#     * saskaitos_nr: sąskaitos numeris.
#     * balansas: sąskaitos balansas (numatytasis pradžioje yra 0).
#     * inesti(suma): metodas, kuris prideda nurodytą sumą prie sąskaitos balanso.
#     * isimti(suma): metodas, kuris sumažina sąskaitos balansą nurodyta suma,
# jei yra pakankamai lėšų, arba išveda pranešimą apie nepakankamą balansą.
#     * informacija(): metodas, kuris grąžina informaciją apie sąskaitą (sąskaitos numeris ir balansas).
#
# Sukurkite bent du objektus pagal šią klasę ir atlikite operacijas,
# tokiu kaip lėšų įnešimas ir išėmimas, bei gaukite sąskaitos informaciją.
#
# class Saskaita:
#     def __init__(self, saskaitos_numeris, balansas):
#
#         self.saskaitos_numeris = saskaitos_numeris
#
#     def info(self):
#         return f"{self.saskaitos_numeris}:"
#
# class Balansas:
#     def __init__(self):
#
#             self.balansas = 0
#
#         def inesti_suma(self):
#             self.balansas =int(input "Inesimo suma")
#             self.balansas += suma
#             if self.balansas >= balansas:
#                 self.balansas -= balansas
#                 print("Balansas pakankamas:")
#             else:
# #                 print('Nepakanka pinigu')
# #
# class Saskaita:
#     def __init__(self, saskaitos_numeris):
#
#         self.saskaitos_numeris = saskaitos_numeris
# class Balansas:
#     def __init__(self):
#         self.balansas = 0
#
#     def lesu_inesimas(self):
#         self.balansas = float(input("iveskite suma: "))
#         self.balansas += balansas
#         print("Balanso likutis: ", balansas)
#
#     def lesu_isemimas(self):
#         self.balansas = float(input("isimti suma: "))
#         if self.balansas >= balansas:
#             self.balansas -= balansas
#             print("isimti suma: ", balansas)
#         else:
#             print("nepankamas balansas ")
#
#     def informacija(self):
#         print("Saskaitos numeris", self.balansas)
#
# saskaita1 = Saskaita("LT2222258")
# balansas1 = Balansas()
# saskaita1.balansas = balansas1
# balansas1.lesu_inesimas()
# balansas1.lesu_isemimas()

#
# saskaita1.informacija()

# class Studentas:
#     def __init__(self, st_vardas):
#         self.st_vardas = st_vardas
#         self.pazymiai = []
#     def prideti_pazymi(self, pazymys):
#         self.pazymiai.append(pazymys)
#     def vidurkis(self):
#         if not self.pazymiai:
#             return 0
#         return sum(self.pazymiai) / len(self.pazymiai)
#
# class Mokytojas:
#     def __init__(self, mokytojo_vardas, destomas_dakykas):
#         self.mokytojo_vardas = mokytojo_vardas
#         self.destomas_dalykas = destomas_dakykas
#     def ivertinimas(self, studentas, pazymys):
#         studentas.prideti_pazymi(pazymys)
#
# studentas1=Studentas('Petras')
# mokytojas1=Mokytojas('Jurgis', 'informatika')
#
# mokytojas1.ivertinimas(studentas1, 3)
#
# print(f'{studentas1.st_vardas}, vidurkis: {studentas1.vidurkis()}')

#
# def pasveikinimas(vardas):
#     sveikinimas = f"Sveiki, {vardas}"
#     return sveikinimas
#
# vardas = input("Iveskite savo varda:")
# sveikinimas = pasveikinimas(vardas)
# print(sveikinimas)
#
# def ar_lyginis(skaicius):
#     if skaicius % 2 == 0:
#         return True
#     else:
#         return False
#
# skaicius = 7
# if ar_lyginis(skaicius):
#     print(f"{skaicius} yra lyginis")
# else:
#     print(f"{skaicius} yra nelyginis")

#
# def suma (a,b):
#     rezultatas = a + b
#     return rezultatas
#
# x= 5
# y= 3
# sumos_rezultatas = suma(x, y)
# print(f"{x} + {y} = {sumos_rezultatas} ")


# def suma ():
#     rezultatas = 5 + 3
#     return rezultatas
#
# x= 5
# y= 3
# sumos_rezultatas = suma(x, y)
# print(f"{x} + {y} = {sumos_rezultatas} ")


# def pasisveikinimas():
#     sveikinimas = f"Sveiki, Diana"
#     return sveikinimas
#
# if __name__ == "__main__":
#     main()


# def vidurkis(skaiciai):
#     suma = sum(skaiciai)
#     avg = suma / len(skaiciai)
#     return avg
#
# sarasas = [5,6,10,15,20,25,30]
# rezultatas = vidurkis(sarasas)
# print(f"saraso vidurkis : {rezultatas}")


# 1. patikrinti ar skaicius yra teigiamas ar neigiamas#
#
# def ar_teigiamas(skaicius):
#     if skaicius > 0:
#         return True
#     else:
#         return False
#
# skaicius = 4
# if ar_teigiamas (skaicius):
#     print(f"{skaicius} yra teigiamas")
# else:
#     print(f"{skaicius} yra neigiamas")

# 2. surasti didziausia skaicius sarase
#
# def didz_skaicius(skaicius):
#     didziausias = skaicius[0]
#     for i in skaicius:
#         if i > didziausias:
#             didziausias = i
#     return didziausias
#
# sarasas = [10,658,12,-2]
# didziausias = didz_skaicius(sarasas)
# print(f"didziausias yra {didziausias}")


# 3. funkcija kuri sujungia du sarasus
# def sujungti_sarasai (sarasas1, sarasas2):
#     sujungtas_sarasas = sarasas1 + sarasas2
#     return sujungtas_sarasas
# s_1 = [1, 2, 3]
# s_2 = [4, 5, 6]
# rezultatas = sujungti_sarasai(s_1, s_2)
# print(rezultatas)


# 4. funkcija suras didziausius skaicius negu nurodytas mano skaicius
#
# def didesnis( listas, skaicius ):
#     didesnis = [sk_1 for sk_1 in listas if sk_1 > skaicius]
#     return didesnis
# listas = [1, 2, 15, 101, 1005]
# n = 8
# didesni_sk = didesnis(listas, n)
# print(f"sarase skaiciai didesni uz {n}: yra {didesni_sk}")

# 1. Parašykite funkciją, kuri priimtų sąrašą studento pažymių ir grąžintų vidurkį;
#
# def studento_sarasas (pavarde, pazymiai):
#     pazymiu_suma = sum(pazymiai)
#     vidurkis = pazymiu_suma / len(pazymiai)
#     return pavarde, vidurkis
#
#
# list1 = [('Petras', [8.9.7]), ('Maryte', [9.9.10])]
# list2 = []
#
# for studentas in studentai:
#     pavarde, pazymiai = studentas
#     rezultatas = studento_sarasas(pavarde, pazymiai)
#     rezultatai.appen(rezultatas)
#
# for rezultatas in rezultatai:
#     pavarde, vidurkis = rezultatas
#     print(f'Studentas: {pavarde}, Vidurkis {vidurkis}')
#
# # 3. Sukurkite funkciją zodziu_kiekis(tekstas), kuri priima tekstą ir grąžina žodžių skaičių tekste.
# # Žodžius galite laikyti atskirtais tarpais;
#
# def zodziu_kiekis(tekstas):
#     zodziai = tekstas.split()
#     return len(zodziai)
#
# s_1 = "Man trys metukai"
# zodziu_skaicius = zodziu_kiekis(s_1)
#
# print(f"zodziu kiekis: {zodziu_skaicius}")
#
# Sukurkite klasę "Studentas", kuri turėtų šias savybes:
#
#     * vardas: studento vardas.
#     * pazymiai: sąrašas su studento pažymiais.
#
# Sukurkite klasę "Mokytojas", kuri turėtų šias savybes:
#
#     * vardas: mokytojo vardas.
#     * Mokytojo dėstoma tema: mokytojo dėstomas dalykas.
#
# Papildykite "Studentas" klasę metodu vidurkis(), kuris apskaičiuoja studento pažymių vidurkį.
#
# Papildykite "Mokytojas" klasę metodu ivertinimas(studentas, pazymys), kuris prideda studentui pažymį.
#
# Sukurkite objektus pagal "Studentas" ir "Mokytojas" klases, pridėkite pažymius ir vykdykite vidurkio apskaičiavimus bei pažymių pridėjimus.

# class Studentas:
#     def __init__(self, st_vardas):
#         self.st_vardas = st_vardas
#         self.pazymiai = []
#     def prideti_pazymi(self, pazymys):
#         self.pazymiai.append(pazymys)
#     def vidurkis(self):
#         if not self.pazymiai:
#             return 0
#         return sum(self.pazymiai) / len(self.pazymiai)
#
# class Mokytojas:
#     def __init__(self, mokytojo_vardas, destomas_dakykas):
#         self.mokytojo_vardas = mokytojo_vardas
#         self.destomas_dalykas = destomas_dakykas
#     def ivertinimas(self, studentas, pazymys):
#         studentas.prideti_pazymi(pazymys)
#
# studentas1=Studentas('Petras')
# mokytojas1=Mokytojas('Jurgis', 'informatika')
#
# mokytojas1.ivertinimas(studentas1, 3)
#
# print(f'{studentas1.st_vardas}, vidurkis: {studentas1.vidurkis()}')

# 6. Sukurkite funkciją sarasas_suma(sarasas), kuri priima sąrašą skaičių ir suskaičiuoja jų sumą.
# Leiskite vartotojui įvesti sąrašą skaičių ir išvesti jų sumą;

# def sarasas_suma(skaiciai):
#     suma = sum(skaiciai)
#     return suma
#
# sarasas = [5,6,10,15,30,15,20,14]
# rezultatas = sarasas_suma(sarasas)
# print(f'saraso suma: {rezultatas}')



# def sarasas_suma(skaiciai):
#     suma = sum(skaiciai)
#     return suma
#
# f = int(input "iveskite nprimus skaicius: ")
# rezultatas = sarasas_suma(f)
# print(f'saraso suma: {rezultatas}')

# 7. Sukurkite funkciją, kuri priimtų skaičių sąrašą ir grąžintų visų sąrašo skaičių sandaugą.

# def sarasas_sandauga(skaiciai):
#     sandauga = 1
#
#     for i in skaiciai:
#         sandauga *= i
#     return sandauga
# sk_sarasas = [2,4,6,8,10]
# print('Saraso skaiciu sandauga lygi:',sarasas_sandauga (sk_sarasas))


# # Sukurkite funkciją kvadrato_plotas(ilgis), kuri priima kvadrato kraštinės ilgį ir grąžina kvadrato plotą.
# kvadrota plotas = a*2
# def kvadrato_plotas (ilgis):
#     plotas =  ilgis **2
#     return plotas
# ilgis = 4
# plotas = kvadrato_plotas(ilgis)
# print(f"kvadrato plotas: {plotas} ")

# class Kava:
#     def __init__(self, pavadinimas, kaina, talpa):
#         self.pavadinimas = pavadinimas
#         self.kaina = kaina
#         self.talpa = talpa
#
#     def atitiktis_puodeliui(self, puodelio_talpa):
#         if self.talpa <= puodelio_talpa:
#             return f"{self.pavadinimas} kava tinka puodeliui su talpa {puodelio_talpa} ml"
#         else:
#             return f"{self.pavadinimas} kava netelpa {puodelio_talpa} ml"
#
# kava1 = Kava("Latte", 6.50, 250 )
# puodelio_talpa = 300
# print(kava1.atitiktis_puodeliui(puodelio_talpa))
#
# #  knigynas turi savybe, knygos, prideti _ieskoti ir atspausdinti visu knygu sarase
# class Knygynas:
#
#     def __init__(self):
#         self.knygos = []
#
#     def prideti_knyga(self,knyga):
#         self.knygos.append((knyga))
#
#     def ieskoti_knygos(self,pavadinimas):
#         for knyga in self.knygos:
#             if knyga['pavadinimas'] == pavadinimas:
#                 return knyga
#         return None
#     def knygu_sarasas(self):
#         if not self.knygos:
#             print('Knygynas tuscias')
#         else:
#             print('knygyno knygu sarasas: ')
#             for knyga in self.knygos:
#                 print(f"Pavadinimas: {knyga[ 'pavadinimas']}, Autorius: {knyga['autorius']}, Metai: {knyga['metai']}")
# knigynas = Knygynas()
# knigynas.prideti_knyga({'pavadinimas' : 'seslis', 'autorius': 'Zemaitis', 'metai': 1981})
# ieskoma_knyga = knigynas.knygos_paieska('seslis')
# if ieskoma_knyga:
#     print(f'rasta knyga: {ieskoma_knyga["pavadinimas"]}')
# else:
#     print('knyga nerasta')
# knigynas.knygu_sarasas()

# Sukurkite klasę "Prekybininkas", kuri turi atributus "vardas" (name) ir "prekės" (items) ( prekių sąrašas).
# Parašykite metodus, kurie leidžia pridėti prekes prie prekių sąrašo, pašalinti prekes ir paskaičiuoti prekių bendrą sumą;
# #
# class Prekybininkas:
#     def __init__(self, name):
#         self.name = name
#         self.prekes = []
#
#     def prideti_preke(self, preke, kiekis =1):
#         for _ in range(kiekis):
#             self.prekes.append(preke)
#
#     def pasalinti_preke(self, preke, kiekis=1):
#         if preke in self.prekes:
#             for _ in range(kiekis):
#                 self.prekes.remove(preke)
#         else:
#             print('tokios prekes nera')
#
#     def prekiu_suma(self):
#         suma =  sum(preke[1] for preke in self.prekes)
#         return suma
#
# pardavejas = Prekybininkas('Martynas')
#
# preke1 = ('kava', 1.0)
# preke2 = ('obuolys', 2.5)
# preke3 = ('kamuolys', 1.5)
#
# pardavejas.prideti_preke(preke1)
# pardavejas.prideti_preke(preke2)
# pardavejas.prideti_preke(preke3,3)
# suma=pardavejas.prekiu_suma()
#
# print(suma)
#
# pardavejas.pasalinti_preke((preke1))
#
# print('prekiu sarasas: ')
# for preke in pardavejas.prekes:
#     print(f"{preke[0]}: {preke[1]}")
# print(f"bendra visu prekiu suma: {suma}")

# knigynas turi savybe, knygos, prideti _ieskoti ir atspausdinti visu knygu sarase
# class Knygynas:
#
#     def __init__(self):
#         self.knygos = []
#
#     def prideti_knyga(self,knyga):
#         self.knygos.append((knyga))
#
#     def ieskoti_knygos(self,pavadinimas):
#         for knyga in self.knygos:
#             if knyga['pavadinimas'] == pavadinimas:
#                 return knyga
#         return None
#     def knygu_sarasas(self):
#         if not self.knygos:
#             print('Knygynas tuscias')
#         else:
#             print('knygyno knygu sarasas: ')
#             for knyga in self.knygos:
#                 print(f"Pavadinimas: {knyga[ 'pavadinimas']}, Autorius: {knyga['autorius']}, Metai: {knyga['metai']}")
# knigynas = Knygynas()
# knigynas.prideti_knyga({'pavadinimas' : 'seslis', 'autorius': 'Zemaitis', 'metai': 1981})
# ieskoma_knyga = knigynas.knygos_paieska('seslis')
# if ieskoma_knyga:
#     print(f'rasta knyga: {ieskoma_knyga["pavadinimas"]}')
# else:
#     print('knyga nerasta')
# # knigynas.knygu_sarasas()
#
# Sukurkite klasę "Darbuotojas" (Employee), kuri turi atributus "vardas" (name), "pareigos" (position), ir "atlyginimas" (salary).
# Parašykite metodus, kurie leidžia keisti darbuotojo pareigas ir atlyginimą;
#
# class Darbuotojas:
#     def __init__(self, vardas, pareigos, atlyginimas):
#         self.vardas = vardas
#         self.pareigos = pareigos
#         self.atlyginimas = atlyginimas
#
#     def pareigu_keitimas(self, naujos_pareigos):
#         self.pareigos = naujos_pareigos
#
#     def atlyginimo_keitimas(self, naujas_atlyginimas):
#         self.atlyginimas = naujas_atlyginimas
#
#
# info1 = Darbuotojas("Petras", "elektrikas", 2000)
#
#
# info1.pareigu_keitimas('Vadovas')
# info1.atlyginimo_keitimas(3600)
#
# print(f" Darbuotojo vardas: {info1.vardas}, pakeistos pareigos{info1.pareigos()}, pakeistas atlyginimas{info1.atlyginimas()} Eur")

# 3. Sukurkite klasę "Skaičiuotuvas", kuri turi metodus "sudėti" (add), "atimti" (subtract), "dauginti" (multiply) ir "dalinti" (divide).
# Šie metodai priima du skaičius ir atlieka atitinkamą matematinę operaciją.
#
# class Skaiciuotuvas:
#     def __init__(self, sudeti, atimti, dauginti, dalinti):
#         self.sudeti = sudeti
#         self.atimti = atimti
#         self.dauginti = dauginti
#         self.dalinti = dalinti
#
#
#     def dvieju_skaiciu_suma(self,number1, number2 ):
#         self. sudeti  = number1+number2
#         return
#
#     def dvieju_skaiciu_atimtis(self,number1, number2):
#         self.atimti = number1 - number2
#         return
#
#     def dvieju_skaiciu_daugyba(self, number1*number2):
#         self.dauginti = number1 ** number2
#         return multiply
#
#
#     def dvieju_skaiciu_dalyba(self, divide):
#         self.dalinti  /= divide
#         return divide
#
#
#
# calculate = Skaiciuotuvas()
#
# s1 = 10
# s2 = 5
#
# calculate = dvieju_skaiciu_suma {s1+s2}
# calculate = dvieju_skaiciu_atimtis {s1-s2}
# calculate = dvieju_skaiciu_daugyba {s1*s2}
# calculate = dvieju_skaiciu_dalyba {s1/s2}
#
#
#
# sumos_rezultatas = calculate.dvieju_skaiciu_suma(s1, s2)
# subtract_rezultatas = calculate.dvieju_skaiciu_atimtis(s1, s2)
# multiply.rezultatas = calculate.dvieju_skaiciu_daugyba(s1, s2)
# divide.rezultatas = calculate.dvieju_skaiciu_dalyba(s1,s2)
#
# print("Sum:", sum_result)
# print("Subtraction:", subtract_result)
# print("Multiplication:", multiply_result)
# print("Division:", divide_result)


# class Skaiciuotuvas:
#     def add(self,a, b):
#         return a+b
#     def subtract(self, a, b):
#         return a-b
#     def multiply(self, a, b):
#         return a*b
#     def divide(self, a, b):
#         if b == 0:
#             return ("dalyba iš 0 negalima")
#         else:
#             return a/b
#
# a = 3
# b = 2
#
# a1 = Skaiciuotuvas()
# suma = a1.add(a, b)
# skirtumas = a1.subtract(a,b)
# sandauga = a1.multiply(a,b)
# dalyba = a1.divide(a,b)
#
# print(f"{suma}, {skirtumas}, {sandauga}, {dalyba}")

# Sukurkite klasę "Klase", kuri turės savybę "pavadinimas" ir sąrašą "pamokos" (pamokų pavadinimai ir laikas).
# Sukurkite klasę "Mokykla", kuri turės sąrašą klasių.
# Parašykite metodą, kuris išveda mokyklos tvarkaraštį su visomis pamokomis.

# class Klase:
#     def __init__(self, pavadinimas):
#         self.pavadinimas = pamokos_pavadinimas
#         self.pamokos = []
#     def prideti_pamoka(self, pavadinimas, laikas):
#         self.pamokos.append((pavadinimas, laikas))
#
#     def gauti_tvarkarasti(self):
#         tvarkarastis = f"Klase: {self.pavadinimas} \n"
#         for pamoka in self.pamokos:
#             pavadinimas, laikas = pamoka
#             tvarkarastis += f"- {pavadinimas}, laikas: {laikas} \n"
#             return tvarkarastis
# class Mokykla:
#     def __init__(self, pavadinimas):
#         self.pavadinimas = pavadinimas
#         self.klases = []
#
#     def prideti_klase (self, klase):
#         self.klases.append(klase)
#
#     def tvarkarastis_galutinis(self):
#         galutinis = f"Mokykla: {self.pavadinimas} \n"
#         for klase in self.klases:
#             galutinis += klase.tvarkarastis()
#         return galutinis
#
#
#
# Mokykla1 = Mokykla ("Vyduno gimnazija")
#
# klase1 = Klase("6 B")
# klase1.prideti_pamoka("Lietuvių", "9:00")
#
# klase2 = Klase("1 E")
# klase2.prideti_pamoka("Anglų", "10:00")
#
#
# Mokykla1 = Mokykla("Vyduno gimnazija")
#
# Mokykla1.prideti_klase(klase1)
# Mokykla1.prideti_klase(klase2)
# tvarkarastis = mokykla.tvarkarastis_galutinis()
#
# print(mokykla.tvarkarastis_galutinis())

# Sukurkite klasę "Žaislas", kuri turėtų savybes, tokias kaip "pavadinimas" ir "amžiaus rekomendacija".
# Tada sukurkite klasę "Vaikas", kuri turėtų vardą ir amžių.
# Tada sukurkite klasę "VaikasSuZaislu", kuri turėtų šio vaiko objektą ir žaislo objektą.
# Patikrinkite, ar vaiko amžius atitinka žaislo amžiaus rekomendaciją.
#
# class Zaislas:
#     def __init__ (self, pavadinimas, amzius):
#         self.pavadinimas = pavadinimas
#         self.amzius = amzius
#
# class Vaikas:
#
#     def __init__ (self, vardas, amzius):
#         self.vardas = vardas
#         self.amzius = amzius
#
#
# class VaikasSuZaislu:
#
#     def __init__ (self, vaikas, zaislas):
#         self.zaislas = zaislas
#         self.vaikas = vaikas
#
#     def vaiko_amziaus_atitiktis(self):
#         if self.vaikas.amzius >= self.zaislas.amzius:
#             return f'{self.vaikas.vardas} gali zaisti su zaislu "{self.zaislas.pavadinimas}" '
#         else:
#             return f'{self.vaikas.vardas} negali zaisti su zaislu "{self.zaislas.pavadinimas}", nes turi paaugti '
#
# zaislas1 = Zaislas ('Roblox', 12)
# vaikas1 = Vaikas('Petriukas',10)
# vaikas_su_zaislu1 = VaikasSuZaislu(vaikas1, zaislas1)
#
# rezultatas = vaikas_su_zaislu1.vaiko_amziaus_atitiktis()
# print(rezultatas)

# Sukurkite programą, kuri leidžia vartotojui valdyti krepšinio komandą.
# Galite kurti klases, pvz., "Komanda", "Žaidėjas", "Treneris".
# Kiekvienas žaidėjas turėtų turėti savo statistiką(taiklumas,pozicija),
# o treneris - instrukcijas ir strategiją(komandos sudeti).
# Programa turi leisti vartotojui pridėti naujus žaidėjus, juos treniruoti ir valdyti komandos sudeti.

# class Treneris:
#     def __init__(self):
#         self.strategija = "ataka"
#     def keisti_strategija(self,nauja_strategija):
#         self.strategija = nauja_strategija
#
#     def strategijos_info(self):
#         return f'naudojama strategija {self.strategija}'
# class Zaidejas:
#     def __init__(self, pavarde, pozicija):
#         self.pavarde = pavarde
#         self.taiklumas = 30
#         self.pozicija = pozicija
#
#     def upgrade(self):
#         self.taiklumas += 5
#         if self.taiklumas > 100:
#             self.taiklumas = 100
#
#     def zaidejo_info(self):
#         return f'{self.pavarde}, zaidejo pozicija {self.pozicija}, ir jo taiklumas {self.taiklumas}%'
# class Komanda:
#     def __init__(self, pavadinimas):
#         self.komanda =[]
#         self.pavadinimas = pavadinimas
#         self.treneris = Treneris()
#     def prideti_zaideja(self,zaidejas):
#         self.komanda.append(zaidejas)
#
#     def isimti_zaideja(self, zaidejas):
#         if zaidejas in self.komanda:
#             self.komanda.remove(zaidejas)
#     def komandos_informacija(self):
#         print(f'{self.pavadinimas}, komandos zaidejai: ')
#         for zaidejas in self.komanda:
#             print(zaidejas.zaidejo_info())
#     def strategijos_info(self):
#         print (self.treneris.strategijos_info())
#
#     def pasirinkti_treneri(self, treneris):
#         self.komanda.append(treneris)
#
#     def pakeisti_treneri(self, treneris):
#         if treneris in self.komanda:
#             self.komanda.remove(treneris)
#
# komanda=Komanda("Puseles")
# zaidejas1=Zaidejas("Greitas", "puolejas")
# zaidejas2=Zaidejas("didelis", "saugas")
# zaidejas3=Zaidejas("vidutinis", "atsarginis")
#
# komanda.prideti_zaideja(zaidejas1)
# komanda.prideti_zaideja(zaidejas2)
# komanda.prideti_zaideja(zaidejas3)
#
# zaidejas1.upgrade()
# zaidejas1.upgrade()
# zaidejas3.upgrade()
#
# komanda.komandos_informacija()
# komanda.strategijos_info()

    # DUomenu analitika

#
#
# import pandas as pd
# import matplotlib.pyplot as plt
#
# # duomenys = {'Vardas': ['Jonas', 'Ieva', 'Petras', 'Ona'],
# #             'Amzius': [25, 28, 22, 30]
# #             }
# # df = pd.DataFrame(duomenys)
# # # print(df)
# #
# # jaunesni = df[df['Amzius'] < 25]
# # # print(jaunesni)
# #
# # vidutinis_amzius = df['Amzius'].mean()
# # print(f'Vidutinis amzius: {vidutinis_amzius}')
#
# # temperaturos = [24.5, 25.2, 23.8, 26.0, 22.5]
# #
# # sr = pd.Series(temperaturos)
# #
# # print(sr)
#
# # Mazejancia tvarka
# # temperaturos = [24.5, 25.2, 23.8, 26.0, 22.5]
# #
# # sr = pd.Series(temperaturos)
# # serija_rikiavimas = sr.sort_values()
# #
# # print(serija_rikiavimas)
#
# # Didejancia tvarka
# # temperaturos = [24.5, 25.2, 23.8, 26.0, 22.5]
# #
# # sr = pd.Series(temperaturos)
# # serija_rikiavimas = sr.sort_values(ascending = False)
# #
# # print(serija_rikiavimas)
#
# # temperaturos = [24.5, 25.2, 23.8, 26.0, 22.5]
# # sr = pd.Series(temperaturos)
# # print(f"pirmas elementas: {sr[0]}")
#
# # # # parodo tik vardus
# # duomenys = {'Vardas': ['Jonas', 'Ieva', 'Petras', 'Ona'],
# #             'Amzius': [25, 28, 22, 30]
# #             }
# # df = pd.DataFrame(duomenys)
# # vardai = df['Vardas']
# # print("Vardai: ")
# # print(vardai)
# # parodo vardus eilute
# # duomenys = {'Vardas': ['Jonas', 'Ieva', 'Petras', 'Ona'],
# #             'Amzius': [25, 28, 22, 30]
# #             }
# # df = pd.DataFrame(duomenys)
# # # vardai = df['Vardas'].to_list()
# # # print("Vardai: ")
# # # print(vardai)
#
# # jeigu noretume prideti nauja stulpeli i savo DataFrame
# # duomenys = {'Vardas': ['Jonas', 'Ieva', 'Petras', 'Ona'],
# #             'Amzius': [25, 28, 22, 30]
# #             }
# # df['Lytis'] = [['Vyras', 'Moteris', 'Vyras', 'Moteris']]
# # df = pd.DataFrame(duomenys)
# # print('Atnaujintas dataframe dsu nauju stulpeliu: ')
# # print(df)
# duomenys = {'Vardas': ['Jonas', 'Ieva', 'Petras', 'Ona'],
#             'Amzius': [25, 28, 22, 30]
#             }
# df = pd.DataFrame(duomenys)
# vardai = df['Vardas']
# print("Vardai: ")
# print(vardai)
#
#
# plt.figure(figsize=(8,5))
# plt.bar(df['Vardas'], df['Amzius'], color='green')
# plt.xlabel('Vardas')
# plt.ylabel('Amzius')
# plt.title('Amzius pagal vardus')
#
# plt.show()
#
# df.head(2)
# df.tail()
