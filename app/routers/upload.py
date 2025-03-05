import chardet

from typing import List
from fastapi import APIRouter, UploadFile, File, Request
from fastapi.templating import Jinja2Templates

from app.services.tfidf_calculator import compute_tfidf

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.post("/upload")
async def upload_file(request: Request, files: List[UploadFile] = File(...)):
    if not files:
        return templates.TemplateResponse("index.html", {"request": request})

    documents = []
    for file in files:
        if file.content_type != "text/plain":
            return templates.TemplateResponse("index.html", {"request": request})

        content = await file.read()
        detected_encoding = chardet.detect(content)["encoding"]

        try:
            text = content.decode(detected_encoding or "utf-8")
            documents.append(text)
        except (UnicodeDecodeError, TypeError):
            return templates.TemplateResponse("index.html", {"request": request})

    if not documents:
        return templates.TemplateResponse("index.html", {"request": request})

    result = compute_tfidf(documents=documents)
    return templates.TemplateResponse("index.html", {"request": request, "tfidf": result})
