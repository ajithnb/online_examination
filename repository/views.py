from django.shortcuts import render
from repository.models import questiondb,AnswersubmissionDB
from repository.serializers import questionserialzer,SubmissionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class QuestionCreateListView(APIView):
    def get(self,request):
        qs=questiondb.objects.all()
        serializer_instance=questionserialzer(qs,many=True)
        return Response(serializer_instance.data)

    def post(self,request):
        form_data = request.data
        serilizer_instance = questionserialzer(data = form_data)
        if serilizer_instance.is_valid():
            actual_data = serilizer_instance.validated_data
            questiondb.objects.create(**actual_data)
            return Response(data = serilizer_instance.data)
        else:
            return Response(data = serilizer_instance.errors)

class QuestionRetrieveUpdateDelete(APIView):
    def get(self,request,pk):
        qs = questiondb.objects.get(id = pk)
        serializer_instance = questionserialzer(qs)
        return Response(data = serializer_instance.data)

    def put(Self,request,pk):
        form_data = request.data
        serializer_instance = questionserialzer(data = form_data)
        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            questiondb.objects.filter(id = pk).update(**actual_data)
            return Response(data = serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

    def delete(self,request,pk):
        questiondb.objects.filter(id = pk).delete()
        return Response(data = {"msg" : "question deleted"})
    

class SubmissionReteieveUpdateDelete(APIView):
    def get(self,request):

        qs=AnswersubmissionDB.objects.all()
        serializer_instance = SubmissionSerializer(qs, many=True)
        return Response(data=serializer_instance.data)
    
    def post(self,request):
        form_data=request.data
        serializer_instance=SubmissionSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data=serializer_instance.validated_data
            AnswersubmissionDB.objects.create(**actual_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)