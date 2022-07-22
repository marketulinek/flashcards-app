from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Card


class CardListView(ListView):
    model = Card
    queryset = Card.objects.all().order_by('box', '-created_at')

class CardCreateView(CreateView):
    model = Card
    fields = ['question', 'answer', 'box']
    success_url = reverse_lazy('card_create')

class CardUpdateView(CardCreateView, UpdateView):
    success_url = reverse_lazy('card_list')