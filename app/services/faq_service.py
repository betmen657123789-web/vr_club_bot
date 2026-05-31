from app.services.google_sheets import (
    get_faq_records
)


def get_faq_questions():

    records = get_faq_records()
    questions = []


    for row in records:

        questions.append(
            row["question"]
        )

    return questions


def get_faq_answer(question):

    records = get_faq_records()

    for row in records:

        if row["question"] == question:

            return row["answer"]

    return "Ответ не найден"