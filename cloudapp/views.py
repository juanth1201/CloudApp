# -*- coding: utf-8 -*-
from distutils.errors import LinkError
from django.shortcuts import render, redirect
import fsutil
import requests as re
from cloudRepo.settings import BASE_DIR
import pdb
# Create your views here.

def main_view(request, directory):
    if '-' in directory:#folders names are separated by - 
        directory = directory.replace('-','\\')# - are changed for \\ so the path can be find using fsutil 
    BS_DIR = str(BASE_DIR) + '\\' + directory#Base dir(containing manage.py) + directory requested 
    dir = fsutil.list_dirs(BS_DIR)#full directory list
    final_dir_list = []
    aux = len(request.path)
    cont = 1
    path_aux = ""#gets the name of every folder
    url_aux = ""#gets link of every folder 
    url_list = []#list containing the links to folders, for the folder tree
    path_list = []#list containing the names of the folders, for the folder tree
    path_dict = {}
    for i in request.path:#this loops through de path, so every directory can be extracted for the navigation bar, path does not give me any URL related info
        if i == '-' or cont == aux:#in case - is found, the directory is added to a list, the last condition is useful when the loop reaches the last character because that's the only way the last directory can be added to the list
            url_aux = url_aux + i#variable that will help to fill the list with the urls for the links in the front-end
            url_list.append('http://127.0.0.1:8000' + url_aux)#list of urls
            if '/home/cloud/' in path_aux:#this is important because the root folder is HOME not home/cloud which are part of the django urls, so path_list in this position is set to home, so it can be seen properly in the botton
                path_list.append('HOME')
            else:
                path_aux = path_aux + i
                path_list.append(path_aux)
            path_aux = ""
        else:
            path_aux = path_aux + i
            url_aux = url_aux + i
        cont += 1
    aux = ""
    for i,j in zip(url_list, path_list):#dict with links and names
        if i[-1] == '-':#condition to take - out of the urls
            i = i[:-1]
        if '-' in j:#condition to take - out of the names
            j = j.replace('-', '')
        path_dict[i] = j
    for i in dir:
        aux = i.replace(str(BS_DIR), '')
        aux = aux[1:]
        final_dir_list.append(aux)#dict filled with the root to the folders rendered, used to edit or delete folder
        aux = ""
    if request.method == 'POST':
        if 'new_folder' in request.POST:
            fsutil.create_dir((BS_DIR + '\\' + request.POST['folder_name']), overwrite=False)
            return redirect('http://127.0.0.1:8000' + request.path)
        elif 'delete' in request.POST:
            fsutil.delete_dir(BS_DIR + '\\' + request.POST['folder_to_delete'])
            return redirect('http://127.0.0.1:8000' + request.path)
        elif 'edit_name' in request.POST:
            fsutil.rename_dir((BS_DIR + '\\' + request.POST['previous_name']), request.POST['new_name'])
            return redirect('http://127.0.0.1:8000' + request.path)
    context = {
        'dir' : final_dir_list,# list of folders to be maped
        'urls': url_list,
        'names': path_dict
    }
    return render(request, 'home.html', context)
