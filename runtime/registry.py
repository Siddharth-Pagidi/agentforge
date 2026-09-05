import sqlite3
from datetime import datetime, timezone
from config import DATABASE_PATH
from schemas.agent_schema import AgentResult
from schemas.team_schema import AgentTeam


class Registry:
    def __init__(self) -> None:
        self.database_path = DATABASE_PATH
        self.initialize()

    def connect(self):
        return sqlite3.connect(self.database_path)

    def initialize(self) -> None:
        with self.connect() as db:
            db.execute("""CREATE TABLE IF NOT EXISTS teams (
                team_name TEXT PRIMARY KEY,
                objective TEXT NOT NULL,
                spec_json TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )""")
            db.execute("""CREATE TABLE IF NOT EXISTS runs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                team_name TEXT NOT NULL,
                task TEXT NOT NULL,
                final_output TEXT NOT NULL,
                duration_ms INTEGER NOT NULL,
                created_at TEXT NOT NULL
            )""")

    def save_team(self, team: AgentTeam) -> None:
        now = datetime.now(timezone.utc).isoformat()
        with self.connect() as db:
            db.execute(
                """INSERT INTO teams(team_name, objective, spec_json, updated_at)
                VALUES (?, ?, ?, ?)
                ON CONFLICT(team_name) DO UPDATE SET
                    objective=excluded.objective,
                    spec_json=excluded.spec_json,
                    updated_at=excluded.updated_at""",
                (team.team_name, team.objective, team.model_dump_json(), now),
            )

    def save_run(
        self,
        team: AgentTeam,
        task: str,
        final_output: str,
        duration_ms: int,
    ) -> int:
        now = datetime.now(timezone.utc).isoformat()
        with self.connect() as db:
            cursor = db.execute(
                """INSERT INTO runs(team_name, task, final_output, duration_ms, created_at)
                VALUES (?, ?, ?, ?, ?)""",
                (team.team_name, task, final_output, duration_ms, now),
            )
            return int(cursor.lastrowid)
