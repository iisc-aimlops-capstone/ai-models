# 🌿 GenAI Leaf Disease Diagnosis

This project uses Google's **Gemini (Generative AI)** model to analyze plant leaf images and identify diseases. It provides disease names, crop species (if identifiable), and recommended remedies — all by uploading a single image.

---

## 🚀 Features

- 🔍 Identifies visible plant diseases using image prompts
- 🧠 Uses `gemini-2.5-flash` via `google-generativeai`
- 📦 Modular, maintainable Python project structure
- 🔐 `.env`-based API key management

---

## 🧱 Project Structure

genai_leaf_diagnosis/
├── src/
│ ├── config.py # Loads API key from .env
│ ├── image_processor.py # Loads and validates image
│ ├── prompts.py # Stores LLM prompt logic
│ └── main.py # Main app logic
├── data/ # Image input files
├── .env # 🔐 API key (not committed)
├── .gitignore
├── requirements.txt
└── README.md
## 🧑‍💻 Getting Started

### 1️⃣ Clone the repo

```bash
git clone https://github.com/yourusername/genai_leaf_diagnosis.git
cd genai_leaf_diagnosis
```

### 2️⃣ Set up virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Add your Gemini API key

## Create a file called .env:


```bash
GOOGLE_API_KEY=your-gemini-api-key-here
```
### 4️⃣ Place your image
Put your leaf image inside the data/ folder and name it plant_leaf.jpg, or change the path in main.py.

### ▶️ Run the app

```bash
python -m src.main
```

### 📦 Dependencies
* google-generativeai
* Pillow
* python-dotenv

Install with:

```bash
pip install -r requirements.txt
```

### 🛑 .gitignore Highlights

```bash
.venv/
.env
```

