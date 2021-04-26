# Romania-graph-greedy-algorithm

**I was asked to implement a graph that represents Romania with its 20 states** {Arad, Bucharest, Craiova, Dobreta, Eforie, Fagaras, Giurgiu, Hirsova, Iasi, Lugoj, Mehadia, Neamt, Oradea, Pitesti, Rimnicu Vilcea, Sibiu, Timisoara, Urziceni, Vaslui, Zerind}.

I created a dictionary ('**dist**') with the distances from each city to Bucharest.

**I was also asked to implement the greedy algorithm**. The idea of this algorithm is to try to solve the problem by making the locally optimal choice at each stage with the hope of finding a global optimum. For that we use the heuristic function [h(n)] that estimates the straight distance from each city to Bucharest (i.e., not using the real distance; those are the distances used in the dictionary I mentioned above.

My algorithm is made up of 2 functions plus the main function. It also has a global variable 'cidade_anterior' that represents the previously visited city - for that, the first '**cidade_origem**' is the one where we start our journey to Bucharest. The functions created are:

## melhor_caminho
It has 2 parameters, the first is the '**cidade_origem**' (city of origin - city where we start the journey to reach Bucharest) and '**cidade_destino**' (the destination city, in this case, Bucharest).

The main idea of this function is to compare the current city with the destination city (Bucharest). If the comparison is true, it prints that you arrived at your destination. If it is not, we use the current city as parameter of the second function that tells us the best city to visit next.

This is a recursive that keeps calling the second function until the stop condition (current city = destination city) is true.

## obter_melhor_vizinhanca
It has only 1 parameter, the _current city_. This function analyze the effort to go to each of its neigbors (cities). The city that takes the less effort is the one chosen by the greedy algorithm.

For the comparison, I used the well-known artifice of creating a variable ('**menor_distancia**') with a very large value ('menor_distancia' = 99999) so I make sure that none of the cities are further away from Bucharest than the value of this variable. When the distance is shorter than _menor_distancia_, I update its value to the value of the distance from the current neighbor city to Bucharest. If it is not, nothing changes, we continue to the next neighbor city.

I algo use thw variable '**melhor_vizinhanca**' to keep the name of the better city to go from the city we are. Once the algorithm analyze all the neighboring cities, it chooses the one that take less effort to go and return it to be used in the function **melhor_caminho**.
