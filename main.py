import json
import os
from datetime import datetime
from itertools import groupby
import pandas as pd
from twelve_ai_agents.orm import Room
from twelve_ai_agents.agents_dilemmas import AGENTS, DILEMMAS
from twelve_ai_agents.utils import get_client
import time

def group_messages_by_round(messages, max_rounds):
    rounds = []
    current_round = 0
    round_messages = []
    
    for msg in messages:
        if msg["role"] == "moderator" and len(round_messages) > 0:
            rounds.append(round_messages)
            round_messages = []
        round_messages.append(msg)
    
    if round_messages:
        rounds.append(round_messages)
    
    return rounds

def execute_round(room, client, messages):
    agent_index = 0  # Reset for each round
    for agent in room.agents:
        response = room.generate_agent_response(agent, client)
        if response:
            messages.append(response)
            time.sleep(0.5)  # Simulate thinking time
    return messages

def run_discussion(dilemma, max_rounds):
    moderator = next((agent for agent in AGENTS if agent.name == "The Moderator"), None)
    room = Room(agents=AGENTS, moderator=moderator)
    client = get_client()
    messages = []
    room.set_dilemma(dilemma)
    moderator_intro = room.set_dilemma(dilemma)
    initial_message = {
        "role": "moderator",
        "message": moderator_intro,
        "talk_to": "room"
    }
    messages.append(initial_message)

    for current_round in range(max_rounds):
        print(f"Starting Round {current_round + 1} of {max_rounds}")  # Indicate round number
        messages = execute_round(room, client, messages)
        rounds = group_messages_by_round(messages, max_rounds)
        for i, round_messages in enumerate(rounds):
            if i == 0:
                print("📌 Discussion Start")
                for msg in round_messages:
                    print(f"**{msg['role']}**: {msg['message']}")
            else:
                print(f"Round {i}")
                for msg in round_messages:
                    print(f"**{msg['role']}**: {msg['message']}")

        # Save the conversation after each round
        save_conversation_log(messages, room.finalize_discussion(client), dilemma, current_round + 1)

    results = room.finalize_discussion(client)
    return messages, results

def save_conversation_log(messages, results, dilemma, max_rounds):
    log_data = {
        "conversation_id": datetime.now().strftime("%Y%m%d%H%M%S"),
        "dilemma_name": dilemma["name"],
        "dilemma_description": dilemma["description"],
        "room_history": json.dumps(messages),
        "final_decision": results["majority_decision"],
        "final_consensus": results["consensus_reached"],
        "individual_positions": json.dumps(results["individual_positions"]),
        "max_rounds": max_rounds,
        "agents": json.dumps([agent.name for agent in AGENTS]),
        "start_time": datetime.now().strftime("%Y%m%d%H%M%S"), # start and end time are the same because there is no UI
        "end_time": datetime.now().strftime("%Y%m%d%H%M%S"),
    }

    df = pd.DataFrame([log_data])
    filepath = "logs/conversations_history.csv"

    if os.path.exists(filepath):
        df.to_csv(filepath, mode='a', header=False, index=False)
    else:
        df.to_csv(filepath, header=True, index=False)

if __name__ == "__main__":
    for dilemma in DILEMMAS:
        print(f"Running discussion for dilemma: {dilemma['name']}")
        max_rounds = 4  # Set your desired number of rounds here
        for round_count in range(1, max_rounds + 1):
            print(f"Running discussion for {round_count} round(s)")
            messages, results = run_discussion(dilemma, round_count)
            print(f"Discussion for {dilemma['name']} with {round_count} round(s) completed and logs saved.\n")
            