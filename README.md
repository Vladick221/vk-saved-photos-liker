# vk-saved-photos-liker
Небольшой python-скрипт для ВК. Лайкает сохраненные фото указанной цели (user_id) при их появлении.

**Для корректной работы необходимо вписать в файл output.txt последнее количество сохраненнок пользователя**
Узнать это количество можно так - actual_count = u_api.photos.get(owner_id=USER_TARGET, album_id='saved')['count']
