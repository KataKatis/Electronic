from tkinter import *
#nombre aléatoire
from random import randint,choice
#fonction mathématique
from math import cos,pi,sqrt,sin
#cryptage de données
import lb_cryptage
#requete web
from urllib.request import urlopen
import webbrowser

sav = open("save.txt","a")      #ouvre le fichier save.text et crée ce fichier si inexistant (fichier pour les sauvegarde)
sav.close()     #ferme le fichier

police = "impact"   #police de carractère définit sur tout le jeu 
version="2.1.1"     #version du jeu
av_jeu = 0      #Variable de lancement du jeu
sav = open("save.txt","r") #    ouverture du fichier de sauvegarde
info_joueur = sav.readlines()   #enregistrement des donnée du joueur dans une liste
sav.close()
if len(info_joueur) < 3:    #verification des données du joueur pour savoir si une connexion est requise
    av_jeu = 1     #mise en attente du lancement de la fenêtre principale (cf boucle plus bas)
    def con():      #fonction destinner à la connexion du joueur
        global Cadre,av_jeu     
        try:        #essaye de détruire la fenetre d'erreur si existante
            Cadre.destroy()
        except:     # sinon passe a la suite
            pass
        Cadre=Frame(inscription,bg="black")     # création de la fenêtre d'erreur
        try:    #essaye de se connecter
            pseudo = value.get()    # recupère le pseudo et le mot de passe
            mdp = value2.get()
            url = "http://don-t-crash2.esy.es/python_info.php?user="+str(pseudo)+"&&mdp="+str(mdp) # création de l'url de connexion
            x = urlopen(url)    #ouverture de l'url
            ch = str(x.read())      #enregistrement du contenu de la page dans une variable
            ch_fin = ch.split("\\n")    #séparation des donnée et enregistrement dans une liste

            ch_fin = str(ch_fin[6:7])
            ch_fin = ch_fin.replace("[" ,"")
            ch_fin = ch_fin.replace("]" ,"")
            ch_fin = ch_fin.replace("'" ,"")
            ch_fin = ch_fin.split()
            if ch_fin[0]=="0":      #vérification de la connexion
                Label(Cadre,text="Pseudo ou mot de passe eroné ",fg="red",font=police+" 20",bg="black").pack()
            else:
                inscription.destroy()   #destruction de la fenêtre 
                save = open("save.txt","w")     #enregistrement des donnée dans le fichier save
                save.write(str(pseudo)+'\n'+str(ch_fin[4])+'\n'+str(ch_fin[1])+'\n'+str(ch_fin[2])+'\n'+str(ch_fin[3])+'\n'+str(ch_fin[5]))
                save.close()
                av_jeu = 0      # lancement de la fenêtre principal (cf boucle plus bas)
        except:     #erreur de connexion au site
            Label(Cadre,text="erreur connexion",fg="red",font=police+" 20",bg="black").pack()
        try:
            Cadre.pack()
        except:
            x=1
    def ins():      #fonction pour l'inscription
        global Cadre,av_jeu
        def verif(chain):   #vérification des longeurs du mot de passe et ddu pseudo ainsi que l'insertion de caractère spéciaux
            error = 0
            if len(str(chain)) > 15 or len(str(chain))< 3:
                error = 1
            ch_er = "&é\"\'(-è_çà)= ;:/!?,<>"
            for ch in chain:
                try:
                    ch_er.index(ch)
                    error = 2
                except:
                    pass
            return error
        try:
            Cadre.destroy()
        except:
            pass
        Cadre=Frame(inscription,bg="black")
        pseudo = value.get()    
        mdp = value2.get()
        mail = value3.get()
        test_1 = verif(pseudo)  #verification
        test_2 = verif(mdp)
        if test_1 == 1 or test_2==1:    #donne l'information au joueur de l'erreur dansson mot de passe ou son pseudo
            erreur = Label(Cadre,text="trop court ou trop long (entre 3 est 15 cractère)",font=police+" 20",fg="red",bg="black").pack()
        if test_1 == 2 or test_2==2:
            erreur = Label(Cadre,text="pas d'espace ou caractère spéciaux",font=police+" 20",fg="red",bg="black").pack()
        if test_1 == 0 or test_2 == 0:
            try:    # tentative de d'inscription
                url = "http://don-t-crash2.esy.es/python_inscription.php?user="+str(pseudo)+"&&mdp="+str(mdp)+"&&mail="+str(mail)+"&&version="+str(version)
                req = urlopen(url) 
                ch = str(req.read())
                ch_fin = ch.split("\\n")

                ch_fin = str(ch_fin[6:7])
                ch_fin = ch_fin.replace("[" ,"")
                ch_fin = ch_fin.replace("]" ,"")
                ch_fin = ch_fin.replace("'" ,"")
                ch_fin = ch_fin.split()
                if ch_fin[0] == "Duplicate":
                    erreur  = Label(Cadre,text="Pseudo existant ",font=police+" 20",fg="red",bg="black").pack()
                else:
                    inscription.destroy()
                    save = open("save.txt","w")
                    save.write(str(pseudo)+'\n'+str(mdp)+'\n1\n0\n0\n0')
                    save.close()
                    av_jeu = 0
                    
            except:
                erreur = Label(Cadre,text="problème de connexion",font=police+" 20",fg="red",bg="black").pack()
        try:
            Cadre.pack()
        except:
            pass
        
    inscription = Tk()  #création de la fenêtre
    inscription.configure(bg = "black")
    inscription.geometry('700x700+0+0')
    inscription.title("don't crash 2")
    Label(inscription,text="Don't crash 2",font=police+" 30",fg="red",bg="black").pack(pady=20)
    Message(inscription,text="Bienvenu, Vous allez pouvoir jouer dans quelques instant, juste le temps de nous donnez quelques informations:",width=600,font=police+" 25",fg="white",bg="black").pack()
    value = StringVar()     #création des variable pseudo,mdp et mail
    value2 = StringVar()
    value3 = StringVar()
    Label(inscription,text="Votre Pseudo:",font=police+" 25",fg="blue",bg="black").pack()
    Entry(inscription,textvariable=value,width=30,font=police).pack()
    Label(inscription,text="Votre Mot de passe:",font=police+" 25",fg="blue",bg="black").pack()
    Entry(inscription,textvariable=value2,width=30,font=police,show="*").pack()
    Label(inscription,text="Votre mail (si inscription):",font=police+" 25",fg="blue",bg="black").pack()
    Entry(inscription,textvariable=value3,width=30,font=police).pack()
    Button(inscription,text="inscription",command=ins,width = 30,font=police+" 15",fg="black").pack(pady=10)
    Button(inscription,text="connexion",command=con,width = 30,font=police+" 15",fg="black").pack(pady=10)
while av_jeu == 1: #boucle qui lance le jeu une fois la connexion ou l'incription  (tourne en continue en arrière plan)
    try:
        inscription.update() #mise a jour de la fentre
    except:
        exit()  #quitte le programme si la fene^tre et fermer avant l'incription ou la connexion
sav = open("save.txt","r")
info_joueur = sav.readlines()
sav.close()
                   
fenetre = Tk()
larg = fenetre.winfo_screenwidth()  #récupération de la largeur et la hauteur de l'écran de l'ordinateur
haut = fenetre.winfo_screenheight()
fenetre.geometry(str(larg)+'x'+str(haut)+'+0+0')    # redimensionnement de la fenetre par rapport au dimension de la fenetre
fenetre.configure(bg = "black")
canvas_back = Canvas(fenetre, width = 702,height = 702,bg= 'white')     #créeation d'un fond blanc plus grand de 2px par rapport a la fentre principal pour creer une bordure
canvas_back.place(x=larg/2,y=haut/2,anchor="center")
canvas = Canvas(fenetre,width=700,height=700,bg='black')
def fin_win():  #fin de la partie
    stop = 2
def barre_progress():   #fonction qui creer une barre de progression par rapport au niveau 
    global time,width
    if stop == 0:    #si le jeu est en marche 
        canvas.delete('progress')
        canvas.create_rectangle(5,5,695,15,fill="gray",tag="progress")
        width = width + (var_progress/2) 
        canvas.create_rectangle(5,5,width,15,fill="green",tag="progress")
        if width < 694.90:
            fenetre.after(500,barre_progress)
def save(): #fonction qui sauvegarde les donnée du joueur 
    save_w = open("save.txt","w")
    save_w.write(str(joueur.name)+'\n'+str(joueur.mdp)+'\n'+str(joueur.level)+'\n'+str(joueur.dead)+'\n'+str(joueur.high_score))
    save_w.close()
    try:    #essaye de sauvegarder les données en ligne
        url = "http://don-t-crash2.esy.es/python_modif.php?user="+str(joueur.name)+"&&mdp="+str(joueur.mdp)+"&&dead="+str(joueur.dead)+"&&level="+str(int(joueur.level))+"&&score="+str(joueur.high_score)+"&&version="+str(version)
        urlopen(url)
    except:
        pass
