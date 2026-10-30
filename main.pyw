import qrcode
import customtkinter as ctk
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Qrcode Generator")
        self.geometry("500x500")
        self.update()
        self.frame = ctk.CTkFrame(self)
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        self.label = ctk.CTkLabel(self.frame,text="")
        self.label.grid(row=0, column=0, sticky="nsew")

        self.save_btn = ctk.CTkButton(self.frame, text="Save", command=self.save)
        self.text = ctk.CTkLabel(self.frame, text="Successfully saved",text_color="green")
        self.entry = ctk.CTkEntry(self.frame)
        self.entry.grid(row=1, column=0, sticky="")
        self.btn = ctk.CTkButton(self.frame, text="Generate", command=self.generate)
        self.btn.grid(row=2, column=0, sticky="")

        self.qr_pil_img = None
    def generate(self):
        string = self.entry.get()

        if string.strip():
            self.text.grid_forget()
            qr = qrcode.QRCode(version=1, box_size=10, border=4)
            qr.add_data(string)
            qr.make(fit=True)
            self.qr_pil_img = qr.make_image(
                fill_color="black", back_color="white"
            ).get_image()

            size_px = int(min(self.winfo_width(), self.winfo_height()) * 0.6)
            new_label = ctk.CTkImage(light_image=self.qr_pil_img,
                                     dark_image=self.qr_pil_img,
                                     size=(size_px, size_px))

            self.label.configure(image=new_label)
            self.save_btn.grid(row=3,column=0,sticky="")

    def save(self):
        if self.qr_pil_img:
            self.qr_pil_img.save("qr.png")
            self.text.grid(row=4,column=0,columnspan=2)
if __name__ == "__main__":
    root = App()
    root.mainloop()
