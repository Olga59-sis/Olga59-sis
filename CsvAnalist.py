#Программа анализов .csv файлов 

import tkinter as tk
from tkinter. scrolledtext import ScrolledText as st
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import os

#Создание главного окна
window = tk.Tk()
window.geometry("550x550")
window.title("Программа анализа .csv файлов")

# Создание меток вывода
Label_00 = tk.Label(text = "файл:")
Label_00.grid(row=0, column=0, padx=10, pady=10, sticky="e")

Label_01 = tk.Label(text = "")
Label_01.grid(row=0, column=1, sticky="w")

Label_10 = tk.Label(text = "Строк:")
Label_10.grid(row=1, column=0, padx=10, pady=10, sticky="e")

Label_11 = tk.Label(text = "")
Label_11.grid(row=1, column=1, sticky="w")

Label_20 = tk.Label(text = "Столбцов:")
Label_20.grid(row=2, column=0, padx=10, pady=10, sticky="e")

Label_21 = tk.Label(text = "")
Label_21.grid(row=2, column=1, sticky="w")

#Cоздание текстового ввода с прокруткой
output_text = st(height = 22, width = 50)
output_text.grid(row=3, column=1, padx=10, pady=10, sticky="w")

#Обрабочик нажатия кнопки
def process_button():
    mb.showinfo(title=None, message="Готово")

#Создание кнопки
button=tk.Button(window, text="Прочитать файл", command=process_button)
button.grid(row=4, column=1)

#Запуск цикла mainloop
window.mainloop()