def arret(j):   #fonction qui arret la partie
    global stop,num_level,curseur_level
    if joueur.mode == "solo_level" or joueur.mode == "survie":  #si le jeu est en mode survie ou niveau en solo
        curseur_level = 0
        stop = 4
        joueur.cache()      #déplace le joueur or du champ de vision
        canvas.create_text(350,200,text="PERDU!",font = police + " 60 ",fill="blue",tag="fin")
        canvas.create_text(350,280,text="Space for start again",font = police + " 30 ",fill="white",tag="fin")
        canvas.create_text(350,320,text="Enter for return to the menu",font = police + " 30 ",fill="white",tag="fin")
        if joueur.high_score < joueur.score:
            joueur.high_score = joueur.score
        joueur.score = 0
        if joueur.mode == "solo_level":
            joueur.dead += 1 #ajoute une mort au joueur
        num_level -= 1
        if joueur.mode == "solo_level":
            canvas.delete("dead")
            canvas.create_text(600,75,text=joueur.dead,font = police + " 40 ",fill="white",tag="fin")
    elif joueur.mode== "multi" or joueur.mode =="multi_survie":
        if j == 1:
            joueur.stop = 1
            joueur.cache()
            if joueur.mode == "multi":
                joueur.dead_multi += 1
            canvas.delete("dead")
            if joueur.mode =="multi":
                canvas.create_text(100,75,text=joueur.dead_multi,font = police + " 40 ",fill=joueur.color,tag="dead")
                canvas.create_text(600,75,text=joueur2.dead_multi,font = police + " 40 ",fill=joueur2.color,tag="dead")
        elif j == 2:
            joueur2.stop = 1
            joueur2.cache()
            joueur2.dead_multi += 1
            canvas.delete("dead")
            if joueur.mode=="multi":
                canvas.create_text(100,75,text=joueur.dead_multi,font = police + " 40 ",fill=joueur.color,tag="dead")
                canvas.create_text(600,75,text=joueur2.dead_multi,font = police + " 40 ",fill=joueur2.color,tag="dead")
        if joueur.stop == 1 and joueur2.stop == 1:
            curseur_level = 0
            stop = 4
            if joueur.mode == "multi":
                canvas.create_text(350,200,text="PERDU!",font = police + " 60 ",fill="blue",tag="fin")
            elif joueur.mode=="multi_survie":
                if joueur2.score > joueur.score:
                    canvas.create_text(350,200,text="player 2 win!!",font = police + " 40 ",fill=joueur2.color,tag="fin")
                elif joueur.score > joueur2.score:
                    canvas.create_text(350,200,text="player 1 win!!",font = police + " 40 ",fill=joueur.color,tag="fin")
                else:
                    canvas.create_text(350,200,text="EQUALITY",font = police + " 40 ",fill="blue",tag="fin")
            canvas.create_text(350,280,text="Space for start again",font = police + " 30 ",fill="white",tag="fin")
            canvas.create_text(350,320,text="Enter for return to the menu",font = police + " 30 ",fill="white",tag="fin")
            num_level -= 1
            joueur.score = 0
            joueur2.score = 0
    elif joueur.mode=="multi_survie":
        if j == 1:
            joueur.stop = 1
            joueur.cache()
        elif j == 2:
            joueur2.stop = 1
            joueur2.cache()
            
        if joueur.stop == 1 and joueur2.stop == 1:
            curseur_level = 0
            stop = 4
            canvas.create_text(350,200,text="PERDU!",font = police + " 60 ",fill="blue",tag="fin")
            canvas.create_text(350,280,text="Space for start again",font = police + " 30 ",fill="white",tag="fin")
            canvas.create_text(350,320,text="Enter for return to the menu",font = police + " 30 ",fill="white",tag="fin")
            num_level -= 1
# Les classes
class Joueur(): 
    def __init__(self,coord,name,mdp,dead,vit,level,score,couleur,num_j):
        #coordonnées du joueur
        self.x = coord[0]
        self.y = coord[1]
        #meilleur score
        self.high_score = int(score)
        self.score = 0
        #vitesse de déplacement
        self.vitesse = vit
        # nombre de mort
        self.dead = int(dead)
        self.dead_multi = 0
        #identifiant
        self.name = name
        self.mdp = mdp
        self.stop = 0
        self.color = couleur
        #mode de jeu
        self.mode = "multi"
        self.level = int(level)
        #varaible pour le déplacement
        self.deplace_x = 0
        self.deplace_y = 0
        self.num_j = num_j
        self.joueur = canvas.create_rectangle(coord[0]-10,coord[1]-10,coord[0]+10,coord[1]+10,fill=couleur)
        #fonction de déplacement
        self.move_y()
        self.move_x()
    def cache(self):    #fonction pour cacher le joueur
        self.x = -800
        self.y=-800
        canvas.coords(self.joueur, self.x-10, self.y-10,self.x+10,self.y+10)
    def deplacement(self,event):
        if self.num_j == 1 :
            if self.mode == "multi" or self.mode == "multi_survie":
                joueur2.deplacement(event)
        touche = event.keysym
        global stop,curseur_level,time_anim,time,var_progress,width,curseur
        if stop == 0 and self.stop == 0 and self.num_j == 1:
            if touche == "Up":
                self.deplace_y = -1
            if touche == "Down":
                self.deplace_y = 1
            if touche == "Left":
                self.deplace_x = -1
            if touche == "Right":
                self.deplace_x = 1
        elif stop == 0 and self.stop == 0 and self.num_j == 2:
            if touche == "z" or touche == "Z":
                self.deplace_y = -1
            if touche == "s" or touche == "S":
                self.deplace_y = 1
            if touche == "q" or touche == "Q":
                self.deplace_x = -1
            if touche == "d" or touche == "D":
                self.deplace_x = 1
        elif stop == 2 and self.num_j == 1:
            if touche == "space":
                stop = 0
                curseur_level = 0
                time = 0
                time_anim = 0
                var_progress = 0
                width =5
                canvas.delete("fin")
                canvas.delete("progress")
                self.stop = 0
                joueur2.stop = 0
                self.x = 350
                self.y = 350
                if self.mode == "multi":
                    joueur2.x = 365
                    joueur2.y = 350
                    self.x = 335
                    self.y = 350
                    canvas.coords(joueur2.joueur, joueur2.x-10, joueur2.y-10,joueur2.x+10,joueur2.y+10)
                canvas.coords(self.joueur, self.x-10, self.y-10,self.x+10,self.y+10)
                jeu()
                barre_progress()
        elif stop == 3 and self.num_j == 1:
            if touche == "space":
                stop = 0
                self.stop = 0
                joueur2.stop = 0
                self.x = 350
                self.y = 350
                canvas.coords(self.joueur, self.x-10, self.y-10,self.x+10,self.y+10)
                if self.mode == "multi":
                    joueur2.x = 365
                    joueur2.y = 350
                    self.x = 335
                    self.y = 350
                    canvas.coords(joueur2.joueur, joueur2.x-10, joueur2.y-10,joueur2.x+10,joueur2.y+10)
                canvas.coords(self.joueur, self.x-10, self.y-10,self.x+10,self.y+10)
                canvas.delete("debut")
                canvas.delete("progress")
                width = 5
                jeu()
                barre_progress()
        elif stop == 4 and self.num_j == 1:
            if touche == "space":
                stop = 0
                curseur_level = 0
                time = 0
                time_anim = 0
                var_progress = 0
                width =5
                canvas.delete("fin")
                canvas.delete("progress")
                self.stop = 0
                joueur2.stop = 0
                self.x = 350
                self.y = 350

                if self.mode == "multi" or self.mode == "multi_survie":
                    joueur2.x = 365
                    joueur2.y = 350
                    self.x = 335
                    self.y = 350
                    canvas.coords(joueur2.joueur, joueur2.x-10, joueur2.y-10,joueur2.x+10,joueur2.y+10)
                canvas.coords(self.joueur, self.x-10, self.y-10,self.x+10,self.y+10)
                if self.mode == "survie" or self.mode == "multi_survie":
                    jeu_survie()
                else:
                    jeu()  
                    barre_progress()
        elif stop == 10 and self.num_j == 1:
            if touche == "space":
                stop = 0
                canvas.delete("debut")
                canvas.delete("progress")
                self.stop = 0
                joueur2.stop = 0
                self.x = 350
                self.y = 350
                if self.mode == "multi_survie":
                    joueur2.x = 365
                    joueur2.y = 350
                    self.x = 335
                    self.y = 350
                    canvas.coords(joueur2.joueur, joueur2.x-10, joueur2.y-10,joueur2.x+10,joueur2.y+10)
                canvas.coords(self.joueur, self.x-10, self.y-10,self.x+10,self.y+10)
                jeu_survie()  
        if stop == 4 or stop == 2 or stop == 5:
            if joueur.mode != "multi":
                save()
            if self.num_j == 1:
                if touche == "Return":
                    canvas.delete("fin")
                    canvas.delete("progress")
                    canvas.delete("score")
                    canvas.delete("dead")
                    joueur.dead_multi = 0
                    joueur2.dead_multi = 0
                    self.stop = 0
                    joueur2.stop = 0
                    self.cache()
                    joueur2.cache()
                    if self.mode == "solo_level" or self.mode == "multi":
                        nb_level = int(info_jeu[0].replace("\n",""))
                        level=1
                        x=50
                        y = 150
                        canvas.create_text(350, 50, text="Choix du niveau", font= str(police) + " 35  ", fill="red",tag="menu_level")
                        canvas.create_text(350, 100, text="retour", font= str(police) + " 30  ", fill="white",tag="menu_level")
                        canvas.create_text(x, y, text=level, font= str(police) + " 22  ", fill="blue",tag="menu_level")
                        canvas.bind("<Key>",menu_solo_level)
                        canvas.bind('<Button-1>',menu_solo_level)
                        curseur = 1
                        while level < nb_level:
                            level=level+1
                            x = x+50
                            if x > 650:
                                x = x - 650
                                y = y +50
                            if level <= joueur.level:
                                couleur = "white"
                            else:
                                couleur = "gray"
                            canvas.create_text(x, y, text=level, font= str(police) + " 22  ", fill=couleur,tag="menu_level")
                    else:
                        joueur2.cache()
                        joueur.cache()
                        joueur.mode=""
                        joueur2.mode=""
                        curseur=1
                        canvas.delete("menu")
                        canvas.create_text(350, 200, text="Jouer solo", font= str(police) + " 30  ", fill="blue",tag="menu")
                        canvas.create_text(350, 300, text="Multijoueur", font= str(police) + " 30  ", fill="white",tag="menu")
                        canvas.create_text(350, 400, text="Vers le site", font= str(police) + " 30  ", fill="white",tag="menu")
                        canvas.create_text(350, 500, text="Configuration", font= str(police) + " 30  ", fill="white",tag="menu")
                        canvas.create_text(350, 650, text="Quitter", font= str(police) + " 30  ", fill="white",tag="menu")
                        canvas.create_text(350, 100, text="Don't Crash 2", font= str(police) + " 40  ", fill="red",tag="title")
                        curseur = 1
                        canvas.bind("<Key>",menu_principal)
                        canvas.bind('<Button-1>',menu_principal)
    def fin_deplacement(self,event):
        if self.num_j == 1 :
            if self.mode == "multi" or self.mode == "multi_survie":
                joueur2.fin_deplacement(event)
        touche = event.keysym
        if self.num_j == 1:
            if touche == "Up" and self.deplace_y < 0:
                self.deplace_y = 0
            elif touche == "Down" and self.deplace_y > 0:
                self.deplace_y = 0
            elif touche == "Right" and self.deplace_x > 0:
                self.deplace_x = 0
            elif touche == "Left" and self.deplace_x < 0:
                self.deplace_x = 0
                
        else:
            if touche == "Z" and self.deplace_y  < 0:
                self.deplace_y = 0
            elif touche == "S" and self.deplace_y  > 0:
                self.deplace_y = 0
            elif touche == "z" and self.deplace_y  < 0:
                self.deplace_y = 0
            elif touche == "s" and self.deplace_y  > 0:
                self.deplace_y = 0
            elif touche == "Q" and self.deplace_x < 0:
                self.deplace_x = 0
            elif touche == "D" and self.deplace_x > 0:
                self.deplace_x = 0
            elif touche == "q" and self.deplace_x < 0:
                self.deplace_x = 0
            elif touche == "d" and self.deplace_x > 0:
                self.deplace_x = 0
    def move_y(self):
        if self.deplace_y != 0 and stop == 0 and self.stop == 0:
            if  self.deplace_y < 0:
                if self.y <= 10:
                    self.y=690
                else:
                    self.y = self.y-4
                    if self.num_j == 1 and self.y > joueur2.y-20 and  self.y < joueur2.y+20 and self.x > joueur2.x-20 and  self.x < joueur2.x+20:
                        self.y = joueur2.y+20
                    elif self.num_j == 2 and self.y >= joueur.y-20 and  self.y < joueur.y+20 and self.x > joueur.x-20 and  self.x < joueur.x+20:
                        self.y = joueur.y+20
                canvas.coords(self.joueur, self.x-10, self.y-10,self.x+10,self.y+10)
            elif  self.deplace_y > 0:
                if self.y >= 690:
                    self.y=10
                else:
                    self.y = self.y + 4
                    if self.num_j == 1 and self.y > joueur2.y-20 and  self.y < joueur2.y+20 and self.x > joueur2.x-20 and  self.x < joueur2.x+20:
                        self.y = joueur2.y-20
                    elif self.num_j == 2 and self.y > joueur.y-20 and  self.y < joueur.y+20 and self.x > joueur.x-20 and  self.x < joueur.x+20:
                        self.y = joueur.y-20
                canvas.coords(self.joueur, self.x-10, self.y-10,self.x+10,self.y+10)
        fenetre.after(15,self.move_y)
    def move_x(self):
        if self.deplace_x != 0 and stop == 0 and self.stop == 0:
            if self.deplace_x < 0:
                if self.x <= 10:
                    self.x=690
                else:
                    self.x= self.x - 4
                    if self.num_j == 1 and self.y > joueur2.y-20 and  self.y < joueur2.y+20 and self.x > joueur2.x-20 and  self.x < joueur2.x+20:
                        self.x = joueur2.x+20
                    elif self.num_j == 2 and self.y > joueur.y-20 and  self.y < joueur.y+20 and self.x > joueur.x-20 and  self.x < joueur.x+20:
                        self.x = joueur.x+20
            elif self.deplace_x > 0:
                if self.x >= 690:
                    self.x=10
                else:
                    self.x = self.x+4
                    if self.num_j == 1 and self.y > joueur2.y-20 and  self.y < joueur2.y+20 and self.x > joueur2.x-20 and  self.x < joueur2.x+20:
                        self.x = joueur2.x-20
                    elif self.num_j == 2 and self.y > joueur.y-20 and  self.y < joueur.y+20 and self.x > joueur.x-20 and  self.x < joueur.x+20:
                        self.x = joueur.x-20
            canvas.coords(self.joueur, self.x-10, self.y-10,self.x+10,self.y+10)
        fenetre.after(15,self.move_x)
