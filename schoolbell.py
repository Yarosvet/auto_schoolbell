#!/usr/bin/env python
import pygame, os, datetime, time

#dll_name = os.path.join(os.path.dirname(__file__), 'sources/avbin')
#pyglet.lib.load_library(dll_name)
sound = 'sources/bell.wav'
schedule = []
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
pygame.init()
pygame.mixer.music.load(sound)


#def exiter(dt):
#    pyglet.app.exit()


def read_schedule(schedule_file_path='sources/schedule_' + weekdays[datetime.datetime.now().weekday()] + '.txt'):
    file = open(schedule_file_path, 'r', encoding='utf-8')
    sched = file.read()
    sched = sched.split('\n')
    for i in range(len(sched)):
        sched[i] = sched[i].strip()
        if sched[i]:
            first = sched[i][:sched[i].index(':')]
            second = sched[i][sched[i].index(':') + 1:]
            sched[i] = (first, second)
        else:
            del sched[i]
    file.close()
    return sched


def play():
#    song = pyglet.media.load(sound, streaming=False)
#    song.play()
#    pyglet.clock.schedule_once(exiter, song.duration)
#    pyglet.app.run()
    a = pygame.mixer.Sound(sound)
    dnow = datetime.datetime.now()
    minutes = str(dnow.minute).rjust(2, '0')
    print(f'[{dnow.hour}:{minutes}] The bell is sounding...')
    pygame.mixer.music.play(loops=1)
    time.sleep(a.get_length())
    pygame.mixer.music.stop()


while True:
    now = datetime.datetime.now()
    schedule = read_schedule()
    if now.weekday() != 6:
        time.sleep(3)
        for el in schedule:
            nowtime = str(now.time())[:2], str(now.time())[3:5]
            if nowtime[1] == el[1] and nowtime[0] == el[0]:
                play()
                time.sleep(61 - datetime.datetime.now().second)
    else:
        time.sleep(60)