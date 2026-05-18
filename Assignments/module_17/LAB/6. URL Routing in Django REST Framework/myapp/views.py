from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from myapp.models import Doctor
from myapp.serializers import DoctorSerializer


class DoctorAPIView(APIView):

    # GET ALL DOCTORS
    def get(self, request, id=None):

        if id is not None:

            doctor = Doctor.objects.get(id=id)

            serializer = DoctorSerializer(doctor)

            return Response(serializer.data)

        doctors = Doctor.objects.all()

        serializer = DoctorSerializer(doctors, many=True)

        return Response(serializer.data)

    # INSERT DOCTOR
    def post(self, request):

        serializer = DoctorSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(
                {
                    "message": "Doctor Added Successfully",
                    "data": serializer.data
                },
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors)

    # UPDATE DOCTOR
    def put(self, request, id):

        doctor = Doctor.objects.get(id=id)

        serializer = DoctorSerializer(
            doctor,
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                {
                    "message": "Doctor Updated Successfully",
                    "data": serializer.data
                }
            )

        return Response(serializer.errors)

    # DELETE DOCTOR
    def delete(self, request, id):

        doctor = Doctor.objects.get(id=id)

        doctor.delete()

        return Response(
            {
                "message": "Doctor Deleted Successfully"
            }
        )