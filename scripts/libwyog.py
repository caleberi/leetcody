import argparse # parsing cli argument
import collections  # necessary data-structure such as order-dict
import configparser # parsing configuration in INI file
import hashlib # for hashing 
import os # for files system abstraction
import sys # extracting information about system / argument
import re # for handling text marching and analysis
import  zlib # for compression


class GitRepository:
    """
    A abstract representation of a version control repository like GIT
    """
    work_tree = None
    git_dir = None
    conf = None

    def __init__(self,path,force=False):
        """
        Creates a  new initialized tracking VSC folder for a project\n
        params: <str> path - path to which the repo should be created
        params: <bool> force - ignore all path check for exitence and overwrite  forcefully
        """
        self.work_tree = path # git tree working path
        self.git_dir = os.path.join(path,".git") # location of .git folder

        if not (force or os.path.isdir(self.git_dir)):
            raise Exception("Not a Git repository %s" % path)
        
        # Read configuration file in .git/config
        self.conf = configparser.ConfigParser()
        cf = repo_file(self,"config")

        if cf and os.path.exists(cf):
            self.conf.read([cf])
        elif not force:
            raise Exception("Configuration is missing")

        if not force:
            vers = int(self.conf.get("core","repositoryformatversion"))
            if  vers != 0 :
                raise Exception("Unsupported repositoryformatversion %s" % vers)



class GitObject:
    repo = None
    def __init__(self,repo,data=None):
        self.repo = repo

        if data != None:
            self.serialize(data)
    
    def serialize(self):
        """
        This function MUST be implemented by subclasses.\n
        It must read the object's contents from self.data, a byte string,\n
        and do whatever it takes to convert it into a meaningful representation.\n
        What exactly that means depend on each subclass."""
        raise Exception("Unimplemented!")
    
    def deserialize(self,data):
        raise Exception("Unimplemented!")


class GitBlob(GitObject):
    fmt = b'blob'

    def serialize(self):
        return self.blobdata

    def deserialize(self, data):
        self.blobdata = data
    
class GitCommit(GitObject):
    fmt = b'commit'

    def serialize(self):
        return kvlm_deserialize(self.kvlm)

    def deserialize(self, data):
        self.kvlm = kvlm_parser(data)
        
class GitTree(GitObject):
    fmt=b'tree'

    def deserialize(self, data):
        self.items = tree_parse(data)

    def serialize(self):
        return tree_serialize(self)


class GitTag(GitCommit):
    fmt = b'tag'

class GitTreeLeaf(object):
    def __init__(self,mode,path,sha):
        self.mode = mode 
        self.path = path
        self.sha = sha



def tree_parse_one(raw,start):
    # find the space terminator of the mode
    space_pos = raw.find(b' ',start)
    assert(space_pos-start==5 or space_pos-start==6)
    # read the mode
    mode = raw[start:space_pos]
    # find the null character
    null_ch = raw.find(b'\x00',space_pos)
    # read the tree path
    path = raw[space_pos+1:null_ch]
    # read the SHA and convert to an hex string
    sha = hex(int.from_bytes(raw[path+1:path+21],"big"))[2:] # hex() adds 0x in front
    return path+1,GitTreeLeaf(mode,path,sha)

def tree_parse(raw):
    pos = 0
    max_len = len(raw)
    ret = list()
    while pos < max_len:
        pos,data = tree_parse_one(raw,pos)
        ret.append(data)
    return ret

def tree_serialize(obj):
    #@FIXME Add serializer!
    ret = b''
    for i in obj.items:
        ret += i.mode
        ret += b' '
        ret += i.path
        ret += b'\x00'
        sha = int(i.sha, 16)
        # @FIXME Does
        ret += sha.to_bytes(20, byteorder="big")
    return ret
        

arg_parser =  argparse.ArgumentParser(description="The stupid content tracker")
arg_subparsers = arg_parser.add_subparsers(title="COMMAND",dest="command")
arg_subparsers.required = True
argsp = arg_subparsers.add_parser(
    "init",
    help="Initialize a new , empty repository."
)
argsp.add_argument(
    "path",
    metavar = "directory",
    nargs="?",
    default=".",
    help="path to initialize the repository "
)

