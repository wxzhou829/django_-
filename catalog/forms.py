from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime #for checking renewal date range.
    
class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="输入一个日期（0-4个星期，默认3个星期）", label='续借日期')

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']
        
        #Check date is not in past. 
        if data < datetime.date.today():
            raise ValidationError(_('非法日期 - 日期太小'))

        #Check date is in range librarian allowed to change (+4 weeks).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('非法日期 - 日期太大'))

        # Remember to always return the cleaned data.
        return data