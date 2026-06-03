"""
FG RiskMap — Financial Distortion Monitor

Demo calculation only.

This script does not make legal, tax, audit, lending, investment, regulatory,
or compliance decisions. It only demonstrates pre-answer risk routing and
distortion mapping.
"""

from pathlib import Path
import csv
import json


ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "sample_workflow_data.csv"
OUTPUT_FILE = ROOT / "outputs" / "sample_output.json"


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def calculate_iti(row: dict) -> float:
    """
    Arithmetic Institutional Tension Index.

    In this simplified demo, ITI is the average of normalized pressure variables.
    """
    variables = [
        float(row["leverage_pressure"]),
        float(row["liquidity_pressure"]),
        float(row["related_party_pressure"]),
        float(row["document_gap_pressure"]),
    ]

    return clamp(sum(variables) / len(variables))


def calculate_giti(row: dict) -> float:
    """
    Geometric Institutional Tension Index.

    In this simplified demo, gITI rises when:
    - routing compression increases;
    - mobility capacity falls;
    - continuity capacity falls.
    """
    routing_compression = float(row["routing_compression"])
    mobility_loss = 1.0 - float(row["mobility_capacity"])
    continuity_loss = 1.0 - float(row["continuity_capacity"])

    variables = [
        routing_compression,
        mobility_loss,
        continuity_loss,
    ]

    return clamp(sum(variables) / len(variables))


def classify_status(iti: float, giti: float, idi: float) -> str:
    """
    Routing status.

    This is not a compliance conclusion.
    It is only a pre-review routing flag.
    """
    if idi >= 0.25 or giti >= 0.75:
        return "Escalate"

    if idi >= 0.15 or giti >= 0.55:
        return "Distorted"

    if iti >= 0.40 or giti >= 0.35:
        return "Watch"

    return "Stable"


def main() -> None:
    results = []

    with DATA_FILE.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            iti = calculate_iti(row)
            giti = calculate_giti(row)
            idi = abs(iti - giti)
            status = classify_status(iti, giti, idi)

            results.append(
                {
                    "period": row["period"],
                    "ITI": round(iti, 4),
                    "gITI": round(giti, 4),
                    "IDI": round(idi, 4),
                    "routing_status": status,
                    "human_review_required": status in ["Distorted", "Escalate"],
                }
            )

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(json.dumps(results, indent=2), encoding="utf-8")

    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
