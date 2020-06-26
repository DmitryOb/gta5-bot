подготовка к запуска бота:
1. файлу ./clickermann/Clickermann.exe нужно сделать по умолчанию запускаемым от имени администратора: Right-click the application >> Go to Properties >> Click the Compatibility tab >> Check "Run this program as an administrator" >> Click OK
2. необходимо установить интерпретатор питона на ПК: https://www.python.org/downloads/ -> Download Python 3.8.3 (сейчас это python-3.8.3.exe)
3. из корня проекта запускаем закачку всех необходимых зависимостей из cmd: pip install -r requirements.txt
4. pip install Pillow
5. установить тессеракт https://github.com/UB-Mannheim/tesseract/wiki в 'C:/Program Files/Tesseract-OCR/tesseract.exe'

порядок запускать бота, подготовки в игре:
1. сама игра должна работать в режиме "оконный без рамок"
2. в игре подьезжаем на машине к шахте, открываем багажник, подьезжаем так чтобы при нажатии "I" (вызов инвентаря) мы видели содержимое багажника и одновременно могли зажимать "E" для копки
3. сворачиваем игру, запускаем run.bat, разворачиваем игру
