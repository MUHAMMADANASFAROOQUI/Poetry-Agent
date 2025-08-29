import asyncio
from connection import config
from agents import Agent, Runner,trace
import rich

# Define lyric poetry agent
lyrical_poetry_agent = Agent(
    name="Lyric Poetry Agent",
    instructions="You are the lyrical poetry agent. You have to analyze lyrical poetry and explain its emotional content.",
    handoff_description="This agent can provide a description of lyrical poetry."
)

# Define narrative poetry agent
narrative_poetry_agent = Agent(
    name="Narrative Poetry Agent",
    instructions="You are the narrative poetry agent. You have to analyze narrative poetry and explain the story.",
    handoff_description="This agent can provide a description of narrative poetry."
)

# Define dramatic poetry agent
dramatic_poetry_agent = Agent(
    name="Dramatic Poetry Agent",
    instructions="You are the dramatic poetry agent. You have to analyze dramatic poetry and explain the character's emotions.",
    handoff_description="This agent can provide a description of dramatic poetry."
)

# Define parent triage agent
triage_agent = Agent(
    name="Triage Agent",
    instructions=(
        "You are the triage agent. The user will give you a stanza of poem . "
        "Your job is to classify whether it is Lyric, Narrative, or Dramatic poetry, "
        "and then hand off the task to the appropriate agent."
    ),
    handoffs=[lyrical_poetry_agent, narrative_poetry_agent, dramatic_poetry_agent]
)



# Main method to run
async def main():
    with trace("Poetry Agent"):
        result = await Runner.run(
            triage_agent, 
            """
                Water, water, every where,
                And all the boards did shrink;
                Water, water, every where,
                Nor any drop to drink.
            """, 
            run_config=config)
        rich.print(f"\n📝 User's Poem:\n")
        rich.print(input)
        rich.print("\n Handoff to ==> ",result.last_agent.name)
        rich.print("\n Explanation =",result.final_output)


if __name__ == "__main__":
    asyncio.run(main())