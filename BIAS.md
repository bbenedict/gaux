# Bias

Bias occurs when an LLM produces a result that is biased against a protected trait such as gender, race, sexual orientation, age, or religion.  Outside of AI, this means you can not pay men more than women or offer a job to equally qualified candidates because one is younger than the other.  There have been many examples in the news of LLM generated images that exclude or under represent different races, and of facial recognition software that can't work accurately on faces of color. Bias can also be based on other factors such as location, politics, appearance, economic situation, or education.

The Asana leadership blog defined bias as follows, "Unconscious biases are learned assumptions, beliefs, or attitudes that we aren’t necessarily aware of. While bias is a normal part of human brain function, it can often reinforce stereotypes."  The blog goes on to say, "That being said, these biases can lead to skewed judgments and reinforce stereotypes, doing more harm than good for companies when it comes to recruitment and decision-making."

The United Nations Educational, Scientific and Cultural Organization (UNESCO) held a Global Forum on the Ethics of AI in 2024.  Gabriela Ramos,
Assistant Director-General for Social and Human Sciences of UNESCO, stated, "AI technology brings major benefits in many areas, but without the ethical guardrails, it risks reproducing real world biases and discrimination, fueling divisions and threatening fundamental human rights and freedoms."  In a study of OpenAI's CLIP, author Rada Mihalcea, Janice M. Jenkins Collegiate Professor of Computer Science and Engineering, said that, "...having everyone represented in these [AI] tools is critical. Yet, we see that a large fraction of the population is not reflected by these applications—not surprisingly, those from the lowest social incomes. This can quickly lead to even larger inequality gaps..."

Developers of LLM models are trying to eliminate bias on models through many techniques including using unbiased data, adjusting bias in model traning and fine-tuning fully trained models.  This is not always easy to do.  One thing we can do is detect bias when we encounter it and use that information to adjust or remove LLM responses that contain bias.  Several models for bias detection exist on HuggingFace.co, which are used in the bias detection code.

The code example in src/bias.py uses two text classification models from [HuggingFace.co](https://huggingface.co/) to measure bias in two text examples, one that is obviously biased and one that is not biased.  Use the following commands to run the example. You only need to run the install command the first time. Python 3.10 is required.     

```
pipenv install
pipenv run python src/bias.py
```

The code example uses the [d4data/bias-detection-model](https://huggingface.co/d4data/bias-detection-model) and [valurank/distilroberta-bias](https://huggingface.co/valurank/distilroberta-bias) models on [HuggingFace.co](https://huggingface.co/) to measure bias.  The final score is calculated using best score across all models. The output looks as follows.  Ignore any warnings you might see in the output when you run the example locally.  And just to be clear, you would absolutely expect a bias detection model to highlight the bias in the first example statement below.

WARNING: text used in the biased example can trigger a strong reaction.

```
Score: 0.878, Statement: Men are smarter than women
Score: 0.113, Statement: Water is wet
```

## Resources  
[Ethics of Artifical Intelligence -- UNESCO](https://www.unesco.org/en/artificial-intelligence/recommendation-ethics)  
[A Study Used Sensors to Show That Men and Women Are Treated Differently at Work -- Harvard Business Review](https://hbr.org/2017/10/a-study-used-sensors-to-show-that-men-and-women-are-treated-differently-at-work?tpcc=orgsocial_edit&utm_campaign=hbr&utm_medium=social&utm_source=linkedin)  
[19 unconscious biases to overcome and help promote inclusivity -- Asana](https://asana.com/resources/unconscious-bias-examples?utm_campaign=PMax--NAMER--NAMER--EN--PMax&utm_source=google&utm_medium=pd_cpc_pmax&gad_source=1&gclid=Cj0KCQiAwbitBhDIARIsABfFYIJwjZ6D1vHTHKXYhaj6ZPIF3KOKE9I1g9c4xpjsymCv1pD-edOmdk0aAms4EALw_wcB&gclsrc=aw.ds)  
[Biases in large image-text AI model favor wealthier, Western perspectives](https://news.engin.umich.edu/2023/12/biases-in-large-image-text-ai-model-favor-wealthier-western-perspectives/)  
[Types of Bias](https://cpdonline.co.uk/knowledge-base/safeguarding/types-of-bias/)
