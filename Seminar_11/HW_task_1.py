'''
Написать программу на Python, которая будет проводить сканирование с использованием nmap.
'''
import nmap


def scan_network(target):
    # Нужно ввести путь, где расположена программа nmap на компьютере
    nm = nmap.PortScanner(nmap_search_path=('C:\\Program Files (x86)\\Nmap\\nmap.exe',))

    print(f'Сканирование {target}...')

    nm.scan(hosts=target, arguments='-sP')

    for host in nm.all_hosts():
        print(f'Хост: {host}')
        print(f'Статус: {nm[host].state()}')
        if 'top' in nm[host]:
            for port in nm[host]['top']:
                print(f'Порт: {port}, Состояние: {nm[host]['top'][port]['state']}')
        print()

if __name__ == '__main__':
    target = input('Введите IP-адрес или диапозон для сканирования: ')
    scan_network(target)
