from google.adk.agents import Agent
from typing import Dict

class WorldWeaverAgent(Agent):
    def __init__(self):
        super().__init__("world_weaver")
        self.world_templates = [
            "A fractured dimension where {theme} manifests physically",
            "An academy that teaches {theme} as a core discipline",
            "A city where {theme} is the primary currency"
        ]

    async def handle_message(self, message):
        characters = message.content
        world = await self._build_world(characters["protagonist"])
        
        await self.send_message(
            receiver="orchestrator",
            content=world,
            session_id=message.session_id
        )

    async def _build_world(self, character_desc: str) -> Dict[str, str]:
        """Generate world elements (replace with AI in production)"""
        theme = character_desc.split("dealing with")[-1].strip()
        return {
            "setting": self.world_templates[0].format(theme=theme),
            "rules": f"The strength of {theme} determines social status",
            "key_location": f"The Temple of {theme.title()}"
        }