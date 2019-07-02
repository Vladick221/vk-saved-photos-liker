import vk_api
import time
import traceback
USER_ACCESS_TOKEN = '' # Токен пользователя с правами фото

# Ид пользователя Вконтакте
USER_TARGET = 1

# Подключение по токену пользователя
vk_u_session = vk_api.VkApi(token=USER_ACCESS_TOKEN)
u_api = vk_u_session.get_api()

while True:
    try:
        # Получаем количество сохраненок на данный момент
        actual_count = u_api.photos.get(owner_id=USER_TARGET, album_id='saved')['count']
        old_count = int(open('output.txt').read())

        # Если количество сохраненнок стало больше
        if (actual_count > old_count):
            new_photos_count = (actual_count - old_count)

            query = u_api.photos.get(owner_id=USER_TARGET, album_id='saved', count=new_photos_count, rev=1)

            for x in query['items']:
                u_api.likes.add(type='photo', owner_id=USER_TARGET, item_id=x['id'])

            # Записываем новое количество сохраненнок
            open('output.txt', 'w').write(str(actual_count))
            time.sleep(0.5)
        # else:
        #     print("New saved photos not detected")

    except Exception:
        print(traceback.format_exc())
        continue