class Cube():
    def __init__(self,coord,x,y,bg):
        self.x = coord[0]
        self.y = coord[1]
        self.deplace_x = x*2.5
        self.deplace_y = y*2.5
        self.bg = bg
        self.crea_cube()
        self.deplacement_cube()
    def crea_cube(self):
        self.cube = canvas.create_rectangle(self.x-10,self.y-10,self.x+10,self.y+10,fill=self.bg)
    def deplacement_cube(self):
        if stop == 0:
            self.x = self.x+ self.deplace_x
            self.y = self.y+ self.deplace_y
            canvas.coords(self.cube, self.x-10, self.y-10,self.x+10,self.y+10)
            if joueur.mode == "multi" or joueur.mode == "multi_survie":
                if self.x >= joueur.x - 20 and self.x <= joueur.x + 20 and self.y >= joueur.y - 20 and self.y <= joueur.y + 20 :
                        arret(1)
                elif self.x >= joueur2.x - 20 and self.x <= joueur2.x + 20 and self.y >= joueur2.y - 20 and self.y <= joueur2.y + 20 :
                        arret(2)
            else:
                if self.x >= joueur.x - 20 and self.x <= joueur.x + 20 and self.y >= joueur.y - 20 and self.y <= joueur.y + 20 :
                        arret(1)
            if self.x > -500 and self.x < 1200 and self.y > -500 and self.y < 1200:
                fenetre.after(50,self.deplacement_cube)
            else:
                canvas.delete(self.cube)
        elif stop != 0:
            canvas.delete(self.cube)
class Cube_follow():
    def __init__(self,coord,x,y,bg):
        self.x = coord[0]
        self.y = coord[1]
        self.dep_x = x
        self.dep_y = y
        self.bg = bg
        self.crea_cube()
        self.deplacement_cube()
    def crea_cube(self):
        self.cube = canvas.create_rectangle(self.x-20,self.y-20,self.x+20,self.y+20,fill=self.bg)
    def deplacement_cube(self):
        if stop == 0:
            if joueur.mode == "multi" or joueur.mode == "multi_survie":
                dist = sqrt(((self.x - joueur.x)**2)+((self.y - joueur.y)**2))
                dist2 = sqrt(((self.x - joueur2.x)**2)+((self.y - joueur2.y)**2))
                if dist2 > dist:
                    x = joueur.x
                    y = joueur.y
                else:
                    x = joueur2.x
                    y = joueur2.y
                if self.x > x :
                    self.x = self.x - (self.dep_x)
                elif self.x < x:
                    self.x= self.x + (self.dep_x)
                if self.y > y:
                    self.y = self.y - self.dep_y
                elif self.y < y :
                    self.y = self.y + self.dep_y
            elif joueur.mode != "multi" and joueur.mode != "multi_survie":
                x = joueur.x
                y = joueur.y
                if self.x > x :
                    self.x = self.x - (self.dep_x)
                elif self.x < x:
                    self.x= self.x + (self.dep_x)
                if self.y > y:
                    self.y = self.y - self.dep_y
                elif self.y < y :
                    self.y = self.y + self.dep_y
            canvas.coords(self.cube, self.x-10, self.y-10,self.x+10,self.y+10)
            if joueur.mode == "multi" or joueur.mode == "multi_survie":
                if self.x >= joueur.x - 20 and self.x <= joueur.x + 20 and self.y >= joueur.y - 20 and self.y <= joueur.y + 20:
                        arret(1)
                elif self.x >= joueur2.x - 20 and self.x <= joueur2.x + 20 and self.y >= joueur2.y - 20 and self.y <= joueur2.y + 20 :
                        arret(2)
            else:
                if self.x >= joueur.x - 20 and self.x <= joueur.x + 20 and self.y >= joueur.y - 20 and self.y <= joueur.y + 30 :
                        arret(1)
            if self.x > -500 and self.x < 1200 and self.y > -500 and self.y < 1200:
                fenetre.after(30,self.deplacement_cube)
            else:
                canvas.delete(self.cube)
        elif stop != 0:
            canvas.delete(self.cube)
class Cube_rot():
    def __init__(self,coord_or,angle,speed,dim,speed_ecart,dep_x,dep_y,mode_dep,time,bg):
        self.stop = 0
        self.vit = speed/100
        self.x_o = coord_or[0]
        self.y_o = coord_or[1]
        self.angle = angle
        self.dim = dim
        self.bg = bg
        self.x = (cos(self.angle)*self.dim)+self.x_o
        self.y = (sin(self.angle)*self.dim)+self.y_o
        self.speed_ecart = speed_ecart
        self.mode = mode_dep
        self.dep_x = dep_x
        self.dep_y = dep_y
        self
        self.time = time
        self.osi = 0
        self.crea_cube()
    def crea_cube(self):
        if self.time > 0 and stop == 0:
            self.time = self.time - 50
            fenetre.after(50,self.crea_cube)
        elif self.time <= 0 and stop == 0:
            self.cube = canvas.create_rectangle(self.x-10,self.y-10,self.x+10,self.y+10,fill=self.bg)
            self.rotation_cube()
    def rotation_cube(self):
        if stop == 0:
            self.y_bis = self.y
            self.x_bis = self.x
            self.angle = self.angle + self.vit
            self.dim = self.dim + self.speed_ecart
            self.x = (cos(self.angle)*self.dim)+self.x_o
            self.y = (sin(self.angle)*self.dim)+self.y_o
            if self.mode == 1:
                self.x_o = self.x_o + self.dep_x
                self.y_o = self.y_o+self.dep_y
            if self.mode == 2:
                if self.dim < 20:
                    canvas.delete(self.cube)
                    self.stop = 1
                    self.mode=0
            if self.mode == 3:
                self.x_o = self.x_o + self.dep_x
                self.y_o = self.y_o+self.dep_y
                if self.y_o > 625 or self.y_o < 75 or self.x_o > 625 or self.x_o < 75:
                    self.dep_x = -self.dep_x
                    self.dep_y = -self.dep_y
            if self.mode == 4:
                self.x_bis = self.x_bis + self.dep_x
                self.osi = self.osi + self.dep_x
                self.y_bis = 100*cos(self.osi/50)
                self.x = self.x_bis
                self.y = self.y_bis+self.y_o
            if self.mode == 5:
                self.y_bis = self.y_bis + self.dep_x
                self.osi = self.osi + self.dep_x
                self.x_bis = 100*cos(self.osi/50)
                self.x = self.x_bis + self.x_o
                self.y = self.y_bis
            if self.mode == 6:
                if joueur.mode != "multi" and joueur.mode != "multi_survie":
                    dist = sqrt(((self.x_o - joueur.x)**2)+((self.y_o - joueur.y)**2))
                    dist2 = sqrt(((self.x_o - joueur2.x)**2)+((self.y_o - joueur2.y)**2))
                    if dist2 > dist:
                        x = joueur.x
                        y = joueur.y
                    else:
                        x = joueur.x
                        y = joueur.y
                    if self.x > x :
                        self.x_o = self.x_o - (self.dep_x)
                    elif self.x < x:
                        self.x_o = self.x_o + (self.dep_x)
                    if self.y > y:
                        self.y_o = self.y_o - self.dep_y
                    elif self.y < y :
                        self.y_o = self.y_o + self.dep_y
            canvas.coords(self.cube, self.x-10, self.y-10,self.x+10,self.y+10)
            if joueur.mode == "multi" or joueur.mode == "multi_survie":
                if self.x >= joueur.x - 20 and self.x <= joueur.x + 20 and self.y >= joueur.y - 20 and self.y <= joueur.y + 20 :
                        arret(1)
                elif self.x >= joueur2.x - 20 and self.x <= joueur2.x + 20 and self.y >= joueur2.y - 20 and self.y <= joueur2.y + 20 :
                        arret(2)
            else:
                if self.x >= joueur.x - 20 and self.x <= joueur.x + 20 and self.y >= joueur.y - 20 and self.y <= joueur.y + 20 :
                        arret(1)
            if self.x > -500 and self.x < 1200 and self.y > -500 and self.y < 1200:
                if self.stop == 0:
                    fenetre.after(50,self.rotation_cube)
            elif self.mode == 2:
                fenetre.after(50,self.rotation_cube)
            else:
                canvas.delete(self.cube)
        elif stop != 0:
            canvas.delete(self.cube)