argsp = arg_subparsers.add_parser(
    "cat-file",
    help="Provide content of the repository"
)

argsp.add_argument(
    "type",
    metavar="type",
    choices=["blob","tree","commit","tag"],
    help="specify the type"
)

argsp.add_argument(
    "object",
    metavar="object",
    help="the object to display"
)

argsp =  arg_subparsers.add_parser(
    "hash-object",
    help="compute the object id and optionally create a blob for the file",
)

argsp.add_argument(
    "-t",
    metavar="type",
    dest="type",
    choices=["blob","tree","commit","tag"],
    default="blob",
    help="specify the type"
)

argsp.add_argument(
    "-w",
    dest="write",
    action="store_true",
    help="actually writes the object into the database"
)

argsp.add_argument("path",
                   help="read object from <file>")

argsp = arg_subparsers.add_parser(
    "log",
    help = "display history of a given commit"
)
argsp.add_argument(
    "commit",
    default="HEAD",
    nargs="?",
    help="commit to start at"
)

argsp = arg_subparsers.add_parser("ls-tree", help="pretty-print a tree object.")
argsp.add_argument("object",
                   help="the object to show.")

argsp = arg_subparsers.add_parser(
    "checkout",
    help="checkout a commit inside of a directory. ")

argsp.add_argument(
    "commit",
    help="the tree or commit to checkout "
)

argsp.add_argument(
    "path",
    help="the empty directory to checkout on."
)
argsp = arg_subparsers.add_parser("show-ref", help="List references.")

argsp = arg_subparsers.add_parser(
    "tag",
    help="List and create tags"
)

argsp.add_argument("-a",
                    action="store_true",
                    dest="create_tag_object",
                    help="whether to create a tag object")

argsp.add_argument("name",
                    nargs="?",
                    help="the new tag's name")

argsp.add_argument("object",
                    default="HEAD",
                    nargs="?",
                    help="the object the new tag will point to"
)

argsp = arg_subparsers.add_parser(
    "rev-parse",
    help="parse revision (or other objects )identifiers")

argsp.add_argument("--wyag-type",
                   metavar="type",
                   dest="type",
                   choices=["blob", "commit", "tag", "tree"],
                   default=None,
                   help="Specify the expected type")

argsp.add_argument("name",
                   help="The name to parse")

def repo_path(repo,*path):
    """Compute path under repo's gitdir."""
    return os.path.join(repo.git_dir,*path)

def repo_file(repo,*path,mkdir=False):
    """
    Same as repo_path, but create dirname(*path) if absent. \n 
    For example, \n\trepo_file(r, \"refs\", \"remotes\", \"origin\", \"HEAD\") will create
    .git/refs/remotes/origin.
    """
    if repo_path(repo,*path[:-1],mkdir=mkdir):
        return repo_path(repo,path)

def repo_dir(repo,*path,mkdir=False):
    """
    Same as repo_path, but mkdir *path if absent.
    """
    path = repo_path(repo,*path)

    if os.path.exists(path):
        if os.path.isdir(path):
            return path
        raise Exception("Not a directory %s" % path) 
    
    if mkdir:
        os.makedirs(path)
        return path
    else:
        return None

def repo_default_config():
    ret =  configparser.ConfigParser()
    
    ret.add_section("core")
    ret.set("core","repositoryformatversion",0)
    ret.set("core","filemode","false")
    ret.set("core","bare","false")
    return ret

def repo_create(path):
    """
    Creates a new git repository at the specified path
    """

    repo =  GitRepository(path,True)

    # check to see if the path does not exist or is an empty dir
    if not os.path.exists(repo.work_tree):
        if not os.path.isdir(repo.work_tree):
            raise Exception("%s is not a directory!" % path)
        if os.listdir(repo.work_tree):
             raise Exception("%s is not empty!" % path)
    else:
        os.makedirs(repo.work_tree)

    assert(repo_dir(repo, "branches", mkdir=True))
    assert(repo_dir(repo, "objects", mkdir=True))
    assert(repo_dir(repo, "refs", "tags", mkdir=True))
    assert(repo_dir(repo, "refs", "heads", mkdir=True))

    # .git/description
    with open(repo_file(repo,"description"),"w") as f:
        f.write("Unnamed repository; edit this file 'description' to name the repository.\n")
    
    # .git/HEAD
    with open(repo_file(repo,"HEAD"),"w") as f:
        f.write("ref: refs/heads/master\n")

    with open(repo_path(repo,"config"),"w") as f:
        config = repo_default_config()
        config.write(f)
    return repo

