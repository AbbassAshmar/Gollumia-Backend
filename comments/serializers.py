from rest_framework import serializers
from .models import Comment,Reply, CommentLikeDislike,ReplyLikeDislike
from authentication.models import User
from authentication.serializers import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField('get_likes')
    dislikes = serializers.SerializerMethodField('get_dislikes')
    interaction = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = "__all__"

    def get_likes(self, obj):
        return CommentLikeDislike.objects.filter(comment=obj, interaction_type=1).count()

    def get_dislikes(self, obj):
        return CommentLikeDislike.objects.filter(comment=obj, interaction_type=2).count()

    def get_interaction(self, obj) :
        user = None
        request = self.context.get("request")
        
        if request and hasattr(request, "user"):
            user = request.user

        if user and user.is_authenticated :
            commentLikeDislike = CommentLikeDislike.objects.filter(user=user, comment=obj).first()
            if not commentLikeDislike :
                return 0
            return commentLikeDislike.interaction_type
        
        return 0
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["user"]= UserSerializer(instance.user).data
        return data

class ReplySerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()
    dislikes = serializers.SerializerMethodField()
    interaction = serializers.SerializerMethodField()

    class Meta:
        model = Reply
        fields = "__all__"

    def get_likes(self, obj):
        return ReplyLikeDislike.objects.filter(reply=obj, interaction_type=1).count()

    def get_dislikes(self, obj):
        return ReplyLikeDislike.objects.filter(reply=obj, interaction_type=2).count()
    
    def get_interaction(self, obj) :
        user = None
        request = self.context.get("request")
        
        if request and hasattr(request, "user"):
            user = request.user

        if user and user.is_authenticated :
            replyLikeDislike = ReplyLikeDislike.objects.filter(user=user, reply=obj).first()
            if not replyLikeDislike :
                return 0
            return replyLikeDislike.interaction_type
        
        return 0
    
    def to_representation(self,instance):
        data = super().to_representation(instance)
        data["user"] = UserSerializer(instance.user).data

        if data["replying_to"] : 
            data['replying_to'] = {
                'id' : instance.replying_to.id,
                "text" : instance.replying_to.text,
                "movie" : instance.replying_to.movie.id,
                "user" : UserSerializer(instance.replying_to.user).data,
                "likes": ReplyLikeDislike.objects.filter(reply=instance.replying_to, interaction_type=1).count(),
                "dislikes": ReplyLikeDislike.objects.filter(reply=instance.replying_to, interaction_type=2).count(),
                "parent_comment" : instance.replying_to.parent_comment.id,
                "created_at" : instance.replying_to.created_at
            }
        else : 
            data["replying_to"] = {
                'id' : instance.parent_comment.id,
                "text" : instance.parent_comment.text,
                "movie" : instance.parent_comment.movie.id,
                "user" : UserSerializer(instance.parent_comment.user).data,
                "likes": CommentLikeDislike.objects.filter(comment=instance.parent_comment, interaction_type=1).count(),
                "dislikes": CommentLikeDislike.objects.filter(comment=instance.parent_comment, interaction_type=2).count(),
                "parent_comment" : None,
                "created_at" : instance.parent_comment.created_at
            }
        
        return data

class CommentReplySerializer(serializers.ModelSerializer) : 
    likes = serializers.SerializerMethodField()
    dislikes = serializers.SerializerMethodField()
    interaction = serializers.SerializerMethodField()

    class Meta : 
        model = Comment
        fields ="__all__"

    def get_interaction(self, obj) :
        user = None
        request = self.context.get("request")
        
        if request and hasattr(request, "user"):
            user = request.user

        if user and user.is_authenticated :
            commentLikeDislike = CommentLikeDislike.objects.filter(user=user, comment=obj).first()
            print(commentLikeDislike)
            if not commentLikeDislike :
                return 0
            return commentLikeDislike.interaction_type
        
        return 0

    def get_likes(self, obj):
        return CommentLikeDislike.objects.filter(comment=obj, interaction_type=1).count()

    def get_dislikes(self, obj):
        return CommentLikeDislike.objects.filter(comment=obj, interaction_type=2).count()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["user"]= UserSerializer(instance.user).data
        data["replies"] = ReplySerializer(instance.replies,many=True,context=self.context).data
        return data

