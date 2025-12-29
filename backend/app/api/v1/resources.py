"""
Resource API endpoints.
Handles resource management and student resource requests.
"""

from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File, Form
from sqlalchemy.orm import Session
from typing import List, Optional
from uuid import UUID

from app.database import get_db
from app.dependencies import get_current_user, require_role
from app.models.user import User, UserRole
from app.schemas.resource import (
    ResourceCreate, ResourceUpdate, ResourceResponse,
    ResourceRequestCreate, ResourceRequestAction, ResourceRequestResponse,
    ResourceType
)
from app.services.resource_service import ResourceService

router = APIRouter(prefix="/resources", tags=["Resources"])


# Resource Request Endpoints
# IMPORTANT: These must be defined BEFORE the /{resource_id} endpoints
# to avoid path parameter conflicts (where "requests" is parsed as a UUID)

@router.post("/requests", response_model=ResourceRequestResponse, status_code=status.HTTP_201_CREATED)
def create_resource_request(
    request_data: ResourceRequestCreate,
    current_user: User = Depends(require_role(UserRole.STUDENT)),
    db: Session = Depends(get_db)
):
    print(f"DEBUG: create_resource_request called. User: {current_user.id}, Data: {request_data}")
    """
    Create a resource request (Student only).
    
    - **title**: Requested resource title
    - **description**: Optional description
    - **type**: Resource type
    - **class_id**: Class UUID
    """

    request = ResourceService.create_request(db, request_data, current_user)
    return request


@router.get("/requests", response_model=List[ResourceRequestResponse])
def get_resource_requests(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Get resource requests.
    
    - Students see only their own requests
    - Teachers see all requests for their classes
    """
    requests = ResourceService.get_requests(db, current_user)
    return requests


@router.put("/requests/{request_id}/approve", response_model=ResourceRequestResponse)
def approve_resource_request(
    request_id: UUID,
    action_data: ResourceRequestAction,
    current_user: User = Depends(require_role(UserRole.TEACHER)),
    db: Session = Depends(get_db)
):
    """
    Approve a resource request and create the resource (Teacher only).
    
    - **teacher_response**: Optional feedback message
    """
    request = ResourceService.approve_request(db, request_id, current_user, action_data)
    return request


@router.put("/requests/{request_id}/reject", response_model=ResourceRequestResponse)
def reject_resource_request(
    request_id: UUID,
    action_data: ResourceRequestAction,
    current_user: User = Depends(require_role(UserRole.TEACHER)),
    db: Session = Depends(get_db)
):
    """
    Reject a resource request (Teacher only).
    
    - **teacher_response**: Optional feedback message
    """
    request = ResourceService.reject_request(db, request_id, current_user, action_data)
    return request


# Resource Endpoints

@router.get("", response_model=List[ResourceResponse])
def get_resources(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Get all resources accessible to the current user.
    
    - Teachers see resources from classes they teach
    - Students see resources from classes they're enrolled in
    """
    resources = ResourceService.get_resources(db, current_user)
    return resources


@router.post("", response_model=ResourceResponse, status_code=status.HTTP_201_CREATED)
async def create_resource(
    title: str = Form(...),
    description: Optional[str] = Form(None),
    type: ResourceType = Form(...),
    class_id: UUID = Form(...),
    url: Optional[str] = Form(None),
    content: Optional[str] = Form(None),
    file: Optional[UploadFile] = File(None),
    current_user: User = Depends(require_role(UserRole.TEACHER)),
    db: Session = Depends(get_db)
):
    """
    Create a new resource (Teacher only).
    
    - **title**: Resource title
    - **description**: Optional description
    - **type**: Resource type (pdf, video, link, notes)
    - **class_id**: Class UUID
    - **url**: URL for video/link types
    - **content**: Text content for notes type
    - **file**: File upload for PDF type
    """
    resource_data = ResourceCreate(
        title=title,
        description=description,
        type=type,
        class_id=class_id,
        url=url,
        content=content
    )
    
    resource = ResourceService.create_resource(db, resource_data, current_user, file)
    return resource


@router.get("/{resource_id}", response_model=ResourceResponse)
def get_resource(
    resource_id: UUID,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Get a single resource by ID.
    
    User must have access to the resource's class.
    """
    resource = ResourceService.get_resource(db, resource_id, current_user)
    return resource


@router.put("/{resource_id}", response_model=ResourceResponse)
def update_resource(
    resource_id: UUID,
    resource_data: ResourceUpdate,
    current_user: User = Depends(require_role(UserRole.TEACHER)),
    db: Session = Depends(get_db)
):
    """
    Update a resource (Teacher only).
    
    - **teacher_response**: Optional feedback message
    """
    resource = ResourceService.update_resource(db, resource_id, resource_data, current_user)
    return resource






@router.delete("/{resource_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_resource(
    resource_id: UUID,
    current_user: User = Depends(require_role(UserRole.TEACHER)),
    db: Session = Depends(get_db)
):
    """
    Delete a resource (Teacher only).
    
    - **teacher_response**: Optional feedback message
    """
    ResourceService.delete_resource(db, resource_id, current_user)
    return None

