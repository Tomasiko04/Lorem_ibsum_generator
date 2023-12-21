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

     2. část programu PROGRAM

                1. Kontrola vstupní hodnoty:
                    Kontrolu vstupních hodnot má zde dvakrát:
                        1.1. maximální počet slov 
                        (Pokud uživatel zadá cokoli jiného než int nebo-li celé číslo bude se ho opakovaně ptát aby zadal maximální počet slov) 
                            (ověřování pomocí instrukce try: except  ValueError:)

                                Program vyzkouší, jestli vstupní hodnota je int, pokud ne zkusí jetli se nejedná o float (desetinné číslo), pokud se nejedná o float předpokládáme že se jedná o str (řetězec) -> následně program zistí kolik je slov v řetězci, pokud se v řetězci nenachází žádné číslo předpokládáme, že uživatel nezadal žádnou vstupní hodnotu.
řádky v kódu 47-51              while True:
                                # Maximální počet slov, který si může uživatel zvolit
                                zadane_max_pocet_slov = input("Zadej maximální počet slov: ")
                                try:
                                    max_pocet_slov = int(zadane_max_pocet_slov)
                                    .
                                    .
                                    .
                                    .
řádky v kódu 190-204            except ValueError:
                                    # Pokud převod na int selže, zkusíme převést na desetinné číslo (float)
                                    try:
                                        max_pocet_slov = float(zadane_max_pocet_slov)
                                        print(f"Zadali jste desetinné číslo: {max_pocet_slov}")
                                        
                                    except ValueError:
                                        # Pokud ani převod na float nebyl úspěšný, předpokládáme, že se jedná o řetězec (str)
                                        max_pocet_slov = str(zadane_max_pocet_slov)
                                        
                                        if len(max_pocet_slov) < 1:
                                            print("Nezadal jsi hodnotu.")
                                            
                                        else:
                                            print(f"Zadali jste řetězec: {max_pocet_slov}")    

                        1.2. zadávání ANO/NE při ukládání vygenrovyného textu
                            Pokud zde uživatel zadá něco jiného než ANO/NE program se ho bude pořád ptát na "Chcete váš soubor uložit(ANO/NE)?: ", pokud zadá ANO přejde se k dalšímu kroku tedy k ukládání (o tom více !!!!!!!!!!) pokud zadá ne program se spustí od začátku, tedy se uživatele zeptá "Zadej maximální počet slov: "
                            (ověření pomocí podminky if)

                            VYCHYTÁVKA: požil jsem funkci .lower() tzn. že všechny znaky na daném inputu převede na malá písmena, i když s jsou velké
řádky v kódu 169-171            while True:
                                    rozhodnuti=input("Chcete váš soubor uložit(ANO/NE)?: ").lower()
                                    if "ano" in rozhodnuti:
                                        .
                                        .
                                        .
                                        .                                                               
řádky v kódu 185-188                elif "ne" in rozhodnuti:
                                        break
                                    else:
                                        print("Zadali jste špatnou odpověď. Muíte dát ANO/NE.")

                2. Nastavování proměnných(po zadání vstupní hodnoty):

                    lorem_text=' ' =>proměnná do které se ukládají slova ze začátku prázdná

                    pocet_slov = 0              >
                    pocet_slov_1vete=0          >>
                                                >>> Z názvu proměnných snado poznáte jaké hodnoty se zde budou ukádat ze začátku jsou všechny nastaveny na 0 JSOU důležité protože díky nim poznáme kdy se má ukončit generování textu či čárky ve větě nebo konec slova či věty 
                    pocet_slov_1odstavec=0      >>
                    carka_ve_vete=0             >

                    Tyto proměnné naopak neříkají kdy má končit generování slovo či věty ALE nastavují délky vět,odstavců či výskyt čárek v souvětí
                    delka_vety=random.choices(slova_ve_vete, weights=pravdepodobnosti_veta, k=1)[0]                 
                    delka_na_odstavci=random.choices(slova_na_odstavci, weights=pravdepodobnosti_odstavci, k=1)[0]  
                    misto_carky=random.choices(carka,weights=pravdepodobnosti_carka, k=1)[0]   

                        např. za proměnnou misto_carky mi dosadí prvek ze seznamu, kde každý prvek má určitou váhu výsledku, kterou si nastavíme u proměnné weights= ,jelikož k=1 tj. počet vybraných prvků ze seznamu, musíme na konec přidat [0], aby byl získán opravdu jediný prvek z tohoto seznamu (random.choice jsem zde nezvolil, jelikož si zde nemohu přiřadit váhy výskytu jednotlivých prvků ze seznamu)

                3. 

                       while pocet_slov < max_pocet_slov:
----------------------------------------------------------------------
dokud  proměnná pocet_slov (zvětšuje se o 1 po kažém vygenerovaném slovu)< max_pocet_slov (nastavení uživatele)
tak se tyto 4 proměnná busou vždy zvětšovat o +1 
                            pocet_slov += 1
                            pocet_slov_1vete+=1
                            pocet_slov_1odstavec+=1
                            carka_ve_vete+=1
 --
 u proměnné delka_slova jsem zkusil použít random.choice s místo daným seznamem rozsah od do kde u maximální hodnoty jsem přídal +1 aby se max hodnota také zaznamenala                          
                            
                            delka_slova = random.choices(range(min_delka_slova, max_delka_slova + 1), weights=pravdepodobnosti_delky_slov, k=1)[0]
                        


