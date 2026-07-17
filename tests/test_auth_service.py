from demo_app.auth_service import SessionStore


def test_refresh_rotation() -> None:
    store = SessionStore()
    _access, refresh = store.issue_tokens("user-1")
    new_access = store.rotate_refresh(refresh, "user-1")
    assert new_access in store.sessions


def test_refresh_reuse_rejected() -> None:
    store = SessionStore()
    _access, refresh = store.issue_tokens("user-1")
    store.rotate_refresh(refresh, "user-1")
    try:
        store.rotate_refresh(refresh, "user-1")
        assert False, "expected ValueError"
    except ValueError as exc:
        assert "reuse" in str(exc)
