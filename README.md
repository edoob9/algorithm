# algorithm
## Search

Problem Solving As Search?
1. Problem Representation
     convert format for using search algorithm(graph, tree) => How?
3. Search Algorithm

### Uninformed Search
|Algorithm|basic Code|설명|
|------|---|---|
|BFS|---|---|
|DFS|---|---|
|Uniform Cost Search|---|---|

### Informed Search

|Algorithm|basic Code|설명|
|------|---|---|
|Greedy|[python](https://github.com/edoob9/algorithm/blob/main/search/Greedy_search.py)|최대 무게/질량을 도달하기 위한 방법을 찾는 알고리즘, 선택의 순간마다 뒤를 생각하지않고, 최적의 상황만을 생각하여 최종 해답에 도달하는 방식|
|A*star|[python code](https://github.com/edoob9/algorithm/blob/main/search/Astar.py)|게임에서 플레이어를 목표지점으로 이동시킬 때 사용하는 알고리즘, 가중치 그래프|

### search
|Algorithm|basic Code|설명|
|------|---|---|
|Brute-Force|[python code](https://github.com/edoob9/algorithm/blob/main/search/Brute-Force.py)|How to find an answer while listing the number of possible cases|
|Bitmask|---|---|

# Index
fringe is a queue sorted in decreasing order of desirability(Expand하기를 원하는 Node의 집합)
