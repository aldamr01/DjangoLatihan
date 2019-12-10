from django import forms


class MahasiswaCreateForm(forms.Form):
    class Meta:
        fields = ('nama', 'email', 'nik',)
    

    nama = forms.CharField()