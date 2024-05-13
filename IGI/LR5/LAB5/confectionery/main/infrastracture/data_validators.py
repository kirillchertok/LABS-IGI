import re


def response_validator(response, request):
    if response is None or request.session.get('role') is None:
        request.session.clear()
        session_validator(request.session)
        return True

def session_validator(session):
    if (session.get('role') is None or session.get('role') == ''):
        session.clear()
        session['role'] = ''
        session['user'] = ''
        session.modified = True

def number_validator(value, t, form):
    try:
        num = t(value)
        if num < 0 or (t == float and num == 0):
            form.add_error(None, f'Неправильный формат числа')
    except:
        form.add_error(None, f'Неправильный формат числа')

def phone_validator(value, form):
    pattern = r'^\+37529\d{7}$'
    if not re.match(pattern, value):
        form.add_error(
            None, 'Номер телефона должен быть вида -> `+37529xxxxxxx`!')
        
def password_validator(value, form):
    if(len(value) < 8):
        form.add_error(None, 'Минимальная длинна пароля - 8 символов')
    if not any(char.isdigit() for char in value):
        form.add_error(None, 'Пароль должен включать хотябы 1 цифру')