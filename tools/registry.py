class ToolRegistry:
    def __init__(self) -> None:
        self.available_tools: dict[str, str] = {}

    def names(self) -> list[str]:
        return list(self.available_tools)

    def descriptions(self) -> str:
        if not self.available_tools:
            return "No external tools are currently available."
        return "\n".join(
            f"- {name}: {description}"
            for name, description in self.available_tools.items()
        )

    def validate(self, requested_tools: list[str]) -> None:
        unknown = sorted(set(requested_tools) - set(self.available_tools))
        if unknown:
            raise ValueError(
                "Unapproved tools requested: " + ", ".join(unknown)
            )
