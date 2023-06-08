
from django.shortcuts import render
import mysql.connector
from django.contrib import messages

from django.shortcuts import render_to_response
from django.conf import settings
import os
from django.conf import settings
from django.http import HttpResponse, Http404
import mimetypes
from django.core.files.storage import FileSystemStorage





    
    
def home(request):
    return render(request,'index.html')
################    
def adminhome(request): 
    return render(request,'adminhome.html')      
def adminlogin(request):
    return render(request,'adminlogin.html')
def adminloginvalidator(request):
    m=request.GET.get("username")
    n=request.GET.get("password")
    if(m == "Admin" and n =="Admin"):
        request.session['sname']=m
        return render(request,'adminhome.html')
    else:
        return render(request,'adminlogin.html',{'message': 'Invalid Credentials'})
def adminaddmember(request):
    return render(request,'adminaddmember.html')
def adminviewmember(request):
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="healthcarenourishmentdb")
    mycursor=mydb.cursor()
    bc="select * from fcm_members"
    print(bc)
    cd=mycursor.execute(bc)
    rows=mycursor.fetchall()
    print(rows)
    return render(request,'adminviewmember.html',{'rowf':rows})    
def deletememberhandler(request):
    memberid=request.POST.get("memberid")
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="healthcarenourishmentdb")
    mycursor=mydb.cursor()
    try:
     mn="update fcm_members set status='deleted' where userid="+memberid
     print(mn)
     mycursor.execute(mn)
     mydb.commit()
     bc="select * from fcm_members"
     print(bc)
     cd=mycursor.execute(bc)
     rows=mycursor.fetchall()
     print(rows)
     return render(request,'adminviewmember.html',{'rowf':rows})     
    except:
     bc="select * from fcm_members"
     print(bc)
     cd=mycursor.execute(bc)
     rows=mycursor.fetchall()
     print(rows)
     return render(request,'adminviewmember.html',{'rowf':rows,'message':'There is some issue. Try after some time.'})   
def adminviewtrainer(request):
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="healthcarenourishmentdb")
    mycursor=mydb.cursor()
    bc="select * from fcm_trainer"
    print(bc)
    cd=mycursor.execute(bc)
    rows=mycursor.fetchall()
    print(rows)
    return render(request,'adminviewtrainer.html',{'rowf':rows})   
def approvetrainerhandler(request):
    trainerid=request.POST.get("trainerid")
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="healthcarenourishmentdb")
    mycursor=mydb.cursor()
    try:
     mn="update fcm_trainer set status='active' where userid="+trainerid
     print(mn)
     mycursor.execute(mn)
     mydb.commit()
     bc="select * from fcm_trainer"
     print(bc)
     cd=mycursor.execute(bc)
     rows=mycursor.fetchall()
     print(rows)
     return render(request,'adminviewtrainer.html',{'rowf':rows})  
    except:
     bc="select * from fcm_trainer"
     print(bc)
     cd=mycursor.execute(bc)
     rows=mycursor.fetchall()
     print(rows)
     return render(request,'adminviewtrainer.html',{'rowf':rows,'message':'There is some issue. Try after some time.'})
def deletetrainerhandler(request):
    trainerid=request.POST.get("trainerid")
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="healthcarenourishmentdb")
    mycursor=mydb.cursor()
    try:
     mn="update fcm_trainer set status='deleted' where userid="+trainerid
     print(mn)
     mycursor.execute(mn)
     mydb.commit()
     bc="select * from fcm_trainer"
     print(bc)
     cd=mycursor.execute(bc)
     rows=mycursor.fetchall()
     print(rows)
     return render(request,'adminviewtrainer.html',{'rowf':rows})  
    except:
     bc="select * from fcm_trainer"
     print(bc)
     cd=mycursor.execute(bc)
     rows=mycursor.fetchall()
     print(rows)
     return render(request,'adminviewtrainer.html',{'rowf':rows,'message':'There is some issue. Try after some time.'})     
def adminadddietplan(request):
    return render(request,'adminadddietplan.html')     
