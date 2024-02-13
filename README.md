# vinted-view-booster

# About The Project
Simple bot for boosting views number for offers on Vinted page for provided users.

# IMPORTANT
Vinted updated their website, so that when no user is logged in, the views don't count... Therefor it is necessary to logg in as a different user in order to be able to boost views on a desired account.

Thus, after a new chrome driver is downloaded (you can see that in logs) change each `cdc_` appearance in chromedriver to for example `dog_` (it is important to replace the string with the same number of letters!)

Check this answer: https://stackoverflow.com/questions/66989755/getting-403-when-using-selenium-to-automate-checkout-process/67112665#67112665


# Built With
Python 3.9.10

# Getting started

### Working with vinted-view-booster:
1. Go to the `if __name__ == __main__:` check.
2. Change `number_of_refreshes` variable to desired number of refreshes, that you want to add to your offer.
3. Change `list_of_vinted_members_to_refresh` to include members, that you want offers to be boosted.
4. Run the script.
5. Statistics about each member and each offer should be printed in the terminal.
6. After successful run, offers should gain number of views.

# Usage
Boosting views of your offers to be more visible for interested people.

# Licence
Distributed under the MIT License. See LICENSE file for more information.
