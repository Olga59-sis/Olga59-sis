#Программа анализов .csv файлов 

import tkinter as tk
from tkinter. scrolledtext import ScrolledText as st
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import os
import pandas as pd


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

# Диалог открытия файла
def do_dialog():
    my_dir = os.getcwd()
    name= fd.askopenfilename(initialdir=my_dir)
    return name

#Обработка csv файла при помощи pandas
def pandas_read_csv(file_name):
    df = pd.read_csv(file_name, header=[0], sep=';')
    cnt_rows = df.shape[0]
    cnt_columns = df.shape[1]
    Label_11['text'] = cnt_rows
    Label_21['text'] = cnt_columns
    return df
    
# Выборка стобца в списке
def get_column(df, column_ix):
    cnt_rows = df.shape[0]
    lst = []
    for i in range(cnt_rows):
        lst.append(df.iat[i, column_ix])
    return lst
    
# Если в этом поле имя, пусть вернет True
def meet_name(field):
    checkfor = ['Вера', 'Анатолий', 'Мария', 'Артем', 'Алексей',
        'Валерия', 'Наталья', 'Оксана', 'Галина', 'Марина', 'Вероника',
        'Виталий', 'Борис', 'Диана', 'Ева']
    for s in checkfor:
        if s in str(field): # Нашлось!
            return True
    #Ничего не совпало
    return False 
    
  
# Если в этом списке многие элементы содержат имя,то пусть вернет True
def list_meet_name(fields_list):
    counter_total = 0
    counte_meet = 0
    for list_item in fields_list:
        counter_total += 1
        if meet_name(list_item):
            counter_meet += 1 
     # Конец подсчета
        if counter_meet /counter_total > 0.1:
         return True
 #Не набралось нужного коллчества совпадений 
    return False
           
            

#Обработчик нажатия кнопки
def process_button():
    file_name = do_dialog()
    Label_01['text'] = file_name
    df = pandas_read_csv(file_name)
    lst = get_column(df, 2)
    for item in lst:
        output_text.insert(tk.END, str(item) + '   '
            + str(meet_name(item)) + os. linesep)
        mb.showinfo(title=None, message= "Готово")
    
#Создание кнопки
button=tk.Button(window, text="Прочитать файл", command=process_button)
button.grid(row=4, column=1)

#Запуск цикла mainloop
window.mainloop()
