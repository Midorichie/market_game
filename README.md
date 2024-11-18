# Prediction Market Game with Bitcoin Integration

## Overview
A decentralized prediction market game leveraging Stacks blockchain, Bitcoin rewards, and multi-source event validation.

## Project Architecture
- **Blockchain**: Stacks (Clarity Smart Contracts)
- **Backend**: Python
- **Game Engine**: Rust
- **Reward Mechanism**: Bitcoin integration

## Features
- Decentralized event prediction
- Multi-source outcome verification
- Reputation-based oracle system
- Secure stake-based betting
- Bitcoin reward distribution

## Prerequisites
- Rust (1.65+)
- Python (3.9+)
- Stacks Blockchain CLI
- Bitcoin Core Wallet

## Installation

### Clone the Repository
```bash
git clone https://github.com/yourusername/prediction-market-game.git
cd prediction-market-game
```

### Setup Environments

#### Rust Game Engine
```bash
cd game_engine
cargo build
cargo test
```

#### Python Backend
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Clarity Smart Contracts
```bash
# Stacks blockchain contract deployment
clarinet check
clarinet deploy
```

## Configuration
Copy `config.example.yml` to `config.yml` and update:
- Blockchain network settings
- Oracle data sources
- Reward wallet configurations

## Running the Application
1. Start Stacks local network
2. Initialize backend services
3. Launch game engine

```bash
# Example startup sequence
stacks-node start
python backend/main.py
cargo run --bin prediction-market
```

## Security Considerations
- Stake-based access control
- Multi-source outcome validation
- Configurable event participation limits

## Contribution Guidelines
1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push and create pull request

## License
MIT License