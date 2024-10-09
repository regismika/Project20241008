# FUNKCIJOS
from random import random

# @@ -0,0 +1,59 @@


# arr = [1, 5, 10]
# sum = 0
# count = 0
# for i in arr:
#     count += 1
#     sum += i
# print(sum / count)


# arr2 = [7,9,1,1,6,684,16,6,8,105,0.5,68,0.5,3551,31,165,3]
#
# def avg(arr):
#     sum = 0
#     count = 0
#     for i in arr:
#         count += 1
#         sum += i
#     return sum / count
#
# print( avg(arr) )
# print( avg(arr2) )
#
# arr3 = [5,5,5,5,5,5,5,5,5,55,5]
#
# print(avg(arr3))



# def sayHi(): #nieko nepriima ir nieko negražina
#     print("hi")
#
# sayHi()
# sayHi()
# sayHi()
# sayHi()
# print(sayHi())
#
# def simPi(): #nieko nepriima, grazina skaiciu
#     return 3.14
#
# print( simPi() )
#
# def sayHiTo(name): #priima, bet nieko negražina
#     print(f'hi {name.upper()}')
#
# sayHiTo("Jonas")
# sayHiTo("Vilius")
# vardas = "Jurgis"
# sayHiTo(vardas)
#
# def intSum (a, b):#priima, gražina
#     return a + b
#
# result = intSum(16,36)
# print(result)

# 1. Sukurkite funkciją, kuri išvestų jūsų vardą ir kodėl pasirinkote
# programavimą. Iškvieskite šią funkciją tris kartus.
# def isvedimas():
#     for i in range(3):
#         print(vardas)
#         print(kodel_programavimas)
# vardas = "Regimantas"
# kodel_programavimas = "buvo smalsu"
# isvedimas()

# 2. Sukurkite funkciją, kuri išvestų 5 eilučių eilėraštį. Iškvieskite šią funkciją 5
# kartus.
# def eilerastis():
#     for i in range(5):
#         print("jei tu ramus")
#         print("Kada visi klejoja")
#         print("pamete galvas kaltina tave")
#         print("tiki savim kada kiti dvejoja")
#         print("ir ju dvejoniu nelaikai kalet")
# eilerastis()

# 3. Sukurkite tris funkcijas, kur kiekviena išvestų skirtingus tekstus. Iškvieskite
# visas tris funkcijas po vieną kartą.
# def pasisveikinimas():
#     print("Labas")
# def paros_metas():
#     print("vakaras")
# def ka_veiki():
#     print("ka tu ka vakare?")
# pasisveikinimas()
# paros_metas()
# ka_veiki()

# 4. Sukurkite dvi funkcijas, kur vienoje būtų viena teksto eilutėje, kitoje kita.
# Sukurkite trečią funkciją, kuri iškviestų pirmas dvi funkcijas. Iškvieskite šią
# trečiąją funkciją už visų funkcijų ribų

# def tekstas1():
#     return "Pingvinas"  # Naudojame return, kad grąžintume tekstą
#
# def tekstas2():
#     return "negyvena Afrikoje"  # Taip pat grąžiname tekstą
#
# def sujungti_tekstai():
#     print(tekstas1() + " " + tekstas2())  # Sujungiame grąžintus tekstus
#
# tekstas1()
# tekstas2()
# sujungti_tekstai()

# 5. Sukurkite funkciją, kurios viduje sugeneruotumėte du atsitiktinius
# skaičius. Funkcijoje suskaičiuokite ir išveskite šių dviejų skaičių sumą,
# kartu išvedant ir patį atliekamą veiksmą (pvz 7 + 2 = 9). Iškvieskite šią
# funkciją keletą kartų.
# import random
#
# def atsitiktiniu_skaiciu_suma():
#     skaicius1 = random.randint(1, 10)  # Generuojame du atsitiktinius skaičius nuo 1 iki 10
#     skaicius2 = random.randint(1, 10)
#
#     suma = skaicius1 + skaicius2
#     print(f"{skaicius1} + {skaicius2} = {suma}")
# for i in range(3):                  # Iškviečiame funkciją keletą kartų
#     atsitiktiniu_skaiciu_suma()

# 6. Sukurkite ir iškvieskite funkciją, kurioje kintamuosiuose būtų saugoma
# informacija apie policininką (vardas, pavardė, amžius, alga, etatas,
# specializacija). Išveskite šią informaciją suformatuotai (pavyzdžiui įterpkite
# į sakinį, ar išveskite sąrašu ar pan.).

