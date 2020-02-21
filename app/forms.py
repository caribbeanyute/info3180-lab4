from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField,TextField
from wtforms.validators import DataRequired, Email

images = ['jpg', 'png']
class UploadForm(FlaskForm):
    file = FileField('file', validators=[ FileRequired(),
        FileAllowed(images, 'Images only!')])
   