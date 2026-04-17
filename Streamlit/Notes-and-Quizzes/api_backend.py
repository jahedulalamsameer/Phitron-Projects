import os, io
from google import genai
from gtts import gTTS
from dotenv import load_dotenv

load_dotenv()
my_api_key = os.getenv("GEMMA_API_KEY")
api_client = genai.Client(api_key=my_api_key)

def note_generator(images):
    prompt = """Summarise the pictures in note format within 150 words in the given language. Add necessary markdowns (use subheader instead of header) to the notes."""
    response = api_client.models.generate_content(model="gemma-4-26b-a4b-it",contents=[images,prompt])

    return response.text 


def audio_trancriber(response):
    note = gTTS(response,slow=False)
    audio_buffer = io.BytesIO()
    note.write_to_fp(audio_buffer)
    return audio_buffer

def quiz_generator(images,notes,level):
    prompt = f"""Generate quizzes based on the pictures and its notes '{notes}' given the difficulty level {level} in the given language. Add necessary markdowns (use subheader instead of header) to the quizzes. Show all answers together in the very last after all the questions, inside a different subheader named 'Answer Key', no matter what the difficulty level is."""
    response = api_client.models.generate_content(model="gemma-4-26b-a4b-it",contents=[images,prompt])
    return response.text
