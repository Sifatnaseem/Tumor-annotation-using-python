
import tkinter as tk
from tkinter import filedialog, colorchooser
from PIL import ImageTk, Image, ImageDraw, ImageGrab

coordinates = []
text_description = []

class App():
    #creating a empty window
    def __init__(self):
        self.window = tk.Tk()
        self.window.after(100, self.selecting_file)
        self.window.update()
        self.window.mainloop()
     #selecting file
    def selecting_file(self):
        self.file_path = filedialog.askopenfilename()
            
        self.image = Image.open(self.file_path)
        self.width, self.height = self.image.size

        self.draw  = ImageDraw.Draw(self.image)
        self.photo = ImageTk.PhotoImage(image=self.image)

        self.frame_tools = tk.Frame(self.window)
        self.frame_tools.pack()
        
        self.canvas = tk.Canvas(self.window, width=self.width, height=self.height)
        self.canvas.pack()
        
        self.canvas.bind("<Button-1>", self.get_x_and_y)
        self.canvas.bind("<B1-Motion>", self.draw_smth)
        
        self.canvas.bind("<Button-3>", self.mouseDown)
        self.window.bind("<Any KeyPress>", lambda event: self.drawText(event.keysym))

        self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        self.save_button = tk.Button(self.window, text='Save', command=self.save)
        self.save_button.pack()

    def get_x_and_y(self, event):
        global lasx, lasy
        lasx, lasy = event.x, event.y

    def draw_smth(self, event):
        global lasx, lasy
        self.canvas.create_line((lasx, lasy, event.x, event.y), fill='red', width=2)
        lasx, lasy = event.x, event.y
        coordinates.append([lasx,lasy])

    def mouseDown(self, event):
        global lasnx, lasny
        lasnx, lasny = event.x, event.y

    def drawText(self, newkey):
        global lasnx, lasny, text
        if None not in {lasnx, lasny}:
            label = self.canvas.create_text(lasnx, lasny,text=newkey,fill= 'red',anchor='nw', font= ('courier',15))
            text = self.canvas.itemcget(label,'text')
            if newkey == "space":
                self.canvas.itemconfig(label, text=text[:-5])
            lasnx += 10
        text_description.append(text) 

    def save(self):
        x=self.canvas.winfo_rootx()+self.canvas.winfo_x()
        y=self.canvas.winfo_rooty()+self.canvas.winfo_y()
        x1=x+self.canvas.winfo_width()
        y1=y+self.canvas.winfo_height()
        ImageGrab.grab().crop((x,y,x1,y1)).save(r'C:\Users\Azmat\OneDrive\Desktop\python final project\TEST.png')
         
        with open(r'C:\Users\Azmat\OneDrive\Desktop\python final project\TEST_circle_coordinates.txt',"w")as output:
            output.write(str(coordinates))
            
        with open(r'C:\Users\Azmat\OneDrive\Desktop\python final project\description.txt', "w") as output:
            output.write(str(text_description))


App()
