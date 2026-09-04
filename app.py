import gradio as gr
from google import genai
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)
def model(msg,history):
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=msg
    )
    return response.text
demo = gr.ChatInterface(
    fn=model,
    title="Study Vision",
    description="Get your doubts clarified here!"
)
demo.launch()