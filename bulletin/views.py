from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, \
    DetailView, ListView, UpdateView

from .fiters import AnsFilter
from .forms import AnsForms, StickerForms
from .models import Ans, Sticker


class StickerList(ListView):
    """Класс обработки списка объявлений всех User."""

    model = Sticker
    ordering = '-datetime_of_creation'
    template_name = 'bulletin/stickers.html'
    context_object_name = 'stickers'
    paginate_by = 10


class StickerDetail(LoginRequiredMixin, DetailView):
    """Класс обрабатывает конкретное объявление Sticker."""

    model = Sticker
    template_name = 'bulletin/sticker.html'
    context_object_name = 'sticker'

    def get_context_data(self, **kwargs):
        """Метод передает в контекст результат проверки наличия откликов \
        на объявление."""
        context = super().get_context_data(**kwargs)
        context['is_not_ans'] = Ans.objects.filter(
            sticker=self.kwargs['pk']
        ).exists()

        return context


class StickerCreate(LoginRequiredMixin, CreateView):
    """Представление для создания нового объекта Sticker."""

    model = Sticker
    template_name = 'bulletin/sticker_create.html'
    form_class = StickerForms

    def form_valid(self, form):
        """Метод заполняет поле author в модели."""
        instance = form.save(commit=False)
        instance.author = self.request.user
        instance.save()

        return super().form_valid(form)


class StickerUpdate(LoginRequiredMixin, UpdateView):
    """Представление для редактирования объекта Sticker."""

    model = Sticker
    template_name = 'bulletin/sticker_create.html'
    form_class = StickerForms

    def dispatch(self, request, *args, **kwargs):
        """Метод запрещает изменение чужих объявлений."""
        id_ = self.kwargs.get('pk')
        author_sticker = Sticker.objects.get(pk=id_).author
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if request.user != author_sticker:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class StickerDelete(LoginRequiredMixin, DeleteView):
    """Представление реализует удаление объекта Sticker."""

    model = Sticker
    template_name = 'bulletin/sticker_delete.html'
    success_url = reverse_lazy('stickers')

    def dispatch(self, request, *args, **kwargs):
        """Метод запрещает удаление чужих объявлений."""
        id_ = self.kwargs.get('pk')
        author_sticker = Sticker.objects.get(pk=id_).author
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if request.user != author_sticker:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class AnsList(LoginRequiredMixin, ListView):
    """Представление откликов на объявление."""

    model = Ans
    ordering = '-datetime_of_creation'
    template_name = 'bulletin/ans_list.html'
    context_object_name = 'ans_sticker_list'
    paginate_by = 10

    def get_queryset(self, **kwargs):
        """Метод возвращает список откликов выбранного объявления."""
        id_ = self.kwargs.get('pk')
        queryset = Ans.objects.filter(sticker=id_)
        return queryset


class AnsDetail(LoginRequiredMixin, DetailView):
    """Класс обрабатывает конкретный отклик Ans."""

    model = Ans
    template_name = 'bulletin/ans.html'
    context_object_name = 'ans'


class AnsCreate(LoginRequiredMixin, CreateView):
    """Представление реализующее создание откликов."""

    model = Ans
    template_name = 'bulletin/ans_create.html'
    form_class = AnsForms

    def form_valid(self, form):
        """Метод заполняет поле author и sticker в модели Ans."""
        instance = form.save(commit=False)
        instance.author = self.request.user
        sticker_response = Sticker.objects.get(pk=self.kwargs.get('pk'))
        instance.sticker = sticker_response
        instance.save()
        return super().form_valid(form)


class PrivateList(LoginRequiredMixin, ListView):
    """Приватная страница пользователя."""

    model = Ans
    ordering = '-datetime_of_creation'
    template_name = 'bulletin/private_list.html'
    context_object_name = 'private'
    paginate_by = 10

    def get_queryset(self, **kwargs):
        """Метод возвращает отклики Ans текущего User на его \
        объявления Sticker."""
        user = self.request.user
        queryset = Ans.objects.filter(sticker__author=user)
        self.filterset = AnsFilter(self.request.GET, queryset)

        return self.filterset.qs

    def get_context_data(self, **kwargs):
        """Добавляем в контекст объект фильтрации."""
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class AnsAccept(LoginRequiredMixin, DetailView):
    """Класс обрабатывает принятие отклика Ans."""

    model = Ans
    template_name = 'bulletin/ans_accept.html'
    context_object_name = 'ans_accept'

    def post(self, request, *args, **kwargs):
        """Метод реализует принятие отклика на объявление. \
        Переключает Ans.condition в положение True."""
        if request.method == 'POST':
            id_ = self.kwargs.get('pk')
            ans_response = Ans.objects.get(pk=id_)
            ans_response.condition = True
            ans_response.save(update_fields=['condition'])
            return redirect('private_list')


class AnsDelete(LoginRequiredMixin, DeleteView):
    """Представление реализует удаление объекта Ans."""

    model = Ans
    template_name = 'bulletin/ans_delete.html'
    success_url = reverse_lazy('private_list')
