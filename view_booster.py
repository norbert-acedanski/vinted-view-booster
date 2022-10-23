import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

my_links = ["https://www.vinted.pl/kobiety/akcesoria/kapelusze-i-czapki-231/2307801080-kapelusz-bezowy" ,
            "https://www.vinted.pl/kobiety/torby/torby-do-reki/2307762449-torebka-w-panterke-mala", 
            "https://www.vinted.pl/mezczyzni/ubrania/swetry-bluzy/swetry-i-bluzy-z-kapturem/1865157093-biala-bluza-mister-tee-skrrt", 
            "https://www.vinted.pl/kobiety/akcesoria/kapelusze-i-czapki/czapki-zimowe/1865157044-czapka-czarna-z-rozowym-logo", 
            "https://www.vinted.pl/kobiety/akcesoria/kapelusze-i-czapki/czapki-zimowe/1865157001-czapka-czarna",
            "https://www.vinted.pl/mezczyzni/obuwie/tenisowki-i-trampki/1865156894-lacoste-tenisowki-bialo-zielone", 
            "https://www.vinted.pl/mezczyzni/ubrania/garnitury-i-blezery/spodnie-garniturowe/1865156847-granatowe-eleganckie-spodnie-hm", 
            "https://www.vinted.pl/mezczyzni/ubrania/sportowe-ubrania-i-akcesoria/koszulki-z-krotkim-rekawem-t-shirty/1865156784-biala-koszulka-malopolska-na-start", 
            "https://www.vinted.pl/mezczyzni/ubrania/topy-and-t-shirty/t-shirty/t-shirty-gladkie/1865156686-czarna-koszulka-champion", 
            "https://www.vinted.pl/mezczyzni/ubrania/swetry-bluzy/swetry-z-okraglym-dekoltem/1865156614-sweter-bordowy-jack-jones", 
            "https://www.vinted.pl/mezczyzni/ubrania/topy-and-t-shirty/t-shirty/t-shirty-gladkie/1865156526-koszulka-czarna-jack-jones", 
            "https://www.vinted.pl/mezczyzni/ubrania/topy-and-t-shirty/t-shirty/t-shirty-gladkie/1865156493-koszulka-kappa-jasno-mietowa", 
            "https://www.vinted.pl/mezczyzni/ubrania/okrycia-wierzchnie/plaszcze/przeciwdeszczowe/1865156427-kurtka-plaszcz-z-kapturem-yourturn", 
            "https://www.vinted.pl/kobiety/akcesoria/kapelusze-i-czapki/czapki-zimowe/1865156403-czapka-zimowa-nyc", 
            "https://www.vinted.pl/mezczyzni/ubrania/swetry-bluzy/swetry-z-okraglym-dekoltem/1865156376-sweter-szary-oliver", 
            "https://www.vinted.pl/mezczyzni/ubrania/plaszcze-i-kurtki/trencze/1865156327-plaszcz-czarny", 
            "https://www.vinted.pl/mezczyzni/ubrania/swetry-bluzy/bluzy/1865156292-bluza-szara-z-kapturem-dwd", 
            "https://www.vinted.pl/kobiety/ubrania/sukienki/krotkie-sukienki/1865156237-sukienka-szara-boohoo", 
            "https://www.vinted.pl/kobiety/ubrania/jeansy/dzinsy-skinny/1865156196-jeansy-biale-divided-rozm-34", 
            "https://www.vinted.pl/kobiety/ubrania/jeansy/dzinsy-do-kostek/1865156165-spodnie-damskie-mango-jeans-rozm-34-bawelniane", 
            "https://www.vinted.pl/kobiety/ubrania/topy-koszulki-i-t-shirty/t-shirty/1865156143-bluzka-szara-z-koralikami-mohito", 
            "https://www.vinted.pl/mezczyzni/ubrania/spodnie/spodnie-z-szerokimi-nogawkami/1865156118-spodnie-meskie-zielonkawe-aiglat", 
            "https://www.vinted.pl/mezczyzni/ubrania/swetry-bluzy/inne/1865156077-bluzka-czerwona-boston-bpc", 
            "https://www.vinted.pl/mezczyzni/ubrania/spodnie/spodnie-eleganckie/1865156060-spodnie-czarne-reserved-rozm-54", 
            "https://www.vinted.pl/mezczyzni/ubrania/spodnie/chinosy/1865156037-ciemne-spodnie-review", 
            "https://www.vinted.pl/mezczyzni/ubrania/dzinsy/dzinsy-straight-fit/1865156007-jeansy-niebieskie-z-plamkami", 
            "https://www.vinted.pl/mezczyzni/akcesoria-dodatki/torby/torby-na-ramie/1865155976-torba-naramienna-regulowana", 
            "https://www.vinted.pl/mezczyzni/akcesoria-dodatki/bizuteria/bransolety/1865155924-bransoletka-meska", 
            "https://www.vinted.pl/mezczyzni/akcesoria-dodatki/szaliki-szale-chusty/szaliki-z-dzianiny/1865155879-szalik-trojkolorowy-bawelniany", 
            "https://www.vinted.pl/mezczyzni/ubrania/topy-and-t-shirty/t-shirty/t-shirty-z-nadrukiem/1865155842-koszulka-t-shirt-z-guzikami", 
            "https://www.vinted.pl/mezczyzni/ubrania/topy-and-t-shirty/t-shirty/t-shirty-z-nadrukiem/1865155775-koszulka-szara-z-nadrukiem-rozmiar-l", 
            "https://www.vinted.pl/mezczyzni/ubrania/topy-and-t-shirty/t-shirty/t-shirty-z-nadrukiem/1865155754-t-shirt-fifty-five-nowa", 
            "https://www.vinted.pl/mezczyzni/ubrania/swetry-bluzy/swetry-i-bluzy-z-kapturem/1865155729-bluza-bialo-szara-z-kapturem", 
            "https://www.vinted.pl/mezczyzni/ubrania/swetry-bluzy/bluzy-rozpinane/1865155709-sweter-gruby-gin-tonic", 
            "https://www.vinted.pl/mezczyzni/akcesoria-dodatki/szaliki-szale-chusty/szaliki-z-dzianiny/1865155681-szalik-szary-hm", 
            "https://www.vinted.pl/mezczyzni/akcesoria-dodatki/szaliki-szale-chusty/duze-szale-i-chusty/1865155664-szalik-abrams-wielokolorowy", 
            "https://www.vinted.pl/mezczyzni/ubrania/swetry-bluzy/swetry-z-okraglym-dekoltem/1865155630-sweter-soliver-niebieski", 
            "https://www.vinted.pl/mezczyzni/kosmetyki/perfumy/1865155582-woda-toaletowa-la-cobra-green", 
            "https://www.vinted.pl/mezczyzni/ubrania/topy-and-t-shirty/t-shirty/t-shirty-z-dlugim-rekawem/1865155544-bluzka-szara-z-dlugim-rekawem", 
            "https://www.vinted.pl/mezczyzni/ubrania/swetry-bluzy/swetry-w-serek/1865155511-sweter-ciemny-w-serek", 
            "https://www.vinted.pl/mezczyzni/ubrania/swetry-bluzy/swetry-z-golfem/1865155487-sweter-ciemny-originals", 
            "https://www.vinted.pl/mezczyzni/ubrania/swetry-bluzy/swetry-z-okraglym-dekoltem/1865155465-sweter-szary-oliver", 
            "https://www.vinted.pl/mezczyzni/akcesoria-dodatki/szaliki-szale-chusty/szaliki-z-dzianiny/1865155437-szalik-w-paski", 
            "https://www.vinted.pl/mezczyzni/ubrania/plaszcze-i-kurtki/bosmanki/1865155419-plaszcz-czarny", 
            "https://www.vinted.pl/mezczyzni/obuwie/eleganckie-buty/1865155390-buty-eleganckie-z-zamszu", 
            "https://www.vinted.pl/mezczyzni/akcesoria-dodatki/szaliki-szale-chusty/duze-szale-i-chusty/1865155354-szalik-szary", 
            "https://www.vinted.pl/mezczyzni/ubrania/swetry-bluzy/swetry-z-okraglym-dekoltem/1865155323-sweter-czarny-livergy", 
            "https://www.vinted.pl/mezczyzni/obuwie/inne/1865155281-buty-przejsciowe-vty"]
