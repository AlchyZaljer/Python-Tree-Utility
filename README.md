# **Python Tree Utility**

### Консольное приложение для отображения структуры файлов и директорий в виде дерева

## **Функциональность**

1. Вывод структуры каталогов в виде дерева с декоративным оформлением.

2. Вывод количества найденных директорий и файлов.

3. Поддержка параметров запуска.

## **Аргументы командной строки**

- `-d` или `--directory` (опционально):
  - Указывает корневую директорию, с которой начинать сканирование.
  - По умолчанию используется текущая директория.

- `-l` или `--level` (опционально):
  - Ограничивает глубину отображаемой структуры.
  - Пример: `--level 2` выведет только два уровня вложенности.
 
### Запуск утилиты:

    python tree.py [options] [dir]


## **Примеры использования**

1. **Запуск утилиты без опций с указанием пути**:
     ```bash
     python tree.py ./test_data/
    
    ./test_data/
    ├── books
    │   ├── Dukaj_Other_songs.pdf
    │   ├── Jonathan Strange & Mr Norrell.pdf
    │   └── Piranesi.pdf
    └── movies
        ├── fantasy
        │   ├── Edward Scissorhands.avi
        │   ├── LOTR
        │   │   └── The Two Towers.avi
        │   └── Time Bandits.avi
        └── sci-fy
            ├── 12 Monkeys.avi
            └── Blade runner.avi
    
    6 directories, 8 files
     ```
   
2. **Запуск утилиты с указанием пути test_data и опцией для отображения только директорий**:
    ```bash
    python tree.py -d test_data
    
    test_data
    ├── books
    └── movies
        ├── fantasy
        │   └── LOTR
        └── sci-fy
    
    6 directories
    ```

3. **Запуск утилиты из корневой директории с опцией -L 1**:
    ```bash
    python tree.py -L 1
    
    .
    ├── bin
    ├── boot
    ├── dev
    ├── etc
    ├── home
    ├── lib
    ├── proc
    ├── root
    ├── sys
    ├── tmp
    ├── usr
    └── var
    
    13 directories, 0 files
    ```
