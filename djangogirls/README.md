# Blog DjangoGirls

Folder zawiera projekt blogu wykonanego w technologii Django. Blog został stworzony w ramach nauki frameworku Django, używając poradnika Djangogirls. 

### Dokumentacja 

[Poradnik Djangogirls](https://tutorial.djangogirls.org/pl/) 

## Kolejne kroki tworzenia bloga

### Instalacja Django i środowiska

Pierwszym krokiem w stworzeniu aplikacji django jest oczywiście instalacja samego frameworku. Przed instalacją, dobrą praktyką jest utworzenie wirtualnego środowiska, które umożliwia oddzielenie środowiska uruchomieniowego dal każdego projektu z osobna. Wprowadzane zmiany w środowisku naszej aplikacji nie wpłyną na inne aplikacje. 

Kolejne kroki instalacji django:
- stworzenie folderu roboczego dla projektu
- stworzenie środowiska wirtualnego za pomocą komendy
```bash
python -m venv py3122_env
```
- aktywacja środowiska wirtualnego
Aby aktywować środowisko witualne należy przejść do folderu Scripts naszego środowiska i uruchomić skrypt activate:
```bash
py3122_env\Scripts\activate
```
Po aktywowaniu środowiska nasza konsola powinna wyświetlać przed każdą linią nazwę naszego środowiska w nawiasach:
![image](https://github.com/perzan22/integracja_system-w_informatycznych_labs/assets/100600167/746f61de-df43-496b-8237-d33a49c97118)

- Instalacja Django
Po aktywacji wirtualnego środowiska można zainstalować Django.
Na początek należy zaktualizować naszego pip, aby był najnowszą wersją:
```bash
py -m pip install --upgrade pip
```
Po zaktualizowaniu pip można instalować najnowszą wersję Django i zapisać pakiety do pliku requiraments.txt
```bash
pip install -U django
pip freeze > requirements.txt
pip install -r requirements.txt
```
Po instalacji plik requiraments.txt powinien wyglądać tak:

![image](https://github.com/perzan22/integracja_system-w_informatycznych_labs/assets/100600167/38fcb612-4ea3-476e-81f4-fc037ae5a64b)

---

### Tworzenie projektu Django

Kolejnym krokiem jest utworzenie nowego projektu Django. Django posiada skrypty, które w prosty sposób tworzą projekt. Dzięki nim sami nie musimy tworzyć wszystkich plików ręcznie. Należy pamiętać, aby przy wszystkich komendach być w folderze roboczym!
- Tworzenie projektu Django
```bash
django-admin.exe startproject mysite .
```
Wywołany skrypt powinien stworzyć wszystkie potrzebne pliki i foldery do uruchomienia strony takie jak: [manage.py](./manage.py), [settings.py](./mysite/settings.py), czy [urls.py](./mysite/urls.py)

- Konfiguracja pliku settings.py
Plik [settings.py](./mysite/settings.py) zawiera całą konfiguracje naszego projektu. Przed rozpoczęciem tworzenia należy skonfigurować go pod aktualnie tworzony projekt. W naszym projekcie można wykonać pare zmian:
  - Zmiana TIME_ZONE na "Europe/Warsaw"
  - Zmiana języka LANGUAGE_CODE na "pl-pl"
  - Dodanie ścieżki do plików statycznych: należy dodać linijkę STATIC_ROOT = BASE_DIR / 'static' pod linijką STATIC_URL = '/static/'
  - Zmiana hosta na ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com'], ponieważ stronę będziemy wdrażać na witrynie pythonanywhere oraz wyświetlać lokalnie
- Dodanie bazy danych
Baza danych domyślnie jest ustawiona w pliku [settings.py](./mysite/settings.py) w części DATABESES. Domyślnie Django używa bazy SQLite3. Aby uruchomić bazę danych należy wpisać polecenie
```bash
py manage.py migrate
```
Po tej komendzie baza danych powinna zostać zainicjowana. 
- Uruchomienie serwera
```bash
py manage.py runserver
```
Po wpisaniu komendy można zobaczyć czy strona działa wpisując w przeglądarce: http://127.0.0.1:8000/

Jeśli wszystko poszło poprawnie strona powinna wyglądać tak:
![image](https://github.com/perzan22/integracja_system-w_informatycznych_labs/assets/100600167/16a8d20b-fb97-4f13-9477-88ba09de8a0f)

---

### Tworzenie modeli w Django

Modele są po prostu obiektem znanym z wielu języków programowania obiektowego, jednak Django zapisuje te obiekty od razu w bazie danych tworząc model. W naszym blogu przyda się model przechowujący informacje o postach na blogu. 

- Stworzenie aplikacji dla naszego projektu
Przed tworzeniem jakichkolwiek modeli należy stworzyć aplikację wewnątrz projektu. Robi to za nas Django za pomocą komendy:
```bash
py manage.py startapp blog
```
W projekcie powinien pojawić się teraz nowy folder 'blog' zawierający kolejne pliki. 

Po stworzeniu aplikacji należy w pliku [settings.py](./mysite/settings.py) dodać nasz blog do części INSTALLED_APPS i ta część pwoinna wyglądać następująco: 

![image](https://github.com/perzan22/integracja_system-w_informatycznych_labs/assets/100600167/fa2b3057-8224-48eb-90b9-d6c6861911d0)

- Tworzenie modelu post
Aby stworzyć model należy w pliku [blog\models](./blog/models.py) taki model zinicjować, nadać mu właściwości i stworzyć jego metody. Model Post może wyglądać w taki sposób:

```bash
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
```
W modelu nadajemy właściwości:
  - author - jest to klucz obcy będący kluczem autora danego posta
  - title - tytuł posta
  - text - treść posta
  - created_date - data utworzenia posta pobierana z metody timezone.now, która zwraca aktualną datę i godzinę
  - published_date - data opublikowania posta

Model post zawiera metodę publish(self), która ustawia datę publikacji na aktualną datę po wywołaniu metody oraz zapisuje post w bazie danych. Metoda __str__(self) zwraca tytuł posta.

- Dodanie tablicy dla modeli Post w bazie danych
Na początek należy zatwierdzić zmiany w modelu za pomocą komendy:
```bash
py manage.py makemigrations blog
```

Django powinien wtedy stworzyć model Post i wpisać go do pliku z migracjami. Teraz należy plik z migracjami zastosować do bazy danych:
```bash
py manage.py migrate blog
```

W ten sposób model Post powinien zostać dodany do bazy danych. 

---

### Administracja Django

Na razie w celu dodawania, czy usuwania postów potrzeba będzie użyć do tego panelu administracyjnego, które Django również nam dostarcza. W pliku [blog/admin.py](./blog/admin.py) należy podmienić kod na:
```bash
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

Dzięki temu model Post będzie widoczny w panelu administracyjnym. 

- Utworzenie superusera
Aby móc zalogować się na panel administracyjny, należy stworzyć konto administracyjne za pomocą komendy
```bash
py manage.py createsuperuser
```

Wyświetli się komunikat o danych do logowania. Należy je wpisać i zatwierdzić.

- Zalogowanie się na konto admina



