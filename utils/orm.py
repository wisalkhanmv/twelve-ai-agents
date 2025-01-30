from typing import List
from pydantic import BaseModel

class Agent(BaseModel):
    name: str  # The agent's name (personality type)
    personality: str  # The approach to problem-solving
    skills: str = "General"  # Skills (default: "General")
    adaptability: int = 5  # Adaptability score (1 to 10, default is 5)
    message_history: List[dict] = []  # Previous messages (empty at initialization)
    final_saying: str = ""  # Final decision made by the agent

class AgentResponse(BaseModel):
    message: str #current message
    talk_to: str #if adressing the whole room then talk_to: room, else it can be directed to any of the 12 agent.
    should_speak: bool #not required to speak unless referred to or has a point to raise.
    final_saying: str #final decision
