"""
Este arquivo define os Data Transfer Objects (DTOs) ou "schemas" para a API,
utilizando SQLModel.

Esses modelos são usados para validar os dados de entrada (payloads de requisições)
e para formatar os dados de saída (respostas da API). Eles são separados
dos modelos de banco de dados para criar um contrato de API claro e seguro.
"""

from typing import Optional, List
from sqlmodel import SQLModel

class PessoaBase(SQLModel):
    """Schema base com os campos comuns de Pessoa."""
    nome: str
    idade: Optional[int] = None
    email: str

class PessoaCreate(PessoaBase):
    """
    Schema usado para criar uma nova Pessoa via API.
    Herda todos os campos de PessoaBase. O cliente não deve enviar o ID.
    """
    pass

class PessoaRead(PessoaBase):
    """
    Schema usado para retornar os dados de uma Pessoa na resposta da API.
    Inclui o ID, que é gerado pelo banco de dados.
    """
    id: int

class PessoaUpdate(SQLModel):
    nome: Optional[str] = None
    idade: Optional[int] = None
    email: Optional[str] = None
    
class EnderecoBase(SQLModel):
    """Schema base com os campos comuns de Endereco."""
    logradouro: str
    numero: str
    cidade: str
    bairro: str
    uf: str

class EnderecoCreate(EnderecoBase):
    """
    Schema usado para criar um novo Endereco via API.
    O ID da pessoa será obtido pela URL, não pelo corpo da requisição.
    """
    pass

class EnderecoRead(EnderecoBase):
    """
    Schema usado para retornar os dados de um Endereco na resposta da API.
    Inclui o ID do endereço e o ID da pessoa a quem ele pertence.
    """
    id: int
    pessoa_id: int


class PessoaReadWithEnderecos(PessoaRead):
    """
    Schema principal para a leitura de uma Pessoa, atendendo ao requisito
    de retornar a pessoa junto com sua lista de endereços.
    """
    enderecos: List[EnderecoRead] = []