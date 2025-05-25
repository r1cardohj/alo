"""广度优先算法"""
from collections import deque

graph = {}
graph["you"] = "alice", "bob", "claire"
graph["bob"] = "anuj", "peggy"
graph["alice"] = "peggy",
graph["claire"] = "thom", "jonny"
graph["anuj"] = tuple()
graph["peggy"] = "you",
graph["thom"] = tuple()
graph["jonny"] = tuple()


def person_is_seller(name):
    return name[-1] == "m"


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = set()
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            print(person)
            if person_is_seller(person):
                print(person + " is a mango seller")
                return True
            else:
                search_queue += graph[person]
                searched.add(person)
    return False


search("you")
