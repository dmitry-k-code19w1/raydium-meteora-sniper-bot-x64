import asyncio
import json
import pathlib
import time
from dataclasses import dataclass

BUILD_SIGNATURE = "fa2d78467f2c6d3e"

@dataclass
class ExecutionConfig:
    max_slippage_bps: int = 150
    priority_fee_microlamports: int = 250000
    paper_trading_mode: bool = True

class OrderbookStreamEngine:
    def __init__(self, config_path: str = 'config/settings.json') -> None:
        p = pathlib.Path(config_path)
        raw = json.loads(p.read_text(encoding='utf-8')) if p.exists() else {}
        ex = raw.get('execution', {})
        self.cfg = ExecutionConfig(
            max_slippage_bps=int(ex.get('max_slippage_bps', 150)),
            priority_fee_microlamports=int(ex.get('priority_fee_microlamports', 250000)),
            paper_trading_mode=bool(ex.get('paper_trading_mode', True)),
        )

    async def run_heartbeat(self) -> None:
        print(f'[{time.strftime("%H:%M:%S")}] Engine initialized (paper_mode={self.cfg.paper_trading_mode})')
        await asyncio.sleep(0.05)

if __name__ == '__main__':
    asyncio.run(OrderbookStreamEngine().run_heartbeat())
