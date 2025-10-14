# https://leetcode.com/problems/clone-graph/description/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        node_mp = {}
        visited = set()
        edge_q = deque()

        node_mp[node.val] = Node(node.val)
        for neighbor in node.neighbors:
            edge_q.append((node, neighbor))
            visited.add((node.val, neighbor.val))
            
            if neighbor.val not in node_mp:
                node_mp[neighbor.val] = Node(neighbor.val)

        while edge_q:
            curr, neighbor = edge_q.popleft()
            
            node_mp[curr.val].neighbors.append(node_mp[neighbor.val])
            node_mp[neighbor.val].neighbors.append(node_mp[curr.val])

            for next_neighbor in neighbor.neighbors:
                if next_neighbor.val not in node_mp:
                    node_mp[next_neighbor.val] = Node(next_neighbor.val)
                
                if (neighbor.val, next_neighbor.val) not in visited and (next_neighbor.val, neighbor.val) not in visited:
                    edge_q.append((neighbor, next_neighbor))
                    visited.add((neighbor.val, next_neighbor.val))
        
        return node_mp[node.val]

            

