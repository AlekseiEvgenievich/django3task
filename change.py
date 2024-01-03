import random

def fix_marks(schoolkid):
    bad_marks = Mark.objects.filter(schoolkid=schoolkid[0], points__in=[2,3])
    for bad_mark in bad_marks:
        bad_mark.points = 5
        bad_mark.save()

def remove_chastisements(schoolkid):
    bad_chastisement = Chastisement.objects.filter(schoolkid=schoolkid[0])
    bad_chastisement.delete()

def create_commendation(full_name, subject):
    try:
        onekid = Schoolkid.objects.get(full_name__contains=full_name)
    except Schoolkid.DoesNotExist:
        print(f"Ученик с именем {full_name} не найден.")
        return
    except Schoolkid.MultipleObjectsReturned:
        print(f"Найдено несколько учеников с именем {full_name}. Уточните запрос.")
        return
    year_of_study = onekid.year_of_study
    group_letter = onekid.group_letter
    subject_lessons = Lesson.objects.filter(year_of_study=year_of_study, group_letter=group_letter, subject__title__contains=subject)
    if subject_lessons:
        random_lesson = random.choice(subject_lessons)
        Commendation.objects.create(
            text="Хвалю!",
            created=random_lesson.date,
            schoolkid=onekid,
            subject=random_lesson.subject,
            teacher=random_lesson.teacher
        )
    else:
        print(f"Не найдены уроки по предмету {subject} для ученика {full_name}.")