def adddietplanhandler(request):
    
    name=request.POST.get("name")
    path="fcmsweb\\static\\dietplans"
    file = request.FILES['myfile']
    fs = FileSystemStorage(location=path)
    filename = fs.save(file.name, file)
    uploaded_file_url = fs.url(filename)
    
    category=request.POST.get("category")
    details=request.POST.get("details")
    from datetime import datetime
    uploaddate=str(datetime.date(datetime.now()))
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="healthcarenourishmentdb")
    mycursor=mydb.cursor()
    try:
     mn="INSERT INTO fcm_dietplans(name,category,details,imagename,date)VALUES('"+name+"','"+category+"','"+details+"','"+filename+"','"+uploaddate+"')"
     print(mn)
     mycursor.execute(mn)
     mydb.commit()
     return render(request,'adminadddietplan.html',{'message': 'Successfully Added.'})
    except:
     return render(request,'adminadddietplan.html',{'message': 'Some issue. Try after some time.'})      
def adminviewdientplan(request):
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="healthcarenourishmentdb")
    mycursor=mydb.cursor()
    bc="select * from fcm_dietplans"
    print(bc)
    cd=mycursor.execute(bc)
    rows=mycursor.fetchall()
    print(rows)
    return render(request,'adminviewdientplan.html',{'rowf':rows}) 
def deletedietplanhandler(request):
    dietplanid=request.POST.get("dietplanid")
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="healthcarenourishmentdb")
    mycursor=mydb.cursor()
    try:
     mn="update fcm_dietplans set status='deleted' where dientno="+dietplanid
     print(mn)
     mycursor.execute(mn)
     mydb.commit()
     bc="select * from fcm_dietplans"
     print(bc)
     cd=mycursor.execute(bc)
     rows=mycursor.fetchall()
     print(rows)
     return render(request,'adminviewdientplan.html',{'rowf':rows})  
    except:
     bc="select * from fcm_dietplans"
     print(bc)
     cd=mycursor.execute(bc)
     rows=mycursor.fetchall()
     print(rows)
     return render(request,'adminviewdientplan.html',{'rowf':rows,'message':'There is some issue. Try after some time.'})
def adminviewstudentAttendance(request):
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="healthcarenourishmentdb")
    mycursor=mydb.cursor()
    bc="select * from fcm_members"
    print(bc)
    cd=mycursor.execute(bc)
    rows=mycursor.fetchall()
    print(rows)
    return render(request,'adminviewstudentAttendance.html',{'rowf':rows})         
def adminviewattendancehandler(request): 
    memberid=request.POST.get("memberid")
   
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="healthcarenourishmentdb")
    mycursor=mydb.cursor()
    bc="select * from fcm_attendance where memberid='"+memberid+"'"
    print(bc)
    cd=mycursor.execute(bc)
    rows=mycursor.fetchall()
    print(rows)       
    return render(request,'adminviewstudentAttendance1.html',{'rowf':rows})  
   

###############      
    
def userlogin(request):
    return render(request,'userlogin.html')
def userforget(request):
    return render(request,'userforget.html')    
    
def userforgetpasswordhandler(request):
    username=request.GET.get("username")
    email=request.GET.get("email")
    newpassword=request.GET.get("newpassword")
    confirmpassword=request.GET.get("confirmpassword")
    if(newpassword!=confirmpassword):
     return render(request,'userforget.html',{'message': 'Newpassword and Confirm Password Not Matched!'})
    
    
    
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="healthcarenourishmentdb")
    mycursor=mydb.cursor()
    q="select * from fcm_members where User_name='"+username+"'  and status='created' and Email='"+email+"'"
    print(q)
    c=mycursor.execute(q)
    print(c)
    row=mycursor.fetchone()
   
        
    if row!=None:
     q1="update fcm_members set Password='"+newpassword+"'  where user_name='"+username+"'"
     print(q1)
     mycursor.execute(q1)
     mydb.commit()
     return render(request, 'userforget.html',{'message': 'Password Changed.'})
    else:
     return render(request,'userforget.html',{'message': 'No User Exists'})  
 
    
