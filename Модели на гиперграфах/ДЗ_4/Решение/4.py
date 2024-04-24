from tkinter import *  # Импорт всех классов и методов из модуля tkinter
from datetime import datetime  # Импорт класса datetime из модуля datetime

temp = 0  # Инициализация переменной для хранения времени
after_id = ''  # Инициализация переменной для хранения идентификатора задачи после

def tick():
   global temp, after_id  # Объявление глобальных переменных temp и after_id
   after_id = root.after(1000, tick)  # Запуск функции tick каждую секунду (1000 миллисекунд)
   f_temp = datetime.fromtimestamp(temp).strftime("%M:%S")  # Форматирование времени в формате MM:SS
   label1.configure(text=str(f_temp))  # Обновление текста метки label1
   temp += 1  # Увеличение значения времени на 1

def start_tick():
   btnStart.pack_forget()  # Скрытие кнопки "Старт"
   btnStop.pack()  # Отображение кнопки "Стоп"
   tick()  # Запуск функции tick

def stop_tick():
   btnStop.pack_forget()  # Скрытие кнопки "Стоп"
   btnContinue.pack()  # Отображение кнопки "Продолжить"
   btnReset.pack()  # Отображение кнопки "Сброс"
   root.after_cancel(after_id)  # Отмена выполнения функции tick

def continue_tick():
   btnContinue.pack_forget()  # Скрытие кнопки "Продолжить"
   btnReset.pack_forget()  # Скрытие кнопки "Сброс"
   btnStop.pack()  # Отображение кнопки "Стоп"
   tick()  # Запуск функции tick

def reset_tick():
   global temp  # Объявление глобальной переменной temp
   temp = 0  # Сброс значения времени на 0
   label1.configure(text='00:00')  # Обновление текста метки label1
   btnContinue.pack_forget()  # Скрытие кнопки "Продолжить"
   btnReset.pack_forget()  # Скрытие кнопки "Сброс"
   btnStart.pack()  # Отображение кнопки "Старт"

root = Tk()  # Создание основного окна приложения
root.title('Секундомер')  # Установка заголовка окна
root.resizable(width=False, height=False)  # Отключение возможности изменения размера окна
root.geometry('300x200')  # Установка размера окна

label1 = Label(root, width=10, font=('Comic Sans MS', 30), text='00:00')  # Создание метки для отображения времени
label1.pack()  # Размещение метки в окне

# Создание кнопок и связывание их с соответствующими функциями
btnStart = Button(root, text='Старт', font=('Comic Sans MS', 20), width=15, command=start_tick)
btnStop = Button(root, text='Стоп', font=('Comic Sans MS', 20), width=15, command=stop_tick)
btnContinue = Button(root, text='Продолжить', font=('Comic Sans MS', 20), width=15, command=continue_tick)
btnReset = Button(root, text='Сброс', font=('Comic Sans MS', 20), width=15, command=reset_tick)
btnStart.pack()  # Размещение кнопки "Старт" в окне

root.mainloop()  # Запуск основного цикла обработки событий tkinter
