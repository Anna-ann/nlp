import spacy
import sqlite3

nlp = spacy.load("en_core_web_sm")

def preprocess_text(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
    return text

def identify_precedent_phenomena(doc):
    conn = sqlite3.connect('selected_precedents.db')
    cursor = conn.cursor()

    identified_phenomena = []

    named_entities = [ent.text for ent in doc.ents]

    tokens = named_entities + [token.text for token in doc]

    for token in tokens:
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

    conn.close()

    return identified_phenomena

if __name__ == "__main__":
    file_path = input("Enter the path to the text file: ")

    text = preprocess_text(file_path)

    doc = nlp(text)

    identified_phenomena = identify_precedent_phenomena(doc)

    for phenomenon in identified_phenomena:
        print(f"Name: {phenomenon['name']}")
        print(f"Cultural Meaning: {phenomenon['cultural_meaning']}")
        print(f"Recognition Level: {phenomenon['recognition_level']}")
        print(f"Interpretation: {phenomenon['interpretation']}")
        print(f"Symbolic Meaning: {phenomenon['symbolic_meaning']}")
        print(f"Associated Event: {phenomenon['associated_event']}")
        print(f"Adaptable Usage: {phenomenon['adaptable_usage']}")
        print(f"Semantic Association: {phenomenon['semantic_association']}")
        print(f"Collocation Patterns: {phenomenon['collocation_patterns']}")
        print(f"Evolution Over Time: {phenomenon['evolution_over_time']}")
        print(f"Cultural Variations: {phenomenon['cultural_variations']}")
        print("-" * 80)
