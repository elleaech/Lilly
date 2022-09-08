import string

class ITargetData:
    hostname: string

def _print_target_data(target_data: ITargetData) -> ITargetData:
    return target_data.hostname
