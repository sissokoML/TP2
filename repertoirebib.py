from os import remove
from os import renames
def ajouter_un_contact():
    nom=input("donner votre nom s'il vous plait ")
    prenom=input("donner votre prenom s'il vous plait ")
    age=input("donner votre age s'il vous plait ")
    tel=input("donner votre contact s'il vous plait ")
    contact=open("contact.txt" ,"w", encoding="utf-8")
    contact=open("contact.txt" ,"a", encoding="utf-8")
    contact.write(nom +"\n")
    contact.write(prenom +"\n")
    contact.write(age +"\n")
    contact.write(tel +"\n")
    contact.close()
def lister_un_contact():
    contact=open("contact.txt" ,"r", encoding="utf-8") 
    pipa=contact
    for lire in pipa:
        print(lire)
def modifier_un_contact():
    print("1.modifier un nom ")
    print("2.modifier un prenom ")    
    print("3.modifier un numero de tel ")
    choix=int(input("donner votre choix ")) 
    if choix==1:
        annom=input("donner l'ancien nom a modifier")
        novnom=input("donner le nouveaux nom a modifier")
        contact=open("contact.txt","r", encoding="utf-8")
        tempon=open("temp.txt","w", encoding="utf-8")
        lignom=contact.readline()
        ligprenom=contact.readline()
        ligtel=contact.readline()
        while lignom!="" or ligprenom!="" or ligtel!="":
            if lignom==annom:
                tempon.write(novnom+"\n")
                tempon.write(ligprenom+"\n")
                tempon.write(ligtel+"\n")
            else:
                tempon.write(lignom+"\n")
                tempon.write(ligprenom+"\n")
                tempon.write(ligtel+"\n")
            lignom=contact.readline()
            ligprenom=contact.readline()
            ligtel=contact.readline()    
        contact.close()    
        tempon.close()
        remove("contact.txt")
        renames("temp.txt","contact.txt")


    elif choix==2:
        anprenom=input("donner l'ancien nom a modifier")
        novprenom=input("donner le nouveaux nom a modifier")
        contact=open("contact.txt","r", encoding="utf-8")
        tempon=open("temp.txt","w", encoding="utf-8")
        lignom=contact.readline()
        ligprenom=contact.readline()
        ligtel=contact.readline()
        while lignom!="" or ligprenom!="" or ligtel!="":
            if ligprenom==anprenom:
                tempon.write(lignom+"\n")
                tempon.write(novprenom+"\n")
                tempon.write(ligtel+"\n")
            else:
                tempon.write(lignom+"\n")
                tempon.write(ligprenom+"\n")
                tempon.write(ligtel+"\n")
            lignom=contact.readline()
            ligprenom=contact.readline()
            ligtel=contact.readline()    
        contact.close()    
        tempon.close()
        remove("contact.txt")
        renames("temp.txt","contact.txt")
def supprimer_un_contact():
    nom_contact=input("donner le nom du contact a supprimer")
    contact=open("contact.txt" ,"r", encoding="utf-8")
    tempon=open("temp.txt","w", encoding="utf-8")
    lignom=contact.readline()
    ligprenom=contact.readline()
    ligtel=contact.readline()
    while lignom!="" or ligprenom!="" or ligtel!="":
        print(lignom)
        print(nom_contact)
        if (lignom.strip()!=nom_contact):
            tempon.write(lignom+"\n")
            tempon.write(ligprenom+"\n")
            tempon.write(ligtel+"\n")
       
        lignom=contact.readline()
        ligprenom=contact.readline()
        ligtel=contact.readline()    
    contact.close()    
    tempon.close()
    remove("contact.txt")
    renames("temp.txt","contact.txt")

        