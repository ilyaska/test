# -*- coding: utf-8 -*-
'''
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
net = input("Введите IP-сеть в формате 10.1.1.0/24: ")
#net = "192.168.1.1/24"
ip, mask = net.split('/')
octets = ip.split('.')
bin_mask = "1" * int(mask) + "0" * (32-int(mask))
print(f'''Network:
{octets[0]:<8} {octets[1]:<8} {octets[2]:<8} {octets[3]:<8}
{int(octets[0]):08b} {int(octets[1]):08b} {int(octets[2]):08b} {int(octets[3]):08b}

Mask:
/{mask}
{int(bin_mask[0:8], 2):<8} {int(bin_mask[8:16], 2):<8} {int(bin_mask[16:24], 2):<8} {int(bin_mask[24:32], 2):<8}
{bin_mask[0:8]} {bin_mask[8:16]} {bin_mask[16:24]} {bin_mask[24:32]}
''')
