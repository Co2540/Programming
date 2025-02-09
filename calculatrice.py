import math, random, time, os, platform


def affichage(chaine): #la fonction permet un même affichage souhaité à différents endroits au lieu de répéter à chaque endroit
	print("_" * 100)
	print(chaine)
	print("_" * 100)


def effacer_terminal():
    # Vérifie le système d'exploitation
    if platform.system() == "Windows":
        os.system("cls")  # Commande pour Windows
    else:
        os.system("clear")  # Commande pour Linux et macOS

#initialisation du menu des jeux
def jeu():
	premierJeu = True
	while True: #permet de revenir au début du menu
		time.sleep(5)
		effacer_terminal()

		if premierJeu == True:
			affichage("\nBienvenue dans l'espace jeu !")
			premierJeu = False
		else:
			affichage("\nUne nouvelle partie ?")

		print("\nVoici nos jeux disponibles :")
		print("1. Plus ou moins")
		print("2. Calcul mental")
		print("3. En développement... (non disponible)")
		print("4. Quitter")

		jeuChoisi = int(input("\nVotre choix : ")) #enregistre le choix voulu

		match(jeuChoisi):

			case(1): #PLUS OU MOINS
				time.sleep(5)
				effacer_terminal()
				print("\nPLUS OU MOINS")
				print("Le principe est simple :")
				print("L'ordinateur va choisir un nombre entre 1 et 100.")
				print("Après la proposition que vous donnerez, il vous dira si le nombre est plus ou moins proche !")
				temps = input("\nVoulez-vous un temps (30 secondes d'accordées) ? ")
				mystere = random.randint(1, 100) #selectionne un nombre aléatoirement

				if temps == "OUI" or temps == "oui" or temps == "Oui": #permet d"avoir un temps
					limite = 30 #limite de 30 secondes fixés
					debut = time.time() #temps enregistré au début

					while True: #boucle pour revenir à la possibilité de donner une proposition
						ecoule = time.time()-debut #soustrait au temps actuel le temps du début
						restant = limite - ecoule #soustrait à la limite le temps écoulé

						print("\nTemps restant : ", int(restant), " secondes.") #affiche le temps restant
						if restant <= 0:
							print("Temps écoulé ! Le nombre était : ", mystere) #si le temps est écoulé le jeu est fini
							break
							time.sleep(5)
							effacer_terminal() #efface le terminal pour que ca soit plus lisible

						nombre = int(input("Donnez un nombre : ")) #permet d'enregistrer la proposition de l'utilisateur
						if nombre > mystere: #si le nombre est supérieur on indique qu'on est trop haut
							print("C'est moins !")
						if nombre < mystere: #s'il est inférieur on est trop bas
							print("C'est plus !")
						if nombre == mystere: #le jeu est fini si la valeur est trouvée en affichant le temps écoulé
							print("C'est gagné ! Le nombre était bien : ", mystere) 
							print("Temps écoulé : ", int(ecoule))
							break
							time.sleep(5)
							effacer_terminal()


				elif temps == "NON" or temps == "non" or temps == "Non": #même principe mais sans temps
					while True:
						nombre = int(input("Donnez un nombre : "))
						if nombre > mystere:
							print("C'est moins !")
						if nombre < mystere:
							print("C'est plus !")
						if nombre == mystere:
							print("C'est gagné ! Le nombre était bien : ", mystere) 
							print("Temps écoulé : ", int(ecoule))
							break
							time.sleep(5)
							effacer_terminal()



			case(2):#CALCUL MENTAL
				time.sleep(5)
				effacer_terminal()

				print("\nCALCUL MENTAL")
				print("Le principe est simple :")
				print("L'ordinateur va choisir deux nombres entre 1 et 100 ainsi qu'une opération entre +, - et *.")
				print("Après le nombre que vous donnerez il vous dira si le résultat est juste ou non !")
				temps = input("\nVoulez-vous un temps (30 secondes d'accordées) ? ")
				mystere1 = random.randint(1, 100) #selectionne un nombre aléatoirement
				mystere2 = random.randint(1, 100) #selectionne un nombre aléatoirement
				op = random.choice(["+", "-", "x"]) #sélectionne une opération dans la liste
				bonNombre = 0

				if temps == "OUI" or temps == "oui" or temps == "Oui": #permet d"avoir un temps
					limite = 30 #limite de 30 secondes fixés
					debut = time.time() #temps enregistré au début

					while True: #une boucle pour continuer les propositions
						ecoule = time.time()-debut #soustrait au temps actuel le temps du début
						restant = limite - ecoule #soustrait à la limite le temps écoulé

						print("\nTemps restant : ", int(restant), " secondes.") #affiche le temps restant
						
						if restant <= 0:
							print("Temps écoulé ! Le résultat était : ", bonNombre) #si le temps est écoulé le jeu est fini
							break
							time.sleep(5)
							effacer_terminal()

						if op == "+":
							print(mystere1, " + ", mystere2, " = ?") #affiche l'opération avec les nombres au hasard
							bonNombre = mystere1 + mystere2 #calcule le résultat
							proposition = int(input("Votre réponse ? ")) #enregistre la proposition du joueur

							if not proposition.is_integer(): #vérifie que la proposition est un entier sinon affiche un message
								print("Merci de donner un nombre.")

							else:
								if proposition == bonNombre: #si c'est le bon nombre ça le renvoie et sort de la boucle
									print("\nBravo ! Le résultat est : ", bonNombre, ". Temps écoulé : ", int(ecoule))
									break
									time.sleep(5)
									effacer_terminal()
								else: #affiche un message si mauvais résultat
									print("\nEh non ! Rententez votre chance.")


						if op == "-": #même fonctionnement
							print(mystere1, " - ", mystere2, " = ?")
							bonNombre = mystere1 - mystere2
							proposition = int(input("Votre réponse ? "))

							if not proposition.is_integer():
								print("Merci de donner un nombre.")
								
							else:
								if proposition == bonNombre:
									print("\nBravo ! Le résultat est : ", bonNombre, ". Temps écoulé : ", int(ecoule))
									break
									time.sleep(5)
									effacer_terminal()
								else:
									print("\nEh non ! Rententez votre chance.")

						if op == "x": #même fonctionnement
							print(mystere1, " x ", mystere2, " = ?")
							bonNombre = mystere1 * mystere2
							proposition = int(input("Votre réponse ? "))

							if not proposition.is_integer():
								print("Merci de donner un nombre.")
								
							else:
								if proposition == bonNombre:
									print("\nBravo ! Le résultat est : ", bonNombre, ". Temps écoulé : ", int(ecoule))
									break
									time.sleep(5)
									effacer_terminal()
								else:
									print("\nEh non ! Rententez votre chance.")



				if temps == "NON" or temps == "Non" or temps == "non": #même principe mais sans le temps
					while True:
						if op == "x":
							print(mystere1, " x ", mystere2, " = ?")
							bonNombre = mystere1 * mystere2
							proposition = int(input("Votre réponse ? "))

							if not proposition.is_integer():
								print("Merci de donner un nombre.")
								
							else:
								if proposition == bonNombre:
									print("\nBravo ! Le résultat est : ", bonNombre, ".")
									break
									time.sleep(5)
									effacer_terminal()
								else:
									print("\nEh non ! Rententez votre chance.")

						if op == "+":
							print(mystere1, " + ", mystere2, " = ?")
							bonNombre = mystere1 + mystere2
							proposition = int(input("\nVotre réponse ? "))

							if not proposition.is_integer():
								print("Merci de donner un nombre.")
								
							else:
								if proposition == bonNombre:
									print("\nBravo ! Le résultat est : ", bonNombre, ".")
									break
									time.sleep(5)
									effacer_terminal()
								else:
									print("\nEh non ! Rententez votre chance.")

						if op == "-":
							print(mystere1, " - ", mystere2, " = ?")
							bonNombre = mystere1 - mystere2
							proposition = int(input("Votre réponse ? "))

							if not proposition.is_integer():
								print("Merci de donner un nombre.")
								
							else:
								if proposition == bonNombre:
									print("\nBravo ! Le résultat est : ", bonNombre, ".")
									break
									time.sleep(5)
									effacer_terminal()
								else:
									print("\nEh non ! Rententez votre chance.")


