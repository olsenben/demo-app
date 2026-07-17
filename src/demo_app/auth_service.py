"""Minimal auth helpers (intentionally simple for agent experiments)."""

from __future__ import annotations

import secrets
from dataclasses import dataclass, field


@dataclass
class SessionStore:
    """In-memory session store for demos."""

    sessions: dict[str, str] = field(default_factory=dict)
    used_refresh_tokens: set[str] = field(default_factory=set)

    def issue_tokens(self, user_id: str) -> tuple[str, str]:
        access = secrets.token_urlsafe(16)
        refresh = secrets.token_urlsafe(16)
        self.sessions[access] = user_id
        return access, refresh

    def rotate_refresh(self, refresh_token: str, user_id: str) -> str:
        """Rotate refresh token; rejects reuse (demo guard)."""
        if refresh_token in self.used_refresh_tokens:
            raise ValueError("refresh token reuse detected")
        self.used_refresh_tokens.add(refresh_token)
        access, _new_refresh = self.issue_tokens(user_id)
        return access
