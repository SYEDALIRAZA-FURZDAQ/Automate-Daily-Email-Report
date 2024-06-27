from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os
import subprocess

class Watcher:
    DIRECTORY_TO_WATCH = "."

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")

        self.observer.join()

class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'modified':
            # Restart the main script on modification
            print(f"File modified: {event.src_path}")
            subprocess.run(["python", "main.py"])

if __name__ == '__main__':
    w = Watcher()
    w.run()
