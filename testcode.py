__author__ = 'Vixus'
from riotwatcher import RiotWatcher

w = RiotWatcher('eda1ed56-6ae8-41bf-97b7-acaa970537dc')

# check if we have API calls remaining
print(w.can_make_request())

me = w.get_summoner(name='vixus360')
print(me)

# championList = w.static_get_champion_list()
# print championList
# print w.get_champion(championList['data']['Lux']['id'])

def print_tabs(count):
    for i in range(count):
        print '\t',

def print_data(obj,tabCount=-1):
    if type(obj) == dict:
        for key, value in obj.items():
            print_tabs(tabCount)

            if hasattr(value, '__iter__'):
                print key,":"
                print_data(value,tabCount+1)
            else:
                print '%s : %s' % (key, value)
    elif type(obj) == list:
        for value in obj:
            if hasattr(value, '__iter__'):
                print_data(value,tabCount+1)
            else:
                print_tabs(tabCount)
                print value
    else:
        print obj


print_data(me)
match_history = w.get_match_history(me['id'])
print match_history[0]

# # takes list of summoner ids as argument, supports up to 40 at a time
# # (limit enforced on riot's side, no warning from code)
# my_mastery_pages = w.get_mastery_pages(str(me['id']))
# # returns a dictionary, mapping from summoner_id to mastery pages
# # unfortunately, this dictionary can only have strings as keys,
# # so must convert id from a long to a string
# print(my_mastery_pages)
#
# my_ranked_stats = w.get_ranked_stats(me['id'])
# print(my_ranked_stats)
#
# my_ranked_stats_last_season = w.get_ranked_stats(me['id'], season=5)
# print(my_ranked_stats_last_season)
#
# # all static methods are prefaced with 'static'
# # static requests do not count against your request limit
# # but at the same time, they don't change often....
# static_champ_list = w.static_get_champion_list()
# print(static_champ_list)
#
# # import new region code
# from riotwatcher import EUROPE_WEST
#
# # request data from EUW
# froggen = w.get_summoner(name='froggen', region=EUROPE_WEST)
# print(froggen)
#
# # create watcher with EUW as its default region
# euw = RiotWatcher('<your-api-key>', default_region=EUROPE_WEST)
#
# # proper way to send names with spaces is to remove them, still works with spaces though
# xpeke = w.get_summoner(name='fnaticxmid')
# print(xpeke)