#carré
class Jeu_1():
    def __init__(self,x,y,dim,vit):
     
        bg =choice(couleur)
        angle = 0.02
        mode = 0
        Cube_rot((x,y),pi/4,angle,dim,vit,vit,0,mode,0,bg)
        Cube_rot((x,y),0,angle,(sqrt(2)/2)*dim,sqrt(2)*vit/2,vit,vit,mode,0,bg)
        Cube_rot((x,y),3*pi/4,angle,dim,vit,vit,0,mode,0,bg)
        Cube_rot((x,y),pi/2,angle,(sqrt(2)/2)*dim,sqrt(2)*vit/2,vit,vit,mode,0,bg)
        Cube_rot((x,y),-3*pi/4,angle,dim,vit,vit,0,mode,0,bg)
        Cube_rot((x,y),pi,angle,(sqrt(2)/2)*dim,sqrt(2)*vit/2,vit,vit,mode,0,bg)
        Cube_rot((x,y),-pi/4,angle,dim,vit,0,vit,mode,0,bg)
        Cube_rot((x,y),-pi/2,angle,(sqrt(2)/2)*dim,sqrt(2)*vit/2,vit,vit,mode,0,bg)
        
#cercle
class Jeu_2():
    def __init__(self,x,y,dim,vit,nb):
        bg =choice(couleur)
        angle = 0
        angle_2 = (2*pi)/nb
        Cube_rot((x,y),angle,0,dim,vit,0,0,0,0,bg)
        while nb > 1:
            nb = nb - 1
            angle = angle + angle_2
            Cube_rot((x,y),angle,0,dim,vit,0,0,0,0,bg)
#triangle
class Jeu_3():
    def __init__(self,x,y,dim,vit):
        
        angle = 0
        bg= choice(couleur)

        Cube_rot((x,y),pi/2,angle,dim,0,0,vit,1,0,bg)
        Cube_rot((x,y),-5*pi/6,angle,dim,0,vit*-sqrt(3)/2,vit*-1/2,1,0,bg)
        Cube_rot((x,y),-pi/6,angle,dim,0,vit*sqrt(3)/2,vit*-1/2,1,0,bg)

        Cube_rot((x,y),pi/6,angle,dim/2,0,vit*sqrt(3)/4,vit*1/4,1,0,bg)
        Cube_rot((x,y),5*pi/6,angle,dim/2,0,vit*-sqrt(3)/4,vit*1/4,1,0,bg)
        Cube_rot((x,y),-pi/2,angle,dim/2,0,0,-vit/2,1,0,bg)
        
#fleche croisement
class Jeu_4():
    def __init__(self,vit):
        
        bg =choice(couleur)
            
        Cube((-300,400),vit,0,bg)
        Cube((-250,450),vit,0,bg)
        Cube((-200,500),vit,0,bg)
        Cube((-150,550),vit,0,bg)
        Cube((-100,600),vit,0,bg)
        Cube((-50,650),vit,0,bg)
        
        Cube((-350,350),vit,0,bg)
        
        Cube((-300,300),vit,0,bg)
        Cube((-250,250),vit,0,bg)
        Cube((-200,200),vit,0,bg)
        Cube((-150,150),vit,0,bg)
        Cube((-100,100),vit,0,bg)
        Cube((-50,50),vit,0,bg)

        Cube((1000,400),-vit,0,bg)
        Cube((950,450),-vit,0,bg)
        Cube((900,500),-vit,0,bg)
        Cube((850,550),-vit,0,bg)
        Cube((800,600),-vit,0,bg)
        Cube((750,650),-vit,0,bg)
        
        Cube((1050,350),-vit,0,bg)
        
        Cube((1000,300),-vit,0,bg)
        Cube((950,250),-vit,0,bg)
        Cube((900,200),-vit,0,bg)
        Cube((850,150),-vit,0,bg)
        Cube((800,100),-vit,0,bg)
        Cube((750,50),-vit,0,bg)
#ligne croisement
class Jeu_5():
    def __init__(self,vit):
     
        bg =choice(couleur)
            
        Cube((-20,125),vit,0,bg)
        Cube((-20,250),vit,0,bg)
        Cube((-20,450),vit,0,bg)
        Cube((-20,575),vit,0,bg)
        Cube((-20,30),vit,0,bg)
        Cube((-20,670),vit,0,bg)

        Cube((720,125),-vit,0,bg)
        Cube((720,250),-vit,0,bg)
        Cube((720,450),-vit,0,bg)
        Cube((720,575),-vit,0,bg)
        Cube((720,30),-vit,0,bg)
        Cube((720,670),-vit,0,bg)

        Cube((125,-20),0,vit,bg)
        Cube((250,-20),0,vit,bg)
        Cube((450,-20),0,vit,bg)
        Cube((575,-20),0,vit,bg)
        Cube((30,-20),0,vit,bg)
        Cube((670,-20),0,vit,bg)

        Cube((125,720),0,-vit,bg)
        Cube((250,720),0,-vit,bg)
        Cube((450,720),0,-vit,bg)
        Cube((575,720),0,-vit,bg)
        Cube((30,720),0,-vit,bg)
        Cube((670,720),0,-vit,bg)
#cercle + rotation
class Jeu_6():
    def __init__(self,coord,dim,speed,nb,ecart,dep_x,dep_y,mode):
        bg =choice(couleur)
        
        Cube_rot(coord,0,speed,dim,ecart,dep_x,dep_y,mode,0,bg)
        angle = 0
        angle_2 = (2*pi)/nb
        while nb > 1:
            nb = nb - 1
            angle = angle + angle_2
            Cube_rot(coord,angle,speed,dim,ecart,dep_x,dep_y,mode,0,bg)
class Jeu_7():
    def __init__(self,coord,speed,ecart,taille,ecart_2,mode):
        bg =choice(couleur)
        angle = 0
        taille_2 = 0
        Cube_rot(coord,angle,-speed,400,ecart,0,0,mode,0,bg)
        while taille > 0:
            taille = taille - 1
            taille_2 = taille_2 + ecart_2
            angle = angle + pi/6
            Cube_rot(coord,angle,-speed,400+taille_2,ecart,0,0,mode,0,bg)
class Jeu_8():
    def __init__(self,coord,dim,taille,speed,ecart,ecart_time,mode):
        bg =choice(couleur)
        time = 0
        Cube_rot(coord,0,-speed,dim,ecart,0,0,mode,0,bg)
        while taille > 0:
            taille = taille -1
            time = time + ecart_time
            Cube_rot(coord,0,-speed,dim,ecart,0,0,mode,time,bg)
class Jeu_9():
    def __init__(self,coord,dim,taille,angle,ecart,ecart_time,mode):
        bg =choice(couleur)
        time = 0
        angle2 = 0
        Cube_rot(coord,angle2,0,dim,ecart,0,0,mode,0,bg)
        while taille > 0:
            angle2 = angle2 + (pi/(angle*2))
            taille = taille -1
            time = time + ecart_time
            Cube_rot(coord,angle2,0,dim,ecart,0,0,mode,time,bg)
class Jeu_10():
    def __init__(self,coord,taille,speed,ecart_time,mode):
        bg =choice(couleur)
        time = 0
        Cube_rot(coord,0,0,0,0,speed,0,mode,0,bg)
        while taille > 0:
            taille -= 1
            time = time + ecart_time
            Cube_rot(coord,0,0,0,0,speed,0,mode,time,bg)
class Jeu_11():
    def __init__(self,coord,coord2,inter,num_ter,num_ter2):
     
        bg =choice(couleur)
        long = coord2[0] - coord[0]
        long2 = coord2[1] - coord[1]
        nb_cube = long//inter
        nb_cube2 = long2//inter
        long_inter_cube = long/nb_cube
        long_inter_cube2 = long2/nb_cube2
        ecart = 0
        ecart2 = 0
        nume1 = 2
        nume2 = nb_cube + 1
        nume3 = 2*nb_cube + nb_cube2
        nume4 = 2*nb_cube + 2*nb_cube2
        while nb_cube >= 0:
            if nume1 > num_ter and nume1 < num_ter2:
                er=1
            else:
                Cube((coord[0]+ecart,coord[1]),0,0,bg)
            if nume3 > num_ter and nume3 < num_ter2:
                er=1
            else:
                Cube((coord[0]+ecart,coord2[1]),0,0,bg)
            ecart = ecart + long_inter_cube
            nume1 += 1
            nume3 -= 1
            nb_cube -= 1
        while nb_cube2 >= 0:
            if nume4 > num_ter and nume4 < num_ter2:
                er=1
            else:
                Cube((coord[0],coord[1]+ecart2),0,0,bg)
                dd=1
            if nume2 > num_ter and nume2 < num_ter2:
                er=1
            else:
                Cube((coord2[0],coord[1]+ecart2),0,0,bg)
                dd=1
            ecart2 = ecart2 + long_inter_cube2
            nume2 += 1
            nume4 -= 1
            nb_cube2 -= 1
