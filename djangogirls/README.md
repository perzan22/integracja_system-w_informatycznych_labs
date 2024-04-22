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

Po wejściu na sdres 127.0.0.1:8000/admin wyświetli się panel do zalogowania się na konto admina:

![image](https://github.com/perzan22/integracja_system-w_informatycznych_labs/assets/100600167/ea0085fb-48bd-40ba-bd63-38baa96d4e96)

Należy wpisać podane wcześniej dane logowania i wyświetli się panel administracyjny z modelem Posts: 

![image](https://github.com/perzan22/integracja_system-w_informatycznych_labs/assets/100600167/1bc0f8e7-2241-4329-bbd8-5835a7bc3f3f) 

W tym panelu można tworzyć, edytować i usuwać posty. 


---


### Wdrażanie na serwer zewnętrzny

Do tej pory nasza strona działała jedynie lokalnie na naszym komputerze. W tym kroku nasza strona zostanie wdrożona na serwer zewnętrzny. W tym celu skorzystano z serwisu [pythonanywhere.com](https://www.pythonanywhere.com/). 

- Stworzenie repozytorium projektowego na GitHub
- Wypchnięcie kodu źródłowego na GitHub
- Wdrożenie na serwis [pythonanywhere.com](https://www.pythonanywhere.com/)
  - Założenie konta na serwisie
  - Stworzenie API Tokena
  - Konfiguracja strony na serwisie
    
  Aby skonfigurować naszą stronę na serwisie wykorzystujemy do tego specjalną konsolę dostępną na serwisie. Jest to konsola podobna do tej na komputerze jednak działająca w środowisku PythonAnywhere. Na początek należy zainstalować pomocnika PythonAnywhere. W konsoli wpisujemy:
```bash
pip3.6 install --user pythonanywhere
```
Następnie należy skonfigurować PythonAnywhere z GitHubem, w moim przypadku wygląda komenda tak:
```bash
pa_autoconfigure_django.py https://github.com/perzan22/integracja_system-w_informatycznych_labs.git
```
Komenda ta pobiera kod z repozytorium, tworzy wirtualne środowisko, aktualizuje plik settings.py do takich pasujących dla PythonAnywhere, konfiguruje nową bazę danych, pliki statyczne oraz PythonAnywhere do obsługi aplikacji internetowej. 

  - Stworzenie superusera dla serwisu PythonAnywhere

Po tych wszystkich krokach należy wejść w zakładkę "Web" na PythonAnywhere i otrzymać link do strony internetowej. 

![image](https://github.com/perzan22/integracja_system-w_informatycznych_labs/assets/100600167/2ef0f05b-235c-4a9c-bfd9-0849a3f72169)

Jeśli w repozytorium znajdują się inne projekty konieczna może być zmiana "source code" w zakładce "Web", tak aby kodem źródłowym był odpowiedni folder: 

![image](https://github.com/perzan22/integracja_system-w_informatycznych_labs/assets/100600167/bf22b014-2d93-4c5a-bf5c-77e252f30bd6)

Teraz strona internetowa powinna dobrze działać pod adresem z serwisu pythonanywhere. 

---

### Django URLs

URL w Django jest niczym innym jak po prostu adresem do konkretnego widoku. Python interpretuje żądanie adresu i próbuje wyświetlić pasujący do URL-a widok. 

Dodawanie URL: 
- Importowanie adresów z folderu blog do głównego pliku [mysite\urls.py](./mysite/urls.py)

Aby naszą stroną główną był adres 127.0.0..1:8000 i wyświetlał dodanec posty należy wszystkie adresy przechowywać w folderze blog. Jednak aby strona czytała te adresy należy zaimporotwać je do głównego pliku z adreesami URL, a więc do [mysite\urls.py](./mysite/urls.py). Należy plik edytować do takiej formy: 
```bash
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
```
Dzięki funkcji include importujemy adresy z blog.urls do głównego pliku adresowego. 

- Stworzenie pliku [blog/urls.py](./blog/urls.py)
W folderze blog należy utworzyć pusty plik urls.py i dodać do niego następującą treść:
```bash
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
```
W powyższym kodzie na początek importujemy wszystkie widoki w folderze blog. Następnie ustalamy, że pod adresem bez żadnego rozwinięcia (127.0.0.1:8000) wyświetlany będzie widok pod nazwą post_list znajdujący się w widokach. Aktualjnie po próbie odpalenia serwera dostaniemy błąd, ponieważ żadnego widoku jeszcze nie ma. 

---

### Widoki Django

Widok jest plikiem, w którym przechowujemy logikę naszej aplikacji. Widok pobiera informacje z modelu i przekazuje je do szablonu HTML. Widoki przechowuje się w pliku [blog\views.py](./blog/views.py). 

- Stworzenie widoku
Widok należy stworzyć w pliku przytoczonym wcześniej.
```bash
def post_list(request):
    return render(request, 'blog/post_list.html', {})
```

Powyższy kod definiuje widok post_list. Na razie po odpaleniu strony pokaże się błąd, ponieważ nadal nie mamy szablonu HTML. 

---

### Szablony HTML

Szablony są tym co na stronie widać, za pomocą kodu HTML. Szablony umieszcza się w katalogu templates naszej aplikacji. 

- Utworzenie katalogu templates w folderze blog
- Utworzenie katalogu blog wewnątrz templates
- Utworzenie szablonu post_list.html wewnątrz templates/blog
- Wypełnienie szablonu kodem HTML
Przykładowy szablon statyczny:
```bash
<html>
    <head>
        <title>Django Girls blog</title>
    </head>
    <body>
        <div>
            <h1><a href="/">Django Girls Blog</a></h1>
        </div>

        <div>
            <p>published: 14.06.2014, 12:14</p>
            <h2><a href="">My first post</a></h2>
            <p>Aenean eu leo quam. Pellentesque ornare sem lacinia quam venenatis vestibulum. Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.</p>
        </div>

        <div>
            <p>published: 14.06.2014, 12:14</p>
            <h2><a href="">My second post</a></h2>
            <p>Aenean eu leo quam. Pellentesque ornare sem lacinia quam venenatis vestibulum. Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut f.</p>
        </div>
    </body>
</html>
```

---

### Dynamiczne dane Django

Dane przekazywane są z modeli do szablonu za pomocą widoków. To właśnie widoki należy edytować tak, aby szablony miały dostęp do modeli w bazach danych. 

- Import modelu do widoku
W pliku blog/views.py należy dodać import:
```bash
from django.shortcuts import render
from .models import Post
```

- Użycie QuerySet do odczytu danych
QuerySet jest niczym innym jak listą obieiktów w bazie danych. Za pomocą specjalnych funkcji możemy odczytywać potrzebne nam obiekty i przekazywać do aplikacji.
W pliku views można dodać:
```bash
from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {})
```

Powyższy kod tworzy tablicę posts i sortuje ją od najstarszej do najnowszej. Tą tablicę przekazujemy do szablonu za pomocą:
```bash
return render(request, 'blog/post_list.html', {'posts': posts})
```

Powyższej zmiany w kodzie. Do blog/post_list.html przekazujemy parametr 'posts', który przechowuje tablicę posts.

---

### Szablony Django

Szablony Django posiadają dodatkowe znaczniki ułatwiaujące nam pisanie kodu HTML. Na przykład można przekazywać dynamiczne właściwości modeli do szablonu za pomocą {{}}:
```bash
{{ posts }}
```

W ten sposób przekazaliśmy całą tablicę posts do szablonu. 

```bash
<div>
    <h1><a href="/">Django Girls Blog</a></h1>
</div>

{% for post in posts %}
    <div>
        <p>published: {{ post.published_date }}</p>
        <h2><a href="">{{ post.title }}</a></h2>
        <p>{{ post.text|linebreaksbr }}</p>
    </div>
{% endfor %}
```

Powyższy kod przekazuje każdy parametr posta za pomocą znacznika z pętlą for, która iteruje po wszystkich opublikowanych postach. 

---

### CSS

Aby strona wyglądała czytelniej i przyjemniej dla użytkowników, należy ją wzbogacić o kod CSS. W naszej aplikacji dodatkowo użyjemy bootstrapa do łatwiej zmiany stylu. Należy w pliku blog/templates/blog/post_list.html dodać między znacznikami head te dwie linijki:

```bash
<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
```

Dzięki temu nasza strona już nabiera stylu: 

![image](https://github.com/perzan22/integracja_system-w_informatycznych_labs/assets/100600167/3bd4344a-e077-4cbe-b304-3731fa9c672d)

- Tworzenie plików statycznych
Pliki statyczne to pliki, które dla każdego użytkownika będą takie same. Są to na przykłąd arkusze stylów lub foldery z obrazkami. Pliki te należy umieścić w nowym folderze static wewnątrz folderu blog. W folderze static można stworzyć kolejny folder o nazwie np. css i w nim tworzyć pliki css ze stylami. Po stworzeniu pliku blog.css można go wypełnić poniższym kodem:
```bash
.page-header {
    background-color: #C25100;
    margin-top: 0;
    padding: 20px 20px 20px 40px;
}

.page-header h1, .page-header h1 a, .page-header h1 a:visited, .page-header h1 a:active {
    color: #ffffff;
    font-size: 36pt;
    text-decoration: none;
}

.content {
    margin-left: 40px;
}

h1, h2, h3, h4 {
    font-family: 'Lobster', cursive;
}

.date {
    color: #828282;
}

.save {
    float: right;
}

.post-form textarea, .post-form input {
    width: 100%;
}

.top-menu, .top-menu:hover, .top-menu:visited {
    color: #ffffff;
    float: right;
    font-size: 26pt;
    margin-right: 20px;
}

.post {
    margin-bottom: 70px;
}

.post h2 a, .post h1 a:visited {
    color: #000000;
}
```

Następnie można dodać klasy do kodu HTML:
```bash
<div class="content container">
    <div class="row">
        <div class="col-md-8">
            {% for post in posts %}
                <div class="post">
                    <div class="date">
                        <p>published: {{ post.published_date }}</p>
                    </div>
                    <h2><a href="">{{ post.title }}</a></h2>
                    <p>{{ post.text|linebreaksbr }}</p>
                </div>
            {% endfor %}
        </div>
    </div>
</div>
```

Oraz zaimportować arkusz css do pliku HTML oraz font z Internetu:

```bash
<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
<link href="//fonts.googleapis.com/css?family=Lobster&subset=latin,latin-ext" rel="stylesheet" type="text/css">
<link rel="stylesheet" href="{% static 'css/blog.css' %}">
```

Strona po odpaleniu powinna wyglądać już przyjemnie. 

---

### Rozbudowa szablonu Django

Szablony Django umożliwiają rozszerzanie szablonów. Można stworzyć szablon bazowy i w zależności od tego co chcemy na stronie wyświetlić to o konkretny szablon go rozszerzamy. 
- Tworzenie szablonu bazowego
W blog/temkplates/blog należy stworzyc plik base.html i zapełnić go kodem:
```bash
<body>
    <div class="page-header">
        <h1><a href="/">Django Girls Blog</a></h1>
    </div>
    <div class="content container">
        <div class="row">
            <div class="col-md-8">
            {% block content %}
            {% endblock %}
            </div>
        </div>
    </div>
</body>
```
Należy zauważyć znaczniki { % block content % } i { % endblock % }, między którymi można umieścić blok o któy rozszerzamy bazowy. 

- Dostosowanie szablonów do pliku bazowego
Nasz szablon post_list.html może teraz wyglądać tak:
```bash
{% extends 'blog/base.html' %}

{% block content %}
    {% for post in posts %}
        <div class="post">
            <div class="date">
                {{ post.published_date }}
            </div>
            <h2><a href="">{{ post.title }}</a></h2>
            <p>{{ post.text|linebreaksbr }}</p>
        </div>
    {% endfor %}
{% endblock %}
```

I dzięki qwykorzystaniu znaczników  { % block content % } i { % endblock % } będzie wpasowywał się do pliku bazowego. Znacznik {% extends %} wskazuje jaki plik jest plikiem bazowym. 

---

### Rozbudowa aplikacji

Aplikację można reozbudować chociażby o wyświetlenie pojedynczego wpisu. 
- Dodanie linku do pojedynczego posta
Należy zamienić linię w szablonie post_list z tytułem strony:
```bash
<h1><a href="{% url 'post_detail' pk=post.pk %}">{{ post.title }}</a></h1>
```
W ten sposób dodaliśmy link w szablonie. Znacznik tutaj dodany generuje nam URL. 'post_detail' oznacza, że szukamy adresu zaczynającego się od 127.0.0.1:8000, natomiast 'pk=post.pk' dodaje do adresu atrybut pk z wartością unikalnego klucza posta. 

- Dodanie URL
Aby URL mógł zostać zinterpretowany należy dodać go w pliku urls.py. Dodajemy URL:
```bash
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
```

Django tworzy teraz ścieżkę 127.0.0.1:8000/post/<int:pk>/ int:pk jest niczym innym jak kluczem naszego posta. Po próbie dostania się na ten URL łączy się z widokiem post_detail. 

- Tworzenie widoku post_detail
Aby strona nie wyświetlała błędu należy dodać widok w pliku blog/views.py. Do istniejącego kodu dodajemy import:
```bash
from django.shortcuts import render, get_object_or_404
```
oraz nowy widok:
```bash
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
```

Dzięki temu stworzyliśmy widok dla post_detail. W przypadku braku posta o danym id wyświetli się błąd 404 dzięki funkcji get_object_or_404.

- Stworzenie szablonu post_detail
Ostatnim punktem jest stworzenie szablonu Django post detail, aby wyświetlał jeden post. Należy stworzyć nowy plik w katalogu blog/templates/blog o nazwie post_detail.html i wypełnić go kodem:
```bash
{% extends 'blog/base.html' %}

{% block content %}
    <div class="post">
        {% if post.published_date %}
            <div class="date">
                {{ post.published_date }}
            </div>
        {% endif %}
        <h2>{{ post.title }}</h2>
        <p>{{ post.text|linebreaksbr }}</p>
    </div>
{% endblock %}
```
Jak widać znowu wykorzystujemy znacznik Django do rozszerzenia szablonu bazowego. Aktualnie po wciśnięciu na tytuł powinniśmy otrzymać poprawny szablon jednego posta.

---




