## Anon_blog
____
## Цель работы:
Разработать и реализовать клиент-серверную информационную систему, реализующую механизм CRUD
## Реализованные возможности
+ добавление текстовых заметок в общую ленту
+ реагирование разных видов на чужие заметки (лайки, дизлайки)
+ добавление комментариев к чужим заметкам
+ "раскрывающиеся комментарии"
+ добавление изображений к заметкам
+ есть паджинация
____
## Ход работы
### 1. Разработка пользовательского интерфейса
В ходе выполнения работы был разработан пользовательский интерфейс при помощи графического редактора [Figma](https://www.figma.com/community)\
![главнвя стр](https://user-images.githubusercontent.com/98755619/209427743-10ebdedf-408f-4c24-b6b2-eb77fd1894df.png) <br>
![подроб инф](https://user-images.githubusercontent.com/98755619/209427754-805045fc-0180-4341-9df3-e820a8352579.png) <br>

### 2. Описание пользовательских сценариев работы
1) Пользователь заходит на сайт и попадает на главную страничку, на которой отображаются последние десять постов.
2) Клиент может нажать на кнопку "показать подробнее", которая располагается под каждым постом, и у него откроется профильная
страничка поста, на которой можно отреагировать на пост, а также оставить свой комментарий.
3) При желании пользователь может нажать на кнопку "новая запись", которая располагается в верхней части сайта, и у него
откроется страничка где он может создать пост, а также прикрепить к нему свою картинку.

### 3. Описание API сервера и хореографии

![add post](https://user-images.githubusercontent.com/98755619/209427777-dc4de841-ad43-43c5-ba56-0e94452544ac.png)

![like_comment](https://user-images.githubusercontent.com/98755619/209427781-af08560e-9a4c-41ff-9ae5-df92bfcea689.png)

### 4. Описание структура базы данных

![BD](https://user-images.githubusercontent.com/98755619/209427793-81ea0bf9-fa2e-42c2-ba0b-0fc8a2375731.png)

### 5. Алгоритмы
Создание поста:
![создание поста](https://user-images.githubusercontent.com/98755619/209427845-17922c36-567e-449a-87d7-8da72af3b9f4.png)

Оставление реакции под постом:
![реакция под постом](https://user-images.githubusercontent.com/98755619/209427854-82f5b65e-682e-42db-8345-e51b17e17b69.png)

Оставление комментария:
![комментарий](https://user-images.githubusercontent.com/98755619/209427866-8d5d4eb1-bafa-457b-a188-5e5286c96d51.png)

### 6. Значимые части кода
примеры модели Post
```
class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    body = models.TextField()
    image = models.ImageField(
        'Картинка',
        upload_to='posts/',
        blank=True
    )
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']
```
Основные view функции:
```
def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, posts_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }

    return render(request, 'posts/index.html', context)


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST,
                        files=request.FILES or None,)
        if form.is_valid():
            commit = form.save(commit=False)
            commit.save()
            return redirect('posts:index')
        return render(request, 'posts/create_post.html', {'form': form})
    form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})
```
