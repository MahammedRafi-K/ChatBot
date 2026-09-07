import gradio as gr
from google import genai
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)
def model(msg, history):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=msg
        )
        return response.text
    except Exception as e:
        return f"Error: {e}"
demo = gr.ChatInterface(
    fn=model,
    title="Study Vision",
    description="Get your doubts clarified here!"
)
demo.launch(
    server_name="0.0.0.0",
    server_port=int(os.environ.get("PORT", 7860))
)