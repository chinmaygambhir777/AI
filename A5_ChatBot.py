from nltk.chat.util import Chat, reflections

# Pattern-Response Pairs
pairs = [

    [
        r"hi|hello|hey",
        ["Hello! Welcome to Customer Support Chatbot."]
    ],

    [
        r".*order.*status.*",
        ["Your order is currently being processed."]
    ],

    [
        r".*payment.*issue.*",
        ["Please check your internet connection or try another payment method."]
    ],

    [
        r".*delivery.*",
        ["Your product will be delivered within 3-5 business days."]
    ],

    [
        r".*return.*policy.*",
        ["Products can be returned within 7 days after delivery."]
    ],

    [
        r".*cancel.*order.*",
        ["Your order cancellation request has been submitted."]
    ],

    [
        r".*thank you.*",
        ["You're welcome! Happy to help you."]
    ],

    [
        r".*quit.*",
        ["Thank you for using Customer Support Chatbot."]
    ],

    [
        r".*",
        ["Sorry, I could not understand your query."]
    ]
]

# Create Chatbot Object
chatbot = Chat(pairs, reflections)

# Start Chatbot
print("===== Customer Support Chatbot =====")
print("Type 'quit' to exit.\n")

chatbot.converse()
