from dataclasses import dataclass

@dataclass
class ScraperConfig:
    max_depth: int = 3
    headless: bool = True
    delay_min: float = 1.0
    delay_max: float = 3.0
    user_agent_rotation: bool = True
    output_dir: str = "output"
