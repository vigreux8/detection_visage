from os import path

class ImagePatch:
    imagefixePath =  path.join("image","groupe_inconnue.jpg")
    imagetracerPath = path.join("image","casque_3d_rezize.png")
    cascadeClassifierPatch = path.join("utils","haarcascade_frontalface_default.xml")



class SettingMain:
    """
    Paramétre globale de l'application 
    
    
    FPS: Nombre d'image ou la fenetre et rafraichis 
    
    CAMERA : active/Desactive la caméra
    [
        Prend uniquement True or False
    ]
    
    
    DEFINITION_CAMERA :
    !!! Définition elever = Programme lents !!!
            1 = 1080p,
            2= 720p,
            3= taille standart (PLUS Rapide)
    
    TEXTE : Texte afficher sur l'écrant
       
    """
    FPS =30
    CAMERA = True
    DEFINITION_CAMERA = None
    TEXTE =[
        "Texte_1",
        "Texte_2",
        "Texte_3",
        "ect..."
             ]