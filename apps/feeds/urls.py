from django.urls import path
from apps.feeds.views import *

app_name = 'feeds'

# TODO: Likes Endpoint for Post and Reply

urlpatterns = [
    path('', show_all, name='show_all'),
    path('post/<uuid:id>/', detail_post, name='detail_post'),
    path('tabs/<str:all_tabs>/', change_tabs, name='change_tabs'),
    
    # Posts
    path('create/post/', create_post, name='create_post'),
    path('post-delete/<uuid:id>', delete_post, name='delete_post'),
    path('post-edit/<uuid:id>', edit_post, name='edit_post'),
    path('post-like/<uuid:id>', like_post, name='like_post'),
    path('post-unlike/<uuid:id>', unlike_post, name='unlike_post'),
    path('json/post/', post_json, name='post_json'),
    path('json/post/user/<int:user>', post_json_by_user, name='post_json_by_user'),
    path('json/post/id/<uuid:id>/', post_json_by_id, name='post_json_by_id'),
    
    # Replies
    path('create/reply/', create_reply, name='create_reply'),
    path('reply-delete/<uuid:id>', delete_reply, name='delete_reply'),
    path('reply-like/<uuid:id>', like_reply, name='like_reply'),
    path('reply-unlike/<uuid:id>', unlike_reply, name='unlike_reply'),
    path('json/reply/<uuid:post_id>', reply_json, name='reply_json'),
    path('json/reply/user/<uuid:post_id>/<int:user>', reply_json_by_user, name='reply_json_by_user'),
    path('json/reply/id/<uuid:id>/', reply_json_by_id, name='reply_json_by_id'),
    
    # Reports
    path('report/', report, name='report'),
    path('json/report/', report_json, name='report_json'),
]