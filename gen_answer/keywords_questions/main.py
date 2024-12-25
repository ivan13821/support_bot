#импорт модулей проекта
from gen_answer.keywords_questions.easy_questions.main import EasyQuestions
from gen_answer.database.main import Database


db = Database('keywords questions')



def search_keywords(message: str):

    """ поиск по введенным ключевым словам """

    text = message

    answer = EasyQuestions.generate_easy_answer(text)

    if answer == []:
        return 'Попробуйте перефразировать свой вопрос'

    return answer


















