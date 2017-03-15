from django import template

register = template.Library()

@register.inclusion_tag("about/abouts.html", takes_context=True)
def show_about(context):
    return{
        "name": context["name"],
        "pic": context["pic"],
        "description": context["description"],
    }
