import os
import re
import subprocess
import pickle


testmode = True

#################
def analyze(lines):
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
            #logger.debug(line)
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
            title = titlepart[:-1]
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
        #filedata['parm1'] = parm1

    # assign parsed data for movie entry
    if type == "movie":
        filedata['path'] = linedata['path']
        filedata['title'] = linedata['moveskip']
        #filedata['parm1'] = parm1
        #display_movie(filedata)

    if type == "multi":
        filedata['title'] = linedata['auto']
        filedata['opts'] = opts
        #filedata['parm1'] = parm1
        #work_multi(filedata, parm1)

    if type == "tv":
        #display_tv(filedata, parm1)

        print("Now what?")

    print(filedata)
    quit()

# send a query through filebot

def sendquery(obj, verb, q=""):
    lines = []

    kosher = pickle.loads(obj)
    titlepath = kosher.fullpath

    if q == "":
        # the main machine - calls filebot with passed parameters
        ##logger.info('QUERY SENT: %s' % dirName)
        ##logger.info("\t%s" % titlepath)



        print("From parser, it's... %s" % titlepath)
       # exit()

        print()
        print("> Processing...")
        print()

        item_exists = os.path.exists(titlepath)

        # if not item_exists:
        #     do_return("No such item.")

        # !! launch a subprocess to open a connection to filebot !!
        proc = subprocess.Popen(["filebot", verb, titlepath, q], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    else:

        lines = []

        # specific query for multiple-choice TV series
        query = "--q \"%s\"" % q

        # !! launch a (modified) subprocess to open a connection to filebot !!
        proc = subprocess.Popen(["filebot", verb, titlepath, query], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # these blocks run for either subprocess case
    for line in proc.stdout.readlines():
        # query each line and add to lines[] array
        line = line.decode(encoding="utf-8")
        line = re.sub("\\n", "", line)
        lines.append(line)

    for line in proc.stderr.readlines():
        # query each line and add to lines[] array
        line = line.decode(encoding="utf-8")
        line = re.sub("\\n", "", line)
        lines.append(line)


    # done, send in the array of lines for parsing
    analyze(lines)