def userloginvalidator(request):
    a=request.GET.get("username")
    b=request.GET.get("password")
    request.session['snam']=a
    print(a)
    print(b)
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="healthcarenourishmentdb")
    mycursor=mydb.cursor()
    q="select * from fcm_members where User_name='"+a+"' and Password='"+b+"' and status='created'"
    print(q)
    c=mycursor.execute(q)
    print(c)
    row=mycursor.fetchone()
   
        
    if row!=None:
       print(row)
       request.session['userid']=row[0]
       request.session['mob']=row[2]
       request.session['email']=row[5]
       return render(request, 'userhome.html',{'sname': request.session['snam']})
    else:
       return render(request,'userlogin.html',{'message': 'Invalid Credentials'})       
def userhome(request): 
    return render(request,'userhome.html',{'sname': request.session['snam']}) 
def userregister(request): 
    return render(request,'userregister.html')
def userregisterhandler(request):
    name=request.POST.get("name")
    gender=request.POST.get("gender")
    dob=request.POST.get("dob")
    mobile=request.POST.get("mobile")
    email=request.POST.get("email")
    username=request.POST.get("userid")
    password=request.POST.get("pw")
    #print(name)
    #print(mobileno)
    #print(gender)
    #print(dob)
    #print(email)
    #print(username)
    #print(password)
    
    mn1="INSERT INTO fcm_members(Name,Mobile_Number,Gender,Dob,Email,User_name,Password)VALUES('"+name+"','"+mobile+"','"+gender+"','"+dob+"','"+email+"','"+username+"','"+password+"')"
    print(mn1)
    from datetime import datetime
    uploaddate=str(datetime.date(datetime.now()))
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="healthcarenourishmentdb")
    mycursor=mydb.cursor()
    try:
     mn="INSERT INTO fcm_members(Name,Mobile_Number,Gender,Dob,Email,User_name,Password)VALUES('"+name+"','"+mobile+"','"+gender+"','"+dob+"','"+email+"','"+username+"','"+password+"')"
     print(mn)
     mycursor.execute(mn)
     mydb.commit()
     return render(request,'userlogin.html',{'message': 'Successfully Registered.'})
    except:
     return render(request,'userlogin.html',{'message': 'Some issue. Try after some time.'})
     
def userprofile(request):
    userid = str(request.session['userid'])
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="healthcarenourishmentdb")
    mycursor=mydb.cursor()
    bc="select * from fcm_members where userid='"+userid+"'"
    print(bc)
    cd=mycursor.execute(bc)
    rows=mycursor.fetchall()
    print(rows)
    return render(request,'userprofile.html',{'rowf':rows})    
    
def userprofileupdatehandler(request):
    userid=request.POST.get("userid")
    mobile=request.POST.get("mobile")
    email=request.POST.get("email")
    pw=request.POST.get("pw")
   
    
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="healthcarenourishmentdb")
    mycursor=mydb.cursor()
    try:
     mn="update fcm_members set Mobile_Number='"+mobile+"', Email='"+email+"',Password='"+pw+"'  where userid='"+userid+"'"
     print(mn)
     mycursor.execute(mn)
     mydb.commit()
     userid = str(request.session['userid'])
     mydb=mysql.connector.connect(host="localhost",user="root",password="",database="healthcarenourishmentdb")
     mycursor=mydb.cursor()
     bc="select * from fcm_members where userid='"+userid+"'"
     print(bc)
     cd=mycursor.execute(bc)
     rows=mycursor.fetchall()
     print(rows)
     return render(request,'userprofile.html',{'rowf':rows})     
    except:
     userid = str(request.session['userid'])
     mydb=mysql.connector.connect(host="localhost",user="root",password="",database="healthcarenourishmentdb")
     mycursor=mydb.cursor()
     bc="select * from fcm_members where userid='"+userid+"'"
     print(bc)
     cd=mycursor.execute(bc)
     rows=mycursor.fetchall()
     print(rows)
     return render(request,'userprofile.html',{'rowf':rows,'message':'There is some issue. Try after some time.'}) 
