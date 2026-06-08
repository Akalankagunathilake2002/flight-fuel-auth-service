import grpc
from concurrent import futures

from app.grpc.generated import auth_pb2
from app.grpc.generated import auth_pb2_grpc

from app.db.database import SessionLocal
from app.models.user import User


class AuthService(auth_pb2_grpc.AuthServiceServicer):

    def ValidateUser(self, request, context):

        username = request.username

        print(f"Received username: {username}")

        db = SessionLocal()

        try:

            user = (
                db.query(User)
                .filter(User.username == username)
                .first()
            )

            if user:
                return auth_pb2.ValidateUserResponse(
                    exists=True,
                    username=user.username
                )

            return auth_pb2.ValidateUserResponse(
                exists=False,
                username=""
            )

        finally:
            db.close()


def serve():

    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10)
    )

    auth_pb2_grpc.add_AuthServiceServicer_to_server(
        AuthService(),
        server
    )

    server.add_insecure_port("[::]:50051")

    print("gRPC Server running on port 50051")

    server.start()

    server.wait_for_termination()


if __name__ == "__main__":
    serve()