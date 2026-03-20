import uuid
from fastapi import APIRouter, HTTPException, status
from app.schemas import IssueCreate, IssueUpdate, IssueOutput, IssueStatus
from app.storage import load_data, save_data

# we export the router to be included in main.py
router = APIRouter(prefix="/api/v1/issues", tags=["issues"])

@router.get("/", response_model=list[IssueOutput])
async def get_issues():
    """Retrieve all issues."""
    issues = load_data()
    return issues

@router.post("/", response_model=IssueOutput, status_code=status.HTTP_201_CREATED)
def create_issue(payload: IssueCreate):
    """Create a new issue."""
    issues = load_data()
    new_issue = {
        "id": str(uuid.uuid4()),
        "title": payload.title,
        "description": payload.description,
        "priority": payload.priority,
        "status": IssueStatus.open,
    }

    issues.append(new_issue)
    save_data(issues)
    return new_issue # return dict, FastAPI will convert to IssueOutput

@router.get("/{issue_id}", response_model=IssueOutput)
def get_issue(issue_id: str):
    """Retrieve a specific issue by ID."""
    issues = load_data()
    for issue in issues:
        if issue["id"] == issue_id:
            return issue
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found🚩")

@router.put("/{issue_id}", response_model=IssueOutput)
def update_issue(issue_id: str, payload: IssueUpdate):
    """Update an existing issue."""
    issues = load_data() # return list of dicts
    for index, issue in enumerate(issues):
        if issue["id"] == issue_id:
            updated_issue = issue.copy() # create a copy to modify
            if payload.title is not None:
                updated_issue["title"] = payload.title
            if payload.description is not None:
                updated_issue["description"] = payload.description
            if payload.priority is not None:
                updated_issue["priority"] = payload.priority
            if payload.status is not None:
                updated_issue["status"] = payload.status

            issues[index] = updated_issue # update the list with the updated issue
            save_data(issues)
            return updated_issue
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found🚩")




