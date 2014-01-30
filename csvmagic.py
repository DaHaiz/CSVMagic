from DH.csv import Csv

# shell controlling options
prompt = "CSVMAGIC> "
errorPrefix = "Error! "
exitShell = False

#init the csv manager
csvManager = Csv()


def print_error(error):
    print(errorPrefix, error)


def quit_cmd(*args):
    return True


def help_cmd(*args):
    print('this will be the help')


def load_file_cmd(file_name, separator=';'):

    print("open file '{}'".format(file_name))

    result = csvManager.load_file(file_name, separator)
    if result:
        print('file loaded')
    else:
        print('loading failed')


def summarize_cmd(*args):
    """ print summary of loaded files """

    print('summary of current csv configuration:')
    print()

    print(csvManager)

def preview_cmd(*args):

    print(csvManager.preview(5))

cmds = {
    'q': quit_cmd,
    'h': help_cmd,
    'l': load_file_cmd,
    's': summarize_cmd,
    'p': preview_cmd
}

# start the shell
print("Welcome to CSVMagic")
print()
while not exitShell:
    command = input(prompt)
    cmdFirstChar = command[0].lower()

    args = command.split(' ')

    if cmdFirstChar in cmds:
        exitShell = cmds[cmdFirstChar](*args[1:])
    else:
        cmds['h']()
