from django.shortcuts import render
from survey_form.models import Survey
from django.views.generic import TemplateView


def index_form(request):
    if request.method == "POST":
        user_lastname=request.POST["user-lastname"]
        user_name = request.POST["user-name"]
        user_subject = request.POST["user-subject"]
        user_subject_grade=request.POST["subject-grade"]
        user_weight = request.POST["user-weight"]
        user_height = request.POST["user-height"]
        user_age = request.POST["user-age"]
        user_birthdate = request.POST["user-birthdate"]
        user_city_age=request.POST["city-age"]
        user_live_with = request.POST["live-with"]
        user_practice_sport = request.POST["practice-sport"]
        user_sleep_hours = request.POST["sleep-hours"]
        user_extra_act = request.POST["extra-activity-space"]

        Survey.objects.create(
            last_name = user_lastname,
            name = user_name,
            subject=user_subject,
            subject_grade =user_subject_grade,
            weight = user_weight,
            height = user_height,
            age = user_age,
            birthdate = user_birthdate,
            city = user_city_age,
            lives_with = user_live_with,
            phisical_act = user_practice_sport,
            sleep_hours = user_sleep_hours,
            extra_act = user_extra_act
            )

    return render(request, "index.html")

class DashboardView(TemplateView):
    template_name = "dashboard.html"
    
    def get_graph_report_ages(self):
        surveys_data = []
        less_18 = 0
        has_19 = 0
        has_20 = 0
        upper_20 = 0
        surveys = Survey.objects.all()
        for data in surveys.values():
            for key, value in data.items():
                if (key == 'age'):
                    if (value <= 18):
                        less_18 += 1
                    elif (value == 19):
                        has_19 += 1
                    elif (value == 20):
                        has_20 += 1
                    elif (value > 20):
                        upper_20 += 1
        surveys_data.append(less_18)
        surveys_data.append(has_19)
        surveys_data.append(has_20)
        surveys_data.append(upper_20)
        return surveys_data

    def normalize(self,s):
        replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
        )
        for a, b in replacements:
            s = s.replace(a, b).replace(a.upper(), b.upper())
        return s

    def get_line_report_city(self):
        surveys_data = []
        barbosa = 0
        chiquinquira = 0
        cucuta = 0
        duitama = 0
        paipa = 0
        samaca = 0
        tunja = 0
        ventaquemada = 0
        surveys = Survey.objects.all()
        for data in surveys.values():
            for key, value in data.items():
                if (key == 'city'):
                    value = self.normalize(value.upper())
                    if 'BARBOSA' in value:
                        barbosa += 1
                    elif 'CHIQUINQUIRA' in value:
                        chiquinquira += 1
                    elif 'CUCUTA' in value:
                        cucuta += 1
                    elif 'DUITAMA' in value:
                        duitama += 1
                    elif 'PAIPA' in value:
                        paipa += 1
                    elif 'SAMACA' in value:
                        samaca += 1
                    elif 'TUNJA' in value:
                        tunja += 1
                    elif 'VENTAQUEMADA' in value:
                        ventaquemada += 1

        surveys_data.append(barbosa)
        surveys_data.append(chiquinquira)
        surveys_data.append(cucuta)
        surveys_data.append(duitama)
        surveys_data.append(paipa)
        surveys_data.append(samaca)
        surveys_data.append(tunja)
        surveys_data.append(ventaquemada)
        return surveys_data

    def get_lives_report(self):
        surveys_data = []
        first_family = 0
        mom = 0
        dad = 0
        brother = 0
        second_family = 0
        second_first_family = 0
        alone = 0
        surveys = Survey.objects.all()
        for data in surveys.values():
            for key, value in data.items():
                if (key == 'lives_with'):
                    if(value=='first-family'):
                        first_family+=1   
                    elif(value=='mom'):
                        mom+=1
                    elif(value=='dad'):
                        dad+=1
                    elif(value=='brother'):
                        brother+=1
                    elif(value=='second-family'):
                        second_family+=1
                    elif(value=='second-first-family'):    
                        second_first_family+=1  
                    elif(value=='alone'): 
                        alone+=1        
        total = len(surveys)
        surveys_data = [{
                    'name': 'Familia primaria',
                    'y': round((first_family*100)/total,2)
                }, {
                    'name': 'Mamá',
                    'y': round((mom*100)/total,2)
                }, {
                    'name': 'Papá',
                    'y': round((dad*100)/total,2)
                }, {
                    'name': 'Hermanos',
                    'y': round((brother*100)/total,2)
                }, {
                    'name': 'Familia secundaria',
                    'y': round((second_family*100)/total,2)
                }, {
                    'name': 'Familia primaria y secundaria',
                    'y': round((second_first_family*100)/total,2)
                },{
                    'name': 'Solo',
                    'y': round((alone*100)/total,2)
                }]
        return surveys_data
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["report_ages"] = self.get_graph_report_ages()
        context["city_report"] = self.get_line_report_city()
        context["report_lives"] = self.get_lives_report()
        return context
