"""
  Function:  mpdct
  --------------------
  Populate the primer classes with active compounds. Exempt compounds occuring in conflicting cases.

  Author:
  Felix Kruger
  momo.sander@googlemail.com
"""                              
def mpdct(confTargets, threshold, release, user, pword, host, port): 
  mpdct = {}
  for primer in primers.keys():
    for target in primers[primer]['targets']:
      
      if target in confTargets:
        continue
        
      ligands = getLigands.getLigandsForTarget(target, release, user, pword, host, port)
      ligands = filterForTarget.filterForTarget(ligands, threshold)
        aff = ligand[1]
        molregno = ligand[2]
        actId = ligand[3]
        try:
          mpdct[primer][molregno]['pAfnty'].append(aff)
          mpdct[primer][molregno]['target'].append(target)
	      mpdct[primer][molregno]['actId'].append(actId)
          mpdct[primer][molregno]['smiles']=smiles
        except KeyError:        
          try:
            mpdct[primer][molregno] = {}
            mpdct[primer][molregno]['pAfnty']=[]
            mpdct[primer][molregno]['target']=[]
	        mpdct[primer][molregno]['actId'] = []
            mpdct[primer][molregno]['smiles']=smiles
            mpdct[primer][molregno]['pAfnty'].append(aff)
            mpdct[primer][molregno]['target'].append(target)
            mpdct[primer][molregno]['actId'].append(actId)
          except KeyError:
            mpdct[primer]={}
            mpdct[primer][molregno] = {}
            mpdct[primer][molregno]['pAfnty']=[]
            mpdct[primer][molregno]['target']=[]
            mpdct[primer][molregno]['actId'] = []
            mpdct[primer][molregno]['smiles']=smiles
            mpdct[primer][molregno]['pAfnty'].append(aff)
            mpdct[primer][molregno]['target'].append(target)
            mpdct[primer][molregno]['actId'].append(actId)
      
  outfile = open('data/mpdct_pKi%s_%s.pkl' %(int(threshold), release),'w')
  pickle.dump(mpdct, outfile)
  outfile.close()  
               
  return mpdct    


