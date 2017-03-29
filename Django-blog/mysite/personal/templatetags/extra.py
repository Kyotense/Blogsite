from django import template
from about.models import AboutUs
from blog.models import Post
from games.models import VideoGame

register = template.Library()

@register.inclusion_tag("about/abouts.html")
def about_us():
    about_list = AboutUs.objects.all()
    return {'about_list':about_list}

@register.inclusion_tag("blog/blog_carousel.html")
def blog_record():
    blog_list = Post.objects.all()
    return {'blog_list':blog_list}

@register.inclusion_tag("games/games_carousel.html")
def game_record():
    game_list = VideoGame.objects.all()
    return {'game_list':game_list}
