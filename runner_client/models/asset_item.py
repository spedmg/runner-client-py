from . import Title

class AssetItem:
    # attrs:
    # actions
    # archive_status
    # archived
    # asset_class
    # asset_owner
    # asset_subtype
    # asset_type
    # asset_type_or_class
    # checksum
    # created_at
    # custom_metadata
    # downloadable
    # file_name
    # folder_ids
    # has_custom_thumbnail
    # has_proxy
    # has_playable_proxy
    # height
    # icon_status
    # id
    # is_audio
    # is_video
    # linked_asset_group_ids
    # managed_by
    # mcs_id
    # name
    # pixel_dimensions
    # ppi
    # proxies
    # proxy_file_size
    # qc_reports
    # rejected
    # restorable
    # restore_minutes_remaining
    # restore_status
    # restored
    # restoring
    # root_title
    # scene
    # scheduled_actions
    # season
    # series
    # shareable
    # size
    # status
    # thumbnail_url
    # thumbnail_mcs_id
    # titles
    # uploaded_at
    # uploaded_by
    # uploaded_by_email
    # usage_classification
    # usage_restriction
    # usage_status
    # width
    # updated_at
    def __init__(self, asset_data):
        self.__asset_data = asset_data
        self.__titles = list(map(lambda d: Title(**d), asset_data['titles']))

    @property
    def asset_subtype(self):
        return self.__asset_data['asset_subtype']

    @property
    def asset_type(self):
        return self.__asset_data['asset_type']

    @property
    def id(self):
        return self.__asset_data['id']

    @property
    def name(self):
        return self.__asset_data['name']

    @property
    def titles(self):
        return self.__titles
