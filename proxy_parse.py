from time import sleep
from os import system, getcwd
from colorama import Fore, init
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

from selenium import webdriver
from selenium.webdriver.chrome.options import Options 

fakeuseragent_client = UserAgent()

user_agent = {"User-Agent": fakeuseragent_client.random}


def prints_init() -> str:
	
	init()
	
	with open("print_data.txt", "r") as file_print_data:
		data_print = file_print_data.read()
	file_print_data.close()
	
	system("cls||clear")
	
	print(f"{Fore.RED}{data_print}")


def get_SOUP(urls) -> BeautifulSoup:
	
	webdriver_options = Options()
	webdriver_options.add_argument("--disable-logging")
	webdriver_options.add_argument("--headless=new")
	webdriver_options.add_experimental_option("excludeSwitches", ["enable-logging"])

	browser = webdriver.Chrome(options=webdriver_options)
	browser.get(urls[0])
	sleep(2)

	html_page = browser.page_source
	soup = BeautifulSoup(html_page, "html.parser")

	return soup

def main():

	prints_init()

	print(f"\n{Fore.RED}$$${Fore.WHITE}\tWAIT PLEASE...\n")
	
	urls    = ["https://checkerproxy.net/archive/2023-07-31"]
	soup    = get_SOUP(urls)
	trs     = soup.find("table", id="resultTable").find("tbody").find_all("tr")
	proxies = []

	for tr in trs:
		proxy = str(tr.find("td")).replace("<td>", "").replace("/td", "").replace(">", "").replace("<", "")
		proxies.append(proxy)

	print(f"{Fore.RED}$$${Fore.WHITE}\tPROXIES FINDED: {len(proxies)}\n\n{Fore.RED}$$${Fore.WHITE}\tPROXY WRITED TO <filtered_proxy.txt>")

	with open("filtered_proxy.txt", "w") as file_proxy:
		file_proxy.write("\n".join(proxies))

if __name__ == "__main__":
	main()