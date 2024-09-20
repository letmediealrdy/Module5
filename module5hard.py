from time import sleep


class UrTube:
    users = []
    videos = []
    current_user = None

    def register(self, nickname, password, age):
        for user in self.users:
            if user.name == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        self.users.append(User(nickname, password, age))
        self.log_in(nickname, password)

    def log_in(self, nickname, password):
        for user in self.users:
            if user.name == nickname and user.password == hash(password):
                self.current_user = user

    def log_out(self):
        self.current_user = None

    def add(self, *video):
        for v in video:
            if v not in self.videos:
                self.videos.append(v)

    def get_videos(self, word):
        matches = []
        for v in self.videos:
            if word.casefold() in v.title.casefold():
                matches.append(v.title)
        return matches

    def watch_video(self, name):
        for v in self.videos:
            if v.title == name:
                if self.current_user:
                    if v.mode and self.current_user.age < 18:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    else:
                        time_now = 0
                        for i in range(v.duration):
                            time_now += 1
                            print(time_now)
                            sleep(1)
                        print('Конец видео')
                else:
                    print("Войдите в аккаунт, чтобы смотреть видео")


class Video:
    def __init__(self, title, duration, **adult_mode):
        self.title = title
        self.duration = duration
        self.mode = False
        self.mode = adult_mode


class User:
    def __init__(self, nickname, password, age):
        self.name = nickname
        self.password = hash(password)
        self.age = age


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user.name)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
