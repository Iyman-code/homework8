from django.shortcuts import render
from django.http import HttpResponse

def manual_form_view(request):
    if request.method == 'POST':
        # Ручное извлечение данных из POST-запроса (без классов forms.Form)
        username = request.POST.get('username')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Валидация данных
        if not username or not email:
            return render(request, 'myapp/form.html', {
                'error': 'Пожалуйста, заполните обязательные поля (Имя и Email).',
                'username': username,
                'email': email,
                'message': message,
            })

        return HttpResponse(
            f"<h3>Форма успешно обработана вручную!</h3>"
            f"<p><b>Имя:</b> {username}</p>"
            f"<p><b>Email:</b> {email}</p>"
            f"<p><b>Сообщение:</b> {message}</p>"
            f'<br><a href="/">Назад к форме</a>'
        )

    return render(request, 'myapp/form.html')
