import numpy as np
from keras.models import load_model
from keras.preprocessing import image
import tkinter as tk
import tkinter.messagebox as mb
import tkinter.filedialog as fd

def predict_digit(img):
    model = load_model(r'C:\Users\ilyad\Diploma Python Server\my_model_binary.h5')
    img_path = img
    img = image.load_img(img_path, target_size=(256, 256))
    img = img.convert('L')
    img = np.array(img)
    img = img / 255.0
    img = img.reshape(1, 256, 256, 1)

    res = model.predict(img)
    print(np.argmax(res, axis=-1), max(res[0]))
    print(res)
    return np.argmax(res), max(res)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Определение заболеваний по рентгенографии")
        btn_file = tk.Button(self, text="Выбрать файл рентгенографии грудной клетки",
                             command=self.choose_file)
        btn_file.pack(padx=60, pady=60)

    def choose_file(self):

        filename = fd.askopenfilename(title="Открыть файл", initialdir="/",
                                      filetypes=[("Изображение", ".png .jpg .jpeg")])
        if filename:
            print(filename)
            digit, acc = predict_digit(filename)
            msg = "Оценочная вероятность пневмонии по данному изображению составляет " + str(int(acc*100))+'%'
            mb.showinfo("Информация", msg)

if __name__ == "__main__":
    app = App()
    app.mainloop()