def usertrainer(request):
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="healthcarenourishmentdb")
    mycursor=mydb.cursor()
    memberid=str(request.session['userid'])
    bc1="select * from membertrainerselection where memberid='"+memberid+"' and status='created'"
    cd1=mycursor.execute(bc1)
    rows1=mycursor.fetchall()
    print(rows1)
    trainerid="none"
    mapno="0"
    for x1 in rows1:
     trainerid = x1[1]
     mapno=str(x1[0])
    print("***************"+trainerid)
    print("***************"+mapno)
    
    
    bc="select * from fcm_trainer where status='active'"
    print(bc)
    cd=mycursor.execute(bc)
    rows=mycursor.fetchall()
    print(rows)
    return render(request,'usertrainer.html',{'rowf':rows,'selectedtrainerid':trainerid,'mapno':mapno})     
def selecttrainerhandler(request):
    trainerid=request.POST.get("trainerid")
    memberid=str(request.session['userid'])
    mapno=request.POST.get("mapno")
    
    from datetime import datetime
    uploaddate=str(datetime.date(datetime.now()))
    #mn="INSERT INTO membertrainerselection(trainerid,memberid,date)VALUES('"+trainerid+"','"+memberid+"','"+uploaddate+"')"
    #print(mn)
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="healthcarenourishmentdb")
    mycursor=mydb.cursor()
    try:
     mn="INSERT INTO membertrainerselection(trainerid,memberid,date)VALUES('"+trainerid+"','"+memberid+"','"+uploaddate+"')"
     print(mn)
     mycursor.execute(mn)
     mydb.commit()
     mn1="update membertrainerselection set status='deleted' WHERE mapno="+mapno
     print(mn1)
     mycursor.execute(mn1)
     mydb.commit()     
     
     
     memberid=str(request.session['userid'])
     bc1="select * from membertrainerselection where memberid='"+memberid+"' and status='created'"
     cd1=mycursor.execute(bc1)
     rows1=mycursor.fetchall()
     print(rows1)
     trainerid="none"
     for x1 in rows1:
      trainerid = x1[1]
      mapno=str(x1[0])
     bc="select * from fcm_trainer where status='active'"
     print(bc)
     cd=mycursor.execute(bc)
     rows=mycursor.fetchall()
     print(rows)
     return render(request,'usertrainer.html',{'rowf':rows,'selectedtrainerid':trainerid,'mapno':mapno})        
     
    except:
    
     memberid=str(request.session['userid'])
     bc12="select * from membertrainerselection where memberid='"+memberid+"' and status='created'"
     cd12=mycursor.execute(bc1)
     rows12=mycursor.fetchall()
     print(rows12)
     trainerid2="none"
     for x12 in rows12:
      trainerid2 = x12[1]
      mapno2=str(x12[0])
     bc2="select * from fcm_trainer where status='active'"
     print(bc2)
     cd2=mycursor.execute(bc2)
     rows2=mycursor.fetchall()
     print(rows2)
     return render(request,'usertrainer.html',{'rowf':rows2,'selectedtrainerid':trainerid2,'mapno':mapno2,'message': 'Some issue. Try after some time.'}) 
def userdietplan(request): 
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="healthcarenourishmentdb")
    mycursor=mydb.cursor()
    #bc="select * from fcm_dietplans where status='created'"
    #print(bc)
    #cd=mycursor.execute(bc)
    #rows=mycursor.fetchall()
    #print(rows)
    memberid=str(request.session['userid'])
    bc1="select * from fcm_features where memberid='"+memberid+"'"
    cd=mycursor.execute(bc1)
    rows=mycursor.fetchall()
    print(rows)
    redirectionhtml="userdietplan.html"
    if len(rows)==0:
     redirectionhtml="userdietplanwof.html"
    else:
     ubmi=0
     upurpose="not selected"
     ucategory="not selected"
     for x1 in rows:
      ubmi = float(x1[6])
      upurpose=x1[5]
     print("********************"+str(ubmi))
     print("********************"+upurpose)
     if(ubmi<18.5):
      ucategory="Underweight"
     if(ubmi>18.5 and ubmi<24.9):
      ucategory="Normalweight"
     if(ubmi>25 and ubmi<29.9):
      ucategory="Overweight"
     if(ubmi>30):
      ucategory="Obesity"
      
     #Getting the proper diet plan on base of user feature
     bc = "select * from fcm_datasets where bmirange='"+ucategory+"' and purpose='"+upurpose+"' and class='yes'"
     print(bc)
     cd=mycursor.execute(bc)
     rowsdataset=mycursor.fetchall()
     highprotiencount=0
     nutralcount=0
     highprotiencount=0
     lowcalorycount=0
     for x1 in rowsdataset:
      print(x1[5])
      if(x1[5]=="lowcalory"):
       lowcalorycount+=1
      if(x1[5]=="nutral"):
       nutralcount+=1
      if(x1[5]=="highprotien"):
       highprotiencount+=1 
     maxcount=max(nutralcount,highprotiencount,lowcalorycount)  
     systemselectedcategory="unknown"
     if(maxcount==nutralcount):
      systemselectedcategory="nutral"
     if(maxcount==highprotiencount):
      systemselectedcategory="highprotien"
     if(maxcount==lowcalorycount):
      systemselectedcategory="lowcalory"
      
      
     print("******highprotiencount*********"+str(highprotiencount))  
     print("********nutralcount*******"+str(nutralcount))
     print("********lowcalorycount*******"+str(lowcalorycount))
     print("********maxcount*******"+str(maxcount))
     print("********systemselectedcategory*******"+systemselectedcategory)
     print()
     bc="select * from fcm_dietplans where status='created' and category='"+systemselectedcategory+"'"
     print(bc)
     cd=mycursor.execute(bc)
     rows1=mycursor.fetchall()
     print(rows1)
    return render(request,redirectionhtml,{'rowfeatures':rows,'rowf':rows1,'ucategory':ucategory,'systemselectedcategory':systemselectedcategory})
