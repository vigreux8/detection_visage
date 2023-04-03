# L'objectif du programme

- Fonctionne avec une image ou une webcam
- Repérer les visages pour placer une image PNG dessus
- Afficher du texte

## Installation

`````
pip install -r requirement.txt
``````

## Paramètre de l'application : 
Se trouvent dans le fichier de constante Setting.py. Pour les modifier, les paramètres se trouvent dans :
```
\\constante\\Setting.py
  -->  Class Setting_main:
```
Ou modifiez les variables dans le fichier main.py en important les variables avec cette commande :
````
from constante.Setting import SettingMain
````

# Utilisation 

- Bien choisir si vous utilisez une caméra ou une image fixe
- Indiquez le chemin de l'image.png à coller sur les visages dans :
````
\\constante\\Setting.py
    --> Class ImagePatch
        --> imagetracerPath
````
- lancer le main


## Si vous utiliser une image :
- Mettez le paramètre caméra à False
- Indiquez l'image sur laquelle les visages seront détectés dans :
 ````
\\constante\\Setting.py
    --> Class ImagePatch
        --> imagefixePath
````