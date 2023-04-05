from django import forms
class ModelForm(forms.Form):
   tenth = forms.IntegerField(max_value=100,min_value=0,label="What was your 10th percentage ?")
   eleventh = forms.IntegerField(max_value=100,min_value=0,label="What was your 11th percentage ?")
   twelfth = forms.IntegerField(max_value=100,min_value=0,label="What was your 12th percentage ?")
   guidance = forms.BooleanField(label="Did you have additional guidance ?")
   EvsI1 = forms.BooleanField(label="Too much socializing drains your energy  ?")
   EvsI2 = forms.BooleanField(label="The more you interact with others, the more energized you feel ?")
   EvsI3 = forms.BooleanField(label="It usually takes you a long time to open up with new people you meet ?")
   SvsI1 = forms.BooleanField(label="You prefer to work your way through a situation rather than plan out all the details ?")
   SvsI2 = forms.BooleanField(label="You rely on your mind rather than your feelings to make decisions ?")
   SvsI3 = forms.BooleanField(label="According to you, It's important to try things out for yourself. ?")
   TvsF1 = forms.BooleanField(label="You'll take time to think about improving each situation ?")
   TvsF2 = forms.BooleanField(label=" Expressing your feelings comes naturally to you ?")
   TvsF3 = forms.BooleanField(label="Using sound(good) logic is how you deal with problems ?")
   JvsP1 = forms.BooleanField(label="You trust your personal experience rather than other people's theories ?")
   JvsP2 = forms.BooleanField(label="You can usually foresee several possible outcomes for the present situation ?")
   JvsP3 = forms.BooleanField(label="You find it useful when people offer criticism of your work ?")
   