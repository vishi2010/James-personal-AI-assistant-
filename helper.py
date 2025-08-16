# engine/helper.py
import re

def Extract_YT_term(command):
    # pattern: play [song name] on youtube
    pattern = r'play\s+(.+?)\s+on youtube'
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else None

def remove_words(input_string, words_to_remove):
    # Convert both input_string and words_to_remove to lowercase for case-insensitive matching
    input_words = input_string.lower().split()
    words_to_remove_lower = [word.lower() for word in words_to_remove]
    
    # Remove unwanted words
    filtered_words = [word for word in input_words if word not in words_to_remove_lower]
    
    # Join the remaining words back into a string
    return ' '.join(filtered_words)

def extract_message_content(command):
    """Extract contact name and message from voice command"""
    command = command.lower()
    
    # Pattern 1: "send message to [name] saying [message]"
    pattern1 = r'send message to\s+(.+?)\s+saying\s+(.+)'
    match1 = re.search(pattern1, command, re.IGNORECASE)
    if match1:
        return match1.group(1).strip(), match1.group(2).strip()
    
    # Pattern 2: "message [name] [message]"
    pattern2 = r'message\s+(\w+)\s+(.+)'
    match2 = re.search(pattern2, command, re.IGNORECASE)
    if match2:
        return match2.group(1).strip(), match2.group(2).strip()
    
    # Pattern 3: "text [name] [message]"
    pattern3 = r'text\s+(\w+)\s+(.+)'
    match3 = re.search(pattern3, command, re.IGNORECASE)
    if match3:
        return match3.group(1).strip(), match3.group(2).strip()
    
    return None, None

def extract_contact_name(command):
    """Extract contact name from call command"""
    command = command.lower()
    
    # Remove common words
    words_to_remove = ['whatsapp', 'call', 'please', 'can', 'you', 'the']
    contact_name = remove_words(command, words_to_remove).strip()
    
    return contact_name if contact_name else None