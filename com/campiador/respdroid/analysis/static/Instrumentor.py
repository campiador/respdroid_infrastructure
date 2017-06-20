import re


class Instrumentor:
    def instrumentApk(self):
        print("instrument APK")

    def instrumentSourceCode(self):
        print("instrument source code")

def parse_java_file(fname):
    print("parsing a java file")

    with open(fname) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    found_decode = False
    line_decode= ""
    for line in content:
        print line
        if "decodeFile"  in line:
            found_decode = True
            line_decode = line

    if found_decode:
        print "found decode"
        print line_decode

        outer = re.compile("(.+)\((.+)\)(.+)")
        m = outer.search(line)

        # Lets use a regular expression to match a date string. Ignore
        # the output since we are just testing if the regex matches.
        regex = r"\((.+)\)"
        # if re.search(regex, line):
        if m != None:
            # Indeed, the expression "([a-zA-Z]+) (\d+)" matches the date string

            # If we want, we can use the MatchObject's start() and end() methods
            # to retrieve where the pattern matches in the input string, and the
            # group() method to get all the matches and captured groups.
            # match = re.search(regex, line)


            # This will print [0, 7), since it matches at the beginning and end of the
            # string
            # print "Match at index %s, %s" % (match.start(), match.end())
            print "Match at index %s, %s" % (m.start(), m.end())
        else:
            print "pattern not matched"




parse_java_file("MainActivity.java")