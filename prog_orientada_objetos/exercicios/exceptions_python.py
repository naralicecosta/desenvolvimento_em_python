# Para criar uma execption, voce so precisa herdar de alguma exeção da linguagem

class MeuError(Exception):
    ...

class OutroError(Exception):
    ...
    
def levantar():
    exception_ = MeuError('a', 'b', 'c')
    exception_.add_note('olha a nota 1') #notas das exceptions
    exception_.add_note('você errou isso')
    raise exception_

try:
    levantar()
    
except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = OutroError('Vou lançar de novo')
    exception_.add_note('Mais uma nova')
    exception_.add_notes__ += error.__notes__.copy()
    raise exception_ from error
    
    