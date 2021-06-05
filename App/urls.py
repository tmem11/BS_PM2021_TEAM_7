from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.adminPage, name='dashboard'),
    path('login/', views.login, name='login'),
    path('Teacher_Register/', views.Teacher_Signup, name='Teacher_Signup'),
    path('Student_Register/', views.Student_Signup, name='Student_Signup'),
    path('teacher', views.teacher_dashboard, name='teacher'),
    path('delete_homework/<int:id>/', views.homework_delete, name='homework_delete'),
    path('homeworkform/', views.homework_form, name='homework_form'),
    path('SolutionForm/', views.Solution_form, name='Solution_form'),
    path('homeowrk<int:id>/', views.homework_form, name='homework_update'),
    path('profile', views.profile, name='profile'),
    path('createmessage/', views.admin_message_form, name='createmessage'),
    path('editAdminMessage/<int:id>', views.admin_message_form, name='editAdminMessage'),
    path('deleteAdminMessage/<int:id>', views.admin_mesaage_delete, name='deleteAdminMessage'),
    path('createTeacherMessage', views.teacher_message_form, name='create_teacher_message'),
    path('editTeacherMessage/<int:id>', views.teacher_message_form, name='editTeacherMessage'),
    path('deleteTeacherMessage/<int:id>', views.teacher_mesaage_delete, name='deleteTeacherMessage'),
    path('teacherMessages', views.showMessages, name="teacherMessages"),
    path('logout', views.logoutUser, name="logout"),
    path('studentdashboard', views.student_dashboard, name="student_dashboard"),
    path('bugreport', views.bugreport, name="bugreport"),
    path('showSolutions', views.showSolutions, name="showSolutions"),
    path('allstudies', views.showStudies, name='showAllStudies'),
    path('approveStudy/<int:id>', views.approveStudy, name="approve_study"),
    path('studiesTeacher', views.showStudiesTeacher, name="showStudentTeacher"),
    path('studyForm', views.study_form, name="addstudy"),
    path('studyform/<int:id>', views.study_form, name="study_update"),
    path('studyform_delete/<int:id>', views.study_delete, name="study_delete"),
    path('allhomework_student', views.showHomework, name='showhomeworkstudent'),
    path('myHomeWorks', views.showStudentHomeworks, name="myHomeWorks"),
    path('showHomeWork/<int:id>', views.showSingleHomeWork, name="showHomeWork"),
    path('addGrade/<int:id>', views.addGrade, name="addGrade"),
    path('addStudent',views.addStudent,name="addStudent"),
    path('addTeacher',views.addTeacher,name="addTeacher"),
    path('myGrades',views.myGrades,name="myGrades"),
    path('showAdminMessages', views.showAdminMessages, name="showAdminMessages"),

    path('user_list/',views.user_list,name="user_list"),
    path('update/<int:id>',views.user_form_edit,name="update_user_info"),
    path('delete/<int:id>',views.delete_user,name="delete_user"),
   # path('create_user/',views.create_user,name="create_user"),
    path('show_details/<int:id>',views.showUser,name="show_details"),
    path('createSolution/<int:id>',views.createSolution,name="createSolution"),
    #path('update_user/<int:id>',views.update_form,name="update_user_form"),
    path('addStudent', views.addStudent, name="addStudent"),
    path('addTeacher', views.addTeacher, name="addTeacher"),
    path('myGrades', views.myGrades, name="myGrades"),
    path('myTeacherComment/<int:id>', views.myTeacherComment, name="myTeacherComment"),

    path('user_list/', views.user_list, name="user_list"),
    path('update/<int:id>', views.user_form_edit, name="update_user_info"),
    path('delete/<int:id>', views.delete_user, name="delete_user"),
#    path('show_details/<int:id>', views.showUser, name="show_details"),
    path('createSolution/<int:id>', views.createSolution, name="createSolution"),
    # path('update_user/<int:id>',views.update_form,name="update_user_form"),
    path('editSolution/<int:id>', views.editSolution, name="editSolution"),
    path('showstudents', views.showMyStudents, name="showMystudent"),
    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="password_rest/password_reset.html"),
         name="reset_password"),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="password_rest/password_reset_sent.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="password_rest/password_reset_form.html"),
         name="password_reset_confirm"),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="password_rest/password_reset_done.html"),
         name="password_reset_complete"),
    path('create_solution_new/<int:id>/',views.createSolution,name="create_solution_new"),
    path('edit_solution_new/<int:id>/<int:sol_id>',views.editSolution,name="edit_solution_new"),
    path('showstudy/<int:id>',views.showStudy,name="showstudy")

]
