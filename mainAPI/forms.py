from django import forms
from .models import ApplicationLoc, ExcelForm


def ch(model,  item):

    choose = [(x.id, getattr(x, item)) for x in model.objects.all()]
    return choose


class AdminApplicationForm(forms.ModelForm):
    raw_materials = forms.ChoiceField(widget=forms.Select, choices=ch(ExcelForm, "raw_material"))
    region_test = forms.ChoiceField(widget=forms.Select, choices=ch(ExcelForm, "region"))

    class Meta:
        model = ApplicationLoc
        fields = '__all__'


