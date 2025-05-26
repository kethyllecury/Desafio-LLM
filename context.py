from collections import defaultdict
from typing import List, Dict

class ContextManager:
    def __init__(self):
        self.sessions: Dict[str, List[dict]] = defaultdict(list)

    def get_context(self, session_id: str) -> List[dict]:
        return self.sessions[session_id]

    def add_message(self, session_id: str, role: str, content: str):
        self.sessions[session_id].append({
            "role": role,
            "content": content
        })

    def reset_context(self, session_id: str):
        self.sessions[session_id] = []

context_manager = ContextManager()
