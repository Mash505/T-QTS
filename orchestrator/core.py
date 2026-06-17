from market_intelligence.agent import MarketIntelligenceAgent
from strategy_brain.agent import StrategyBrain
from risk_governor.agent import RiskGovernor
from execution_engine.agent import ExecutionEngine
from memory_vault.memory import MemoryVault
from nerve_system.bus import EventBus
from nerve_system.topics import *

class Orchestrator:

    def __init__(self):
        self.market = MarketIntelligenceAgent()
        self.strategy = StrategyBrain()
        self.risk = RiskGovernor()
        self.execution = ExecutionEngine()

        self.memory = MemoryVault()
        self.bus = EventBus()

    def run_cycle(self):

        # 1. MARKET EVENT
        market_data = self.market.get_market_data()

        self.bus.publish(MARKET_TOPIC, market_data)
        self.memory.save_event("MARKET", market_data)

        # 2. STRATEGY
        signal = self.strategy.generate_signal(market_data)

        self.bus.publish(SIGNAL_TOPIC, signal)
        self.memory.save_event("SIGNAL", signal)

        # 3. RISK
        decision = self.risk.evaluate(signal)

        self.bus.publish(RISK_TOPIC, decision)
        self.memory.save_event("RISK", decision)

        # 4. EXECUTION
        if decision["approved"]:
            result = self.execution.execute(signal)
        else:
            result = {"status": "rejected"}

        self.bus.publish(EXECUTION_TOPIC, result)
        self.memory.save_event("EXECUTION", result)

        return {
            "market": market_data,
            "signal": signal,
            "risk": decision,
            "execution": result
        }
