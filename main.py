from adk.api import AgentSystem
from agents.orchestrator import OrchestratorAgent
from agents.idea_catalyst import IdeaCatalystAgent
from agents.character_alchemist import CharacterAlchemistAgent
from agents.world_weaver import WorldWeaverAgent
from agents.twist_innovator import TwistInnovatorAgent
from agents.visual_muse import VisualMuseAgent
import asyncio
import uuid

def initialize_agents():
    """Initialize all agents in the system"""
    agent_system = AgentSystem()
    
    agent_system.register(OrchestratorAgent())
    agent_system.register(IdeaCatalystAgent())
    agent_system.register(CharacterAlchemistAgent())
    agent_system.register(WorldWeaverAgent())
    agent_system.register(TwistInnovatorAgent())
    agent_system.register(VisualMuseAgent())
    
    return agent_system

async def simulate_users(agent_system):
    """Simulate multiple users submitting ideas"""
    user_prompts = [
        "A detective who solves crimes in dreams",
        "An artist whose paintings alter reality",
        "A librarian guarding books that rewrite themselves"
    ]
    
    for idx, prompt in enumerate(user_prompts):
        session_id = f"user_{idx+1}_{uuid.uuid4().hex[:6]}"
        await agent_system.send_message(
            receiver="orchestrator",
            content=prompt,
            session_id=session_id
        )
        await asyncio.sleep(0.5)  # Simulate user delay

if __name__ == "__main__":
    print("🌟 Imagination Boost Platform 🌟")
    system = initialize_agents()
    
    # Start simulation (in production, replace with web server)
    asyncio.run(simulate_users(system))
    asyncio.run(system.run())