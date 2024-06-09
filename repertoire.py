from repertoirebib import*
while True:
    print("############MENUE PRINCIPALE ##########")
    print("1.ajouter un contact ")
    print("2.lister un contact")
    print("3.modifier un contact ")
    print("4.supprimer un contact ")
    print("5.rechercher un contact par son nom")
    choice=int(input("donner votre choix "))
    if choice==6:
        break
    elif choice==1:
        print("bienvenue dans la partie ajouter un contact") 
        ajouter_un_contact()
    elif choice==2:
        print("bienvenue dans la partie lister un contact") 
        lister_un_contact()
    elif choice==3:
        print("bienvenue dans la partie modifier un contact")
        modifier_un_contact()
    elif choice==4:
        print("bienvenue dans la partie supprimer un contact")
        supprimer_un_contact()  
    elif choice==5:
        print("bienvenue dans la partie recherche de contact") 
        rechercher_un_contact()               