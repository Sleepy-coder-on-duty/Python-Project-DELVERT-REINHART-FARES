#Projet Info#

filepath1=input("Veuillez saisir le chemin d'accées au fichier csv de données à traiter: ")
filepath2=input("Veuillez saisir le chemin d'accès au fichier csv sur lequel vous souhaiter écrire les données utilisées pour les tracer de grpahiques: ")


#On crée toutes les listes pour extraire les données dans des listes distinctes:
#Listes pour graphique en courbe
ABX_bact_f=[]                                                                                       # Valeur de Y
ABX_day_f=[]                                                                                        # Valeur de X
ABX_id_f=[]                                                                                         # Courbe en fonction de l'id du sujet de test

placebo_bact_f=[]                                                                                   # Valeur de Y du temoin
placebo_day_f=[]                                                                                    # Valeur de X du temoin
placebo_id_f=[]                                                                                     # NCourbe en fonction de l'id du temoin

#Listes pour graphique violon cecal
ABX_bact_cecal=[]                                                                                   # Valeur de Y
ABX_id_cecal=[]                                                                                     # Nombre de courbe en fonction de l'id du sujet de test
placebo_bact_cecal=[]                                                                               # Valeur de Y du temoin
placebo_id_cecal=[]                                                                                 # Point en fonction de l'id du temoin

#Listes pour graphique violon ileal
ABX_bact_ileal=[]                                                                                   # Valeur de Y
ABX_id_ileal=[]                                                                                     # Nombre de courbe en fonction de l'id du sujet de test
placebo_bact_ileal=[]                                                                               # Valeur de Y du temoin
placebo_id_ileal=[]                                                                                 # Point en fonction de l'id du temoin



#On extrait les données du fichier csv dans les listes associées
    
fichier1 = open(filepath1, 'r')
line=fichier1.readline()
while line!='':
    line=fichier1.readline()
    rawline=line.split(';')
    if rawline==['']:
        break
    elif 'ABX' in rawline and 'fecal' in rawline:
        ABX_id_f.append(rawline[4])
        ABX_day_f.append(rawline[7])
        ABX_bact_f.append(rawline[8])
    elif 'placebo' in rawline and 'fecal' in rawline:
        placebo_id_f.append(rawline[4])
        placebo_day_f.append(rawline[7])
        placebo_bact_f.append(rawline[8])
    elif 'ABX' in rawline and 'cecal' in rawline:
        ABX_bact_cecal.append(rawline[8])
        ABX_id_cecal.append(rawline[4])
    elif 'placebo' in rawline and 'cecal' in rawline:
        placebo_bact_cecal.append(rawline[8])
        placebo_id_cecal.append(rawline[4])
    elif 'ABX' in rawline and 'ileal' in rawline:
        ABX_bact_ileal.append(rawline[8])
        ABX_id_ileal.append(rawline[4])
    else:
        placebo_bact_ileal.append(rawline[8])
        placebo_id_ileal.append(rawline[4])
                        
a=len(ABX_id_f)
x=len(placebo_id_f)
nb_idABX=list(set(ABX_id_f))  #on supprime les doublons se trouvant dans la liste ABX_id_f
nb_idplacebo=list(set(placebo_id_f)) #on supprime les doublons se trouvant dans la liste placebo_id_f
fichier1.close()

#On retourne toutes les données récoltées sur un doncument CSV

#Pour créer un ensemble de données plus lisible sur le doc csv on regroupe toutes les données avec les mêmes identifiants de souris
#Données pour le graphique en courbe:
fichier2=open(filepath2,'w')
c1=a
c2=ABX_id_f
d=nb_idABX
liste1=ABX_day_f
liste2=ABX_bact_f
fichier2.write("Les données utilisées pour le tracer des courbes de souris sous antibiotiques sont les suivantes:"+ '\n')
fichier2.write("ID ; Abscisse ; Ordonnée"+ '\n')
for i in range(0,len(d)-1):
    x1=d[i]
    fichier2.write('\n')
    for j in range(0,c1-1):
        if c2[j]==d[i]:
            write=';'.join([x1,liste1[j], liste2[j]])
            fichier2.write(write)
            fichier2.write('\n')
fichier2.write('\n'+'\n')
e1=x
e2=placebo_id_f
f=nb_idplacebo
liste3=placebo_day_f
liste4=placebo_bact_f
fichier2.write("Les données utilisées pour le tracer des courbes de souris sous placebo sont les suivantes:" +'\n')
fichier2.write("ID ; Abscisse ; Ordonnée"+ '\n')
for i in range(0,len(f)-1):
    x2=f[i]
    fichier2.write('\n')
    for j in range(0,e1-1):
        if e2[j]==f[i]:
            write2=';'.join([x2,liste3[j],liste4[j]])
            fichier2.write(write2)
            fichier2.write('\n')

fichier2.write('\n'+'\n')