def repo_find(path=".",required=True):

    path = os.path.realpath(path)  # /user/documents/project/..

    if os.path.isdir(os.path.join(path,".git")) :
        return GitRepository(path)
    
    # If we haven't returned, recurse in parent, if w
    parent = os.path.realpath(os.path.join(path,".."))

    if parent == path:
        # Bottom case
        # os.path.join("/", "..") == "/":
        # If parent==path, then path is root.
        if required:
            raise Exception("No git directory.")
        else:
            return None
    
    # Recursive case
    return repo_find(parent, required)


def select_git_object_type(type,sha):
    types={
        b"commit":GitCommit,
        b"tree":GitTree,
        b"tag":GitTag,
        b"blob":GitBlob
    }
    if type in types:
        return types[type]
    else:
        raise Exception(
            "Unknown type {0} for object {1}".format(
                type.decode("ascii"), sha)
        )



def object_read(repo,sha):
    """
    Read an object's object_id from a repository\n
    returns: <GitRepository> whose type depend on the object.
    """
    path = repo_path(repo,"objects",sha[:2],sha[2:])
    
    with open(path,"rb") as f:
        raw = zlib.decompress(f.read())
        # Read object type
        x = raw.find(b' ')
        fmt = raw[0:x]
        # Read and validate object size
        y = raw.find(b'\x00',x)
        sz = int(raw[x:y].decode("ascii"))
        if sz != len(raw)-y-1:
            raise Exception("Malformed object {0}: bad length".format(sha))
        # Pick constructor
        c = select_git_object_type(fmt,sha)
        # Call constructor and return object
        return c(repo, raw[y+1:])

def object_write(obj,actually_write=True):
    """
    Performs serialization of object and hash computation of the repository\n
    before create dir and files such as  this : \n
    .git/objects/e6/73d1b7eaa0aa01b5bc2442d570a765bdaae751
    """
    # serialize object data
    data = obj.serialize()
    # add header
    result = obj.fmt + b' ' + str(len(data)).encode() + b'\x00' + data
    # compute hash 
    sha =  hashlib.sha1(result).hexdigest()
    if actually_write:
        # compute path
        path  = repo_path(obj.repo,"objects",sha[:2],sha[2:],mkdir=actually_write)
        with open(path, 'wb') as f:
            # compress and write
            f.write(zlib.compress(result))

    return sha




def object_find(repo, name, fmt=None, follow=True):
    sha = object_resolve(repo, name)

    if not sha:
        raise Exception("No such reference {0}.".format(name))

    if len(sha) > 1:
        raise Exception("Ambiguous reference {0}: Candidates are:\n - {1}.".format(name,  "\n - ".join(sha)))

    sha = sha[0]

    if not fmt:
        return sha

    while True:
        obj = object_read(repo, sha)

        if obj.fmt == fmt:
            return sha

        if not follow:
            return None

        # Follow tags
        if obj.fmt == b'tag':
            sha = obj.kvlm[b'object'].decode("ascii")
        elif obj.fmt == b'commit' and fmt == b'tree':
            sha = obj.kvlm[b'tree'].decode("ascii")
        else:
            return None


def cat_file(repo,obj,fmt=None):
    obj = object_read(repo,repo_find(repo,obj,fmt=fmt))
    sys.stdout.buffer.write(obj.serialize())

