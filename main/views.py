from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, ListView
from main.models import Categoriya, Book


class Index(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        kwargs['categoriya'] = Categoriya.objects.all()

        return super().get_context_data(**kwargs)



class Book_del(View):

    template_name= 'main/shop.html'

    def get(self, request, id):
        book = Book.objects.filter(categoriya_id=id)

        # print(book.name())
        for i in book.values_list('price'):
            y = list((i))
            for j in y:
                # print(j-30)
                u = j/100*30
            print(u)

            # u = y/100*30
            # print(u)
            # u = str(y)
            # t = int((u))
            # print(type(t))


        return render(request, 'main/shop.html', {"book": book, 'u': u})





