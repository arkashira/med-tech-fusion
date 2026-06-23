from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Engineer:
    id: int
    name: str
    portfolio: List[str]
    experience: int

class EngineerPlatform:
    def __init__(self):
        self.engineers = {}

    def add_engineer(self, engineer: Engineer):
        self.engineers[engineer.id] = engineer

    def search_engineers(self, query: str) -> List[Engineer]:
        return [engineer for engineer in self.engineers.values() if query in engineer.name]

    def get_engineer_profile(self, engineer_id: int) -> Engineer:
        return self.engineers.get(engineer_id)

    def send_message(self, engineer_id: int, message: str) -> bool:
        if engineer_id in self.engineers:
            # Simulate sending a message
            print(f"Message sent to engineer {engineer_id}: {message}")
            return True
        return False
