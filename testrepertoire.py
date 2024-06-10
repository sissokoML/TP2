while True:
    print("Menue Principale")
    print("1.ajouter un contact ")
    print("2.lister un contact ")
    print("3.modifier un contact ")
    print("4.supprimer un contact")
    print ("5.rechercher un contact ")
    print("6.appuyer sur 6 pour quiter")
    choice==int(input("donner votre choix s'il vous plait "))
    if choice==6:
        break
    elif choice==1:
        print("bienvenue dans la tables ajouter un contact")
        ajouter_un_contact()
    elif choice==2:
        print("bienvenue dans la tables lister un contact ")
        lister()
    elif choice==3:
        print("bienvenue dans la tables modifier un contact")
        modifier()
    elif choice==4:
        print("bienvenue dans la tables supprimer un contact") 
        supprimer()
    else choice==5:
        print ("bienvenue dans la  tables recherche de contact ")
        recherche()    
