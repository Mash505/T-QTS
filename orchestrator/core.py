from market_intelligence.agent import MarketIntelligenceAgent
from strategy_brain.agent import StrategyBrain
from risk_governor.agent import RiskGovernor
from execution_engine.agent import ExecutionEngine
from nerve_system.bus import EventBus
from memory_vault.memory import MemoryVault


class Orchestrator:

    def __init__(self):
        self.market = MarketIntelligenceAgent()
        self.strategy = StrategyBrain()
        self.risk = RiskGovernor()
        self.execution = ExecutionEngine()
        self.bus = EventBus()
        self.memory = MemoryVault()

    def run_cycle(self):

        # 1. Market Data
        market_data = self.market.get_market_data()

        self.memory.save_event("MARKET", market_data)

        # 2. Strategy
        signal = self.strategy.generate_signal(market_data)

        self.memory.save_event("SIGNAL", signal)

        # 3. Risk Check
        decision = self.risk.evaluate(signal)

        self.memory.save_event("RISK", decision)

        # 4. Execution
        if decision["approved"]:
            result = self.execution.execute(signal)
        else:
            result = {"status": "rejected"}

        self.memory.save_event("EXECUTION", result)

        return {
            "market": market_data,
            "signal": signal,
            "risk": decision,
            "execution": result
        }
