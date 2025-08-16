Big big big thanks to projects with Digambar for the great set of tutorials. In the db.py script you are going to have to manually add all the contacts you want to have in the jarvis.db file. I recommend downloading the SQL viewer extension in VS code. The code written is specifically made for MacOS. If you do wish to fork this over please feel free to. Some of the features such as opening apps require commands in the vs code terminal. in the features script I have written open -a {query}. For people who use windows this command would be changed to start {query}. Another difference that may cause issues on windowsOS is the feature where you can call and message people from whatsapp. If you wish to add the feature where you can call and message people through whatsapp I recommend going to google contacts or the contacts app in your macbook and pressing export. Then put the contact into a google sheets, afterwards delete any collumns you don't wish to have, finally export using .CSV format. I apologize for any differences I may be forgetting. I also recommend downloading pvporcupine library if you do wish to add a wake word into your project so that if you simply say "blueberry" it would start listening. To avoid the outrages fees of pvporcupine you can simply pip install an older version such as pvporcupine 1.9.2 the command would look something like: pip install pvporcupine==1.9.2. I unfortunatly could not add this feature into my project since the older version lacks support to the Mac terminal. If you face any issues regarding the code please feel free to contact me at vishishtvb@gmail.com. Thank you! 

Here are some of the pip install commands you are going to need:

pip install os 

pip install webbrowser

pip install sqlite3

pip install time 

pip install eel

pip install speechrecognition as sr

pip install google-genai

pip install pyaudio 

pip install pyttsx3  
