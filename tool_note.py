
from datetime import datetime
import uuid


class Note:
    def __init__(self, title: str, content: str):
        self.id = str(uuid.uuid4())

        self.title = title
        self.content = content
        self.created_at = datetime.now().isoformat()
        self.status = True

    def to_dict(self):
        if self.status:
            return {
                "id": self.id,
                "title": self.title,
                "content": self.content,
                "created_at": self.created_at
            }
