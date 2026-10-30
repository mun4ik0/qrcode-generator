import qrcode
import customtkinter as ctk
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Qrcode Generator")
        self.geometry("500x500")
        self.frame = ctk.CTkFrame(self)
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        self.label = ctk.CTkLabel(self.frame,text="")
        self.label.grid(row=0, column=0, sticky="nsew")
        self.entry = ctk.CTkEntry(self.frame)
        self.entry.grid(row=1, column=0, sticky="")
        self.btn = ctk.CTkButton(self.frame, text="Generate", command=self.generate)
        self.btn.grid(row=2, column=0, sticky="")

    def generate(self):
        string = self.entry.get()
        output = self.label
        if string.strip():
            qr = qrcode.QRCode(version=1, box_size=10, border=4)
            qr.add_data(string)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white").get_image()
            new_label = ctk.CTkImage(light_image=img, dark_image=img, size=(300, 300))
            output.configure(image=new_label)
            output.image = new_label


root = App()
root.mainloop()
