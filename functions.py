import os
import os.path
import re
import subprocess
import sys
import lib.config as config
import readchar
import terminaltables
from blessed import Terminal
from colorama import Fore, Back

cfg = config.cfg

from lib.log import logger

if cfg['term'] == "yes":
    tabletype = terminaltables.SingleTable
else:
    tabletype = terminaltables.AsciiTable

testmode = cfg['testmode']
dirName = cfg['system_vars']['dirName']
t = Terminal()
print(Back.BLACK, Fore.LIGHTGREEN_EX)
print(Fore.LIGHTGREEN_EX)
print(t.clear)
# set foreground text to green

# testmode = True

# from colorama import Fore, Back, Style

vidfiles = cfg['system_vars']['videofiles']

workdirs = []

def do_revert(parm1):
    proc = subprocess.Popen(["filebot", "-revert", parm1], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    do_return("Quitting...")


def do_return(text):
    print("Exiting: %s" % text)
    print()

    if cfg['location'] == "menu":
        input("Press any key...")
        menu_start()
    else:
        logger.info("Menu session ended.")
        quit()


# ------------------------------------

def work_multi(data, parm1):
    print(t.clear)

    title = "%s v%s" % (cfg['system_vars']['program_name'], cfg['system_vars']['program_ver'])
    print(t.center(title))

    print("Ambiguous TV show name... choose correct entry")
    print()
    counter = 1
    tabledata = []
    tabledata.append(["Option", "Variant"])

    for option in data['opts']:
        tabledata.append([counter, data['opts'][counter-1]])
        counter += 1

    table = tabletype(tabledata)
    print(table.table)

    print()
    max_count = counter - 1
    prompt = "Choose an option 1 through %i or \"Q\" to quit: " % max_count
    choice = input(prompt)

    if choice == "q" or choice == "Q":
        do_revert(parm1)
    else:

        choice = int(float(choice))

        if choice < 1 or choice > max_count:
            print("Out of bounds")
            work_multi(data)
        else:
            option = data['opts'][choice - 1]
            sendquery("-rename", data['parm1'], option)

    exit(0)
#-------------------------------------

def display_movie(data):
    print("> Movie located...")
    print()

    tabledata = []
    table = ""
    tabledata.append(["", "Title"])
    tabledata.append(["Movie renamed", data['title']])
    if "srtfile" in data:
        tabledata.append(["Subtitles located:", data['srtfile']])

    table = tabletype(tabledata)
    print(table.table)

    print()

    proceed = query_yes_no("Proceed?", "yes")

    if not proceed:
        do_revert(parm1)
        do_return("> Aborted")

    print()
    print("> Moving file to destination directory...")

    mv_cmd = ""
    mv_cmds = []
    moveables = ("title", "srtfile")
    for item in moveables:
        if item in data:
            move_me = re.escape(data[item])
            move_me = data[item]

            source_file = "%s/%s" % (data['path'], move_me)
            dest_file = "%s/%s" % (config.cfg['mediafiles']['movies'], move_me)
            mv_cmd = "cp \'%s\' \'%s\'" % (source_file, dest_file)

            mv_cmds.append(mv_cmd)

    if testmode:
        print(mv_cmds)
    else:
        for item in mv_cmds:
            # print(item)
            os.system(item)

    if data['path'] == cfg['mediafiles']['downloads']:
        rm_cmd = "rm -rf %s" % data['path']
        os.system(rm_cmd)

    do_return("Completed.")


# -------------------------------------

def display_tv(data, parm1):
    # cfg = configread
    episodes = []
    episodecount = 0

    if cfg['term'] == "yes":
        tabletype = terminaltables.SingleTable
    else:
        tabletype = terminaltables.AsciiTable

    testmode = cfg['testmode']

    title = data['title']

    try:
        episodes = data['episodes']
    except KeyError:
        episodes.append(data['file'])

    print("> TV show located...")
    print()
    # logger.info("TV Show located: %s" % title)

    tabledata = []

    tabledata.append(["TV show found", title])
    tabledata.append(["Episodes:", episodes[0]])

    episodecount = 1
    while episodecount < len(episodes):
        tabledata.append(["", episodes[episodecount]])
        episodecount += 1

    table = tabletype(tabledata)
    # table.inner_heading_row_border = False
    print(table.table)
    print()
    if testmode:
        proceed = True
    else:
        proceed = query_yes_no("Proceed?", "yes")

    if not proceed:
        do_revert(parm1)
    else:

        print("")
        print("> Checking destination directory...")

        dest_dir = "%s/%s" % (cfg['mediafiles']['tv'], data['title'])
        valid_dir = (os.path.isdir(dest_dir))
        if valid_dir:
            print("> Destination directory exists, continuing...")
        else:
            create = query_yes_no("> Destination directory does not exist. Create it?", "yes")

            if create:
                try:
                    os.mkdir(dest_dir)
                except FileNotFoundError:
                    print("Destination directory cannot be created. Please check the directory and \
                           re-run \"mick.py setup\"")
                    exit()
                print("> Directory created.\n")
            else:
                print("> Aborting...")
                # logging.info("TV renaming and moving aborted (%s)" % dict['title'])
                do_return(" done.")

                # destination dir in places, move files
                # movefiles(dict)

    # else to original "Proceed?" prompt
    # else:
    #     print()
    #     print("> Aborted.")
    #     data['quit_reason'] = "> Aborted."
    #     do_return("")

    #### move files ####

    files_to_move = episodes

    len_of_moveables = len(files_to_move)
    counter = 0

    srcpath = data['path']

    while counter <= len_of_moveables - 1:
        destpath = "%s" % cfg['mediafiles']['tv']
        esc_title = re.escape(data['title'])
        esc_episode = episodes[counter]
        destpath = "\"%s/%s\"" % (destpath, esc_episode)
        tmp_episode = episodes[counter]
        esc_episode = re.escape(tmp_episode)
        srcfile = "\"%s/%s\"" % (srcpath, episodes[counter])

        mv_cmd = ("cp %s %s" % (srcfile, destpath))

        if testmode:
            print(mv_cmd)
            # os.system(mv_cmd)
        else:
            print("   Moving %s" % data['episodes'][counter])
            os.system(mv_cmd)

        counter = counter + 1

    print()
    print("> Removimg original source...")
    rm_cmd = "rm -rf %s" % data['path']
    if data['path'] == cfg['mediafiles']['downloads']:
        rm_cmd = "rm -rf %s" % data['path']

        do_return("Completed. Didn't destroy Bikini Atoll")
    else:
        rm_cmd = "rm -rf %s" % data['path']
        os.system(rm_cmd)
        do_return("Completed")


# --------------------------------------

def no_dupes(list):
    workarray = []
    for item in list:
        if item not in workarray:
            workarray.append(item)
    return workarray


def load_dirs():
    dirs = []
    roots = {}
    from collections import defaultdict
    dir_dict = defaultdict(dict)
    dir_dict['']['readme.txt'] = 1

    counter = 0
    # Set the directory you want to start from
    rootDir = '/home/bundito/Downloads'
    roots = defaultdict(dict)
    roots[rootDir]['hello.jpg'] = 2

    filenames = []

    for dirName, subdirList, fileList in os.walk(rootDir):
        # print('Found directory: %s' % dirName)
        # dirnames.append(dirName)

        # fname = ""
        for fname in fileList:
            # print(fname)
            file_ext = fname[-3:]

            if file_ext in vidfiles:
                filenames.append(fname)

                dirs.append(dirName)

    dirs = no_dupes(dirs)

    for filename in os.listdir(rootDir):
        filename_ext = filename[-3:]
        #   print(filename_ext)
        if filename_ext in vidfiles:
            filename = "%s/%s" % (rootDir, filename)
            dirs.append(filename)

    try:
        dirs.remove(rootDir)
    except ValueError:
        dirs = ""
    return dirs


####################################

def draw_table():
    workdirs = load_dirs()

    print(t.clear)

    title = "%s v%s" % (cfg['system_vars']['program_name'], cfg['system_vars']['program_ver'])
    print(t.center(title))

    data = []

    if workdirs == "":
        data.append(["                                 "])
        data.append(["                                 "])
        data.append(["      No unprocessed files."])
        data.append(["                                 "])
        data.append(["                                 "])
        table = tabletype(data)
        table.inner_heading_row_border = False
        print(table.table)
        print()
        logger.info("No files for menu")
        return 0

    counter = 1
    for item in workdirs:
        entry = workdirs[counter - 1]
        entrydata = os.path.split(entry)
        name = entrydata[1]

        name = "%s" % entrydata[1]

        data.append([counter, name])
        counter = counter + 1
        # print(workdirs)
    # table = SingleTable(data)
    table = tabletype(data)
    table.inner_heading_row_border = False
    print(table.table)
    print()
    return counter


################################

def parse_delete(delnum, totalrows):
    if delnum == "q" or delnum == "Q":
        menu_start()
    else:

        workdirs = load_dirs()

        num = (int(float(delnum)))
        num = num - 1

        # print(rows)
        if num < 0 or num > totalrows:
            menu_start()

        entry = workdirs[num]
        entrydata = os.path.split(entry)
        name = entrydata[1]
        query = "> Delete %s?" % name
        confirm = query_yes_no(query, "yes")

        if confirm:
            entry = re.escape(entry)
            os.system("rm -rf %s" % entry)
            logger.info("Manual deletion of %s" % name)
            menu_start()
        else:
            menu_start()


def parse_num(input=0, start=-1, end=99):
    workdirs = load_dirs()

    try:
        input = int(float(input))
    except ValueError:
        menu_start()

        start = int(float(start))
        end = int(float(end))

        if input < start or input > end:
            menu_start()

    num = input - 1
    entry = workdirs[num]
    entrydata = os.path.split(entry)
    name = entrydata[1]

    query = "Rename and copy %s? " % name
    confirm = query_yes_no(query, "yes")

    if not confirm:
        menu_start()
    else:
        logger.info("Renaming from menu: %s" % entry)
        config.write_cfg("location", "menu")
        cfg = config.reread_config()
        sendquery("-rename", entry)


def menu_start():
    workdirs = load_dirs()
    rows = draw_table()

    choice = 99

    if workdirs == "":
        print()
        print("Exiting...")
        print()
        exit()

    choice = input("Enter a number to rename and copy. \"D\" to delete, or \"Q\" to quit: ")

    if choice == "q" or choice == "Q":
        print()
        print("> Aborting...")
        print()
        quit()

    elif choice == "d" or choice == "D":
        print()
        delnum = input("> Item number to delete or \"Q\" to go back: ")

        if input == "q" or input == "Q":
            menu_start()
        else:
            parse_delete(delnum, rows - 1)
            menu_start()
    else:
        parse_num(choice, 1, rows)


def query_yes_no(question, default="yes") \
        :
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")


####################################################

def do_setup():
    no_movies = True
    no_tv = True

    curr_movies = config.cfg['mediafiles']['movies']
    curr_tv = config.cfg['mediafiles']['tv']

    movieprompt = "> Directory for movie files [%s]: " % curr_movies
    tvprompt = "> Directory for TV files [%s]: " % curr_tv

    print(config.program_name + " " + config.program_ver)
    print()
    print('> Set up destination directories...')
    print()

    while no_movies:
        dir_movies = input(movieprompt)

        # query filesystem to see if directory exists
        valid_dir = (os.path.isdir(dir_movies))
        if valid_dir:
            no_movies = False
        else:
            print("%s is not a valid directory." % dir_movies)

    while no_tv:
        dir_tv = input(tvprompt)

        # auery filesystem to see if directory exists
        valid_dir = (os.path.isdir(dir_tv))
        if valid_dir:
            no_tv = False
        else:
            print("%s is not a valid directory." % dir_tv)

    config.cfg['mediafiles']['movies'] = dir_movies
    config.cfg['mediafiles']['tv'] = dir_tv
    config.write_cfg(['mediafiles']['movies'], dir_movies)
    config.write_cfg(['mediafiles']['tv'], dir_tv)

    print()
    print("> Configuration file updated.")


#######################################################################
# the beating heart - analyzes the filebot lines
# and makes decisions about what they contain.
# It's complicated

def analyze(lines, parm1):
    # print(lines)

    print("> Data obtained. Analyzing...")
    print()

    linedata = {}
    filedata = {}
    episodes = {}
    episode_counter = 1
    episode_names = []
    variants = {}
    opts = ""

    for line in lines:

        # testmode = True

        if testmode:
            logger.debug(line)
            print(line)

        # filebot line contains reference to TV show name auto-detection
        if re.search("Auto-detect", line):
            showname = re.search('.*\[(.*)\]', line)
            showname = showname.group(1)
            if re.search(".*\.srt", showname):
                linedata['srtfile'] = showname
            else:
                linedata['auto'] = showname

        # filebot line contains reference to movie title matching
        if line[0:8] == "Fetching":
            lineparts = line.split(" [")
            titlepart = lineparts[1]
            title = titlepart[:-2]
            linedata['title'] = title
            if re.search(".*\.srt", title):
                linedata['srtfile'] = title
            else:
                linedata['fetch'] = title

        # filebot line with "rename" also shows which database is being used
        if line[0:6] == "Rename":
            db = re.search('.*\[(.*)\]', line)
            db = db.group(1)
            if db == "TheTVDB":
                type = "tv"
            elif db == "TheMovieDB":
                type = "movie"
            else:
                type = "other"

            linedata['type'] = type

        # filebot line showing whether or not a file is renamed
        if (re.search("\[MOVE\]", line)) or (re.search("Skipped", line)):
            filename = ""
            filepath = ""

            # not renamed; filename is already correct
            if re.search("Skipped", line):
                grp1 = re.search('\[(.*)\].because.*$', line)
                match = grp1.group(1)
                filename = os.path.basename(match)
                filepath = os.path.dirname(match)
                episode_names.append(filename)

                # file needs renaming
            elif re.search("MOVE", line):
                findit = re.search('.*to \[(.*)\]', line)
                grp1 = findit.group(1)
                fullpath = grp1
                filename = os.path.basename(grp1)
                filepath = os.path.dirname(grp1)
                episode_names.append(filename)

            # both halves of above if/else set the same variables
            linedata['path'] = filepath
            if re.search(".*\.srt", filename):
                linedata['srtfile'] = filename
            else:
                linedata['moveskip'] = filename

        # ambigous tv show title; options shown and captured
        if line[0:8] == "Multiple":
            choices = re.search('.*\[(.*)\].*', line)
            opts = choices.group(1)
            opts = opts.split(", ")
            linedata['type'] = "multi"
            type = "multi"

    # -------- LINE() loop ends here ---------------#

    # assign parsed bits appropriate for TV show
    if linedata['type'] == "tv":
        filedata['episodes'] = []
        for ep in episode_names:
            parts = os.path.splitext(ep)
            if parts[1] != ".nfo":
                filedata['episodes'].append(ep)

        try:
            filedata['title'] = linedata['fetch']
        except KeyError:
            filedata['title'] = linedata['auto']
        filedata['path'] = linedata['path']
        filedata['parm1'] = parm1

    # assign parsed data for movie entry
    if type == "movie":
        filedata['path'] = linedata['path']
        filedata['title'] = linedata['moveskip']
        filedata['parm1'] = parm1
        display_movie(filedata)

    if type == "multi":
        filedata['title'] = linedata['auto']
        filedata['opts'] = opts
        filedata['parm1'] = parm1
        work_multi(filedata, parm1)

    if type == "tv":
        display_tv(filedata, parm1)

        print("Now what?")


##########################################################
def do_quit(reason, data=""):
    print("Terminated: %s" % reason)
    print("Quitting.")
    quit()


def workmulti(dict):
    # TODO - try and handle multiple choice for movies like Trainspotting

    options = dict['choices']
    check_keys = []
    key = ""

    print()
    print("> Ambiguious TV show name. Please choose the correct entry:")
    print()
    size = len(options)
    counter = 1

    print(divline)
    print()

    while counter <= size:
        print("   %i: %s" % (counter, dict['choices'][counter]))
        check_keys.append(str(counter))
        counter = counter + 1

    check_keys.append("q")
    check_keys.append("Q")

    print(divline)
    print()
    print("> Select 1 through %s (or Q to cancel:" % size)

    while key not in check_keys:

        if testmode:
            key = str(5)
        else:
            key = readchar.readkey()

        if key == "q" or key == "Q":
            return
        else:
            index = int(key)
            opt_chosen = (dict['choices'][index])

            print("> Continuing with %s" % opt_chosen)
            print()
            print("> Processing...")
            # resubmit query to filebot
            extra_param = opt_chosen
            output = sendquery("-rename", dirName, extra_param)

            finished_data = analyze(output)

            display_tv(finished_data)

    return


# ------------------------------------------

# send a query through filebot

def sendquery(verb, parm1, q=""):
    lines = []
    if q == "":
        # the main machine - calls filebot with passed parameters
        logger.info('QUERY SENT: %s' % dirName)
        logger.info("\t%s" % parm1)

        pgm = "%s v%s" % (cfg['system_vars']['program_name'], cfg['system_vars']['program_ver'])

        print(t.clear)
        print(t.center(pgm))

        print()
        print("> Processing...")
        print()

        item_exists = os.path.exists(parm1)

        if not item_exists:
            do_return("No such item.")

        proc = subprocess.Popen(["filebot", verb, parm1, q], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    else:

        lines = []
        parm2 = "--q \"%s\"" % q

        logger.info('QUERY SENT (extra param: %s) : %s' % (q, dirName))
        proc = subprocess.Popen(["filebot", verb, parm1, parm2], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    for line in proc.stdout.readlines():
        # query each line and add to lines[] array
        line = line.decode(encoding="utf-8")
        lines.append(line)

    for line in proc.stderr.readlines():
        # query each line and add to lines[] array
        line = line.decode(encoding="utf-8")
        lines.append(line)

    # done, pass the array back
    analyze(lines, parm1)


# ---------------------------------------------------------------#

def dispatcher(func, opts="", opts2=""):
    if func == "query":
        sendquery("-rename", opts)

    if func == "setup":
        do_setup()

        # if __name__ == '__main__':
        #      # test1.py executed as script
        #      # do something
        #      dispatcher(fn, opt="", q2="")
