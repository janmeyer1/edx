from twilio.rest import Client
from datetime import datetime
import os
import requests
from bs4 import BeautifulSoup
from difflib import SequenceMatcher
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Twilio credentials
account_sid = 'ACfe445b759c0bb088bc79e704f6886426'
auth_token = 'd377bc87ced004775858d0e0e5ce7279'
twilio_phone_number = '+12565302522'  # Updated Twilio WhatsApp number
your_phone_number = '+4915174278492'

# Twilio client
client = Client(account_sid, auth_token)

# Paths for saving data
keywords_file = 'keywords.txt'
digest_file = 'digest.txt'

# Function to perform web search and return a digest
def search_and_digest(query):
    try:
        search_url = f'https://api.duckduckgo.com/?q={query}&format=json'
        response = requests.get(search_url)
        response.raise_for_status()  # Raise HTTPError for bad responses
        data = response.json()
        results = [result['text'] for result in data.get('Results', [])]
        digest = ' '.join(results)
        return digest
    except Exception as e:
        logger.error(f"Error during search_and_digest: {e}")
        return "Error during search. Please try again later."

# Function to save keywords to a file
def save_keywords(keywords):
    with open(keywords_file, 'w') as file:
        for keyword in keywords:
            file.write(keyword + '\n')

# Function to save digest to a file
def save_digest(digest):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'digest_{timestamp}.txt'
    with open(filename, 'w') as file:
        file.write(digest)

# Function to compare two digests and report the most important updates
def compare_and_report(old_digest, new_digest):
    similarity_ratio = SequenceMatcher(None, old_digest, new_digest).ratio()
    if similarity_ratio < 0.95:
        return "There are significant updates in the search results."
    else:
        return "No significant updates found."

# Function to process user commands
def process_command(command, keywords, digest):
    if command.startswith('search'):
        query = command.replace('search ', '')
        new_digest = search_and_digest(query)
        save_digest(new_digest)
        return "Search results saved."

    elif command.startswith('keywords'):
        save_keywords(keywords)
        return "Keywords saved."

    elif command.startswith('digest'):
        new_digest = search_and_digest(' '.join(keywords))
        report = compare_and_report(digest, new_digest)
        save_digest(new_digest)
        return report
