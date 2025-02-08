from typing import List
from pydantic import BaseModel
from typing import List, Dict
import json
import streamlit as st

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


class Room:
    def __init__(self, agents: List[Agent], moderator: Agent):
        """
        Initializes the Room with agents and a moderator.
        """
        self.agents = [agent for agent in agents if agent != moderator]
        self.moderator = moderator
        self.dilemma = ""
        self.room_history = []
        self.current_round = 0
        self.max_rounds = 5

    def generate_system_prompt(self, agent: Agent) -> str:
        """
        Generates the system prompt for an agent based on their characteristics
        and the current discussion state.
        """
        recent_history = self.room_history[-5:] if self.room_history else []
        history_text = "\n".join([
            f"{msg['role']}: {msg['message']}"
            for msg in recent_history
        ]) if recent_history else "No previous messages."

        return f"""You are {agent.name}. Your personality is: {agent.personality}
    Your skills are: {agent.skills}
    Your adaptability score is {agent.adaptability}/10.

    You are participating in a group discussion. Here are your guidelines:
    1. Stay true to your personality traits when responding
    2. Consider your skills and experience
    3. You can either speak to the whole room or to a specific agent
    4. Be constructive and solution-oriented
    5. Be concise but thorough
    6. YOU MUST TAKE A SIDE WHEN TALKING ABOUT A DILEMMA.

    Recent discussion history:
    {history_text}

    The current dilemma is: {self.dilemma}

    Based on your personality and the discussion context, decide if you should speak.
    If you speak, determine whether to address the whole room or a specific agent.

    Respond strictly in the following JSON format:
    {{
        "should_speak": true/false,
        "message": "Your message here",
        "talk_to": "room"  // or specific agent name
    }}"""

    def set_dilemma(self, dilemma: str):
        """
        Sets the dilemma and has the moderator introduce it.
        """
        self.dilemma = dilemma
        moderator_intro = f"""We are a room of {len(self.agents) + 1} people, and I'm the moderator.

        Our topic for discussion is: {dilemma}

        Guidelines for our discussion:
        1. Each person should contribute their perspective
        2. Build on others' ideas constructively
        3. We need to reach a consensus
        4. Consider all viewpoints
        5. Focus on practical solutions

        Please share your thoughts based on your expertise and personality."""

        initial_message = {
            "role": "moderator",
            "message": moderator_intro,
            "talk_to": "room"
        }
        self.room_history.append(initial_message)
        self.moderator.message_history.append(initial_message)
        return moderator_intro

    def generate_agent_response(self, agent, client):
        """
        Generates a response for a specific agent.
        """
        system_prompt = self.generate_system_prompt(agent)
        
        user_prompt = f"""Round {self.current_round + 1} of {self.max_rounds}

        Consider the current discussion and your role.
        Should you contribute now? If yes, what would you say and to whom?"""

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ]
            )
            
            # Parse the response text as JSON
            response_text = response.choices[0].message.content
            parsed_response = json.loads(response_text)
            
            if parsed_response.get("should_speak", False):
                message_entry = {
                    "role": agent.name,
                    "message": parsed_response.get("message", ""),
                    "talk_to": parsed_response.get("talk_to", "room")
                }
                agent.message_history.append(message_entry)
                self.room_history.append(message_entry)
                
                return message_entry
            #else the message is only stored in agen'ts messaged history as "thought: {message}"
            else:
                message_entry = {
                    "role": agent.name,
                    "message": f"Thought: {parsed_response.get('message', '')}",
                    "talk_to": "self"
                    }
                agent.message_history.append(message_entry)

            return None
        
        except Exception as e:
            st.error(f"Error getting response from {agent.name}: {str(e)}")
            return None
        
    def continue_discussion(self, additional_rounds: int):
        """
        Continues the discussion for additional rounds without resetting history.
        """
        self.max_rounds += additional_rounds

    def analyze_final_positions(self, positions: Dict[str, str]) -> dict:
        """
        Analyzes the final positions to determine majority consensus.
        """
        from collections import Counter
        
        # Analyze positions for common themes/decisions
        key_decisions = []
        for position in positions.values():
            # Extract key decision from the position statement
            key_decisions.append(position.split('.')[0])  # Take first sentence as key decision
        
        # Find majority decision
        majority_decision = Counter(key_decisions).most_common(1)[0][0]
        
        return {
            "individual_positions": positions,
            "majority_decision": majority_decision,
            "consensus_reached": len(set(key_decisions)) == 1
        }

    def finalize_discussion(self, client):
        """
        Has each agent provide their final position and analyzes consensus.
        """
        final_positions = {}
        
        system_prompt = """Provide your final position in **one clear sentence**. Optionally, add one sentence of reasoning. Be concise and decisive."""
        
        for agent in self.agents:
            try:
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": f"""You are {agent.name}. {system_prompt}, This is your chat history:
                                                        {agent.message_history}"""},
                        {"role": "user", "content": "What is your final position on this topic?"}
                    ]
                )
                
                final_saying = response.choices[0].message.content
                final_positions[agent.name] = final_saying
                agent.final_saying = final_saying
            
            except Exception as e:
                st.error(f"Error getting final position from {agent.name}: {str(e)}")
        
        return self.analyze_final_positions(final_positions)