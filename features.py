import os
from shlex import quote
import subprocess
import time
import webbrowser
import urllib.parse

import pyautogui
from engine.config import ASSITANT_NAME
from engine.command import speak
import sqlite3

from engine.helper import Extract_YT_term, remove_words

con = sqlite3.connect("jarvis.db")
cursor = con.cursor()

def openCommand(query):
    query = query.replace(ASSITANT_NAME, "")
    query = query.replace("open", "").strip()
    app_name = query.lower()
def openCommand(query):
    query = query.replace(ASSITANT_NAME, "")
    query = query.replace("open", "").strip()
    app_name = query.strip()

    if app_name != "":
        try:
            cursor.execute('SELECT path FROM sys_command WHERE LOWER(name) = ?', (app_name.lower(),))
            results = cursor.fetchall()

            if results:
                speak(f"Opening {app_name}")
                os.system(f'open "{results[0][0]}"')  

            else:
                cursor.execute('SELECT url FROM web_command WHERE LOWER(name) = ?', (app_name.lower(),))
                results = cursor.fetchall()

                if results:
                    speak(f"Opening {app_name} website")
                    webbrowser.open(results[0][0])
                else:
                    speak(f"Opening {app_name}")
                    os.system(f'open -a "{app_name}"') 
        except Exception as e:
            speak("Something went wrong while opening")
            print(e)


def PlayYoutube(command):
    song = Extract_YT_term(command)
    if song:
        speak(f"Playing {song} on YouTube")
        os.system(f'open "https://www.youtube.com/results?search_query={song}"')
    else:
        speak("I couldn't find what you were looking for")

def findContact(name):
    try:
        name = name.strip().lower()
        cursor.execute("SELECT name, mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", 
                      ('%' + name + '%', name + '%'))
        results = cursor.fetchall()
        return results
    except Exception as e:
        print(f"Database error: {e}")
        return []

def whatsappMessage(command):
    try:
        command = command.lower()
        
        if "send message to" in command and "saying" in command:
            parts = command.split("send message to")[1].split("saying")
            contact_name = parts[0].strip()
            message_text = parts[1].strip()
        elif "message" in command:
            parts = command.split("message")[1].strip().split()
            if len(parts) >= 2:
                contact_name = parts[0]
                message_text = " ".join(parts[1:])
            else:
                speak("Please specify both contact name and message")
                return
        else:
            speak("Please say 'send message to [name] saying [message]' or 'message [name] [message]'")
            return

        contacts = findContact(contact_name)
        
        if not contacts:
            speak(f"Sorry, I couldn't find {contact_name} in your contacts")
            return
        
        if len(contacts) > 1:
            speak(f"Found multiple contacts with {contact_name}. Using the first one: {contacts[0][0]}")
        
        contact_name_db = contacts[0][0]
        phone_number = contacts[0][1]
        
        phone_number = ''.join(filter(str.isdigit, phone_number))
        
        if not phone_number.startswith('1') and len(phone_number) == 10:
            phone_number = '1' + phone_number
        
        speak(f"Sending message to {contact_name_db}")
        
        encoded_message = urllib.parse.quote(message_text)
        
        whatsapp_url = f"https://web.whatsapp.com/send?phone={phone_number}&text={encoded_message}"
        
        webbrowser.open(whatsapp_url)
        
        time.sleep(5)
        
        try:
            time.sleep(3)
            pyautogui.press('enter')
            speak("Message sent successfully")
        except Exception as e:
            speak("Message window opened. Please click send manually.")
            print(f"Auto-send failed: {e}")
            
    except Exception as e:
        speak("Something went wrong while sending the message")
        print(f"WhatsApp message error: {e}")

def whatsappCall(command):
    try:
        command = command.lower()
        
        if "call" in command:
            if "whatsapp call" in command:
                contact_name = command.replace("whatsapp call", "").strip()
            else:
                contact_name = command.replace("call", "").strip()
        else:
            speak("Please say 'call [contact name]' or 'whatsapp call [contact name]'")
            return
        
        contacts = findContact(contact_name)
        
        if not contacts:
            speak(f"Sorry, I couldn't find {contact_name} in your contacts")
            return
        
        if len(contacts) > 1:
            speak(f"Found multiple contacts with {contact_name}. Using the first one: {contacts[0][0]}")
        
        contact_name_db = contacts[0][0]
        phone_number = contacts[0][1]
        
        phone_number = ''.join(filter(str.isdigit, phone_number))
        
        if not phone_number.startswith('1') and len(phone_number) == 10:
            phone_number = '1' + phone_number
        
        speak(f"Calling {contact_name_db} on WhatsApp")
        
        whatsapp_url = f"https://web.whatsapp.com/send?phone={phone_number}"
        
        webbrowser.open(whatsapp_url)
        
        time.sleep(8)
        
        try:
            pyautogui.hotkey('ctrl', 'shift', 'c')  
            speak("Call initiated. Please check your WhatsApp Web window.")
        except Exception as e:
            speak("WhatsApp opened. Please click the call button manually.")
            print(f"Auto-call failed: {e}")
            
    except Exception as e:
        speak("Something went wrong while making the call")
        print(f"WhatsApp call error: {e}")

def listContacts():
    try:
        cursor.execute("SELECT name FROM contacts ORDER BY name")
        results = cursor.fetchall()
        
        if results:
            contact_names = [contact[0] for contact in results[:10]]
            if len(results) > 10:
                speak(f"You have {len(results)} contacts. Here are the first 10: {', '.join(contact_names)}")
            else:
                speak(f"Your contacts are: {', '.join(contact_names)}")
        else:
            speak("No contacts found in your database")
    except Exception as e:
        speak("Something went wrong while retrieving contacts")
        print(f"List contacts error: {e}")

def searchContact(command):
    try:
        command = command.lower()
        if "search contact" in command:
            search_term = command.replace("search contact", "").strip()
        elif "find contact" in command:
            search_term = command.replace("find contact", "").strip()
        else:
            speak("Please say 'search contact [name]' or 'find contact [name]'")
            return
        
        contacts = findContact(search_term)
        
        if contacts:
            if len(contacts) == 1:
                speak(f"Found contact: {contacts[0][0]} with number {contacts[0][1]}")
            else:
                names = [contact[0] for contact in contacts]
                speak(f"Found {len(contacts)} contacts: {', '.join(names)}")
        else:
            speak(f"No contacts found matching {search_term}")
    except Exception as e:
        speak("Something went wrong while searching contacts")
        print(f"Search contact error: {e}")