class Jeu_12():
    def __init__(self,coord,dim,inter,num_ter,num_ter2,mode):
     
        bg =choice(couleur)
        if mode == 1:
            long = dim - coord[0]
            nb_cube = long//inter
            long_inter_cube = long/nb_cube
            ecart = 0
            nume1 = 1
            while nb_cube >= 0:
                if nume1 > num_ter and nume1 < num_ter2:
                    er=1
                else:
                    Cube((coord[0]+ecart,coord[1]),0,0,bg)
                ecart = ecart + long_inter_cube
                nume1 += 1
                nb_cube -= 1
        elif mode == 2:
            long = dim - coord[1]
            nb_cube = long//inter
            long_inter_cube = long/nb_cube
            ecart = 0
            nume1 = 1
            while nb_cube >= 0:
                if nume1 > num_ter and nume1 < num_ter2:
                    er=1
                else:
                    Cube((coord[0],coord[1]+ecart),0,0,bg)
                ecart = ecart + long_inter_cube
                nume1 += 1
                nb_cube -= 1
class Jeu_13():
    def __init__(self,coord,dim,inter,num_ter,num_ter2,vit,mode):
     
        bg =choice(couleur)
        if mode == 1:
            long = dim - coord[0]
            nb_cube = long//inter
            long_inter_cube = long/nb_cube
            ecart = 0
            nume1 = 1
            while nb_cube >= 0:
                if nume1 > num_ter and nume1 < num_ter2:
                    er=1
                else:
                    Cube_rot((coord[0]+ecart,coord[1]),0,0,0,0,0,vit,1,0,bg)
                ecart = ecart + long_inter_cube
                nume1 += 1
                nb_cube -= 1
        elif mode == 2:
            long = dim - coord[1]
            nb_cube = long//inter
            long_inter_cube = long/nb_cube
            ecart = 0
            nume1 = 1
            while nb_cube >= 0:
                if nume1 > num_ter and nume1 < num_ter2:
                    er=1
                else:
                    Cube_rot((coord[0],coord[1]+ecart),0,0,0,0,vit,0,1,0,bg)
                ecart = ecart + long_inter_cube
                nume1 += 1
                nb_cube -= 1
class Jeu_14():
    def __init__(self,coord,dep_x,dep_y):
        bg =choice(couleur)
        Cube_follow(coord,dep_x,dep_y,bg)
class Jeu_15():
    def __init__(self,coord,dim,speed,nb,ecart,dep_x,dep_y,mode):
        bg =choice(couleur)
        
        angle = 0
        angle_2 = (2*pi)/nb
        angle = angle + angle_2
        while nb > 2:
            nb = nb - 1
            angle = angle + angle_2
            Cube_rot(coord,angle,speed,dim,ecart,dep_x,dep_y,mode,0,bg)
def jeu_horloge():
    global time_anim
    if time_anim > 0 and stop == 0:
        time_anim = time_anim - 200
        fenetre.after(200,jeu_horloge)
    elif time_anim <= 0 and stop == 0:
        time_anim = 0
        jeu()
def jeu_horloge_survie():
    global time_anim
    if joueur.mode == "survie" and stop==0:
        joueur.score += 35
        canvas.delete("score")
        canvas.create_text(600,75,text=joueur.score,font=police + " 30 ",tag="score",fill=joueur.color)
    elif joueur.mode == "multi_survie" and stop==0:
        if joueur.stop == 0:
            joueur.score += 35
        if joueur2.stop == 0:
            joueur2.score += 35
        canvas.delete("score")
        canvas.create_text(100,75,text=joueur.score,font=police + " 30 ",tag="score",fill=joueur.color)
        canvas.create_text(600,75,text=joueur2.score,font=police + " 30 ",tag="score",fill=joueur2.color)
    if time_anim > 0 and stop == 0:
        time_anim = time_anim - 200
        fenetre.after(200,jeu_horloge_survie)
    elif time_anim <= 0 and stop == 0:
        time_anim = 0
        jeu_survie()
def jeu():
    global curseur_level,time,time_anim,var_progress,stop,info_level,width,num_level
    if stop == 0:
        if curseur_level == 0:
            try:
                num_level = num_level +1
                level = open("solo_level/level_"+str(num_level)+".txt","r")
                info_level = level.readlines()
                level.close()
                time = int(info_level[0].replace("/n",""))
                var_progress = 690 / time
                curseur_level = 2
                stop = 3
                canvas.create_text(350,200,text="Press space to start",font = police + " 40 ",fill="white",tag="debut")
                if joueur.mode == "solo_level":
                    canvas.create_text(600,75,text=joueur.dead,font = police + " 40 ",fill=joueur.color,tag="dead")
                elif  joueur.mode == "multi":
                    canvas.create_text(100,75,text=joueur.dead_multi,font = police + " 40 ",fill=joueur.color,tag="dead")
                    canvas.create_text(600,75,text=joueur2.dead_multi,font = police + " 40 ",fill=joueur2.color,tag="dead")              
            except:
                canvas.create_text(350,200,text="Vous avez finit les niveaux !!! ",font = police + " 40 ",fill="white",tag="fin")
                stop = 5
        else:
            type_jeu = int(info_level[curseur_level].replace("/n",""))
            if type_jeu == 1:
                x= int(info_level[curseur_level+1].replace("/n",""))
                y= int(info_level[curseur_level+2].replace("/n",""))
                dim= int(info_level[curseur_level+3].replace("/n",""))
                vit= int(info_level[curseur_level+4].replace("/n",""))
                Jeu_1(x,y,dim,vit)
                time_anim = int(info_level[curseur_level+6].replace("/n","")) 
                curseur_level = curseur_level+8
                jeu_horloge()
            elif type_jeu == 2:
                x= int(info_level[curseur_level+1].replace("/n",""))
                y= int(info_level[curseur_level+2].replace("/n",""))
                dim= int(info_level[curseur_level+3].replace("/n",""))
                vit= int(info_level[curseur_level+4].replace("/n",""))
                nb = int(info_level[curseur_level+5].replace("/n",""))
                Jeu_2(x,y,dim,vit,nb)
                time_anim = int(info_level[curseur_level+7].replace("/n","")) 
                curseur_level = curseur_level+9
                jeu_horloge()
            elif type_jeu == 3:
                x= int(info_level[curseur_level+1].replace("/n",""))
                y= int(info_level[curseur_level+2].replace("/n",""))
                dim= int(info_level[curseur_level+3].replace("/n",""))
                vit= int(info_level[curseur_level+4].replace("/n",""))
                Jeu_3(x,y,dim,vit)
                time_anim = int(info_level[curseur_level+6].replace("/n","")) 
                curseur_level = curseur_level+8
                jeu_horloge()
            elif type_jeu == 4:
                vit= int(info_level[curseur_level+1].replace("/n",""))
                Jeu_4(vit)
                time_anim = int(info_level[curseur_level+3].replace("/n","")) 
                curseur_level = curseur_level+5
                jeu_horloge()
            elif type_jeu == 5:
                vit= int(info_level[curseur_level+1].replace("/n",""))
                Jeu_5(vit)
                time_anim = int(info_level[curseur_level+3].replace("/n","")) 
                curseur_level = curseur_level+5
                jeu_horloge()
            elif type_jeu == 6:
                x= int(info_level[curseur_level+1].replace("/n",""))
                y= int(info_level[curseur_level+2].replace("/n",""))
                dim= int(info_level[curseur_level+3].replace("/n",""))
                angle_speed= int(info_level[curseur_level+4].replace("/n",""))
                ecart = int(info_level[curseur_level+5].replace("/n",""))
                dep_x = int(info_level[curseur_level+6].replace("/n",""))
                dep_y = int(info_level[curseur_level+7].replace("/n",""))
                mode = int(info_level[curseur_level+8].replace("/n",""))
                nb = int(info_level[curseur_level+9].replace("/n",""))
                Jeu_6((x,y),dim,angle_speed,nb,ecart,dep_x,dep_y,mode)
                time_anim = int(info_level[curseur_level+11].replace("/n","")) 
                curseur_level = curseur_level+13
                jeu_horloge()
            elif type_jeu == 7:
                x= int(info_level[curseur_level+1].replace("/n",""))
                y= int(info_level[curseur_level+2].replace("/n",""))
                nb_cube= int(info_level[curseur_level+3].replace("/n",""))
                angle_speed= int(info_level[curseur_level+4].replace("/n",""))
                ecart = int(info_level[curseur_level+5].replace("/n",""))
                ecart_cube = int(info_level[curseur_level+6].replace("/n",""))
                mode = int(info_level[curseur_level+7].replace("/n",""))
                
                Jeu_7((x,y),angle_speed,ecart,nb_cube,ecart_cube,mode)
                time_anim = int(info_level[curseur_level+9].replace("/n","")) 
                curseur_level = curseur_level+11
                jeu_horloge()
            elif type_jeu == 8:
                x= int(info_level[curseur_level+1].replace("\n",""))
                y= int(info_level[curseur_level+2].replace("\n",""))
                dim= int(info_level[curseur_level+3].replace("\n",""))
                nb_cube= int(info_level[curseur_level+4].replace("\n",""))
                angle_speed= int(info_level[curseur_level+5].replace("\n",""))
                ecart = int(info_level[curseur_level+6].replace("\n",""))/10
                ecart_time = int(info_level[curseur_level+7].replace("\n",""))
                mode = int(info_level[curseur_level+8].replace("\n",""))
                
                Jeu_8((x,y),dim,nb_cube,angle_speed,ecart,ecart_time,mode)
                time_anim = int(info_level[curseur_level+10].replace("/n","")) 
                curseur_level = curseur_level+12
                jeu_horloge()
            elif type_jeu == 9:
                x= int(info_level[curseur_level+1].replace("\n",""))
                y= int(info_level[curseur_level+2].replace("\n",""))
                dim= int(info_level[curseur_level+3].replace("\n",""))
                nb_cube= int(info_level[curseur_level+4].replace("\n",""))
                angle_speed= int(info_level[curseur_level+5].replace("\n",""))
                ecart = int(info_level[curseur_level+6].replace("\n",""))
                ecart_time = int(info_level[curseur_level+7].replace("\n",""))
                mode = int(info_level[curseur_level+8].replace("\n",""))
                
                Jeu_9((x,y),dim,nb_cube,angle_speed,ecart,ecart_time,mode)
                time_anim = int(info_level[curseur_level+10].replace("/n","")) 
                curseur_level = curseur_level+12
                jeu_horloge()
            elif type_jeu == 10:
                x= int(info_level[curseur_level+1].replace("\n",""))
                y= int(info_level[curseur_level+2].replace("\n",""))
                vit = int(info_level[curseur_level+3].replace("\n",""))
                nb_cube= int(info_level[curseur_level+4].replace("\n",""))
                ecart_time = int(info_level[curseur_level+5].replace("\n",""))
                mode = int(info_level[curseur_level+6].replace("\n",""))
                
                Jeu_10((x,y),nb_cube,vit,ecart_time,mode)
                time_anim = int(info_level[curseur_level+8].replace("/n","")) 
                curseur_level = curseur_level+10
                jeu_horloge()
            elif type_jeu == 11:
                x= int(info_level[curseur_level+1].replace("\n",""))
                y= int(info_level[curseur_level+2].replace("\n",""))
                x2 = int(info_level[curseur_level+3].replace("\n",""))
                y2= int(info_level[curseur_level+4].replace("\n",""))
                inter = int(info_level[curseur_level+5].replace("\n",""))
                num_ter = int(info_level[curseur_level+6].replace("\n",""))
                num_ter2 = int(info_level[curseur_level+7].replace("\n",""))
                
                Jeu_11((x,y),(x2,y2),inter,num_ter,num_ter2)
                time_anim = int(info_level[curseur_level+9].replace("/n","")) 
                curseur_level = curseur_level+11
                jeu_horloge()
            elif type_jeu == 12:
                x= int(info_level[curseur_level+1].replace("\n",""))
                y= int(info_level[curseur_level+2].replace("\n",""))
                dim = int(info_level[curseur_level+3].replace("\n",""))
                inter = int(info_level[curseur_level+4].replace("\n",""))
                num_ter = int(info_level[curseur_level+5].replace("\n",""))
                num_ter2 = int(info_level[curseur_level+6].replace("\n",""))
                mode = int(info_level[curseur_level+7].replace("\n",""))
                
                Jeu_12((x,y),dim,inter,num_ter,num_ter2,mode)
                time_anim = int(info_level[curseur_level+9].replace("/n","")) 
                curseur_level = curseur_level+11
                jeu_horloge()
            elif type_jeu == 13:
                x= int(info_level[curseur_level+1].replace("\n",""))
                y= int(info_level[curseur_level+2].replace("\n",""))
                dim = int(info_level[curseur_level+3].replace("\n",""))
                inter = int(info_level[curseur_level+4].replace("\n",""))
                num_ter = int(info_level[curseur_level+5].replace("\n",""))
                num_ter2 = int(info_level[curseur_level+6].replace("\n",""))
                vit = int(info_level[curseur_level+7].replace("\n",""))
                mode = int(info_level[curseur_level+8].replace("\n",""))
                
                Jeu_13((x,y),dim,inter,num_ter,num_ter2,vit,mode)
                time_anim = int(info_level[curseur_level+10].replace("/n","")) 
                curseur_level = curseur_level+12
                jeu_horloge()
            if type_jeu == 14:
                x= int(info_level[curseur_level+1].replace("/n",""))
                y= int(info_level[curseur_level+2].replace("/n",""))
                dep_x= int(info_level[curseur_level+3].replace("/n",""))
                dep_y= int(info_level[curseur_level+4].replace("/n",""))
                Jeu_14((x,y),dep_x,dep_y)
                time_anim = int(info_level[curseur_level+6].replace("/n","")) 
                curseur_level = curseur_level+8
                jeu_horloge()
            elif type_jeu == 15:
                x= int(info_level[curseur_level+1].replace("/n",""))
                y= int(info_level[curseur_level+2].replace("/n",""))
                dim= int(info_level[curseur_level+3].replace("/n",""))
                angle_speed= int(info_level[curseur_level+4].replace("/n",""))
                ecart = int(info_level[curseur_level+5].replace("/n",""))
                dep_x = int(info_level[curseur_level+6].replace("/n",""))
                dep_y = int(info_level[curseur_level+7].replace("/n",""))
                mode = int(info_level[curseur_level+8].replace("/n",""))
                nb = int(info_level[curseur_level+9].replace("/n",""))
                Jeu_15((x,y),dim,angle_speed,nb,ecart,dep_x,dep_y,mode)
                time_anim = int(info_level[curseur_level+11].replace("/n","")) 
                curseur_level = curseur_level+13
                jeu_horloge()
            elif stop == 0:
                if width >= 610:
                    if type_jeu == 999:
                        stop = 2
                        joueur.cache()
                        joueur2.cache()
                        curseur_level = 0
                        canvas.create_text(350,200,text="Gagné!!",font = police + " 60 ",fill="red",tag="fin")
                        canvas.create_text(350,280,text="Press space for the next level",font = police + " 30 ",fill="white",tag="fin")
                        canvas.create_text(350,320,text="Enter for return to the menu",font = police + " 30 ",fill="white",tag="fin")
                        if num_level == joueur.level:
                            joueur.level = joueur.level + 1
