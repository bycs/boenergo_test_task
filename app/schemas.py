from pydantic import BaseModel


class QuadraticEquationOutput(BaseModel):
    solution: float | tuple[float, float] | None


class Color(BaseModel):
    color: str
