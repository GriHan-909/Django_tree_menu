def build_tree(items):
    item_dict = {item.id: {'item': item, 'children': []} for item in items}
    root = []

    for item in items:
        if item.parent_id:
            item_dict[item.parent_id]['children'].append(item_dict[item.id])
        else:
            root.append(item_dict[item.id])

    return root

def get_active_branch(tree, current_url):
    def find_path(node, path):
        item = node['item']
        if item.get_absolute_url().rstrip('/') == current_url.rstrip('/'):
            return path + [item.id]
        for child in node['children']:
            result = find_path(child, path + [item.id])
            if result:
                return result
        return None

    for node in tree:
        result = find_path(node, [])
        if result:
            return set(result)
    return set()

