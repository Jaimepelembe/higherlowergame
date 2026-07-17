def readFile(fileName):
    """ Read a whole file"""

    try:
        file=open(fileName,"r")
        content=file.read()

    except FileNotFoundError:
        print("Error: The file was not founded.")
        #Create the file
        with open(fileName, "w") as fileText:
            fileText.write("0")
            return "0"
    except PermissionError:
        print("Error: Permission denied to read this file.")
    except IsADirectoryError:
        print("Error: The specified path is a folder, not a file.")
            
    except Exception as ex:
        print(f"Error: {ex}")
    else:
        if content=="":
            content="0"
        return content



def writeFile(fileName,value):
    """Write in a file"""

    try:
        file=open(fileName,"w")
        file.write(value)

    except FileNotFoundError:
        print("Error: The file was not founded.")
        #Create the file
        with open(fileName, "w") as fileText:
            fileText.write("")
    except PermissionError:
        print("Error: Permission denied to read this file.")
    except IsADirectoryError:
        print("Error: The specified path is a folder, not a file.")
            
    except Exception as ex:
        print(ex)
    else:
        print("New score saved sucessfuly.")

    finally:
        if 'file' in locals() or not file.closed(): # locals() Verify the locals variables
            file.close()

