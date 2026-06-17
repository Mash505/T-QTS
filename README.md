# T-QTS (T Quantitative Trading System)

> Fully autonomous multi-agent AI trading system for Indian Stock Market, Crypto, and Forex.

---

## ⚠️ DISCLAIMER

T-QTS is an experimental financial AI system.

It does NOT guarantee profits.
All trading involves risk of loss.

Use at your own responsibility.
Always start with paper trading.

---

## 🧠 OVERVIEW

T-QTS is a modular AI trading architecture consisting of multiple autonomous agents:

- Market Intelligence Agent
- Strategy Brain (AI/ML)
- Risk Governor
- Execution Engine
- Memory Vault
- Orchestrator (System Brain)

---

## 🏗️ SYSTEM ARCHITECTURE
---

## 🤖 CORE AGENTS

### 1. Market Intelligence Agent
- Freqtrade
- FreqAI
- Real-time market data processing

### 2. Strategy Brain
- FinRL (Reinforcement Learning)
- Decision making engine
- BUY / SELL / HOLD signals

### 3. Risk Governor
- Stop-loss enforcement
- Position sizing
- Drawdown protection
- Kill switch system

### 4. Execution Engine
- Broker APIs (Binance / Zerodha / Forex brokers)
- Order execution system
- Trade monitoring

### 5. Memory Vault
- Redis (real-time memory)
- PostgreSQL (trade history)
- TimescaleDB (market data)
- Vector DB (AI knowledge memory)

### 6. Orchestrator
- LangGraph / CrewAI
- Controls full system flow

---

## 📱 MOBILE APP (T-QTS CONTROL TOWER)

Flutter-based app:

- Live portfolio tracking
- Trade monitoring
- AI decision dashboard
- Risk alerts
- System control panel
- Emergency STOP button

---

## 🧠 SELF-LEARNING SYSTEM

T-QTS continuously improves using:

- Trade history learning
- Pattern recognition
- Strategy evaluation
- Backtesting feedback loop
- Paper trading validation

Learning Flow:

```

Trade → Store Memory → Analyze → Improve Strategy → Validate → Deploy
