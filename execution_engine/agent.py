class ExecutionEngine:

    def execute(self, signal):

        return {
            "status": "executed",
            "order": signal,
            "message": "Simulated trade executed"
        }
