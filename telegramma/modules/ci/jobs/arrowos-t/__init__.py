"""ArrowOS T CI project."""

from telegramma.modules.ci.utils.aosp.job import AOSPJob

class Job(AOSPJob):
        name = "ArrowOS"
        version = "13.0"
        android_version = "13"
        zip_name = "Arrow-*.zip"
        lunch_prefix = "arrow"
        date_regex = "Arrow-[a-z][0-9.]+-[a-zA-Z]+-[a-zA-Z]+-([0-9]+)-[a-zA-Z]+.zip"
