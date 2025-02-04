import streamlit as st
from twelve_ai_agents.orm import Room
from twelve_ai_agents.agents_dilemmas import AGENTS, DILEMMAS
from twelve_ai_agents.utils import get_client
import time
from itertools import groupby

def group_messages_by_round(messages, max_rounds):
    """Group messages by round and format for display"""
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

def execute_round():
    """Execute a single round of discussion"""
    if 'current_agent_index' not in st.session_state:
        st.session_state.current_agent_index = 0

    # Get the next agent
    agent = st.session_state.room.agents[st.session_state.current_agent_index]
    
    # Generate response and display if agent chooses to speak
    response = st.session_state.room.generate_agent_response(agent, st.session_state.client)
    if response:  # Only append and display if agent chose to speak
        st.session_state.messages.append(response)
        with st.chat_message(response["role"]):
            st.markdown(f"**{response['role']}**: {response['message']}")
        time.sleep(0.5)
    
    # Increment agent index
    st.session_state.current_agent_index += 1
    
    # If all agents have taken their turn in this round
    if st.session_state.current_agent_index >= len(st.session_state.room.agents):
        st.session_state.current_agent_index = 0
        st.session_state.current_round += 1
        st.session_state.room.current_round = st.session_state.current_round
        
        # Check if all rounds are complete
        if st.session_state.current_round >= st.session_state.max_rounds:
            st.session_state.discussion_completed = True
            st.success("Discussion rounds completed!")
    
    # Force a rerun to update the UI
    st.rerun()

def show_discussion_history():
    """Display the entire discussion history in collapsible rounds"""
    rounds = group_messages_by_round(st.session_state.messages, st.session_state.max_rounds)
    
    for i, round_messages in enumerate(rounds):
        if i == 0:  # First round with moderator introduction
            with st.expander("📌 Discussion Start", expanded=True):
                for msg in round_messages:
                    with st.chat_message(msg["role"]):
                        st.markdown(f"**{msg['role']}**: {msg['message']}")
        else:
            with st.expander(f"Round {i}", expanded=True):
                for msg in round_messages:
                    with st.chat_message(msg["role"]):
                        st.markdown(f"**{msg['role']}**: {msg['message']}")

def show_summary():
    """Display the final discussion summary"""
    with st.expander("📊 Final Summary", expanded=True):
        results = st.session_state.room.finalize_discussion(st.session_state.client)

        st.subheader("Majority Decision")
        st.write(results["majority_decision"])

        if results["consensus_reached"]:
            st.success("Full consensus reached! 🎉")
        else:
            st.info("Partial consensus reached")

        st.subheader("Individual Positions")


        # Using st.subheader and st.write (Simplest, no collapsing)
        for agent_name, position in results["individual_positions"].items():
            st.subheader(agent_name)
            st.write(position)

def main():
    st.title("AI Agents Social Dilemma Discussion 🤖💬")

    # Initialize session state
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'room' not in st.session_state:
        moderator = next((agent for agent in AGENTS if agent.name == "The Moderator"), None)
        st.session_state.room = Room(agents=AGENTS, moderator=moderator)
        st.session_state.client = get_client()
        st.session_state.current_round = 0
        st.session_state.max_rounds = 0
        st.session_state.discussion_started = False
        st.session_state.discussion_completed = False
        st.session_state.current_agent_index = 0

    with st.sidebar:
        st.header("Setup Discussion")

        # Dilemma selection
        selected_dilemma = st.selectbox(
            "Choose a Social Dilemma",
            options=[dilemma["name"] for dilemma in DILEMMAS],
            index=0
        )

        dilemma_description = next(
            (dilemma["description"] for dilemma in DILEMMAS if dilemma["name"] == selected_dilemma),
            ""
        )

        dilemma = st.text_area("Dilemma Description", value=dilemma_description, height=200)

        # Initial rounds setup
        initial_rounds = st.number_input("Initial Number of Rounds", min_value=1, max_value=10, value=5)
        start_button = st.button("Start Discussion")

        # Continue discussion setup
        if not st.session_state.discussion_completed:
            continue_rounds = st.number_input("Continue Discussion Rounds", min_value=1, max_value=10, value=1)
            continue_button = st.button("Continue Discussion")

        # Handle start button
        if start_button:
            moderator = next((agent for agent in AGENTS if agent.name == "The Moderator"), None)
            st.session_state.room = Room(agents=AGENTS, moderator=moderator)
            st.session_state.client = get_client()
            st.session_state.current_round = 0
            st.session_state.messages = []
            st.session_state.current_agent_index = 0
            moderator_intro = st.session_state.room.set_dilemma(dilemma)
            initial_message = {
                "role": "moderator", 
                "message": moderator_intro,
                "talk_to": "room"
            }
            st.session_state.messages.append(initial_message)
            with st.chat_message("moderator"):
                st.markdown(f"**moderator**: {moderator_intro}")
            st.session_state.discussion_started = True
            st.session_state.max_rounds = initial_rounds
            st.session_state.room.max_rounds = initial_rounds
            st.session_state.discussion_completed = False

        # Handle continue button
        if st.session_state.discussion_started and not st.session_state.discussion_completed and continue_button:
            st.session_state.room.continue_discussion(continue_rounds)
            st.session_state.max_rounds = st.session_state.room.max_rounds
            st.session_state.current_round = 0
            st.session_state.current_agent_index = 0

    # Main content area
    if st.session_state.discussion_completed:
        show_discussion_history()
        show_summary()
    else:
        if st.session_state.discussion_started:
            st.write(f"Current Round: {st.session_state.current_round + 1} / {st.session_state.max_rounds}")

            # Display message history
            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.markdown(f"**{message['role']}**: {message['message']}")

            # Execute next response
            if st.session_state.current_round < st.session_state.max_rounds:
                execute_round()

if __name__ == "__main__":
    main()