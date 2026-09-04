class Planner:

    def analyze_task(self, request):

        request = request.lower()

        if "research" in request:
            return "research"

        if "write" in request:
            return "writer"

        if "analyze" in request:
            return "analysis"

        return "general"