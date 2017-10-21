from tkinter import *
import base64
from tkinter import messagebox

fonte = ('SourceCodePro', 15)


class TlBase64(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)

        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (TelaInicial, TlEncode, TlDecode):
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
        # Título
        lbTil = Label(self, text='Encode|Decode', font=fonte)
        lbTil.place(x=124, y=10)
        # Botão Encode
        btEnc = Button(self, text='Enconde', font=fonte,
                       command=lambda: controller.show_frame(TlEncode))
        btEnc.place(x=150, y=50)
        # Botão Decode
        btDec = Button(self, text='Decode', font=fonte,
                       command=lambda: controller.show_frame(TlDecode))
        btDec.place(x=155, y=100)
        # Botão Quit
        btQuit = Button(self, text='Sair', font=fonte,
                        command=exit)
        btQuit.place(x=170, y=150)


class TlEncode(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        # Entrada Encode
        texenc = Text(self, bd=5, width=30, height=6, font=fonte)
        texenc.place(x=0, y=0)
        # Botão Krypt
        btKry = Button(self, text='Krypt', font=fonte,
                       command=lambda: encode_tex(texenc))
        btKry.place(x=200, y=150)
        # Botão Voltar
        btback = Button(self, text='Voltar', font=fonte,
                        command=lambda: controller.show_frame(TelaInicial))
        btback.place(x=100, y=150)


class TlDecode(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        # Entrada Decode
        texdec = Text(self, bd=5, width=30, height=6, font=fonte)
        texdec.place(x=0, y=0)
        # Botão DKrypt
        btDKry = Button(self, text='DKrypt', font=fonte,
                        command=lambda: decode_tex(texdec))
        btDKry.place(x=200, y=150)
        # Botão Voltar
        btback = Button(self, text='Voltar', font=fonte,
                        command=lambda: controller.show_frame(TelaInicial))
        btback.place(x=100, y=150)


def encode_tex(texenc):
    encrypt = ''
    data = texenc.get(1.0, END)
    encoded = data.encode('ascii')
    bit_encrypt = base64.b64encode(encoded)
    bit_encrypt = str(bit_encrypt)

    for i in range(1, len(bit_encrypt)):
        if bit_encrypt[i] == "'":
            pass
        else:
            encrypt += bit_encrypt[i]
    arq_enc = open('arqEncode.txt', 'w')
    arq_enc.write(encrypt)
    arq_enc.close()
    messagebox.showinfo('Encode', 'Mensagem codificada, arquivo salvo com sucesso!')
    return encrypt


def decode_tex(texdec):
    decrypt = ''
    data = texdec.get(1.0, END)
    bit_decrypt = base64.b64decode(data)
    bit_decrypt = str(bit_decrypt)

    for j in range(1, len(bit_decrypt)):
        if bit_decrypt[j] == "'":
            pass
        else:
            decrypt += bit_decrypt[j]

    arq_dec = open('arqDecode.txt', 'w')
    arq_dec.write(decrypt.strip())
    arq_dec.close()
    messagebox.showinfo('Decode', 'Mensagem decodificada, arquivo salvo com sucesso')


b64 = TlBase64()
b64.title('Encode|Decode by: tiagokriok')
b64.geometry('380x200')
b64.resizable(FALSE, FALSE)
b64.mainloop()
