from flask import request

def protect():
    ip_addr = request.remote_addr #este e o metodo ao nao se utilizar um proxy, caso utilize, voce devera pegar de outro modo
    return ip_addr