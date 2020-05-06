import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time

firebase_admin.initialize_app(credentials.Certificate('/home/pi/fkey.json'))
db = firestore.client()
def on_snapshot(doc_snapshot, changes, read_time):
    for doc in doc_snapshot:
        print(u'Received document snapshot: {}'.format(doc.id))
        print(doc.to_dict())

doc_ref = db.collection(u'datas').document(u'text')
doc_watch = doc_ref.on_snapshot(on_snapshot)

while True:
    print(".")
    time.sleep(5)