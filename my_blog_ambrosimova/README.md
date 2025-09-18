В папке _db_ лежит служебный файл. \
В папке _models_ лежат классы таблиц БД. \
В файле _config.py_ путь до БД sqlite. \
В файле _create_table_ запускается создание таблиц БД. \
В _main.py_ заполняются таблицы данными. \
В _queries.py_ лежат запросы к БД. \

Мой проект **my_blog_ambrosimova** лежит во внешней папке **courses_homework**. Поэтому пути в файлах относительные. 

Запускаю файлы командами \
`` python -m my_blog_ambrosimova.create_table`` -- создание БД и таблиц \
``python -m my_blog_ambrosimova.main `` -- заполнение таблиц \
``python -m my_blog_ambrosimova.queries`` -- запросы \