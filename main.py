import textbase
from textbase.message import Message
from textbase import models
import os
from typing import List
#own code
import requests
from bs4 import BeautifulSoup
import csv

# #beautiful soup- data extraction

url = "https://www.moneycontrol.com/stocks/marketstats/sector-scan/bse/today.html"

# Send a request to the URL and get the HTML content
response = requests.get(url)
html_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find all the span elements with the specified class names
name_spans = soup.find_all("span", class_=["SubSectorWeb_w120__1ezEW"])

# Extract the names from the spans and store them in a list
names_list = [span.text.strip() for span in name_spans]

name_spans_per = soup.find_all("td", class_=["SubSectorWeb_grn__13lsS","SubSectorWeb_rd__1lg1i"])

# Extract the names from the spans and store them in a list
names_lis_per = [span.text.strip() for span in name_spans_per]

data = list(zip(names_list, names_lis_per))

# Specify the file path for the CSV file
csv_file_path = "/Users/aniketartani/Documents/chatbot/textbase-main/output_data.csv"

# Write the data to the CSV file
with open(csv_file_path, "w", newline="", encoding="utf-8") as csv_file:
    # Create a CSV writer object
    csv_writer = csv.writer(csv_file)

    # Write the header row
    csv_writer.writerow(["Name", "Percentage"])

    # Write the data rows
    csv_writer.writerows(data)
    print("extraction done")
#
# import torch
from transformers import pipeline
import pandas as pd
tqa = pipeline(task="table-question-answering",model="google/tapas-base-finetuned-wtq")
table=pd.read_csv("/Users/aniketartani/Documents/chatbot/textbase-main/output_data.csv")
table = table.astype(str)

# # Load your OpenAI API key
# models.OpenAI.api_key = "YOUR_API_KEY"
# # or from environment variable:
# # models.OpenAI.api_key = os.getenv("OPENAI_API_KEY")

# # Prompt for GPT-3.5 Turbo
# SYSTEM_PROMPT = """You are chatting with an AI. There are no specific prefixes for responses, so you can ask or talk about anything you like. The AI will respond in a natural, conversational manner. Feel free to start the conversation with any question or topic, and let's have a pleasant chat!
# """


@textbase.chatbot("talking-bot")
def on_message(message_history: List[Message], state: dict = None):
    """Your chatbot logic here
    message_history: List of user messages
    state: A dictionary to store any stateful information

    Return a string with the bot_response or a tuple of (bot_response: str, new_state: dict)
    """

    if state is None or "counter" not in state:
        state = {"counter": 0}
    else:
        state["counter"] += 1
        
    # bart
    user_message = message_history[-1].content
    if user_message=="hi":
        bot_response="Hello!I give real analysis of Industry Market"
    else:    
        bot_response =tqa(table=table,query=user_message)["answer"]

    # query = "I am having chills?Dr. is there any disease happened to me"

    return bot_response, state