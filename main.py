import eel
from engine.command import *

eel.init('www')

eel.start(
    'index.html',
    size=(600, 1200),   # Popup size
    host='localhost',
    port=8000,
)
