import json
from tool_note import Note

class NoteManager:
    def __init__(self, filename: str = "notes.json"):
        self.filename = filename
        self.notes: list[Note] = []
        self.load_notes()

    def load_notes(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.notes = [Note(**note) for note in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.notes = []

    def save_notes(self):
        with open(self.filename, "w") as f:
            json.dump([note.to_dict() for note in self.notes], f, indent=4)

    def add_note(self, title: str, content: str):
        note = Note(title, content)
        self.notes.append(note)
        self.save_notes()
        print(f"Note '{title}' saved.")

    def list_notes(self):
        for note in self.notes:
            print(f"[{note.created_at}] {note.title}")

# Пример использования
if __name__ == "__main__":
    manager = NoteManager()
    manager.add_note("Идея проекта", "Реализовать мини-блокнот на Python")
    manager.add_note("Заметка", "Изучить FastAPI и SQLAlchemy")
    print("\nВсе заметки:")
    manager.list_notes()
    breakpoint()
    