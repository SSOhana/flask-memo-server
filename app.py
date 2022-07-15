from flask import Flask
from flask_jwt_extended import JWTManager, jwt_manager
from flask_restful import Api
from config import Config
from resources.follow import FollowListResource, FollowResource
from resources.memo import MemoInfoResource, MemoInfooResource, MemoListResource
from resources.user import UserLoginResource, UserLogoutResource, UserRegisterResource, jwt_blacklist

app = Flask(__name__)

# 환경 변수 설정
app.config.from_object(Config)

jwt = JWTManager(app)

# 로그아웃 된 유저인지 확인하는 함수 작성
@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload) :
    jti = jwt_payload['jti']
    return jti in jwt_blacklist

# api 라는 변수 만들기
api = Api(app)


# 경로와 리소스를 연결한다.
api.add_resource(UserRegisterResource, '/users/register')       # 회원가입 API
api.add_resource(UserLoginResource, '/users/login')             # 로그인 API
api.add_resource(UserLogoutResource, '/users/logout')           # 로그아웃 API
api.add_resource(MemoListResource, '/memo')                     # 메모 생성, 조회 API
api.add_resource(MemoInfoResource, '/memo/<int:memo_Id>')       # 메모
api.add_resource(FollowResource, '/follow/<int:follow_id>')     # 친구 맺기 API
api.add_resource(FollowListResource, '/follow')                 # 친구 게시글 API

if __name__ == '__main__' :
    app.run()