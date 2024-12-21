#Projet Info#

filepath1=input("Veuillez saisir le chemin d'accées au fichier csv de données à traiter: ")
filepath2=input("Veuillez saisir le chemin d'accès au fichier csv sur lequel vous souhaiter écrire les données utilisées pour les tracer de grpahiques: ")


#On crée toutes les listes pour extraire les données dans des listes distinctes:
#Listes pour graphique en courbe
ABX_bact_f=[]
ABX_day_f=[]
ABX_id_f=[]

placebo_bact_f=[]
placebo_day_f=[]
placebo_id_f=[]

#Listes pour graphique violon cecal
ABX_bact_cecal=[]
ABX_id_cecal=[]
placebo_bact_cecal=[]
placebo_id_cecal=[]

#Listes pour graphique violon ileal
ABX_bact_ileal=[]
ABX_id_ileal=[]
placebo_bact_ileal=[]
placebo_id_ileal=[]


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
write1=[]
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
write2=[]
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
write3=[]
for i in range(0,len(g2)-1):
    write3=';'.join([g2[i],g1[i]])
    fichier2.write(write3)
    fichier2.write('\n')

fichier2.write('\n')

fichier2.write("Pour le graphique en violon des souris traités avec un placebo:"+'\n')
fichier2.write("ID ; nombre de bactéries" + '\n')
write4=[]
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
write5=[]
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


#Génération des graphiques
import matplotlib.pyplot as plt
import math
import numpy as np

#Graphique en courbes
figure,axes=plt.subplots()
def graphique_f(listex,listey,couleur):
    for i in range(0,len(listey)-1):
        listey[i]=float(math.log(float(listey[i]))/math.log(10))
    axes.plot(listex,listey,color=couleur,label='Souris sous traitement antibiotiques')
    return(axes)

#Pour les courbes des éachantillons issu de souris sans antibiotiques
for i in range(0,len(nb_idABX)-1):
    ABX=[]
    day=[]
    for j in range(0,len(ABX_bact_f)-1):
        if ABX_id_f[j]==nb_idABX[i]:
            ABX.append(ABX_bact_f[j])
            day.append(ABX_day_f[j])
    B='blue'
    graphique_f(day,ABX,B)
axes.legend('Souris sous antibiotiques')

#Pour les courbes des éachantillons issu de souris sans antibiotiques
for i in range(0,len(nb_idplacebo)-1):
    placebo=[]
    day=[]
    for j in range(0,len(nb_idplacebo)-1):
        if placebo_id_f[j]==nb_idABX[i]:
            placebo.append(placebo_bact_f[j])
            day.append(placebo_day_f[j])
    O='orange'
    graphique_f(day,placebo,O)
axes.legend('Souris sous placebo')

axes.set_xlabel("Jour d'expérimentation")
axes.set_ylabel("log10 du nombre de bactéries vivantes par g d'échantillon")
axes.set_title("Evolution du log10 du nombre de bactéries vivantes par g d'échantillon")
figure.savefig('Graphique en courbe des échantillons de feces.png',dpi=600)


#Graphique en violon des échantillons d'ileum
figure2,axes2=plt.subplots()

for i in range(0,len(ABX_bact_ileal)-1):
    ABX_bact_ileal[i]=(math.log(float(ABX_bact_ileal[i]))/math.log(10))
for i in range(0,len(placebo_bact_ileal)-1):
    placebo_bact_ileal[i]=(math.log(float(placebo_bact_ileal[i]))/math.log(10))
X1=np.array(ABX_bact_ileal)
X2=np.array(placebo_bact_ileal)
axes2.violinplot(X1)
axes2.violinplot(X2)

axes2.set_ylabel("log10 du nombre de bacétries vivantes par g d'échantillon")
axes2.set_title("Données sur les échantillons d'ileum")
figure2.savefig("Graphique en violon des échantillons d'ileum.png",dpi=600)


#Graphique en violon des échantillons de caecum
figure3,axes3=plt.subplots()

for i in range(0,len(ABX_bact_cecal)-1):
    ABX_bact_cecal[i]=(math.log(float(ABX_bact_cecal[i]))/math.log(10))
for i in range(0,len(placebo_bact_cecal)-1):
    placebo_bact_cecal[i]=(math.log(float(placebo_bact_cecal[i]))/math.log(10))
X3=np.array(ABX_bact_cecal)
X4=np.array(placebo_bact_cecal)
axes3.violinplot(X3)
axes3.violinplot(X4)

axes3.set_ylabel("log10 du nombre de bactéries vivantes par g d'échantillon")
axes3.set_title("Données sur les échantillons de caecum")
figure3.savefig("Graphique en violon des échantillons de caecum.png",dpi=600)
