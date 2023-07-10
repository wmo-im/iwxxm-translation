#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Utility for verifying that examples in the LATEST_VERSION directory validate against the appropriate version of the IWXXM
schemas and schematrons.

The main() is intended for use in a Continuous Integration process and as such returns status codes.  Non-zero values
indicate validation failures.  The main() function reads the sub-directories under the LATEST_VERSION directory to get the
IWXXM instances to validate.

Confirmed to run in Python 3.11
"""

import sys, os

def main():
    cwd = os.getcwd()
    if not os.path.isfile( os.path.join( cwd, 'README.md' ) ):
        print("This script must be run from the root directory of the repository, normally iwxxm-translation, which contains README.md")
        sys.exit(1)

    # get path to examples and IWXXM version
    with open('LATEST_EXAMPLE') as fhandle:
        LEPath = fhandle.read().strip()
        fhandle.close()

    FullLatestExamplePath = os.path.join(cwd, LEPath)

    with open(os.path.join(FullLatestExamplePath, 'IWXXM_VERSION')) as fhandle:
        XSDVersion = fhandle.read().strip()
        fhandle.close()

    returnCode = 0
    for f in os.scandir(FullLatestExamplePath):
        if f.is_dir():
            result = validate_dir(cwd, f, XSDVersion)
            if result > 0:
                print("========= Validation FAILED on %s =========" % f)
                returnCode = result
            else:
                print("========= Validation SUCCESSFUL on %s =========" % f)
            returnCode = returnCode | result

    if returnCode != 0:
        sys.exit( returnCode )

def validate_dir(rdir, dir, ver):
    fdir = os.path.join(rdir, dir)
    FullCatalogPath = os.path.join(rdir, 'catalog.xml')

    print('Validating %s against IWXXM Schema and Schematron' % fdir)
    validationResult = os.system( 'bin/crux-1.3-all.jar -c %s -s externalSchema/schemas.wmo.int/iwxxm/%s/rule/iwxxm.sch %s/*.xml' % (FullCatalogPath, ver, fdir) )
    #validationResult = os.system( 'bin/crux-1.3-all.jar -c %s %s/*.xml' % (FullCatalogPath, fdir) ) 
    if validationResult > 0:
        print('FAILED validation.  Continuing...')
    else:
        print('SUCCESSFUL validation')

    # this can return status codes of 256, which is an undefined value sometimes interpreted as 0.  Force it to a valid value
    if validationResult != 0:
        validationResult = 1
    return validationResult

if __name__ == '__main__':
    main()
