from django.http import Http404

def has_post_access(test_object,request_user,method):

    if method == "view":
        if (test_object.author.id == request_user.id) or (test_object.is_published):
            return True
        
        else:
            raise Http404("Post not published yet")
    #Update methods
    else:
        if test_object.author.id == request_user.id:
            return True
        else:
            raise Http404("Cannot edit post: Permission Error")


def has_comment_update_delete_access(test_object,request_user):

    if (test_object.author.id == request_user.id):
        return True
    
    else:
        raise Http404("Permission Error: You can only edit/delete your own comments")