import sys

class OptParser:

    def __init__(self, config):
        self._args = {}
        self._abbrevToFullName = {}
        for argConfig in config:
            self._args[argConfig._fullName] = (argConfig._argType, argConfig._defaultValue)
            self._abbrevToFullName[argConfig._abbrev] = argConfig._fullName

    def parse(self, sysArgs):
        parsed = {}
        for sysArg in sysArgs:
            if sysArg.startswith("--"):
                if sysArg.find("=") >= 0:
                    name, value = sysArg[2:].split("=")
                    argType, _ = self._args[name]
                    value = self.parseValue(value, argType) 
                    parsed[name] = value
                else:
                    parsed[sysArg[2:]] = ""
            elif sysArg.startswith("-"):
                if sysArg.find("=") >= 0:
                    abbrev, value = sysArg[1:].split("=")
                    name = self._abbrevToFullName[abbrev]
                    argType, _ = self._args[name]
                    value = self.parseValue(value, argType) 
                    parsed[name] = value
                else:
                    first = sysArg[1]
                    firstName = self._abbrevToFullName[first]
                    argType, _ = self._args[firstName]
                    if argType is not None:
                        parsed[firstName] = argType(sysArg[2:])
                    else:
                        for c in sysArg[1:]:
                            name = self._abbrevToFullName[c]
                            parsed[name] = ""
        self.fillDefaults(parsed)
        return parsed

    def parseValue(self, value, argType):
        return argType(value) if argType is not None else value 

    def fillDefaults(self, parsed):
        for name in self._args:
            _, defaultValue = self._args[name]
            if name not in parsed and defaultValue is not None:
                parsed[name] = defaultValue

class OptConfig:

    def __init__(self, fullName, abbrev, argType=None, defaultValue=None):
        self._fullName = fullName
        self._abbrev = abbrev
        self._argType = argType
        self._defaultValue = defaultValue

if __name__ == "__main__":
    parser = OptParser([OptConfig("version", "v"), OptConfig("fallow", "f"), OptConfig("iterations", "i", int, 1), OptConfig("context", "C", int, 0)])
    parsedOptions = parser.parse(sys.argv[1:])
    print(parsedOptions)

