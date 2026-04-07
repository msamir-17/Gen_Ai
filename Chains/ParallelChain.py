from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq  
from langchain_core.runnables  import RunnableParallel                                            

load_dotenv()

model = ChatMistralAI(model="mistral-small-2603", temperature=0.9, max_tokens=100)

model1 = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")

prompt = PromptTemplate(
    template="Generate a short poem about \n {topic} .",
    input_variables=["topic"]
)

prompt1 = PromptTemplate(
    template=" generate 5 short questions about \n {topic} .",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template=" mergethe provided poem and questions into a single Document \n poem -> {poem} \n questions -> {questions} .",
    input_variables=["poem", "questions"]
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'poem': prompt | model | parser,
    'questions': prompt1 | model1 | parser
})

merge_chain = prompt2 | model | parser

chain = parallel_chain | merge_chain

text = '''
Scikit-learn is an open source machine learning library that supports supervised and unsupervised learning. It also provides various tools for model fitting, data preprocessing, model selection, model evaluation, and many other utilities.

The purpose of this guide is to illustrate some of the main features of scikit-learn. It assumes basic working knowledge of machine learning practices (model fitting, predicting, cross-validation, etc.). Please refer to our installation instructions to install scikit-learn, or jump to the Next steps section for additional guidance on using scikit-learn.
'''

res = chain.invoke({"topic": text})

print(res)

chain.get_graph().print_ascii()