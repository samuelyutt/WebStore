from django import forms

class CustomerCreateForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''

    GENDER_CHOICES = ((0, '先生'), (1, '女士'))

    username = forms.EmailField(label='電子郵件信箱 *')
    password = forms.password = forms.CharField(label='密碼 *', min_length=8, max_length=64, widget=forms.PasswordInput)
    password_confirm = forms.password = forms.CharField(label='確認密碼 *', min_length=8, max_length=64, widget=forms.PasswordInput)
    last_name = forms.CharField(label='姓 *', max_length=20)
    first_name = forms.CharField(label='名 *', max_length=40)
    gender = forms.ChoiceField(choices = GENDER_CHOICES, label='稱謂 *') 
    shipping_postal_code = forms.CharField(label='郵遞區號', max_length=5, required=False)
    shipping_address = forms.CharField(label='收件地址', max_length=200, required=False)
    contact_phone_no = forms.CharField(label='聯絡電話', max_length=20, required=False)





