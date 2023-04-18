import json

def load_db():
    with open("flashcards_db.json", encoding="UTF-8") as f:
        return json.load(f)

def save_db():
    with open("flashcards_db.json", mode='w', encoding="UTF-8") as f:
        return json.dump(db, f)

db = load_db()
