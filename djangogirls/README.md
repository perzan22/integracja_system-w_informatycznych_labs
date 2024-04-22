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


