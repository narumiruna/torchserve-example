from ts.context import Context


class ModelHandler:
    def initialize(self, context: Context):
        pass

    def handle(self, data, context):
        return ["Hello, world!"]
