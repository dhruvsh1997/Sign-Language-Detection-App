import Tkinter as tk
from AnimatedGif import AnimatedGif
from main import callByName, callByAudio

def counter(message):
    messageLabel.config(text=message)

def getDataByRecordAudio():
    counter("Please wait while we are processing")
    responseData = callByAudio()
    showAnimation(responseData)

def getDataByWord():
    counter("Please wait while we are processing")
    inputData = inputWord.get()
    if inputData == "":
        counter("Please Enter a Valid Word")
        return

    counter("Please wait while we are processing")
    responseData = callByName(inputData)
    showAnimation(responseData)

def showAnimation(responseData):
    message = responseData[0]
    path_to_pic = responseData[1]
    if (path_to_pic == "error"):
        counter(message)
        return
    showAnimationGif(path_to_pic, message)

def showAnimationGif(path_to_pic, message):
    Window = tk.Toplevel()
    canvas = tk.Canvas(Window, height=50, width=200)
    lbl_with_my_gif = AnimatedGif(Window, path_to_pic, 0.1)  # (tkinter.parent, filename, delay between frames)
    lbl_with_my_gif.pack()
    messageLabel = tk.Label(Window, text=message)
    messageLabel.pack(pady=20)
    counter("Last Word: "+message)
    exit_button = tk.Button(Window, text="Exit", command=Window.destroy)
    exit_button.pack(pady=20)
    lbl_with_my_gif.start()
    canvas.pack()

ws = tk.Tk()
ws.title("SIGN LANGUAGE INTERFACE")
ws.geometry("450x300")
label = tk.Label(ws, text=" SIGN LANGUAGE INTERFACE")
label.pack(pady=10)

messageLabel = tk.Label(ws, text="Please Press Record Button To Start or Type a Word in Textbox")
messageLabel.pack(pady=20)

inputWord = tk.Label(ws, text="Word").place(x=40, y=100)
inputWord = tk.Entry(ws, width=30)
inputWord.place(x=110, y=100)

showSign = tk.Button(ws, text="Find", bg='White', fg='Black',
                   command=lambda: getDataByWord())
showSign.place(x=330, y=98)

recordButton = tk.Button(ws, text="Record", bg='White', fg='Black',
                   command=lambda: getDataByRecordAudio())
recordButton.place(x=200, y=150)

exit_button = tk.Button(ws, text="Exit", fg='Red', command=ws.destroy)
exit_button.place(x=215, y=200)

ws.mainloop()