"""
Project api
"""
from utils import get
from aou_api import api
from http import HTTPStatus
from user.models import CustomUser
from project.models import Project

@api.get("/proj")
def get_project(request, id: str):
    return get(Project, id)

@api.post("/proj/create")
def create_project(request, uid: str):
    try:
        user = CustomUser.objects.get(id=uid)
    except Project.DoesNotExist:
        return {"error": "User does not exist", "status": HTTPStatus.FORBIDDEN}
    
    project = Project.objects.create(owner=user, title="New Project")

    project.save()
    return project.json()

@api.post("/proj/edit")
def edit_project(request, pid: str, title: str = None):
    try:
        project = Project.objects.get(id=pid)

        if title is not None:
            project.title = title

        project.save()
    except Project.DoesNotExist:
        return {"error": "Project does not exist", "status": HTTPStatus.FORBIDDEN}

    return HTTPStatus.OK

@api.delete("/proj/delete")
def delete_project(request, id: str):
    try:
        project = Project.objects.get(id=id)
        project.delete()
    except Project.DoesNotExist:
        return {"error": "Project does not exist", "status": HTTPStatus.FORBIDDEN}

    return HTTPStatus.OK