from rest_framework.response import Response
from rest_framework.views import APIView
from docs.serializers import ItemImportSerializer, \
    ItemUpdateSerializer
from docs.models import Item
from rest_framework.parsers import JSONParser
from docs.restFunctions import dfsGet, dfsDelete, get_graph


class ItemPostView(APIView):
    def post(self, request):
        data = JSONParser().parse(request)
        items = data["items"]
        date = data["updateDate"]
        for item in items:
            item["date"] = date
            if item["type"] == "FILE":
                if item["size"] <= 0:
                    return Response("Validation Failed", status=400)
            if item["type"] == "FOLDER":
                try:
                    if item["url"] > 255:
                        return Response("Validation Failed", status=400)
                except KeyError:
                    pass
            serializer = ItemImportSerializer(data=item)
            if serializer.is_valid():
                serializer.save()
            else:
                try:
                    if serializer.errors["id"][0] == "item с таким id уже существует.":
                        instance = Item.objects.get(pk=item["id"])
                        serializer = ItemUpdateSerializer(data=item, instance=instance)
                        if serializer.is_valid():
                            serializer.save()
                    else:
                        return Response("Validation Failed", status=400)
                except KeyError:
                    return Response("Validation Failed", status=400)
        files = Item.objects.all()
        return Response(status=200)


class ItemDeleteView(APIView):
    # DELETE
    def delete(self, request, pk):
        date = request.GET.get('date')
        files = Item.objects.all()
        try:
            file = Item.objects.get(pk=pk)
        except KeyError:
            return Response("Item not found", status=404)

        graph = dict()
        try:
            get_graph(graph, files)
            visited = dfsDelete(graph, file.id, [])
            if file.parentId != '':
                parent = Item.objects.get(pk=file.parentId)
                data = {'type': parent.type, 'date': date}
                serializer = ItemUpdateSerializer(data=data, instance=parent)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response("Validation Failed", status=400)
            for i in range(len(visited)):
                id = visited[len(visited) - 1 - i]
                obj = Item.objects.get(pk=id)
                obj.delete()

            return Response(status=200)
        except:
            return Response("Validation Failed", status=400)


class ItemGetView(APIView):
    def get(self, request, pk):
        files = Item.objects.all()
        try:
            file = Item.objects.get(pk=pk)
        except:
            return Response("Item not found", status=404)
        graph = dict()
        visited = []
        get_graph(graph, files)
        data = dfsGet(graph, file.id, visited)
        return Response(data=data, status=200)
