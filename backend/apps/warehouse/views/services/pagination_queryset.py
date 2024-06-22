# def get_pag_queryset(ObjectModel, query=None):
#     queryset = []
#     queries = query.split(" ")
#     for q in queries:
#         items = ObjectModel.objects.filter(
#                 Q(item__name__icontains=q) |
#                 Q(income_seria__icontains=q) |
#                 Q(item__seria__icontains=q)
#             ).distinct()
#         for new in items:
#             queryset.append(new)
#
#     return list(set(queryset))