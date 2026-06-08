import grpc

from app.grpc.generated import auth_pb2
from app.grpc.generated import auth_pb2_grpc


channel = grpc.insecure_channel("localhost:50051")

stub = auth_pb2_grpc.AuthServiceStub(channel)

response = stub.ValidateUser(
    auth_pb2.ValidateUserRequest(
        username="akalanka"
    )
)

print(response)