def userviewattendance(request):
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="healthcarenourishmentdb")
    mycursor=mydb.cursor()
    memberid=str(request.session['userid'])
    bc1="select * from fcm_attendance where memberid='"+memberid+"'"
    cd1=mycursor.execute(bc1)
    rows1=mycursor.fetchall()
    print(rows1)
    
    return render(request,'userattendance.html',{'rowf':rows1})      
    
    
def userviewmessage(request):
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="healthcarenourishmentdb")
    mycursor=mydb.cursor()
    memberid=str(request.session['userid'])
    bc1="select * from fcm_messages where memberid='"+memberid+"'"
    cd1=mycursor.execute(bc1)
    rows1=mycursor.fetchall()
    print(rows1)
    
    return render(request,'userviewmessage.html',{'rowf':rows1})  
 
     
    
###############      
    
def trainerlogin(request):
    return render(request,'trainerlogin.html')

def trainerforget(request):
    return render(request,'trainerforget.html')    
    
def trainerforgetpasswordhandler(request):
    username=request.GET.get("username")
    email=request.GET.get("email")
    newpassword=request.GET.get("newpassword")
    confirmpassword=request.GET.get("confirmpassword")
    if(newpassword!=confirmpassword):
     return render(request,'trainerforget.html',{'message': 'Newpassword and Confirm Password Not Matched!'})
    
    
    
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="healthcarenourishmentdb")
    mycursor=mydb.cursor()
    q="select * from fcm_trainer where User_name='"+username+"'   and Email='"+email+"'"
    print(q)
    c=mycursor.execute(q)
    print(c)
    row=mycursor.fetchone()
   
        
    if row!=None:
     q1="update fcm_trainer set Password='"+newpassword+"'  where user_name='"+username+"'"
     print(q1)
     mycursor.execute(q1)
     mydb.commit()
     return render(request, 'trainerforget.html',{'message': 'Password Changed.'})
    else:
     return render(request,'trainerforget.html',{'message': 'No User Exists'})      
    
    
    
def trainerloginvalidator(request):
    a=request.GET.get("username")
    b=request.GET.get("password")
    request.session['snam']=a
    print(a)
    print(b)
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="healthcarenourishmentdb")
    mycursor=mydb.cursor()
    q="select * from fcm_trainer where User_name='"+a+"' and Password='"+b+"' and status='active'"
    print(q)
    c=mycursor.execute(q)
    print(c)
    row=mycursor.fetchone()
   
        
    if row!=None:
       print(row)
       request.session['userid']=row[0]
       request.session['username']=row[1]
       request.session['mob']=row[2]
       request.session['email']=row[5]
       return render(request, 'trainerhome.html',{'sname': request.session['snam']})
    else:
       return render(request,'trainerlogin.html',{'message': 'Invalid Credentials'})  
