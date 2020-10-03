from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests


# Create your views here.

def index(request):
    return render(request, 'avengers/index.html')

def result(request):

    username = request.POST.get('username')

    url = f'https://api.github.com/users/{username}'
    url2 = url + '/orgs'


    r = requests.get(url.format(username)).json()
    r2 = requests.get(url2.format(username)).json()




    #
    # print("Followers :", r['followers'])
    # print("Repositories (public) :", r['public_repos'])
    # print("No. of Organizations joined :", len(r2))
    # print("Profile Picture URL :", r['avatar_url'] + '.png')

    # print(r)

    # print(r3)



    if len(r) == 2:
        params = { 'username': username }
        return render(request, 'error404.html', params)
    else:
        if username == 'AnubhavMadhav':
            full_name = r['name']
            display_name = r['name'].strip().split(' ')[0]
            quote = "You are the Strongest. You have the ability to do whatever you want. You are the master of all."
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
                quote = " You use a wide variety of tools and seek to master in many programming languages."
                params = {'profile_pic': r['avatar_url'] + '.png', 'full_name': full_name, 'display_name': display_name,
                          'quote': quote, 'nfolls': r['followers'], 'norgs': len(r2), 'nrepos': r['public_repos']}
                return render(request, 'avengers/gamora.html', params)
            elif score > 15 and score <= 20:
                quote = "You are really helpful to your teammates or colleagues. You enjoy music a lot."
                params = {'profile_pic': r['avatar_url'] + '.png', 'full_name': full_name, 'display_name': display_name,
                          'quote': quote, 'nfolls': r['followers'], 'norgs': len(r2), 'nrepos': r['public_repos']}
                return render(request, 'avengers/star-lord.html', params)
            elif score > 20 and score <= 22:
                quote = "You are highly skilled, and deserve to be on the top."
                params = {'profile_pic': r['avatar_url'] + '.png', 'full_name': full_name, 'display_name': display_name,
                          'quote': quote, 'nfolls': r['followers'], 'norgs': len(r2), 'nrepos': r['public_repos']}
                return render(request, 'avengers/falcon.html', params)
            elif score > 22 and score <= 25:
                quote = "You are analytical, thoughtful, reserved and polite. You prefer to think through all possible directions and then follow the most logical path. Maybe you're good at Algorithms. "
                params = {'profile_pic': r['avatar_url'] + '.png', 'full_name': full_name, 'display_name': display_name,
                          'quote': quote, 'nfolls': r['followers'], 'norgs': len(r2), 'nrepos': r['public_repos']}
                return render(request, 'avengers/vision.html', params)
            elif score > 25 and score <= 30:
                quote = "You have a strong sense of justice and honor. You are known for your loyalty and bravery."
                params = {'profile_pic': r['avatar_url'] + '.png', 'full_name': full_name, 'display_name': display_name,
                          'quote': quote, 'nfolls': r['followers'], 'norgs': len(r2), 'nrepos': r['public_repos']}
                return render(request, 'avengers/winter-soldier.html', params)
            elif score > 30 and score <= 35:
                quote = "You are laser focused on what you are good at. You always give a positive association to pursue your goals in life."
                params = {'profile_pic': r['avatar_url'] + '.png', 'full_name': full_name, 'display_name': display_name,
                          'quote': quote, 'nfolls': r['followers'], 'norgs': len(r2), 'nrepos': r['public_repos']}
                return render(request, 'avengers/ant-man.html', params)
            elif score > 35 and score <= 40:
                quote = "You are a very nice human, and a very good friend as well. You are known for your loyalty and bravery."
                params = {'profile_pic': r['avatar_url'] + '.png', 'full_name': full_name, 'display_name': display_name,
                          'quote': quote, 'nfolls': r['followers'], 'norgs': len(r2), 'nrepos': r['public_repos']}
                return render(request, 'avengers/war-machine.html', params)
            elif score > 40 and score <= 45:
                quote = "You are fond of learning many programming languages and frameworks. You’re aggressive, meanwhile wisecracking."
                params = {'profile_pic': r['avatar_url'] + '.png', 'full_name': full_name, 'display_name': display_name,
                          'quote': quote, 'nfolls': r['followers'], 'norgs': len(r2), 'nrepos': r['public_repos']}
                return render(request, 'avengers/rocket-raccoon.html', params)
            elif score > 45 and score <= 50:
                quote = "You are a kind human with a fierce heart. You have a talent to say a lot, by saying a little."
                params = {'profile_pic': r['avatar_url'] + '.png', 'full_name': full_name, 'display_name': display_name,
                          'quote': quote, 'nfolls': r['followers'], 'norgs': len(r2), 'nrepos': r['public_repos']}
                return render(request, 'avengers/groot.html', params)
            elif score > 50 and score <= 55:
                quote = "You are fearless and respect equality. You are known for your Integrity and Self-Control."
                params = {'profile_pic': r['avatar_url'] + '.png', 'full_name': full_name, 'display_name': display_name,
                          'quote': quote, 'nfolls': r['followers'], 'norgs': len(r2), 'nrepos': r['public_repos']}
                return render(request, 'avengers/black-panther.html', params)
            elif score > 55 and score <= 60:
                quote = "You are very strong at times. You are an introverted individual with emotional fragility and caring personality."
                params = {'profile_pic': r['avatar_url'] + '.png', 'full_name': full_name, 'display_name': display_name,
                          'quote': quote, 'nfolls': r['followers'], 'norgs': len(r2), 'nrepos': r['public_repos']}
                return render(request, 'avengers/scarlet-witch.html', params)
            elif score > 60 and score <= 70:
                quote = "You’re capable of more than you think. You are known for your selflessness."
                params = {'profile_pic': r['avatar_url'] + '.png', 'full_name': full_name, 'display_name': display_name,
                          'quote': quote, 'nfolls': r['followers'], 'norgs': len(r2), 'nrepos': r['public_repos']}
                return render(request, 'avengers/doctor-strange.html', params)
            elif score > 70 and score <= 80:
                quote =  "'With Great Powers comes Great Responsibilities!!' You never misuse your powers. And, you live your life for the betterment of humankind."
                params = {'profile_pic': r['avatar_url'] + '.png', 'full_name': full_name, 'display_name': display_name,
                          'quote': quote, 'nfolls': r['followers'], 'norgs': len(r2), 'nrepos': r['public_repos']}
                return render(request, 'avengers/spider-man.html', params)
            elif score > 80 and score <= 95:
                quote = "You are a Human of Action. Very powerful. You’re an Assertive Entertainer as well."
                params = {'profile_pic': r['avatar_url'] + '.png', 'full_name': full_name, 'display_name': display_name,
                          'quote': quote, 'nfolls': r['followers'], 'norgs': len(r2), 'nrepos': r['public_repos']}
                return render(request, 'avengers/captain-marvel.html', params)
            elif score > 95 and score <= 100:
                quote = "You are a bit cocky and very confident in yourself. You have an Observant Personality and a Logical Thinking."
                params = {'profile_pic': r['avatar_url'] + '.png', 'full_name': full_name, 'display_name': display_name,
                          'quote': quote, 'nfolls': r['followers'], 'norgs': len(r2), 'nrepos': r['public_repos']}
                return render(request, 'avengers/hawkeye.html', params)
            elif score > 100 and score <= 110:
                quote = "You are Fearless. You are confident in both, your Beauty and Intelligence."
                params = {'profile_pic': r['avatar_url'] + '.png', 'full_name': full_name, 'display_name': display_name,
                          'quote': quote, 'nfolls': r['followers'], 'norgs': len(r2), 'nrepos': r['public_repos']}
                return render(request, 'avengers/black-widow.html', params)
            elif score > 110 and score <= 130:
                quote = "You are a Genius. You have an ability to make decisions based on morality. You are known for your expertise in multiple scientific fields."
                params = {'profile_pic': r['avatar_url'] + '.png', 'full_name': full_name, 'display_name': display_name,
                          'quote': quote, 'nfolls': r['followers'], 'norgs': len(r2), 'nrepos': r['public_repos']}
                return render(request, 'avengers/hulk.html', params)
            elif score > 130 and score <= 160:
                quote = "'You can do this all day!!' You have abilities to do anything you want. You are known for your justice, fairness and individualism."
                params = {'profile_pic': r['avatar_url'] + '.png', 'full_name': full_name, 'display_name': display_name,
                          'quote': quote, 'nfolls': r['followers'], 'norgs': len(r2), 'nrepos': r['public_repos']}
                return render(request, 'avengers/captain-america.html', params)
            elif score > 160 and score <= 200:
                quote = "You have powers and abilities far greater than others. You are known for your honesty and courage. Moreover, you are a Man of Instincts."
                params = {'profile_pic': r['avatar_url'] + '.png', 'full_name': full_name, 'display_name': display_name,
                          'quote': quote, 'nfolls': r['followers'], 'norgs': len(r2), 'nrepos': r['public_repos']}
                return render(request, 'avengers/thor.html', params)
            elif score > 200:
                quote = "'I am Iron Man!!', suits to you. You are the best of all. You have a nature of never giving up. You are known for your perseverance, and are loved by all."
                params = {'profile_pic': r['avatar_url'] + '.png', 'full_name': full_name, 'display_name': display_name,
                          'quote': quote, 'nfolls': r['followers'], 'norgs': len(r2), 'nrepos': r['public_repos']}
                return render(request, 'avengers/iron-man.html', params)

