from django import template

register = template.Library()


@register.filter
def get_range(value, args):
  """
    Filter - returns a list containing range made from given value
    Usage (in template):

    <ul>{% for i in value|get_range:args %}
      <li>{{ i }}. Do something</li>
    {% endfor %}</ul>

    Results with the HTML:
    <ul>
      <li>0. Do something</li>
      <li>1. Do something</li>
      <li>2. Do something</li>
    </ul>

    Instead of 3 one may use the variable set in the views
  """
  return range(value, args)
