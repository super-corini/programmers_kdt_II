from json.decoder import JSONDecodeError

from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework.exceptions import ParseError

from .models import Game
from .forms import GameForm
from .serializers import GameSerializer

# Create your views here.
def index(request) :
    return render(request, 'index.html', {})

@csrf_exempt
def game_view(request) :
    game_query_set = Game.objects.all()
    game_cols = ['id', 'Title', 'Platform', 'Genre', 'Price', 'Stock', 'Reserved', 'Extinct']

    game_form = GameForm()
    table_view = True

    is_json = True
    valid_ok = False
    d_container = None

    # 이유는 모르겠지만 request.POST를 한번 호출하지 않으면 html form 데이터가 반영되지 않음
    post_form = request.POST    

    # Create
    if request.method == 'POST' :
        try :
            json_data = JSONParser().parse(request)
        except (JSONDecodeError, ParseError) :
            json_data = {}
            is_json = False

        if is_json : # POST Data to JSON
            serializer = GameSerializer(data = json_data)
            if serializer.is_valid() :
                input_title = json_data['title']
                input_platform = json_data['platform']
                valid_ok = True
                d_container = serializer
            else :  # JSON Valid False
                return JsonResponse(serializer.errors, status = 400)

        else :      # POST data to Form
            form = GameForm(request.POST)
            if form.is_valid() :
                input_title = form.cleaned_data['title']
                input_platform = form.cleaned_data['platform']
                valid_ok = True
                d_container = form
            else :
                for e_message in form.errors.values() :
                    messages.error(request, e_message)

        if valid_ok and d_container :
            if len(Game.objects.filter(title=input_title, platform=input_platform)) == 0 :
                d_container.save()
            else :
                error_message = '{} ({}) is already exist'.format(input_title, input_platform)
                
                if is_json :
                    return JsonResponse({"Error" : error_message}, status=400)
                else :
                    messages.error(request, error_message)
                    game_form = form

    return render(request, 'game.html', 
        {'game_list' : game_query_set, 'table_view' : table_view, 'game_form':game_form, 'game_cols': game_cols})

@csrf_exempt
def game_ud(request, id) :
    obj = Game.objects.get(id=id)

    # Update
    if request.method == 'PUT' :
        json_data = JSONParser().parse(request)
        serializer = GameSerializer(obj, data = json_data)
        if serializer.is_valid() :
            serializer.save()
        else :
            return JsonResponse(serializer.errors, status=400)

    # Delete
    elif request.method == 'DELETE' :
        obj.delete()

    # Read One Object 
    elif request.method == 'GET' :
        serializer = GameSerializer(obj)
        return JsonResponse(serializer.data, safe=False)
    else :
        return JsonResponse({'message' : 'Bad Request'}, status=400)

    return redirect('/games')
