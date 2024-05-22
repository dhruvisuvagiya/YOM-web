from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
from django.http import HttpResponse
from django.core.paginator import Paginator


from layout.models import reg
from layout.models import form
from layout.models import form_offer
from layout.models import form_photos
from layout.models import form_post
from layout.models import form_contact
from layout.models import form_category
from layout.models import add_work
from layout.models import sliderdata
from layout.models import offerdata
from layout.models import photosdata
from layout.models import postdata
from layout.models import workdata
from django.core.mail import send_mail


# Create your views here.

def index(req):
    
    # if 'id' not in req.session:
        # return redirect('/register/')
        
    data=form.objects.filter(Default=1).values()
    data1=form_offer.objects.all().values()
    data2=form_photos.objects.all().values()
    data3=form_post.objects.all().values()[:3]
    
    return render(req,'index.html',{'data':data,'data1':data1,'data2':data2,'data3':data3}) 

def index_2(req):
    return render(req,'index-2.html')

def services(req):
    return render(req,'services.html')

def clients(req):
    return render(req,'clients.html')

def blog(req):
    
    data=form_post.objects.all().values()
    
    return render(req,'blog.html',{'data':data})

def blog_grid(req):
    return render(req,'blog-grid.html')

def blog_single(req,id):
    
    data=form_post.objects.filter(id=id).values()
    # print(data)
 
    # info=data[0]
    # print(info)
    return render(req,'blog-single.html',{'data':data})


def about(req):
    return render(req,'about.html')

def work_3columns(req,id):
    
    data = form_category.objects.all().values()

    if data.count() == 1:
        info = data.get()
        req.session['id']=info.id
        id=req.session['id']

    data1 = form_category.objects.filter(id=id).values()
    # print(data1)

    for x in data1:
        a=(x['Category'])

    if data1.count() == 1:
        data2 = add_work.objects.filter(Category=a).values()
        # print(data2)
    else:
        data2 = add_work.objects.all().values()
        # print(data2)

    return render(req,'work-3columns.html',{'data':data,'data2':data2})

def work_4columns(req):
    return render(req,'work-4columns.html')

def single_project(req):

    data = add_work.objects.all().values()[:3]
    data1 = add_work.objects.all().values()[3:6]

    return render(req,'single-project.html',{'data':data,'data1':data1})

def contact(req):

    if req.method=="POST":

        name=req.POST['nm']
        email=req.POST['em']
        subject=req.POST['sb']
        message=req.POST['msg']

        if name == '' or email == '' or subject == '' or message == '':
            return redirect('/contact')
        else:
            c=form_contact(
                Name=name,
                Email=email,
                Subject=subject,
                Message=message
            )

            c.save()

    return render(req,'contact.html')

def data_contact(req):
    data=form_contact.objects.all().values()
    return render(req,'data_contact.html',{ 'data' : data })

def edit_contact(req,id):
    
    data=form_contact.objects.filter(id=id).get()
    
    if req.method=="POST":
        
        name=req.POST['nm']
        email=req.POST['em']
        subject=req.POST['sb']
        message=req.POST['msg']
        
        data.Name=name
        data.Email=email
        data.Subject=subject
        data.Message=message
        
        data.save()
        return redirect('/data_contact')
    
    return render(req,'contact.html',{'data':data})

def delete_contact(req,id):
    form_contact.objects.filter(id=id).delete()
    return redirect('/data_contact')

def index1(req):
    return render(req,'index1.html')

def login(req):
    
    if req.method=="POST":
        email=req.POST['em']
        password=req.POST['pass']
        
        data=reg.objects.filter(Email = email,Password=password)
        
        if data.count()==1:
            return redirect('/index1')
        else:
            return redirect('/login')
    
    return render(req,'login.html')

def register(req):

    if req.method=="POST":
        
        name=req.POST['nm']
        email=req.POST['em']
        password=req.POST['pass']
        rpassword=req.POST['rpass']
        
        if name!='' and email!='' and password!='' and rpassword!='':
            
            if password!=rpassword:
                return redirect('/register')
            else:
                r=reg(
                    Name=name,
                    Email=email,
                    Password=password
                )
            
                r.save()
                return redirect('/login')
        else:
            return redirect('/register')
    
    return render(req,'register.html')

def forgot_password(req):
    x=''
    y=''
    # id=''
    if req.method == "POST":
        email=req.POST['em']
        
        if email == '':
                y='Please Enter Your Registered Email Id.'
        else:
            data = reg.objects.filter(Email=email)
    
            if data.count() == 1:
                info=data.get()
                req.session['id']=info.id
                return redirect('/recover-password/' + str(info.id))
            else:
                x='The provided email is not associated with any account.'
                
    return render(req,'forgot-password.html',{'x':x,'y':y})