aga_links = ["https://www.vinted.pl/kobiety/ubrania/topy-koszulki-i-t-shirty/inne/2027376673-krotki-t-shirt",
             "https:/www.vinted.pl/kobiety/ubrania/topy-koszulki-i-t-shirty/bluzki-bez-rekawow/2027363892-topik-w-paseczki",
             "https:/www.vinted.pl/kobiety/ubrania/topy-koszulki-i-t-shirty/topy-z-baskinka/2027350006-czarny-top",
             "https:/www.vinted.pl/kobiety/ubrania/topy-koszulki-i-t-shirty/podkoszulki/2027335825-szary-t-shirt-z-wilkiem",
             "https:/www.vinted.pl/kobiety/ubrania/topy-koszulki-i-t-shirty/crop-topy/2027319016-biala-bluzeczka-z-wiazaniem-na-szyi",
             "https:/www.vinted.pl/kobiety/akcesoria/bizuteria/korale-wisiorki-naszyjniki/2027242526-bransoletka-dla-mlodziutkiej-nastolatki-opakowanie-w-zestawie",
             "https:/www.vinted.pl/kobiety/akcesoria/bizuteria/bransoletki/2027236636-srebrna-bransoletka-z-serduszkami",
             "https:/www.vinted.pl/kobiety/ubrania/topy-koszulki-i-t-shirty/inne/2027230515-bluzeczka-hm",
             "https:/www.vinted.pl/kobiety/akcesoria/bizuteria/bransoletki/2027222897-srebrna-bransoletka",
             "https:/www.vinted.pl/kobiety/akcesoria/bizuteria/broszki/2026886009-broszka",
             "https:/www.vinted.pl/dom/akcesoria-i-ozdoby/regaly/2026884223-slon-z-urocza-trabeczka",
             "https:/www.vinted.pl/kobiety/akcesoria/bizuteria/bransoletki/2026878931-bransoletka-z-regulacja-wielkosci",
             "https:/www.vinted.pl/kobiety/akcesoria/bizuteria/bransoletki/2026876670-bransoletka",
             "https:/www.vinted.pl/kobiety/akcesoria/bizuteria/bransoletki/2026872264-bransoletka-z-muszelek",
             "https:/www.vinted.pl/kobiety/akcesoria/bizuteria/bransoletki/2026870183-bransoletka",
             "https:/www.vinted.pl/kobiety/akcesoria/bizuteria/zestawy-bizuterii/2026857752-zestaw-bransoletek",
             "https:/www.vinted.pl/kobiety/ubrania/topy-koszulki-i-t-shirty/bluzki-bez-rekawow/1875072977-egzotyczna-bluzka",
             "https:/www.vinted.pl/kobiety/ubrania/sukienki/male-czarne/1875072945-czarna-przylegajaca-do-ciala-sukienka",
             "https:/www.vinted.pl/kobiety/ubrania/sukienki/sukienki-wizytowe/imprezowe-slash-koktajlowe/1875072918-imprezowa-sukienka-z-cekinami",
             "https:/www.vinted.pl/kobiety/ubrania/topy-koszulki-i-t-shirty/t-shirty/1875072890-czerwona-bluzeczka-dekolt-w-serek",
             "https:/www.vinted.pl/kobiety/ubrania/sukienki/sukienki-bez-ramiaczek/1875072860-krociutka-sukieneczka",
             "https:/www.vinted.pl/kobiety/ubrania/topy-koszulki-i-t-shirty/bluzki-z-3-slash-4-rekawami/1875072828-bluzeczka-z-rekawem-34",
             "https:/www.vinted.pl/kobiety/ubrania/topy-koszulki-i-t-shirty/t-shirty/1875072804-bluzeczka-w-rozmiarze-s",
             "https:/www.vinted.pl/kobiety/ubrania/spodnice/spodnice-krotkie/1875072785-czarna-minioweczka-rozmiar-s",
             "https:/www.vinted.pl/kobiety/ubrania/topy-koszulki-i-t-shirty/inne/1875072763-dwa-czarne-topy-letnia-okazja",
             "https:/www.vinted.pl/kobiety/ubrania/topy-koszulki-i-t-shirty/inne/1875072743-slodki-podkoszulek-dla-dziewczyny",
             "https:/www.vinted.pl/kobiety/ubrania/spodnie-i-legginsy/spodnie-typu-proste/1875072717-spodnie-w-kolorze-khaki-rozmiar-s"]


