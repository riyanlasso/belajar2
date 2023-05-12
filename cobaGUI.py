import numpy as np
import pyqtgraph.opengl as gl
import btk

# load file c3d
reader = btk.btkAcquisitionFileReader()
reader.SetFilename("path/to/c3d/file")
reader.Update()
acq = reader.GetOutput()

# extract coordinate data from the file
n_frames = acq.GetPointFrameNumber() # number of frames in the file
point_names = acq.GetPoints().GetItemNames() # names of the markers in the file
data = np.zeros((n_frames, len(point_names), 3)) # array to store coordinate data
for i, name in enumerate(point_names):
    point_data = acq.GetPoint(name).GetValues()
    data[:, i, :] = point_data[:, :3]

# create a 3D visualization
app = gl.QtGui.QApplication([])
w = gl.GLViewWidget()
w.opts['distance'] = 500
w.show()

# create a line plot for each marker
for i, name in enumerate(point_names):
    color = (i/len(point_names), 1-i/len(point_names), 0, 1)
    pos = data[:, i, :]
    line = gl.GLLinePlotItem(pos=pos, color=color, width=2, antialias=True)
    w.addItem(line)

# run the application
gl.QtGui.QApplication.instance().exec_()