def kvlm_parser(raw,start=0,dct=None):
    if not dct:
        # You CANNOT declare the argument as dct=OrderedDict() or all
        # call to the functions will endlessly grow the same dict.
        dct =  collections.OrderedDict()
    # we search for the next space and the next newline.
    space =  raw.find(b' ',start)
    newline = raw.find(b' ',start)
    # If space appears before newline, we have a keyword.

    # Base case
    # =========
    # If newline appears first (or there's no space at all, in which
    # case find returns -1), we assume a blank line.  A blank line
    # means the remainder of the data is the message.
    if (space < 0) or (newline < space):
        assert(newline == start)
        dct[b' '] = raw[start+1]
        return dct
    # Recursive case
    # ==============
    # we read a key-value pair and recurse for the next.
    key = raw[start:space]
    # find the end of the value.  Continuation lines begin with a
    # space, so we loop until we find a "\n" not followed by a space.
    end = start
    while True:
        end = raw.find(b'\n', end+1)
        if raw[end+1] != ord(' '): break
    
    # grab the value
    # also, drop the leading space on continuation lines
    value = raw[space+1:end].replace(b'\n ', b'\n')
    # don't overwrite existing data contents
    if key in dct:
        if type(dct[key]) == list:
            dct[key].append(value)
        else:
            dct[key] = [ dct[key], value ]
    else:
        dct[key]=value
    return kvlm_parser(raw, start=end+1, dct=dct)


def kvlm_deserialize(kvlm):
    ret = b''
    # output fields
    for k in kvlm.keys():
        # skip the message itself
        if k == b'': continue
        val = kvlm[k]
        # normalize to a list
        if type(val) != list:
            val = [val]
        for v in val:
            ret += k + b' ' + (v.replace(b'\n', b'\n ')) + b'\n'
    # append message
    ret += b'\n' + kvlm[b'']
    return ret


def object_hash(fd,fmt,repo=None):
    data = fd.read()

    # choose constructor depending on
    # object type found in header.
    if fmt==b"commit" : obj = GitCommit(repo,data)
    elif fmt==b"tree" : obj = GitTree(repo,data)
    elif fmt==b"tag": obj = GitTag(repo,data)
    elif fmt == b"blob": obj=GitBlob(repo,data)
    else:
        raise Exception("Unknown type %s!" % fmt)
    return object_write(obj,repo)

def log_graphviz(repo,sha,seen):

    if sha in seen:
        return

    seen.add(sha)
    commit = object_read(repo, sha)
    assert (commit.fmt==b'commit')

    if not b'parent' in commit.kvlm.keys():
        # base case: the initial commit
        return
    
    parents = commit.kvlm[b'parent']
    if type(parents) != list:
        parents = [ parents ]
    
    for p in parents:
        p = p.decode("ascii")
        print ("c_{0} -> c_{1};".format(sha, p))
        log_graphviz(repo, p, seen)


def tree_checkout(repo, tree, path):
    for item in tree.items:
        obj = object_read(repo, item.sha)
        dest = os.path.join(path, item.path)

        if obj.fmt == b'tree':
            os.mkdir(dest)
            tree_checkout(repo, obj, dest)
        elif obj.fmt == b'blob':
            with open(dest, 'wb') as f:
                f.write(obj.blobdata)

def ref_resolve(repo,ref):
    with open(repo_file(repo,ref),"r") as fp:
        data = fp.read()[:-1] # drop the \n
    if data.startswith("ref: "):
        return ref_resolve(repo,data[5:])
    return data


def ref_list(repo, path=None):
    if not path:
        path = repo_dir(repo, "refs")
    ret = collections.OrderedDict()
    # Git shows refs sorted.  To do the same, we use
    # an OrderedDict and sort the output of listdir
    for f in sorted(os.listdir(path)):
        can = os.path.join(path, f)
        if os.path.isdir(can):
            ret[f] = ref_list(repo, can)
        else:
            ret[f] = ref_resolve(repo, can)

    return ret

def show_ref(repo, refs, with_hash=True, prefix=""):
    for k, v in refs.items():
        if type(v) == str:
            print ("{0}{1}{2}".format(
                v + " " if with_hash else "",
                prefix + "/" if prefix else "",
                k))
        else:
            show_ref(repo, v, with_hash=with_hash, prefix="{0}{1}{2}".format(
                prefix, "/" if prefix else "", k))


