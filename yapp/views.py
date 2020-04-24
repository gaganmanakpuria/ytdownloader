from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import youtube_dl
import subprocess
from .models import ydl,videos
from django.contrib.auth.models import User
from django.contrib.auth import login ,logout,authenticate
from django.conf import settings
from django.contrib.auth.decorators import login_required
import os.path
import pafy

# Create your views here.

def index(r):
    if r.method=="POST":
        # print(r.POST)
        global TXT
        TXT=r.POST['ytxt']
        media_path = settings.MEDIA_ROOT
        nm=pafy.new(TXT).title
        if " " in nm:
            nm=nm.replace(" ","_")
        nm=nm[:10]+".mp4"
        
        commands="youtube-dl -o "+nm+" " +TXT
        
        # pa = os.path.expanduser("~")+"/Downloads"
        # pa=str(pa)
        # pa= pa.replace("\\" , "/" )
        # print(pa)

        subprocess.check_output(commands,shell=True,cwd=media_path)
        # k=videos(av=a)
        # k.save()
        
        # print("DONE")
       
        return HttpResponseRedirect("down/{}".format(nm))

    return render(r,"home.html")



def contactview(r):
    return render(r,'contact.html')

def user_login(r):
    if r.method=="POST":
        un=r.POST['uname']
        pwd=r.POST['psd']
        user=authenticate(username=un,password=pwd)
        if user:
            login(r,user)
            return HttpResponseRedirect("/admin")
        else:
            return render(r,"home.html")
    else:
        return render(r,'home.html')

@login_required
def user_logout(r):
    logout(r)
    return HttpResponseRedirect("/")



def down(r,nm):
    
    # media_path = settings.MEDIA_ROOT
    # a=subprocess.check_output("dir /o-d /t:c " ,shell=True,cwd=media_path).decode()
    # b=a.split("\n")

    # li=[]
    # for i in range(len(b)):
    #     if len(b[i][28:])==0:
    #         pass
    #     else:
                    
    #         li.append(b[i][28:])
    # d=[]
    # for j in range(2,len(li)):
    #     d.append(li[j])
    # st = d[0].split(" ")[-1]
    
    # media_path = settings.MEDIA_ROOT
    # print(media_path)
    # nm=pafy.new(txt).title
    # nm=nm[:10]+".mp4"
    # if " " in nm:
    #     nm=nm.replace(" ","_")
    st=nm
    if r.method=="POST":
        media_path = settings.MEDIA_ROOT
        os.remove(media_path+"/"+st)
        return redirect("home")   
    
    print(st)
    dic={"status":st}
    return render(r,"down.html",dic)