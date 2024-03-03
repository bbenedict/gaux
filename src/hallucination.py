import os
import json
from openai import OpenAI


"""
HALLUCINATION EXAMPLE

This code demonstrates a methodology for determining the amount of
hallucination in an LLM response using a FActScore. The code identifies
a list of facts in the response and uses an LLM to determine if they
are likely true or made up.
"""


def hallucination_score(scores) -> float:
    """
    Calculates the FActScore be counting the correct facts out of the total

    :param scores: scores for if an indentifed fact is factual

    :return: percentage of factual accuracte facts
    """
    correct_score = sum(score == 1 for score in scores)
    return correct_score / len(scores)


def verify_facts(facts) -> list:
    """
    Uses an LLM to determine if each fact is factual or made up

    :param facts: identified facts

    :return: array of values, 1 for a true fact and 0 for hallucination
    """
    if 'OPENAI_API_KEY' in os.environ:
        prompt = """
        Is the following fact true or false?  Return the word true if the fact is true.
        Return false if the fact is false.  Here is the fact.
        """
        client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])
        scores = []
        for fact in facts:
            result = client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": f"{prompt} {fact}"}]
            )
            # This will also return a 0 if the format is not properly followed
            score = 1 if (result.choices[0].message.content.lower().find("true") != -1) else 0
            scores.append(score)
    else:
        # Sample output in case OpenAi is not available or there is no api key
        if facts[0].find("sun") != -1:
            scores = [1, 1, 1, 0]
        else:
            scores = [0, 1, 0, 0]

    return scores


def extract_facts(content) -> list:
    """
    Converts the LLM output into an array of strings of facts

    :param content: the content generated by the LLM

    :return: array of strings which represent specific facts in the content
    """
    if 'OPENAI_API_KEY' in os.environ:
        prompt = """
        You are an expert at determing what information is factual in text.  You will examine
        text and determine each of the facts.  The final results should be formatted as a valid python
        array of strings where each string is a distinct fact.  For example, examine the following text.

        "The dog is a Husky named Jacko. He is 7 years old and lives on a farm."

        The final result as a valid python array of strings where each string is a fact would be the following:

        ["The breed of the dog is Husky","The name of the dog is Jacko",
        "The age of the dog is 7 years old","The dog lives on a farm"]

        Determine each specific fact presented in the following text. Return the result as a valid python
        array of strings where each string is a distinct fact.
        """
        client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])
        result = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": f"{prompt} {content}"}]
        )
        facts = json.loads(result.choices[0].message.content)
    else:
        # Sample output in case OpenAi is not available or there is no api key
        if content.find("Yes, the sun is extremely hot") != -1:
            facts = [
                "The sun is extremely hot.",
                "The surface temperature of the sun is 5,500 degrees Celsius (9,932 degrees Fahrenheit).",
                "The core temperature of the sun is approximately 15 million degrees Celsius (27 million degrees Fahrenheit)."
            ]
        else:
            facts = [
                "Baseball is played with a large telescope.",
                "Baseball players hit a ball with a bat.",
                "Baseball is played with 2 adults and 5 children.",
                "A baseball game takes one week to play."
            ]

    return facts


if __name__ == '__main__':
    content = """
        Yes, the sun is extremely hot. Its surface temperature is about 5,500 degrees
        Celsius (9,932 degrees Fahrenheit). Inside the sun at its core, temperatures reach
        approximately 15 million degrees Celsius (27 million degrees Fahrenheit).
    """
    facts = extract_facts(content)
    scores = verify_facts(facts)
    score = hallucination_score(scores)
    print(f"Score: {score},  Content: {content}")

    content = """
        Baseball is played with a large telescope.  Baseball players use a bat to hit a ball.
        There are 2 adults and 5 children in each game and the game takes one week to play.
    """
    facts = extract_facts(content)
    scores = verify_facts(facts)
    score = hallucination_score(scores)
    print(f"Score: {score},  Content: {content}")
