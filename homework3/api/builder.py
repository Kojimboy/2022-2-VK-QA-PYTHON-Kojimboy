import uuid
from dataclasses import dataclass


class Builder:
    @staticmethod
    def campaign(campaign_name=None, banner_name=None):
        @dataclass
        class Campaign:
            campaign_name: str
            banner_name: str
            id: None = None

        if campaign_name is None:
            campaign_name = str(uuid.uuid1())

        if banner_name is None:
            banner_name = str(uuid.uuid1())

        return Campaign(campaign_name=campaign_name, banner_name=banner_name)

    @staticmethod
    def segment(segment_name=None, object_type=None):
        @dataclass
        class Segment:
            segment_name: str
            object_type: str
            id: None = None

        if segment_name is None:
            segment_name = str(uuid.uuid1())

        return Segment(segment_name=segment_name, object_type=object_type)

    @staticmethod
    def source_group(url=None):
        @dataclass
        class Source:
            url: str
            vk_id: None = None
            object_id: None = None

        return Source(url=url)
