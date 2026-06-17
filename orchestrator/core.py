from market_intelligence.agent import MarketIntelligenceAgent
from strategy_brain.agent import StrategyBrain
from risk_governor.agent import RiskGovernor
from execution_engine.agent import ExecutionEngine

from nerve_system.bus import EventBus


class Orchestrator:

    def __init__(self):
        self.market = MarketIntelligenceAgent()
        self.strategy = StrategyBrain()
        self.risk = RiskGovernor()
        self.execution = ExecutionEngine()
        self.bus = EventBus()

    def run_cycle(self):

        # 1. Market Data
        market_data = self.market.get_market_data()

        # 2. Strategy Signal
        signal = self.strategy.generate_signal(market_data)

        # 3. Risk Check
        decision = self.risk.evaluate(signal)

        # 4. Execution
        if decision["approved"]:
            result = self.execution.execute(signal)
        else:
            result = {"status": "rejected"}

        return {
            "market": market_data,
            "signal": signal,
            "risk": decision,
            "execution": result
        }
