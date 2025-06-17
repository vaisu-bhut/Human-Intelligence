from google.adk.agents import Agent
from typing import List

class TwistInnovatorAgent(Agent):
    def __init__(self):
        super().__init__("twist_innovator")
        self.twist_intensity = 0.7  # 0-1 scale

    async def handle_message(self, message):
        world_data = message.content
        twists = await self._generate_twists(world_data["setting"])
        
        await self.send_message(
            receiver="orchestrator",
            content=twists,
            session_id=message.session_id
        )

    async def _generate_twists(self, setting: str) -> List[str]:
        """Create narrative surprises (scale with twist_intensity)"""
        return [
            f"The {setting.split()[0]} is actually a sentient being",
            "The protagonist's goal was a distraction from the real conflict",
            "What appears as magic is actually advanced nanotechnology"
        ][:int(3 * self.twist_intensity)]