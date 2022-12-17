from tkinter import Tk,Frame,Canvas
from time import sleep
from random import choice

n = 17
windowx = 854
windowy = 480

class Hanoi:
    def __init__(self):
        self.__scheiben = scheiben
    

    def erstelle_lists(self):
        pass

class Scheibe:
    def __init__(self,x:int,y:int,breite:int,laenge:int,id:int):
        self.__x = x
        self.__y = y
        self.__breite = breite
        self.__laenge = laenge
        self.__next_x = 0
        self.__next_y = 0
        self.__id = id
        self.__farbe = ""

        
        # if not isinstance(x, int) or not isinstance(y, int):
        #     raise TypeError("die x Koordinate ist kein integer oder die y Koordinate ist kein Integer")
        
        if not isinstance(breite, int) or not isinstance(laenge, int):
            raise TypeError("die breite ist kein Integer oder die laenge is kein Integer")

        if not isinstance(id, int):
            raise TypeError("Die ID ist kein Integer")

        self.farbe_generieren()

    def get_x(self):
        return self.__x + windowx / 5
    
    def get_y(self):
        return self.__y

    def get_laenge(self):
        return self.__laenge + self.__y 
    
    def get_breite(self):
        return self.__breite + self.__x + windowx / 5
    
    def get_next_x(self):
        return self.__next_x
    
    def get_next_y(self):
        return self.__next_y
    
    def get_id(self):
        return self.__id

    def get_farbe(self):
        return self.__farbe

    def set_next_x(self, next: int):
        if not isinstance(next, int):
            raise TypeError()
        self.__next_x = next
    
    def set_next_y(self, next: int):
        if not isinstance(next, int):
            raise TypeError()
        self.__next_y = next

    def verschiebe(self):
        self.x += self.__next_x
        self.y += self.__next_y

    def farbe_generieren(self):
        farben_buchstaben = "0123456789abcdef"
        farbe = "#"
        for i in range(6):
            farbe += choice(farben_buchstaben)

        self.__farbe = farbe

class Stack:
    def __init__(self):
        self.__liste = []
        self.scheiben_generieren()
    
    def getstack(self):
        return self.__liste
            

    def scheiben_generieren(self):
        breite = 170
        x = 20
        y = windowy/2
        for i in range(n):
            scheibe = Scheibe(x, y, breite, 10, i)
            breite -= 10
            x += 5
            y -= 10
            print(type(x))
            print(type(y))
            self.__liste.append(scheibe)


#hier muss die init funktion die Hanoi Klasse aufrufen und die Scheiben verschiebung durchspielen
# dazu müssen noch die Funktionen zur Implementierung der Animation noch geschrieben werden
# nach jeder Bewegung eines Objektes müssen die Animationen alle neugeladen werden
class Animation:
    def __init__(self):
        pass

    def animieren(self):
        # Fenster anlegen
        window = Tk()
        window.title("GUI Test Window")
        # Frame anlegen
        frame = Frame(window)
        frame.pack()
        # Canvas anlegen, Hintergrundfarbe und Größe wählen
        canvas = Canvas(frame, bg="#f0e0b0", width=windowx, height=windowy)
        canvas.pack()
        # Animation starten
        #(... hier kommt das Hauptprogramm hin)
        stack = Stack()
        stack = stack.getstack()
        for i in stack:
            print(i.get_x(),i.get_y(),i.get_breite(),i.get_laenge(),i.get_farbe())
            item = canvas.create_rectangle(i.get_x(),i.get_y(),i.get_breite(),i.get_laenge(),fill=i.get_farbe())
        # for i in range (500):
            # canvas.move(item, 1, 0) # Gespeicherte Position verändern
            # canvas.update() # Bildschirm aktualisieren
            # sleep(0.01) # Delay (in Sek.)
        # Fenster offenhalten
        window.mainloop()

s = Animation()
s.animieren()