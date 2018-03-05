## get info and search
* greet
    - utter_greet
* search
    - utter_ask_flavor
* provide_flavor{"flavor": "川菜"}
    - slot{"flavor": "川菜"}
    - utter_ask_location
* provide_location{"location": "Irvine"}
    - slot{"location": "Irvine"}
    - action_search_restaurants
> search_finished

## get info and search
* greet
    - utter_greet
* search{"flavor": "川菜"}
    - slot{"flavor": "川菜"}
    - utter_ask_location
* provide_location{"location": "Irvine"}
    - slot{"location": "Irvine"}
    - action_search_restaurants
> search_finished

## get info and search
* greet
    - utter_greet
* search{"location": "Irvine"}
    - slot{"location": "Irvine"}
    - utter_ask_flavor
* provide_flavor{"flavor": "川菜"}
    - slot{"flavor": "川菜"}
    - action_search_restaurants
> search_finished

## get info and search
* greet
    - utter_greet
* search{"flavor": "川菜", "location": "Irvine"}
    - slot{"location": "Irvine"}
    - slot{"flavor": "川菜"}
    - action_search_restaurants
> search_finished

## return results
> search_finished
    - slot{"results": []}
    - utter_bye
    - action_restart

## return results
> search_finished
    - slot{"results": [["香港云吞面世家", "3.70", "934 N Hill St, Los Angeles, CA 90012", "(213) 626-6050", "10"]]}
    - utter_goodornot
* deny
    - action_more_results
    - slot{"results": []}
    - utter_bye
    - action_restart

## return results
> search_finished
    - slot{"results": [["香港云吞面世家", "3.70", "934 N Hill St, Los Angeles, CA 90012", "(213) 626-6050", "10"]]}
    - utter_goodornot
* deny
    - action_more_results
    - slot{"results": [["香港云吞面世家", "3.70", "934 N Hill St, Los Angeles, CA 90012", "(213) 626-6050", "10"]]}
    - utter_goodornot
* deny
    - action_more_results
    - slot{"results": []}
    - utter_bye
    - action_restart

## return results
> search_finished
    - slot{"results": [["香港云吞面世家", "3.70", "934 N Hill St, Los Angeles, CA 90012", "(213) 626-6050", "10"]]}
    - utter_goodornot
* deny
    - action_more_results
    - slot{"results": [["香港云吞面世家", "3.70", "934 N Hill St, Los Angeles, CA 90012", "(213) 626-6050", "10"]]}
    - utter_goodornot
* deny
    - action_more_results
    - slot{"results": [["香港云吞面世家", "3.70", "934 N Hill St, Los Angeles, CA 90012", "(213) 626-6050", "10"]]}
    - utter_goodornot
* deny
    - action_more_results
    - slot{"results": []}
    - utter_bye
    - action_restart

## return results
> search_finished
    - slot{"results": [["香港云吞面世家", "3.70", "934 N Hill St, Los Angeles, CA 90012", "(213) 626-6050", "10"]]}
    - utter_goodornot
* deny
    - action_more_results
    - slot{"results": [["香港云吞面世家", "3.70", "934 N Hill St, Los Angeles, CA 90012", "(213) 626-6050", "10"]]}
    - utter_goodornot
* deny
    - action_more_results
    - slot{"results": [["香港云吞面世家", "3.70", "934 N Hill St, Los Angeles, CA 90012", "(213) 626-6050", "10"]]}
    - utter_goodornot
* deny
    - action_more_results
    - slot{"results": [["香港云吞面世家", "3.70", "934 N Hill St, Los Angeles, CA 90012", "(213) 626-6050", "10"]]}
    - utter_goodornot
* deny
    - action_more_results
    - slot{"results": []}
    - utter_bye
    - action_restart

## return results
> search_finished
    - slot{"results": [["香港云吞面世家", "3.70", "934 N Hill St, Los Angeles, CA 90012", "(213) 626-6050", "10"]]}
    - utter_goodornot
* affirm
    - utter_bye
    - action_restart

## return results
> search_finished
    - slot{"results": [["香港云吞面世家", "3.70", "934 N Hill St, Los Angeles, CA 90012", "(213) 626-6050", "10"]]}
    - utter_goodornot
* deny
    - action_more_results
    - slot{"results": [["香港云吞面世家", "3.70", "934 N Hill St, Los Angeles, CA 90012", "(213) 626-6050", "10"]]}
    - utter_goodornot
* affirm
    - utter_bye
    - action_restart

## return results
> search_finished
    - slot{"results": [["香港云吞面世家", "3.70", "934 N Hill St, Los Angeles, CA 90012", "(213) 626-6050", "10"]]}
    - utter_goodornot
* deny
    - action_more_results
    - slot{"results": [["香港云吞面世家", "3.70", "934 N Hill St, Los Angeles, CA 90012", "(213) 626-6050", "10"]]}
    - utter_goodornot
* deny
    - action_more_results
    - slot{"results": [["香港云吞面世家", "3.70", "934 N Hill St, Los Angeles, CA 90012", "(213) 626-6050", "10"]]}
    - utter_goodornot
* affirm
    - utter_bye
    - action_restart

## return results
> search_finished
    - slot{"results": [["香港云吞面世家", "3.70", "934 N Hill St, Los Angeles, CA 90012", "(213) 626-6050", "10"]]}
    - utter_goodornot
* deny
    - action_more_results
    - slot{"results": [["香港云吞面世家", "3.70", "934 N Hill St, Los Angeles, CA 90012", "(213) 626-6050", "10"]]}
    - utter_goodornot
* deny
    - action_more_results
    - slot{"results": [["香港云吞面世家", "3.70", "934 N Hill St, Los Angeles, CA 90012", "(213) 626-6050", "10"]]}
    - utter_goodornot
* deny
    - action_more_results
    - slot{"results": [["香港云吞面世家", "3.70", "934 N Hill St, Los Angeles, CA 90012", "(213) 626-6050", "10"]]}
    - utter_goodornot
* affirm
    - utter_bye
    - action_restart

