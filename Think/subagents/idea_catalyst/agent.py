from google.adk.agents import Agent

class IdeaCatalystAgent(Agent):
    def __init__(self):
        super().__init__("idea_catalyst")
        self.creativity_level = 1.0  # Adjustable creativity parameter

    async def handle_message(self, message):
        prompt = message.content
        variants = await self._generate_ideas(prompt)
        
        await self.send_message(
            receiver="orchestrator",
            content=variants,
            session_id=message.session_id
        )

    async def _generate_ideas(self, prompt):
        """Generate multiple story angles (replace with actual AI call)"""
        return [
            f"Sci-fi: {prompt} in 3023 with neural implants",
            f"Fantasy: {prompt} in a magic academy",
            f"Noir: {prompt} in 1940s Los Angeles"
        ]