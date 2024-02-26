import grpc
from protos import clothing_store_pb2, clothing_store_pb2_grpc


def get_tshirt(channel):
    req = clothing_store_pb2.ArticleSearchRequest(barcode="1")
    response = channel.GetArticleByBarcode(req)
    print(response)


with grpc.insecure_channel('localhost:50051') as channel:
    stub = clothing_store_pb2_grpc.ClothingStoreStub(channel=channel)
    get_tshirt(stub)

