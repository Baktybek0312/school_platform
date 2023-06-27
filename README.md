**Бэкенд для образовательного  приложения**

Для того чтобы запусть данный проект вам необходимо создать папку:

mkdir "название вашей папки, например: mkdir test", далее зайти в эту папку с командой cd test или как вы его назвали.

С клонируйте репозиторию: git clone https://github.com/Baktybek0312/educational_platform_kraken.git

вы можете узнать больше здесь: https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/adding-and-cloning-repositories/cloning-and-forking-repositories-from-github-desktop

Зависимости/пакеты серверной части Создайте виртуальную среду для Python 3.

_Перейдите к терминалу и запустите:_
virtualenv env

Замените env на фактическое имя, которое вы хотите дать своей виртуальной среде Python.

_Активируйте виртуальную среду_
source env/bin/activate

_Сначала нам нужно установить все библиотеки pip install -r requirements.txt_

_Coздайте файл .env и настройте как на экземпляре .env.example_
SECRET_KEY=your_secret_key DEBUG_MODE=True DATABASE_URL=postgres://user:password@host:port/database_name