# Written By Ismael Heredia in the year 2021

from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.views.generic.edit import View
from django.contrib import messages
import json
from django.views.decorators.csrf import csrf_exempt
import html5print

def index(request):
    return render(request, 'home/index.html')

@csrf_exempt
def format(request):

	code = request.POST.get("code", "")
	code_type = request.POST.get("code_type", "")
	indent_width = int(request.POST.get("indent_width", ""))

	pretty_code = ""

	status = 0
	message = ""

	try:
		if code_type == "html":
			pretty_code = html5print.HTMLBeautifier.beautify(code, indent_width)
		elif code_type == "css":
			pretty_code = html5print.CSSBeautifier.beautify(code, indent_width)
		elif code_type == "js":
			pretty_code = html5print.JSBeautifier.beautify(code, indent_width)
		elif code_type == "json":
			parsed_json = json.loads(code)
			pretty_code = json.dumps(parsed_json, indent=indent_width, sort_keys=True)
		status = 1
		message = "Code formatted"
	except:
		message = "Error formatting code"
		pass

	json_code = {}

	json_code["status"] = status
	json_code["message"] = message
	json_code["pretty_code"] = pretty_code

	result = json.dumps(json_code)

	return HttpResponse(result, content_type='application/json')
