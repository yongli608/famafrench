"""
This file is part of famafrench.
Copyright (c) 2020, Christian Jauregui <chris.jauregui@berkeley.edu>
See file LICENSE.txt for license information.

Filename
_________
`examples/famafrench_allsorts_me_beta.py`

Construct portfolio returns based using univariate or bivariate sorts on
* Size (ME)
* Market Beta (BETA)

Ken French online library:
Portfolios Formed on Market Beta
____________________________________
https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/Data_Library/det_port_form_BETA.html

25 Portfolios Formed on Size and Market Beta
____________________________________
https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/Data_Library/tw_5_ports_me_BETA.html

"""
import os
import datetime as dt
import famafrench.famafrench as ff

startDate = dt.date(1960, 1, 1)  # "default" startDate
endDate = dt.date.today()  # "default" endDate
#startDate = dt.date(1970, 1, 1)
#endDate = dt.date(2019, 12, 31)

# pickled_dir
pickled_dir = os.getcwd() + '/famafrench/pickled_db/'

#%%
#***************************************************************************#
#***************************************************************************#
#*****************           Market Beta (BETA)          *******************#
#***************************************************************************#
#***************************************************************************#

#**********************************************************************************************#
# Daily Portfolios Formed on Market Beta (BETA)
#**********************************************************************************************#
runQuery, runEstimation = False, True
ffFreq = 'D'
ffFactors, ffsortCharac, ffportCharac = [], ['BETA'], ['BETA']
ff_D = ff.FamaFrench(pickled_dir, runQuery, ffFreq, ffsortCharac, ffFactors, ffportCharac, runEstimation)

# - 3 portfolios (3x1) sorted on ['BETA']
sortingDim = [3]
ff_D.getFamaFrenchStats('Returns',  ffFreq, startDate, endDate, sortingDim, 'vw')
ff_D.getFamaFrenchStats('NumFirms', ffFreq, startDate, endDate, sortingDim)
ff_D.getFamaFrenchStats('Characs',  ffFreq, startDate, endDate, sortingDim)

# - 5 portfolios (5x1) sorted on ['BETA']
sortingDim = [5]
ff_D.getFamaFrenchStats('Returns',  ffFreq, startDate, endDate, sortingDim, 'vw')
ff_D.getFamaFrenchStats('NumFirms', ffFreq, startDate, endDate, sortingDim)
ff_D.getFamaFrenchStats('Characs',  ffFreq, startDate, endDate, sortingDim)

# - 10 portfolios (10x1) sorted on ['BETA']
sortingDim = [10]
ff_D.getFamaFrenchStats('Returns',  ffFreq, startDate, endDate, sortingDim, 'vw')
ff_D.getFamaFrenchStats('NumFirms', ffFreq, startDate, endDate, sortingDim)
ff_D.getFamaFrenchStats('Characs',  ffFreq, startDate, endDate, sortingDim)


#%%
#**********************************************************************************************#
# Monthly Portfolios Formed on Market Beta (BETA)
#**********************************************************************************************#
runQuery, runEstimation = False, True
ffFreq = 'M'
ffFactors, ffsortCharac, ffportCharac = [], ['BETA'], ['ME', 'BETA']
ff_M = ff.FamaFrench(pickled_dir, runQuery, ffFreq, ffsortCharac, ffFactors, ffportCharac, runEstimation)

# - 3 portfolios (3x1) sorted on ['BETA']
sortingDim = [3]
ff_M.getFamaFrenchStats('Returns',  ffFreq, startDate, endDate, sortingDim, 'vw')
ff_M.getFamaFrenchStats('NumFirms', ffFreq, startDate, endDate, sortingDim)
ff_M.getFamaFrenchStats('Characs',  ffFreq, startDate, endDate, sortingDim)

# - 5 portfolios (5x1) sorted on ['BETA']
sortingDim = [5]
#portTableM = ff_M.getPortfolioReturns(False, startDate, endDate, sortingDim, 'vw')
#kfportTableM = ff_M.getkfPortfolioReturns(ffFreq, startDate, endDate, sortingDim, 'vw')
_, _, _, = ff_M.comparePortfolios('Returns',  ffFreq, startDate, endDate, sortingDim, 'vw')
_, _, _, = ff_M.comparePortfolios('NumFirms', ffFreq, startDate, endDate, sortingDim)
_, _, _, = ff_M.comparePortfolios('Characs',  ffFreq, startDate, endDate, sortingDim)
ff_M.getFamaFrenchStats('Returns',  ffFreq, startDate, endDate, sortingDim, 'vw')
ff_M.getFamaFrenchStats('NumFirms', ffFreq, startDate, endDate, sortingDim)
ff_M.getFamaFrenchStats('Characs',  ffFreq, startDate, endDate, sortingDim)

