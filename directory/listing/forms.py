from django import forms
from .models import article
from .models import linkimp
from .models import linkmid
from .models import link 
from .models import contact

class articles(forms.ModelForm):
    class Meta:
        model=article
        fields={'name','domain','title','body',}
class linkimps(forms.ModelForm):
    class Meta:
        model=linkimp
        fields={'title','url','description','mkeyword','mdescription','name','email','category','reciprocal',}

class linkmids(forms.ModelForm):
    class Meta:
        model=linkmid
        fields={'title','url','description','mkeyword','mdescription','name','email','category','reciprocal',}

class links(forms.ModelForm):
    class Meta:
        model=link
        fields={'title','url','description','mkeyword','mdescription','name','email','category','reciprocal',}

class contacts(forms.ModelForm):
    class Meta:
        model=contact
        fields={'name','email','message',}
