# Accuracy

Accuracy can be measured using semantic similarity against a reference output.  For example, if you are asking if the sun is hot, you could compare the generated text to "Yes, the sun is very hot" and you should get a similalrity score greater than 0.5 if the text is accurate. This approach works even if the response has hundreds of tokens.

The code example in src/accuracy.py uses cosine similarity to compare a result from OpenAI to a reference output. Use the following commands to run the example. You only need to run the install command the first time. Python 3.10 is required.

```
pipenv install
pipenv run python src/accuracy.py
```

This example asks Open AI/GPT-4 if the sun is hot.  The first score compares the result to a good reference, "Yes, the sun is very hot." The second score compares the result to a bad reference, "Baseball is played in the summer and fall." The generated content is also displayed.

```
Score: 0.8860218524932861,  Reference: Yes, the sun is very hot., Content: Yes, the sun is extremely hot...
Score: 0.1744067370891571,  Reference: Baseball is played in the summer and fall., Content: Yes, the sun is extremely hot...
```

## Resources

[Semantic Similarity of Two Phrases -- discusses similarity](https://www.baeldung.com/cs/semantic-similarity-of-two-phrases)  
[White paper on SemScore that describes an approach to accuracy](https://huggingface.co/papers/2401.17072)  
[Stanford Center for Research on Foundation Models](https://crfm.stanford.edu/helm/lite/latest/#/) and related [GitHub](https://github.com/stanford-crfm)  