from requests import get


def test_request(message, request):
    output = f'{message}: {get(request)} {get(request).json()}'
    print('-' * len(output))
    print(output)
    print('-' * len(output))
    print()


cases = [
    ['Получение всех работ', 'http://127.0.0.1:8080/api/jobs'],
    ['Корректное получение одной работы', 'http://127.0.0.1:8080/api/jobs/1'],
    ['Ошибочный запрос на получение одной работы — неверный id', 'http://127.0.0.1:8080/api/jobs/999'],
    ['Ошибочный запрос на получение одной работы — строка', 'http://127.0.0.1:8080/api/jobs/q']
]
for case in cases:
    test_request(*case)
