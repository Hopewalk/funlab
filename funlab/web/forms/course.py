from flask_wtf import FlaskForm
from wtforms import (
    validators,
    StringField,
    SelectField,
    DateField,
    widgets,
    fields,
    ValidationError,
)
from flask_mongoengine.wtf import model_form
from funlab import models

BaseCourseForm = model_form(
    models.Course,
    FlaskForm,
    exclude=[
        "created_date",
        "updated_date",
        "creator",
        "updater",
        "status"
    ],
    field_args={
        "name" : {"label": "Course name"},
        "description" : {"label" : "Description"},
        "code" : {"label" : "Code"},
        "enrollment" : {"label" : "Enrollment"},

    }
)

class CourseForm(BaseCourseForm):
    professors = fields.SelectField("Professor")