def jeu_survie():
    global curseur_level,time,time_anim,var_progress,stop,info_level,width,vit1,vit2,time1,time2,play
    #definition des variable de vitesse et temps d'apparion
    if joueur.score < 70:
        vit1 = 4
        vit2 = 2
        time1 = 2000
        time2 = 5500
        play = 0
    if stop == 0: # si le jeu est en marche
        if curseur_level == 0: 
            play += 1 # ajout un au nombre de figure lancé
            if play >= 5: #augmante la difficulté toute les 5 figures
                play = 0
                vit1 += 1
                vit2 += 1
                time1 -= 200
                time2 -= 300
            type_jeu = randint(1,10)
            time = randint(time1,time2)
            # si le types du jeu est égal a 1
            if type_jeu == 1:
                ale =randint(0,1)
                if ale == 0:
                    vit= randint (vit2,vit1)
                else:
                    vit= randint (-vit1,-vit2)
                x= randint(20,550) #position aléatoire
                y= randint (20,550)
                dim= randint (50,400) #dimension aléatoire
                Jeu_1(x,y,dim,vit) # on appelle la figure 1
                time_anim = randint (time1,time2) #temps avant la prochaine figure aléatoire
                jeu_horloge_survie()
            elif type_jeu == 2:
                ale =randint(0,1)
                if ale == 0:
                    vit= randint (vit2,vit1)
                else:
                    vit= randint (-vit1,-vit2)
                x= randint (20,550)
                y= randint (20,550)
                dim= randint (50,400)
                nb = randint (5,17)
                Jeu_2(x,y,dim,vit,nb)
                time_anim = randint (time1,time2)
                jeu_horloge_survie()
            elif type_jeu == 3:
                ale=randint(0,1)
                if ale == 0:
                    vit= randint (vit2,vit1)
                else:
                    vit= randint (-vit1,-vit2)
                x= randint (20,550)  
                y= randint (20,550)
                dim= randint (50,400)
                Jeu_3(x,y,dim,vit)
                time_anim = randint (time1,time2)
                jeu_horloge_survie()
            elif type_jeu == 4:
                vit= randint (1,6)
                Jeu_4(vit)
                time_anim = randint (time1,time2)
                jeu_horloge_survie()
            elif type_jeu == 5:
                ale=randint(0,1)
                if ale == 0:
                    vit= randint (vit2,vit1)
                else:
                    vit= randint (-vit1,-vit2)
                Jeu_5(vit)
                time_anim = randint (time1,time2)
                jeu_horloge_survie()
            elif type_jeu == 6:
                x= randint (20,550)
                y= randint (20,550)
                dim= randint (50,400)
                angle_speed= randint (2,6)
                ale2= randint (0,1)
                if ale2==0:
                    ecart= randint(vit2,vit1)
                else:
                    ecart= randint (-vit1,-vit2)
                dep_x = randint (-5,5)
                dep_y = randint (-5,5)
                mode = randint (0,2)
                nb = randint (6,16)
                Jeu_6((x,y),dim,angle_speed,nb,ecart,dep_x,dep_y,mode)
                time_anim = randint (time1,time2)
                jeu_horloge_survie()
            elif type_jeu == 7:
                x= randint (20,550)
                y= randint (20,550)
                nb_cube= int(randint (20,50))
                angle_speed= randint (2,6)
                ale2= randint (0,1)
                if ale2==0:
                    ecart= randint(vit2,vit1)
                else:
                    ecart= randint (-vit1,-vit2)
                ecart_cube = randint (50,150)
                mode = randint (0,2) 
                Jeu_7((x,y),angle_speed,ecart,nb_cube,ecart_cube,mode)
                time_anim = randint (time1,time2)
                jeu_horloge_survie()
            elif type_jeu == 8:
                x= randint(20,550)
                y= randint (20,550)
                dim= randint (50,400)
                nb_cube= randint (20,50) 
                angle_speed= randint (2,6)
                ecart= randint (1,8)
                ecart_time = randint (50,150)
                mode = randint (0,2) 
                Jeu_8((x,y),dim,nb_cube,angle_speed,ecart,ecart_time,mode)
                time_anim = randint(time1,time2)
                jeu_horloge_survie()
            elif type_jeu == 9:
                x= randint(20,550)
                y= randint (20,550)
                dim= randint (50,400)
                nb_cube= randint(50,100)
                angle_speed= randint (2,6)
                ecart = randint (1,8)
                ecart_time = randint (50,150)
                mode = 0
                Jeu_9((x,y),dim,nb_cube,angle_speed,ecart,ecart_time,mode)
                time_anim = randint(time1,time2)
                jeu_horloge_survie()
            elif type_jeu == 10:
                x= randint(100,450) 
                y= randint (100,450)
                ale= randint(0,1)
                if ale==0:
                    vit= randint(vit2,vit1)
                else:
                    vit= randint(-vit1,-vit2)
                nb_cube= randint (25,175) 
                ecart_time = randint (50,150)
                mode = randint (4,5)
                Jeu_10((x,y),nb_cube,vit,ecart_time,mode)
                time_anim = randint(time1,time2)
                jeu_horloge_survie()
