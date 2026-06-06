from app.services.google_sheets import get_faq_records


def get_faq_questions():
    records = get_faq_records()
    return [row["question"] for row in records]


def get_faq_answer(index: int):
    records = get_faq_records()

    try:
        row = records[index]
        return {
            "question": row["question"],
            "answer": row["answer"]
        }
    except IndexError:
        return {
            "question": "Ошибка",
            "answer": "Ответ не найден"
        }