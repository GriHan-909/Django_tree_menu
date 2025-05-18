from django import template
from ..models import Menu, MenuItem
from ..utils import build_tree, get_active_branch

register = template.Library()

@register.inclusion_tag('tree_menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_url = request.path

    try:
        menu = Menu.objects.get(name=menu_name)
        items = MenuItem.objects.filter(menu=menu).select_related('parent')
    except Menu.DoesNotExist:
        return {'menu_tree': []}

    tree = build_tree(items)
    active_branch = get_active_branch(tree, current_url)
    return {'menu_tree': tree, 'active_branch': active_branch, 'request': request}
