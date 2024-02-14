from espresso.tasks import sentence_to_morse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication


class MorseCodeEntryView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        # Access posted data using request.data dictionary
        sentence = request.data.get('sentence')

        if sentence:
            # Call the sentence_to_morse task
            morse_code_task = sentence_to_morse.delay(sentence)
            return Response({"task_id": morse_code_task.id}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"error": "No sentence provided"}, status=status.HTTP_400_BAD_REQUEST)


class MorseCodeResultView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, task_id, format=None):
        # Retrieve the result of the task using the task_id
        try:
            morse_code_task = sentence_to_morse.AsyncResult(task_id)
            morse_code = morse_code_task.get(
                timeout=1)  # Specify a timeout if needed
            return Response({"morse_code": morse_code}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