def trainerregister(request): 
    return render(request,'trainerregister.html')       
def trainerregisterhandler(request):
    name=request.POST.get("name")
    gender=request.POST.get("gender")
    dob=request.POST.get("dob")
    mobile=request.POST.get("mobile")
    email=request.POST.get("email")
    experience=request.POST.get("experience")
    details=request.POST.get("details")
    username=request.POST.get("userid")
    password=request.POST.get("pw")
    #print(name)
    #print(mobileno)
    #print(gender)
    #print(dob)
    #print(email)
    #print(username)
    #print(password)
    
    mn1="INSERT INTO fcm_trainer(Name,Mobile_Number,Gender,Dob,Email,experience,details,User_name,Password)VALUES('"+name+"','"+mobile+"','"+gender+"','"+dob+"','"+email+"','"+experience+"','"+details+"','"+username+"','"+password+"')"
    print(mn1)
    from datetime import datetime
    uploaddate=str(datetime.date(datetime.now()))
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="healthcarenourishmentdb")
    mycursor=mydb.cursor()
    try:
     mn="INSERT INTO fcm_trainer(Name,Mobile_Number,Gender,Dob,Email,experience,details,User_name,Password)VALUES('"+name+"','"+mobile+"','"+gender+"','"+dob+"','"+email+"','"+experience+"','"+details+"','"+username+"','"+password+"')"
     print("******************"+mn)
     mycursor.execute(mn)
     mydb.commit()
     #inserting the userid in string format selection process
     mn2="SELECT max(userid) FROM fcm_trainer"
     print("**********************"+mn2)
     mycursor.execute(mn2)
     print("**********************"+mn2)
     row2=mycursor.fetchone()
     print(row2)
     lastuserid=row2[0]
     print("**********************"+str(lastuserid))
     mn1="update fcm_trainer set userids='"+str(lastuserid)+"' WHERE userid="+str(lastuserid)
     print(mn1)
     mycursor.execute(mn1)
     mydb.commit()
     return render(request,'trainerregister.html',{'message': 'Successfully Registered.'})
    except:
     return render(request,'trainerregister.html',{'message': 'Some issue. Try after some time.'})         
def trainerhome(request): 
    return render(request,'trainerhome.html',{'sname': request.session['snam']}) 
def trainerprofile(request):
    trainerid = str(request.session['userid'])
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="healthcarenourishmentdb")
    mycursor=mydb.cursor()
    bc="select * from fcm_trainer where userid='"+trainerid+"'"
    print(bc)
    cd=mycursor.execute(bc)
    rows=mycursor.fetchall()
    print(rows)
    return render(request,'trainerprofile.html',{'rowf':rows})    
def trainerprofileupdatehandler(request):
    userid=request.POST.get("userid")
    mobile=request.POST.get("mobile")
    email=request.POST.get("email")
    pw=request.POST.get("pw")
    experience=request.POST.get("experience")
    details=request.POST.get("details")
    
    
   
    
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="healthcarenourishmentdb")
    mycursor=mydb.cursor()
    try:
     mn="update fcm_trainer set Mobile_Number='"+mobile+"', Email='"+email+"',experience='"+experience+"',details='"+details+"',Password='"+pw+"'  where userid='"+userid+"'"
     print(mn)
     mycursor.execute(mn)
     mydb.commit()
     userid = str(request.session['userid'])
     mydb=mysql.connector.connect(host="localhost",user="root",password="",database="healthcarenourishmentdb")
     mycursor=mydb.cursor()
     bc="select * from fcm_trainer where userid='"+userid+"'"
     print(bc)
     cd=mycursor.execute(bc)
     rows=mycursor.fetchall()
     print(rows)
     return render(request,'trainerprofile.html',{'rowf':rows})     
    except:
     userid = str(request.session['userid'])
     mydb=mysql.connector.connect(host="localhost",user="root",password="",database="healthcarenourishmentdb")
     mycursor=mydb.cursor()
     bc="select * from fcm_trainer where userid='"+userid+"'"
     print(bc)
     cd=mycursor.execute(bc)
     rows=mycursor.fetchall()
     print(rows)
     return render(request,'trainerprofile.html',{'rowf':rows,'message':'There is some issue. Try after some time.'})    
