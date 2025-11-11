## Запуск тестов и получение отчёта о покрытии


1. Установите зависимости:
   ```bash
   pip install coverage
   ```
2. Запустите тесты с измерением покрытия:

    ```bash
    cd hw_5 # при необходимости переходим в директорию hw_5
    coverage run -m unittest issue_5.py -v
    ```

3. Сгенерируйте отчёт в HTML:

    ```bash
    coverage html
    ```

4. Откройте отчёт в браузере:
    ```bash
    open htmlcov/index.html  # для macOS
    # или
    start htmlcov\index.html  # для Windows
    ```

5. Ожидаемый результат

    См. файл result.txt.