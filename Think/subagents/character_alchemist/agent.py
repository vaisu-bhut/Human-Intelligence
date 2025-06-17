from google.adk.agents import Agent
from typing import Dict, List

class CharacterAlchemistAgent(Agent):
    def __init__(self):
        super().__init__("character_alchemist")
        self.archetypes = ["hero", "mentor", "trickster", "shadow"]

    async def handle_message(self, message):
        story_ideas = message.content
        characters = await self._develop_characters(story_ideas[0])  # Take first idea
        
        await self.send_message(
            receiver="orchestrator",
            content=characters,
            session_id=message.session_id
        )

    async def _develop_characters(self, story_idea) -> Dict[str, str]:
        """Create character profiles (replace with AI)"""
        return {
            "protagonist": f"A {self.archetypes[0]} dealing with {story_idea.split(':')[1]}",
            "mentor": f"An eccentric {self.archetypes[1]} who knows too much",
            "antagonist": f"A {self.archetypes[3]} representing creative blocks"
        }