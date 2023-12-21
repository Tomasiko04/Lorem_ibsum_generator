Lorem ibsum generátor
    
    Co to vlastně je?
        Lorem ipsumje označen proužívaný v grafickém designu a navrhování jako demonstrativní 
        výplňový text při vytváření pracovních ukázek grafických návrhů (např. fontů nebo 
        rozvržení časopisů či HTML stránek). 
    
    Popis mého pokusu o vytvoření vlastního Lorem ibsum generátoru v krocích:
        
        1. část programu (SEZNAMY (písmena, slabiky)+ JEJICH PRVĚPODOBNOSTI + POČTY)
            Tato část, jak již název napovídá, obsahuje veškerá se seznamy, 
            pravděpodobnosti a počty slabik ve slově, slov ve větách a vět v odstavci:
                
                A)SLABIK – zde jsme čerpal ze stránky 
                -> https://nlp.fi.muni.cz/cs/FrekvenceSlovLemmat <- 
                kde se nachází frekvence písmen, bigramů, trigramů, délka slov;
                vybral jsem si odsud tedy pár českých slabik, které se
                v českém jazyce vyskytují a přiřadil jsme jim dané pravděpodobosti 
                UKÁZKA: 
                (V kódu řádky: 8, 10)
                
                SLABIKY
                ['a','á','e','é','i','í','y','ý','o','ó','u','st', 'ní', 'po', 'ov',
                 'ro', 'en', 'na', 'je', 'pr', 'te', 'le', 'ko', 'ne', 'od', 'ra', 
                 'to', 'ou', 'no', 'la', 'li', 'ho', 'pro', 'ost', 'sta', 'pře', 
                 'ter', 'ení', 'ova', 'pod', 'kte', 'pra', 'ého', 'sti', 
                 'řed', 'kon', 'nos', 'ick', 'ová', 'při', 'sou', 'ist', 'edn']
                PRAVDĚPODOBNOSTI
                [66,21,78,11,45,31,17,9,82,1,31,66, 21, 16, 16, 10, 36, 1, 78, 
                11, 14, 4, 3, 12, 10, 45, 31, 19, 37, 40, 32, 66, 1, 82, 1, 34, 
                1, 39, 11, 46, 8, 55, 1, 31, 1, 6, 
                43, 1, 1, 17, 9, 21, 10]

                B)Počet slabik VE SLOVĚ 
                Zde jsem si zvolil, že v každém slově se bude vyskytovat 1 nebo až 4 slabiky 
                (řádky v kódu: 15,16), kdy nejvíce se vyskytují slova 
                se 3 slabikami dále se 2 slebikami se 4 slabikami a nejméně s 1 slabikou.
                (pravděpodobnosti řádky v kódu: 19–25)

                    # Minimální a maximální délka slova
                    min_delka_slova = 1
                    max_delka_slova = 4

                    # Pravděpodobnosti pro délky slov od 1 do 10
                    pravdepodobnosti_delky_slov = [
                        5,  # délka slova 1
                        10,  # délka slova 2
                        15,  # délka slova 3
                        8,  # délka slova 4

                    ]

                C)Počet slov VE VETĚ
                Zde jsem si zvolil, že v každé větě se budu vyskytovat 5, 10, 14, 16, 20 slov (řádky v kódu: 31,32), kdy nejvíce se vyskytují věty 
                s 16 slovy, dále pak se 14 slovy, poté 20 slovy, následně s 10 slovy a nejméně s 5 slovy.

                slova_ve_vete=[5,10,14,16,20]
                pravdepodobnosti_veta=[2,5,9,12,8]

                D)Počet slov NA ODSTAVCI
                Zde jsem si zvolil, že v každé odstavci se budu vyskytovat 50, 60, 70 slov (řádky v kódu: 37,38), kdy nejvíce se vyskytují odstavce 
                s 60 slovy, dále pak s 50 slovy a nejméně se 70 slovy.

                slova_na_odstavci=[50,60,70]
                pravdepodobnosti_odstavci=[9,12,8]

                VYCHYTÁVKA: Každý začátek odstavce je odsazen, akorát při spuštění v PYTHONU to nejde vždy vidět, proto doporučuji si daný text otevřít v textovém souboru, do kterého Vám tento text PYTHON uloží, pokud budete na konci chtít.  

                POZOR: Jelikož každý odstavec končí po 50, 60 nebo po 70 slovech většinou se stane, že poslední věta neobsahuje předem daný počet slov VE VĚTĚ (počet slov ve větě je zmíněn v části 1 v bodě c))

                VÝVOJ: Ze začátku jsem si zvolil, že se mi odstavce budou dělit po každých 50 slovech -> to se mi zdálo jednoduché tak jsem určil že v každém odstavci bude 50, 60 nebo 70 slov

                E)Čárka ve větě
                Nakonec mě ještě napadlo, že by generátor mohl generovat i čárky v souvětí. Generátor postujpuje tak, že za každými 20, 45 nebo 10 solovy napíše čárku. nejvíce se vyskytne čárka po 20 slovech, dále pak po 45 slovecha a nejméně po 10 slovech(pravděpodobnost je čistě můj odhad)
                
                carka=[10,20,45]
                pravdepodobnosti_carka=[10,15,13]
                
                VYCHYTÁVKA:
                V části PROGRAM jsem část s čárkami v souvětí ošetřil tak, že se čárka nevyskytne před tečkou na konci věty či před 1. slovem ve větě.

                
                




