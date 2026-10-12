#kirjuta programm, mis küsib kasutajalt eesnime ja tervitab teda

#Algus
#Küsi kasutajalt eesnimi
#Salvesta väärtus muutujasse first_name
#Väljastab tervitust "Hello, (eesnimi)!"
#Lõpp


first_name=input("Palun sisesta oma eesnimi: ")
print("Hello, " + first_name + "!")

#f-string
print(f"Hello, {first_name}!")

#tehke nii ,et programm küsib kasutajalt eesnime ja perekonnanime ning tervitab teda terviknimega