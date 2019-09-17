import pyglet, os, datetime, time

dll_name = os.path.join(os.path.dirname(__file__), 'sources/avbin')
pyglet.lib.load_library(dll_name)
sound = 'sources/bell.mp3'
schedule = []
# belled_schedule = []
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def exiter(dt):
    pyglet.app.exit()


# def clean_belled_schedule(fnow):
#     now_weekday = fnow.weekday()
#     if not belled_schedule:
#         return
#     for i in range(len(schedule)):
#         if schedule[i][0] != now_weekday:
#             del schedule[i]


def read_schedule(schedule_file_path='sources/schedule_' + weekdays[datetime.datetime.now().weekday()] + '.txt'):
    file = open(schedule_file_path, 'r', encoding='utf-8')
    sched = file.read()
    sched = sched.split('\n')
    for i in range(len(sched)):
        sched[i] = sched[i].strip()
        first = sched[i][:sched[i].index(':')]
        second = sched[i][sched[i].index(':') + 1:]
        sched[i] = (first, second)
    file.close()
    return sched


def play():
    song = pyglet.media.load(sound, streaming=False)
    song.play()
    pyglet.clock.schedule_once(exiter, song.duration)
    dnow = datetime.datetime.now()
    print(f'[{dnow.hour}:{dnow.minute}] The bell is sounding...')
    # belled_schedule.append((dnow.weekday(), dnow.time().minute))
    pyglet.app.run()


while True:
    now = datetime.datetime.now()
    schedule = read_schedule()
    if now.weekday() != 6:
        time.sleep(3)
        # clean_belled_schedule(now)
        for el in schedule:
            nowtime = str(now.time())[:2], str(now.time())[3:5]
            if nowtime[1] == el[1] and nowtime[0] == el[0]:
                # if (now.weekday, now.hour, now.minute) not in belled_schedule:
                play()
                time.sleep(61 - now.minute)
    else:
        time.sleep(60)
