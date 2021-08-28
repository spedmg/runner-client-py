from attr import attrs, attrib

@attrs(kw_only=True)
class Title:
    alpha                 = attrib(default=None)
    eidr                  = attrib(default=None)
    full_name             = attrib(default=None)
    gmdm_id               = attrib(default=None)
    gpms_id               = attrib(default=None)
    gpms_id_and_name      = attrib(default=None)
    id                    = attrib(default=None)
    name                  = attrib(default=None)
    season_number         = attrib(default=None)
    season_number_integer = attrib(default=None)
    season_number_prefix  = attrib(default=None)
    season_number_suffix  = attrib(default=None)
    title_level           = attrib(default=None)
    title_type            = attrib(default=None)
    walker_id             = attrib(default=None)
