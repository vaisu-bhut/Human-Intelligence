from google.adk.agents import Agent
from typing import Dict

class VisualMuseAgent(Agent):
    def __init__(self):
        super().__init__("visual_muse")
        self.style_presets = [
            "digital art, vibrant colors",
            "watercolor, dreamy aesthetic",
            "steampunk illustration"
        ]

    async def handle_message(self, message):
        twists = message.content
        visuals = await self._create_visual_prompts(twists[0])
        
        await self.send_message(
            receiver="orchestrator",
            content=visuals,
            session_id=message.session_id
        )

    async def _create_visual_prompts(self, twist: str) -> Dict[str, str]:
        """Generate visual concepts (connect to image model in production)"""
        return {
            "main_scene": f"{self.style_presets[0]}, {twist}, dramatic lighting",
            "character_design": f"{self.style_presets[1]}, protagonist with glowing markings",
            "mood_board": f"{self.style_presets[2]}, surreal architecture, emotional atmosphere"
        }