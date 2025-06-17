from google.adk.agents import Agent
from models.session import UserSession

class OrchestratorAgent(Agent):
    def __init__(self):
        super().__init__("orchestrator")
        self.sessions = {}  # session_id: UserSession

    async def handle_message(self, message):
        session_id = message.session_id
        
        if session_id not in self.sessions:
            self.sessions[session_id] = UserSession(
                user_input=message.content,
                session_id=session_id
            )
            await self._start_workflow(session_id)
        else:
            await self._process_agent_response(
                session_id,
                message.sender,
                message.content
            )

    async def _start_workflow(self, session_id):
        """Initiate the agent collaboration chain"""
        session = self.sessions[session_id]
        await self.send_message(
            receiver="idea_catalyst",
            content=session.user_input,
            session_id=session_id
        )
        session.log_agent_engagement("idea_catalyst")

    async def _process_agent_response(self, session_id, agent_name, content):
        """Route responses between agents"""
        session = self.sessions[session_id]
        session.update_progress(agent_name, content)
        
        if agent_name == "idea_catalyst":
            await self._engage_character_alchemist(session_id, content)
        elif agent_name == "character_alchemist":
            await self._engage_world_weaver(session_id, content)
        elif agent_name == "world_weaver":
            await self._engage_twist_innovator(session_id, content)
        elif agent_name == "twist_innovator":
            await self._engage_visual_muse(session_id, content)
        elif agent_name == "visual_muse":
            await self._finalize_session(session_id)

    # Additional agent-specific engagement methods...