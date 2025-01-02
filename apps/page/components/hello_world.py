from django_unicorn.components import UnicornView


class HelloWorldView(UnicornView):
    name = "World"

    def clear_name(self):
        self.name = ""
