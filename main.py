from tkinter import *
from model import *


def choose_topic(topic):
    label_choice.config(text="Тема - " + topic.lower() + ", выбрана")
    create_data("data/" + topic.lower() + ".txt")


def show_menu(event):
    menu.post(event.x_root, event.y_root)


topics = ["Коты", "Собаки", "Хомяки", "Дельфины", "Бабочки"]
root = Tk()
root.title("GUI на Python")
root["bg"] = "#d0b084"
root.geometry("800x700+350+100")

main_label = Label(text="Это приложение проверяет как текст написанный в рамке соотносится с темой."
                   "\nВыберите любую из предложенных тем.", fg="black", bg="#d0b084", font="Arial 14")
main_label.pack()

label_choice = Label(text="Ничего не выбрано", fg="black", bg="#d0b084", font="Arial 14")
label_choice.pack()

menu = Menu(root, tearoff=0)
for topic in topics:
    menu.add_command(label=topic, command=lambda topic=topic: choose_topic(topic))

btn_menu = Button(root, text="Выберите тему", background="#ffa26a", foreground="black", padx="20", pady="10", font="12")
btn_menu.pack()
btn_menu.bind("<Button-1>", show_menu)

label_text = Label(text="Введите текст в форму для сравнения: \n (Можно взять из папки ForComparison) ", fg="black", bg="#d0b084", font="Arial 14")
label_text.place(relx=0.5, rely=0.25, anchor='center')

text = Text(width=90, height=15)
text.place(relx=0.5, rely=0.48, anchor='center')

itog = Button(text="Проверить", background="#ffa26a", foreground="black", padx="70", pady="10", font="12", command=lambda: find_accuracy(text, label_accuracy))
itog.place(relx=0.5, rely=0.75, anchor = 'center')

label_accuracy = Label(text="Точность равна: ", fg="black", bg="#d0b084", font="Arial 14")
label_accuracy.place(relx = 0.5, rely = 0.82, anchor = 'center')

root.mainloop()

