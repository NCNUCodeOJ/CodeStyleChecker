"""checker python lint"""
import subprocess
import os
from .utils import InitSubmissionEnv


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
    """checker_py checker python file lint"""
    ret = {}
    command = ["pylint", file]
    link = "https://vald-phoenix.github.io/pylint-errors/plerr/errors/format/"

    # get lint message
    result = subprocess.run(command, cwd="/setting", stdout=subprocess.PIPE)
    result = result.stdout.decode("utf-8")
    result = result.splitlines()

    # capture score
    # 10.0 - ((float(5 * error + warning + refactor + convention) / statement) * 10)
    ret["score"] = result[-2].split(" ")[6].split("/")[0]

    # remove empty lines and not format error message
    lint_results = result[1:-4]

    # deal with lint results
    ret["wrong"] = []
    for one_line in lint_results:
        tmp = one_line.split(":")
        ret["wrong"].append({
            "line": tmp[1].strip(),
            "col": tmp[2].strip(),
            "rule": tmp[3].strip(),
            "description": link + tmp[3].strip()
        })

    return ret
