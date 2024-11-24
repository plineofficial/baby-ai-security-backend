from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import (
    InputRequired,
    Length,
    EqualTo, 
    Email, 
    ValidationError,
    StopValidation
)
from exceptions.exception_handler import exception_handler


def create_login_validator():
    class LoginValidator(FlaskForm):
        email = StringField('email', validators=[
            InputRequired('Обязательное поле'),
            Email(message='Некорректная почта')
        ])
        password = StringField('password', validators=[
            InputRequired('Обязательное поле')
        ])
        
    return LoginValidator()

def create_register_validator(database):
    class RegisterValidator(FlaskForm):
        email = StringField('email', validators=[
            InputRequired('Обязательное поле'),
            Email(message='Некорректная почта')
        ])
        password = StringField('password', validators=[
            InputRequired('Обязательное поле'),
            Length(min=6, message='Пароль должен быть минимум из 6 символов')
        ])
        password_confirm = StringField('password_confirm', validators=[
            InputRequired('Обязательное поле'),
            EqualTo('password', 'Пароли не совпадают')
        ])
        
        def validate_email(self, email):
            if email.errors:
                raise StopValidation()
            
            try:
                cursor = database.cursor()
                cursor.execute("""
                    SELECT id, email, password FROM users
                    WHERE email = '%s'
                    """ % email.data
                )
                user = cursor.fetchone()
                if user:
                    raise ValidationError('Почта уже используется')
                
            except Exception as ex:
                if isinstance(ex, (ValidationError, StopValidation)):
                    raise ex
                return exception_handler(ex)
            
            finally:
                if 'cursor' in locals():
                    cursor.close()
            
    return RegisterValidator()
        
def create_user_confirmation_validator():
    class UserConfirmationValidator(FlaskForm):
        password = StringField('password', validators=[
            InputRequired('Обязательное поле')
        ])
        
    return UserConfirmationValidator()
        
        
    
       