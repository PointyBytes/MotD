import attrs


@attr.s
class MOTD:
    url: str = attr.ib()
