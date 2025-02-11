#Ce programme vise à changer le nom des fichiers selon une caractéristique précise.
#Ici, lorsque la taille des fichiers est supérieure à 1ko, son nom change selon les paramètres expliqués plus bas
#Bonne découverte !

#!/bin/bash

echo "Saisissez un nom :" #initialise le nouveau nom qu'on veut donner aux fichiers
read nom
echo "Choisissez un chemin vers un répertoire :" #permet d'aller dans le répertoire contenant les fichiers
red rep

if [ -d "$rep"]; then #si le répertoire existe on exécute la suite

	cd $rep #accès vers le répertoire
	ls -lh #affiche l'ensemble des fichiers avant modification

	i = 1 #permet de donner un nom qui différencie les fichiers
	for file in $(find -type f -size +1k); do #sélectionne les fichiers qui ont une taille supérieure à 1k
		nouveau_nom = "$nom$i-$$" #assigne nouveau nom composé de celui choisi avec le du PID du processus ($$)
		mv "$file" "$nouveau_nom" #modifie le nom
		i = $((i+1)) #augmente le i en fonction du nombre de fichier
done

ls -lh

else
	echo "Répertoire non existant"
	exit #si le répertoire n'existe pas on sort du programme
fi
