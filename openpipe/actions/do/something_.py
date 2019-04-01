"""
Prints "Hello World!" followed by the config item
"""
from openpipe.pipeline.engine import ActionRuntime


class Action(ActionRuntime):

    category = "Data Analysis"

    optional_config = """
    $_$     # The optional config item, defaults to the input item
    """

    def on_input(self, item):
        print("Hello World!", self.config)
        self.put(item)
