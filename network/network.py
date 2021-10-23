#%%
# Import all
import torch
from torch import nn
from torch.autograd import Variable
from torch import optim
import torch.nn.functional as F

import matplotlib
# matplotlib.use('Agg')
%matplotlib inline

import datetime as dt, itertools, pandas as pd, matplotlib.pyplot as plt, numpy as np

import utility as util

global logger

util.setup_log()
util.setup_path()
logger = util.logger
text_process.logger = logger

use_cuda = torch.cuda.is_available()
logger.info("Is CUDA available? %s.", use_cuda)

#%%