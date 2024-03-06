## Effectiveness

Effectiveness for LLMs comes down to how well did the LLM complete the desired task.  For example, if you asked an LLM to summarize a video meeting, is the result a short an accurate summary of what was discussed?  Is it too long to be considered a summary?  

In the article, "The art of prompting: how to win", by Keerti Hariharan, the author states, "If you are using an LLM, prompting is at the heart of making it effective. Your prompt provides a roadmap for the model to generate meaningful responses."

Here are some of the most common prompting techniques to improve LLM effectiveness:

__few-shot__ -- provide a prompt that has a few exact examples of what to do and then prompt the LLM to complete the task.  
__act as if__ -- instruct the LLM to repond by acting as if the LLM was a specific role or person like a lawyer, politician, or third-grade science teacher.  
__task and steps__ -- instruct the LLM what specific task you wish it to perform and then provide steps for how the AI might reason out the solution.  
__chain of thought__ -- provde the LLM with similar prompts and related examples of how the LLM might work though the problem, therefore helping the AI see how to reason the answer out by following the chain of thought.  
__tree of thought__ -- start the prompt with a base thought related to a task and then expand upwards with major topics (branches) and sub-topics (leaves) that fill out the prompt.  
__examples__ -- present several examples of what the LLM could provide as a response and then prompt the LLM for an additional or related response.

The code example in src/effectiveness.py uses the chain of thought approach to prompting with OpenAI/GPT-4.  Use the following commands to run the example. You only need to run the install command the first time. Python 3.10 is required.

```
pipenv install
pipenv run python src/effectiveness.py
```

This example uses the chain of thought approach for prompting Open AI/GPT-4 to do simple math.

```
Prompt:
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

Content: Joe started with 1 can and bought 2 six-packs with 6 bottles each. 1 + 2 * 6 = 13.
The answer is 13.
```

## Resources

[The art of prompting: how to win -- Alkymi](https://www.alkymi.io/resources/blog/the-art-of-prompting-how-to-win-conversations-and-influence-llms)  
[Prompt engineering: A guide to improving LLM performance -- circleci](https://circleci.com/blog/prompt-engineering/)  
[Chatbot Arena](https://lmsys.org/blog/2023-12-07-leaderboard/)  