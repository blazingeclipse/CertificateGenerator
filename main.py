__author__ = 'jaime'

from xhtml2pdf import pisa             # import python module
from DefaultString import DefaultString
from Value import Value

from fnmatch import fnmatch



def replaceValues(sourceHTML, valueList):
    for value in valueList:
        tag = '%' + str(value.getName()) + '%'
        sourceHTML = sourceHTML.replace(tag,str(value.getValue()))
    return sourceHTML

def checkIfAllValuesAreFound(sourceHTML):
    if fnmatch(sourceHTML,'%*%') == -1:
        return True

    return False

# Utility function
def convertHtmlToPdf(sourceHtml, outputFilename):
    # open output file for writing (truncated binary)
    resultFile = open(outputFilename, "w+b")

    # convert HTML to PDF
    pisaStatus = pisa.CreatePDF(
            sourceHtml,                # the HTML to convert
            dest=resultFile)           # file handle to recieve result

    # close output file
    resultFile.close()                 # close output file

    # return True on success and False on errors
    return pisaStatus.err

# Main program
if __name__=="__main__":
    pisa.showLogging()
    # Define your data
    sourceHtml = "<html><body><p>Name: %name% <br/>" \
                 "              Age:  %age% <br/><p></body></html>"
    outputFilename = "test.pdf"
    valueList = []
    valueList.append(Value('name',DefaultString(["John doe","Jane doe","James bond"])))
    sourceHtml = replaceValues(sourceHtml, valueList)
    print sourceHtml
    if(checkIfAllValuesAreFound(sourceHtml) == False):
        print 'Not all variables were removed from the template!'
    convertHtmlToPdf(sourceHtml, outputFilename)