import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import i2clcda
import time

vtext=""
char_max=16
firebase_admin.initialize_app(credentials.Certificate('/home/pi/fkey.json'))
db = firestore.client()

def on_snapshot(doc_snapshot, changes, read_time):
    global vtext
    for doc in doc_snapshot:
        print(doc.to_dict()["vtext"])
        vtext=doc.to_dict()["vtext"]

doc_ref = db.collection(u'datas').document(u'text')
doc_watch = doc_ref.on_snapshot(on_snapshot)
i2clcda.lcd_init()
while True:
    time.sleep(1)
    print(vtext)
    i2clcda.lcd_string(vtext,i2clcda.LCD_LINE_1)