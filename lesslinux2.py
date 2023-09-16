#Задание 1.
#Условие:
#Дополнить проект тестами, проверяющими команды вывода списка файлов (l) и разархивирования с путями (x).

from checkers import checkout

out = "/home/user/out"


def test_step1():
    res1 = checkout("cd {};7z x arx2.7z".format(out), "Everything is Ok")
    res2 = checkout("ls {}".format(out), "test1")
    assert res1 and res2, "test1 FAIL"

def test_step2():
    assert (checkout("cd {};7z l arx2.7z".format(out), "test2")), "test2 FAIL"

#Задание 2.

# Установить пакет для расчёта crc32
#sudo apt install libarchive-zip-perl
# Доработать проект, добавив тест команды расчёта хеша (h). Проверить, что хеш совпадает с рассчитанным командой crc32.

from checkers import checkout
from checkers import calc_crc32

out = "/home/user/out"


def test_step1():
    assert (checkout("cd {};7z h arx2.7z".format(out), calc_crc32(None, 'hash_crc'))), "Test1 FAIL"
