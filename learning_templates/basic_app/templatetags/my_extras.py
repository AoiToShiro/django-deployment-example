from django import template

register = template.Library()

def cut(value,arg):
    """
    This cuts out all values of "agr" from the string
    """
    return value.replace(arg,'')

# first "cut" is what you want to name it, the second is the name of the function
register.filter('cut',cut)
