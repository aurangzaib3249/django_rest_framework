
from django.http import JsonResponse
from rest_framework.decorators import *
from http import HTTPStatus

class FieldCheckView(APIView):
	"""
	custom dispatch to check post data params
	"""
	required_params=[]
	def dispatch(self, request, *args, **kwargs):
		self.args = args
		self.kwargs = kwargs
		request = self.initialize_request(request, *args, **kwargs)
		self.request = request
		self.headers = self.default_response_headers 
		try:
			self.initial(request, *args, **kwargs)
			if request.method.lower() in self.http_method_names:
				handler = getattr(self, request.method.lower(),
								  self.http_method_not_allowed)
			else:
				handler = self.http_method_not_allowed
			if request.method.lower()=="post" and not request_validator(request,self.required_params):
				
				response= JsonResponse(
                {
                    "Message":'parameters mising {}'.format(request_get_missing(request,self.required_params)),
                    "Required Parameters":self.required_params,
                    "Wrong Parameters":request_wrong_parameters(request,self.required_params),
                    "status":400
                }
				)
			else:
				response = handler(request, *args, **kwargs)
		except Exception as exc:
			response = self.handle_exception(exc)

		self.response = self.finalize_response(request, response, *args, **kwargs)
		return self.response
def request_validator(request,check_list):
    try:
        data=request.data
        for field in check_list:
            if field not in data:
                return False
    except Exception as e:
        return False
    return True
def request_get_missing(request,check_list):
    try:
        data=request.data
        list=[]
        for field in check_list:
            if field not in data:
                list.append(field)
        return list  
    except Exception as e:
        return []

def request_wrong_parameters(request,check_list):
    try:
        data=request.data
        list=[]
        for field in data:
            if field not in check_list:
                list.append(field)
        return list  
    except Exception as e:
        return []