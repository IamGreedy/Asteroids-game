import pygame

class Score :
    def __init__(self):
        self.value=0
        self.highscore = self.load_highscore ()
    
    def add_points (self,points):
        self.value+=points
    
    def draw (self,screen):
        font = pygame.font.Font(None,36) #Crée une police de caractère, NONE = police par défaut et 36 = taille de la police
        text = font.render (f"score : {self.value}", True, (200,200,200)) # Crée une imag ede texte qui contient le score, texte à afficher, TRUE = texte plus lisse; (200,200,200) = couleur du texte
        screen.blit(text, (10,10)) # affiche le texte sur l'écran à la position 10,10 (en haut à gauche)
        hs_text=font.render(f"High : {self.highscore}", True, (160,160,160)) 
        screen.blit(hs_text,(10,40)) # Affiche le highscore un peu plus bas

    def save_highscore (self):
        if self.value> self.highscore:
            with open("highscore.txt", "w") as f: # ouvre ou crée un fichier highscore.txt en mode écriture ("w") ; with garantie quele fichier sera fermé à la fin et f représente le fichier ouvert
                f.write (f"{self.value}") # écrit le score actuel converti en texte
    
    def load_highscore(self):
        try :
            with open("highscore.txt", "r") as f: # ouvre le fichier highscore en mode read "r"
                return int(f.read().strip()) # lis le contenu du fichier et le renvoie, strip() supprime les espaces ou retour à la ligne autour du texte ; int(......) convertit le texte en entier : "120" devient 120
        except:
            return 0 # si jamais le fichier n'existe pa , on renvoie 0
    