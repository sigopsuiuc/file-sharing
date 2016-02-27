# Interactive Shell
# This is the file where the interactive shell is written
# It is used for human interaction


class InteractiveShell:

    def __init__(self):
        pass

    # Usage: Show the newest changes made by other peers
    # Arguments: none
    # Return Value: a list of changed filenames
    # Side effect: update files.db entry
    # Notes:
    def fetch(self, li_filename, peer):
        pass

    # Usage: Show the changes made by your own
    # Arguments: none
    # Return Value: a list of changed filenames
    # Side effect: update files.db entry
    # Notes:
    def status(self, li_filename):
        pass

    # Usage: update files to the version from user
    # Arguments: none
    # Return Value: a list of changed filenames
    # Side effect: update files.db entry, update local files
    # Notes:
    def update(self, li_ilename, peer):
        pass



