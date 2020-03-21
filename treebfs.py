tree = {'5':['4', '6'],
 '4':['2', '3'], '6':['7', '8'],
  '2': [], '3':[], '7':[], '8':[]}

''' tree illistration
         5
      /     \
    4        6
  /   \    /   \
3     2 7     8
''' 
visited = []
que = []

def bfs(visited, tree, topNode):
	visited.append(topNode)
	que.append(topNode)
	while que:
		s = que.pop(0)
		print(s + ' - ')
		for child in tree[s]:			
			if child not in visited:
				visited.append(child)
				que.append(child)
				
bfs(visited, tree, '5')