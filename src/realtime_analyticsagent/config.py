import os
from dotenv import load_dotenv


load_dotenv()

MistralAI_API_KEY = os.getenv("MISTRAL_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
API_URL = os.getenv("REALTIME_ANALYTICS_API_URL")


def validate_config():

    missing = []


    if not MistralAI_API_KEY:
        missing.append("MistralAI_API_KEY")

    if not TAVILY_API_KEY:
        missing.append("TAVILY_API_KEY")

    if not API_URL:
        missing.append("API_URL")

    
    if missing:
        raise RuntimeError(f"Missing required configuration: {', '.join(missing)}")



if __name__ == "__main__":
    
    print("MistralAI_API_KEY:", MistralAI_API_KEY)
    print("TAVILY_API_KEY:", TAVILY_API_KEY)
    print("API_URL:", API_URL)

