import os

def check(n: str):
    if n == 'Minsu':
        print("Hi {}! Welcome to admins97's Homepage!".format(n))
        return True
    else:
        return False
    
def test_check():
    assert check(str(os.environ["VISIT_NUM"])) == True
