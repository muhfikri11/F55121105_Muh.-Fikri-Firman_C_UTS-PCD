from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageOps

class Application(Frame):
    
    def _init_(self, master):
        super()._init_(master)
        self.master = master
        self.master.title("Muh. Fikri Firman_F55121105")
        self.pack()
        self.create_widgets()
    
    def create_widgets(self):
        self.nama = Label(self, text="Nama : Muh. Fikri Firman")
        self.nama.pack(padx=10, pady=10)
        
        self.nim = Label(self, text="Nim : F55121105")
        self.nim.pack(padx=10, pady=10)

        self.kelas = Label(self, text="Kelas : C")
        self.kelas.pack(padx=10, pady=10)
        
        self.btn_open = Button(self, text="Buka Gambar", command=self.open_image)
        self.btn_open.pack(padx=10, pady=10)
        
        self.btn_grayscale = Button(self, text="grayscale", command=self.grayscale_image)
        self.btn_grayscale.pack(padx=10, pady=10)
        
        self.btn_invert = Button(self, text="Invert Color", command=self.invert_image)
        self.btn_invert.pack(padx=10, pady=10)
        
        self.btn_quit = Button(self, text="Keluar", command=self.master.destroy)
        self.btn_quit.pack(padx=10, pady=10)
    
    def open_image(self):
        self.filename = filedialog.askopenfilename(title="Pilih Gambar", filetypes=(("File Gambar", ".jpg;.png"), ("Semua File", ".")))
        if self.filename:
            self.img = Image.open(self.filename)
            self.show()
    
    def grayscale_image(self):
        if hasattr(self, 'img'):
            grayscale_img = self.img.convert("L")
            grayscale_img.show()
    
    def invert_image(self):
        if hasattr(self, 'img'):
            inverted_img = ImageOps.invert(self.img)
            inverted_img.show()

root = Tk()
app = Application(root)
app.mainloop()