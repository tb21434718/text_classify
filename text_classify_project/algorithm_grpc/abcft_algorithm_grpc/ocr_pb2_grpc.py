# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import ocr_pb2 as ocr__pb2


class OcrServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.detectElement = channel.unary_unary(
        '/com.abcft.pdfextract.rpc.ocr.OcrService/detectElement',
        request_serializer=ocr__pb2.OcrRequest.SerializeToString,
        response_deserializer=ocr__pb2.ElementReply.FromString,
        )
    self.predictText = channel.unary_unary(
        '/com.abcft.pdfextract.rpc.ocr.OcrService/predictText',
        request_serializer=ocr__pb2.OcrRequest.SerializeToString,
        response_deserializer=ocr__pb2.TextReply.FromString,
        )
    self.batchPredictText = channel.unary_unary(
        '/com.abcft.pdfextract.rpc.ocr.OcrService/batchPredictText',
        request_serializer=ocr__pb2.BatchOcrRequest.SerializeToString,
        response_deserializer=ocr__pb2.TextReply.FromString,
        )


class OcrServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def detectElement(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def predictText(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def batchPredictText(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_OcrServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'detectElement': grpc.unary_unary_rpc_method_handler(
          servicer.detectElement,
          request_deserializer=ocr__pb2.OcrRequest.FromString,
          response_serializer=ocr__pb2.ElementReply.SerializeToString,
      ),
      'predictText': grpc.unary_unary_rpc_method_handler(
          servicer.predictText,
          request_deserializer=ocr__pb2.OcrRequest.FromString,
          response_serializer=ocr__pb2.TextReply.SerializeToString,
      ),
      'batchPredictText': grpc.unary_unary_rpc_method_handler(
          servicer.batchPredictText,
          request_deserializer=ocr__pb2.BatchOcrRequest.FromString,
          response_serializer=ocr__pb2.TextReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'com.abcft.pdfextract.rpc.ocr.OcrService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))