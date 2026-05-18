from django.http import JsonResponse
import random

def joke_api(request):

    jokes = [

        {
            "setup": "Why do programmers prefer dark mode?",
            "punchline": "Because light attracts bugs."
        },

        {
            "setup": "Why did the computer go to the doctor?",
            "punchline": "Because it caught a virus."
        },

        {
            "setup": "Why was the computer cold?",
            "punchline": "Because it forgot to close Windows."
        },

        {
            "setup": "Why did Python live on land?",
            "punchline": "Because it was above C-level."
        }

    ]

    joke = random.choice(jokes)

    return JsonResponse(joke)