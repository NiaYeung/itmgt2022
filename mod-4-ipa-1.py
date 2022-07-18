#!/usr/bin/env python
# coding: utf-8

# In[21]:


import numpy as np

def tic_tac_toe(board):
    for b in (board, np.transpose(board)):
        for row in b:
            if len(set(row)) == 1:
                return row[0]
    downwards_diagonal = [board[i][i] for i in range(len(board))]
    upwards_diagonal = [board[i][len(board) - 1 - i] for i in range(len(board))]
    if len(set(downwards_diagonal)) == 1:
        return board[0][0]
    if len(set(upwards_diagonal)) == 1:
        return board[0][len(board)-1]
    return "NO WINNER"


board1 = [
['X','X','O'],
['O','X','O'],
['O','','X'],
]

board2 = [
['X','X','O'],
['O','X','O'],
['','O','X'],
]

board3 = [
['O','X','O'],
['','O','X'],
['X','X','O'],
]

board4 = [
['X','X','X'],
['O','X','O'],
['O','','O'],
]

board5 = [
['X','X','O'],
['O','X','O'],
['X','','O'],
]

board6 = [
['X','X','O'],
['O','X','O'],
['X','',''],
]

board7 = [
['X','X','O',''],
['O','X','O','O'],
['X','','','O'],
['O','X','','']
]

board8 = [
['O','O','X','','','O'],
['X','O','X','','X','O'],
['O','','','O','X','O'],
['X','X','O','','','O']
]


# In[22]:


tic_tac_toe(board8)


# In[17]:


tic_tac_toe(board1)


# In[19]:


tic_tac_toe(board7)


# In[23]:


tic_tac_toe([['X','X','O','O'], ['O','X','O','O'],
['X','','','O'],
['O','X','','O']])


# In[38]:


social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
}
    

def relationship_status(to_member, from_member, social_graph):

    to = social_graph[to_member]
    other = social_graph[from_member]
    toMember = to['following']
    fromMember = other['following']
    if to_member in fromMember and from_member not in toMember:
        return "followed by"
    if to_member in fromMember and from_member in toMember:
        return "friends"
    if from_member in toMember and to_member not in fromMember:
        return "follower"
    if from_member not in toMember and to_member not in fromMember and to_member != from_member:
        return "no relationship"
    return "error, please imput again"


# In[34]:


relationship_status("@jobenilagan", "@joeilagan", social_graph)


# In[39]:


relationship_status("@jobenilagan", "@jobenilagan", social_graph)


# In[2]:


legs = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}

legs1 = {
    ('a1', 'a2'): {
        'travel_time_mins': 10
    },
    ('a2', 'b1'): {
        'travel_time_mins': 10230
    },
    ('b1', 'a1'): {
        'travel_time_mins': 1
    }
}

def eta(first_stop, second_stop, route_map):
    stops = list(route_map.keys())
    eta = 0
    if first_stop == second_stop:
        for x in (stops):
            ride = route_map[x]
            eta += ride['travel_time_mins']
        return eta
    else:
        nextStop = first_stop
        while nextStop != second_stop:
            for x in (stops):
                if nextStop == x[0]:
                    ride = route_map[x]
                    eta += ride['travel_time_mins']
                    nextStop = x[1]
                    break
        return eta 


# In[3]:


eta("a1", "a1", legs1)


# In[ ]:




