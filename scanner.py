import socket
import threading
import argparse

semaforo = threading.Semaphore(100)

def scan_port(host, port):
    with semaforo:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            
            resultado = sock.connect_ex((host, port))
            
            if resultado == 0:
                try:
                    sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
                    banner = sock.recv(1024).decode("utf-8", errors="ignore").strip()
                except:
                    banner = "sem banner"
                
                print(f"Porta {port}: ABERTA | Banner: {banner[:100]}")
            
            sock.close()

        except:
            pass

def main():
    # Define os argumentos da CLI
    parser = argparse.ArgumentParser(description="Port Scanner com banner grabbing")
    parser.add_argument("--host", required=True, help="Host alvo (ex: scanme.nmap.org)")
    parser.add_argument("--start", type=int, default=1, help="Porta inicial (padrão: 1)")
    parser.add_argument("--end", type=int, default=1024, help="Porta final (padrão: 1024)")
    
    args = parser.parse_args()
    
    print(f"\nEscaneando {args.host} — portas {args.start} a {args.end}\n")
    
    threads = []
    for porta in range(args.start, args.end + 1):
        t = threading.Thread(target=scan_port, args=(args.host, porta))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\nScan concluído!")

if __name__ == "__main__":
    main()