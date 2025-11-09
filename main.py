import tkinter as tk
from tkinter import filedialog, messagebox
import smtplib
import webbrowser
import os
import pyautogui
from time import sleep

# Cores e fonte
cor_fundo = "#ffffff"
cor_texto = "#ff6600"
fonte_padrao = ("Arial", 12)

# Tela principal de login
root = tk.Tk()
root.title("Login - Sistema de Automação")
root.geometry("400x350")
root.configure(bg=cor_fundo)


def validar_login():
    usuario = entrada_usuario.get().strip().lower()
    senha = entrada_senha.get().strip()

    usuarios_permitidos = ["tfcamargo", "thifcamargo04@gmail.com"]
    senhas_permitidas = ["THIago070404", "Thi070404"]

    if usuario in usuarios_permitidos:
        if senha in senhas_permitidas:
            messagebox.showinfo("Bem-vindo", "Olá Thiago!\nbem-vindo ao sistema.")
            root.destroy()
            abrir_interface_automacao()
        else:
            messagebox.showerror("Error password", "Senha incorreta!! \nTente novamente com outra senha.")
            
    elif usuario == "adm":
        if senha == "123":
            messagebox.showinfo("Bem-vindo", "Olá, Adm.\nAcesso autorizado!!")
            root.destroy()
            abrir_interface_automacao()
        else:
            messagebox.showerror("Error password", "Senha incorreta!! \nTente novamente com outra senha.")
    else:
        messagebox.showerror("Error", "Acesso Negado!! \nVocê não possui permissão para acessar esse sistema.")


def abrir_interface_automacao():
    janela = tk.Tk()
    janela.title("Escolha o tipo de automação")
    janela.geometry("400x250")
    janela.configure(bg=cor_fundo)

    tk.Label(janela, text="Escolha o tipo de automação:", font=fonte_padrao, fg=cor_texto, bg=cor_fundo).pack(pady=20)

    tk.Button(janela, text="Automação de E-mails", command=abrir_email_interface, width=25, font=fonte_padrao, bg=cor_texto, fg="white").pack(pady=10)
    tk.Button(janela, text="Automação de Mensagens", command=abrir_mensagem_interface, width=25, font=fonte_padrao, bg=cor_texto, fg="white").pack(pady=10)


def abrir_email_interface():
    janela = tk.Toplevel()
    janela.title("Automação de E-mails")
    janela.geometry("500x500")
    janela.configure(bg=cor_fundo)

    def enviar_email_gmail_web():
        destinatario = entrada_destinatario.get()
        assunto = entrada_assunto.get()
        corpo = texto_email.get("1.0", tk.END)
        
        if not destinatario or not assunto:
            messagebox.showerror("Erro", "Preencha todos os campos obrigatórios.")
            return
        messagebox.showinfo("Aviso", "O Gmail será aberto. Certifique-se de estar logado e não mexa no computador até o envio.")

        # Abre o Gmail no navegador
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox?compose=new")
        sleep(10)  # Tempo para o Gmail carregar totalmente

        # Preenche o e-mail automaticamente
        pyautogui.write(destinatario)
        sleep(1)
        pyautogui.press("tab") 
        sleep(0.5)
        pyautogui.press("tab")  # Vai para o campo de assunto
        sleep(0.5)
        pyautogui.write(assunto)
        sleep(0.5)
        pyautogui.press("tab")  
        sleep(0.5)
        pyautogui.write(corpo)
        sleep(1)
        pyautogui.hotkey("ctrl", "enter")  # Envia o e-mail

    tk.Label(janela, text="Seu e-mail:", font=fonte_padrao, fg=cor_texto, bg=cor_fundo).pack(pady=15)
    entrada_usuario = tk.Entry(janela, width=40)
    entrada_usuario.pack()

    tk.Label(janela, text="E-mail do destinatário:", font=fonte_padrao, fg=cor_texto, bg=cor_fundo).pack(pady=15)
    entrada_destinatario = tk.Entry(janela, width=40)
    entrada_destinatario.pack()

    tk.Label(janela, text="Assunto:", font=fonte_padrao, fg=cor_texto, bg=cor_fundo).pack(pady=15)
    entrada_assunto = tk.Entry(janela, width=40)
    entrada_assunto.pack()

    tk.Label(janela, text="Texto:", font=fonte_padrao, fg=cor_texto, bg=cor_fundo).pack(pady=5)
    texto_email = tk.Text(janela, height=5, width=50)
    texto_email.pack()

    tk.Button(janela, text="Enviar", command=enviar_email_gmail_web, bg=cor_texto, fg="white").pack(pady=10)


def abrir_mensagem_interface():
    janela = tk.Toplevel()
    janela.title("Automação de Mensagens")
    janela.geometry("500x400")
    janela.configure(bg=cor_fundo)

    def gerar_link():
        numero = entrada_numero.get()
        msg_cliente = entrada_msg_cliente.get()
        
        if not numero or not msg_cliente:
            messagebox.showerror("Erro", "Preencha todos os campos obrigatórios.")
            return

        link = f"https://api.whatsapp.com/send?phone=55{numero}&text={msg_cliente.replace(' ', '%20')}"
        webbrowser.open(link)

    tk.Label(janela, text="Seu número (com DDD):", font=fonte_padrao, fg=cor_texto, bg=cor_fundo).pack(pady=25)
    entrada_numero = tk.Entry(janela, width=30)
    entrada_numero.pack()

    tk.Label(janela, text="Mensagem enviada pelo cliente: ", font=fonte_padrao, fg=cor_texto, bg=cor_fundo).pack(pady=25)
    entrada_msg_cliente = tk.Entry(janela, width=50)
    entrada_msg_cliente.pack()

    tk.Button(janela, text="Gerar link WhatsApp", command=gerar_link, bg=cor_texto, fg="white").pack(pady=75)

# Interface de login
label_titulo = tk.Label(root, text="LOGIN - SISTEMA DE AUTOMAÇÃO", font=("Arial", 14), fg=cor_texto, bg=cor_fundo)
label_titulo.pack(pady=20)

tk.Label(root, text="Usuário:", font=fonte_padrao, fg=cor_texto, bg=cor_fundo).pack()
entrada_usuario = tk.Entry(root, width=30)
entrada_usuario.pack(pady=5)

tk.Label(root, text="Senha:", font=fonte_padrao, fg=cor_texto, bg=cor_fundo).pack()
entrada_senha = tk.Entry(root, show="*", width=30)
entrada_senha.pack(pady=5)

tk.Button(root, text="Entrar", command=validar_login, font=fonte_padrao, bg=cor_texto, fg="white").pack(pady=20)

root.mainloop()
