# app/routers/pessoa.py
from fastapi import HTTPException
from sqlmodel import Session, select
from controller.generic import create_crud_router, Hooks
from model.models import Pessoa
from model.dto import PessoaCreate, PessoaUpdate, PessoaReadWithEnderecos, PessoaRead

class PessoaHooks(Hooks[Pessoa, PessoaCreate, PessoaUpdate]):
    def pre_create(self, payload: PessoaCreate, session: Session) -> None:
        """Verifica se o e-mail já existe antes de criar."""
        statement = select(Pessoa).where(Pessoa.email == payload.email)
        if session.exec(statement).first():
            raise HTTPException(status_code=409, detail="E-mail já cadastrado.")

    def pre_update(self, payload: PessoaUpdate, obj: Pessoa, session: Session) -> None:
        """Verifica se o novo e-mail (se fornecido) já pertence a outra pessoa."""
        if payload.email is not None and payload.email != obj.email:
            statement = select(Pessoa).where(Pessoa.email == payload.email)
            existing_user = session.exec(statement).first()
            if existing_user and existing_user.id != obj.id:
                raise HTTPException(status_code=409, detail="E-mail já cadastrado para outro usuário.")

# Criamos o router CRUD genérico para Pessoa
# Note que para a leitura de um objeto, usamos o schema que inclui os endereços
router = create_crud_router(
    model=Pessoa,
    create_schema=PessoaCreate,
    update_schema=PessoaUpdate,
    read_schema=PessoaReadWithEnderecos, # <- Retorna pessoa com endereços no GET /pessoas/{id}
    prefix="/pessoas",
    tags=["Pessoas"],
    hooks=PessoaHooks(),
)