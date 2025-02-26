from django.shortcuts import render


def page_not_found(request, exception):
	return render(request, 'error-pages/404.html', status=404)


def server_error(request):
	return render(request, 'error-pages/500.html', status=500)


def bad_request(request, exception):
	return render(request, 'error-pages/400.html', status=400)


def permission_denied(request, exception):
	return render(request, 'error-pages/403.html', status=403)
