Lorem ibsum generátor
    
    Co to vlastně je?
        Lorem ipsumje označen proužívaný v grafickém designu a navrhování jako demonstrativní 
        výplňový text při vytváření pracovních ukázek grafických návrhů (např. fontů nebo 
        rozvržení časopisů či HTML stránek). 
    
    Popis mého pokusu o vytvoření vlastního Lorem ibsum generátoru v krocích:
        
        1. část programu (SEZNAMY (písmena, slabiky)+ JEJICH PRVĚPODOBNOSTI + POČTY)
            Tato část, jak již název napovídá, obsahuje veškerá se seznamy, 
            pravděpodobnosti a počty slabik ve slově, slov ve větách a vět v odstavci:
                
                A)SLABIK – zde jsme čerpal ze stránky -> https://nlp.fi.muni.cz/cs/FrekvenceSlovLemmat <- 
                kde se nachází frekvence písmen, bigramů, trigramů, délka slov; vybral jsem si odsud tedy 
                pár českých slabik, které se v českém jazyce vyskytují a přiřadil jsme jim dané pravděpodobosti UKÁZKA: 
                (V kódu řádky: 8, 10)
                
                SLABIKY
                ['a','á','e','é','i','í','y','ý','o','ó','u','st', 'ní', 'po', 'ov', 'ro', 'en', 'na',
                 'je', 'pr', 'te', 'le', 'ko', 'ne', 'od', 'ra', 'to', 'ou', 'no', 'la', 'li', 'ho',
                 'pro', 'ost', 'sta', 'pře', 'ter', 'ení', 'ova', 'pod', 'kte', 'pra', 'ého', 'sti', 
                 'řed', 'kon', 'nos', 'ick', 'ová', 'při', 'sou', 'ist', 'edn']
                PRAVDĚPODOBNOSTI
                [66,21,78,11,45,31,17,9,82,1,31,66, 21, 16, 16, 10, 36, 1, 78, 11, 14, 4, 3, 12, 
                10, 45, 31, 19, 37, 40, 32, 66, 1, 82, 1, 34, 1, 39, 11, 46, 8, 55, 1, 31, 1, 6, 
                43, 1, 1, 17, 9, 21, 10]

                B)Počet slabik VE VĚTĚ – zde jsem si zvolil, že v každém slově se bude
                 vyskytovat 1 nebo až 4 slabiky (řádky v kódu: 15,16), kdy nejvíce se vyskytují slova 
                 se 3 slabikami dále se 2 slebikami se 4 slabikami a nejméně s 1 slabikou
                 (pravděpodobnosti řádky v kódu: 19–25)



