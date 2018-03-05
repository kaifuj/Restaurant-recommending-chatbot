from rasa_core.actions import Action
from rasa_core.events import SlotSet
import pymysql

class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
        flavor = tracker.get_slot("flavor")
        location = tracker.get_slot("location")
        query = """SELECT name, rate, address, phone, price
                   FROM restaurants
                   WHERE flavor = '{0}'
                     AND (location LIKE '%{1}%' OR zipcode = '{1}')
                   ORDER BY rate DESC """.format(flavor, location)
        db = pymysql.connect("localhost","root","970128","sys",charset='utf8' )
        cursor = db.cursor()
        cursor.execute(query)
        results = list(cursor.fetchall())
        tracker.update(SlotSet("results", results))
        if len(tracker.get_slot("results")) == 0:
            dispatcher.utter_message("抱歉，未能找到符合要求的餐馆。")
            return
        else:
            dispatcher.utter_message("为您推荐以下满足要求的餐馆：\n")
            count = 0
            for i in range(len(tracker.get_slot("results"))):
                item = tracker.get_slot("results")[0]
                print("{0}  评分：{1}\n{2}\n{3}\n人均价格：{4}\n\n".format(item[0].strip(),item[1].strip(),item[2].strip(),item[3].strip(),item[4].strip()))
                del tracker.get_slot("results")[0]
                if len(tracker.get_slot("results")) == 0:
                    dispatcher.utter_message("以上是全部的推荐结果了~")
                count = count + 1
                if count == 3:
                    return

class ActionMoreResults(Action):
    def name(self):
        return 'action_more_results'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("为您推荐以下满足要求的餐馆：\n")
        count = 0
        for i in range(len(tracker.get_slot("results"))):
            item = tracker.get_slot("results")[0]
            print("{0}  评分：{1}\n{2}\n{3}\n人均价格：{4}\n\n".format(item[0].strip(),item[1].strip(),item[2].strip(),item[3].strip(),item[4].strip()))
            del tracker.get_slot("results")[0]
            if len(tracker.get_slot("results")) == 0:
                dispatcher.utter_message("以上是全部的推荐结果了~")
            count = count + 1
            if count == 3:
                return

