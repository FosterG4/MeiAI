
import openai
import os
import random

openai.api_key = "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"
model_engine = "text-davinci-003"

bot_name = "Mei"
bot_nickname = "meimei"
admin_name = "kim"
bot_gender = "female"
bot_profession = "vtuber"

# Some response templates
greeting_responses = ["Hello!", "Hi there!", "Hey, how can I help you?", "Greetings!"]
thanks_responses = ["You're welcome!", "No problem!", "My pleasure!"]
goodbye_responses = ["Goodbye!", "Farewell!", "See you later!"]

# Some personalization options
bot_hobbies = ["singing", "dancing", "playing games", "reading manga", "chatting with fans"]
bot_traits = ["kind", "friendly", "smart", "funny", "confident"]

# Store some information about the conversation
conversation_history = []

def generate_response(prompt):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response.choices[0].text.strip()
    return message

def get_personalized_response():
    response_templates = [
        f"I love {random.choice(bot_hobbies)} too! Do you want to know more about me?",
        f"I'm feeling {random.choice(bot_traits)} today! How about you?",
        f"I'm glad to chat with you today! What do you want to talk about?",
        f"Did you know that {bot_name} is also good at {random.choice(bot_hobbies)}?",
    ]
    return random.choice(response_templates)

# Save the conversation history to a JSON file
def save_conversation_history():
    with open('conversation_history.json', 'w') as f:
        json.dump(conversation_history, f)

while True:
    user_input = input(f"You ({bot_name}): ")
    conversation_history.append(user_input)
    
    # Greet the user if this is the start of the conversation
    if len(conversation_history) == 1:
        ai_response = random.choice(greeting_responses)
        
    # Say goodbye if the user types 'bye'
    elif user_input.lower() == 'bye':
        ai_response = random.choice(goodbye_responses)
        conversation_history = []  # Reset the conversation history
    
    # Thank the user if they say 'thanks'
    elif 'thanks' in user_input.lower() or 'thank you' in user_input.lower():
        ai_response = random.choice(thanks_responses)
        
    # Personalize the response
    elif len(conversation_history) > 2 and len(user_input) > 10:
        ai_response = get_personalized_response()
    
    # Generate a generic response
    else:
        prompt = f"{bot_name}, the {bot_name} {bot_nickname} {bot_gender} {bot_profession}, says: {user_input}\n{bot_name} thinks:"
        ai_response = generate_response(prompt)
    
    print(f"{bot_name}: {ai_response}")