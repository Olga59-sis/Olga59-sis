#Программа анализов .csv файлов 

import tkinter as tk

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



#Запуск цикла mainloop
window.mainloop()
