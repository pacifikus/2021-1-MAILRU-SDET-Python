Регистрация
- *test_doubled_email*: серверная ошибка при вводе уже зарегистрированной почты
- *test_incorrect_password_length*: серверная ошибка при вводе слишком длинного пароля

API
- *test_add_user*: добавление пользователя через api - неверный код (210 вместо 201) 
- *test_add_user_with_invalid_name*: добавляется пользователь с некорректным username ('', '11', 'q'*17) 
- *test_add_user_with_invalid_pass*: добавляется пользователь с некорректным password ('', 'q'*300) 
- *test_add_user_with_invalid_email*: добавляется пользователь с некорректным email ('', 'qwe', '@qweqweqwe.ru', '.qwe@mail.ru', 'q'*65) 
- *test_add_user_with_exists_email*: добавляется пользователь с существующим email 

Главная страница
- *test_vk_id_appear*: vk id не появляется на главной странице 
- *test_go_to_centos*: centos ведет на fedora  