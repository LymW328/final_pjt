1. Article, Comment 모델에서 user id키를  외부키로 가지고 오고 싶은데 dj-rest-auth를 사용한 경우 - 이는 N:1의 관계로 설정가능 설정되어 있다.
2. 과연 dj-rest-auth에서 Article과 Comment에 N:1의 관계로 user id 연결할 수 있는가? 
 - user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)로, rest-auth를 사용하지 않았을 떄와 동일한 코드로 설정 가능하다.
 
 3. 1번 댓글이 작성된 게시물의 content조회 => comment.article_id
 4. article = Article.objects.get(pk=1)
 5. django에서 USER모델을 참조하는 법
    5-1. medel.py에서는 setting.AUTH_USER_MODEL
    다른모든곳에서는 get_user_model()

6. article create 시 not null constraint - user_id칼럼 누락
    저장 시 작성자 정보가 같이 저장 될 수 있도록 save의 commit옵션 사용
    if ...,is valid():
        article = form.save(commit=False)
        article.user = request.user
    ??? serializer.is_valisd(raiser_exception=True) 와 같을까?
