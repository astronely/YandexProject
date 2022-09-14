from docs.models import Item
import datetime

def get_graph(graph, files):
	for item in files:
		parent = item.parentId
		try:
			temp = graph[item.id]
		except KeyError:
			graph[item.id] = []

		try:
			parents = ((graph[parent]).copy())
			parents.append(str(item.id))
			graph[parent] = parents
		except KeyError:
			if parent != "None":
				graph[parent] = [item.id]
		except AttributeError:
			pass

def fileToDictionary(file):
	output = dict()
	output["id"] = file.id
	if file.url == '':
		output["url"] = None
	else:
		output["url"] = file.url
	output["date"] = file.date
	if file.parentId == '':
		output["parentId"] = None
	else:
		output["parentId"] = file.parentId
	output["type"] = file.type
	output["size"] = file.size
	output["children"] = None
	return output

def dfsGet(graph, node, visited):
	if node not in visited:
		item = Item.objects.get(pk=node)
		last_date = datetime.datetime.strptime(str(item.date), "%Y-%m-%dT%H:%M:%SZ")
		children = []
		visited.append(node)
		for k in graph[node]:
			child = dfsGet(graph, k, visited)
			children.append(child)
			child_date = datetime.datetime.strptime(str(child["date"]), "%Y-%m-%dT%H:%M:%SZ")
			if child_date > last_date:
				last_date = child_date
		item = fileToDictionary(Item.objects.get(pk=node))
		if len(children) > 0:
			item["children"] = children
			item["size"] = 0
			for j in range(len(children)):
				item["size"] += int(children[j]["size"])
		item["date"] = last_date.isoformat() + 'Z'
		return item

def dfsDelete(graph, node, visited):
	if node not in visited:
		visited.append(node)
		for k in graph[node]:
			dfsDelete(graph, k, visited)
	return visited
