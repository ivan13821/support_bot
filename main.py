from fastapi import FastAPI
from gen_answer.keywords_questions.main import search_keywords
from pydantic import BaseModel


#Запуск
#uvicorn main:app --host localhost --port 8000


app = FastAPI()

class Item(BaseModel):
    """Тело запроса"""
    question: str


@app.get("/")
async def root(question: Item):

    """ генерирует ответ на основе введеных слов """

    answer = search_keywords(question.question)

    return {"answer": answer}