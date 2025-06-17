"""
Root agent for the creative pipeline.

This file exposes the orchestrator agent, which coordinates all subagents:
- idea_catalyst
- character_alchemist
- world_weaver
- twist_innovator
- visual_muse

The orchestrator manages the workflow and message passing between these agents.
"""

from .subagents.orchestrator import orchestrator