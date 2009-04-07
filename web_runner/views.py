from django.http import HttpResponse, HttpRequest
from django.shortcuts import render_to_response

global button_text = 'Start'
def runner(request):
    """Runs the TestMaker middleware until stopped."""
    t_vals = {}
    button_text = 'Stop' if button_text == 'Start' else 'Start'
    t_vals['button_text'] = button_text
    t_vals['status'] = 'Running' if button_text == 'Stop' else 'Stopped'
    return render_to_response('runner.html',t_vals)