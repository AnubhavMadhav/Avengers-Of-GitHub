from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests


# Create your views here.

def index(request):
    return render(request, 'avengers/index.html')

def result(request):
    # return render(request, 'avengers/thor.html')
    username = request.POST.get('username')

    url = f'https://api.github.com/users/{username}'
    url2 = url + '/orgs'


    r = requests.get(url.format(username)).json()
    r2 = requests.get(url2.format(username)).json()

    # display_name = ""
    # full_name = ""


    #
    # print("Followers :", r['followers'])
    # print("Repositories (public) :", r['public_repos'])
    # print("No. of Organizations joined :", len(r2))
    # print("Profile Picture URL :", r['avatar_url'] + '.png')

    # print(r2)
    # print("Space")
    # print(r3)



    if username is None:
        params = { 'username': username }
        return render(request, 'error404.html', params)
    else:
        if username == 'AnubhavMadhav':
            full_name = r['name']
            quote = "Anubhav Madhav is the Best."
            params = {'profile_pic': r['avatar_url'] + '.png' , 'full_name': full_name, 'display_name':display_name, 'quote': quote, 'nfolls': r['followers'], 'norgs': len(r2), 'nrepos': r['public_repos'] }
            return render(request, 'avengers/thor.html', params)
        else:
            score = r['followers'] + r['public_repos'] + len(r2)
            if r['name'] is not None:
                display_name = r['name'].strip().split(' ')[0]
                full_name = r['name']
                # print(username)
                # display_name = first_name
                # print("Hello", first_name)
            else:
                # print("Hello", r['login'])
                display_name = r['login']
                full_name = display_name

            if score <= 10:
                quote = "Welcome to the World of GitHub. Seems like you are new to GitHub and if not, then work hard, make some repositories, get some followers and get promoted to a much powerful Avenger."
                params = {'profile_pic': r['avatar_url'] + '.png', 'full_name': full_name, 'display_name': display_name,
                          'quote': quote, 'nfolls': r['followers'], 'norgs': len(r2), 'nrepos': r['public_repos']}
                return render(request, 'avengers/baby-groot.html', params)
            elif score > 10 and score <= 15:
                quote = "Welcome to the World of GitHub. Seems like you are new to GitHub and if not, then work hard, make some repositories, get some followers and become a good Avenger."
                params = {'profile_pic': r['avatar_url'] + '.png', 'full_name': full_name, 'display_name': display_name,
                          'quote': quote, 'nfolls': r['followers'], 'norgs': len(r2), 'nrepos': r['public_repos']}
                return render(request, 'avengers/gamora.html', params)
            elif score > 15 and score <= 20:
                quote = "Welcome to the World of GitHub. Seems like you are new to GitHub and if not, then work hard, make some repositories, get some followers and become a good Avenger."
                params = {'profile_pic': r['avatar_url'] + '.png', 'full_name': full_name, 'display_name': display_name,
                          'quote': quote, 'nfolls': r['followers'], 'norgs': len(r2), 'nrepos': r['public_repos']}
                return render(request, 'avengers/star-lord.html', params)
            elif score > 20 and score <= 25:
                quote = "Welcome to the World of GitHub. Seems like you are new to GitHub and if not, then work hard, make some repositories, get some followers and become a good Avenger."
                params = {'profile_pic': r['avatar_url'] + '.png', 'full_name': full_name, 'display_name': display_name,
                          'quote': quote, 'nfolls': r['followers'], 'norgs': len(r2), 'nrepos': r['public_repos']}
                return render(request, 'avengers/falcon.html', params)
            elif score > 25 and score <= 30:
                quote = "Welcome to the World of GitHub. Seems like you are new to GitHub and if not, then work hard, make some repositories, get some followers and become a good Avenger."
                params = {'profile_pic': r['avatar_url'] + '.png', 'full_name': full_name, 'display_name': display_name,
                          'quote': quote, 'nfolls': r['followers'], 'norgs': len(r2), 'nrepos': r['public_repos']}
                return render(request, 'avengers/winter-soldier.html', params)
            elif score > 30 and score <= 35:
                quote = "Welcome to the World of GitHub. Seems like you are new to GitHub and if not, then work hard, make some repositories, get some followers and become a good Avenger."
                params = {'profile_pic': r['avatar_url'] + '.png', 'full_name': full_name, 'display_name': display_name,
                          'quote': quote, 'nfolls': r['followers'], 'norgs': len(r2), 'nrepos': r['public_repos']}
                return render(request, 'avengers/ant-man.html', params)
            elif score > 35 and score <= 40:
                quote = "Welcome to the World of GitHub. Seems like you are new to GitHub and if not, then work hard, make some repositories, get some followers and become a good Avenger."
                params = {'profile_pic': r['avatar_url'] + '.png', 'full_name': full_name, 'display_name': display_name,
                          'quote': quote, 'nfolls': r['followers'], 'norgs': len(r2), 'nrepos': r['public_repos']}
                return render(request, 'avengers/war-machine.html', params)
            elif score > 40 and score <= 45:
                quote = "Welcome to the World of GitHub. Seems like you are new to GitHub and if not, then work hard, make some repositories, get some followers and become a good Avenger."
                params = {'profile_pic': r['avatar_url'] + '.png', 'full_name': full_name, 'display_name': display_name,
                          'quote': quote, 'nfolls': r['followers'], 'norgs': len(r2), 'nrepos': r['public_repos']}
                return render(request, 'avengers/rocket-raccoon.html', params)
            elif score > 45 and score <= 50:
                quote = "Welcome to the World of GitHub. Seems like you are new to GitHub and if not, then work hard, make some repositories, get some followers and become a good Avenger."
                params = {'profile_pic': r['avatar_url'] + '.png', 'full_name': full_name, 'display_name': display_name,
                          'quote': quote, 'nfolls': r['followers'], 'norgs': len(r2), 'nrepos': r['public_repos']}
                return render(request, 'avengers/groot.html', params)
            elif score > 50 and score <= 55:
                quote = "Welcome to the World of GitHub. Seems like you are new to GitHub and if not, then work hard, make some repositories, get some followers and become a good Avenger."
                params = {'profile_pic': r['avatar_url'] + '.png', 'full_name': full_name, 'display_name': display_name,
                          'quote': quote, 'nfolls': r['followers'], 'norgs': len(r2), 'nrepos': r['public_repos']}
                return render(request, 'avengers/black-panther.html', params)
            elif score > 55 and score <= 60:
                quote = "Welcome to the World of GitHub. Seems like you are new to GitHub and if not, then work hard, make some repositories, get some followers and become a good Avenger."
                params = {'profile_pic': r['avatar_url'] + '.png', 'full_name': full_name, 'display_name': display_name,
                          'quote': quote, 'nfolls': r['followers'], 'norgs': len(r2), 'nrepos': r['public_repos']}
                return render(request, 'avengers/scarlet-witch.html', params)
            elif score > 60 and score <= 70:
                quote = "Welcome to the World of GitHub. Seems like you are new to GitHub and if not, then work hard, make some repositories, get some followers and become a good Avenger."
                params = {'profile_pic': r['avatar_url'] + '.png', 'full_name': full_name, 'display_name': display_name,
                          'quote': quote, 'nfolls': r['followers'], 'norgs': len(r2), 'nrepos': r['public_repos']}
                return render(request, 'avengers/doctor-strange.html', params)
            elif score > 70 and score <= 80:
                quote = "Welcome to the World of GitHub. Seems like you are new to GitHub and if not, then work hard, make some repositories, get some followers and become a good Avenger."
                params = {'profile_pic': r['avatar_url'] + '.png', 'full_name': full_name, 'display_name': display_name,
                          'quote': quote, 'nfolls': r['followers'], 'norgs': len(r2), 'nrepos': r['public_repos']}
                return render(request, 'avengers/spider-man.html', params)
            elif score > 80 and score <= 95:
                quote = "Welcome to the World of GitHub. Seems like you are new to GitHub and if not, then work hard, make some repositories, get some followers and become a good Avenger."
                params = {'profile_pic': r['avatar_url'] + '.png', 'full_name': full_name, 'display_name': display_name,
                          'quote': quote, 'nfolls': r['followers'], 'norgs': len(r2), 'nrepos': r['public_repos']}
                return render(request, 'avengers/captain-marvel.html', params)
            elif score > 95 and score <= 100:
                quote = "Welcome to the World of GitHub. Seems like you are new to GitHub and if not, then work hard, make some repositories, get some followers and become a good Avenger."
                params = {'profile_pic': r['avatar_url'] + '.png', 'full_name': full_name, 'display_name': display_name,
                          'quote': quote, 'nfolls': r['followers'], 'norgs': len(r2), 'nrepos': r['public_repos']}
                return render(request, 'avengers/hawkeye.html', params)
            elif score > 100 and score <= 110:
                quote = "Welcome to the World of GitHub. Seems like you are new to GitHub and if not, then work hard, make some repositories, get some followers and become a good Avenger."
                params = {'profile_pic': r['avatar_url'] + '.png', 'full_name': full_name, 'display_name': display_name,
                          'quote': quote, 'nfolls': r['followers'], 'norgs': len(r2), 'nrepos': r['public_repos']}
                return render(request, 'avengers/black-widow.html', params)
            elif score > 110 and score <= 130:
                quote = "Welcome to the World of GitHub. Seems like you are new to GitHub and if not, then work hard, make some repositories, get some followers and become a good Avenger."
                params = {'profile_pic': r['avatar_url'] + '.png', 'full_name': full_name, 'display_name': display_name,
                          'quote': quote, 'nfolls': r['followers'], 'norgs': len(r2), 'nrepos': r['public_repos']}
                return render(request, 'avengers/hulk.html', params)
            elif score > 130 and score <= 160:
                quote = "Welcome to the World of GitHub. Seems like you are new to GitHub and if not, then work hard, make some repositories, get some followers and become a good Avenger."
                params = {'profile_pic': r['avatar_url'] + '.png', 'full_name': full_name, 'display_name': display_name,
                          'quote': quote, 'nfolls': r['followers'], 'norgs': len(r2), 'nrepos': r['public_repos']}
                return render(request, 'avengers/captain-america.html', params)
            elif score > 160 and score <= 200:
                quote = "Welcome to the World of GitHub. Seems like you are new to GitHub and if not, then work hard, make some repositories, get some followers and become a good Avenger."
                params = {'profile_pic': r['avatar_url'] + '.png', 'full_name': full_name, 'display_name': display_name,
                          'quote': quote, 'nfolls': r['followers'], 'norgs': len(r2), 'nrepos': r['public_repos']}
                return render(request, 'avengers/thor.html', params)
            elif score > 200:
                quote = "Welcome to the World of GitHub. Seems like you are new to GitHub and if not, then work hard, make some repositories, get some followers and become a good Avenger."
                params = {'profile_pic': r['avatar_url'] + '.png', 'full_name': full_name, 'display_name': display_name,
                          'quote': quote, 'nfolls': r['followers'], 'norgs': len(r2), 'nrepos': r['public_repos']}
                return render(request, 'avengers/iron-man.html', params)

