from os import path

class ImagePatch:
    imagefixePath =  path.join("image","_test.png")
    imagetracerPath = path.join("image","casque_b_to_b.png")
    cascadeClassifierPatch = path.join("utils","haarcascade_frontalface_default.xml")

class Setting_main:
    FPS =60
    CAMERA = True
    #1 = 1080p, 2= 720p #other desatfiver
    DEFINITION = 2
    DEFINITION_CHOISIS =""
    
class CamConstante:
    CONSTANTE_1 = 1
    