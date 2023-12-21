import random
import string

#######################  SEZNAMY (písmena, slabiky)+ JEJICH PRVĚPODOBNOSTI  ###############################
##
# Slabiky
#nedával jsme ->ú<- protože kdyby, protože by se mohlo vyskytovat i tam kde nechci to samé platí i o ->ů<-
slabiky = ['a','á','e','é','i','í','y','ý','o','ó','u','st', 'ní', 'po', 'ov', 'ro', 'en', 'na', 'je', 'pr', 'te', 'le', 'ko', 'ne', 'od', 'ra', 'to', 'ou', 'no', 'la', 'li', 'ho', 'pro', 'ost', 'sta', 'pře', 'ter', 'ení', 'ova', 'pod', 'kte', 'pra', 'ého', 'sti', 'řed', 'kon', 'nos', 'ick', 'ová', 'při', 'sou', 'ist', 'edn']
# Pravděpodobnosti pro každé písmeno abecedy
pravdepodobnosti_pismen = [66,21,78,11,45,31,17,9,82,1,31,66, 21, 16, 16, 10, 36, 1, 78, 11, 14, 4, 3, 12, 10, 45, 31, 19, 37, 40, 32, 66, 1, 82, 1, 34, 1, 39, 11, 46, 8, 55, 1, 31, 1, 6, 43, 1, 1, 17, 9, 21, 10]


##POCET SLABIK
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



##
# Počet slov VE VĚTĚ
slova_ve_vete=[5,10,14,16,20]
pravdepodobnosti_veta=[2,5,9,12,8]


##
# Počet slov NA ODSTAVCI
slova_na_odstavci=[50,60,70]
pravdepodobnosti_odstavci=[9,12,8]

##
# Čárka ve větě
carka=[10,20,45]
pravdepodobnosti_carka=[10,15,13]


######################################  PROGRAM  #######################################################
while True:
    # Maximální počet slov, který si může uživatel zvolit
    zadane_max_pocet_slov = input("Zadej maximální počet slov: ")
    try:
        max_pocet_slov = int(zadane_max_pocet_slov)

        # Generování lorem ipsum textu s využitím pravděpodobností pro délky slov a pravděpodobností pro písmena
        lorem_text = ' '
        pocet_slov = 0

        pocet_slov_1vete=0
        pocet_slov_1odstavec=0

        carka_ve_vete=0

        delka_vety=random.choices(slova_ve_vete, weights=pravdepodobnosti_veta, k=1)[0]

        delka_na_odstavci=random.choices(slova_na_odstavci, weights=pravdepodobnosti_odstavci, k=1)[0]

        misto_carky=random.choices(carka,weights=pravdepodobnosti_carka, k=1)[0]

        while pocet_slov < max_pocet_slov:
            
            pocet_slov += 1
            
            pocet_slov_1vete+=1
            pocet_slov_1odstavec+=1

            carka_ve_vete+=1
            
            
            delka_slova = random.choices(range(min_delka_slova, max_delka_slova + 1), weights=pravdepodobnosti_delky_slov, k=1)[0]
            """
            if pocet_slov_1odstavec==1  and pocet_slov_1vete !=1:  #velké slovo na odstavce kromě PRVNÍHO   
                slovo = ''.join(random.choices(slabiky, weights=pravdepodobnosti_pismen, k=delka_slova)).upper()
                lorem_text += slovo + ' '
                

            if pocet_slov_1vete==1:  #velké slovo na začátku věty     
                slovo = ''.join(random.choices(slabiky, weights=pravdepodobnosti_pismen, k=delka_slova)).upper()
                lorem_text += slovo + ' '

            else:
                slovo = ''.join(random.choices(slabiky, weights=pravdepodobnosti_pismen, k=delka_slova))
                lorem_text += slovo + ' '
            """



            """
            if pocet_slov_1odstavec==1  and pocet_slov_1vete !=1:  #velké písmeno na odstavce kromě PRVNÍHO   
                slovo = ''.join(random.choices(slabiky, weights=pravdepodobnosti_pismen, k=delka_slova))
                nove_slovo= ' '.join([slovo.capitalize() if index == 0 else slovo for index, slovo in enumerate(slovo.split())])
                lorem_text += nove_slovo + ' '
            """    
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
        
#####   UKLÁDÁNÁ SOUBORU   #####
                    
        while True:
            rozhodnuti=input("Chcete váš soubor uložit(ANO/NE)?: ").lower()
            if "ano" in rozhodnuti:
                # Vygenerování textu
                generated_text = lorem_text

                # Název souboru, do kterého chcete zapsat text
                file_name = input("Napište název vašeho vygenerovaného textu: ")

                # Otevření souboru v režimu zápisu (w - write)
                with open(file_name, "w", encoding="utf-8") as file:
                    # Zápis textu do souboru
                    file.write(generated_text)
    
                print(f"Text byl úspěšně zapsán do souboru {file_name}.")
                break
            elif "ne" in rozhodnuti:
                break
            else:
                print("Zadali jste špatnou odpověď. Muíte dát ANO/NE.")

    except ValueError:
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

