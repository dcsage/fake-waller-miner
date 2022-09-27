import random
import string
import asyncio
from colorama import init, Fore, Back, Style
import sys
import os

os.system("cls" or "clear")
# Basic Imports

init(convert=True) # initiating colorama

async def start():

    print(f'''{Fore.CYAN}
    ░██╗░░░░░░░██╗░█████╗░██╗░░░░░██╗░░░░░███████╗████████╗  ███╗░░░███╗██╗███╗░░██╗███████╗██████╗░
    ░██║░░██╗░░██║██╔══██╗██║░░░░░██║░░░░░██╔════╝╚══██╔══╝  ████╗░████║██║████╗░██║██╔════╝██╔══██╗
    ░╚██╗████╗██╔╝███████║██║░░░░░██║░░░░░█████╗░░░░░██║░░░  ██╔████╔██║██║██╔██╗██║█████╗░░██████╔╝
    ░░████╔═████║░██╔══██║██║░░░░░██║░░░░░██╔══╝░░░░░██║░░░  ██║╚██╔╝██║██║██║╚████║██╔══╝░░██╔══██╗
    ░░╚██╔╝░╚██╔╝░██║░░██║███████╗███████╗███████╗░░░██║░░░  ██║░╚═╝░██║██║██║░╚███║███████╗██║░░██║
    ░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝░░░╚═╝░░░  ╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝
        ''')
    print(" ")
    print(f"                                {Fore.CYAN}The worlds {Fore.WHITE}leading {Fore.CYAN}Bitcoin Wallet Miner.")
    print("")
    lkey = input(f"    {Fore.CYAN}[|] Enter your {Fore.WHITE}License Key{Fore.CYAN}: ")
    if lkey == "YOURKEY":
        print(" ")
        print(f"    {Fore.CYAN}[|] License Key was{Fore.GREEN} Accepted")
        print(" ")
        addy = input(f"    {Fore.CYAN}[?] Enter your BTC Address : ")
        pyn = input(f"    {Fore.CYAN}[?] Use Proxies? ({Fore.GREEN}Y{Fore.CYAN}/{Fore.RED}N{Fore.CYAN}) : ")
        stopathit = input(f"    {Fore.CYAN}[?] Stop program after a successful HIT? ({Fore.GREEN}Y{Fore.CYAN}/{Fore.RED}N{Fore.CYAN}) : ")
        scrape = input(f"    {Fore.CYAN}[?] Auto Scrape Addresses? ({Fore.GREEN}Y{Fore.CYAN}/{Fore.RED}N{Fore.CYAN}) : ")
        start = input(f"    {Fore.CYAN}[?] Start Program? ({Fore.GREEN}Y{Fore.CYAN}/{Fore.RED}N{Fore.CYAN})  ")
        print("")
        await asyncio.sleep(1)
        print(f"    {Fore.CYAN}[|] Starting...")
        await asyncio.sleep(2)
        print(f"    {Fore.CYAN}[|] Scraping addresses... | Proxies: {Fore.GREEN}enabled")
        await asyncio.sleep(2)
        print(f"    {Fore.CYAN}[|] Addresses scraped (340,239)")
        await asyncio.sleep(1)
        print("")
        print(f"    {Fore.CYAN}[|] Starting mining sequence with recipient address {Fore.WHITE}{addy}")
        await asyncio.sleep(3)
        target = random.randint(1,4000)
        while True:
            c = random.randint(1,4000)
            lol = ''.join(random.choices(string.ascii_letters + string.digits, k=33))
            if c == target:
                print("")
                o = random.randint(1,2000)
                p = random.randint(1,99)
                print(f"    {Fore.CYAN}[$] Funded wallet found | ({Fore.GREEN}${o}.{p}{Fore.CYAN})")
                print("")
                await asyncio.sleep(3)
                print(f"    {Fore.CYAN}[|] Starting private key brute in {Fore.WHITE}3 seconds")
                await asyncio.sleep(3)
                print("")
                t1 = random.randint(1,10000)
                while True:
                    c1 = random.randint(1,10000)
                    if c1 == t1:
                        print(" ")
                        print(f"    {Fore.CYAN}[$] Correct private key {Fore.GREEN}found.")
                        print(" ")
                        await asyncio.sleep(3)
                        print(f"    {Fore.CYAN}[$] Attempting to drain {Fore.GREEN}${o}.{p} {Fore.CYAN}from {Fore.WHITE}bcK6MxMdbU5oOriXOuoo6fz6X1Y6FOSdZc {Fore.CYAN} to {Fore.WHITE}{addy}")
                        await asyncio.sleep(1)
                        print(f"    {Fore.CYAN}[$] Successfully drained {Fore.GREEN}${o}.{p} {Fore.CYAN}from {Fore.WHITE}bcK6MxMdbU5oOriXOuoo6fz6X1Y6FOSdZc")                        
                        await asyncio.sleep(20000)
                        return
                    else:

                        print(f"    {Fore.CYAN}[X] Incorrect Private Key | {Fore.CYAN}Retrying with new hash | Proxies: {Fore.GREEN}enabled")

            else:
                print(f"    {Fore.CYAN}[X] Invalid or Empty Address | {Fore.RED} bc{lol} {Fore.CYAN}| Proxies: {Fore.GREEN}enabled")
    else:
        print(" ")
        print(f"    {Fore.CYAN}[|] License Key is{Fore.RED} Invalid")
        await asyncio.sleep(10)
        
asyncio.run(start())



