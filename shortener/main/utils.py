import random,string

def code_generator(chars=string.ascii_letters+string.digits):
    x=''
    for i in range(8):
        x=x+(random.choice(chars))
    return 'http://'+x

def create_shortcode(instance):
    new_code=code_generator()
    Klass=instance.__class__
    qs_exists=Klass.objects.filter(shortcode=new_code).exists()
    if qs_exists:
        return create_shortcode(instance)
    else:
        return new_code
