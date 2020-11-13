from rest_framework import viewsets

class GetUserForPostView(viewsets.ModelViewSet):
    def create(self, request):
        request.data.update({'user': request.user.id})
        return super(GetUserForPostView, self).create(request)

    def update(self, request, pk=None):
        request.data.update({'user': request.user.id})
        return super(GetUserForPostView, self).update(request, pk)