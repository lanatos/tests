Репозиторий содержит примеры моих работ.

1. Каталог Selenium - end-to-end тест для проверки работы с заявками на размещение рекламы (автоматизированный, pytest / Selenium WebDriver / Allure)

2. Каталог API -Автоматизированные тесты API (pytest / requests / Allure)

Команда запуска тестов (Chrome в headless режиме): 

	pytest --alluredir <каталог для хранения отчетов, находящийся в workspace CI> -m smoke

	pytest --alluredir <каталог для хранения отчетов, находящийся в workspace CI> -m regress

При необходимости запуска в Firefox:

	pytest --brower_name=firefix --alluredir <каталог для хранения отчетов, находящийся в workspace CI> -m smoke

	pytest --brower_name=firefix --alluredir <каталог для хранения отчетов, находящийся в workspace CI> -m regress
