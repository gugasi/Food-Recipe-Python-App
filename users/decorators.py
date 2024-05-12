from django.http import HttpResponse

def add_extra_context(view_func):
    def wrapper(request, *args, **kwargs):
        extra_context = {
            'extra_variable': 'This is an extra variable',
        }
        response = view_func(request, *args, **kwargs)
        
        if isinstance(response, HttpResponse) and hasattr(response, 'context_data'):
            if 'extra_context' in response.context_data:
                response.context_data['extra_context'].update(extra_context)
            else:
                response.context_data['extra_context'] = extra_context
        
        return response
    
    return wrapper
