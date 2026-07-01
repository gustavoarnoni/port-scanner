# 🔍 Port Scanner

A simple port scanner written in Python with multithreading and banner grabbing.

## Features

- TCP port scanning
- Multithreaded (fast)
- Banner grabbing (identifies running services)
- CLI interface

## Usage

```bash
python3 scanner.py --host  --start  --end 
```

## Examples

```bash
# Full scan (ports 1-1024)
python3 scanner.py --host scanme.nmap.org

# Specific range
python3 scanner.py --host scanme.nmap.org --start 1 --end 100

# Single port
python3 scanner.py --host scanme.nmap.org --start 80 --end 80
```

## Sample Output

```bash
Escaneando scanme.nmap.org — portas 1 a 1024
Porta 22: ABERTA | Banner: SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.13
Porta 80: ABERTA | Banner: HTTP/1.1 200 OK ... Server: Apache/2.4.7 (Ubuntu)
Scan concluído!
```

## Legal

Only use against hosts you own or have explicit permission to scan.