# Performance

Performance with Generative AI is variable depending on the task defined by the prompt.  An LLM might be providing a simple answer to a prompt or it might be writing a statement of purpose for a college application.  By comparison, web pages are expected to render in just a few seconds if that.  The most important aspect of performance is the expected performance or target duration.

User experience or observed performance are the driving factors behind LLM streaming.  Streaming enables an LLM to quickly return the first few words of a response and then continue to stream the rest of the response in small chunks.  It provides the appearance of better performance through quick feedback to the user, often referred to as the time to first token (TTFT).  From the article, "Understanding performance benchmarks for LLM inference", auther Philip Kiely states, "Human visual reaction time averages around 200 milliseconds, so getting your time to first token below this threshold makes chat-type applications feel snappy and responsive."  For streaming, you can also look at time between tokens known as inter-token latency (ITL).  

Another important aspect of LLM performance is throughput including throughput versus number of tokens. For web applications, this is more commonly known as scalability as verified by performance testing.  Testing tools such as Apache Bench enable you to spin up many users simultaneously executing the same test over and over again. And of course, testing against different GPUs or service levels will lead to different results.

The code example in src/performance.py uses the timer-score library to test the performance of OpenAI. Use the following commands to run the example. You only need to run the install command the first time. Python 3.10 is required.

```
pipenv install
pipenv run python src/performance.py
```

This example tests the performance Open AI/GPT-4 using a question about the sun, reporting on time to first token and the total completion time.  A performance score is generated using the timer_score library which produces a score from 0 to 1 for execution against a target duration.  The target for time to first token is 0.5 seconds.  The target for total completion is 5 seconds.

```
First token -- score: 0.41 target: 0.5 duration: 0.68
Completion -- score: 0.33 target: 5 duration: 5.72
Content: The sun is hot because of the nuclear fusion that takes place within...
```

## Resources

[How page speed affects Web User Experience -- uxplanet](https://uxplanet.org/how-page-speed-affects-web-user-experience-83b6d6b1d7d7)  
[Understanding performance benchmarks for LLM inference -- baseten](https://www.baseten.co/blog/understanding-performance-benchmarks-for-llm-inference/)  
[Reproducible Performance Metrics for LLM inference](https://www.anyscale.com/blog/reproducible-performance-metrics-for-llm-inference)  
[Apache Bench](https://httpd.apache.org/docs/2.4/programs/ab.html)
