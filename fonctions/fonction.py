import pygame 
from numpy import random
import cv2
from constante.Setting import SettingMain,ImagePatch
CORRECTION_RATIO = 0.5
from math import floor
from numpy import random

class DrawingTexte():
    def __init__(self,fenetre) -> None:
        self.texte = SettingMain.TEXTE
        self.fenetre = fenetre
        self.witch = self.fenetre.get_width()
        self.height = self.fenetre.get_height()
        self.pading_bloque = 50
        self.pading_texte = 10
        self.font = pygame.font.Font(None,50)
        
    def texte_drawing(self,texte="je suis du texte"):
        surface_texte = self.font.render(texte,True,(255,255,255))
        cord_x_texte = self.witch/2-surface_texte.get_width()/2
        # cord_y_texte = self.height-self.pading_bloque
        cord_y_texte = self.pading_bloque
        
        cord_x_bakcground = self.witch/2-(surface_texte.get_width()+self.pading_texte)/2
        # cord_y_bakcground = self.height-self.pading_bloque-self.pading_texte/2
        cord_y_bakcground = self.pading_bloque-self.pading_texte/2
        
        
        
        rectangle = pygame.Rect(cord_x_bakcground,cord_y_bakcground,surface_texte.get_width()+self.pading_texte,surface_texte.get_height()+self.pading_texte)
        pygame.draw.rect(self.fenetre,(241,77,37),rectangle,border_radius=20)
        self.fenetre.blit(surface_texte,(cord_x_texte,cord_y_texte))
        
    def selection_aléatoire(self,taille_liste):
        return random.randint(0,taille_liste)
    
    
    def selection_augmenter(self,taille_liste,index_actuelle):
        if index_actuelle >= taille_liste-1:
            return 0
        else:
            return index_actuelle +1

class TraitementImage:

    def mise_a_l_echelle_fenetre(image_background:object,image_a_modifier:object):
        if image_a_modifier.shape[1] < image_background.shape[1]:
            ratio =(image_background.shape[1]/image_a_modifier.shape[1])
            print("ratio si inférieur",ratio)
            # print("image a modifier = ",image_a_modifier.shape[1])
            # print("image a background = ",image_background.shape[1])
            # print("ratio= ",ratio)
            x,y=round(image_a_modifier.shape[1]/ratio),round(image_a_modifier.shape[0]/ratio)
        else:
            ratio = (image_background.shape[1]/image_a_modifier.shape[1])
            print("ratio si superieur",ratio)
            x,y =round(image_a_modifier.shape[1]*ratio),round(image_a_modifier.shape[0]*ratio)
        return x,y

    def mise_a_l_echelle_pygame_img_visage(background_width,visage_width:int,image_a_modifier:object):
        ratio = background_width/visage_width
        image_a_modifier = pygame.transform.scale(image_a_modifier,(image_a_modifier.get_width()/ratio,image_a_modifier.get_height()/ratio))
        print("ratio:",ratio)       
        return image_a_modifier

    def preset_definition_video():
        mode = SettingMain.DEFINITION_CAMERA
        if mode == 1:
            return 1920,1080
        if mode == 2:
            return 1280,720
        else :
            return False
    
class Detection_visage:
    def recuperation_visage(frame):
        # print("frame",frame)
        cascadeClassifier = cv2.CascadeClassifier(ImagePatch.cascadeClassifierPatch)
        frame_grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        detecte_face = cascadeClassifier.detectMultiScale(frame_grey,minSize=(20, 20),maxSize=(500,500))
        # print("detecte_face",detecte_face)
        # faces = []
        # for (x_cv2, y_cv2, w_cv2, h_cv2) in detecte_face:
        #     # Conversion des coordonnées de sortie en coordonnées exploitables par Pygame
        #     x_pygame = x_cv2
        #     y_pygame = y_cv2
        #     w_pygame = w_cv2
        #     h_pygame = h_cv2
        #     faces.append((x_pygame, y_pygame, w_pygame, h_pygame))
        return detecte_face

class gestion_du_temps:
    def __init__(self) -> None:
        self.elapsed_time =0
        self.last_time = 0
        self.current_time = pygame.time.get_ticks()
    
    def si_temps_ecouler(self,delais):
        delais *=1000
        self.current_time = pygame.time.get_ticks()
        self.elapsed_time = self.current_time - self.last_time + self.elapsed_time
        self.last_time = self.current_time
        if self.elapsed_time > delais:
            self.elapsed_time = 0
            return True
        else : 
            return False
         
