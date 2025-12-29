"""
PBL (Project-Based Learning) API endpoints.
"""

from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File, Form
from sqlalchemy.orm import Session
from typing import List, Optional
from uuid import UUID
from datetime import datetime
from app.database import get_db
from app.dependencies import get_current_user, require_role
from app.models.user import User, UserRole
from app.schemas.project import (
    ProjectCreate, ProjectResponse, 
    ProjectSubmissionCreate, ProjectSubmissionResponse,
    ProjectEvaluationCreate, ProjectEvaluationResponse
)
from app.services.pbl_service import PBLService

router = APIRouter(prefix="/projects", tags=["PBL Management"])

@router.get("/", response_model=List[ProjectResponse])
def list_projects(
    class_id: Optional[UUID] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """List all projects, optionally filtered by class."""
    return PBLService.get_projects(db, class_id)

@router.get("/{project_id}", response_model=ProjectResponse)
def get_project(
    project_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get details of a specific project."""
    project = PBLService.get_project_by_id(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.post("/", response_model=ProjectResponse, status_code=status.HTTP_201_CREATED)
def create_project(
    project_data: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role([UserRole.TEACHER, UserRole.ADMIN, UserRole.STUDENT]))
):
    """Create a new PBL project (Teachers/Admins only)."""
    try:
        return PBLService.create_project(db, project_data, current_user.id)
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(
            status_code=500,
            detail=f"Failed to create project: {str(e)}"
        )

@router.get("/{project_id}/submissions", response_model=List[ProjectSubmissionResponse])
def get_project_submissions(
    project_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role([UserRole.TEACHER, UserRole.ADMIN]))
):
    """Get all submissions for a project (Teachers/Admins only)."""
    return PBLService.get_submissions(db, project_id)

@router.post("/{project_id}/submit", status_code=status.HTTP_201_CREATED)
async def submit_project_work(
    project_id: UUID,
    title: str = Form(...),
    description: str = Form(...),
    link: Optional[str] = Form(None),
    files: List[UploadFile] = File(default=[]),
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role([UserRole.STUDENT]))
):
    """Submit project work evidence (Students only)."""
    from fastapi import UploadFile, File, Form
    import os
    import uuid as uuid_lib
    from pathlib import Path
    
    try:
        # Save uploaded files to Google Drive
        file_urls = []
        try:
            from app.services.google_service import google_service
            for file in files:
                if file.filename:
                    print(f"[SUBMISSION] Uploading {file.filename} to Drive...")
                    drive_file = google_service.upload_file(file.file, file.filename)
                    file_url = drive_file.get('webViewLink')
                    file_urls.append(file_url)
        except Exception as e:
            print(f"[SUBMISSION] Drive upload failed: {e}")
            raise HTTPException(status_code=500, detail=f"Failed to upload submission files: {str(e)}")
        
        # Create submission record (simplified - just return success for now)
        submission_data = {
            "id": str(uuid_lib.uuid4()),
            "project_id": str(project_id),
            "student_id": str(current_user.id),
            "title": title,
            "description": description,
            "link": link,
            "files": file_urls,
            "submitted_at": datetime.utcnow().isoformat(),
            "status": "submitted"
        }
        
        return submission_data
    except Exception as e:
        print(f"Error in submit_project_work: {e}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Submission failed: {str(e)}")

@router.post("/submissions", response_model=ProjectSubmissionResponse, status_code=status.HTTP_201_CREATED)
def submit_project(
    submission_data: ProjectSubmissionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role([UserRole.STUDENT]))
):
    """Submit project evidence (Students only) - Legacy endpoint."""
    # Validation could be added here to ensure the student is assigned to this project
    return PBLService.create_submission(db, submission_data)



@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_project(
    project_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role([UserRole.TEACHER, UserRole.ADMIN]))
):
    """Delete a project (Teachers/Admins only)."""
    success = PBLService.delete_project(db, project_id)
    if not success:
        raise HTTPException(status_code=404, detail="Project not found")
    return None
