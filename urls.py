"""BBS14 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from app01 import views
from django.views.static import serve
from BBS14 import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # 路由分发的本质   include
    # re_path(r'^index/', ([
    #             re_path(r'^index_1/', ([
    #                 path(r'^index_1_1/', views.index),
    #                 path(r'^index_1_2/', views.index),
    #                 path(r'^index_1_3/', views.index),
    #
    #                                     ], None, None)),
    #             re_path(r'^index_2/', views.index),
    #             re_path(r'^index_3/',views.index),
    #                      ], None, None)),
                
            
    
    re_path(r'^register/', views.register, name='reg'),
    re_path(r'^login/', views.login, name='log'),
    
    # 图片验证码相关操作
    re_path(r'^get_code/', views.get_code, name='gc'),
    
    # 首页
    re_path(r'^home/', views.home, name='home'),
    
    # 修改密码
    re_path(r'^set_password/', views.set_password, name='set_pwd'),
    
    # 推出登录
    re_path(r'^logout/', views.logout, name='logout'),
    
    # 暴露后端值订文件夹资源
    re_path(r'^media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}),
    # 在暴露资源的时候一定要明确该资源是否可以暴露
    
    # 点赞点踩
    re_path(r'^up_or_down/', views.up_or_down),
    
    # 评论
    re_path(r'^comment/', views.comment),
    
    # 后台管理
    re_path(r'^backend/', views.backend),
    # 添加文章
    re_path(r'^add/article/', views.add_article),
    # 编辑器上传图片接口
    re_path(r'^upload_image/', views.upload_image),
    # 修改用户头像
    re_path(r'^set/avatar/', views.set_avatar),
    
    # 个人站点页面搭建
    re_path(r'^(?P<username>\w+)/$', views.site, name='site'),
    
    # 侧边栏筛选功能
    # re_path(r'^(?P<username>\w+)/category/(\d+)', views.site),
    # re_path(r'^(?P<username>\w+)/tag/(\d+)', views.site),
    # re_path(r'^(?P<username>\w+)/archive/(\w+)/', views.site),
    # 上面的三条url其实可以合并成一条
    re_path(r'^(?P<username>\w+)/(?P<condition>category|tag|archive)/(?P<param>.*)', views.site),
    
    # 文章详情页
    re_path(r'^(?P<username>\w+)/article/(?P<article_id>\d+)', views.article_detail),
]
