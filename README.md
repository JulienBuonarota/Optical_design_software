
# Installation
# How to
## Create a new system

Examples :
- Simple lens :   “ () “
- 3 lens “ (() () )) “


For a quick start, the type of the DIOPTRE is interpreted from the
symbol use, i.e. "(" for a ???????? and ")" for a ???????. It is
important to notice that dtThe surface
can be change afterward to any kind of surface.

| définie une ouverture (circulaire par défaut mais qui peut être de forme quelconque) 
qui permet de définir des pupilles

"[" et "]" define a miror

The order of the symbols refer to the order of which the ray go
through them and not how they are positionned in space.


The characteristics of each surface can be set afterward trhough the
edition of a dictionnary as follow : 

{"Dioptre 1":{

   "Rayon de courbure": 100 mm

A dictionnary will be created for each surfaces when the system is
first created. Surfaces can be added or deleted as necessary afterward.


## Visualise a system
## Plot a Spot Diagram



## Fonctionnement général du logiciel
### première version avec lancé de rayons
1) [utilisateur] création d'un fichier texte avec la string décrivant le système
2) Création a partir de ce fichier texte de
   - fichier csv de description des surfaces
   - fichier csv de description des parametre d'etudes
3) Editions de ces fichiers csv par l'utilisateur
4) A partir des deux fichier csv (system, parametre d'etude)
   - creation des rayons initiaux
   - calcul de la propagation des rayons
   - Plot du système optique
     - avec ou sans rayons
     - selon la coupe X ou Y 