--------------------------------------------------------------------


                4. Tato část programu zjišťuje jestli se jedná 1. slovo ve větě pokud ANO přiřadí proměnné slovo slabiky s danou váhou jejich výskytu a také využije proměnné delka_slova (nastavená výše) abychom měli daný počet slabik ve slově zde jsem již nepoužil [0] jelikož nevybírám jednu věc o nějaké váze výskytu ze seznamu

                VELKÉ PÍSMENO mi určuje  část kódu-> ' '.join([slovo.capitalize() if index == 0 else slovo for index, slovo in enumerate(slovo.split())]) <- kde 'slovo.split()' rozdělí vstupní text na seznam slov;
                                     'enumerate(slovo.split())'    tato část kódu vrací dvojice (index, slovo) pro každé slovo v seznamu (index je pořadové číslo slova a slovo je samo slovo)
                                    
                                    '[slovo.capitalize() if index == 0 else slovo for index, slovo in enumerate(text.split())]:' 
                                    Toto je seznamový výraz, který prochází každé slovo ve vstupním textu. Pokud je index (pořadové číslo slova) rovno 0 (první slovo), použije se metoda capitalize() na zvětšení prvního písmena slova, jinak zůstane slovo beze změny.

                                    ' '.join(...): Nakonec se používá metoda join(), aby se spojila upravená slova zpět do řetězce, kde jsou oddělena mezerami. Výsledek je přiřazen do proměnné novy_text

                    jakmile 




                            if pocet_slov_1vete==1:  #velké písmeno na začátku věty     
                                slovo = ''.join(random.choices(slabiky, weights=pravdepodobnosti_pismen, k=delka_slova))
                                
                                
                                nove_slovo= ' '.join([slovo.capitalize() if index == 0 else slovo for index, slovo in enumerate(slovo.split())])
                                lorem_text += nove_slovo + ' '

                            else:
                                slovo = ''.join(random.choices(slabiky, weights=pravdepodobnosti_pismen, k=delka_slova))
                                lorem_text += slovo + ' '
                                
                                if carka_ve_vete % misto_carky == 0 and pocet_slov_1vete % delka_vety != 0 and pocet_slov_1odstavec % delka_na_odstavci != 0:
                                    
                                    
                                    lorem_text =lorem_text.rstrip() + ', '
                                    carka_ve_vete=0
                                    misto_carky=0
                                    misto_carky=random.choices(carka,weights=pravdepodobnosti_carka, k=1)[0]
                            
                            
                            
                            
                            
                            
                            # Přidá tečku každých 5,10,14,16,20 slov (jestliže je pocet_slov_1vete děliteny beze zbytku) a přidání mezery na začátku nové věty
                                #POKUD bych odstranil ''and pocet_slov_1odstavec % 50 != 0'' tak by se mi tečka za větou na konci nějakého odstavce vygenerovat 2x

                            
                            
                            
                            
                            if pocet_slov_1vete % delka_vety == 0 and pocet_slov <= max_pocet_slov and pocet_slov_1odstavec % delka_na_odstavci != 0:
                                lorem_text = lorem_text.rstrip() + '. ' #+ slovo.upper() + ' '
                                #lorem_text += '. ' + slovo.upper() + ' '
                                
                                delka_vety=0                    #[5,10,14,16,20]           
                                pocet_slov_1vete=0
                                
                                delka_vety=random.choices(slova_ve_vete, weights=pravdepodobnosti_veta, k=1)[0]
                                
                                

                            # Přidá odstavec po každých 50,60,70 slovech
                            if pocet_slov_1odstavec % delka_na_odstavci == 0 and pocet_slov <= max_pocet_slov:
                                lorem_text = lorem_text.rstrip()
                                lorem_text += '.\n\n' # Odstavec
                                lorem_text += ' ' #odskok
                                
                            
                                delka_vety=0                    #[5,10,14,16,20]
                                pocet_slov_1vete=0
                                delka_na_odstavci=0             #[50,60,70]
                                pocet_slov_1odstavec=0

                                delka_vety=random.choices(slova_ve_vete, weights=pravdepodobnosti_veta, k=1)[0]
                                delka_na_odstavci=random.choices(slova_na_odstavci, weights=pravdepodobnosti_odstavci, k=1)[0]
                            



                                #if pocet_slov != max_pocet_slov: #velké slovo na začátku odstavce
                                #    lorem_text +=slovo.upper()+ ' '



                            #tečka na koneci generování
                            #if lorem_text != '.':
                            #    lorem_text = lorem_text.rstrip()
                            #    lorem_text += '. '
                                    
                            if pocet_slov_1vete % delka_vety != 0 and pocet_slov_1odstavec % delka_na_odstavci != 0:
                                lorem_text = lorem_text.rstrip() + '. '
                                print(lorem_text)
                            else:
                                print(lorem_text)


