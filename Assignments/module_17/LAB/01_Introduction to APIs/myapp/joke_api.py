import requests

# API URL for random joke
url = "https://official-joke-api.appspot.com/random_joke"

try:
    # Send GET request
    response = requests.get(url)

    # Convert response to JSON
    joke = response.json()

    # Display joke
    print("\n😂 Random Joke:\n")
    print(joke["setup"])
    print(joke["punchline"])

except Exception as e:
    print("Error fetching joke:", e)