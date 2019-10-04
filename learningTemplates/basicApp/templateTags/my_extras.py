#first register everything

from django import template
#create an object called register
register = template.Library()
#write a function to be a  custom template filter
@register.filter(name='cut')
def cut(value,arg):
    """
    this cust out all values of "arg" from the string!
    """
    return value.replace(arg,'')
#now register This
#register.filter('cut',cut)
