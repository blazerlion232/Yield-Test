from sensor_simulator import data_gen

class monitor():
    tdata = data_gen.genTemp()
    vdata = data_gen.genVolt()
    fdata = data_gen.genFspd()


    def tFault(tdata):
        totT_faults = 0
        for n in tdata:
            if tdata[n] > 80:
                totT_faults += 1
        return totT_faults

    def vFault(vdata):
            totV_faults = 0
            for n in vdata:
                if vdata[n] > 0.8:
                    totV_faults += 1
            return totV_faults

    def fFault(fdata):
            totF_faults = 0
            for n in fdata:
                if fdata[n] > 80:
                    totF_faults += 1
            return totF_faults
    
    def count(tdata):
        tot = 0
        for n in tdata:
             tot += 1
        return tot

    def sysAtRisk(t, v, f, tot):
        totalErrors = t + v + f
        if (totalErrors / tot) > 0.9:
             return True
        else:
             return False

    def totErrors(t, v, f):
        totError = t + v + f
        return totError

    def findings(tot, totError, sysRisk, t, v, f):
        yield("===== SYSTEM REPORT =====")
        yield("Total readings processed" + tot)
        yield("Total faults detected" + totError)
        yield("Is the System at risk: " + sysRisk)
        yield("Total number of Temperature based dangers: " + t)
        yield("Total number of CPU Voltage based dangers: " + v)
        yield("Total number of Fan Speed based dangers: " + f)
        yield("=========================")

    def run(self):
        t = self.tFault(self.tdata)
        v = self.vFault(self.vdata)
        f = self.fFault(self.fdata)
        tot = self.count(self.tdata)
        sysRisk = self.sysAtRisk(t, v, f, tot)
        Error = self.totErrors(t,v,f)
        return self.findings(tot, Error, sysRisk, t, v, f)

class main():
     monitor.run()