from django.forms import ModelForm
from .models import Post,Coment,Author



class CreatePostViewForm(ModelForm):
    class Meta:
        model =  Post
        exclude = ["post_time","post_update_time"]

class DeletePostViewForm(ModelForm):
    class Meta:
        model =  Post
        fields = "__all__"


class ModifyPostViewForm(ModelForm):
    class Meta:
        model =  Post
        fields = "__all__"


class ComentViewForm(ModelForm):
    class Meta:
        model = Coment
        exclude = ["post_time","post_update_time","post","author"]