# - 10 portfolios (10x1) sorted on ['BETA']
sortingDim = [10]
_, _, _, = ff_M.comparePortfolios('Returns',  ffFreq, startDate, endDate, sortingDim, 'vw')
_, _, _, = ff_M.comparePortfolios('Characs',  ffFreq, startDate, endDate, sortingDim)
ff_M.getFamaFrenchStats('Returns',  ffFreq, startDate, endDate, sortingDim, 'vw')
ff_M.getFamaFrenchStats('NumFirms', ffFreq, startDate, endDate, sortingDim)
ff_M.getFamaFrenchStats('Characs',  ffFreq, startDate, endDate, sortingDim)


#%%
#**********************************************************************************************#
# Annual Portfolios Formed on Market Beta (BETA)
#**********************************************************************************************#
runQuery, runEstimation = False, True
ffFreq = 'A'
ffFactors, ffsortCharac, ffportCharac = [], ['BETA'], ['ME', 'BETA']
ff_A = ff.FamaFrench(pickled_dir, runQuery, ffFreq, ffsortCharac, ffFactors, ffportCharac, runEstimation)

# - 3 portfolios (3x1) sorted on ['BETA']
sortingDim = [3]
ff_A.getFamaFrenchStats('Returns',  ffFreq, startDate, endDate, sortingDim, 'vw')
ff_A.getFamaFrenchStats('NumFirms', ffFreq, startDate, endDate, sortingDim)
ff_A.getFamaFrenchStats('Characs',  ffFreq, startDate, endDate, sortingDim)

# - 5 portfolios (5x1) sorted on ['BETA']
sortingDim = [5]
_, _, _, = ff_A.comparePortfolios('Returns',  ffFreq, startDate, endDate, sortingDim, 'vw')
_, _, _, = ff_A.comparePortfolios('Characs',  ffFreq, startDate, endDate, sortingDim)
ff_A.getFamaFrenchStats('Returns',  ffFreq, startDate, endDate, sortingDim, 'vw')
ff_A.getFamaFrenchStats('NumFirms', ffFreq, startDate, endDate, sortingDim)
ff_A.getFamaFrenchStats('Characs',  ffFreq, startDate, endDate, sortingDim)

# - 10 portfolios (10x1) sorted on ['BETA']
sortingDim = [10]
_, _, _, = ff_A.comparePortfolios('Returns',  ffFreq, startDate, endDate, sortingDim, 'vw')
_, _, _, = ff_A.comparePortfolios('Characs',  ffFreq, startDate, endDate, sortingDim)
ff_A.getFamaFrenchStats('Returns',  ffFreq, startDate, endDate, sortingDim, 'vw')
ff_A.getFamaFrenchStats('NumFirms', ffFreq, startDate, endDate, sortingDim)
ff_A.getFamaFrenchStats('Characs',  ffFreq, startDate, endDate, sortingDim)


#%%
#*******************************************************************************#
#*******************************************************************************#
#*************            Size (ME) x Market Beta (BETA)            ************#
#*******************************************************************************#
#*******************************************************************************#

#**********************************************************************************************#
# Daily Portfolios Formed on Size (ME) x Market Beta (BETA)
#**********************************************************************************************#
runQuery, runEstimation = False, True
ffFreq = 'D'
ffFactors, ffsortCharac, ffportCharac = [], ['ME', 'BETA'], ['ME', 'BETA']
ff_D = ff.FamaFrench(pickled_dir, runQuery, ffFreq, ffsortCharac, ffFactors, ffportCharac, runEstimation)

# - 6 portfolios (2x3) sorted on ['ME, 'BETA']
sortingDim = [2, 3]
ff_D.getFamaFrenchStats('Returns',  ffFreq, startDate, endDate, sortingDim, 'vw')
ff_D.getFamaFrenchStats('NumFirms', ffFreq, startDate, endDate, sortingDim)
ff_D.getFamaFrenchStats('Characs',  ffFreq, startDate, endDate, sortingDim)

# - 25 portfolios (5x5) sorted on ['ME, 'BETA']
sortingDim = [5, 5]
ff_D.getFamaFrenchStats('Returns',  ffFreq, startDate, endDate, sortingDim, 'vw')
ff_D.getFamaFrenchStats('NumFirms', ffFreq, startDate, endDate, sortingDim)
ff_D.getFamaFrenchStats('Characs',  ffFreq, startDate, endDate, sortingDim)

