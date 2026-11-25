from sensor_simulator import data_gen

class monitor():

    def __init__(self):
        tdata = data_gen.genTemp()
        vdata = data_gen.genVolt()
        fdata = data_gen.genFanSpd()


    def tFault(self,tdata):
        totT_faults = 0
        for n in tdata:
            if n > 80:
                totT_faults += 1
        return totT_faults

    def vFault(self, vdata):
            totV_faults = 0
            for n in vdata:
                if n > 0.8:
                    totV_faults += 1
            return totV_faults

    def fFault(self, fdata):
            totF_faults = 0
            for n in fdata:
                if n > 650:
                    totF_faults += 1
            return totF_faults
    
    def count(self, tdata):
        tot = 0
        for n in tdata:
            tot += 1
        return tot

    def totErrors(self, tdata, fdata, vdata):
        fault_indexes = set()
        for index, value in enumerate(tdata):
            if value > 80:
                fault_indexes.add(index)
        for index, value in enumerate(vdata):
            if value > 0.8:
                fault_indexes.add(index)
        for index, value in enumerate(fdata):
            if value > 650:
                fault_indexes.add(index)
        totError = len(fault_indexes)
        return totError

    def sysAtRisk(self, tot, totErrors):
        if (totErrors / tot) > 0.9:
            return True
        else:
            return False

    def findings(self, tot, totError, sysRisk, t, v, f):
        yield("===== SYSTEM REPORT =====")
        yield(f"Total readings processed: {tot}")
        yield(f"Total faults detected: {totError}")
        yield(f"Is the System at risk: {sysRisk}")
        yield(f"Total number of Temperature based dangers: {t}")
        yield(f"Total number of CPU Voltage based dangers: {v}")
        yield(f"Total number of Fan Speed based dangers: {f}")
        yield("=========================")

    def run(self):
        t = self.tFault(self.tdata)
        v = self.vFault(self.vdata)
        f = self.fFault(self.fdata)
        tot = self.count(self.tdata)
        totErrors = self.totErrors(self.tdata,self.vdata,self.fdata)
        sysRisk = self.sysAtRisk(self, tot, totErrors)
        return self.findings(tot, totErrors, sysRisk, t, v, f)

class main():

    def __init__(self):
        self.monitor = monitor()

    def run(self):
        results = self.monitor.run()
        for results in results:
            print(results)

if __name__ == "__main__":
    application = main()
    application.run()