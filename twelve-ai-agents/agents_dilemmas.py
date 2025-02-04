from .orm import Agent

AGENTS = [
    Agent(
        name="The Visionary",
        personality="Creative, innovative, forward-thinking, and optimistic. Always sees the bigger picture.",
        adaptability=8
    ),
    Agent(
        name="The Strategist",
        personality="Logical, analytical, and meticulous. Great at planning and solving complex problems.",
        adaptability=7
    ),
    Agent(
        name="The Nurturer",
        personality="Empathetic, caring, and supportive. Naturally puts others' needs first.",
        adaptability=6
    ),
    Agent(
        name="The Explorer",
        personality="Adventurous, curious, and spontaneous. Loves trying new things and exploring ideas.",
        adaptability=9
    ),
    Agent(
        name="The Moderator",
        personality="Knows all about the problem. Ensures the conversation stays on track without giving direct opinions.",
        adaptability=7
    ),
    Agent(
        name="The Innovator",
        personality="Thinks outside the box and provides unconventional solutions to problems.",
        adaptability=10
    ),
    Agent(
        name="The Realist",
        personality="Practical, grounded, and focused on what works in the real world.",
        adaptability=5
    ),
    Agent(
        name="The Advocate",
        personality="Passionate about fairness and justice, ensuring everyone's voice is heard.",
        adaptability=6
    ),
    Agent(
        name="The Negotiator",
        personality="Great at resolving conflicts and finding middle ground in tough situations.",
        adaptability=8
    ),
    Agent(
        name="The Analyst",
        personality="Data-driven and methodical, focusing on facts and logic to reach conclusions.",
        adaptability=7
    ),
    Agent(
        name="The Optimist",
        personality="Sees the best in every situation and motivates the group to stay positive.",
        adaptability=8
    ),
    Agent(
        name="The Pragmatist",
        personality="Focuses on practical solutions and achieving tangible results.  Efficient and results-oriented.",
        adaptability=7
    ),
]

DILEMMAS = [
  {
    "name": "The Free Rider Problem",
    "description": "A team of five is working on a project. Everyone is expected to contribute equally, but one person realizes they can slack off because others will cover for them. If everyone thinks this way, the project will fail. How would you ensure everyone contributes fairly without creating resentment?"
  },
  {
    "name": "Overusing Shared Resources (Tragedy of the Commons)",
    "description": "A village shares a common water supply. Overuse by a few individuals depletes the resource, leaving others without water. What policies or systems could you implement to ensure sustainable resource use?"
  },
  {
    "name": "Whistleblowing Ethics",
    "description": "You work at a company where you discover unethical practices. Reporting these practices could harm your career but ignoring them could harm many people. How do you balance your personal risks with the greater good?"
  },
  {
    "name": "Online Trolling and Misinformation",
    "description": "You manage a social media platform. A group spreads harmful misinformation that could influence people negatively, but banning them might raise free speech concerns. How do you decide what content should stay or go while respecting differing opinions?"
  },
  {
    "name": "Vaccination and Herd Immunity",
    "description": "A new vaccine is released for a contagious disease. Some people refuse to take it, either due to fear or personal beliefs, but herd immunity requires a majority to participate. How do you persuade or incentivize people to get vaccinated without infringing on personal freedoms?"
  },
  {
    "name": "The Tragedy of the Commons",
    "description": "A community shares a public resource, such as a fishing lake. If everyone fishes sustainably, the lake thrives. But if individuals overfish for personal gain, the resource becomes depleted, harming everyone in the long term. What strategies would you propose to manage shared resources fairly and sustainably?"
  },
  {
    "name": "The Trolley Problem",
    "description": "A runaway trolley is headed toward five people tied to the tracks. You can pull a lever to divert it to another track, but that track has one person tied to it. Do you sacrifice one to save five? What ethical framework would guide your decision-making?"
  },
  {
    "name": "Climate Change Responsibility",
    "description": "Cutting personal carbon emissions (e.g., driving less, reducing energy use) helps the planet, but your impact alone is negligible compared to systemic changes needed at the corporate and governmental levels. How would you balance personal actions with advocating for larger-scale solutions?"
  },
  {
    "name": "The Prisoner's Dilemma",
    "description": "Two suspects are arrested and interrogated separately. If both stay silent, they each get a minor sentence. If one betrays the other, the betrayer goes free while the other faces a harsh penalty. If both betray, they both receive moderate sentences. How would you convince the other person to trust you and cooperate?"
  },
  {
    "name": "Income Inequality and Redistribution",
    "description": "A wealthy individual is asked to pay higher taxes to fund public services like education and healthcare. While this helps society, it reduces their disposable income. What policies or incentives could encourage fair redistribution without stifling innovation or motivation?"
  },
  {
    "name": "Vaccination Choice",
    "description": "Vaccines protect public health through herd immunity, but some individuals avoid vaccination due to fears of side effects, relying on others to get vaccinated. This puts vulnerable populations at risk. How would you encourage widespread participation in vaccination programs?"
  },
  {
    "name": "The Neighbor's Tree",
    "description": "Your neighbor's tree drops leaves into your yard, creating extra cleanup work for you. Confronting them might damage your relationship, but ignoring it feels unfair. What’s the best way to approach your neighbor to resolve the issue diplomatically?"
  }
]