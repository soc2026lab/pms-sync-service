import json
from pathlib import Path


def test_settings_load():
    settings = json.loads((Path(__file__).parent / "fixtures" / "staging_db.json").read_text())
    assert settings["db_user"] == "sync_test"