# def saugoti_informacija(vardas, pavarde, amzius, alga, etatas, specializacija):
#     informacija = {
#         "Vardas": vardas,
#         "Pavardė": pavarde,
#         "Amžius": amzius,
#         "Alga": alga,
#         "Etatas": etatas,
#         "Specializacija": specializacija
#     }
#     return informacija
#
# rezultatas = saugoti_informacija("Jonas", "Trijonis", "25", "2000", "patrulis", "Viešoji tvarka")
#
# print(f"Informacija apie asmenį:\n Vardas: {rezultatas['Vardas']}\n Pavardė: {rezultatas['Pavardė']}\n Amžius: {rezultatas['Amžius']} metai\n Alga: {rezultatas['Alga']} EUR\n Etatas: {rezultatas['Etatas']}\n Specializacija: {rezultatas['Specializacija']}")
# print(f"{rezultatas['Vardas']} {rezultatas['Pavardė']} yra {rezultatas['Amžius']} metų amžiaus, dirba kaip {rezultatas['Etatas']}, specializuojasi {rezultatas['Specializacija']}, ir uždirba {rezultatas['Alga']} EUR per mėnesį.")


# 7. Sukurkite funkciją, kuri išvestų 10 atsitiktinių skaičių. Po visų išvestų
# skaičių turėtų padėti tuščią eilutę. Šią funkciją iškvieskite 5 kartus.

import random
# def udz7a():
#     random_skaiciai = []
#     for i in range(10):
#         random_skaiciai.append(random.randint(1,50))
#     print(f'{random_skaiciai} \n')
#
# for i in range(5):
#     udz7a()
#
#
# print("------------------")
# def uzd7():
#     for i in range(10):
#         print(random.randint(1, 50))
#
# for i in range(0,5):
#     uzd7()

# 8. Sukurkite funkciją, kuri išvestų atsitiktinį skaičių. Už funkcijos ribų
# sukurkite ciklą, kurį būtų vykdomas 10 kartų. Iškvieskite sukurtą funkciją cikle. Turėtumėte pamatyti 10 atsitiktinių skaičių.

# def iskviesti_skaiciu():
#     random_skaicius = []
#     for i in range(1):
#         random_skaicius.append(random.randint(1, 50))
#     print(f'{random_skaicius}')
# for i in range(10):
#         iskviesti_skaiciu()

# 9. Sukurkite funkciją pasisveikinimui, šiai funkcijai per argumentus
# perduokite vardą, funkcijoje išveskite tekstą labas ir gautą vardą.
# Sukurkite kitą funkciją, kuri irgi per argumentus gautų vardą, tačiau
# pasakytų 'viso gero' ir patį vardą. Ne funkcijose susikurkite kintamąjį
# vardui saugoti ir įrašykite vardą. Iškvieskite abi funkcijas, perduodant
# kintamąjį joms.

# def pasisveikinimo_funkcija(vardas):
#     print('labas', vardas)
#
# def atsisveikinimas(vardas):
#     print('viso gero', vardas)
#
# vardas = "Marius"
# pasisveikinimo_funkcija(vardas)
# atsisveikinimas(vardas)

# 10.Sukurkite funkciją, kuriai perduotumėte du skaičius. Ši funkcija turi rasti
# kuris skaičius yra didesnis ir išvesti gautą atsakymą, o jei skaičiai lygūs -
# tuomet išvesti, kad skaičiai lygūs. Iškvieskite šią funkciją keletą kartų,
# duodant skirtingus skaičius.


# 11. Sukurkite funkciją, kuri per argumentus gautų automobilių duomenis
# (markė, modelis, gamybos metai, darbinis tūris). Ši funkcija turėtų šiuos
# duomenis išvesti kaip nors gražiai formatuotai. Iškvieskite šią funkciją du
# kartus, perduodant skirtingus duomenis jai.
# 12).Sukurkite funkciją sumai skaičiuoti, ši funkcija per argumentus turėtų
# gauti du skaičius, bei išvesti patį veiksmą kartu su atsakymu (pvz 7 + 5 =
# 12). Sukurkite tokias pačias funkcijas skirtumui, sandaugai ir dalmeniui
# rasti. Sukurkite dar vieną funkciją, kuri sugeneruotų du atsitiktinius
# skaičius, bei iškviestų kitas 4 funkcijas, perduodant joms sugeneruotus
# skaičius. Šią bendrąją funkciją iškvieskite keletą kartų.