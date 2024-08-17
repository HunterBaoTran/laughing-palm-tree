import os
import serpapi

from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('SERPAPI_KEY')
clinet = serpapi.Client(api_key=api_key)

result = clinet.search(
    q="IQ Viet My",
    engine = "google",
    hl = 'en',
    api_key = os.getenv('SERPAPI_KEY'),
    gl = "us",
)

print(result)