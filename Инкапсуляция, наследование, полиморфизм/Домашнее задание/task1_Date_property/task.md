Реализовать для класса `Date` свойства день, месяц и год.
- Setter дня должен проверять, что значение является целочисленным, положительным и не большим 31 для всех дат.
- Setter месяца должен проверять, что значение является целочисленным, большим 1 и меньшим 12 для всех дат.
- Setter года должен проверять, что значение является целочисленным и положительным.

Конструктор должен проверять с помощью метода `is_valid_date`, что сочетание день, месяц и год корректны, 
в противном случае генерировать ошибку `ValueError`.
