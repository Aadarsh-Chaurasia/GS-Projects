from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from django.contrib.auth.models import User
import json

# Handle /api/blogposts/
def list_or_create_blog_post(request):
    if request.method == 'GET':
        # List all blogs
        print('Hello')
        blogs = BlogPost.objects.all()
        blog_list = [{'title': blog.title, 'content': blog.content} for blog in blogs]
        return JsonResponse(blog_list, safe=False)

    elif request.method == 'POST':
        # Create a new blog (authentication required)
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'Authentication required to create a blog.'}, status=401)

        data = json.loads(request.body)
        title = data.get("title")
        content = data.get("content")
        if title and content:
            post = BlogPost.objects.create(title=title, content=content, author=request.user)
            return JsonResponse({
                "id": post.id,
                "title": post.title,
                "content": post.content,
                "author": post.author.username
            }, status=201)
        else:
            return JsonResponse({"error": "Title and content are required."}, status=400)

    return JsonResponse({'error': 'Method not allowed'}, status=405)


# Handle /api/blogposts/{id}/
def blog_post_detail(request, post_id):
    if request.method == 'GET':
        post = get_object_or_404(BlogPost, id=post_id)
        post_data = {
            "id": post.id,
            "title": post.title,
            "content": post.content,
            "author": post.author.username
        }
        return JsonResponse(post_data)

    # PUT method will update the blog post
    if request.method == "PUT":
        # Authenticating user
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'Authentication required to create a blog.'}, status=401)

        # Checking if the user requesting is author or not
        post = get_object_or_404(BlogPost, id=post_id)
        if post.author != request.user:
            return JsonResponse({"error": "You are not the author of this post."}, status=403)

        data = json.loads(request.body)
        title = data.get("title")
        content = data.get("content")
        post.title = title if title else post.title
        post.content = content if content else post.content
        post.save()
        return JsonResponse({
            "id": post.id,
            "title": post.title,
            "content": post.content,
            "author": post.author.username
        })

    # Delete method will delete the blog post
    if request.method == "DELETE":
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'Authentication required to create a blog.'}, status=401)

        post = get_object_or_404(BlogPost, id=post_id)
        if post.author != request.user:
            return JsonResponse({"error": "You are not the author of this post."}, status=403)

        post.delete()
        return JsonResponse({"message": "Post deleted successfully."}, status=204)
    
    return JsonResponse({"error": "Invalid request method."}, status=405)




