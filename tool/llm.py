from dotenv import load_dotenv
import os
from langchain.chat_models import init_chat_model
from langchain.chat_models.base import BaseChatModel



def get_llm() -> BaseChatModel:
    """This medthod gets the llm."""
    load_dotenv()
    llm= init_chat_model(
        model= os.getenv('MODEL_ID'),
        model_provider= os.getenv('MODEL_PROVIDER'))
    
    return llm