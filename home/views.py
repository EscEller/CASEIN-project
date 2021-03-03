from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from home.models import UserInformation, DepartmentInformation, UserAccount
from operator import itemgetter


@login_required(login_url='/accounts/login/')
def contacts(request):
    context = {}
    return render(
        request,
        'home/contacts_page.html',
        context=context)


@login_required(login_url='/accounts/login/')
def team_page(request):
    user_id = request.user.id
    model_user = UserInformation
    model_dep = DepartmentInformation

    username = model_user.objects.get(user_id=user_id).last_name + ' ' + \
               model_user.objects.get(user_id=user_id).first_name + ' ' + \
               model_user.objects.get(user_id=user_id).patronymic

    user_email = request.user.email

    user_position = model_user.objects.get(user_id=user_id).position
    user_phone = model_user.objects.get(user_id=user_id).phone_number
    user_office = model_user.objects.get(user_id=user_id).office

    user_dep_id = model_user.objects.get(user_id=user_id).department_id
    user_dep_title = model_dep.objects.get(depart_id=user_dep_id).title

    user_team_list = model_user.objects.filter(department_id=user_dep_id).values('user_id')
    user_team_len = len(user_team_list)

    is_head = False
    head_name = ''
    head_position = ''
    head_email = ''
    head_phone = ''
    head_office = ''

    is_mentor = False
    is_head_mentor = False
    mentor_name = ''
    mentor_position = ''
    mentor_email = ''
    mentor_phone = ''
    mentor_office = ''

    teammates_name_list = []
    teammates_position_list = []
    teammates_email_list = []
    teammates_phone_list = []
    teammates_office_list = []

    for user_dict in user_team_list:
        cur_user_id = user_dict['user_id']
        if cur_user_id != user_id:

            is_head_h = model_user.objects.get(user_id=cur_user_id).is_head

            is_mentor_h = (model_user.objects.get(user_id=cur_user_id).mentor == request.user.id)

            if is_head_h:
                is_head = True

                head_name = model_user.objects.get(user_id=cur_user_id).last_name + ' ' + \
                            model_user.objects.get(user_id=cur_user_id).first_name + ' ' + \
                            model_user.objects.get(user_id=cur_user_id).patronymic
                head_position = model_user.objects.get(user_id=cur_user_id).position
                head_email = UserAccount.objects.get(id=cur_user_id).email
                head_phone = model_user.objects.get(user_id=cur_user_id).phone_number
                head_office = model_user.objects.get(user_id=cur_user_id).office

            if is_mentor_h:
                if is_head_h:
                    is_head_mentor = True
                is_mentor = True
                mentor_name = model_user.objects.get(user_id=cur_user_id).last_name + ' ' + \
                              model_user.objects.get(user_id=cur_user_id).first_name + ' ' + \
                              model_user.objects.get(user_id=cur_user_id).patronymic
                mentor_position = model_user.objects.get(user_id=cur_user_id).position
                mentor_email = UserAccount.objects.get(id=cur_user_id).email
                mentor_phone = model_user.objects.get(user_id=cur_user_id).phone_number
                mentor_office = model_user.objects.get(user_id=cur_user_id).office

            if not is_head_h and not is_mentor_h:
                teammates_name = model_user.objects.get(user_id=cur_user_id).last_name + ' ' + \
                                 model_user.objects.get(user_id=cur_user_id).first_name + ' ' + \
                                 model_user.objects.get(user_id=cur_user_id).patronymic

                teammates_email_list.append(UserAccount.objects.get(id=cur_user_id).email)

                teammates_name_list.append(teammates_name)

                teammates_position = model_user.objects.get(user_id=cur_user_id).position

                teammates_position_list.append(teammates_position)

                teammates_phone = model_user.objects.get(user_id=cur_user_id).phone_number

                teammates_phone_list.append(teammates_phone)

                teammates_office = model_user.objects.get(user_id=cur_user_id).office

                teammates_office_list.append(teammates_office)

    user_team_data = zip(teammates_name_list, teammates_position_list,
                         teammates_email_list, teammates_phone_list, teammates_office_list)

    user_team_data = (list(user_team_data))

    user_team_data.sort(key=itemgetter(1, 0), reverse=False)

    is_team = is_head or is_mentor or (user_team_len > 1)

    context = {
        'user_dep_title': user_dep_title,

        'username': username,
        'user_email': user_email,
        'user_position': user_position,
        'user_phone': user_phone,
        'user_office': user_office,

        'is_head_mentor': is_head_mentor,

        'is_head': is_head,
        'head_name': head_name,
        'head_email': head_email,
        'head_position': head_position,
        'head_phone': head_phone,
        'head_office': head_office,

        'is_mentor': is_mentor,
        'mentor_name': mentor_name,
        'mentor_email': mentor_email,
        'mentor_position': mentor_position,
        'mentor_phone': mentor_phone,
        'mentor_office': mentor_office,

        'is_team': is_team,
        'user_team_data': user_team_data
    }

    return render(
        request,
        'home/team_page.html',
        context=context)


@login_required(login_url='/accounts/login/')
def home_page(request):
    context = {}
    return render(
        request,
        'home/home_page.html',
        context=context)


@login_required(login_url='/accounts/login/')
def norm_docks(request):
    context = {}
    return render(
        request,
        'home/docks/norm_docks.html',
        context=context)


@login_required(login_url='/accounts/login/')
def polit_bez(request):
    context = {}
    return render(
        request,
        'home/docks/polit_bez.html',
        context=context)


@login_required(login_url='/accounts/login/')
def instructions(request):
    context = {}
    return render(
        request,
        'home/docks/instructions.html',
        context=context)


@login_required(login_url='/accounts/login/')
def korpculture(request):
    context = {}
    return render(
        request,
        'home/docks/korpculture.html',
        context=context)


def start_page(request):
    context = {}
    return render(
        request,
        'home/start_page.html',
        context=context)
