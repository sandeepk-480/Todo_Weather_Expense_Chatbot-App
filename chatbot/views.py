from django.shortcuts import render
import spacy
from chatbot.models import ChatMessage
from django.shortcuts import redirect
from django.urls import reverse


# Loading Spacy
nlp = spacy.load('en_core_web_sm')

# Intents
intents = {
    "greet": ["hello", "hi", "hey"],
    "weather": ["weather", "forecast"],
    "goodbye": ["bye", "goodbye", "see you"],
    "thanks": ["thanks", "thank you"],
    "joke": ["joke", "tell me a joke"],
    "time": ["time", "current time"],
    "help": ["help", "assistance"],
    "name": ["your name", "who are you", "name"],
    "fun_fact": ["fun fact", "interesting fact", "fact"],
    "music_recommendation": ["music", "recommend me music"],
}

# Responses
responses = {
    "greet": "Hello! How can I help you today?",
    "weather": "The weather is currently sunny.",
    "goodbye": "Goodbye! Have a great day!",
    "thanks": "You're welcome! If you have more questions, feel free to ask.",
    "joke": "Why don't scientists trust atoms? Because they make up everything!",
    "time": "I don't have real-time capabilities, but your device should display the current time.",
    "help": "Sure, I'm here to help! What do you need assistance with?",
    "name": "I'm a chatbot here to assist you. You can call me Chatty!",
    "fun_fact": "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!",
    "music_recommendation": '''Here are some recommendations, 
    Artist: Vampire Weekend,
    Album: "Modern Vampires of the City" ''',
}


def chatbotView(request):
    previous_interactions = list(ChatMessage.objects.values()[::-1])

    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        doc = nlp(user_input)

        # Determining Intent
        # for intent, keywords in intents.items():
        #     if any(token.text.lower() in keywords for token in doc):
        #         detected_intent = intent
        #         break
        #     else:
        #         detected_intent = None

        for intent, keywords in intents.items():

            detected_intent = None
            for token in doc:
                if token.text.lower() in keywords:
                    detected_intent = intent
                    break
            else:
                detected_intent = None
                
            if detected_intent:
                break
        
        # Generate response
        if detected_intent:
            bot_response = responses.get(detected_intent, "I'm not sure how to respond to that.")
        else:
            bot_response = "I'm sorry, I didn't understand your request."
        
        # chat_message = {'user_input': user_input, 'bot_response': bot_response}
        chat_message = ChatMessage(user_input=user_input, bot_response=bot_response)
        chat_message.save()

        # Query previous interactions
        previous_interactions = list(ChatMessage.objects.values()[::-1])

        return render(request, 'chatbot/chatbot.html', {'chat_message':chat_message, 'previous_interactions': previous_interactions})

    return render(request, 'chatbot/chatbot.html', {'previous_interactions': previous_interactions})


def del_chat(request, pk):
    data = ChatMessage.objects.get(id=pk)
    data.delete()
    return redirect(reverse('chatbot'))