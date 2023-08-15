from tkinter import *
import smtplib
from tkinter import messagebox
import re
# Create the main window
root = Tk()
root.title("Email Sender")
root.geometry("552x400")
root.minsize(552,400)
root.maxsize(552,400)
root.iconbitmap("img1.ico")
# Create and place widgets
def main():
    screen=Frame(root,width=552,height=400,bg="DodgerBlue")
    screen.place(x=0,y=0)
    global email_entry
    global password_entry

    Label(screen, text="Email Sender", font=("Helvetica", 20,"bold"),bg="DodgerBlue").place(x=195,y=10)

    email_label = Label(screen, text="Your Email:",font=("Helvetica", 10,"bold"),width=17,bg="RoyalBlue")
    email_label.place(x=80,y=107)
    email_entry = Entry(screen,text="",font=("Helvetica", 15),width=20)
    email_entry.place(x=250,y=105)

    password_label = Label(screen, text="Your Password:",font=("Helvetica", 10,"bold"),width=17,bg="RoyalBlue")
    password_label.place(x=80,y=157)
    password_entry = Entry(screen, show="*",text="",font=("Helvetica", 15),width=20)
    password_entry.place(x=250,y=155)
    login = Button(screen, text="Login",font=("Helvetica", 15,"bold"), command=log,width=10,bg="RoyalBlue")
    login.place(x=225,y=335)


def validelogin():
    sender_email = str(email_entry.get())
    sender_password = str(password_entry.get())
    if (sender_email == "") or (sender_password == ""):
        messagebox.showinfo("Notification", "Fill all the Fields")
        return False
    else:
        email_regex = re.compile(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$")
        if not email_regex.match(sender_email):
            messagebox.showinfo("Notification", "Enter a valid Email Address")
            return False
        else:
            return True
def log():
    global server
    if validelogin():
        try:
            sender_email = str(email_entry.get())
            sender_password = str(password_entry.get())
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, sender_password)
            messagebox.showinfo("Notification", "you are logged in")
            frame1()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
def validmess():
    recipient_email = recipient_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", END)
    if (recipient_email== "") or (subject == "" ) or (message == ""):
        messagebox.showinfo("Notification", "Fill all the Fields")
        return False
    else:
        email_regex = re.compile(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$")
        if not email_regex.match(recipient_email):
            messagebox.showinfo("Notification", "Enter a valid Email Address")
            return False
        else:
            return True
def logout():
    try:
        server.quit()
        messagebox.showinfo("Notification", "logged out")
        password_entry.delete(0, END)
        email_entry.delete(0, END)
        main()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def frame1():
    screen1 = Frame(root, width=552, height=400, bg="RoyalBlue")
    screen1.place(x=0, y=0)
    global recipient_entry
    global subject_entry
    global subject_entry
    global message_text
    recipient_label = Label(screen1, text="Recipient's Email:",bg="DodgerBlue",font=("Helvetica", 10,"bold"))
    recipient_label.place(x=10,y=5)
    recipient_entry = Entry(screen1,text="",font=("Helvetica", 18),width=30)
    recipient_entry.place(x=10,y=30)

    subject_label = Label(screen1, text="Subject:",bg="DodgerBlue",font=("Helvetica", 10,"bold"))
    subject_label.place(x=10,y=65)
    subject_entry = Entry(screen1,text="",font=("Helvetica", 18),width=30)
    subject_entry.place(x=10,y=90)

    message_label = Label(screen1, text="Message:",bg="DodgerBlue",font=("Helvetica", 10,"bold"))
    message_label.place(x=10,y=125)
    message_text = Text(screen1, height=9, width=59,font=("Helvetica", 12,))
    message_text.place(x=10,y=150)

    send_button = Button(screen1, text="Send Email", command=send_email,bg="DodgerBlue",font=("Helvetica", 13,"bold"))
    send_button.place(x=443,y=320)
    logout1 = Button(screen1, text="Logout", command=logout,bg="DodgerBlue",font=("Helvetica", 13,"bold"))
    logout1.place(x=240,y=360)
def send_email():
    global server
    if validmess():
        try:
            sender_email = email_entry.get()
            sender_password = password_entry.get()
            recipient_email = recipient_entry.get()
            subject = subject_entry.get()
            message = message_text.get("1.0", END)

            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, sender_password)

            email_message = f"Subject: {subject}\n\n{message}"
            server.sendmail(sender_email, recipient_email, email_message)

            server.quit()
            messagebox.showinfo("Success", "Email sent successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
main()
# Start the Tkinter main loop
root.mainloop()
