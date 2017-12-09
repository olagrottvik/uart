"""! @package utils


"""
import re
import json
import os

spacesInTab = 2


def indentString(string, tabs=1, breakLine=False):
    """! @brief adds indent spaces to all lines in string
    """

    indent = spacesInTab * tabs * (" ")
    # Add indent to every line and recreate string
    string = [indent + line for line in re.split(r"\n", string)]
    string = "\n".join(string)

    # Remove last string if it only contains indent
    string = fixLastIndentOnlyLine(string, tabs)

    if breakLine:
        string += '\n'
    return string


def jsonParser(filename='module.json'):
    with open(filename) as json_data:
        d = json.load(json_data)
        return d


def jsonToString(filename='module.json'):
    with open(filename) as json_data:
        d = json_data.read()
        return d


def fixLastIndentOnlyLine(string, tabs):
    """! @brief Will edit the last line if it only contains indentation to an 
    empty string
    """
    stringList = re.split(r"\n", string)
    if stringList[-1] == (spacesInTab * tabs * (" ")):
        stringList[-1] = ''

    string = "\n".join(stringList)
    return string


def compareJSON(json1, json2, raiseError=False):
    """! @brief Will compare two JSON strings, and return False if they differ. An
    extra argument can be used to force the function to raise an error with the line
    the difference was observed.
    """
    for linenumber, (line1, line2) in enumerate(zip(json1.splitlines(),
                                                    json2.splitlines())):
        if (line1 != line2):
            if raiseError:
                raise Exception("JSON differs at line: " + str(linenumber))
            return False

    return True


def writeStringToFile(string, outputFile, outputDir):
    """! @brief Write string to file

    """

    # Create output directory if it does not exist
    os.makedirs(outputDir, 0o777, True)

    print('Writing string to ' + os.path.join(outputDir, outputFile))

    with open(os.path.join(outputDir, outputFile), 'w') as strfile:
        strfile.write(string)


def cont():
        try:
            input("Press enter to continue...")
        except SyntaxError:
            pass


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')


def add_line_breaks(string, min_length):
    """! @brief Adds line breaks on the next space after the minimum length of a line"""
    requirement = min_length
    replace = False
    positions = []
    for i, char in enumerate(string):
        if i > requirement:
            replace = True
        if replace and char == ' ':
            positions.append(i)
            requirement = i + min_length
            replace = False
    for rep in positions:
        string = string[:rep] + '\n' + string[rep + 1:]

    return string
