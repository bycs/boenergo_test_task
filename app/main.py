from fastapi import FastAPI
from fastapi import HTTPException

from app.schemas import Color
from app.schemas import QuadraticEquationOutput
from app.utils import quadratic_equation


app = FastAPI()


@app.get("/get_quadratic_equation", response_model=QuadraticEquationOutput)
async def get_quadratic_equation(a: float, b: float, c: float):
    if a == 0:
        detail = [
            {
                "loc": ["query", "a"],
                "msg": "ensure this value is greater than 0",
                "type": "value_error",
            }
        ]
        raise HTTPException(status_code=422, detail=detail)
    solution = quadratic_equation(a, b, c)
    return {"solution": solution}


@app.get("/guess_color/{item_number}", response_model=Color)
async def guess_color(item_number: int):
    if item_number < 1 or item_number > 100:
        detail = [
            {
                "loc": ["path", "item_number"],
                "msg": "Item number must be between 1 and 100",
                "type": "value_error",
            }
        ]
        raise HTTPException(status_code=400, detail=detail)

    blue_items: int = 70
    green_items: int = 20

    if item_number <= blue_items:
        return {"color": "blue"}
    elif item_number <= blue_items + green_items:
        return {"color": "green"}
    else:
        return {"color": "red"}
