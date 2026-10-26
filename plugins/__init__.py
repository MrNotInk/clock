"""
weld plugin hook template.
"""


def before_build(config: dict) -> None:
    pass


def after_build(config: dict, archive_path: str) -> None:
    pass


def before_install(config: dict) -> None:
    pass


def after_install(config: dict) -> None:
    pass


def before_remove(pkg_name: str) -> None:
    pass


def after_remove(pkg_name: str) -> None:
    pass


def before_update(config: dict) -> None:
    pass


def after_update(config: dict) -> None:
    pass
