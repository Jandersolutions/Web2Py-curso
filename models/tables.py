# -*- coding:utf-8 -*-

from datetime import datetime

Notas = db.define_table('notas',
    Field('nota' , 'float' , default=0  ,label="Nota"),
    Field('aluno' , 'reference auth_user' , label='Aluno'),
    Field('professor' , 'reference auth_user' , ondelete='SET NULL',label="Professor")
)
Biblioteca = db.define_table('biblioteca',
      Field('arquivo' , 'upload' , notnull=True , label="Arquivo"),
      Field('professor' , 'reference auth_user' , ondelete='SET NULL', notnull=True , label="Professor")
)
Forum = db.define_table('forum',
      Field('titulo' , 'string' , notnull=True , label="Titulo" ),
      Field('mensagem' , 'text' , notnull=True , label="Mensagem" ),
      auth.signature
)
Comentarios = db.define_table('comentarios',
      Field('titulo' , 'string' , notnull=True , label="Titulo" ),
      Field('mensagem' , 'text' , notnull=True , label="Mensagem"),
      Field('postagem' , 'reference forum'  , label="Postagem"),
      auth.signature
)