import logging
from google.generativeai import GenerativeModel, configure
from src.config import get_api_key
from src.image_processor import load_image
from src.prompts import get_disease_diagnosis_prompt

def diagnose_plant_disease(image_path: str) -> str:
    # Setup Gemini API
    api_key = get_api_key()
    configure(api_key=api_key)
    model = GenerativeModel("gemini-2.5-flash")

    # Load image and prompt
    image = load_image(image_path)
    prompt = get_disease_diagnosis_prompt()

    # Query the model
    response = model.generate_content([prompt, image])
    return response.text

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        result = diagnose_plant_disease("data/image-1.jpg")
        logging.info(f"Diagnosis result:\n{result}")
    except Exception as e:
        logging.error(f"Error during diagnosis: {e}")
