from tkinter import Tk,Frame,Canvas
from time import sleep
from random import choice

#Anzahl = 11

width = 1500
height = 1000


class Hanoi:
    def __init__(self,n:int):
        self.__disks = n
        
        # cut 20 pixel from up and 20 pixel from down
        self.__disk_height = (height - 40) / n
        
        # cut 10 pixel from (right,left,between stack1 and stack2, between stack2 and stack3)
        self.__disk_max_width = (width - 40) / 4
    
    def tower_of_hanoi(self,n, source, auxiliary, target):
        if self.__disks == 1:
            print("Move disk 1 from source", source, "to target", target)
            return
        self.tower_of_hanoi(n - 1, source, target, auxiliary)
        
        print("Move disk", n, "from source", source, "to target", target)
        
        self.tower_of_hanoi(n - 1, auxiliary, source, target)
    
    
    def erstelle_lists(self):
        pass


class Disk:
    def __init__(self,x:int,y:int,breite:int,hoehe:int,id:int):
        self.__x = x
        self.__y = y
        self.__next_x = breite
        self.__next_y = hoehe
        self.__id = id
        self.__farbe = ""
        
        if not isinstance(breite, int) or not isinstance(hoehe, int):
            raise TypeError("die breite ist kein Integer oder die laenge is kein Integer")

        if not isinstance(id, int):
            raise TypeError("Die ID ist kein Integer")

        self.farbe_generieren()

    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y

    # die hoehe ist der Differenz vom 2. y und 1. y
    def get_hoehe(self):
        return self.__next_y + self.__y 
    
    # die breite ist der unterschied vom 2. x und 1. x
    def get_breite(self):
        return self.__next_x + self.__x
    
    # get method for the second x
    def get_next_x(self):
        return self.__next_x
    
    # get method for the second y
    def get_next_y(self):
        return self.__next_y
    
    # get method for the id
    def get_id(self):
        return self.__id

    # get method for the disc color
    def get_farbe(self):
        return self.__farbe

    # set method for the second x
    def set_next_x(self, next: float):
        
        if not isinstance(next, int):
            raise TypeError()
        
        self.__next_x = next
    
    # set method for the second y
    def set_next_y(self, next: int):
        
        if not isinstance(next, int):
            raise TypeError()
        
        self.__next_y = next

    
    def verschiebe_x(self, parameter):
        self.__x += parameter
        self.__next_x += parameter
    
    
    def verschiebe_y(self, parameter):
        self.__y += parameter
        self.__next_y += parameter


    def farbe_generieren(self):
        farben_buchstaben = "0123456789abcdef"
        farbe = "#"
        for _ in range(6):
            farbe += choice(farben_buchstaben)

        self.__farbe = farbe



class Stack:
    def __init__(self,position):
        self.__liste = []
        
        # where the stack is in pixel, used to move the disks
        # the stack cannot know which one is itself
        self.__position = position
        

    def getstack(self):
        return self.__liste

    
    def get_position(self):
        return self.__position
    
    
    def addtostack(self, disk: Disk):
        self.__liste.append(disk)
    
    
    def popofstack(self):
        self.__liste.pop()
        
    def set_first_coordinates(self,n,max_width,disk_height):
        
        self.__disk_height = disk_height
        self.__disk_max_width = max_width
        
        # the first disk is on 10 pixel away of the border
        x1 = 10
        x2 = self.__disk_max_width + 10
        
        y1 = height - 20
        y2 = height - 20 - self.__disk_height
        
        # how small should the next disk get
        # maximum width of disk minus the minimum disk width divided by the count of disks
        disk_width =  (self.__disk_max_width - 20) / n
        
        disk_object = Disk(x1,y1,x2,y2,n)
        self.addtostack(disk_object)
        
        
        # create disks and add them to the stack
        # n - 1: the n is already done.
        #the x1,y1 is the lower point and the x2,y2 is the higher point
        for i in range(n - 1,0,-1):
             
            x1 += disk_width
            x2 -= disk_width
            
            y1 = y2
            y2 -= self.__disk_height
            
            disk_object = Disk(x1,y1,x2,y2,i)
            self.addtostack(disk_object)

        
    def set_height_disks(self):
        
        s = 20
        
        for index,i in enumerate(self.__liste):
            
            # if not index:
            #     i.set_y(height - s)
            #     i.set_next_y(s + self.__disk_height)
            #     s += self.__disk_height
            
            i.set_y(height - s)
            i.set_next_y(height - s - self.__disk_height)
            
            s += self.__disk_height



class Animation:
    def __init__(self,stacks,width=1500,height=1000):
        self.__stacks = stacks
        self.__width = width
        self.__height = height    

    def create_window(self):
        
        self.__window = Tk()    
        self.__window.title("Tower Of HANOI")
        
        # Frame anlegen
        self.__frame = Frame(self.__window)
        self.__frame.pack()
        
        # Canvas anlegen, Hintergrundfarbe und Größe wählen
        self.__canvas = Canvas(self.__frame, bg="#f0e0b0", width=self.__width, height=self.__height)
        self.__canvas.pack()
                

    def animieren(self):
        
        self.create_window()

        for i in self.__stacks:
            
            for j in i.getstack():
                
                #print(j.get_x(),j.get_y(),j.get_next_x(),j.get_next_y(),j.get_farbe())
                self.__canvas.create_rectangle(j.get_x(),j.get_y(),j.get_breite(),j.get_laenge(),fill=j.get_farbe())
            
        # Fenster offenhalten
        self.__window.mainloop()