def recover_password(req,id):
    
    id=req.session['id']
    
    if req.method == "POST":
        password=req.POST['ps']
        cpassword=req.POST['cps']
        
        if password != cpassword:
            return redirect('/recover-password/'+ str(id))
        else:
            data = reg.objects.filter(id=id).get()
            data.Password=password
            data.save()
            return redirect('/login')            
    
    return render(req,'recover-password.html') 

def general(req):
    
    frm = sliderdata()
    
    if req.method=="POST":
        
        frm = sliderdata(req.POST,req.FILES)
        frm.save()
        
        # title=req.POST['title']
    #     description=req.POST['des']
    #     url=req.POST['imgurl']
    #     default=req.POST['dv']
        
    #     if title == '' or description == '' or url == '' or  default == '':
    #         return redirect('/general')
    #     else:

    #         f=form(
    #             Title=title, 
    #             Description=description, 
    #             URL=url,
    #             Default=default
    #         )        
            
    #         f.save()
        
    return render(req,'general.html',{"frm":frm})

def data_slider(req):
    data=form.objects.all().values()
    return render(req,'data_slider.html',{'data':data})

def edit_slider(req,id):
    
    data=form.objects.filter(id=id).get()
    form = sliderdata(instance=data)
    
    if req.method == 'POST':
        form = sliderdata(req.POST,req.FILES,instance=data)
        document  = form.save(commit=False)
        document.save()

    # if req.method=="POST":
        
    #     title=req.POST['title']
    #     description=req.POST['des']
    #     img=req.FILES['imgurl']
    #     default=req.POST['dv']
        
    #     data.Title=title
    #     data.Description=description
    #     data.image=img
    #     data.Default=default
        
    #     data.save()
        # return redirect('/data_slider')
    
    return render(req,'general.html',{'data':form})

def delete_slider(req,id):
    form.objects.filter(id=id).delete()
    return redirect('/data_slider/')

def offer_form(req):
    
    form=offerdata()
    
    if req.method=="POST":
        
        form = offerdata(req.POST,req.FILES)
        form.save()
        
        # title=req.POST['title']
        # icon_url=req.POST['iurl']
        # icon_title=req.POST['ititle']
        # description=req.POST['des']
        
        # if title == '' or icon_url == '' or icon_title == '' or description == '':
        #     return redirect('/offer')
        # else:

        #     o=form_offer(
        #         Title=title, 
        #         Icon_URL=icon_url, 
        #         Icon_Title=icon_title,
        #         Description=description, 
        #     )        
            
        #     o.save()
    
    return render(req,'offer.html',{'form':form})

def data_offer(req):
    data=form_offer.objects.all().values()
    return render(req,'data_offer.html',{ 'data' : data })

def edit_offer(req,id):
    
    data=form_offer.objects.filter(id=id).get()
    
    if req.method=="POST":
        
        icon_url=req.POST['iurl']
        icon_title=req.POST['ititle']
        description=req.POST['des']
        
        data.Icon_URL=icon_url
        data.Icon_Title=icon_title
        data.Description=description
        
        data.save()
        return redirect('/data_offer')
    
    return render(req,'offer.html',{'data':data})

def delete_offer(req,id):
    form_offer.objects.filter(id=id).delete()
    return redirect('/data_offer/')
    
def photos_form(req):
    
    form = photosdata()
    
    if req.method=="POST":
        
        form =  photosdata(req.POST,req.FILES)
        form.save()
        
        # title=req.POST['title']
        # image_url=req.POST['iurl']
        # image_title=req.POST['ititle']
        # description=req.POST['des']
        
        # if title == '' or image_url == '' or image_title == '' or description == '':
        #     return redirect('/photos')
        # else:

        #     p=form_photos(
        #         Title=title, 
        #         Image_URL=image_url, 
        #         Image_Title=image_title,
        #         Description=description, 
        #     )        
            
        #     p.save()
    
    return render(req,'photos.html',{'form':form})

def data_photos(req):
    data=form_photos.objects.all().values()
    return render(req,'data_photos.html',{ 'data' : data })

def edit_photos(req,id):
    
    data=form_photos.objects.filter(id=id).get()
    
    if req.method=="POST":
        
        title=req.POST['title']
        image_url=req.POST['iurl']
        image_title=req.POST['ititle']
        description=req.POST['des']
        
        data.Title=title
        data.Image_URL=image_url
        data.Image_Title=image_title
        data.Description=description
        
        data.save()
        return redirect('/data_photos')
    
    return render(req,'photos.html',{'data':data})

def delete_photos(req,id):
    form_photos.objects.filter(id=id).delete()
    return redirect('/data_photos/')

