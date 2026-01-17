import yaml
from pathlib import Path


# Resolve project root dynamically
BASE_DIR = Path(__file__).resolve().parents[2]


def load_yaml(file_path: Path) -> dict:
    with open(file_path, "r") as f:
        return yaml.safe_load(f)


# Load parameters and thresholds
PARAMETERS_PATH = BASE_DIR / "src" / "config" / "parameters.yaml"
THRESHOLDS_PATH = BASE_DIR / "src" / "config" / "thresholds.yaml"

parameters = load_yaml(PARAMETERS_PATH)
thresholds = load_yaml(THRESHOLDS_PATH)
