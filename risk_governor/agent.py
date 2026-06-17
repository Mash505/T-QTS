class RiskGovernor:

    def evaluate(self, signal):

        if signal["confidence"] < 0.65:
            return {
                "approved": False,
                "reason": "Low confidence"
            }

        return {
            "approved": True
        }
