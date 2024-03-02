from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Cm, Inches, Mm, Emu
import random
import datetime
from readFromText import IF, ICE, ZIP, PHONE, EMAIL, ADDRESS, NAME, RC, WEBSITE 
#import matplotlib.pyplot as plt
#Import template document


#Render automated report
def generate():
    # FACTURE
    facture = "0002"

    # AMOUNTS
    taux = 0.2
    today = datetime.datetime.now().strftime('%d') + '/' + datetime.datetime.now().strftime('%m') + '/' + datetime.datetime.now().strftime('%Y')
    today_en = datetime.datetime.now().strftime('%m') + '/' + datetime.datetime.now().strftime('%d') + '/' + datetime.datetime.now().strftime('%Y')
    template = DocxTemplate(f'Templates/{docType}.docx')


    # Declare template variables
    context = {
    
    # Company Info
    "C_NAME": NAME,
    "C_ADDRESS": ADDRESS,
    "C_PHONE": PHONE,
    "C_EMAIL": EMAIL,
    "C_RC": RC,
    "C_ZIP": ZIP,
    "C_ICE": ICE,
    "C_IF": IF,
    "C_WEBSITE": WEBSITE,

    #Client Info
    'Client': client,
    'Adresse': adress,
    'Ville': ville,
    'Email': email,
    'Phone': num,
    'ICE': ice ,
    'Facture': facture,
    'Price': price,
    'TVA': round(taux * int(price), 3),
    'Total': round(taux * int(price) + int(price), 3),
    'French_date': today,

    "ID": "id",
    'tp': "",
    'rc': "",
    'if': ""
    #rc if tp

    }
    template.render(context)
    template.save(f'Generated/{docType}_{facture}.docx')

def main():
    global ville, adress, price , ice , email, num, rc , i_f , tp,  client, id, docType
    
    choice = 9
    docChoice = 1
    language="en"
    while choice != 0:

        print("\n\n ************** Factures Générateur v1 **************")
        print("\n\n 1) Crée un document")
        print(" 2) Génerer un document")
        print(" 3) Changer la langue")
        choice = int(input("\n$ "))

        if choice == 1: # Adding values

            print("\n\n Selectionner le type:")
            print("     1) Facture")
            print("     2) Devis")
            docChoice = int(input("$ "))
            if docChoice == 1:
                docType= "facture"
            else: 
                docType= "devis"

            #add id
            client = input("\n\nClient: ")
            adress= input("Adress: ")
            ville= input("Ville: ")
            email = input("Email: ")
            num = input("Telephone: ")

            #Personne Morale
            ice = input("ICE: ")

            print("Add more? (y/n)")
            additionalInfo = str(input())
            if additionalInfo == "y":
                rc = input("RC: ")
                i_f = input("IF: ")
                tp= input("TP: ")
                id= input("ID: ")

            #Elements
            price = input("Prix HT: ")   

        if choice == 2: # Generate
            print(f"\nClient: {client} \nAddresse: {adress} \nVille: {ville} \nEmail: {email} \nTélépphone: {num}")
            print("\n\n 1) Génerer")
            print(" 2) Modifier \n")
            decision = int(input("$"))

            if decision == 1:
                generate()

        if choice == 3:
            print("\n\n Selectionner la langue:")
            print("     1) Francais")
            print("     2) Anglais")
            langChoice = int(input("$ "))
            if langChoice == 1:
                language="fr"
            else: language="en"

if __name__ == "__main__":
    main()


#TODO 
# - Invoce number incrementation
# - languages
# - convert docx to pdf
# - upload to drive

# Tutorial : https://plainenglish.io/blog/how-to-generate-automated-word-documents-with-python-d6b7f6d3f801