def trainerattendance(request): 
    trainerid = str(request.session['userid'])
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="healthcarenourishmentdb")
    mycursor=mydb.cursor()
    #bc="select * from fcm_members where status='created'"
    bc="select * from fcm_members where status='created' and userid IN (select memberid from membertrainerselection where trainerid='"+trainerid+"')"
    print(bc)
    cd=mycursor.execute(bc)
    rows=mycursor.fetchall()
    print(rows)
    return render(request,'trainerattendance.html',{'rowf':rows,'sname': request.session['snam']})  
def trainertakememberattendance(request): 
    memberid=request.POST.get("memberid")
    membername=request.POST.get("membername")
    trainerid=str(request.session['userid'])
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="healthcarenourishmentdb")
    mycursor=mydb.cursor()
    bc="select * from fcm_attendance where trainerid='"+trainerid+"' and memberid='"+memberid+"'"
    print(bc)
    cd=mycursor.execute(bc)
    rows=mycursor.fetchall()
    print(rows)       
    return render(request,'trainertakememberattendance.html',{'rowf':rows,'sname': request.session['snam'],'memberid':memberid,'membername':membername})
def trainertakememberattendancehandler(request): 
    memberid=request.POST.get("memberid")
    membername=request.POST.get("membername")
    trainerid=str(request.session['userid'])
    adate=request.POST.get("adate")
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="healthcarenourishmentdb")
    mycursor=mydb.cursor()
    mn="INSERT INTO fcm_attendance(trainerid,memberid,membername,date)VALUES('"+trainerid+"','"+memberid+"','"+membername+"','"+adate+"')"
    print(mn)
    mycursor.execute(mn)
    mydb.commit()
    
    
    
    bc="select * from fcm_attendance where trainerid='"+trainerid+"' and memberid='"+memberid+"'"
    print(bc)
    cd=mycursor.execute(bc)
    rows=mycursor.fetchall()
    print(rows)       
    return render(request,'trainertakememberattendance.html',{'rowf':rows,'sname': request.session['snam'],'memberid':memberid,'membername':membername})    
def trainerpf(request): 
    trainerid = str(request.session['userid'])
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="healthcarenourishmentdb")
    mycursor=mydb.cursor()
    #bc="select * from fcm_members where status='created'"
    bc="select * from fcm_members where status='created' and userid IN (select memberid from membertrainerselection where trainerid='"+trainerid+"')"
    print(bc)
    cd=mycursor.execute(bc)
    rows=mycursor.fetchall()
    print(rows)
    return render(request,'trainerpf.html',{'rowf':rows,'sname': request.session['snam']})  
    
    
    
def trainertakememberfeatures(request): 
    memberid=request.POST.get("memberid")
    membername=request.POST.get("membername")
    trainerid=str(request.session['userid'])
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="healthcarenourishmentdb")
    mycursor=mydb.cursor()
    bc="select * from fcm_features where memberid='"+memberid+"'"
    print(bc)
    cd=mycursor.execute(bc)
    rows=mycursor.fetchall()
    print(rows)
    redirectionhtml="trainertakememberfeatures.html"
    if len(rows)>0:
     redirectionhtml="trainertakememberupdatefeatures.html"
    return render(request,redirectionhtml,{'rowf':rows,'sname': request.session['snam'],'memberid':memberid,'membername':membername})
    
def trainertakememberfeatureshandler(request): 
    memberid=request.POST.get("memberid")
    membername=request.POST.get("membername")
    height=request.POST.get("height")
    weight=request.POST.get("weight")
    purpose=request.POST.get("purpose")
    bmi=request.POST.get("bmi")
    trainerid=str(request.session['userid'])
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="healthcarenourishmentdb")
    mycursor=mydb.cursor()
    mn="INSERT INTO fcm_features(memberid,membername,height,weight,purpose,bmi)VALUES('"+memberid+"','"+membername+"','"+height+"','"+weight+"','"+purpose+"','"+bmi+"')"
    print(mn)
    mycursor.execute(mn)
    mydb.commit()


    bc="select * from fcm_features where memberid='"+memberid+"'"
    print(bc)
    cd=mycursor.execute(bc)
    rows=mycursor.fetchall()
    print(rows)
    redirectionhtml="trainertakememberfeatures.html"
    if len(rows)>0:
     redirectionhtml="trainertakememberupdatefeatures.html"
    return render(request,redirectionhtml,{'rowf':rows,'sname': request.session['snam'],'memberid':memberid,'membername':membername,'message': 'Added'})
