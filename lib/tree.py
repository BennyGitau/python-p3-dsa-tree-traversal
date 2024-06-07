class Tree:
  def __init__(self, root = None):
    self.root = root
#depth first traversal method
  def get_element_by_id(self, id): 
    nodes_to_visit=[self.root]
    while nodes_to_visit:
      node = nodes_to_visit.pop(0)
      if node['id'] == id:
        return node
      if node['children']:
        #add children nodes to the beginning of nodes to visit list
        nodes_to_visit = node['children'] + nodes_to_visit
    return None
#breadth first traversal method
  def get_element_by_id(self, id):
    nodes_to_visit=[self.root]
    while nodes_to_visit:
      node = nodes_to_visit.pop(0)
      if node['id'] == id:
        return node
      if node['children']:
        #add children nodes to end of nodes to visit list
        nodes_to_visit =nodes_to_visit + node['children']
    return None
    
