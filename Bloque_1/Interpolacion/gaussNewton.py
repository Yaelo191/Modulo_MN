import numpy as np

def relErrorTot(xolds, xnews):
  errs = np.abs((xnews - xolds)/xnews)
  return np.sum(errs)

def model(cs, xi):
  p = cs[0]* np.cos(cs[1]*xi + cs[2])
  return p

def getKrs(data, cs):
  """
  rho = p(xj)/sigma_j, b = yj/sigma_j
  """
  K = np.zeros((data.shape[1], cs.size))
  
  K[:,0] = np.cos(cs[1]*data[1,:] + cs[2])/data[2,:]
  K[:,1] = -cs[0]*data[1,:]*np.sin(cs[1]*data[1,:] + cs[2])/data[2,:]
  K[:,2] = -cs[0]*np.sin(cs[1]*data[1,:] + cs[2])/data[2,:]
  
  rs = (data[1,:] - model(cs, data[0,:]))/data[2,:]
  return K, rs
    
def gaussnewton(data, ckm1, kmax=50, tol=1.e-8):
  for _ in range(kmax):
    K, rs = getKrs(data, ckm1)
    matK = K.T@K
    invmatK = np.linalg.inv(matK)
    ck = ckm1 + invmatK@K.T@rs
    err = relErrorTot(ckm1, ck)
    if err < tol:
      break
    ckm1 = np.copy(ck)
    
  return ckm1
    