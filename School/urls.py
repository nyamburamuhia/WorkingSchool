from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$','main.views.welcome'),
                       url(r'^student/login_form/$','students.views.login_student_form'),
                       #url(r'^teacher/login_form/$','teachers.views.login_teacher_form'),
                       url(r'^student/register/$','students.views.register_student'),
                       #url(r'^teacher/register/$','teachers.views.register_teacher'),
                       url(r'^student/register/add/$','students.views.register_student_add'),
                       #url(r'^teacher/register/add/$','teachers.views.register_teacher_add'),
                       url('^student/login/$','students.views.login_student'),
                       url(r'^student/list_students/$','students.views.list_students'),
                       url(r'^student/delete/(?P<student_id>\d+)/$','students.views.delete_student'),
                       url(r'^student/edit/(?P<student_id>\d+)/$','students.views.edit_student_form'),
                       url(r'^student/edit/(?P<student_id>\d+)/(.*)$','students.views.edit_student'),
                       
    # Examples:
    # url(r'^$', 'Students.views.home', name='home'),
    # url(r'^Students/', include('Students.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
