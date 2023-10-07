from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from drf_api3.permissions import IsOwnerOrReadOnly

class ProfileList(APIView):
    """
    List all profiles
    No Create view (post method), as profile creation handled by django signals
    """
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(
            profiles, many = True, context={'request':request})
        return Response(serializer.data)

class ProfileDetail(APIView):
    '''auto render a form'''
    serializer_class = ProfileSerializer
    ''' Set the permission_classes attribute'''

    permission_classes = [IsOwnerOrReadOnly]

    ''' Check if profile exists '''
    def get_object(self, pk):
        try:
            profile = Profile.objects.get(pk=pk)
            '''check object permissions line'''
            self.check_object_permissions(self.request, profile)
            return profile
        except Profile.DoesNotExist:
            raise Http404
    
    '''
    Get profile details
    '''
    def get(self,request,pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(
            profile, context={'request':request})
        return Response(serializer.data)
    
    '''
    Edit profile details
    '''
    def put(self,request,pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(
            profile, data= request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)