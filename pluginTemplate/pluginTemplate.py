
## NOTICE!!! Rename 'pluginTemplate' to 'plugin' or any other supported names.
## NOTICE!!! Supported Names can be found here: 'https://github.com/Cracko298/iszlib#example-plugin'

def Credits():
    ## Credits for Creator + Version Number (Example v3.2.2)
    global version, developer
    version = "v1.0.0"
    developer = "Example Creator"
    return version, developer
Credits()

def MainApp():
    ## Your Code Here.
    print("This is an Example Plugin.")

    