# - 100 portfolios (10x10) sorted on ['ME, 'BETA']
sortingDim = [10, 10]
ff_D.getFamaFrenchStats('Returns',  ffFreq, startDate, endDate, sortingDim, 'vw')
ff_D.getFamaFrenchStats('NumFirms', ffFreq, startDate, endDate, sortingDim)
ff_D.getFamaFrenchStats('Characs',  ffFreq, startDate, endDate, sortingDim)


#%%
#**********************************************************************************************#
# Monthly Portfolios Formed on Size (ME) x Market Beta (BETA)
#**********************************************************************************************#
runQuery, runEstimation = False, True
ffFreq = 'M'
ffFactors, ffsortCharac, ffportCharac = [], ['ME', 'BETA'], ['ME', 'BETA']
ff_M = ff.FamaFrench(pickled_dir, runQuery, ffFreq, ffsortCharac, ffFactors, ffportCharac, runEstimation)

# - 6 portfolios (2x3) sorted on ['ME, 'BETA']
sortingDim = [2, 3]
ff_M.getFamaFrenchStats('Returns',  ffFreq, startDate, endDate, sortingDim, 'vw')
ff_M.getFamaFrenchStats('NumFirms', ffFreq, startDate, endDate, sortingDim)
ff_M.getFamaFrenchStats('Characs',  ffFreq, startDate, endDate, sortingDim)

# - 25 portfolios (5x15 sorted on ['ME, 'BETA']
sortingDim = [5, 5]
_, _, _, = ff_M.comparePortfolios('Returns',  ffFreq, startDate, endDate, sortingDim, 'vw')
_, _, _, = ff_M.comparePortfolios('NumFirms', ffFreq, startDate, endDate, sortingDim)
_, _, _, = ff_M.comparePortfolios('Characs',  ffFreq, startDate, endDate, sortingDim)
ff_M.getFamaFrenchStats('Returns',  ffFreq, startDate, endDate, sortingDim, 'vw')
ff_M.getFamaFrenchStats('NumFirms', ffFreq, startDate, endDate, sortingDim)
ff_M.getFamaFrenchStats('Characs',  ffFreq, startDate, endDate, sortingDim)

# - 100 portfolios (10x10) sorted on ['ME, 'BETA']
sortingDim = [10, 10]
ff_M.getFamaFrenchStats('Returns',  ffFreq, startDate, endDate, sortingDim, 'vw')
ff_M.getFamaFrenchStats('NumFirms', ffFreq, startDate, endDate, sortingDim)
ff_M.getFamaFrenchStats('Characs',  ffFreq, startDate, endDate, sortingDim)


#%%
#**********************************************************************************************#
# Annual Portfolios Formed on Size (ME) x Market Beta (BETA)
#**********************************************************************************************#
runQuery, runEstimation = False, True
ffFreq = 'A'
ffFactors, ffsortCharac, ffportCharac = [], ['ME', 'BETA'], ['ME', 'BETA']
ff_A = ff.FamaFrench(pickled_dir, runQuery, ffFreq, ffsortCharac, ffFactors, ffportCharac, runEstimation)

# - 6 portfolios (2x3) sorted on ['ME, 'BETA']
sortingDim = [2, 3]
ff_A.getFamaFrenchStats('Returns',  ffFreq, startDate, endDate, sortingDim, 'vw')
ff_A.getFamaFrenchStats('NumFirms', ffFreq, startDate, endDate, sortingDim)
ff_A.getFamaFrenchStats('Characs',  ffFreq, startDate, endDate, sortingDim)

# - 25 portfolios (5x15 sorted on ['ME, 'BETA']
sortingDim = [5, 5]
_, _, _, = ff_A.comparePortfolios('Returns',  ffFreq, startDate, endDate, sortingDim, 'vw')
_, _, _, = ff_A.comparePortfolios('Characs',  ffFreq, startDate, endDate, sortingDim)
ff_A.getFamaFrenchStats('Returns',  ffFreq, startDate, endDate, sortingDim, 'vw')
ff_A.getFamaFrenchStats('NumFirms', ffFreq, startDate, endDate, sortingDim)
ff_A.getFamaFrenchStats('Characs',  ffFreq, startDate, endDate, sortingDim)

# - 100 portfolios (10x10) sorted on ['ME, 'BETA']
sortingDim = [10, 10]
ff_A.getFamaFrenchStats('Returns',  ffFreq, startDate, endDate, sortingDim, 'vw')
ff_A.getFamaFrenchStats('NumFirms', ffFreq, startDate, endDate, sortingDim)
ff_A.getFamaFrenchStats('Characs',  ffFreq, startDate, endDate, sortingDim)
