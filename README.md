# Изменения в электронном дневнике

Этот проект предназначен для редактирования данных в электронном дневнике. **[Электронный дневник](https://github.com/devmanorg/e-diary/tree/master)** - это проект, написанный на Джанго.

## Описание функций

В данном проекте реализованы три функции:

- **fix_marks**: 
  Исправляет плохие оценки на отличные в базе данных.

- **remove_chastisements**: 
  Удаляет плохие замечания в базе данных.

- **create_commendation**: 
  Создает хорошие замечания.

### change.py script
Этот скрипт предназначен для редактирования базы данных. Существует две возможности использовать данный скрипт:

- Django shell(копируйте код и вставьте в командную строку)
#### Вызов Django shell
```bash
    python manage.py shell
```

- используйте import данных функций в manage.py
