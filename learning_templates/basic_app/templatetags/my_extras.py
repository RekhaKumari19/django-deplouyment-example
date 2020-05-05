from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all values of "arg" from the string!
    value is variable or value from context dictionary you will pass
    arg is any additional argument.
    """
    return value.replace(arg,'')

# Now we need to register this cut function
#register.filter('cut', cut)
# Here fisrt argument is string that you call the function through template tag
# second argument is just the name of function itself.
