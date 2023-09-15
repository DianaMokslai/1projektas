
import pandas as pd
import matplotlib.pyplot as plt

# duomenys = {'Vardas': ['Jonas', 'Ieva', 'Petras', 'Ona'],
#             'Amzius': [25, 28, 22, 30]
#             }
# df = pd.DataFrame(duomenys)
# # print(df)
#
# jaunesni = df[df['Amzius'] < 25]
# # print(jaunesni)
#
# vidutinis_amzius = df['Amzius'].mean()
# print(f'Vidutinis amzius: {vidutinis_amzius}')

# temperaturos = [24.5, 25.2, 23.8, 26.0, 22.5]
#
# sr = pd.Series(temperaturos)
#
# print(sr)

# Mazejancia tvarka
# temperaturos = [24.5, 25.2, 23.8, 26.0, 22.5]
#
# sr = pd.Series(temperaturos)
# serija_rikiavimas = sr.sort_values()
#
# print(serija_rikiavimas)

# Didejancia tvarka
# temperaturos = [24.5, 25.2, 23.8, 26.0, 22.5]
#
# sr = pd.Series(temperaturos)
# serija_rikiavimas = sr.sort_values(ascending = False)
#
# print(serija_rikiavimas)

# temperaturos = [24.5, 25.2, 23.8, 26.0, 22.5]
# sr = pd.Series(temperaturos)
# print(f"pirmas elementas: {sr[0]}")

# # # parodo tik vardus
# duomenys = {'Vardas': ['Jonas', 'Ieva', 'Petras', 'Ona'],
#             'Amzius': [25, 28, 22, 30]
#             }
# df = pd.DataFrame(duomenys)
# vardai = df['Vardas']
# print("Vardai: ")
# print(vardai)
# parodo vardus eilute
# duomenys = {'Vardas': ['Jonas', 'Ieva', 'Petras', 'Ona'],
#             'Amzius': [25, 28, 22, 30]
#             }
# df = pd.DataFrame(duomenys)
# # vardai = df['Vardas'].to_list()
# # print("Vardai: ")
# # print(vardai)

# jeigu noretume prideti nauja stulpeli i savo DataFrame
# duomenys = {'Vardas': ['Jonas', 'Ieva', 'Petras', 'Ona'],
#             'Amzius': [25, 28, 22, 30]
#             }
# df['Lytis'] = [['Vyras', 'Moteris', 'Vyras', 'Moteris']]
# df = pd.DataFrame(duomenys)
# print('Atnaujintas dataframe dsu nauju stulpeliu: ')
# print(df)
# duomenys = {'Vardas': ['Jonas', 'Ieva', 'Petras', 'Ona'],
#             'Amzius': [25, 28, 22, 30]
#             }
# df = pd.DataFrame(duomenys)
# vardai = df['Vardas']
# print("Vardai: ")
# print(vardai)


# plt.figure(figsize=(8,5))
# plt.bar(df['Vardas'], df['Amzius'], color='green')
# plt.xlabel('Vardas')
# plt.ylabel('Amzius')
# plt.title('Amzius pagal vardus')
# plt.show()
# df.head(2)
# df.tail()
# data = {'Miestas': ['Vilnius', 'Kaunas', 'KLaipeda', 'Mazeikiai'],
#         'Lytis': ['Vyras', 'Vyras', 'Moteris', 'Vyras'],
#         'Amzius': [25, 25, 22, 30, 24]
#         }
# data1 = pd.DataFrame(data)
#
# vidutinis_amzius_pagal_miesta = data1.groupby('Miestas')['Amzius'].sum()
# print(vidutini_amzius_pagal_miesta)


# Sukurkite Pandas DataFrame(4 miestai ir ju populiacija).
# Filtravimas ir paieška:
# a. Filtruokite miestus, kurių populiacija yra didesnė nei 200 000 žmonių.
# b. Raskite miestą, turintį mažiausią populiaciją.
# Duomenų grupavimas ir agregavimas:
# a. Pridėkite stulpelį "Šalis" prie ankstesnio DataFrame, kuriame nurodoma, kuri šalis priklauso kiekvienam miestui (pvz., "Lietuva").
# b. Grupuokite duomenis pagal "Šalis" stulpelį ir apskaičiuokite bendrą populiaciją kiekvienai šaliai.
# Duomenų rikiavimas:
# Rikiuokite miestus pagal populiaciją mažėjimo tvarka.

duomenys = {'Miestas': ['Vilnius', 'Kaunas', 'Klaipeda', 'Plunge'],
            'Populiacija': [500000, 295000, 152000, 33665]
            }
df = pd.DataFrame(duomenys)
miestai = df['Miestas']
populiacija = df['Populiacija']

populiacijos_filtravimas = df[df['Populiacija'] > 200000]
print(populiacijos_filtravimas)
print(df.min())


df['Salis'] = ['Lietuva', 'Lietuva', 'Italija', 'Lietuva']

print('Atnaujintas dataframe dsu nauju stulpeliu: ')
print(df)

Grupavimas = df.groupby('Salis')['Populiacija'].sum()
mazejancia_tvarka = df.sort_values(by='Populiacija')


plt.figure(figsize=(8,5))
plt.bar(df['Miestas'], df['Populiacija'], color='blue')
plt.xlabel('Miestas')
plt.ylabel('Populiacija')
plt.title('Populiacija pagal miestu pavadinimus')
plt.show()
