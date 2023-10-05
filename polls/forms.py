from django.forms import modelformset_factory, SplitDateTimeWidget
from .question import Question


QuestionsFormSet = modelformset_factory(
    Question,
    fields=("question_text", "pub_date"),
    # widgets={"pub_date": SplitDateTimeWidget},
    extra=1,
)
