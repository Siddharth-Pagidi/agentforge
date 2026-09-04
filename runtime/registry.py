import sqlite3


class AgentRegistry:

    def __init__(self):

        self.db = sqlite3.connect(
            "agentforge.db"
        )

        self.db.execute("""
        CREATE TABLE IF NOT EXISTS agents(
            name TEXT PRIMARY KEY,
            spec TEXT
        )
        """)

    def register(self, spec):

        self.db.execute(
            """
            INSERT OR REPLACE INTO agents
            VALUES(?,?)
            """,
            (
                spec.name,
                spec.model_dump_json()
            )
        )

        self.db.commit()

    def list_agents(self):

        cursor = self.db.execute(
            "SELECT name FROM agents"
        )

        return [
            row[0]
            for row in cursor.fetchall()
        ]