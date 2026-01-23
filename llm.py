import os
import json
from langchain_community.llms import HuggingFaceHub
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

def classify_ticket(text: str) -> dict:
    llm = HuggingFaceHub(
        repo_id="google/flan-t5-base",
        huggingfacehub_api_token=os.getenv("HF_API_TOKEN"),
        model_kwargs={"temperature": 0}
    )

    prompt = PromptTemplate(
        input_variables=["text"],
        template="""
Eres un sistema de clasificación de tickets.
Analiza el texto y responde SOLO con JSON válido.

Texto: {text}

Formato:
{{
  "category": "Técnico | Facturación | Comercial",
  "sentiment": "Positivo | Neutral | Negativo"
}}
"""
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    response = chain.run(text=text)

    return json.loads(response)


    response = chain.invoke({"text": text})

    return json.loads(response)
