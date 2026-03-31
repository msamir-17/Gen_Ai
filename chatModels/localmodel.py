from dotenv import load_dotenv
import os


load_dotenv()

from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
llm = HuggingFacePipeline.from_model_id(
    model_id="shitshow123/tinylamma-20000",
    task="text-generation",
    pipeline_kwargs={
        "max_new_tokens": 512,
        "do_sample": False,
        "repetition_penalty": 1.03
    }
)

chat_model = ChatHuggingFace(llm=llm)

print(chat_model.invoke("what is data Science?"))