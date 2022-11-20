
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from movies.serializers import MovieListSerializer , MovieDetailSerializer, MovieCommentSerializer, TrendListSerializer

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404

from .models import Movie, MovieComment, Trend
 

# 영화 리스트
# 221017(월)_코딩 Live 강의 Python 트랙_오후_5_Build RESTful API - Article 20분까지 체크함!
@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)   
    return Response(serializer.data)
    
@api_view(['GET'])
def trend_list(request):
    movies = Trend.objects.all()
    serializer = TrendListSerializer(movies, many=True)   
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    # comments = movie.comment_set.all()
    # 역참조한 comments정보를 어떻게 serializer로 같이 보내줄까?
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
def movie_comment_list(request):
    if request.method == 'GET':
        comments = MovieComment.objects.all()
        serializer = MovieCommentSerializer(comments, many=True)   
        return Response(serializer.data)



# 이 두개가 필요한가?

@api_view(['GET', 'DELETE', 'PUT'])
def movie_comment_detail(request, comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(MovieComment, pk=comment_pk)

    if request.method == 'GET':
        serializer = MovieCommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = MovieCommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
