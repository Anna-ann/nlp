import spacy
import sqlite3
from langdetect import detect

# Load the English language model
nlp_en = spacy.load("en_core_web_sm")

# Load the Russian language model
nlp_ru = spacy.load("ru_core_news_md")

def preprocess_text(file_path):
    # Read the content of the file
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
    return text

def identify_language(text):
    # Detect the language of the text
    try:
        language = detect(text)
        return language
    except:
        # Return a default language if detection fails
        return "en"  # Assuming English by default

def identify_precedent_phenomena(text):
    # Identify the language
    language = identify_language(text)

    # Choose the appropriate language model
    if language == "ru":
        language_model = nlp_ru
    else:
        language_model = nlp_en

    # Connect to the database
    conn = sqlite3.connect('selected_precedents.db')
    cursor = conn.cursor()

    # Create a list to store identified precedent phenomena
    identified_phenomena = []

    # Tokenize and process the input text
    doc = language_model(text)

    # Extract named entities using spaCy's named entity recognition (NER)
    named_entities = [ent.text for ent in doc.ents]

    # Combine named entities and individual tokens
    tokens = named_entities + [token.text for token in doc]

    # Iterate through each token in the processed text
    for token in tokens:
        # Check if the token is a precedent phenomenon
        cursor.execute("SELECT * FROM precedent_phenomena WHERE name = ?;", (token,))
        result = cursor.fetchone()

        if result:
            identified_phenomena.append({
                'name': result[0],
                'cultural_meaning': result[1],
                'recognition_level': result[2],
                'interpretation': result[3],
                'symbolic_meaning': result[4],
                'associated_event': result[5],
                'adaptable_usage': result[6],
                'semantic_association': result[7],
                'collocation_patterns': result[8],
                'evolution_over_time': result[9],
                'cultural_variations': result[10]
            })

    # Close the database connection
    conn.close()

    return identified_phenomena

# Example usage
file_path = "test.txt"
text = preprocess_text(file_path)
results = identify_precedent_phenomena(text)
print("Results:", results)
