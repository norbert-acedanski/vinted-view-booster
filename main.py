import logging
import pyautogui
import pyperclip
import time

from view_booster import ViewBooster

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)

if __name__ == "__main__":
    number_of_refreshes = 3
    list_of_vinted_members_to_refresh = ["stokrotka0299"]#, "predator97a"]
    duration_dict = {}
    all_items_url = {}
    total_start_time = time.time()
    with ViewBooster() as view_booster:
        for member_number, member in enumerate(list_of_vinted_members_to_refresh):
            start_time = time.time()
            view_booster.open_url("https://www.vinted.pl/")
            view_booster.decline_all_cookies() if member_number == 0 else None
            view_booster.choose_option_in_search_item("user")
            view_booster.search_phrase_in_search_bar(member)
            view_booster.choose_searched_phrase(member)
            number_of_items = view_booster.get_number_of_items_of_a_user()
            while len(view_booster.all_visible_user_items()) != number_of_items:
                view_booster.scroll_max_down()
            all_items_url[member] = view_booster.get_all_items_url()
    logging.info("Number of items found for each user:")
    for user, items in all_items_url.items():
        logging.info(f"{user=}, number of items: {len(items)}")
    logging.info(f"Number of views increased for each item: {number_of_refreshes + 1}\n")
    logging.info("Please open a separate Browser window, open Vinted page and Log in to it. After that, click Enter...")
    input()
    logging.info("Leave your mouse in the area of the Browser window (Do not click mouse there) and click Enter...")
    input()
    pyautogui.click()
    for user, items in all_items_url.items():
        logging.info(f"Starting boosts for {user=}")
        for item_number, item_url in enumerate(items, 1):
            logging.info(f"{item_number}/{len(items)}: {item_url}")
            pyautogui.hotkey("ctrl", "t")
            pyperclip.copy(item_url)
            pyautogui.hotkey("ctrl", "v")
            pyautogui.press("enter")
            time.sleep(5)
            for refresh_number in range(1, number_of_refreshes + 1):
                logging.info(f"Boost no. {refresh_number}/{number_of_refreshes}")
                pyautogui.press("f5")
                time.sleep(2)
            pyautogui.hotkey("ctrl", "w")
        logging.info(f"Finished boosting for {user=}")
        stop_time = time.time()
        user_duration = int(stop_time - start_time)
        duration_dict[member] = user_duration
        logging.info(f"\nDuration for user {member}: {user_duration//60}min {user_duration%60}s")
    total_stop_time = time.time()
    if len(list_of_vinted_members_to_refresh) > 1:
        logging.info("Summary:")
        logging.info(f"Duration for all users: {int(total_stop_time - total_start_time)//60}min "
                     f"{int(total_stop_time - total_start_time)%60}s\n")
        for member, duration in duration_dict.items():
            logging.info(f"Duration for {member}: {duration//60}min {duration%60}s")
    logging.info("\nEverything was refreshed properly for all users! :)")
