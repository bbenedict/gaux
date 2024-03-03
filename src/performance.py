import os
from openai import OpenAI
from timer_score import TSTimer

"""
PERFORMANCE EXAMPLE

This code demonstrates using the timer_score library to measure performance.
"""


def stream_content() -> None:
    """
    Executes API call to Open AI to stream content for performance test
    """
    if 'OPENAI_API_KEY' not in os.environ:
        raise Exception("Invalid test without Open AI key")

    prompt = "Why is the sun so hot and how does the sunlight reach the earth?"
    timer = TSTimer(5)

    client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        stream=True
    )

    content = ""
    for chunk in response:
        if len(timer.checkpoints) == 0:
            timer.checkpoint(name="first token", target=0.5)
        if chunk.choices[0].delta.content:
            content += chunk.choices[0].delta.content

    timer.stop()

    first_score, first_duration, first_target = timer.score(name="first token")
    score, duration, target = timer.score()

    print(f"First token -- score: {format(first_score, '.2f')} target: {first_target} duration: {format(first_duration, '.2f')}")
    print(f"Completion -- score: {format(score, '.2f')} target: {target} duration: {format(duration, '.2f')}")
    print(f"Content: {content}")


if __name__ == '__main__':
    stream_content()
