from fastapi import FastAPI, HTTPException, Path
from fastapi.responses import ORJSONResponse
from sqlalchemy import select

from app.dependencies import session_dep
from app.models import ItemModel
from app.schemas import ItemSchema


app = FastAPI(
    title='fastapi-app',
    redoc_url=None,
    default_response_class=ORJSONResponse,
    swagger_ui_parameters={'defaultModelsExpandDepth': -1},
)


@app.get('/ping')
def ping():
    return {'msg': 'pong'}


@app.get('/items/{id}')
async def get_item(
    session: session_dep,
    item_id: int = Path(alias='id'),
) -> ItemSchema:
    stmt = select(ItemModel).where(ItemModel.id == item_id)
    result = await session.execute(stmt)
    result = result.scalar()

    if not result:
        raise HTTPException(
            status_code=404,
            detail='Item not found.',
        )

    return result