class ViewBooster:
    def __init__(self) -> None:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("start-maximized")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(executable_path="./chromedriver/chromedriver.exe", options=chrome_options)
        self.driver.implicitly_wait(10)

    def open_url(self, url: str) -> None:
        self.driver.get(url)
        assert "Vinted" in self.driver.title

    def wait_for_confirm_choices(self) -> None:
        try:
            self.driver.find_element(by=By.XPATH, value="//*[@id='onetrust-accept-btn-handler']")
        except NoSuchElementException:
            print("Page did not load properly, refreshing...")
            self.refresh_page()
            self.wait_for_confirm_choices()

    def get_current_view_count(self) -> int:
        return int(self.driver.find_element(
            by=By.XPATH,
            value="//div[@class='details-list__item']/div[contains(text(), 'Liczba')]/following-sibling::div").text)

    def close_window(self) -> None:
        self.driver.close()

    def refresh_page(self) -> None:
        self.driver.refresh()


if __name__ == "__main__":
    number_of_refreshes = 9
    list_of_links = [*my_links, *aga_links]
    estimated_time_seconds = len(list_of_links)*(5 + number_of_refreshes*3)
    print(f"Estimated time of process: {estimated_time_seconds//3600}h, "
          f"{estimated_time_seconds//60 - 60*(estimated_time_seconds//3600)}min, {estimated_time_seconds%60}s")
    view_booster = ViewBooster()
    start_time = time.time()
    for link_number, link in enumerate(list_of_links[::-1], 1):
        print(f"{link_number}/{len(list_of_links)}: {link[link.rfind('/') + link[link.rfind('/'):].find('-') + 1:]}")
        view_booster.open_url(link)
        view_booster.wait_for_confirm_choices()
        print(f"Current view count: {view_booster.get_current_view_count()}")
        for refresh_number in range(1, number_of_refreshes + 1):
            print(f"Refresh no. {refresh_number}/{number_of_refreshes}")
            view_booster.refresh_page()
            view_booster.wait_for_confirm_choices()
            print(f"Current view count: {view_booster.get_current_view_count()}")
    view_booster.close_window()
    stop_time = time.time()
    print(f"Time taken: {int(stop_time - start_time)}s")
    print("Everything was refreshed properly! :)")
        