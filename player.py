'''
Create a class Player with the following attributes:

- playerId - int
- playerName - String
- runs - int
- playerType - String
- matchType - String

Write a parameterized constructor to initialize these attributes.

Create a class Solution with the main method.

Implement the following two static methods in the Solution class:

1. findPlayerWithLowestRuns

This method takes an array of Player objects and a String representing the player type as input parameters.

- Find and return the lowest runs scored by a player whose playerType matches the given String.
- The comparison must be case-insensitive.
- If no player matches the given player type, return 0.

2. findPlayerByMatchType

This method takes an array of Player objects and a String representing the match type as input parameters.

- Return an array of Player objects whose matchType matches the given String.
- The comparison must be case-insensitive.
- Sort the matching Player objects in descending order of playerId.
- If no player matches the given match type, return null.

Main Method Requirements:

- Use a Scanner object to read the details of four Player objects in the following attribute order:
  1. playerId
  2. playerName
  3. runs
  4. playerType
  5. matchType
- Read two additional String values: the player type and match type to search for.
- Call both static methods from the main method.

For findPlayerWithLowestRuns:
- If the returned value is greater than 0, print the runs.
- Otherwise, print "No such player".

For findPlayerByMatchType:
- If the returned array is not null, print the playerId of each Player object.
- Otherwise, print "No Player with given matchType".

Note:
- No two Players will have the same playerId or runs.
- All searches must be case-insensitive.

TEST CASE 1

Input:
11
Sachin
100
International
One day
12
Shewag
133
International
Test
13
Varun
78
State
Test
14
Ashwin
67
State
One day
State
One day

Output:
67
14
11

Explanation:
The lowest runs among players of type State is 67. Players with matchType One day have IDs 11 and 14. In descending order of playerId, the output is 14 followed by 11.

TEST CASE 2

Input:
11
Sachin
100
International
One day
12
Shewag
133
International
Test
13
Varun
78
State
Test
14
Ashwin
67
State
One day
District
T20

Output:
No such player
No Player with given matchType

Explanation:
No player has playerType District, and no player has matchType T20.

TEST CASE 3 (Case-insensitive search)

Input:
11
Sachin
100
International
One day
12
Shewag
133
International
Test
13
Varun
78
State
Test
14
Ashwin
67
State
One day
sTaTe
oNe DaY

Output:
67
14
11

Explanation:
The search is case-insensitive, so sTaTe matches State and oNe DaY matches One day.
'''
class Player:
    def __init__(self,pid,pname,runs,ptype,mtype):
        self.pid=pid
        self.pname=pname
        self.runs=runs
        self.ptype=ptype
        self.mtype=mtype
class solution:
    @staticmethod
    def findplayerwithlruns(arr_player,trgt_ptype):
        runs=[]
        for i in arr_player:
            if i.ptype.lower()==trgt_ptype.lower():
                runs.append(i.runs)
        if runs==[]:
            print("No such player")
        else:
            print(min(runs))
    def findplayerbymatchtype(arr_player,trgt_mtype):
        player_id=[]
        for i in arr_player:
            if i.mtype.lower()==trgt_mtype.lower():
                player_id.append(i.pid)
        if player_id==[]:
            print("No Player with given matchType")
        else:

            player_id.sort(reverse=True)  
            for i in player_id:
                print(i)

n=int(input())
lst_player=[]
for i in range(n):
    pid=int(input())
    pname=input()
    runs=int(input())
    ptype=input()
    mtype=input()
    lst_player.append(Player(pid,pname,runs,ptype,mtype))

trgt_ptype=input()
trgt_mtype=input()
solution.findplayerwithlruns(lst_player,trgt_ptype)
solution.findplayerbymatchtype(lst_player,trgt_mtype)

