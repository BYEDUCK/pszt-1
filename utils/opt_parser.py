import sys


class OptParser:

    def __init__(self, config):
        self._args = {}
        self._abbrevToFullName = {}
        for arg_config in config:
            self._args[arg_config._fullName] = (arg_config._argType, arg_config._defaultValue)
            self._abbrevToFullName[arg_config._abbrev] = arg_config._fullName

    def parse(self, sys_args):
        parsed = {}
        for sysArg in sys_args:
            if sysArg.startswith("--"):
                # parse long name with value after '='
                if sysArg.find("=") >= 0:
                    name, value = sysArg[2:].split("=")
                    arg_type, _ = self._args[name]
                    value = self._parse_value(value, arg_type)
                    parsed[name] = value
                # parse long name without value
                else:
                    parsed[sysArg[2:]] = ""
            elif sysArg.startswith("-"):
                # parse short name with value after '='
                if sysArg.find("=") >= 0:
                    abbrev, value = sysArg[1:].split("=")
                    name = self._abbrevToFullName[abbrev]
                    arg_type, _ = self._args[name]
                    value = self._parse_value(value, arg_type)
                    parsed[name] = value
                else:
                    first = sysArg[1]
                    first_name = self._abbrevToFullName[first]
                    arg_type, _ = self._args[first_name]
                    # parse short name with value without '='
                    if arg_type is not None:
                        parsed[first_name] = arg_type(sysArg[2:])
                    # parse short names without values
                    else:
                        for c in sysArg[1:]:
                            name = self._abbrevToFullName[c]
                            parsed[name] = ""
        self._fill_defaults(parsed)
        return parsed

    @staticmethod
    def _parse_value(value, arg_type):
        return arg_type(value) if arg_type is not None else value

    def _fill_defaults(self, parsed):
        for name in self._args:
            _, default_value = self._args[name]
            if name not in parsed and default_value is not None:
                parsed[name] = default_value


class OptConfig:

    def __init__(self, full_name, abbrev, arg_type=None, default_value=None):
        self._fullName = full_name
        self._abbrev = abbrev
        self._argType = arg_type
        self._defaultValue = default_value


if __name__ == "__main__":
    parser = OptParser([OptConfig("version", "v"), OptConfig("fallow", "f"), OptConfig("iterations", "i", int, 1),
                        OptConfig("context", "C", int, 0)])
    parsedOptions = parser.parse(sys.argv[1:])
    print(parsedOptions)
