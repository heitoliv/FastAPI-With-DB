# app/routers/team.py
from controller.generic import create_crud_router
from model.models import Endereco
from model.dto import EnderecoCreate, EnderecoRead, EnderecoUpdate

router = create_crud_router(
    model=Endereco,
    create_schema=EnderecoCreate,
    update_schema=EnderecoUpdate,
    read_schema=EnderecoRead,
    prefix="/teams",
    tags=["teams"],
)