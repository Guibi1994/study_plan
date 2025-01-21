import requests


def get_joke_data(word: str) -> dict:
    params = {"term": word, "limit": 2}
    headers = {"Accept": "application/json"}
    jokes = requests.get(
        "https://icanhazdadjoke.com/search", params=params, headers=headers
    )
    print(jokes)
    jokes = jokes.json()
    return jokes
    # return {"results": [x["joke"] for x in jokes["results"]]}


result = get_joke_data("magic")

type(result)
len(result["results"])
