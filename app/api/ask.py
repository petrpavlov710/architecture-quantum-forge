from fastapi import APIRouter
from pydantic import BaseModel

from app.rag.rag_chain import call_llm
from app.scripts.query_index import make_query

ask_router = APIRouter()


class QueryRequest(BaseModel):
    question: str


class QueryResponse(BaseModel):
    answer: str | None = None
    error: str | None = None


@ask_router.post("/ask", response_model=QueryResponse)
def ask(req: QueryRequest):
    try:
        context = make_query(req.question)
        answer = call_llm(req.question, context)
        return {"answer": answer.strip()}
    except Exception as e:
        print(f"Ошибка обработки запроса: {e}")
        return {"error": str(e)}
