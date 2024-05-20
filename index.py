from tkinter import *
from tkinter import ttk, messagebox
import googletrans
from googletrans import Translator
import threading

# Configuração inicial da janela principal
root = Tk()
root.title("Tradutor")
root.geometry("1080x400")
root.resizable(False, False)
root.configure(background="white")

# Função para atualizar os rótulos dos idiomas selecionados nas comboboxes
def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000, label_change)  # Chama a função novamente após 1 segundo

# Função para traduzir o texto em uma thread separada
def translate_now():
    text_ = text1.get(1.0, END)  # Obtém o texto do widget Text
    t1 = Translator()  # Cria uma instância do tradutor
    try:
        # Traduz o texto da linguagem de origem para a linguagem de destino
        trans_text = t1.translate(text_, src=combo1.get(), dest=combo2.get())
        trans_text = trans_text.text

        # Insere o texto traduzido no widget Text de saída
        text2.delete(1.0, END)
        text2.insert(END, trans_text)
    except AttributeError as e:
        # Exibe uma mensagem de erro específica se ocorrer um AttributeError
        messagebox.showerror("Erro", "Erro de tradução. Por favor, verifique sua conexão de internet ou tente novamente.")
    except Exception as e:
        # Exibe uma mensagem de erro genérica para outras exceções
        messagebox.showerror("Erro", str(e))

# Função para iniciar a tradução em uma thread separada
def translate_now_thread():
    translate_thread = threading.Thread(target=translate_now)
    translate_thread.start()

# Dicionário de idiomas suportados pela API do Google Translate
language = googletrans.LANGUAGES
languageV = list(language.values())  # Lista dos nomes dos idiomas
lang1 = language.keys()  # Lista das chaves dos idiomas

# Configuração da combobox para selecionar o idioma de origem
combo1 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="readonly")
combo1.place(x=110, y=20)
combo1.set("english")  # Define o idioma padrão como inglês

# Rótulo para exibir o idioma de origem selecionado
label1 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)

# Configuração da combobox para selecionar o idioma de destino
combo2 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="readonly")
combo2.place(x=730, y=20)
combo2.set("choose language")  # Define o texto padrão como "choose language"

# Rótulo para exibir o idioma de destino selecionado
label2 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label2.place(x=620, y=50)

# Frame para o widget Text de entrada
f = Frame(root, bg="Black", bd=5)
f.place(x=10, y=118, width=440, height=210)

# Widget Text para inserir o texto a ser traduzido
text1 = Text(f, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

# Scrollbar para o widget Text de entrada
scrollbar1 = Scrollbar(f)
scrollbar1.pack(side="right", fill='y')
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# Frame para o widget Text de saída
f1 = Frame(root, bg="Black", bd=5)
f1.place(x=620, y=118, width=440, height=210)

# Widget Text para exibir o texto traduzido
text2 = Text(f1, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

# Scrollbar para o widget Text de saída
scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side="right", fill='y')
scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

# Botão para iniciar a tradução
translate = Button(root, text="Traduzir", font=("Roboto", 15), activebackground="white", cursor="hand2", bd=1, width=10, height=2, bg="black", fg="white", command=translate_now_thread)
translate.place(x=476, y=250)

# Chama a função para atualizar os rótulos dos idiomas
label_change()

# Inicia o loop principal da interface gráfica
root.mainloop()
