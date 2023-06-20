def Backup():
    from os import getenv, getcwd, path, makedirs
    from datetime import date, datetime

    appdata = getenv('LOCALAPPDATA')
    directory = getcwd()
    now_date = date.today()
    get_var = datetime.now()
    now_time = get_var.strftime("%H:%M")
    backup_dir = path.join(directory,'_dat','MMplugins',f'{now_date} - {now_time}')

    isz_save_dir = path.join(appdata,'ISZ','Saved','SaveGames')

    print(f'Backup Files At: {backup_dir}')

def Inject():
    from os import getenv, getcwd, path, makedirs
    from datetime import date, time

    appdata = getenv('LOCALAPPDATA')
    directory = getcwd()
    now_date = date.today()

    isz_save_dir = path.join(appdata,'ISZ','Saved','SaveGames')

    print(f'Inject Files At: {isz_save_dir}')

def Credits():
    global developer, mod_menu, organization, version
    developer = "Toaster-YT"
    mod_menu = "Cracko298"
    organization = "ISZ-Hacker-Organization"
    version = "v1.0.1"

    return developer, mod_menu, organization, version

Credits()