class Storage(object):

  @staticmethod
  def setup(folder_list, file_list):
    """ Setup storage to work.
    Make sure required folders exist. If not, create new folders
    Make sure required files exist. If not, create new files.

    Parameters:
    folder_list: list of RELATIVE paths to folders.
    files_list: list of RELATIVE paths to files.
    """
    print "setup method"