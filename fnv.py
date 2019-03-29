import os
import argparse
import fnvhash

def ouput(hash_string, hash_val):
  print("hash_string = \"", hash_string, "\", hash_val = ", hash_val)

class fnv_run:
  def __init__(self, cur_run_file_path):
    run_file_abs_path = os.path.abspath(cur_run_file_path)
    self.def_hash_file = os.path.dirname(run_file_abs_path) + r"\hash_string.txt"
    print(self.def_hash_file)

  def parse_arg(self):
    parser = argparse.ArgumentParser(description = "fnv1a hash helper")
    # TODO - 待支持多个给定字符串，当前仅1个
    parser.add_argument("-s", "-S", "--hash_given_string_list", nargs = 1, dest = "hash_given_string_list", help = r"hash the given string")
    parser.add_argument("-f", "-F", "--hash_file", nargs = 1, dest = "hash_file", help = r"the path of hash string file, def hash_string.txt of cur path")
    return parser.parse_args()

  def load_hash_file(self, hash_src_file):
    with open(hash_src_file, 'r') as hf: 
      hash_string_list = hf.readlines()
      print("load hash string from {}".format(hash_src_file))
      return hash_string_list

  def hash_string_list(self, hash_string_list):
    for hash_string in hash_string_list:
      hash_string = hash_string.strip()
      hash_val = fnvhash.fnv1a_32(hash_string.encode('utf-8'))
      ouput(hash_string, hash_val)

  def hash_file(self):
    if self.args.hash_file:
      hash_string_list = self.load_hash_file(self.args.hash_file[0])
    else:
      hash_string_list = self.load_hash_file(self.def_hash_file)

    self.hash_string_list(hash_string_list)
  
  def run(self):
    self.args = self.parse_arg()

    if self.args.hash_given_string_list:
      self.hash_string_list(self.args.hash_given_string_list)
    else:
      self.hash_file()

if __name__ == "__main__":
  fnv_run_obj = fnv_run(__file__)
  fnv_run_obj.run()