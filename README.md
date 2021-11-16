Репозиторий содержит примеры моих работ.

1. Каталог Docs
    1.1. Тест-кейсы
    1.2. Матрица трассировки
    1.3. Интеграционные тест-кейсы

2. Каталог Selenium - end-to-end тест для проверки работы с заявками на размещение рекламы (автоматизированный, pytest / Selenium WebDriver / Allure)

3. Автоматизироанные тесты API (pytest / requests / Allure)

Команда запуска тестов (Chrome в headless режиме): 

pytest --alluredir <каталог для хранения отчетов, находящийся в workspace CI> -m smoke
pytest --alluredir <каталог для хранения отчетов, находящийся в workspace CI> -m regress

При необходимости запуска в Firefox:
pytest --brower_name=firefix --alluredir <каталог для хранения отчетов, находящийся в workspace CI> -m smoke
pytest --brower_name=firefix --alluredir <каталог для хранения отчетов, находящийся в workspace CI> -m regress
