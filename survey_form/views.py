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
        data = [15,32,17,25]
        try:
            less_20 = Survey.objects.filter(age=20)
        except:
            pass
        
        return data
    
    def get_line_report_city(self):
        data = [1,1,1,1,2,1,73,1]
        try:
            Ciudades = Survey.objects.filter(city="Tunja")
        except:
            pass
        
        return data
    
    def get_lives_report(self):
        data = [1,1,1,1,2,1,73,1]
        try:
            Ciudades = Survey.objects.filter(city="Tunja")
        except:
            pass
        
        return data
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["report_ages"] = self.get_graph_report_ages()
        context["city_report"] = self.get_line_report_city()
        context["report_lives"] = self.get_lives_report()
        return context
