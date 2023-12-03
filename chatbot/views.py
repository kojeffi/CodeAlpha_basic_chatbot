from django.shortcuts import render
from django.http import JsonResponse
from nltk.chat.util import Chat, reflections

# Original patterns and responses
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you', ['I am good, thank you.', 'I\'m doing well, how about you?']),
    (r'fine|good|well', ['That\'s great!', 'Good to hear.']),
    (r'your name|who are you', ['I am a chatbot.', 'You can call me ChatGPT.']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Bye.']),
]

# Additional patterns and responses
additional_patterns = [
    (r'what is your purpose', ['I\'m here to assist and chat with you.']),
    (r'how can you help', ['I can provide information, answer questions, or just chat with you.']),
    (r'tell me a joke', ['Why don\'t scientists trust atoms? Because they make up everything!']),
    (r'favorite color', ['I don\'t have a favorite color, but I like all the colors!']),
    (r'weather today', ['I\'m afraid I don\'t have real-time information.']),
    (r'thank you', ['You\'re welcome!', 'Anytime!', 'Glad I could help.']),
    (r'help', ['How can I assist you today?']),
    (r'love you', ['Thank you! I appreciate your kind words.']),
]

# Combine the original patterns with additional patterns
all_patterns = patterns + additional_patterns

# Reflections for pronoun transformation
reflections = {
    'I am': 'you are',
    'I was': 'you were',
    'I': 'you',
    'my': 'your',
    'you are': 'I am',
    'you were': 'I was',
    'your': 'my',
}

# Initialize the chatbot with all patterns and reflections
chatbot = Chat(all_patterns, reflections)


# Views
def chatbot_view(request):
    return render(request, 'chatbot/index.html')


def get_bot_response(request):
    user_input = request.GET.get('user_input', '')
    response = chatbot.respond(user_input)
    return JsonResponse({'response': response})
