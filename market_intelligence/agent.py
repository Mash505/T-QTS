import random
import time

class MarketIntelligenceAgent:

    def get_market_data(self, symbol="BTCUSDT"):
        return {
            "symbol": symbol,
            "price": round(random.uniform(60000, 70000), 2),
            "timestamp": time.time()
        }
