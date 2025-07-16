# Команды для проверки проекта News Portal в Django shell
# Открыть shell через
# python manage.py shell

# Затем вставьте следующий Python-код:

from django.contrib.auth.models import User
from news.models import Author, Category, Post, Comment

# 1. Создание пользователей
u1 = User.objects.create_user('john_doe', password='1234')
u2 = User.objects.create_user('jane_smith', password='1234')

# 2. Создание авторов
a1 = Author.objects.create(user=u1)
a2 = Author.objects.create(user=u2)

# 3. Категории
cat1 = Category.objects.create(name='Politics')
cat2 = Category.objects.create(name='Science')
cat3 = Category.objects.create(name='Education')
cat4 = Category.objects.create(name='Sports')

# 4. Статьи и новость
post1 = Post.objects.create(author=a1, post_type='AR', title='Political Crisis', content='Some detailed political article...')
post2 = Post.objects.create(author=a1, post_type='AR', title='Education Reform', content='Important discussion about education system...')
post3 = Post.objects.create(author=a2, post_type='NW', title='Breaking News: Tech Discovery', content='New tech invention...')

# 5. Присвоение категорий
post1.categories.add(cat1, cat2)
post2.categories.add(cat3)
post3.categories.add(cat2, cat4)

# 6. Комментарии
c1 = Comment.objects.create(post=post1, user=u2, text='Great article!')
c2 = Comment.objects.create(post=post1, user=u1, text='Thanks!')
c3 = Comment.objects.create(post=post2, user=u2, text='Very informative.')
c4 = Comment.objects.create(post=post3, user=u1, text='Wow! Surprising.')

# 7. Лайки/дизлайки
post1.like()
post1.like()
post2.dislike()
c1.like()
c2.dislike()
c3.like()
c4.like()

# 8. Обновление рейтингов
a1.update_rating()
a2.update_rating()

# 9. Лучший пользователь
best_author = Author.objects.order_by('-rating').first()
print(f'Best author: {best_author.user.username}, Rating: {best_author.rating}')

# 10. Лучшая статья
best_post = Post.objects.order_by('-rating').first()
print(f'Date: {best_post.created_at}, Author: {best_post.author.user.username}, Rating: {best_post.rating}')
print(f'Title: {best_post.title}')
print(f'Preview: {best_post.preview()}')

# 11. Комментарии к этой статье
for c in best_post.comment_set.all():
    print(f'Date: {c.created_at}, User: {c.user.username}, Rating: {c.rating}')
    print(f'Text: {c.text}\n')