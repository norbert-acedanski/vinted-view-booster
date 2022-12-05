import time

from view_booster import ViewBooster

if __name__ == "__main__":
    number_of_refreshes = 9
    list_of_vinted_members_to_refresh = ["norbert97a", "stokrotka0299", "kamanna"]
    duration_dict = {}
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
            all_items_url = view_booster.get_all_items_url()
            print(f"\nCurrent member: {member}")
            print(f"Number of items found: {number_of_items}")
            print(f"Number of views increased for each item: {number_of_refreshes + 1}")
            print(f"Number of all views increased for all items: {(number_of_refreshes + 1)*number_of_items}\n")
            for item_number, item_url in enumerate(all_items_url, 1):
                print(f"\n{item_number}/{len(all_items_url)}: "
                      f"{item_url[item_url.rfind('/') + item_url[item_url.rfind('/'):].find('-') + 1:]}")
                view_booster.open_url(item_url)
                print(f"Current view count: {view_booster.get_current_view_count()}")
                for refresh_number in range(1, number_of_refreshes + 1):
                    print(f"Refresh no. {refresh_number}/{number_of_refreshes}")
                    view_booster.refresh_page()
                    print(f"Current view count: {view_booster.get_current_view_count()}")
            stop_time = time.time()
            user_duration = int(stop_time - start_time)
            duration_dict[member] = user_duration
            print(f"\nDuration for user {member}: {user_duration//60}min {user_duration%60}s")
    total_stop_time = time.time()
    if len(list_of_vinted_members_to_refresh) > 1:
        print("\n\nSummary:")
        print(f"\nDuration for all users: {int(total_stop_time - total_start_time)//60}min "
              f"{int(total_stop_time - total_start_time)%60}s\n")
        for member, duration in duration_dict.items():
            print(f"Duration for {member}: {duration//60}min {duration%60}s")
    print("Everything was refreshed properly for all users! :)")