def menu_solo(event):
    global curseur,mode_jeu,stop
    touche = event.keysym
    canvas.delete("menu")
    if touche == "Down":
        curseur = curseur + 1
        if curseur > 3:
            curseur = 1
    elif touche == "Up":
        curseur = curseur -1
        if curseur < 1:
            curseur = 3
    canvas.create_text(350, 100, text="Choix du mode", font= str(police) + " 40  ", fill="red",tag="menu")
    if curseur == 1:
        canvas.create_text(350, 275, text="Mode niveaux", font= str(police) + " 30  ", fill="blue",tag="menu")
    else:
        canvas.create_text(350, 275, text="Mode niveaux", font= str(police) + " 30  ", fill="white",tag="menu")
    if curseur == 2:
        canvas.create_text(350, 350, text="Mode survie", font= str(police) + " 30  ", fill="blue",tag="menu")
    else:
        canvas.create_text(350, 350, text="Mode survie", font= str(police) + " 30  ", fill="white",tag="menu")
    if curseur == 3:
        canvas.create_text(350, 425, text="retour", font= str(police) + " 30  ", fill="blue",tag="menu")
    else:
        canvas.create_text(350, 425, text="retour", font= str(police) + " 30  ", fill="white",tag="menu")
    if touche == "??":
        if event.y > 240 and event.y < 310:
            if joueur.mode=="solo":
                joueur.mode = "solo_level"
                joueur2.mode = "solo_level"
            canvas.delete("menu")
            canvas.delete("title")
            nb_level = int(info_jeu[0].replace("\n",""))
            level=1
            x=50
            y = 150
            canvas.create_text(350, 50, text="Choix du niveau", font= str(police) + " 35  ", fill="red",tag="menu_level")
            canvas.create_text(350, 100, text="retour", font= str(police) + " 30  ", fill="white",tag="menu_level")
            canvas.create_text(x, y, text=level, font= str(police) + " 22  ", fill="blue",tag="menu_level")
            canvas.bind("<Key>",menu_solo_level)
            canvas.bind('<Button-1>',menu_solo_level)
            curseur = 1
            while level < nb_level:
                level=level+1
                x = x+50
                if x > 650:
                    x = x - 650
                    y = y +50
                if level <= joueur.level:
                    couleur = "white"
                else:
                    couleur = "gray"
                canvas.create_text(x, y, text=level, font= str(police) + " 22  ", fill=couleur,tag="menu_level")
        if event.y > 325 and event.y < 385:
            if joueur.mode == "solo":
                joueur.mode="survie"
            elif joueur.mode == "multi":
                joueur.mode = "multi_survie"
                joueur2.mode= "multi_survie"
            canvas.delete("menu")
            canvas.delete("title")
            stop = 10
            canvas.create_text(350,200,text="Press space to start",font = police + " 40 ",fill="white",tag="debut")
            canvas.bind("<Key>",joueur.deplacement)
            canvas.unbind("<Button-1>")
        if event.y > 390 and event.y < 460:
            canvas.delete("menu")
            canvas.create_text(350, 200, text="Jouer solo", font= str(police) + " 30  ", fill="blue",tag="menu")
            canvas.create_text(350, 300, text="Multijoueur", font= str(police) + " 30  ", fill="white",tag="menu")
            canvas.create_text(350, 400, text="Vers le site", font= str(police) + " 30  ", fill="white",tag="menu")
            canvas.create_text(350, 500, text="Configuration", font= str(police) + " 30  ", fill="white",tag="menu")
            canvas.create_text(350, 650, text="Quitter", font= str(police) + " 30  ", fill="white",tag="menu")
            canvas.create_text(350, 100, text="Don't Crash 2", font= str(police) + " 40  ", fill="red",tag="title")
            curseur = 1
            canvas.bind("<Key>",menu_principal)
            canvas.bind('<Button-1>',menu_principal)
    if touche == "Return":
        if curseur == 1:
            if joueur.mode=="solo":
                joueur.mode = "solo_level"
                joueur2.mode = "solo_level"
            elif joueur.mode == "multi":
                joueur.mode = "multi"
                joueur2.mode = "multi"
            canvas.delete("menu")
            canvas.delete("title")
            nb_level = int(info_jeu[0].replace("\n",""))
            level=1
            x=50
            y = 150
            canvas.create_text(350, 50, text="Choix du niveau", font= str(police) + " 35  ", fill="red",tag="menu_level")
            canvas.create_text(350, 100, text="retour", font= str(police) + " 30  ", fill="white",tag="menu_level")
            canvas.create_text(x, y, text=level, font= str(police) + " 22  ", fill="blue",tag="menu_level")
            canvas.bind("<Key>",menu_solo_level)
            canvas.bind('<Button-1>',menu_solo_level)
            curseur = 1
            while level < nb_level:
                level=level+1
                x = x+50
                if x > 650:
                    x = x - 650
                    y = y +50
                if level <= joueur.level:
                    couleur = "white"
                else:
                    couleur = "gray"
                canvas.create_text(x, y, text=level, font= str(police) + " 22  ", fill=couleur,tag="menu_level")
        if curseur == 2:
            if joueur.mode == "solo":
                joueur.mode="survie"
            elif joueur.mode == "multi":
                joueur.mode = "multi_survie"
                joueur2.mode= "multi_survie"
            canvas.delete("menu")
            canvas.delete("title")
            stop = 10
            canvas.create_text(350,200,text="Press space to start",font = police + " 40 ",fill="white",tag="debut")
            canvas.bind("<Key>",joueur.deplacement)
            canvas.unbind("<Button-1>")
            
        if curseur == 3:
            canvas.delete("menu")
            canvas.create_text(350, 200, text="Jouer solo", font= str(police) + " 30  ", fill="blue",tag="menu")
            canvas.create_text(350, 300, text="Multijoueur", font= str(police) + " 30  ", fill="white",tag="menu")
            canvas.create_text(350, 400, text="Vers le site", font= str(police) + " 30  ", fill="white",tag="menu")
            canvas.create_text(350, 500, text="Configuration", font= str(police) + " 30  ", fill="white",tag="menu")
            canvas.create_text(350, 650, text="Quitter", font= str(police) + " 30  ", fill="white",tag="menu")
            canvas.create_text(350, 100, text="Don't Crash 2", font= str(police) + " 40  ", fill="red",tag="title")
            curseur = 1
            canvas.bind("<Key>",menu_principal)
            canvas.bind('<Button-1>',menu_principal)
