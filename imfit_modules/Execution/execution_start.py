from execution_main import ExecutionModule

class StartExecution(ExecutionModule):
    
    def startExecutionBtn(self):
        
        #This button runs the execution plan on Dockers
        
        pass

    def createDocker(self):
        
        #This function creates Dockers for execution
        
        pass
    
    def executeOS(self):
        
        #The function executes OS for Docker
        
        pass

    def executePython(self):
        
        #The function executes Python for Docker
        
        pass
    
    def executeROS(self):
        
        #The function executes ROS for Docker
        
        pass
    
    def executeGazebo(self):
        
        #The function executes Gazebo for Docker
        
        pass

class TakeDatas(StartExecution):
    
    #These functions take the datas from Dockers for analyzing and monitoring
    
    def takeDockerData(self):        
        pass

    def takeOSData(self):
        pass

    def takeOSData(self):
        pass

    def takePythonData(self):
        pass
    
    def takeROSData(self):
        pass
    
    def takeGazeboData(self):
        pass

class LogFileData(StartExecution):
    
    #These functions create and take "Log Files"
    
    def createLogFiles(self):
        pass

    def takeLogFileData(self):
        pass

class RosbagFileData(StartExecution):
    
    #These functions create and take ".rosbag" for monitoring
    
    def createRosbagFile(self):
        pass

    def takeRosbagFileData(self):
        pass

class TerminateDockers(TakeDatas):
    
    def terminateDockers(self):
        
        #This function terminates the dockers for every execute
        
        pass

    def checkTerminate(self):
        
        #This function checks the terminate situation
        
        pass
