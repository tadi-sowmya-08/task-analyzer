from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaskSerializer

@api_view(['POST'])
def analyze_tasks(request):
    serializer = TaskSerializer(data=request.data, many=True)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    tasks = serializer.validated_data

    # 🧮 Simple scoring formula
    results = []
    for t in tasks:
        score = t['importance'] * 10 - t['estimated_hours'] * 2
        results.append({
            "title": t['title'],
            "score": round(score, 2)
        })

    # Sort tasks by score (highest first)
    results = sorted(results, key=lambda x: x['score'], reverse=True)

    return Response(results)