def trainertakememberfeaturesupdatehandler(request): 
    print("--------------------------------------")
    memberid=request.POST.get("memberid")
    membername=request.POST.get("membername")
    height=request.POST.get("height")
    weight=request.POST.get("weight")
    purpose=request.POST.get("purpose")
    bmi=request.POST.get("bmi")
    trainerid=str(request.session['userid'])
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="healthcarenourishmentdb")
    mycursor=mydb.cursor()
    print("--------------------------------------")
    mn="update fcm_features set height='"+height+"',weight='"+weight+"',purpose='"+purpose+"',bmi='"+bmi+"' where memberid="+memberid
    print(mn)
    mycursor.execute(mn)
    mydb.commit()
    
    bc="select * from fcm_features where memberid='"+memberid+"'"
    print(bc)
    cd=mycursor.execute(bc)
    rows=mycursor.fetchall()
    print(rows)
    redirectionhtml="trainertakememberfeatures.html"
    if len(rows)>0:
     redirectionhtml="trainertakememberupdatefeatures.html"
    return render(request,redirectionhtml,{'rowf':rows,'sname': request.session['snam'],'memberid':memberid,'membername':membername,'message': 'Updated'})
    


def trainermessage(request): 
    trainerid = str(request.session['userid'])
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="healthcarenourishmentdb")
    mycursor=mydb.cursor()
    #bc="select * from fcm_members where status='created'"
    bc="select * from fcm_members where status='created' and userid IN (select memberid from membertrainerselection where trainerid='"+trainerid+"')"
    print(bc)
    cd=mycursor.execute(bc)
    rows=mycursor.fetchall()
    print(rows)
    return render(request,'trainermessage.html',{'rowf':rows,'sname': request.session['snam']})          
def trainersendmessage(request): 
    memberid = request.POST.get("memberid")
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="healthcarenourishmentdb")
    mycursor=mydb.cursor()
    
    bc="select * from fcm_members where status='created' and userid='"+memberid+"'"
    print(bc)
    cd=mycursor.execute(bc)
    rows=mycursor.fetchall()
    print(rows)
    return render(request,'trainersendmessage.html',{'rowf':rows,'sname': request.session['snam']}) 
    
def trainersendmessagehandler(request): 
    memberid=request.POST.get("memberid")
    membername=request.POST.get("membername")
    trainername=str(request.session['username'])
    
    trainerid=str(request.session['userid'])
    message=request.POST.get("message")
    from datetime import datetime
    uploaddate=str(datetime.date(datetime.now()))
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="healthcarenourishmentdb")
    mycursor=mydb.cursor()
    mn="INSERT INTO fcm_messages(trainerid,trainername,memberid,membername,message,date)VALUES('"+trainerid+"','"+trainername+"','"+memberid+"','"+membername+"','"+message+"','"+uploaddate+"')"
    print(mn)
    mycursor.execute(mn)
    mydb.commit()


    bc="select * from fcm_messages where trainerid='"+trainerid+"' and memberid='"+memberid+"'"
    print(bc)
    cd=mycursor.execute(bc)
    rows=mycursor.fetchall()
    print(rows)
    return render(request,'trainerviewmessage.html',{'rowf':rows,'sname': request.session['snam']}) 
    
    
def trainerviewmessage(request): 
    memberid=request.POST.get("memberid")
   
    
    trainerid=str(request.session['userid'])
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="healthcarenourishmentdb")
    mycursor=mydb.cursor()
    bc="select * from fcm_messages where trainerid='"+trainerid+"' and memberid='"+memberid+"'"
    print(bc)
    cd=mycursor.execute(bc)
    rows=mycursor.fetchall()
    print(rows)
    return render(request,'trainerviewmessage.html',{'rowf':rows,'sname': request.session['snam']})     
 


    

          
    
    
    