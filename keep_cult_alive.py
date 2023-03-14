from flask import Flask
from threading import Thread
app = Flask('')

@app.route('/')
def main():
  return ("The demon has awoken! Become one of his chosen...")

def run():
  app.run(host="0.0.0.0", port = 8080)

def creatures_coming():
  server = Thread(target=run)
  server.start()
