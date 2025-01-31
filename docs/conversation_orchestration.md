# Conversation Orchestration System

## Core Components

### Room Class

The central orchestrator that manages the entire conversation flow. It's responsible for:

- Maintaining a list of participating agents
- Tracking conversation history
- Managing discussion rounds
- Ensuring orderly communication

### Conversation Flow

1. **Initialization**

   - Room is created with a list of agents and a designated moderator
   - Each agent has their own personality, skills, and adaptability level
   - An empty conversation history is initialized

2. **Setting the Dilemma**

   - Moderator introduces the topic/dilemma to all agents
   - Sets up discussion guidelines
   - Creates the first entry in room_history

3. **Discussion Rounds**
   Each round consists of:
   - Generating contextual prompts for each agent
   - Collecting responses from agents
   - Recording responses in both individual and room histories
   - Checking discussion progress

## Key Features

### Dynamic System Prompts

For each agent interaction, the system generates a contextual prompt that includes:

- Agent's personality and characteristics
- Recent conversation history (last 5 messages)
- Current discussion context
- Guidelines for participation

### Targeted Communication

Agents can communicate in two ways:

- To the entire room ("room")
- To specific agents (direct communication)

### Progress Tracking

The system monitors discussion progress through:

- Counting unique speakers
- Tracking participation rates
- Ensuring sufficient engagement (70% participation threshold)

### Discussion Termination

Discussion ends when either:

- Maximum rounds are reached
- Sufficient progress is detected
- Followed by final position statements from all agents

## Implementation Details

### Message Structure

Each message in the room_history contains:

- role: Who's speaking (agent name or "moderator")
- message: The content of the message
- talk_to: The intended recipient(s)

### Error Handling

- Robust error handling for API calls
- Graceful degradation if agents fail to respond
- Continued operation even if some agents don't participate

### Final Phase

1. **Finalization**

   - Each agent provides their final position
   - Positions are recorded and stored

2. **Summary**
   - Complete discussion history is presented
   - Final decisions from each agent are displayed

## Usage Example

```python
# Initialize room
room = Room(agents=agents, moderator=moderator)

# Set discussion topic
room.set_dilemma("How should we handle project deadline delays?")

# Run full discussion
room.run_discussion(client=client, rounds=5)
```

## Best Practices

1. **Prompts**

   - Keep system prompts contextual and personality-driven
   - Include recent history for continuity
   - Maintain clear guidelines

2. **Flow Control**

   - Use max_rounds to prevent endless discussions
   - Monitor participation rates
   - Allow for natural conclusion when consensus is reached

3. **History Management**
   - Maintain both individual and room-wide history
   - Limit context window for efficiency
   - Track both public and targeted messages

This orchestration system creates a structured environment for multi-agent discussions while maintaining personality-driven interactions and natural conversation flow.

Would you like me to elaborate on any particular aspect of the system?
