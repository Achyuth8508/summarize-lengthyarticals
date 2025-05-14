from transformers import pipeline

summarize=pipeline("summmarization")


text="""The Hugging Face library has revolutionized the field of natural language processing with its transformers library.
This library provides state-of-the-art models for various NLP tasks including text summarization, text classification, question answering, and more. 
With easy-to-use APIs and pre-trained models, developers can quickly integrate advanced NLP capabilities into their applications. 
The community-driven approach ensures continuous improvement and innovation in the library, making it a valuable resource for both researchers and practitioners."""

summary=summarize(text,max_length=100,min_length=10,do_sample=False)

print('Original size of Text:',len(text))

print (summary[0]['summary_text'])

print('Summarized size of Text:',len(summary))