#initialisation de la calculatrice
def choixCalculatrice():
	premierTour = True #permet de savoir si le premier tour n'est pas passé

	while True: #permet de revenir au menu après chaque fois à part au moment du break

		if premierTour == True: #affichage pour le premier tour
			affichage("\nBienvenue sur la SuperCalculatrice ! Voici les différentes possibilités : ")
			premierTour = False #initialise la variable à faux car le premier tour est passé
		else:
			affichage("\nFaire une nouvelle opération ou quitter ? ") #affichage pour chaque boucle suivante

		print("\n1. Division")
		print("2. Multiplication")
		print("3. Soustraction")
		print("4. Addition")
		print("5. Racine carré")
		print("6. Puissance")
		print("7. Pourcentage")
		print("8. Jeu")
		print("9. Quitter")
		print("\nVous pouvez sélectionner plusieurs nombres en fonction de l'opération souhaitée.")

		operation = int(input("\nQue voulez faire ? ")) #permet d'enregistrer le choix rentré

		match(operation): #différentes possibilités de la variable

			case(1): #DIVISION
				n = float(input("\nD'accord. Saisissez un nombre : "))
				n2 = float(input("Un autre nombre : "))
				entier = input("Voulez vous la divison entière (c'est à dire le résultat entier) ? Oui/Non ")
				if entier == "oui" or entier == "Oui" or entier == "OUI":
					total = n//n2 #renvoie uniquement l'entier
				elif entier == "non" or entier == "Non" or entier == "NON" :
					choix = input("Voulez vous la division classique ou le reste ? Classique/Reste : ")
					if choix == "Classique" or choix == "CLASSIQUE" or choix == "classique":
						total = n/n2 #renvoie le nombre possiblement décimal comme 2.0
					elif choix == "reste" or choix == "RESTE" or choix == "Reste":
						total = n%n2 #renvoie le reste
					else: 
						print("Choix mal compris.")
						continue
				else: #si ce n'est pas un nombre qui est entré
					print("Choix mal compris.")
					continue

				if total.is_integer(): #vérifie si le nombre n'est pas décimal pour ne pas renvoyer par exemple 2.0
					print("Le résultat est : ", int(total)) #int transforme le chiffre en int, il sera sans décimale
				else:
					print("Le résultat est : ", total)

				time.sleep(5)
				effacer_terminal() 

				
			
			case(2): #MULTIPLICATION, même principe pour les autres
				plus = True
				total = float(input("\nD'accord. Saisissez un nombre : "))
				rentrés = []
				rentrés.append(total)

				while plus: #création d'une boucle pour ajouter autant de nombre que l'utilisateur souhaite
					nombre = float(input("Un autre nombre : "))
					total *= nombre #multiplie le total par le nouveau nombre

					while True:
						rajouter = input("Rajouter un nombre ? Oui/Non ")
						if rajouter == "oui" or rajouter == "Oui":
							break
						elif rajouter == "non" or rajouter == "Non":
							plus = False #la boucle s'arrête et le résultat est renvoyé

							if total.is_integer():
								print("Le résultat est :", int(total))
							else:
								print("Le résultat est :", total)
							break
							time.sleep(5)
							effacer_terminal()

						else: #si la valeur entrée n'est pas dans les choix on revient au menu
							print("Choix non compris.")
							print("Valeurs rentrées : ", rentrés)

					


			case(3): #SOUSTRACTION
				plus = True
				total = float(input("\nD'accord. Saisissez un nombre : "))
				rentrés = []
				rentrés.append(total)
			
				while plus:
					nombre = float(input("Un autre nombre : "))
					total -= nombre
					rentrés.append(nombre)

					while True:
						rajouter = input("\nRajouter un nombre ? Oui/Non ")
						if rajouter == "oui" or rajouter == "Oui":
							break
						elif rajouter == "non" or rajouter == "Non":
							plus = False

							if total.is_integer():
								print("Le résultat est : ", int(total))
							else:
								print("Le résultat est : ", total)
							break
							time.sleep(5)
							effacer_terminal()

						else:
							print("Choix non compris.")
							print("Valeurs rentrées : ", rentrés)
						


			case(4): #ADDITION
				plus = True
				total = float(input("\nD'accord. Saisissez un nombre : "))
				rentrés = []
				rentrés.append(total)
				
				while plus:
					nombre = float(input("Un autre nombre : "))
					total += nombre #additionne le nombre au reste
					rentrés.append(nombre)

					while True:
						rajouter = input("Rajouter un nombre ? Oui/Non ")
						if rajouter == "oui" or rajouter == "Oui":
							break
						elif rajouter == "non" or rajouter == "Non":
							plus = False

							if total.is_integer():
								print("Le résultat est : ", int(total))
							else:
								print("Le résultat est : ", total)
							break
							time.sleep(5)
							effacer_terminal()

						else:
							print("Choix non compris.")
							print("Valeurs rentrées : ", rentrés)


			case(5):
				n = float(input("D'accord. Saisissez un nombre : "))
				total = math.sqrt(n)
				if total.is_integer():
					print("Le résultat est : ", int(total))
				else:
					print("Le résultat est : ", total)
				time.sleep(5)
				effacer_terminal()
					
			


			case(6):
				n = float(input("D'accord. Saisissez un nombre : "))
				n2 = float(input("Un autre nombre : "))
				total = n**n2

				if total.is_integer():
					print("Le résultat est : ", int(total))
				else:
					print("Le résultat est : ", total)
				time.sleep(5)
				effacer_terminal()
				

			case(7):
				n = float(input("D'accord. Saisissez un nombre : "))
				total = n/100

				if total.is_integer():
					print("Le résultat est : ", int(total), "%.")
				else:
					print("Le résultat est : ", total, "%.")
				time.sleep(5)
				effacer_terminal()


			case(8):
				jeu()


			case(9): #QUITTER
						print("A bientôt !")
						break #sort de la boucle générale 
						time.sleep(5)
						effacer_terminal()


			case _: #si le choix n'est pas parmi les valeurs on revient au début de la boucle
				print("Choix non valide, veuillez recommencer")

choixCalculatrice()