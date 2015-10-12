__author__ = 'janderson'
# -*- coding utf-8 -*-

Notas.aluno.requires = IS_IN_DB(db, 'auth_user.id' , '%(first_name)s %(last_name)s' , zero = 'Selecione um')
Notas.professor.requires = IS_IN_DB(db, 'auth_user.id' , '%(first_name)s %(last_name)s' , zero = 'Selecione um')

Biblioteca.arquivo.requires = IS_UPLOAD_FILENAME(extension='pdf')
Biblioteca.professor.requires = IS_IN_DB(db, 'auth_user.id' , '%(first_name)s %(last_name)s' , zero = 'Selecione um')

Forum.mensagem.requires = IS_NOT_EMPTY(error_message='Não pode estar vazio!')
Forum.titulo.requires = IS_NOT_EMPTY(error_message="Titulo não pode estar vazio!")

Comentarios.mensagem.requires = IS_NOT_EMPTY()
Comentarios.postagem.requires = IS_IN_DB(db, 'forum.id' , '%(mensagem)s' , zero='Selecione um:')
Comentarios.titulo.requires = IS_NOT_EMPTY(error_message="Titulo não pode estar vazio!")

IS_DATETIME(format='%d/%m/%Y')





