import socket
import ipaddress

# Чтение списка доменов
file_path = 'domains.txt'
with open(file_path, 'r') as file:
    domains = file.readlines()

domains = [domain.strip() for domain in domains]

# Получение IP адреса для каждого домена и сохранение в файл
output_file = 'ip_addresses.txt'  # Имя файла для сохранения IP-адресов
with open(output_file, 'w') as file:
    ip_addresses = []  # Список для хранения найденных IP-адресов
    for domain in domains:
        try:
            ip_address = socket.gethostbyname(domain)
            ip_addresses.append(ip_address)
            file.write(f"Домен: {domain} - IP адрес: {ip_address}\n")
            print(f"Домен: {domain} - IP адрес: {ip_address}")
        except socket.gaierror:
            file.write(f"Домен {domain} не может быть разрешен\n")
            print(f"Домен {domain} не может быть разрешен")

    # Получение диапазонов IP-адресов
    ip_ranges = []
    for ip in ip_addresses:
        try:
            network = ipaddress.ip_network(ip)
            ip_ranges.append(network)
        except ValueError:
            print(f"Невозможно получить диапазон для IP-адреса: {ip}")

    # Сохранение диапазонов IP-адресов в файл
    file.write("\nДиапазоны IP-адресов:\n")
    for ip_range in ip_ranges:
        file.write(str(ip_range) + "\n")
        print(f"Найден диапазон IP-адресов: {ip_range}")

print(f"Список IP-адресов и диапазоны сохранены в файл: {output_file}")