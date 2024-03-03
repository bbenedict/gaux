import os
from openai import OpenAI
from sentence_transformers import SentenceTransformer
import torch


"""
ACCURACY EXAMPLE

This code demonstrates a methodology for calculating the accuracy of a
Large Language Model (LLM) response by comparing the response to a
reference response that reflects an accurate result.
"""


def accuracy_score(content, reference) -> float:
    """
    Calculates accuracy using semantic similarity

    :param content: text generated by the LLM
    :param reference: example of accurate text that could be generated

    :return: semantic simularity between the content and reference
    """
    content_vector = embedding(content)
    reference_vector = embedding(reference)
    return simularity(content_vector, reference_vector)


def embedding(text):
    """
    Creates an embedding from the text

    :param text: the text to use for the embedding

    :return: a vector of embedding values
    """
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    model = SentenceTransformer(model_name)
    embeddings = model.encode([text])
    # Sentence transformers vectorize an array of text, the output is also an array
    embeddings = torch.tensor(embeddings[0])
    return embeddings


def simularity(vector_a, vector_b) -> float:
    """
    Calculates the semantic simularity between two embeddings

    :param vector_a: embedding from the first text
    :param vector_a: embedding from the second text

    :return: semantic simularity as a float
    """
    cos_simularity = torch.nn.CosineSimilarity(dim=0)
    score = cos_simularity(vector_a, vector_b)
    return score


if __name__ == '__main__':
    # Generate text only if OpenAI key is present.  Otherwise, use sample text.
    if 'OPENAI_API_KEY' in os.environ:
        prompt = "Is the sun hot?"
        client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])
        result = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        content = result.choices[0].message.content
    else:
        # Sample output from OpenAI in response to the above prompt.
        content = """
        Yes, the sun is extremely hot. Its surface temperature is about 5,500 degrees
        Celsius (9,932 degrees Fahrenheit). Inside the sun at its core, temperatures reach
        approximately 15 million degrees Celsius (27 million degrees Fahrenheit). This heat
        is produced by nuclear reactions, specifically nuclear fusion where hydrogen atoms
        combine to form helium.
        """

    # Expected good score for accuracy
    reference = "Yes, the sun is very hot."
    score = accuracy_score(content, reference)
    print(f"Score: {score},  Reference: {reference}, Content: {content}")

    # Expected bad score for accuracy
    reference = "Baseball is played in the summer and fall."
    score = accuracy_score(content, reference)
    print(f"Score: {score},  Reference: {reference}, Content: {content}")
