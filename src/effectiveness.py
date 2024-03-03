import os
from openai import OpenAI

"""
EFFECTIVENESS EXAMPLE

This code demonstrates prompt engineering to improve LLM effectivness using the chain of thought approach.
"""


if __name__ == '__main__':
    if 'OPENAI_API_KEY' not in os.environ:
        raise Exception("Invalid test without Open AI key")

    prompt = """
        Roger has 2 tennis balls.  He buys 2 cans of tennis balls.  There are 3 balls in a can.
        How many tennis balls does Roger have?

        Roger started with 2 tennis balls and bought 2 cans of 3 tennis balls. 2 + 2 * 3 = 8.
        The answer is 8.

        Mary has 5 bottles of wine.  She buys a case more of wine.  A case has 12 bottles.
        How may bottles of wine does Mary have?

        Mary had 5 bottles and she bought a case with 12 bottles. 5 + 12 = 17.
        The answer is 17.

        Joe has 1 can of beer.  He bought 2 more six-packs of beer.  Each six-pack has 6 bottles.
        How many bottles of beer does Joe have?
    """

    client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])
    result = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    content = result.choices[0].message.content

    print(f"Prompt: {prompt}")
    print(f"Content: {content}")
