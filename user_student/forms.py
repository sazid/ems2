from django import forms

from users.models import User
from core.models import Exam, Question


class ExamForm(forms.ModelForm):
    def __init__(self, exam_pk=None, *args, **kwargs):
        super(ExamForm, self).__init__(*args, **kwargs)

        questions = Question.objects.filter(exams__in=[exam_pk])

        for q in questions:
            if q.question_type == Question.QUESTION_TYPE_MCQ:
                self.fields[f'question_{q.pk}'] = forms.CharField(required=False, label=q.title)
            if q.question_type == Question.QUESTION_TYPE_DESCRIPTIVE:
                self.fields[f'question_{q.pk}'] = forms.CharField(required=False, widget=forms.Textarea, label=q.title)
            if q.question_type == Question.QUESTION_TYPE_FILE:
                self.fields[f'question_{q.pk}'] = forms.FileField(required=False, label=q.title)

    class Meta:
        model = Exam
        fields = tuple()
        # fields = ('name', 'note', 'start', 'end',)
