import json
from dotmap import DotMap

with open("gw/bootstrap.ign","r") as ignFile:
    bootstrap_ignition = json.load(ignFile)
with open("gw/master.ign","r") as ignFile:
    master_ignition = json.load(ignFile)
with open("gw/worker.ign","r") as ignFile:
    worker_ignition = json.load(ignFile)
with open("azuredeploy.parameters.json", "r") as jsonFile:
    data = DotMap(json.load(jsonFile))

data.parameters.BootstrapIgnition.value =  "\'" + json.dumps(bootstrap_ignition) + "\'"
data.parameters.MasterIgnition.value =  "\'" + json.dumps(master_ignition) + "\'"
data.parameters.WorkerIgnition.value =  "\'" + json.dumps(worker_ignition) + "\'"

with open("runit.parameters.json", "w") as jsonFile:
    json.dump(data, jsonFile)
