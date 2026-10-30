#  QR Code Generator

A modern, fast, and lightweight desktop application built with Python that allows users to instantly generate QR codes from any text input or URL. 

The application features a clean, responsive graphical user interface (GUI) that adapts beautifully to system themes, providing an effortless user experience.

---

##  What the Program Does

* **Instant Generation:** Converts any text, website link, Wi-Fi credential, or plain data into a QR code in real-time.
* **Smart UI Layout:** Uses an adaptive grid that scales perfectly, ensuring the entry field and button stay fixed at the bottom while giving maximum space to the QR code.
* **Modern Styling:** Built on top of `CustomTkinter` to provide a dark/light mode capable interface out of the box.
* **Validation:** Safe text-handling prevents the application from breaking or generating blank/broken images if the input field is empty.
* **Dynamic Rendering:** Re-renders the QR code container instantly whenever the "Generate" button is clicked without needing to restart the app.

---

##  Getting Started

Follow these simple steps to clone, install, and run the project locally.

### 1. Clone the Repository
```bash
git clone https://github.com && cd qrcode-generator
```

### 2. Install Dependencies
Make sure you have Python installed, then run:
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python main.py
```

---

##  Requirements & Tech Stack

* **Python 3.8+**
* **CustomTkinter** (v5.2.0+) - For the modern desktop graphical interface.
* **qrcode** (v7.4.2+) - For generating the standard-compliant QR code matrices.
* **Pillow** (v10.0.0+) - For image processing and seamless rendering inside Tkinter widgets.

---

##  License

This project is licensed under the **MIT License** - feel free to use, modify, and distribute it as you wish. See the `LICENSE` file for details.
