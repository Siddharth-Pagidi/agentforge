from schemas.agent_schema import AgentSpec


class AgentFactory:

    def create_agent(self, agent_type):

        if agent_type == "research":

            return AgentSpec(
                name="ResearchAgent",
                purpose="Research information from sources",
                tools=[
                    "web_search"
                ],
                workflow=[
                    "create_plan",
                    "search_sources",
                    "verify_sources",
                    "generate_report"
                ],
                model="gpt-5"
            )

        if agent_type == "analysis":

            return AgentSpec(
                name="AnalysisAgent",
                purpose="Analyze information",
                tools=[
                    "calculator"
                ],
                workflow=[
                    "collect_data",
                    "run_analysis",
                    "generate_summary"
                ],
                model="gpt-5"
            )

        if agent_type == "writer":

            return AgentSpec(
                name="WriterAgent",
                purpose="Write content",
                tools=[],
                workflow=[
                    "create_outline",
                    "write_draft",
                    "edit_content"
                ],
                model="gpt-5"
            )

        return AgentSpec(
            name="GeneralAgent",
            purpose="General tasks",
            tools=[],
            workflow=[
                "process_request"
            ],
            model="gpt-5"
        )