from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Category, Article, Comment, Ingredient, RecipeIngredient

# 게시글 C
class ArticleCreateSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'content', 'category', 'tags', 'recipe', 'ingredients']


# 게시글 U
class ArticlePutSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'content', 'image', 'category', 'tags', 'recipe', 'ingredients']


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return obj.user.nickname
    
    # 댓글 조회 시리얼라이저-직렬화
    class Meta:
        model = Comment
        fields = ['comment', 'author', 'created_at', 'updated_at'] # author, created_at 등 조회에 필요한 것들

# 레시피 재료 가져오기
class RecipeIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeIngredient
        fields = ['ingredient_quantity', 'ingredient_unit', ]

# 게시글 R
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"

    user = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    comments_set = CommentSerializer(many=True) # comments_set이라는 역참조 필드 존재
    comments_count = serializers.SerializerMethodField()
    recipeingredient_set = RecipeIngredientSerializer(many=True) # related_name을 이용해서 변수 이름을 정하자

    def get_user(self, obj):
        return obj.user.nickname
    
    def get_comments_count(self, obj):
        return obj.comments_set.count()
    
    def get_likes_count(self, obj):
        return obj.likes.count()


# 댓글 작성
class CommentCreateSerializer(ModelSerializer):
    # 댓글 생성 시리얼라이저-직렬화, 검증까지
    class Meta:
        model = Comment
        fields = ['comment',]   # json으로 받을 데이터 필드


# 동시 저장을 위해 모델 저장 2개 설정
class RecipeIngredientCreateSerializer(ModelSerializer):
    class Meta:
        model = RecipeIngredient
        fields = ['ingredient_quantity', 'ingredient_unit']

    class Veta:
        model = Ingredient
        fields = "__all__"