def object_resolve(repo, name):
    """
    Resolve name to an object hash in repo.
    This function is aware of:

    - the HEAD literal
    - short and long hashes
    - tags
    - branches
    - remote branches
    """
    candidates = list()
    hashRE = re.compile(r"^[0-9A-Fa-f]{4,40}$")

    # Empty string?  Abort.
    if not name.strip():
        return None

    # Head is nonambiguous
    if name == "HEAD":
        return [ ref_resolve(repo, "HEAD") ]


    if hashRE.match(name):
        if len(name) == 40:
            # This is a complete hash
            return [ name.lower() ]

        # This is a small hash 4 seems to be the minimal length
        # for git to consider something a short hash.
        # This limit is documented in man git-rev-parse
        name = name.lower()
        prefix = name[0:2]
        path = repo_dir(repo, "objects", prefix, mkdir=False)
        if path:
            rem = name[2:]
            for f in os.listdir(path):
                if f.startswith(rem):
                    candidates.append(prefix + f)

    return candidates

def matcher(cmd):

    def cmd_init(args):
        repo_create(args.path)

    def cmd_cat_file(args):
        repo = repo_find()
        cat_file(repo,args.object,fmt=args.type.encode())

    def cmd_hash_object(args):
        if args.write:
            repo = GitRepository(".")
        else:
            repo = None
        with open(args.path,"rb") as fd:
            sha = object_hash(fd,args.type.encode(),repo)  
            print(sha)


    def cmd_log(args):
        repo = repo_find()
        print("digraph wyoglog{")
        log_graphviz(repo,object_find(repo,args.commit),set())
        print("}")

    def cmd_ls_tree(args):
        repo = repo_find()
        obj = object_read(repo, object_find(repo, args.object, fmt=b'tree'))

        for item in obj.items:
            print("{0} {1} {2}\t{3}".format(
                 "0" * (6 - len(item.mode)) + item.mode.decode("ascii"),
            # Git's ls-tree displays the type
            # of the object pointed to.  We can do that too :)
            object_read(repo, item.sha).fmt.decode("ascii"),
            item.sha,
            item.path.decode("ascii")))

    def cmd_checkout(args):
        repo = repo_find()
        obj = object_find(repo,object_find(repo,args.commit))
        # if the object is a commit , grab the tree
        if obj.fmt == b'commit':
            obj = object_find(repo,obj.kvlm[b'tree'].decode("ascii"))
        # verify that  path is an empty directory
        if os.path.exists(args.path):
            if os.path.isdir(args.path):
                raise Exception("Not a directory {0}!".format(args.path))
            if os.listdir(args.path):
                raise Exception("Not empty {0}!".format(args.path))
        else:
            os.makedirs(args.path)
        tree_checkout(repo,obj,os.path.realpath(args.path).encode())

    def cmd_show_ref(args):
        repo = repo_find()
        refs = ref_list(repo)
        show_ref(repo, refs, prefix="refs")

    def cmd_tag(args):
        repo = repo_find()

        if args.name:
            tag_create(args.name,
                    args.object,
                    type="object" if args.create_tag_object else "ref")
        else:
            refs = ref_list(repo)
            show_ref(repo, refs["tags"], with_hash=False)

    def cmd_rev_parse(args):
        if args.type:
            fmt = args.type.encode()

        repo = repo_find()

        print (object_find(repo, args.name, args.type, follow=True))

    commands = {
        # "add" : cmd_add,
        "cat-file":cmd_cat_file,
        "checkout":cmd_checkout,
        # "commit":cmd_commit,
        "hash-object":cmd_hash_object,
        "init": cmd_init,
        "log":cmd_log,
        "ls-tree":cmd_ls_tree,
        # "merge":cmd_merge,
        # "rebase":cmd_rebase,
        "rev-parse":cmd_rev_parse,
        # "rm":cmd_rm,
        "show_ref":cmd_show_ref,
        "tag":cmd_tag,
        # "clone":cmd_clone
    }
    if cmd in commands:
        return commands[cmd]
    else:
        # return cmd_help
        return "None"
    

def main(argv=sys.argv[1:]):
    """
    Entry point but we have to remove the python3 from the incoming argument \n
    by slicing starting from index removing python3 which is at index 0
    """
    args = arg_parser.parse_args(argv)
    matcher(args.command)(args)