# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """

    return dict(message=T('Welcome to web2py!'))


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

def inserir_notas():
    nota = SQLFORM(Notas)
    if nota.process().accepted:
        session.flash = "Nota enviada com sucesso!"
        redirect(URL('index'))
    elif nota.errors:
        response.flash = "Erros no formulario!"
    else:
        response.flash = "Prencha o formulario!"
    return dict(nota=nota)

def ver_notas():
    id_notas = request.args(0, cast=int)
    notas = db(Notas.id == id_notas).select()
    return dict(notas=notas)

def atualizar_notas():
    id_notas = request.args(0 , cast=int)
    form = SQLFORM(Notas, id_notas , showid=False)
    if form.process().accepted:
        session.flash = "Nota atualizada com sucesso!"
        redirect(URL('ver_notas' , args=[id_notas]))
    elif form.errors:
        response.flash = "Erros no formulario!"
    else:
        response.flash = "Prencha o formulario!"
    return dict(form=form)

def apagar_notas():
    id_notas = request.args(0 ,cast=int)
    db(Notas.id == id_notas).delete()
    session.flash = "Nota apagada!"
    redirect(URL('ver_notas'))


def nova_mensagem():
    form = SQLFORM(Forum)
    if form.process().accepted:
        session.flash = "Mensagem enviada com sucesso!"
        redirect(URL('index'))
    elif form.errors:
        response.flash = "Erros no formulario!"
    else:
        response.flash = "Prencha o formulario!"
    return dict(formulario=form)

def ver_mensagem():
    id_mensagem = request.args(0 , cast=int)
    mensagem = db(Forum.id == id_mensagem).select(),first()
    return dict(mensagem=mensagem)

def forum():
    mensagens = db(Forum.id > 0).select()
    return dict(mensagens=mensagens)

def atualizar_mensagem():
    id_mensagem = request.args(0 , cast=int)
    form = SQLFORM(Forum, id_mensagem , showid=False)
    if form.process().accepted:
        session.flash = "Mensagem enviada com sucesso!"
        redirect(URL('ver_mensagem' , args[id_mensagem]))
    elif form.errors:
        response.flash = "Erros no formulario!"
    else:
        response.flash = "Prencha o formulario!"
    return dict(form=form)

def apagar_mensagem():
    id_mensagem = request.args(0 , cast=int)
    db(Forum.id == id_mensagem).delete()
    session.flash = "Mensagem apagada"
    redirect(URL('Forum'))

def novo_arquivo():
    form = crud.create(Biblioteca)
    return dict(form=form)

def editar_arquivo():
    id_arquivo = request.args(0 , cast=int)
    form = crud.update(Biblioteca, id_arquivo)
    return dict(form=form)

def exibir_arquivos():
    grid = SQLFORM.grid(Biblioteca)
    return dict(grid=grid)

def contato():
    form = SQLFORM.factory(
    Field('nome' , requires=IS_NOT_EMPTY()),
    Field('email' , requires=IS_EMAIL()),
    Field('mensagem' , 'text' , requires=IS_NOT_EMPTY())
    )
    if form.process().accepted:
        session.flash = "Mensagem Recebida"
        redirect(URL('index'))
    elif form.errors:
        response.flash = "Erros no formulario"
    else:
        response.flash = "Preencha o formulario"
    return dict(form=form)
