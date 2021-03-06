from main import Gesture
from data import DataManager

app_id = 1
app = Gesture(app_id)

manager = DataManager()

app.train(manager.folders,manager.names,manager.labels)	
#print len(app.features[0])
app.initClassifier()
test = app.getDataFromFile("triangle2.txt")
print manager.folders[app.predict(test)-1]
#print app.predict(test)
app.plotImage("triangle2.txt")
