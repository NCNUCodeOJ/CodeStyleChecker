"""checker python lint"""
import subprocess
import os
from .utils import InitSubmissionEnv

checker = "/src/checkstyle-9.0-all.jar"
config = "/setting/google.xml"
pwd = "/tmp"


def check(submission_id, filename, src):
    """checker_py checker python file lint"""
    with InitSubmissionEnv(pwd, submission_id=str(submission_id)) as tmp_dir:
        submission_dir = tmp_dir
        src_path = os.path.join(submission_dir, filename+".py")

        with open(src_path, "w", encoding="utf-8") as file:
            file.write(src)
        
        os.chmod(src_path, 0o400)

        return _checker(src_path)


def _checker(file):
    """checker_py checker java file lint"""
    ret = {}
    command = ["java", "-jar", checker, "-c", config, file]

    # get lint message
    result = subprocess.run(command, cwd=pwd, stdout=subprocess.PIPE)
    result = result.stdout.decode("utf-8")
    result = result.splitlines()

    # remove unnecessary lines
    lint_results = result[1:-1]

    # deal with lint results
    ret["wrong"] = []
    for one_line in lint_results:
        tmp = one_line.split(" ")
        ret["wrong"].append({
            "line": tmp[1].split(":")[1].strip(),
            "col": tmp[1].split(":")[2].strip(),
            "rule": tmp[-1].strip()[1:-1],
            "description": " ".join(tmp[2:-1]),
        })
    
    # get code line count
    command = ["cloc", "--quiet", file]
    result = subprocess.run(command, cwd=pwd, stdout=subprocess.PIPE)
    result = result.stdout.decode("utf-8")
    count = int(result.splitlines()[-2].split()[-1])

    ret["score"] = "%.2f" % round( 10 - len(ret["wrong"]) / count * 10, 2)

    return ret
