from django import forms

def check_for_s(value):
    if value[0].lower()=='s':
        raise forms.ValidationError('started with s')

def check_for_len(value):
    if len(value)<5:
        raise forms.ValidationError('len is < 5')
from django.core import validators


class StudentForm(forms.Form):
    Sname=forms.CharField(max_length=100,validators=[check_for_s,validators.MinLengthValidator(5)])
    Sage=forms.IntegerField()
    Sid=forms.IntegerField()
    Semail=forms.EmailField(validators=[check_for_s])
    Remail=forms.EmailField()
    mobile=forms.CharField(min_length=10,max_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])
    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)


    def clean(self):
        e=self.cleaned_data['Semail']
        r=self.cleaned_data['Remail']
        if e!=r:
            raise forms.ValidationError('emails not matched')
    
    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']
        if len(bot)>0:
            raise forms.ValidationError('bot')
        











