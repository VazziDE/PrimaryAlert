import tkinter

root = tkinter.Tk()
root.geometry("300x300")
root.resizable(False, False)
root.title("PrimaryAlert")

canvas = tkinter.Canvas(root, height=300, width=300)
canvas.pack()


def checkInput():
    testnumber = numberinput.get().split(" ")[0]
    if testnumber != "":

        intOfString = int(testnumber)
        if intOfString > 0:
            isPrimary = True
            alreadyDividers = 0

            for x in range(1, intOfString + 1):
                if isPrimary:
                    if alreadyDividers < 3:
                        if intOfString % x == 0:
                            alreadyDividers += 1
                    else:
                        break
            if alreadyDividers == 1 or alreadyDividers > 2:
                isPrimary = False
            if isPrimary:
                result.config(text="Your Number " + str(intOfString) + " is a primary.")
            else:
                result.config(text="Your Number " + str(intOfString) + " is not a primary.")
            numberinput.delete(0, "end")


title = tkinter.Label(root, fg="#9c88ff", text="PrimaryAlert")
title.config(font=("Sitka Display", 32))
canvas.create_window(150, 50, window=title)

numberinput = tkinter.Entry(root, background="#00a8ff", foreground="#ffffff")
canvas.create_window(150, 150, window=numberinput)

checkbtn = tkinter.Button(root, background="#4cd137", foreground="black", text="Check", command=checkInput)
canvas.create_window(150, 200, window=checkbtn)

result = tkinter.Label(root, fg="black", text="")
result.config(font=("Sitka Display", 15))
canvas.create_window(150, 250, window=result)

root.mainloop()
