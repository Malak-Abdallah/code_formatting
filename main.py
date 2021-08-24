# pre-commit hook : run different hooks to your code and check the code format
# if the hook passed we can commit the code, else we have to fix the code and recheck

# git init to the code we want to pre-commit
# then pre-commit install
# create .pre-commit-config.yaml file to add the hooks we want to check

# ----------------------------------------
# naming conventions:


def multiply_by_two(x):  # recommended
    return x * 2


# class name must start with capital letters
class Formatting:
    # choose clear names for variables or functions
    # variables and function must be small letters  and use underscore if more than one word is needed
    x = "John Smith"  # Not recommended
    name = "John Smith"  # recommended

    def db(self, x):  # Not recommended
        return x * 2

    #  CONSTANTS must be in capital letters
    NAME = "malk"

    # -----------------------------------
    # Linters are programs that analyze code and flag errors, then provide suggestion on how to fix the error
    # ex: flake8
    # there are autoformatters as black , than can be run in the terminal
