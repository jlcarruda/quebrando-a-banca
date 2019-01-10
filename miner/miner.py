class Miner:
  import pandas as pd
  import matplotlib.pyplot as plt
  import numpy as np

  def process_chain(self):
    print 'empty process chain'

  def process(self):
    self.before_process()
    self.process_chain()
    self.after_process()

  def before_process(self):
    print "beforeProcess"

  def after_process(self):
    print "afterProcess"