def menu_solo_level(event):
    global curseur,num_level,stop,curseur_level
    touche = event.keysym
    if touche == "Right":
        curseur += 1
        if curseur > joueur.level:
            curseur = 1
    elif touche == "Left" :
        curseur -= 1
        if curseur < 1:
            curseur = joueur.level
    elif touche == "Down":
        curseur = curseur + 13
        if curseur > joueur.level:
            curseur = joueur.level
    elif touche == "Up":
        curseur = curseur - 13
        if curseur < 1:
            curseur = 0
    nb_level = int(info_jeu[0].replace("\n",""))
    level=0
    x=0
    y = 150
    canvas.delete("menu_level")
    canvas.create_text(350, 50, text="Choix du niveau", font= str(police) + " 35  ", fill="red",tag="menu_level")
    if curseur == 0:
        canvas.create_text(350, 100, text="retour", font= str(police) + " 30  ", fill="blue",tag="menu_level")
    else:
        canvas.create_text(350, 100, text="retour", font= str(police) + " 30  ", fill="white",tag="menu_level")
    while level < nb_level:
        level=level+1
        x = x+50
        if x > 650:
            x = x - 650
            y = y +50
        if level <= joueur.level:
            couleur = "white"
        else:
            couleur = "gray"
        if curseur == level:
            couleur = "blue"
        canvas.create_text(x, y, text=level, font= str(police) + " 22  ", fill=couleur,tag="menu_level")
    if touche == "??":
        mod_x = (event.x+25) // 50
        mod_y = ((event.y-75) // 50)-1
        lev = mod_x + (13*mod_y)
        if lev >0 and lev<= joueur.level:
            num_level = lev-1
            canvas.delete("menu_level")
            stop = 0
            jeu()
            barre_progress()
            canvas.bind("<Key>",joueur.deplacement)
            canvas.unbind("<Button-1>")
        elif event.y > 75 and event.y < 125:
            if joueur.mode == "multi":
                    joueur.dead_multi = 0
                    joueur2.dead_multi = 0
            if joueur.mode =="solo_level":
                joueur.mode = "solo"
                joueur2.mode="solo"
            curseur = 1
            canvas.delete("menu_level")
            canvas.create_text(350, 275, text="Mode niveaux", font= str(police) + " 30  ", fill="blue",tag="menu")
            canvas.create_text(350, 350, text="Mode survie", font= str(police) + " 30  ", fill="white",tag="menu")
            canvas.create_text(350, 425, text="retour", font= str(police) + " 30  ", fill="white",tag="menu")
            canvas.create_text(350, 100, text="Choix du mode", font= str(police) + " 40  ", fill="red",tag="menu")
            canvas.bind('<Key>',menu_solo)
            canvas.bind('<Button-1>',menu_solo)
    if touche == "Return":
        if curseur > 0:
            num_level = curseur-1
            canvas.delete("menu_level")
            stop = 0
            jeu()
            barre_progress()
            canvas.bind("<Key>",joueur.deplacement)
            canvas.unbind("<Button-1>")
        elif curseur == 0:
            curseur = 1
            if joueur.mode == "multi":
                    joueur.dead_multi = 0
                    joueur2.dead_multi = 0
            if joueur.mode =="solo_level":
                joueur.mode = "solo"
                joueur2.mode="solo"
            canvas.delete("menu_level")
            canvas.create_text(350, 275, text="Mode niveaux", font= str(police) + " 30  ", fill="blue",tag="menu")
            canvas.create_text(350, 350, text="Mode survie", font= str(police) + " 30  ", fill="white",tag="menu")
            canvas.create_text(350, 425, text="retour", font= str(police) + " 30  ", fill="white",tag="menu")
            canvas.create_text(350, 100, text="Choix du mode", font= str(police) + " 40  ", fill="red",tag="menu")
            canvas.bind('<Key>',menu_solo)
            canvas.bind('<Button-1>',menu_solo)
def menu_principal(event):
    global curseur
    #fonction pour actualiser le menu leur du choix
    def actual_menu():
        global curseur
        canvas.delete("menu")
        if curseur == 1: #verifie si le curseur et poser sur la première ligne et le met en bleu si c'est le cas
            canvas.create_text(350, 200, text="Jouer solo", font= str(police) + " 30  ", fill="blue",tag="menu")
        else:
            canvas.create_text(350, 200, text="Jouer solo", font= str(police) + " 30  ", fill="white",tag="menu")
        if curseur == 2:
            canvas.create_text(350, 300, text="Multijoueur", font= str(police) + " 30  ", fill="blue",tag="menu")
        else:
            canvas.create_text(350, 300, text="Multijoueur", font= str(police) + " 30  ", fill="white",tag="menu")
        if curseur == 3:
            canvas.create_text(350, 400, text="Vers le site", font= str(police) + " 30  ", fill="blue",tag="menu")
        else:
             canvas.create_text(350, 400, text="Vers le site", font= str(police) + " 30  ", fill="white",tag="menu")
        if curseur == 4:
            canvas.create_text(350, 500, text="Configuration", font= str(police) + " 30  ", fill="blue",tag="menu")
        else:
            canvas.create_text(350, 500, text="Configuration", font= str(police) + " 30  ", fill="white",tag="menu")
        if curseur == 5:
            canvas.create_text(350, 650, text="Quitter", font= str(police) + " 30  ", fill="blue",tag="menu")
        else:
            canvas.create_text(350, 650, text="Quitter", font= str(police) + " 30  ", fill="white",tag="menu")
    
    touche=event.keysym
    if touche == 'Down': # déplacement vers le bas
        if curseur<5:
            curseur = curseur+1
        else:
            curseur=1
        actual_menu()
            
    elif touche=='Up': # déplacement vers le haut
        if curseur>1:

            curseur=curseur-1
        else:
            curseur=5
        actual_menu()
    elif touche == "??": # si l'on utilise la souris
        if event.y > 600 and event.y < 700: # si la position de la souris et sur tel choix 
            fenetre.destroy()
        elif event.y > 150 and event.y < 250:
            joueur.mode = "solo"
            joueur2.mode = "solo"
            canvas.delete("menu")
            canvas.delete("title")
            # créer le menu solo
            canvas.create_text(350, 275, text="Mode niveaux", font= str(police) + " 30  ", fill="blue",tag="menu")
            canvas.create_text(350, 350, text="Mode survie", font= str(police) + " 30  ", fill="white",tag="menu")
            canvas.create_text(350, 425, text="retour", font= str(police) + " 30  ", fill="white",tag="menu")
            canvas.create_text(350, 100, text="Choix du mode", font= str(police) + " 40  ", fill="red",tag="menu")
            canvas.bind('<Key>',menu_solo)
            canvas.bind('<Button-1>',menu_solo)
        elif event.y >250 and event.y < 350:
            joueur.mode = "multi"
            joueur2.mode = "multi"
            curseur = 1
            # créer le menu multi
            canvas.delete("menu")
            canvas.delete("title")
            canvas.create_text(350, 275, text="Mode niveaux", font= str(police) + " 30  ", fill="blue",tag="menu")
            canvas.create_text(350, 350, text="Mode survie", font= str(police) + " 30  ", fill="white",tag="menu")
            canvas.create_text(350, 425, text="retour", font= str(police) + " 30  ", fill="white",tag="menu")
            canvas.create_text(350, 100, text="Choix du mode", font= str(police) + " 40  ", fill="red",tag="menu")
            canvas.bind('<Key>',menu_solo)
            canvas.bind('<Button-1>',menu_solo)
        elif event.y >350 and event.y < 450:
            webbrowser.open('http://www.don-t-crash2.esy.es')
    elif touche== "Return": #si il y a pression de la touche entrer 
        if curseur == 5:
            fenetre.destroy()
        elif curseur == 1:
            joueur.mode = "solo"
            joueur2.mode = "solo"
            canvas.delete("menu")
            canvas.delete("title")
            canvas.create_text(350, 275, text="Mode niveaux", font= str(police) + " 30  ", fill="blue",tag="menu")
            canvas.create_text(350, 350, text="Mode survie", font= str(police) + " 30  ", fill="white",tag="menu")
            canvas.create_text(350, 425, text="retour", font= str(police) + " 30  ", fill="white",tag="menu")
            canvas.create_text(350, 100, text="Choix du mode", font= str(police) + " 40  ", fill="red",tag="menu")
            canvas.bind('<Key>',menu_solo)
            canvas.bind('<Button-1>',menu_solo)
        elif curseur == 2:
            joueur.mode = "multi"
            joueur2.mode = "multi"
            curseur = 1
            canvas.delete("menu")
            canvas.delete("title")
            canvas.create_text(350, 275, text="Mode niveaux", font= str(police) + " 30  ", fill="blue",tag="menu")
            canvas.create_text(350, 350, text="Mode survie", font= str(police) + " 30  ", fill="white",tag="menu")
            canvas.create_text(350, 425, text="retour", font= str(police) + " 30  ", fill="white",tag="menu")
            canvas.create_text(350, 100, text="Choix du mode", font= str(police) + " 40  ", fill="red",tag="menu")
            canvas.bind('<Key>',menu_solo)
            canvas.bind('<Button-1>',menu_solo)
        elif curseur == 3:
            webbrowser.open('http://www.don-t-crash2.esy.es')
def menu_inter_multi(event):
    global curseur,mode_jeu,value4,value5
    touche = event.keysym
    canvas.delete("menu")
    if touche == "Down":
        curseur = curseur + 1
        if curseur > 3:
            curseur = 1
    elif touche == "Up":
        curseur = curseur -1
        if curseur < 1:
            curseur = 3
    canvas.create_text(350, 100, text="Choix du mode", font= str(police) + " 40  ", fill="red",tag="menu")
    if curseur == 1:
        canvas.create_text(350, 275, text="Mode niveaux", font= str(police) + " 30  ", fill="blue",tag="menu")
    else:
        canvas.create_text(350, 275, text="Mode niveaux", font= str(police) + " 30  ", fill="white",tag="menu")
    if curseur == 2:
        canvas.create_text(350, 350, text="Mode survie", font= str(police) + " 30  ", fill="blue",tag="menu")
    else:
        canvas.create_text(350, 350, text="Mode survie", font= str(police) + " 30  ", fill="white",tag="menu")
    if curseur == 3:
        canvas.create_text(350, 425, text="retour", font= str(police) + " 30  ", fill="blue",tag="menu")
    else:
        canvas.create_text(350, 425, text="retour", font= str(police) + " 30  ", fill="white",tag="menu")
        
    if touche == "Return":
        if curseur == 1:
            mode_jeu = "multi"
            canvas.delete("menu")
            canvas.delete("title")
            nb_level = int(info_jeu[0].replace("\n",""))
            level=1
            x=50
            y = 150
            canvas.create_text(350, 50, text="Choix du niveau", font= str(police) + " 35  ", fill="red",tag="menu_level")
            canvas.create_text(350, 100, text="retour", font= str(police) + " 30  ", fill="white",tag="menu_level")
            canvas.create_text(x, y, text=level, font= str(police) + " 22  ", fill="blue",tag="menu_level")
            canvas.bind("<Key>",menu_solo_level)
            curseur = 1
            while level < nb_level:
                level=level+1
                x = x+50
                if x > 650:
                    x = x - 650
                    y = y +50
                if level <= joueur.level:
                    couleur = "white"
                else:
                    couleur = "gray"
                canvas.create_text(x, y, text=level, font= str(police) + " 22  ", fill=couleur,tag="menu_level")   
        if curseur == 3:
            canvas.delete("menu")
            canvas.create_text(350, 200, text="Jouer solo", font= str(police) + " 30  ", fill="blue",tag="menu")
            canvas.create_text(350, 300, text="Multijoueur", font= str(police) + " 30  ", fill="white",tag="menu")
            canvas.create_text(350, 400, text="Vers le site", font= str(police) + " 30  ", fill="white",tag="menu")
            canvas.create_text(350, 500, text="Configuration", font= str(police) + " 30  ", fill="white",tag="menu")
            canvas.create_text(350, 650, text="Quitter", font= str(police) + " 30  ", fill="white",tag="menu")
            canvas.create_text(350, 100, text="Don't Crash 2", font= str(police) + " 40  ", fill="red",tag="title")
            curseur = 1
            canvas.bind("<Key>",menu_principal)

info_gene = open("info_jeu.txt","r")
info_jeu = info_gene.readlines()
info_gene.close()
#variable definit au debut
info_level = 0
num_level = 0
stop = 0
couleur = ["cyan","magenta","yellow","gray","blue","white","purple","red","green","brown","orange"]
curseur_level = 0
time = 0
time_anim = 0
var_progress = 0
width =5
curseur = 1
mode_jeu = 0
vit1 = 4
vit2 = 2
time1 = 2000
time2 = 5500
play = 0

canvas.create_text(350, 200, text="Jouer solo", font= str(police) + " 30  ", fill="blue",tag="menu")
canvas.create_text(350, 300, text="Multijoueur", font= str(police) + " 30  ", fill="white",tag="menu")
canvas.create_text(350, 400, text="Vers le site", font= str(police) + " 30  ", fill="white",tag="menu")
canvas.create_text(350, 500, text="Configuration", font= str(police) + " 30  ", fill="white",tag="menu")
canvas.create_text(350, 650, text="Quitter", font= str(police) + " 30  ", fill="white",tag="menu")
canvas.create_text(350, 100, text="Don't Crash 2", font= str(police) + " 40  ", fill="red",tag="title")

#création du joueur principal
joueur = Joueur((-20,-20),info_joueur[0].replace("\n",""),info_joueur[1].replace("\n",""),info_joueur[3].replace("\n",""),20,info_joueur[2].replace("\n",""),info_joueur[4].replace("\n",""),"white",1)
joueur2 = Joueur((-40,-40),'j_2','jjg',0,20,999,1,'red',2)
canvas.focus_set()
canvas.bind('<Key>',menu_principal)
canvas.bind('<KeyRelease>',joueur.fin_deplacement)
canvas.bind('<Button-1>',menu_principal)
canvas.place(x=larg/2,y=haut/2,anchor="center")
fenetre.mainloop()
