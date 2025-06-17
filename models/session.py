from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class UserSession:
    user_input: str
    session_id: str
    progress: List[Dict[str, str]] = field(default_factory=list)
    agents_engaged: List[str] = field(default_factory=list)

    def log_agent_engagement(self, agent_name: str):
        self.agents_engaged.append(agent_name)

    def update_progress(self, agent_name: str, content: str):
        self.progress.append({agent_name: content})
        self.log_agent_engagement(agent_name)