def post_form(req):
    
    form = postdata()
    
    if req.method=="POST":
        
        form = postdata(req.POST,req.FILES)
        form.save()
        
        # image_url=req.POST['iurl']
        # title=req.POST['title']
        # description=req.POST['des']
        
        # if title == '' or description == '' or image_url == '':
        #     return redirect('/post')
        # else:

        #     p=form_post(
        #         Title=title, 
        #         Image_URL=image_url, 
        #         Description=description, 
        #     )        
            
        #     p.save()
    
    return render(req,'post.html',{'form':form})

def data_post(req):
    data=form_post.objects.all().values()
    paginator = Paginator(data, 5) # Display 25 objects per page
    page_number = req.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(req,'data_post.html',{ 'page_obj' : page_obj })

def edit_post(req,id):
    
    data=form_post.objects.filter(id=id).get()
    
    if req.method=="POST":
        
        title=req.POST['title']
        image_url=req.POST['iurl']
        description=req.POST['des']
        
        data.Title=title
        data.Image_URL=image_url
        data.Description=description
        
        data.save()
        return redirect('/data_post')
    
    return render(req,'post.html',{'data':data})

def delete_post(req,id):
    form_post.objects.filter(id=id).delete()
    return redirect('/data_post/')

def category_form(req):
    
    if req.method=="POST":
        
        category=req.POST['ct']
        
        if category == '':
            return redirect('/category')
        else:

            c=form_category(
                Category=category, 
            )        
            
            c.save()
    
    return render(req,'category.html')

def data_category(req):
    data=form_category.objects.all().values()
    return render(req,'data_category.html',{ 'data' : data })

def edit_category(req,id):
    
    data=form_category.objects.filter(id=id).get()
    
    if req.method=="POST":
        
        category=req.POST['ct']
        
        data.Category=category
        
        data.save()
        return redirect('/data_category')
    
    return render(req,'category.html',{'data':data})

def delete_category(req,id):
    form_category.objects.filter(id=id).delete()
    return redirect('/data_category/')

def work_form(req):
    
    form = workdata()
    
    if req.method=="POST":
        
        form = workdata(req.POST,req.FILES)
        form.save()
    
    return render(req,'work.html',{'form':form})

def data_work(req):
    data=add_work.objects.all().values()
    paginator = Paginator(data, 10) # Display 25 objects per page
    page_number = req.POST.get('page')
    page_obj = paginator.get_page(page_number)
    return render(req,'data_work.html',{ 'page_obj' : page_obj, 'data' : data})

def edit_work(req,id):
    
    data=add_work.objects.filter(id=id).get()
    
    if req.method=="POST":
        
        category=req.POST['ct']
        file=req.FILES['fl']
        
        data.Category=category
        data.File=file
        
        data.save()
        return redirect('/data_work')
    
    return render(req,'work.html',{'data':data})

def delete_work(req,id):
    add_work.objects.filter(id=id).delete()
    return redirect('/data_work/')


def getuserdata(request):
    
    user = reg.objects.values()
    
    return JsonResponse({'data':list(user)})

def getsliderdata(req):
    
    user = form.objects.values()
    
    return JsonResponse({'data':list(user[0])})

def getofferdata(req):
    
    user = form_offer.objects.values()
    
    return JsonResponse({'data':list(user)[0]})

def getphotosdata(req):
    
    user = form_photos.objects.values()
    
    return JsonResponse({'data':list(user)[1]})

def getpostdata(req):
    
    user = form_post.objects.values()
    
    return JsonResponse({'data':list(user)[:-1]})

def getcontactdata(req):
    
    user = form_contact.objects.values()
    
    return JsonResponse({'data': list(user)[0]}) 

def getcategorydata(req):
    
    user = form_category.objects.values()
    
    return JsonResponse({'data':list(user)})

def getworkdata(req):
    
    user = add_work.objects.values()
    
    return JsonResponse({'data':list(user)})

def sendmaildata(request):
    
    send_mail(
    'This Creative Message For Testing Purpose',
    'This Meassage Body for Testing....!',
    'dhruvisuvagiya592@gmail.com',
    ['dhruvisuvagiya592@gmail.com'],
    fail_silently=False,
    )
    return HttpResponse("Your Mail Is Send Successfully")

def mailpass(req):
    
    a='1747'
    
    send_mail(
    'Password',
    a,
    'dhruvisuvagiya592@gmail.com',
    ['sarthikpatel1111@gmail.com'],
    fail_silently=False,
    )
    
    if req.method == "POST":
        password=req.POST['ps']
        
        if  password == a:
            return HttpResponse('Correct Password')
        else:
            return HttpResponse('Wrong Password') and redirect('/mail/')
            # return HttpResponse('Wrong Password') and render(req,'mail.html')
                
    return render(req,'mail.html')

def ajaxdata(request):
    return render(request,"ajaxdemo.html")


def get_data(request):
    data = {'message': 'Hello, World!'}
    return JsonResponse(data)

