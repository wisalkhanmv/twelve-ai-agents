import streamlit as st
from utils.orm import Room
from utils.agents_personalities import agents
from utils.utils import get_client

def main():
    st.title("AI Agents Social Dilemma Discussion 🤖💬")
    
    # Initialize session state variables if not already set
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    if 'room' not in st.session_state:
        # Find moderator
        moderator = next((agent for agent in agents if agent.name == "The Moderator"), None)
        # Initialize room
        st.session_state.room = Room(agents=agents, moderator=moderator)
        st.session_state.client = get_client()

    # Sidebar for setting dilemma
    with st.sidebar:
        st.header("Setup Discussion")
        dilemma = st.text_area("Enter the Social Dilemma:", 
                                "A team member is not contributing to a group project. How should the team respond?")
        start_button = st.button("Start Discussion")
        
        if start_button:
            # Reset messages
            st.session_state.messages = []
            # Set dilemma
            moderator_intro = st.session_state.room.set_dilemma(dilemma)
            # Add moderator's introduction to messages
            st.session_state.messages.append({
                "role": "moderator", 
                "content": moderator_intro
            })

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Add a next round button
    if st.button("Next Round of Discussion"):
        # Generate responses for each agent
        for agent in st.session_state.room.agents:
            response = st.session_state.room.generate_agent_response(agent, st.session_state.client)
            
            if response:
                st.session_state.messages.append({
                    "role": response["role"], 
                    "content": response["message"]
                })
                st.experimental_rerun()

    # Add a finalize discussion button
    if st.button("Finalize Discussion"):
        final_positions = st.session_state.room.finalize_discussion(st.session_state.client)
        
        st.header("Final Positions")
        for agent_name, position in final_positions.items():
            st.subheader(agent_name)
            st.write(position)

if __name__ == "__main__":
    main()