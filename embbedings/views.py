from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("jinaai/jina-embeddings-v3", trust_remote_code=True)
"""
task = "retrieval.query"
embeddings = model.encode(
    ["What is the weather like in Berlin today?"],
    task=task,
    prompt_name=task,
)
"""
@api_view(["POST"])
def generate_embedding_view(request):
    data = request.data  # Obtener los datos enviados en el POST
    type = data.get("type")
    if type:
        file = request.FILES['data']
        if file and type == "txt":
            content = [line.decode("utf-8").strip() for line in file.readlines()]
            task = "retrieval.query"
            embeddings = model.encode(
                content,
                task=task,
                prompt_name=task,
            )
            response = []
            for embedding, text in zip(embeddings, content):
                item = {
                    "vector": embedding,
                    "metadata": {
                        "text": text  # Additional metadata
                    }
                }
                response.append(item)
    return Response({"response": response}, status=status.HTTP_200_OK)
