import pyttsx3
import speech_recognition as sr
import eel
import time

# Initialize Gemini API
GEMINI_AVAILABLE = False
client = None

try:
    from google import genai
    client = genai.Client(api_key="Your Gemini api key herer please")
    GEMINI_AVAILABLE = True
    print("Gemini API configured successfully")
except Exception as e:
    print(f"Gemini setup error: {e}")
    GEMINI_AVAILABLE = False

def speak(text):
    engine = pyttsx3.init("nsss")
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[14].id)  
    engine.setProperty('rate', 174)
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()

def get_ai_response(query):
    if GEMINI_AVAILABLE and client:
        try:
            # Add instruction to keep response concise
            prompt = f"{query}. Please keep your response concise, no more than 100 words."
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            return response.text.strip()
        except Exception as e:
            print(f"Gemini API error: {e}")
            return fallback_response(query)
    else:
        return fallback_response(query)

def fallback_response(query):
    responses = {
        "hello": "Hello! How can I help you today?",
        "how are you": "I'm doing well, thank you for asking!",
        "joke": "why do programmers prefer dark mode? becaues light attracts bugs",
        "thanks": "You're welcome! Is there anything else I can help you with?",
    }
    
    query_lower = query.lower()
    for key, response in responses.items():
        if key in query_lower:
            return response
    
    return "I understand you're asking about: " + query + ". Unfortunately, I don't have access to my AI service right now, but I'm still here to help with your other commands!"

def takecommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("listening...")
        eel.DisplayMessage('listening...')
        eel.sleep(0.1)
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=10, phrase_time_limit=6)

    try:
        print('recognizing')
        eel.DisplayMessage('recognizing')
        eel.sleep(0.1)
        query = r.recognize_google(audio, language='en')
        print(f"user said: {query}")
        eel.DisplayMessage(query)
        time.sleep(2)  

    except Exception as e:
        print(f"Recognition error: {e}")
        return ""

    return query.lower()

@eel.expose
def openWhatsApp():
    import webbrowser
    speak("Opening WhatsApp Web")
    webbrowser.open("https://web.whatsapp.com")

@eel.expose
def allCommands(text_query=None, message=1):
    if text_query:
        query = text_query.lower()
        print(f"Text command: {query}")
    elif message == 1:
        query = takecommand()
        print(f"Voice command: {query}")
    else:
        query = str(message).lower()

    if not query:
        return

    if "open" in query:
        from engine.features import openCommand
        openCommand(query)
    
    elif "on youtube" in query:
        from engine.features import PlayYoutube
        PlayYoutube(query)
    
    elif "send message" in query or "message" in query:
        from engine.features import whatsappMessage
        whatsappMessage(query)
    
    elif "whatsapp call" in query or ("call" in query and "whatsapp" in query):
        from engine.features import whatsappCall
        whatsappCall(query)
        
    elif "call" in query:
        from engine.features import whatsappCall
        whatsappCall(query)
    
    elif "list contacts" in query or "show contacts" in query:
        from engine.features import listContacts
        listContacts()
    
    elif "search contact" in query or "find contact" in query:
        from engine.features import searchContact
        searchContact(query)
    
    else: 
        ai_response = get_ai_response(query)
        speak(ai_response)
    
    eel.ShowHood()