import sqlite3
import pandas



db = sqlite3.connect("contactbook.db")
cursor = db.cursor()

try:
    cursor.execute("CREATE TABLE Contacten (ID INTEGER PRIMARY KEY NOT NULL, naam VARCHAR(50), leeftijd smallint UNSIGNED, adres VARCHAR(50), email VARCHAR(100))")
except sqlite3.OperationalError:
    pass

def adresboek():
    herhalen = True
    while herhalen:
        keuze = input("Wat wenst u te doen? [B]ekijken/[A]anpassen/[T]oevoegen of [S]luiten: ").lower()
        if keuze == "bekijken" or keuze == "b":
            contacts = cursor.execute('select * from Contacten')
            df = pandas.DataFrame(contacts, columns=["ID", "Naam", "Leeftijd", "Straat", "Email"])
            if df.empty:
                print("Geen contacten aanwezig")
            else:
                print(df)
            # for i in cursor:
            #     print(i)
        elif keuze == 'aanpassen' or keuze == 'a':
            change_inputs()
            pass
        elif keuze == "toevoegen" or keuze == "t":
            add_user()
            pass
        else:
            herhalen = False


def change_inputs():
    contacts = cursor.execute('select * from Contacten')
    df = pandas.DataFrame(contacts, columns=["ID", "Naam", "Leeftijd", "Straat", "Email"])
    if df.empty:
        print("Geen contacten aanwezig")
    else:
        print(df)
        identiteit = input("Welk id wil je aanpassen?: ")
        aanpassing = input("Wat wil je doen? [D]elete/[E]dit : ").lower()
        if aanpassing == "edit" or aanpassing == 'e':
            veranderen = input('Wat wens je te wijzigen? [N]aam/ [L]eeftijd /[A]dres / [E]mail?: ').lower()
            if veranderen == 'l' or veranderen == 'leeftijd':
                leeftijd_aanpassing = input("Leeftijd?: ")
                command = "UPDATE Contacten SET leeftijd = (?) WHERE ID = (?)"
                togheter = (leeftijd_aanpassing, identiteit)
                cursor.execute(command, togheter)
                db.commit()
            if veranderen == 'n' or veranderen == 'naam':
                naam_aanpassing = input("Naam?: ")
                command_naam = 'UPDATE Contacten SET naam = (?) WHERE ID = (?)'
                togheter_naam = (naam_aanpassing, identiteit)
                cursor.execute(command_naam, togheter_naam)
                db.commit()            
            if veranderen == 'a' or veranderen == 'adres':
                adres_aanpassing = input("Adres?: ")
                command_adres = 'UPDATE Contacten SET adres = (?) WHERE ID = (?)'
                togheter_adres = (adres_aanpassing, identiteit)
                cursor.execute(command_adres, togheter_adres)
                db.commit()            
            if veranderen == 'e' or veranderen == 'email':
                email_aanpassing = input("Email?: ")
                command_email = 'UPDATE Contacten SET email = (?) WHERE ID = (?)'
                togheter_email = (email_aanpassing, identiteit)
                cursor.execute(command_email, togheter_email)
                db.commit()
        elif aanpassing == "delete" or aanpassing == 'd':
            delete_user(identiteit)
        else:
            pass


def delete_user(x):
    command_delete = 'DELETE FROM Contacten WHERE ID = (?)'
    togheter_delete = (x,)
    cursor.execute(command_delete, togheter_delete)
    db.commit()
    print("persoon is verwijderd")

def add_user():
    naam = input("Naam: ")
    leeftijd = input("Leeftijd: ")
    adres = input("Adres: ")
    email = input("Email: ")
    cursor.execute("INSERT INTO Contacten (naam, leeftijd, adres, email) VALUES (?,?,?,?)", (naam, leeftijd, adres, email))
    db.commit()
    return


adresboek()
print("Bedankt vaarwel!")
db.close()