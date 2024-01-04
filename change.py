import random

from datacenter.models import Chastisement, Lesson, Schoolkid

COMMENDATION = ['Молодец!', 'Правильно!', 'Хорошо!', 'Умница!', 'Замечательно!', 'Хвалю!']


def get_kid(full_name):
    try:
        kid = Schoolkid.objects.get(full_name__contains=full_name)
    except Schoolkid.DoesNotExist:
        print(f"Ученик с именем {full_name} не найден.")
        return None
    except Schoolkid.MultipleObjectsReturned:
        print(f"Найдено несколько учеников с именем {full_name}. Уточните запрос.")
        return None
    return kid


def fix_marks(full_name):
    kid = get_kid(full_name)
    if not isinstance(kid, Schoolkid):
        return
    Mark.objects.filter(schoolkid=kid, points__in=[4,5]).update(points=2)


def remove_chastisements(full_name):
    kid = get_kid(full_name)
    if not isinstance(kid, Schoolkid):
        return
    Chastisement.objects.filter(schoolkid=kid).delete()


def create_commendation(full_name, subject):
    kid = get_kid(full_name)
    if not isinstance(kid, Schoolkid):
        return
    year_of_study = kid.year_of_study
    group_letter = kid.group_letter
    subject_lessons = Lesson.objects.filter(year_of_study=year_of_study, group_letter=group_letter, subject__title__contains=subject).order_by('?')
    if subject_lessons:
        random_lesson = subject_lessons.first()
        Commendation.objects.create(
            text=random.choice(COMMENDATION),
            created=random_lesson.date,
            schoolkid=kid,
            subject=random_lesson.subject,
            teacher=random_lesson.teacher
        )
    else:
        print(f"Не найдены уроки по предмету {subject} для ученика {full_name}.")

