import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/PC PERFORMANCE/Downloads"

class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Olá, {event.src_path}foi criado!")

    def on_deleted(self, event):
        print(f"Opa! Alguém excluiu {event.src_path}!") 

    def on_moved(self, event):
        print(f"O arquivo {event.src_path} foi movido ou renomeado") 

    def on_deleted(self, event):
        print(f"O arquivo {event.src_path} foi deletado")   

event_handler = FileEventHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive=True)

observer.start()

try:
    while True:
        time.sleep(2)
        print("executando...")
except KeyboardInterrupt:
    print("Interrompido!")
    observer.stop()        