class initilisation_programme:
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.temps = gestion_du_temps()
        self.image_principale_cv2 =None
        self.image_principale_pygame = None
        self.SCREEN_HEIGHT = None
        self.SCREEN_WIDTH = None
        self.flux_video = None
        self.detecte_face = None
        self.image_tracer_pygame = None
        self.index_phrase = 0
        self.init_set_size_pygame_screen_if_image_or_video()
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT)) 
        self.image_tracer_cv2 = cv2.imread(ImagePatch.imagetracerPath)
        self.init_mise_a_l_echelle_image_tracer()
        self.stylo = DrawingTexte(self.screen)
        self.detecte_face = Detection_visage.recuperation_visage(self.image_principale_cv2)


    def init_set_size_pygame_screen_if_image_or_video(self):
        if SettingMain.CAMERA:
            # print("condition")
            self.flux_video = cv2.VideoCapture(0)
            self.set_size_video()
        else : 
            self.image_principale_cv2 = cv2.imread(ImagePatch.imagefixePath)
            self.SCREEN_HEIGHT,self.SCREEN_WIDTH = self.image_principale_cv2.shape[0:2]

    
    def set_size_video(self):  
        print("size_video")          
        if SettingMain.DEFINITION_CAMERA in (1,2):
            width,height=TraitementImage.preset_definition_video()
            self.flux_video.set(cv2.CAP_PROP_FRAME_WIDTH,width)
            self.flux_video.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
            self.SCREEN_HEIGHT,self.SCREEN_WIDTH = self.flux_video.read()[1].shape[0:2]
            # print("screen_height set size video :",self.SCREEN_HEIGHT)
            # print("screen_witch set size video :",self.SCREEN_WIDTH)
            self.image_principale_cv2 = self.flux_video.read()[1]
        else :
            # print("else")
            self.SCREEN_HEIGHT,self.SCREEN_WIDTH = self.flux_video.read()[1].shape[0:2]
            self.image_principale_cv2 = self.flux_video.read()[1]
            # print("screen_height set size video :",self.SCREEN_HEIGHT)
            # print("screen_witch set size video :",self.SCREEN_WIDTH)
            
        
    def init_mise_a_l_echelle_image_tracer(self):
        new_whith,new_height =  TraitementImage.mise_a_l_echelle_fenetre(self.image_principale_cv2,self.image_tracer_cv2)
        img_casque = pygame.image.load(ImagePatch.imagetracerPath).convert_alpha()
        img_casque = pygame.transform.scale(img_casque,(new_whith,new_height))
        print("//new_whith",new_height,"//new_height:",new_height)
        self.image_tracer_pygame = img_casque
    
    #utiliser dans la boucle
    def afficher_texte(self):
        if self.temps.si_temps_ecouler(random.randint(2,4)):
            self.index_phrase = self.stylo.selection_augmenter(len(self.stylo.texte),self.index_phrase)
    
    def detect_visage(self):
        self.detecte_face = Detection_visage.recuperation_visage(self.image_principale_cv2)
        
    def read_webcam(self):
         self.image_principale_cv2 = self.flux_video.read()[1]
    
    def conv_img_cv2_to_pygame(self):
        inisialisation = cv2.cvtColor(self.image_principale_cv2, cv2.COLOR_BGR2RGB)
        inisialisation = cv2.rotate(inisialisation,cv2.ROTATE_90_COUNTERCLOCKWISE)
        self.image_principale_pygame = pygame.surfarray.make_surface(inisialisation)
        
        
    def test_detection_visage(self):
        detecte = Detection_visage.recuperation_visage(self.image_principale_cv2)
        #  print("detecte :",detecte)
        frame = pygame.transform.flip(frame,True,False)
        
    def run(self):
        if not SettingMain.CAMERA:
            # print("image_cv2 :",self.image_principale_cv2)
            self.detect_visage()
            self.conv_img_cv2_to_pygame()
            print("//taille",self.image_tracer_pygame.get_size())
        while True:
            # print("boucle")
            self.afficher_texte()
            if SettingMain.CAMERA :
                self.read_webcam()
                self.detect_visage()
                self.conv_img_cv2_to_pygame()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if SettingMain.CAMERA:
                        self.flux_video.release()
                    pygame.quit()
                    exit()
            self.screen.blit(self.image_principale_pygame,(0, 0))
            self.stylo.texte_drawing(self.stylo.texte[self.index_phrase])
            for (x,y,visage_witch,visage_height) in self.detecte_face:
                casque = TraitementImage.mise_a_l_echelle_pygame_img_visage(self.SCREEN_WIDTH,visage_witch,self.image_tracer_pygame)
                self.screen.blit(casque,(x,y-50))
                pygame.display.update()
            pygame.display.flip()
            self.clock.tick(SettingMain.FPS)
            