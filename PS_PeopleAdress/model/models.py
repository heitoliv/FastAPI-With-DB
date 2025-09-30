from typing import Optional,List
from sqlmodel import SQLModel, Field, Relationship

class PessoaBase(SQLModel):
    nome : str = Field(index=True, min_length=3, max_length=200)
    idade : Optional[int] = Field(default=None, ge=0, le=200)
    email : str = Field(unique=True, index=True, max_length=100)

class Pessoa(PessoaBase, table=True):
    id : Optional[int] = Field(default=None, primary_key=True, index=True)
    enderecos: List["Endereco"] = Relationship(
        back_populates="pessoa",
        sa_relationship_kwargs={"cascade": "all, delete-orphan"} # Deleta os endereços se a pessoa for deletada
    )

class EnderecoBase(SQLModel):
    logradouro : str = Field(index=True, min_length=3, max_length=150)
    numero : str = Field(default=None, index=True)
    uf : str = Field(index=True, default=None, max_length=2)
    cidade : str = Field(index=True, default=None, max_length=50)
    bairro : str = Field(index=True, default=None, max_length=50)


class Endereco(EnderecoBase,table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    pessoa_id: Optional[int] = Field(default=None, foreign_key="pessoa.id")
    pessoa: Optional["Pessoa"] = Relationship(back_populates="enderecos")
