from faker import Faker


fake = Faker()


def make_name():
    name = fake.name()
    split_name = tuple(name.split())
    if len(split_name) == 2:
        return split_name
    else:
        make_name()


def make_profile():
    pgh = fake.text()
    return pgh


def generate_names(num_names=1000):
    '''
    Generate a list of first_name, last_name tuples for whichever
    range num_names is set to
    '''
    name_list = [make_name() for i in range(num_names)]
    return name_list


if __name__ == '__main__':
    #print(generate_names())
    print(make_profile())

