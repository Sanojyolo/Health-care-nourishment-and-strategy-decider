
from django.urls import path
from . import views



urlpatterns = [

path('', views.home, name='home'),
path('home', views.home, name='home'),
path('adminlogin', views.adminlogin, name='adminlogin'),
path('adminloginvalidator', views.adminloginvalidator, name='adminloginvalidator'),
path('adminhome', views.adminhome, name='adminhome'),
path('adminaddmember', views.adminaddmember, name='adminaddmember'),
path('adminviewmember', views.adminviewmember, name='adminviewmember'),
path('deletememberhandler', views.deletememberhandler, name='deletememberhandler'),
path('adminviewtrainer', views.adminviewtrainer, name='adminviewtrainer'),
path('approvetrainerhandler', views.approvetrainerhandler, name='approvetrainerhandler'),
path('deletetrainerhandler', views.deletetrainerhandler, name='deletetrainerhandler'),
path('adminadddietplan', views.adminadddietplan, name='adminadddietplan'),
path('adddietplanhandler', views.adddietplanhandler, name='adddietplanhandler'),
path('adminviewdientplan', views.adminviewdientplan, name='adminviewdientplan'),
path('deletedietplanhandler', views.deletedietplanhandler, name='deletedietplanhandler'),
path('adminviewstudentAttendance', views.adminviewstudentAttendance, name='adminviewstudentAttendance'),
path('adminviewattendancehandler', views.adminviewattendancehandler, name='adminviewattendancehandler'),












path('userlogin', views.userlogin, name='userlogin'),
path('userforget', views.userforget, name='userforget'),
path('userforgetpasswordhandler', views.userforgetpasswordhandler, name='userforgetpasswordhandler'),

path('userloginvalidator', views.userloginvalidator, name='userloginvalidator'),
path('userhome', views.userhome, name='userhome'),
path('userregister', views.userregister, name='userregister'),
path('userregisterhandler', views.userregisterhandler, name='userregisterhandler'),
path('userprofile', views.userprofile, name='userprofile'),
path('userprofileupdatehandler', views.userprofileupdatehandler, name='userprofileupdatehandler'),
path('usertrainer', views.usertrainer, name='usertrainer'),
path('selecttrainerhandler', views.selecttrainerhandler, name='selecttrainerhandler'),
path('userdietplan', views.userdietplan, name='userdietplan'),
path('userviewattendance', views.userviewattendance, name='userviewattendance'),







path('trainerlogin', views.trainerlogin, name='trainerlogin'),
path('trainerforget', views.trainerforget, name='trainerforget'),
path('trainerforgetpasswordhandler', views.trainerforgetpasswordhandler, name='trainerforgetpasswordhandler'),

path('trainerloginvalidator', views.trainerloginvalidator, name='trainerloginvalidator'),
path('trainerhome', views.trainerhome, name='trainerhome'),
path('trainerregister', views.trainerregister, name='trainerregister'),
path('trainerregisterhandler', views.trainerregisterhandler, name='trainerregisterhandler'),
path('trainerprofile', views.trainerprofile, name='trainerprofile'),
path('trainerprofileupdatehandler', views.trainerprofileupdatehandler, name='trainerprofileupdatehandler'),
path('trainerattendance', views.trainerattendance, name='trainerattendance'),
path('trainertakememberattendance', views.trainertakememberattendance, name='trainertakememberattendance'),
path('trainertakememberattendancehandler', views.trainertakememberattendancehandler, name='trainertakememberattendancehandler'),
path('trainerpf', views.trainerpf, name='trainerpf'),
path('trainertakememberfeatures', views.trainertakememberfeatures, name='trainertakememberfeatures'),
path('trainertakememberfeatureshandler', views.trainertakememberfeatureshandler, name='trainertakememberfeatureshandler'),
path('trainertakememberfeaturesupdatehandler', views.trainertakememberfeaturesupdatehandler, name='trainertakememberfeaturesupdatehandler'),
path('trainermessage', views.trainermessage, name='trainermessage'),
path('trainersendmessage', views.trainersendmessage, name='trainersendmessage'),
path('trainersendmessagehandler', views.trainersendmessagehandler, name='trainersendmessagehandler'),
path('trainerviewmessage', views.trainerviewmessage, name='trainerviewmessage'),
path('userviewmessage', views.userviewmessage, name='userviewmessage'),









]


