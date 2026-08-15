from __future__ import annotations

from enum import Enum


class PromotionStage(str, Enum):
    DEV = "dev"
    QA = "qa"
    STG = "stg"
    PRD = "prd"


def stage_order() -> list[str]:
    return [stage.value for stage in PromotionStage]


def validate_stage(stage: str) -> str:
    normalized = stage.lower().strip()
    valid = {item.value for item in PromotionStage}

    if normalized not in valid:
        allowed = ", ".join(sorted(valid))
        raise ValueError(f"Unsupported stage '{stage}'. Expected one of: {allowed}")

    return normalized


def next_stage(stage: str) -> str:
    stages = stage_order()
    validated = validate_stage(stage)
    index = stages.index(validated)

    if index == len(stages) - 1:
        raise ValueError("Promotion has reached the final stage: prd")

    return stages[index + 1]
