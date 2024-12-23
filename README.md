Projet CY-Antibio-Tech

Prérequis:

Python
Bibliothèque matplotlib
Fichier CSV contenant les données à traiter, le fichier CSV d'entrée doit contenir des colonnes séparées par des points-virgules (;)

Description:

Ce projet est un code python qui permet de générer des graphiques automatiquement à partir de données issues d’expériences de laboratoire.
Celles-ci ont été préalablement stockées dans un document CSV. 


Le code permet d’obtenir un graphique standard (courbe) et un graphique violon pour des paramètres mesurés
Le code créer une courbe ou un point pour chaque sujets de tests et témoins. 


Le code permet de saisir en entrée le chemin d'accès au fichier csv contenant les données brutes de l’expérience afin de créer un fichier contenant les données utiles pour tracer les graphiques. 
Ce code traite ces fichiers en séparant les données CSV puis en ajoutant à des listes contenant nos valeurs de X, Y et le nombre de courbe ou point.
Le script permet aussi de retirer les doublons éventuelles dans notre liste afin d’éviter des erreurs.



De plus il recrée dans un autre document CSV (fichier crée au préalable par l'utilisateur dans le même emplacement que le code) à partir des listes précédentes mais en regroupant les données en fonction des identifiants des sujets de test. 
L'utilisateur crée aussi au préalable dans le même emplacement que le code un dossier où le programme enregistrera les graphiques génerés (le chemin d'accès de ce dossier sera saisi par l'utilisateur dans le code).

Les différents graphiques sont tracés avec les données que l’on désire. 


Le premier graphe est un graphique en courbe d’une valeur a en ordonnée en fonction d’une valeur de temps.

Le second et troisième graphiques sont des graphiques en violon à partir d’une autre valeur ‘b’ et une autre valeur ‘c’ en fonction de chaque sujet de test.


Il est important de noter que le code à été fait en fonction de notre document CSV contenant les données de l'expérience, il fonctionne donc avec des noms de colonnes spécifiques. 

Pour l’utilisation dans un document contenant les données issues d’autres expérience il faut s’assurer de changer les noms des colonnes et des listes dans le script avec celles qui correspondent dans votre document CVS afin d’obtenir les graphiques souhaités. 

Quand on active le code, celui-ci nous demande de rentrer le chemin d'accès du fichier csv à exploiter et du fichier csv de sortie qui listera les données que l'on va utiliser pour les tracer de graphiques.

Si l'expérience n’a pas autant de données différentes afin de faire un ou les deux graphiques en violons alors la fonction rendra un graphique vide. 

Si vous désirez obtenir un deuxième graphique en courbe classique au lieu d’un graphique en violon alors copiez-collez le premier code permettant le tracé du graphique et remplacez les valeurs des listes avec celle de vos données désirées. 
Les graphiques sont enregistrés au format PNG dans le dossier dont le chemin d'accès a été spécifié.
