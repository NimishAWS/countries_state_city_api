from django.shortcuts import render
import json
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.utils.translation import gettext_lazy as _

# Create your views here.

class GetCountries(APIView):
    """
    Get country state and city list from json data file
    """

    def get(self, request):
        try:
            with open(
                os.path.join(settings.STATIC_DIRS, "countries.json")
            ) as json_file:
                data = json.load(json_file)
                country = request.GET.get("country", None)
                country_name = country.title()
                if country_name:
                    country = [
                        {"name": i["name"], "iso2": i["iso2"], "iso3": i["iso3"]}
                        for i in data
                        if country_name.lower() in i["name"].lower()
                    ]
                    return Response(
                        {
                            "status_code": status.HTTP_200_OK,
                            "message": _("Country"),
                            "country": country,
                        },
                        status=status.HTTP_200_OK,
                    )
                return Response(
                    {
                        "status_code": status.HTTP_200_OK,
                        "message": _("Country list"),
                        "country_list": [
                            {"name": i["name"], "iso2": i["iso2"], "iso3": i["iso3"]}
                            for i in data
                        ],
                    },
                    status=status.HTTP_200_OK,
                )
        except:
            return Response(
                {
                    "status_code": status.HTTP_400_BAD_REQUEST,
                    "message": _("Country list does not exist"),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


class GetStates(APIView):
    """
    Get country state and city list from json data file
    """

    def get(self, request):
        try:
            with open(os.path.join(settings.STATIC_DIRS, "states.json")) as json_file:
                data = json.load(json_file)
                country = request.GET.get("country_code", None)
                country_code = country.upper()
                search = request.GET.get("search", None)

                # get all the states of the country code from json file else return all the states
                if country_code and search:
                    # states = [i for i in data if i['country_code'] == country_code]
                    states = [
                        {
                            "name": i["name"],
                            "country_name": i["country_name"],
                            "state_code": i["state_code"],
                        }
                        for i in data
                        if i["country_code"] == country_code
                        and search.lower() in i["name"].lower()
                    ]

                    return Response(
                        {
                            "status_code": status.HTTP_200_OK,
                            "message": _("States List"),
                            "states": states,
                        },
                        status=status.HTTP_200_OK,
                    )
                else:
                    return Response(
                        {
                            "status_code": status.HTTP_200_OK,
                            "message": _("All States for Country"),
                            "states": data,
                        },
                        status=status.HTTP_200_OK,
                    )
        except:
            return Response(
                {
                    "status_code": status.HTTP_400_BAD_REQUEST,
                    "message": _("State list does not exist"),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


class GetCities(APIView):
    """
    Get country state and city list from json data file
    """

    def get(self, request):
        try:
            with open(os.path.join(settings.STATIC_DIRS, "cities.json")) as json_file:
                data = json.load(json_file)
                country = request.GET.get("country_code", None)
                country_code = country.upper()
                state = request.GET.get("states_code", None)
                state_code = state.upper()
                search = request.GET.get("search", None)

                if state_code and country_code and search:
                    # states = [i for i in data if i['country_code'] == country_code]
                    states = [
                        {
                            "name": i["name"],
                            "country_name": i["country_name"],
                            "state_code": i["state_code"],
                        }
                        for i in data
                        if i["state_code"] == state_code
                        and i["country_code"] == country_code
                        and search.lower() in i["name"].lower()
                    ]
                    return Response(
                        {
                            "status_code": status.HTTP_200_OK,
                            "message": _("Cities List"),
                            "states": states,
                        },
                        status=status.HTTP_200_OK,
                    )
                else:
                    return Response(
                        {
                            "status_code": status.HTTP_200_OK,
                            "message": _("All Cities for States"),
                            "states": data,
                        },
                        status=status.HTTP_200_OK,
                    )
        except:
            return Response(
                {
                    "status_code": status.HTTP_400_BAD_REQUEST,
                    "message": _("City list does not exist"),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

