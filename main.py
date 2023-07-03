from tkinter import *
from model import *


def func(string):
    label_choice.config(text=string)
    if label_choice["text"] == "Выбрана тема про котов":
        create_data("data/catsMain.txt")
    elif label_choice["text"] == "Выбрана тема про собак":
        create_data("data/dogsMain.txt")
    elif label_choice["text"] == "Выбрана тема про хомяков":
        create_data("data/hamstersMain.txt")


root = Tk()
root.title("GUI на Python")
root["bg"] = "#d0b084"
root.geometry("800x700+350+100")

main_label = Label(text="Это приложение проверяет как текст написанный в рамке соотносится с темой."
                   "\nВыберите любую из предложенных тем.", fg="black", bg="#d0b084", font="Arial 14")
main_label.pack()

label_choice = Label(text="Ничего не выбрано", fg="black", bg="#d0b084", font="Arial 14")
label_choice.pack()

btn_cats = Button(text="Тема: Коты", background="#ffa26a", foreground="black",
                  padx="60", pady="10", font="16", command=lambda: func("Выбрана тема про котов"))
btn_cats.place(x=15, y=100)

btn_dogs = Button(text="Тема: Собаки", background="#ffa26a", foreground="black",
                  padx="60", pady="10", font="16", command=lambda: func("Выбрана тема про собак"))
btn_dogs.place(x=255, y=100)

btn_rabbits = Button(text="Тема: Хомяки", background="#ffa26a", foreground="black",
                     padx="60", pady="10", font="16", command=lambda: func("Выбрана тема про хомяков"))
btn_rabbits.place(x=515, y=100)

label_text = Label(text="Введите текст в форму для сравнения: \n (Можно взять из папки ForComparison) ", fg="black", bg="#d0b084",
                   font="Arial 14")
label_text.place(relx=0.5, rely=0.3, anchor='center')

text = Text(width=90, height=15)
text.place(relx=0.5, rely=0.53, anchor='center')

itog = Button(text="Проверить", background="#ffa26a", foreground="black",
              padx="70", pady="10", font="16", command=lambda: find_accuracy(text, label_accuracy))
itog.place(x=280, y=550)

label_accuracy = Label(text="Точность равна: ", fg="black", bg="#d0b084", font="Arial 14")
label_accuracy.place(relx = 0.5,
                   rely = 0.9,
                   anchor = 'center')

root.mainloop()

