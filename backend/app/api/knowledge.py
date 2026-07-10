from fastapi import APIRouter
from pydantic import BaseModel

from app.knowledge.indexer import query_engine

router = APIRouter(
    prefix="/knowledge",
    tags=["Knowledge"],
)


class Query(BaseModel):
    question: str


@router.post("/ask")
def ask(query: Query):

    response = query_engine.query(query.question)

    return {
        "answer": str(response)
    }