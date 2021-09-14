from .models import Comment

def fetchComments(request, post):
    comments = Comment.objects.filter(post=post)
        
    data = {}
    result = []
    for comment in comments:
        
        result.append({
            'id':comment.id,
            'comment':comment.comment,
            'commenter_image':comment.user.profile.profile_image.url
            })

    data['results']=result

    return data