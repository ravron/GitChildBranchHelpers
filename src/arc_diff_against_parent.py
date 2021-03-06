import sys

from git_helpers import get_current_branch, arc, fail_if_not_rebased
from git_rebase_children import get_branch_tracker

try:
    # noinspection PyUnresolvedReferences
    from typing import List
except ImportError:
    pass


def main(extra_arc_diff_options):
    # type: (List[str]) -> None
    if extra_arc_diff_options:
        extra_args = " " + " ".join(extra_arc_diff_options)
    else:
        extra_args = ""

    current_branch = get_current_branch()
    with get_branch_tracker() as tracker:
        parent = tracker.parent_for_child(current_branch)
        fail_if_not_rebased(current_branch, parent, tracker)
        arc("diff %s%s" % (parent, extra_args))

if __name__ == '__main__':
    args = sys.argv[1:]
    main(args)
