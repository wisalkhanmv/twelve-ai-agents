# **Simulating Real-World Decision-Making with Twelve AI Agents**

In traditional AI interactions, we usually receive a single response from a model trained to provide a well-reasoned answer. But what if, instead of a single AI perspective, we had multiple AI agents—each with a distinct personality—debating and refining ideas collaboratively? That’s the experiment I conducted with **Twelve AI Agents**, an open-source project designed to simulate real-life meetings where AI-driven personalities discuss complex issues, challenge one another, and (hopefully) converge on a decision.

## **The Idea Behind Twelve AI Agents**

In real-world decision-making, different perspectives matter. A marketing strategist, a visionary CEO, a cautious analyst, and a pragmatic operations manager will each see a problem through a unique lens. Inspired by this, I developed twelve AI agents, each embodying different problem-solving styles:

- **The Visionary** – Thinks big and long-term.
- **The Strategist** – Plans and optimizes outcomes.
- **The Nurturer** – Prioritizes ethical and human-centered solutions.
- **The Explorer** – Seeks unconventional and out-of-the-box ideas.
- **The Moderator** – Ensures structured discussion and decision-making.
- **The Innovator** – Pushes for radical and transformative solutions.
- **The Realist** – Grounds discussions in practicality.
- **The Advocate** – Represents specific interests or ethical concerns.
- **The Negotiator** – Works toward compromises and middle-ground solutions.
- **The Analyst** – Focuses on data-driven insights.
- **The Optimist** – Sees opportunities and positive outcomes.
- **The Pragmatist** – Focuses on what is feasible and efficient.

These agents aren’t just static personas; they adapt over multiple discussion rounds, reconsidering their views based on new arguments. This flexibility prevents them from being locked into rigid positions, making the discussions dynamic.

## **How It Works**

The process is straightforward:

1. **A problem is introduced** – The **Moderator** AI presents a dilemma or decision-making scenario.
2. **Agents discuss** – Each agent contributes based on their perspective. Some may choose to stay silent but internally process the discussion.
3. **Multiple rounds of refinement** – The agents debate, challenge, and adapt their views over several rounds, attempting to reach a consensus.
4. **Final decision (or lack thereof)** – After a set number of rounds, the discussion ends, and the final conclusions are recorded.

## **The Dilemmas We Tested**

To evaluate how well this multi-agent system works, I tested it with **twelve different dilemmas**, including:

- **The Free Rider Problem** – How should societies handle individuals who benefit without contributing?
- **Tragedy of the Commons** – Managing shared resources sustainably.
- **Whistleblower Ethics** – When is it ethical to expose wrongdoing?
- **The Trolley Problem** – Classic moral dilemma of choosing between two evils.
- **Climate Change Responsibility** – Who should take action, and how?
- **The Prisoner’s Dilemma** – Cooperation vs. self-interest in decision-making.
- **Income Inequality and Redistribution** – How should wealth be distributed?
- **Vaccination and Herd Immunity** – Balancing personal choice with public health.
- **Online Trolling and Misinformation** – How to counteract digital toxicity.
- **The Neighbor’s Tree Problem** – Small-scale conflict resolution.

### **Findings: Do They Reach Consensus?**

Interestingly, the agents **often failed to reach a final consensus** on highly philosophical dilemmas. For example, in the **Trolley Problem**, instead of picking a side (saving one person vs. saving five), they drifted into discussions on the ethics of decision-making itself. Similarly, in the **Tragedy of the Commons**, the discussion turned into a debate on governance rather than a clear resolution.

However, in **strategic decision-making scenarios**—such as creating a **marketing plan** or deciding on a business growth strategy—the agents performed much better. The diverse perspectives actually helped refine decisions, leading to well-balanced conclusions. This shows that the model is particularly useful in **collaborative strategy-building rather than strict moral dilemmas**.

## **Challenges and Considerations**

While this approach is promising, it has some drawbacks:

- **Time and Cost** – Running multiple AI agents over multiple discussion rounds is computationally expensive.
- **Lack of Decisiveness** – On certain issues, they prioritize discussion over resolution, sometimes leading to endless debates.
- **Derailment Risks** – Conversations can drift into tangents, especially with ethical dilemmas.

## **Making It Open-Source**

To allow others to experiment with this framework, I developed a Python library called **Twelve AI Agents**, which is available as an **open-source project**. Users can install the package, define their own discussion environments, and have the agents tackle any problem they choose.

I also included logging capabilities, so every discussion session is recorded for further analysis. Whether it’s for **business strategy, ethics, policy-making, or even game design**, users can simulate these multi-agent discussions and gain unique insights.

## **Final Thoughts**

Is this better than a single AI reasoning model? In some cases, yes—especially when multiple perspectives are valuable. However, the process is slower and computationally heavy. While traditional AI gives you **one best answer**, this method provides a **group discussion with diverse viewpoints**, making it useful for collaborative decision-making.

I’ll be sharing more insights on this project, but for now, if you want to experiment with **Twelve AI Agents**, check out the open-source project and see how these AI personalities navigate decision-making!
