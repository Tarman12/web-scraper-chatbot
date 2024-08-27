import openai
import requests
from bs4 import BeautifulSoup


openai.api_key = 'your_api_key_here'


def fetch_website_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.get_text(separator='\n')  
    else:
        return None

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150
    )
    return response.choices[0].message['content']


def run_chatbot():
    url = input("Enter the website URL: ")
    website_content = fetch_website_content(url)
    
    if not website_content:
        print("Failed to fetch website content. Please check the URL and try again.")
        return
    
    print("\nChatbot is ready! You can start asking questions.\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot session ended.")
            break
    
        prompt = f"Here is some content from the website: {website_content[:2000]}.\n\nUser's question: {user_input}\n\nAnswer based on the website content:"
        
       
        response = chat_with_gpt(prompt)
        print(f"Chatbot: {response}\n")

if __name__ == "__main__":
    run_chatbot()