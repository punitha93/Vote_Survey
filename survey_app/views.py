from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404
from .models import election_survey_details, results_partynames

def survey_details (request):
    if request.method == "GET":
        return render(request,'post_survey.html')
    
    elif request.method == "POST":            
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        gender = request.POST['gender']
        dob = request.POST['dob']
        city = request.POST['city']
        party_name = request.POST['party_name']

        obj = election_survey_details(first_name=firstname,last_name=lastname,gender=gender,dob=\
                                      dob,city=city,party_name=party_name)
        obj.save()
        obj, created = results_partynames.objects.get_or_create(party_name=party_name, defaults={'vote_count':0})
        if created:
            x = results_partynames.objects.get(party_name=party_name)
            x.vote_count=1
            x.save()
        else:
            x = results_partynames.objects.get(party_name=party_name)
            x.vote_count += 1
            x.save()
            
            # x = int(results_partynames.objects.get(party_name=party_name).vote_count)
            # results_partynames.objects.filter(party_name=party_name).update(vote_count=x+1)               
        return redirect('/survey/results/')
    else:
        print("No valid request")
    
def survey_result(request):
    if request.method == "GET":
        results = results_partynames.objects.values()
        return render(request,'survey_results.html',{"results":results})