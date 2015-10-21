import cmd

from shellassist.calendar import date_functions
from shellassist.shell.go import Go
from shellassist.shell.add import Add


class ShellAssistCmd(cmd.Cmd):
  
  def __init__(self):
    cmd.Cmd.__init__(self)
    self.current_date = date_functions.get_today_date()
  
  def update_prompt(self):
    date_string = date_functions.date_string(self.current_date)
    self.prompt = '[ ' + date_string +  ' ] > '

  def preloop(self):
    print "Running Shell Assist..."
    self.update_prompt()

  def postcmd(self, stop, line):
    self.update_prompt()
    return stop

  def do_quit(self, arg):
    quit()

  def do_exit(self, arg):
    quit()

  def do_go(self, arg):
    go = Go(self, arg)
    go.execute()

  def do_add(self, arg):
    add = Add(self, arg)
    add.execute()



def main():
  shell = ShellAssistCmd()
  shell.cmdloop()