from yandex_music import Client
from pypresence import Presence
import config
import time


client = Client().from_credentials(config.Login, config.Password)
rpc = Presence(config.TokenDiscord)
rpc.connect()

while True:
    queues = client.queues_list()
    last_queue = client.queue(queues[0].id)

    last_track_id = last_queue.get_current_track()
    last_track = last_track_id.fetch_track()
    
    id_track = last_track.id
    id_album = last_track.albums[0].id

    url = f'https://music.yandex.ru/album/{id_album}/track/{id_track}'
    artists = ', '.join(last_track.artists_name())
    title = last_track.title

    rpc.update(state=title, details=artists, large_image='logomain', buttons=[{"label": "Слушать ▶️", "url": url}])
    time.sleep(15)
