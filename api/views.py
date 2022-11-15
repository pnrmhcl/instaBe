import requests
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from insta_be.responses import response_200, response_400


@api_view(['GET'])
@permission_classes([AllowAny])
def get_user(request):
    fields = "id, username, account_type,media_count"
    access_token = request.data['access_token']
    path = "https://graph.instagram.com/me?fields=" + fields + "&access_token=" + access_token
    response = requests.get(path)
    response_dict = response.json()
    return response_200(data=response_dict)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_user_media(request):
    access_token = request.data['access_token']
    user_id = "https://graph.instagram.com/me?fields=" + "id" + "&access_token=" + access_token
    user_id_response = requests.get(user_id)
    user_id_response_dict = user_id_response.json()
    a = user_id_response_dict.values()
    ls = []
    for obj in a:
        ls.append(obj)
    path = "https://graph.instagram.com/v15.0/" + ls[0] + "/media?access_token=" + access_token
    response = requests.get(path)
    response_dict = response.json()
    pm = []
    for obj in response_dict["data"]:
        pm.append(obj)
    lm = []
    sm = []
    for obj in pm:
        lm.append(list(obj.values()))
    for media_id in lm:
        media_path = "https://graph.instagram.com/" + media_id[
            0] + "?fields=id,media_type,media_url,username,caption,timestamp&access_token=" + access_token
        media_path_response = requests.get(media_path)
        media_path_response_dict = media_path_response.json()
        sm.append(media_path_response_dict)
    return response_200(data=sm)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_single_media(request, media_id):
    access_token = request.data['access_token']
    user_id = "https://graph.instagram.com/me?fields=" + "id" + "&access_token=" + access_token
    user_id_response = requests.get(user_id)
    user_id_response_dict = user_id_response.json()
    a = user_id_response_dict.values()
    ls = []
    for obj in a:
        ls.append(obj)
    medias = "https://graph.instagram.com/v15.0/" + ls[0] + "/media?access_token=" + access_token
    response = requests.get(medias)
    response_dict = response.json()
    pm = []
    for obj in response_dict["data"]:
        pm.append(obj)
    lm = []
    for obj in pm:
        lm.append(list(obj.values()))
    path = "https://graph.instagram.com/" + str(
        media_id) + "?fields=id,media_type,media_url,username,caption,timestamp" + "&access_token=" + access_token
    path_response = requests.get(path)
    path_response_dict = path_response.json()
    sm = []
    for object in lm:
        if object[0] == str(media_id):
            sm.append(media_id)
    if len(sm) == 0:
        return response_400()
    return response_200(data=path_response_dict)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_user_media_count(request):
    fields = "id, media_count"
    access_token = request.data['access_token']
    path = "https://graph.instagram.com/me?fields=" + fields + "&access_token=" + access_token
    response = requests.get(path)
    response_dict = response.json()
    return response_200(data=response_dict)
