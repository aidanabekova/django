from django import forms

from parser import parser, models, parser2



class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('Anime', 'Anime'),
        ('Zetflix', 'Zetflix'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)
    class Meta:
        fields = [
            'media_type'
        ]

    def parser_data(self):
        if self.data['media_type'] == 'Anime':
            anime_data = parser.parser()
            for i in anime_data:
                models.Film.objects.create(**i)

        elif self.data['media_type'] == 'tvshows':
            zetflix_data = parser2.parser()
            for i in zetflix_data:
                models.Zetflix.objects.create(**i)






