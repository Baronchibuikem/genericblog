from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EmailPostForm, CommentForm, SubscriptionForm
from django.core.mail import send_mail


def post_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    blogs = Post.published.all().order_by("-publish")
    form = SubscriptionForm(request.POST or None,
                            request.FILES or None)  # we embedded a form where users can input their emails to subcribe to our newsletter
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Thank you for subscribing")
    else:
        form = SubscriptionForm
    query = request.GET.get("q")
    if query:
        blogs = blogs.filter(Q(title__icontains=query)|
                                         Q(body__icontains=query)

                                         ).distinct()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        blogs = blogs.filter(category=category)
    paginator = Paginator(blogs, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    template = 'blog/post/list.html'
    context = {
        'posts': posts,
        'page': page,
        'form': form,
        'category': category, 
        'categories': categories,
    }
    return render(request, template, context )


def post_detail(request, year, month, day, post, category_slug=None):
    category = None
    categories = Category.objects.all()
    post = get_object_or_404(Post, slug=post,
            status='published',
            publish__year=year,
            publish__month=month,
            publish__day=day)
    comments = post.comments.filter(approved_comment=True)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.post = post
                new_comment.save()
        messages.add_message(request, messages.INFO, 'Your Comment has been submitted for review. It will be added shortly')
    else:
        comment_form = CommentForm
    template = 'blog/post/detail.html',
    context ={
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
         'category': category, 
        'categories': categories,}
    return render(request, template, context)


"""def post_share(request, post_id):
    #Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        #Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(
                post.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
            from_email = settings.EMAIL_HOST_USER
            to_email = [from_email, 'youremail@mail.com']

            # send_mail(subject, message, 'admin@myblog.com',
            #           [cd['to']])
            send_mail(
                subject, message, from_email, to_email, fail_silently=False,
            )

            sent = True
    else:
        form = EmailPostForm()
    template = 'blog/post/share.html'
    context = {
        'post': post,
        'form': form,
        'sent': sent,
    }
    return render(request, template, context)"""




