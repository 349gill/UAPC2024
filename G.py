""""
Ideas:

- Represent the city as a graph with districts as nodes and bridges as edges, Each edge has a weight representing the time to cross the bridge.

- The tornado follows a predicted course and will make the bridges it crosses unstable and unusable.
As the tornado reaches each district in sequence, it invalidates the corresponding bridge at a specific time.

- Use Dijkstra’s algorithm to find the shortest path from the starting district to the evacuation shelter.
Modify the algorithm to account for the bridges becoming unusable at specific times.

"""