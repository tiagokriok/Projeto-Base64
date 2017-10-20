from tkinter import *

fonte = ('SourceCodePro', 15)


class TlBase64(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self,*args,**kwargs)
        container = Frame(self)

        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (TelaInicial,):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(TelaInicial)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class TelaInicial(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        # Botão Encode
        btEnc = Button(self, text='Enconde', font=fonte,
                       command=lambda: controller.show_frame(TlEncode))
        btEnc.place(x=150, y=50)
        # Botão Decode
        btDec = Button(self, text='Decode', font=fonte,
                       command=lambda:controller.show_frame(TlDecode))
        btDec.place(x=155, y=100)


class TlEncode(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        # entenc = Entry(self, )


b64 = TlBase64()
b64.title('Encode|Decode by: tiagokriok')
b64.geometry('380x200')
b64.mainloop()
