from tkinter import *
from tkinter import messagebox
from os import path
from PIL import ImageTk, Image
import random


class HangmanGUI(object):

    def __init__(self):

        self.tk = Tk(screenName="Hangman")

        self.bgcolor = "grey"
        self.tk.title("Poker")
        self.tk.geometry("900x400")

        self.frame = Frame(master=self.tk, bg=self.bgcolor)
        self.frame.pack_propagate(0)
        self.frame.pack(fill=BOTH, expand=1)

        self.label = Label(self.frame, text="Hangman Game", bg=self.bgcolor, fg="white")
        # self.label.grid(row=0, column=2)
        self.label.place(x=300, y=20)
        self.label.config(font=("Courier", 30))

        self.letter_frame = Frame(master=self.frame, bg=self.bgcolor)
        # self.letter_frame.grid(row=6, column=2, columnspan=2)
        self.letter_frame.place(x=500, y=200, anchor="ne")

        self.letters = []
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"

        # game Logic
        self.max_errors = 5
        self.load_images()
        self.words = open("words.txt", "r").read().split("\n")

        self.image_canvas = Canvas(master=self.frame, bg="green", highlightthickness=0, height = 250, width= 250)
        # self.image_canvas.grid(row=5, column=3)
        self.image_canvas.place(x=520, y=100)

        self.label_solution = Label(master=self.frame, bg="darkgray", font=("Helvetica", 36))
        # self.label_solution.grid(row=5, column=2)
        self.label_solution.place(x=260, y=100, anchor="n")

        for i in range(len(self.alphabet)):
            self.letters.append(Button(master=self.letter_frame, text=self.alphabet[i], relief="flat",
                                       font=('Helvetica', 10),
                                       command=lambda i=i: self.select(i)))

        self.play()

        self.tk.mainloop()

    def load_images(self):
        self.dir = path.dirname(__file__)
        self.img_dir = path.join(self.dir, "hangman")

        self.size = 500, 500
        self.images = []
        for i in range(self.max_errors):
            im = Image.open(path.join(self.img_dir, str(i+1)+".gif"))
            # im.thumbnail(self.size)
            im = im.resize((250, 250), Image.ANTIALIAS)
            im1 = ImageTk.PhotoImage(im)
            self.images.append(im1)

    def select(self, index):

        guessed = False

        for i, letter in enumerate(self.solution):
            if letter == self.alphabet[index]:
                temp = self.hidden.split()
                temp[i] = letter
                self.hidden = " ".join(temp)
                # print(self.hidden)
                self.label_solution.config(text=self.hidden)
                self.label_solution.update_idletasks()

                guessed = True

        self.letters[index].grid_forget()

        if not guessed:
            self.errors += 1
            if self.max_errors <= self.errors:
                self.lose()
            self.image_canvas.create_image(0, 0, image=self.images[self.errors], anchor='nw')

        if "".join(self.hidden.split()) == self.solution:
            self.win()

    def play(self):

        self.solution = random.choice(self.words)
        print(self.solution)
        self.hidden = ""
        self.errors = 0
        self.image_canvas.create_image(0, 0, image=self.images[self.errors], anchor='nw')
        for letter in self.solution:
            self.hidden += "_ "

        self.label_solution.config(text=self.hidden)
        self.label_solution.update_idletasks()

        for i in range(len(self.alphabet)):
            self.letters[i].grid(row=0, column=i + 1)

        # print(self.hidden)

    def win(self):
        if messagebox.askyesno("WIN", "You won!! Do you want to play again?"):
            self.play()
        else:
            exit(0)

    def lose(self):
        if messagebox.askyesno("Lost", "You lost!! Do you want to play again?"):
            self.play()
        else:
            exit(0)


if __name__ == "__main__":
    g = HangmanGUI()
