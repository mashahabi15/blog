class BaseView:
    def __init__(self):
        pass

    def initial(self, request, *args, **kwargs):
        self.user = request.user
        if not self.user.is_authenticated:
            return
