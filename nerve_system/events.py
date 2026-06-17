from dataclasses import dataclass
import time

@dataclass
class MarketEvent:
    symbol: str
    price: float
    timestamp: float = time.time()


@dataclass
class SignalEvent:
    symbol: str
    action: str   # BUY / SELL / HOLD
    confidence: float
    timestamp: float = time.time()


@dataclass
class OrderEvent:
    symbol: str
    action: str
    quantity: float
    timestamp: float = time.time()
