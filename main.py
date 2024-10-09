# FUNKCIJOS

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
# for _ in range(3):                  # Iškviečiame funkciją keletą kartų
#     atsitiktiniu_skaiciu_suma()

# 6. Sukurkite ir iškvieskite funkciją, kurioje kintamuosiuose būtų saugoma
# informacija apie policininką (vardas, pavardė, amžius, alga, etatas,
# specializacija). Išveskite šią informaciją suformatuotai (pavyzdžiui įterpkite
# į sakinį, ar išveskite sąrašu ar pan.).
# def saugoti_informacija(vardas, pavarde, amzius, alga, etatas, specializacija):
#     informacija = {
#         "Vardas": vardas,
#         "Pavarde": pavarde,
#         "Amžius": amzius,
#         "alga": alga,
#         "etatas": etatas,
#         "specializacija": specializacija
#     }
#     return informacija
# rezultatas = saugoti_informacija("Jonas", "Trijonis", "25", "2000", "patrulis", "Viesoji tvarka")
# print(rezultatas)


# 7. Sukurkite funkciją, kuri išvestų 10 atsitiktinių skaičių. Po visų išvestų
# skaičių turėtų padėti tuščią eilutę. Šią funkciją iškvieskite 5 kartus.
# 8. Sukurkite funkciją, kuri išvestų atsitiktinį skaičių. Už funkcijos ribų
# sukurkite ciklą, kurį būtų vykdomas 10 kartų. Iškvieskite sukurtą funkciją cikle. Turėtumėte pamatyti 10 atsitiktinių skaičių.