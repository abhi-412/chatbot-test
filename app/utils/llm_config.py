import os

# o4-mini was hard-coded in two places and was deprecated by OpenAI, which
# returned 404 model_not_found on every turn: the agent run raised, run()
# returned None, and the user just saw "Sorry, something went wrong."
# Keeping the id in one env-backed place means the next deprecation is an App
# Service setting away instead of a code change plus redeploy.
DEFAULT_CHAT_MODEL = "gpt-4.1-mini"


def chat_model_name() -> str:
    """Model id for the conversational agent and the issue extractor."""
    return os.environ.get("OPENAI_CHAT_MODEL") or DEFAULT_CHAT_MODEL
