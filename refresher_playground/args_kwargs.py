def addition_simplified(*args):
    return sum(args)

addition_simplified(3, 5, 7, 12, 14, 55)


def what_are_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

what_are_kwargs(1, 2, 3, 4, name='Jose', location='UK')



def defined_keyword_args(arg1, name, location):
    print(name)
    print(location)

defined_keyword_args(56, location='UK', name='Jose')
# general args come first, defined keyword args come after, they can be in
# any order as they have a key assigned