#Données pour les grpahiques en violon
fichier2.write("Les données utilisées pour le tracer des graphiques en violon des études du microbiote cecal sont les suivantes:" + '\n')
g1=ABX_bact_cecal
g2=ABX_id_cecal
h1=placebo_bact_cecal
h2=placebo_id_cecal
fichier2.write("Pour le graphique en violon des souris traités avec des antibiotiques:" +'\n')
fichier2.write("ID ; nombre de bactéries" + '\n')
for i in range(0,len(g2)-1):
    write3=';'.join([g2[i],g1[i]])
    fichier2.write(write3)
    fichier2.write('\n')

fichier2.write('\n')

fichier2.write("Pour le graphique en violon des souris traités avec un placebo:"+'\n')
fichier2.write("ID ; nombre de bactéries" + '\n')
for i in range(0, len(h2)-1):
    write4=';'.join([h2[i],h1[i]])
    fichier2.write(write4)
    fichier2.write('\n')
    
fichier2.write('\n')
z1=ABX_bact_ileal
z2=ABX_id_ileal 
y1=placebo_bact_ileal 
y2=placebo_id_ileal
fichier2.write("Les données utilisées pour le tracer des graphiques en violon des études du microbiote ileal sont les suivantes:" +'\n')
fichier2.write("Pour le graphique en violon des souris traités avec des antibiotiques:" +'\n')
fichier2.write("ID ; nombre de bactéries" + '\n')
for i in range(0,len(z2)-1):
    write5=';'.join([z2[i],z1[i]])
    fichier2.write(write5)
    fichier2.write('\n')

fichier2.write('\n')

fichier2.write("Pour le graphique en violon des souris traités avec un placebo:"+'\n')
fichier2.write("ID ; nombre de bactéries" + '\n')
write6=[]
for i in range(0,len(y2)-1):
    write6=';'.join([y2[i],y1[i]])
    fichier2.write(write6)
    fichier2.write('\n')
        
fichier2.close()


#Création des graphiques
import matplotlib.pyplot as plt
import math
import numpy as np

#Dossier où seront enregistré les graphiques
dossier_graph = input("Entrez le chemin d'accès du dossier où enregistrer le graphique: ")

#Graphique en courbes
figure,axes=plt.subplots()
axes.set_xlabel("Jour d'expérimentation")
axes.set_ylabel("log10 du nombre de bactéries vivantes par g d'échantillon",fontsize=8)
axes.set_title("Evolution du log10 du nombre de bactéries vivantes par g d'échantillon"+'\n'+"Gris=Placebo    Bleu=antibiotiques")
axes.grid(True)
   
def tracer_graph(listeR,listeid,listey,listex,couleur,AP):
    for i in range(0,len(listeR)-1):
        ABX_P=[]
        day=[]
        for j in range(0,len(listey)-1):
            if listeid[j]==listeR[i]:
                ABX_P.append(math.log10(float(listey[j])))
                day.append(int(listex[j]))
        axes.plot(day,ABX_P,color=couleur)
tracer_graph(nb_idABX,ABX_id_f,ABX_bact_f,ABX_day_f,'blue','antibiotiques')
tracer_graph(nb_idplacebo,placebo_id_f,placebo_bact_f,placebo_day_f,'grey','placebo')

nom_fichier=f"{dossier_graph}/Graphique en courbe des échantillons de feces.png.png"
figure.savefig(nom_fichier,dpi=600)


#On combine les jeux de données dans des arrays
X1=np.array(ABX_bact_ileal,dtype=np.float64)
X2=np.array(placebo_bact_ileal,dtype=np.float64)
Array1=[X1,X2]

X3=np.array(ABX_bact_cecal,dtype=np.float64)
X4=np.array(placebo_bact_cecal,dtype=np.float64)
Array2=[X3,X4]

#fonction permettant de tracer les graphiques en violon
def violin_plot(data,sample,nom_fichier):
    figure,axes=plt.subplots()

    num_groups = len(data)
    for index in range(num_groups):
        group = data[index]
        parts = axes.violinplot(group, positions=[index + 1], showmeans=True, showextrema=True)

    parts['cmeans'].set_color("green")
    parts['cbars'].set_color("black")

    axes.set_yscale("log")
    axes.set_title(f"Données sur les échantillons {sample}"+'\n'+"Groupe 1=placebo    Groupe 2=antibiotiques", fontsize=16)
    axes.set_xlabel('Groupe de données', fontsize=14)
    axes.set_ylabel('log10 du nombre de bactéries vivantes/g - Echelle logarithmique', fontsize=8)
    axes.set_xticks(range(1, num_groups + 1), [f'Groupe {i+1}' for i in range(num_groups)])
    figure.savefig(nom_fichier, dpi=300)

# Appeler la fonction pour tracer le graphique
violin_plot(Array1,"d'ileum",f"{dossier_graph}\Graphique sur les données d'échantillons ileum.png")
violin_plot(Array2,"de caecum",f"{dossier_graph}\Graphique sur les données d'échantillons caecum.png")
